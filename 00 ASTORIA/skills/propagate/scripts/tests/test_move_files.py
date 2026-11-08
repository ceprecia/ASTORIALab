"""Synthetic move/reference/rollback checks. No personal vault content is used."""
import errno
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import unicodedata
from unittest import mock

SPEC = importlib.util.spec_from_file_location("astoria_move_files_test", Path(__file__).parents[1] / "move_files.py")
MOVE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOVE
SPEC.loader.exec_module(MOVE)


class MoveFilesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.vault = self.root / "vault"
        self.vault.mkdir()

    def tearDown(self):
        self.temporary.cleanup()

    def put(self, name, content):
        path = self.vault / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)
        return path

    def run_moves(self, rows, apply=True, **options):
        return MOVE.execute(self.vault, rows, apply=apply,
                            backup_dir=self.root / "recovery", **options)

    def test_dry_run_has_no_writes(self):
        self.put("Incoming/paper.pdf", b"original\x00bytes")
        self.put("Projects/MOC.md", "# Project\nRead [[Incoming/paper.pdf|Paper]].\n")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}], apply=False)
        self.assertEqual(result["status"], "dry_run", result)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertFalse((self.root / "recovery").exists())

    def test_moved_note_outbound_relative_link_and_title_query_fragment(self):
        self.put("Incoming/note.md", '[Reference](../Knowledge/a%20paper.pdf?download=1#page=2 "Keep this title")\n')
        self.put("Knowledge/a paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/note.md", "destination": "Library/topic/note.md"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Library/topic/note.md").read_text(),
                         '[Reference](../../Knowledge/a%20paper.pdf?download=1#page=2 "Keep this title")\n')

    def test_root_note_rebases_unmoved_root_asset(self):
        self.put("note.md", '[Asset](asset.png)\n<img src="asset.png">\n')
        self.put("asset.png", b"root asset")
        result = self.run_moves([{"source": "note.md", "destination": "Library/topic/note.md"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Library/topic/note.md").read_text(),
                         '[Asset](../../asset.png)\n<img src="../../asset.png">\n')

    def test_unicode_source_spelling_and_outgoing_reference_are_consistent(self):
        decomposed = unicodedata.normalize("NFD", "café.md")
        self.put("Incoming/" + decomposed, "[Asset](../asset.png)\n")
        self.put("asset.png", b"asset")
        result = self.run_moves([{"source": "Incoming/café.md", "destination": "Library/topic/café.md"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Library/topic/café.md").read_text(), "[Asset](../../asset.png)\n")

    def test_wiki_alias_anchor_embed_and_visible_rename_label(self):
        self.put("Incoming/old.md", "# Heading\noriginal\n")
        original = '![[Incoming/old#Heading|Visible label]]\n[[old]]\n'
        self.put("MOC.md", original)
        result = self.run_moves([{"source": "Incoming/old.md", "destination": "Library/new.md"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "MOC.md").read_text(),
                         '![[Library/new#Heading|Visible label]]\n[[Library/new|old]]\n')

    def test_markdown_file_uri_absolute_html_reference_style_and_canvas(self):
        old = self.put("Incoming/a paper.pdf", b"paper\x00")
        self.put("MOC.md", '[Absolute](<' + str(old) + '> "absolute title")\n'
                 '[URI](' + old.as_uri() + '?q=yes#page=1)\n'
                 '[Reference][paper]\n[paper]: <Incoming/a paper.pdf> "reference title"\n'
                 '<a href="Incoming/a%20paper.pdf?q=1&amp;x=2#p">HTML label</a>\n')
        canvas = '{ "nodes": [{ "type": "file", "file": "Incoming/a paper.pdf", "text": "Leave this prose" }] }\n'
        self.put("board.canvas", canvas)
        result = self.run_moves([{"source": "Incoming/a paper.pdf", "destination": "Library/a paper.pdf"}])
        self.assertEqual(result["status"], "applied", result)
        text = (self.vault / "MOC.md").read_text()
        self.assertIn('<' + str(self.vault / "Library/a%20paper.pdf") + '> "absolute title"', text)
        self.assertIn((self.vault / "Library/a paper.pdf").as_uri() + '?q=yes#page=1', text)
        self.assertIn('[paper]: <Library/a%20paper.pdf> "reference title"', text)
        self.assertIn('href="Library/a%20paper.pdf?q=1&amp;x=2#p"', text)
        self.assertEqual((self.vault / "board.canvas").read_text(),
                         canvas.replace('"Incoming/a paper.pdf"', '"Library/a paper.pdf"'))

    def test_parentheses_and_spaces_in_markdown_destination(self):
        self.put("Incoming/a paper (final).pdf", b"paper")
        self.put("MOC.md", '[Keep label](Incoming/a paper (final).pdf "Keep title")\n')
        result = self.run_moves([{"source": "Incoming/a paper (final).pdf", "destination": "Library/a paper (final).pdf"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "MOC.md").read_text(),
                         '[Keep label](Library/a%20paper%20%28final%29.pdf "Keep title")\n')

    def test_markdown_quoted_title_can_contain_closing_parenthesis(self):
        self.put("Incoming/paper.pdf", b"paper")
        self.put("MOC.md", '[Label](Incoming/paper.pdf "Keep ) exactly")\n')
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "MOC.md").read_text(), '[Label](Library/paper.pdf "Keep ) exactly")\n')

    def test_moc_prose_headings_decisions_and_log_narrative_preserved(self):
        self.put("Incoming/paper.pdf", b"paper")
        original = ('# Project MOC\n\nA decision in my own words.\r\n'
                    'The historical path was Incoming/paper.pdf.\n'
                    'Historical inline path: `Incoming/paper.pdf`.\n'
                    '```text\nQuoted provenance: [[Incoming/paper.pdf|Example]]\n```\n'
                    '## Research Log\n\n### 2020-01-01\n'
                    'We recorded an observation; preserve every word.\n'
                    'Read [[Incoming/paper.pdf#page=2|Original displayed label]].\n')
        path = self.put("Projects/MOC Subject.md", original)
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}])
        self.assertEqual(result["status"], "applied", result)
        expected = original.replace('[[Incoming/paper.pdf#page=2|Original displayed label]]',
                                    '[[Library/paper.pdf#page=2|Original displayed label]]')
        self.assertEqual(path.read_bytes(), expected.encode("utf-8"))

    def test_complete_package_and_directory_links(self):
        self.put("Incoming/package/readme.md", '[Internal](assets/figure.svg)\n[External](../common.md)\n')
        self.put("Incoming/package/assets/figure.svg", '<svg><image href="../icons/source.png"/></svg>')
        self.put("Incoming/package/icons/source.png", b"image\x00bytes")
        self.put("Incoming/package/.metadata", b"preserve metadata file")
        (self.vault / "Incoming/package/empty").mkdir()
        self.put("Incoming/common.md", "shared\n")
        self.put("MOC.md", '[Package](Incoming/package)\n[Subfolder](Incoming/package/assets)\n')
        result = self.run_moves([{"source": "Incoming/package", "destination": "Research/devices/package"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertFalse((self.vault / "Incoming/package").exists())
        self.assertTrue((self.vault / "Research/devices/package/empty").is_dir())
        self.assertEqual((self.vault / "Research/devices/package/.metadata").read_bytes(), b"preserve metadata file")
        self.assertEqual((self.vault / "Research/devices/package/readme.md").read_text(),
                         '[Internal](assets/figure.svg)\n[External](../../../Incoming/common.md)\n')
        self.assertEqual((self.vault / "MOC.md").read_text(),
                         '[Package](Research/devices/package)\n[Subfolder](Research/devices/package/assets)\n')

    def test_reviewed_agent_paths_include_inline_and_fenced_commands_not_history(self):
        old, new = "Incoming/paper.pdf", "Library/paper.pdf"
        self.put(old, b"paper")
        original = ('# Instructions\nUnicode: café.\nRead `' + old + '` first.\n'
                    'Run:\n```sh\nopen ' + old + '\n```\n'
                    'Historical source: `' + old + '`.\n')
        path = self.put("AGENTS.md", original)
        starts = [original.index(old), original.index(old, original.index(old) + 1)]
        edits = [{"file": "AGENTS.md", "start": start, "old": old, "new": new, "base": "vault"}
                 for start in starts]
        result = self.run_moves([{"source": old, "destination": new}], path_edits=edits)
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual(result["reviewed_path_edits"], 2)
        self.assertEqual(path.read_text(), original.replace(old, new, 2))
        self.assertTrue(any(item["code"] == "context_sensitive_path_reference" for item in result["warnings"]))
        self.assertEqual((self.root / "recovery/originals/AGENTS.md").read_text(), original)

    def test_reviewed_moc_script_and_config_paths_move_as_one_transaction(self):
        old, new = "Incoming/paper.pdf", "Library/paper.pdf"
        self.put(old, b"paper")
        contents = {"Projects/MOC.md": "# Study\nCurrent input: `" + old + "`.\nKeep this decision.\n",
                    "scripts/read.py": 'input_path = "' + old + '"\n',
                    "config.yaml": 'input_path: "' + old + '"\n'}
        edits = []
        for name, content in contents.items():
            self.put(name, content)
            edits.append({"file": name, "start": content.index(old), "old": old, "new": new, "base": "vault"})
        result = self.run_moves([{"source": old, "destination": new}], path_edits=edits)
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual(result["blocked"], [])
        for name, content in contents.items():
            self.assertEqual((self.vault / name).read_text(), content.replace(old, new))
        self.assertEqual((self.vault / new).read_bytes(), b"paper")

    def test_reviewed_document_path_rebases_when_document_moves(self):
        self.put("asset.png", b"asset")
        text = "Use `asset.png` for this figure.\n"
        self.put("note.md", text)
        edits = [{"file": "note.md", "start": text.index("asset.png"),
                  "old": "asset.png", "new": "../../asset.png"}]
        result = self.run_moves([{"source": "note.md", "destination": "Library/topic/note.md"}], path_edits=edits)
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Library/topic/note.md").read_text(),
                         "Use `../../asset.png` for this figure.\n")

    def test_reviewed_literal_path_preserves_percent_and_hash_filename_characters(self):
        old, new = "Incoming/a%20b#1.pdf", "Library/a%20b#1.pdf"
        self.put(old, b"literal filename")
        text = 'input_path = "' + old + '"\n'
        self.put("read.py", text)
        result = self.run_moves([{"source": old, "destination": new}], path_edits=[
            {"file": "read.py", "start": text.index(old), "old": old, "new": new, "base": "vault"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "read.py").read_text(), text.replace(old, new))

    def test_unreviewed_relative_code_path_with_literal_hash_or_percent_blocks(self):
        for filename in ["a#1.csv", "a%20b.csv"]:
            old, new = "Inputs/" + filename, "Library/" + filename
            self.put(old, "data\n")
            content = 'input_path = "' + filename + '"\n'
            self.put("Inputs/read.py", content)
            result = self.run_moves([{"source": old, "destination": new}], apply=False)
            self.assertEqual(result["status"], "blocked", (filename, result))
            self.assertTrue(any(item["code"] == "unsupported_path_reference" for item in result["blocked"]))
            self.assertEqual((self.vault / "Inputs/read.py").read_text(), content)
            self.assertTrue((self.vault / old).exists())

    def test_late_relative_code_path_with_literal_hash_or_percent_rolls_back(self):
        for number, filename in enumerate(["a#1.csv", "a%20b.csv"]):
            old, new = "Inputs/" + filename, "Library/" + filename
            self.put(old, "data\n")
            content = 'input_path = "../Inputs/' + filename + '"\n'
            def concurrent(stage, path=None):
                if stage == "after_move":
                    self.put("scripts/new.py", content)
            with mock.patch.object(MOVE, "checkpoint", concurrent):
                result = MOVE.execute(self.vault, [{"source": old, "destination": new}], apply=True,
                                      backup_dir=self.root / ("recovery_" + str(number)))
            self.assertEqual(result["status"], "rolled_back", (filename, result))
            self.assertTrue((self.vault / old).exists())
            self.assertEqual((self.vault / "scripts/new.py").read_text(), content)

    def test_reviewed_package_pointer_uses_complete_literal_not_prefix(self):
        self.put("Incoming/package/data/a.csv", "value\n1\n")
        old, new = "Incoming/package/data/a.csv", "Library/package/data/a.csv"
        text = 'input_path = "' + old + '"\n'
        self.put("read.py", text)
        result = self.run_moves([{"source": "Incoming/package", "destination": "Library/package"}], path_edits=[
            {"file": "read.py", "start": text.index(old), "old": old, "new": new, "base": "vault"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "read.py").read_text(), text.replace(old, new))

    def test_unselected_literal_in_script_comment_remains_a_reported_blocker(self):
        old, new = "Incoming/a.pdf", "Library/a.pdf"
        self.put(old, b"a")
        text = 'path = "' + old + '"\n# Historical source: ' + old + '\n'
        self.put("read.py", text)
        result = self.run_moves([{"source": old, "destination": new}], path_edits=[
            {"file": "read.py", "start": text.index(old), "old": old, "new": new, "base": "vault"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["code"] == "unsupported_path_reference" for item in result["blocked"]))
        self.assertEqual((self.vault / "read.py").read_text(), text)
        self.assertTrue((self.vault / old).exists())

    def test_reviewed_paths_reject_escaping_and_invalid_base(self):
        self.put("Incoming/a.pdf", b"a")
        text = 'input_path = "Incoming/a.pdf"\n'
        self.put("read.py", text)
        record = {"file": "read.py", "start": text.index("Incoming/a.pdf"),
                  "old": "Incoming/a.pdf", "new": 'Library/"quoted"/a.pdf', "base": "vault"}
        for edit in [record, dict(record, new="Library/a.pdf", base=[]),
                     dict(record, old="Incoming\\/a.pdf", new="Library/a.pdf")]:
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": 'Library/"quoted"/a.pdf'}],
                                    apply=False, path_edits=[edit])
            self.assertEqual(result["status"], "blocked", result)

    def test_reviewed_path_rejects_quote_insertion_inside_larger_command_string(self):
        old = "Incoming/a.csv"
        self.put(old, "a\n")
        content = 'command = "cat ' + old + '"\n'
        self.put("read.py", content)
        for new in ['Library/"quoted"/a.csv', "Library/'quoted'/a.csv", "Library/`quoted`/a.csv"]:
            result = self.run_moves([{"source": old, "destination": new}], apply=False,
                                    path_edits=[{"file": "read.py", "start": content.index(old),
                                                 "old": old, "new": new, "base": "vault"}])
            self.assertEqual(result["status"], "blocked", result)
            self.assertEqual((self.vault / "read.py").read_text(), content)
            self.assertTrue((self.vault / old).exists())

    def test_reviewed_path_rejects_arbitrary_text_target_offset_and_substring(self):
        self.put("Incoming/a.pdf", b"a")
        self.put("Other/b.pdf", b"b")
        content = 'Choice: `Incoming/a.pdf`; keep my decision.\n'
        self.put("MOC.md", content)
        good = {"file": "MOC.md", "start": content.index("Incoming/a.pdf"),
                "old": "Incoming/a.pdf", "new": "Library/a.pdf", "base": "vault"}
        for edit in [dict(good, new="Other/b.pdf"), dict(good, start=0),
                     dict(good, start=content.index("a.pdf"), old="a.pdf")]:
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}],
                                    apply=False, path_edits=[edit])
            self.assertEqual(result["status"], "blocked", result)
        self.assertEqual((self.vault / "MOC.md").read_text(), content)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_reviewed_path_rejects_filename_prefix_before_hash_or_question_suffix(self):
        self.put("Incoming/a.csv", "a\n")
        for suffix in ["#tag", "?tag", ".", ";tag", "&tag", " extra"]:
            self.put("Incoming/a.csv" + suffix, "other file\n")
            content = "path = 'Incoming/a.csv" + suffix + "'\n"
            self.put("read.py", content)
            result = self.run_moves([{"source": "Incoming/a.csv", "destination": "Library/a.csv"}],
                                    apply=False, path_edits=[{"file": "read.py", "start": content.index("Incoming/a.csv"),
                                                             "old": "Incoming/a.csv", "new": "Library/a.csv", "base": "vault"}])
            self.assertEqual(result["status"], "blocked", (suffix, result))
            self.assertTrue((self.vault / "Incoming/a.csv").exists())
            self.assertEqual((self.vault / "read.py").read_text(), content)

    def test_reviewed_path_overlap_system_and_hold_are_rejected(self):
        self.put("Incoming/a.pdf", b"a")
        content = "Read `Incoming/a.pdf`.\n"
        for name in ["MOC.md", "00 ASTORIA/instructions.md", "Held/AGENTS.md"]:
            self.put(name, content)
        record = {"file": "MOC.md", "start": content.index("Incoming/a.pdf"),
                  "old": "Incoming/a.pdf", "new": "Library/a.pdf", "base": "vault"}
        for edits, options in [([record, record], {}),
                               ([dict(record, file="00 ASTORIA/instructions.md")], {}),
                               ([dict(record, file="Held/AGENTS.md")], {"holds": ["Held"]})]:
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}],
                                    apply=False, path_edits=edits, **options)
            self.assertEqual(result["status"], "blocked", result)

    def test_reviewed_path_write_failure_rolls_back_dependency_and_move(self):
        old, new = "Incoming/a.pdf", "Library/a.pdf"
        self.put(old, b"a")
        content = 'Read `' + old + '`.\n'
        self.put("AGENTS.md", content)
        edits = [{"file": "AGENTS.md", "start": content.index(old), "old": old, "new": new, "base": "vault"}]
        def failure(stage, path=None):
            if stage == "after_write":
                raise OSError("simulated dependency write failure")
        with mock.patch.object(MOVE, "checkpoint", failure):
            result = self.run_moves([{"source": old, "destination": new}], path_edits=edits)
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "AGENTS.md").read_text(), content)
        self.assertTrue((self.vault / old).exists())
        self.assertFalse((self.vault / new).exists())

    def test_reviewed_path_concurrent_dependency_edit_is_retained_without_move(self):
        old, new = "Incoming/a.pdf", "Library/a.pdf"
        self.put(old, b"a")
        content = 'Read `' + old + '`.\n'
        self.put("AGENTS.md", content)
        edits = [{"file": "AGENTS.md", "start": content.index(old), "old": old, "new": new, "base": "vault"}]
        def concurrent(stage, path=None):
            if stage == "after_backup":
                self.put("AGENTS.md", "New owner decision.\n" + content)
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": old, "destination": new}], path_edits=edits)
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "AGENTS.md").read_text(), "New owner decision.\n" + content)
        self.assertTrue((self.vault / old).exists())

    def test_literal_dependency_added_during_apply_rolls_back(self):
        self.put("Incoming/a.pdf", b"a")
        def concurrent(stage, path=None):
            if stage == "after_move":
                self.put("scripts/new.py", 'path = "Incoming/a.pdf"\n')
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())
        self.assertEqual((self.vault / "scripts/new.py").read_text(), 'path = "Incoming/a.pdf"\n')

    def test_cli_reviewed_path_edit_file(self):
        self.put("Incoming/a.pdf", b"a")
        content = 'Read `Incoming/a.pdf`.\n'
        self.put("AGENTS.md", content)
        plan = self.root / "moves.json"
        plan.write_text(json.dumps([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}]))
        edits = self.root / "paths.json"
        edits.write_text(json.dumps([{"file": "AGENTS.md", "start": content.index("Incoming/a.pdf"),
                                      "old": "Incoming/a.pdf", "new": "Library/a.pdf", "base": "vault"}]))
        result = subprocess.run([sys.executable, "-S", str(Path(MOVE.__file__)), "--vault", str(self.vault),
                                 "--plan", str(plan), "--path-edits", str(edits), "--apply",
                                 "--backup-dir", str(self.root / "recovery")], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["reviewed_path_edits"], 1)
        self.assertEqual((self.vault / "AGENTS.md").read_text(), content.replace("Incoming", "Library"))

    def test_collision_and_duplicate_destination_refused(self):
        self.put("Incoming/a.pdf", b"a")
        self.put("Incoming/b.pdf", b"b")
        self.put("Library/existing.pdf", b"existing")
        for rows in [
            [{"source": "Incoming/a.pdf", "destination": "Library/existing.pdf"}],
            [{"source": "Incoming/a.pdf", "destination": "Library/new.pdf"},
             {"source": "Incoming/b.pdf", "destination": "Library/new.pdf"}],
        ]:
            result = self.run_moves(rows)
            self.assertEqual(result["status"], "blocked", result)
        self.assertEqual((self.vault / "Library/existing.pdf").read_bytes(), b"existing")
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_path_escape_root_overlap_and_hold_refused(self):
        self.put("Incoming/package/a.txt", "a")
        cases = [
            [{"source": ".", "destination": "elsewhere"}],
            [{"source": "../outside", "destination": "elsewhere"}],
            [{"source": "Incoming/package", "destination": "/outside"}],
            [{"source": "Incoming/package", "destination": "Incoming/package/nested"}],
            [{"source": "Incoming/package", "destination": "Library/package"},
             {"source": "Incoming/package/a.txt", "destination": "Library/a.txt"}],
        ]
        for rows in cases:
            self.assertEqual(self.run_moves(rows)["status"], "blocked")
        result = self.run_moves([{"source": "Incoming/package", "destination": "Library/package"}],
                                holds=["Incoming/package/a.txt"])
        self.assertEqual(result["status"], "blocked", result)

    def test_system_root_and_incoming_system_reference_excluded(self):
        self.put("00 ASTORIA/skills/example.md", "[[Incoming/paper.pdf]]\n")
        self.put("Incoming/paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["code"] == "system_handoff" for item in result["blocked"]))
        result = self.run_moves([{"source": "00 ASTORIA/skills/example.md", "destination": "Library/example.md"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertEqual((self.vault / "00 ASTORIA/skills/example.md").read_text(), "[[Incoming/paper.pdf]]\n")

    def test_app_private_root_is_not_a_move_source(self):
        self.put(".obsidian/app.json", "{}\n")
        result = self.run_moves([{"source": ".obsidian/app.json", "destination": "Library/app.json"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue((self.vault / ".obsidian/app.json").exists())

    def test_renamed_system_root_is_read_only(self):
        self.put("My AI/guide.md", "Use [[Incoming/paper.pdf]].\n")
        self.put("Incoming/paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}],
                                system_root="My AI")
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["code"] == "system_handoff" for item in result["blocked"]))
        self.assertEqual((self.vault / "My AI/guide.md").read_text(), "Use [[Incoming/paper.pdf]].\n")

    def test_matching_system_examples_and_inline_provenance_do_not_block(self):
        original = ('# Example\n\n```json\n{"source": "Incoming/paper.pdf"}\n```\n'
                    'Historical inline path: `Incoming/paper.pdf`.\n')
        self.put("Engine/SKILL.md", original)
        self.put("Incoming/paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}],
                                system_root="Engine")
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Engine/SKILL.md").read_text(), original)
        self.assertTrue(any(item["code"] == "context_sensitive_path_reference" for item in result["warnings"]))

    def test_symlink_source_parent_and_package_member_refused(self):
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "paper.pdf").write_bytes(b"outside")
        (self.vault / "link").symlink_to(outside, target_is_directory=True)
        self.put("Incoming/a.pdf", b"a")
        result = self.run_moves([{"source": "link/paper.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "blocked", result)
        result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "link/a.pdf"}])
        self.assertEqual(result["status"], "blocked", result)
        self.put("Incoming/package/a.txt", "a")
        (self.vault / "Incoming/package/escape").symlink_to(outside, target_is_directory=True)
        result = self.run_moves([{"source": "Incoming/package", "destination": "Library/package"}])
        self.assertEqual(result["status"], "blocked", result)

    def test_held_incoming_reference_causes_handoff(self):
        self.put("Active package/readme.md", "[paper](../Incoming/paper.pdf)\n")
        self.put("Incoming/paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}],
                                holds=["Active package"])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["code"] == "held_reference" for item in result["blocked"]))

    def test_unsupported_code_path_reference_blocks_move(self):
        self.put("analysis.py", 'input_path = "Incoming/paper.pdf"\n')
        self.put("Incoming/paper.pdf", b"paper")
        result = self.run_moves([{"source": "Incoming/paper.pdf", "destination": "Library/paper.pdf"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["code"] == "unsupported_path_reference" for item in result["blocked"]))

    def test_unsupported_relative_code_and_css_references_are_reported(self):
        self.put("Incoming/a.png", b"image")
        self.put("Incoming/style.css", 'body {background: url("a.png")}\n')
        self.put("Incoming/analysis.py", 'source = "a.png"\n')
        result = self.run_moves([{"source": "Incoming/a.png", "destination": "Library/a.png"}])
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue(any(item["file"] == "Incoming/analysis.py" for item in result["blocked"]))
        self.assertTrue(any(item["code"] == "unsupported_css_reference" for item in result["blocked"]))

    def test_failure_after_move_rolls_back_original_bytes(self):
        self.put("Incoming/a.pdf", b"a\x00")
        self.put("MOC.md", "[[Incoming/a.pdf|a]]\n")
        def fail(stage, path=None):
            if stage == "after_move":
                raise OSError("simulated move failure")
        with mock.patch.object(MOVE, "checkpoint", fail):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "Incoming/a.pdf").read_bytes(), b"a\x00")
        self.assertEqual((self.vault / "MOC.md").read_text(), "[[Incoming/a.pdf|a]]\n")
        self.assertFalse((self.vault / "Library/a.pdf").exists())
        self.assertEqual((self.root / "recovery/originals/Incoming/a.pdf").read_bytes(), b"a\x00")

    def test_failure_after_reference_write_rolls_back_note_and_move(self):
        self.put("Incoming/a.pdf", b"a")
        self.put("MOC.md", "Words stay. [[Incoming/a.pdf|Label]]\n")
        def fail(stage, path=None):
            if stage == "after_write":
                raise OSError("simulated write failure")
        with mock.patch.object(MOVE, "checkpoint", fail):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "MOC.md").read_text(), "Words stay. [[Incoming/a.pdf|Label]]\n")
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_rollback_retains_concurrent_note_edit(self):
        self.put("Incoming/a.pdf", b"a")
        self.put("MOC.md", "[[Incoming/a.pdf]]\n")
        def fail(stage, path=None):
            if stage == "after_write":
                (self.vault / path).write_text("User wrote this during the operation.\n")
                raise OSError("simulated concurrent edit")
        with mock.patch.object(MOVE, "checkpoint", fail):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rollback_incomplete", result)
        self.assertEqual((self.vault / "MOC.md").read_text(), "User wrote this during the operation.\n")
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_destination_created_after_preflight_is_not_overwritten(self):
        self.put("Incoming/a.pdf", b"a")
        def concurrent(stage, path=None):
            if stage == "after_backup":
                self.put("Library/a.pdf", b"concurrent file")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "Library/a.pdf").read_bytes(), b"concurrent file")
        self.assertEqual((self.vault / "Incoming/a.pdf").read_bytes(), b"a")

    def test_source_changed_after_preflight_is_retained(self):
        self.put("Incoming/a.pdf", b"a")
        def concurrent(stage, path=None):
            if stage == "after_backup":
                self.put("Incoming/a.pdf", b"new user bytes")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertEqual((self.vault / "Incoming/a.pdf").read_bytes(), b"new user bytes")

    def test_unrelated_concurrent_addition_and_edit_do_not_freeze_batch(self):
        self.put("Incoming/a.pdf", b"a")
        self.put("Other.md", "unrelated before\n")
        def concurrent(stage, path=None):
            if stage == "after_backup":
                self.put("Other.md", "unrelated current work\n")
                self.put("New unrelated.md", "another chat's work\n")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "applied", result)
        self.assertEqual((self.vault / "Other.md").read_text(), "unrelated current work\n")
        self.assertTrue((self.vault / "New unrelated.md").exists())

    def test_new_affected_incoming_reference_requires_replan(self):
        self.put("Incoming/a.pdf", b"a")
        def concurrent(stage, path=None):
            if stage == "after_backup":
                self.put("New incoming.md", "[[Incoming/a.pdf]]\n")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())
        self.assertEqual((self.vault / "New incoming.md").read_text(), "[[Incoming/a.pdf]]\n")

    def test_incoming_reference_added_during_apply_rolls_back(self):
        self.put("Incoming/a.pdf", b"a")
        def concurrent(stage, path=None):
            if stage == "after_move":
                self.put("New incoming.md", "[[Incoming/a.pdf]]\n")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())
        self.assertEqual((self.vault / "New incoming.md").read_text(), "[[Incoming/a.pdf]]\n")

    def test_concurrent_change_to_moved_bytes_is_not_clobbered_by_rollback(self):
        self.put("Incoming/a.pdf", b"original")
        def concurrent(stage, path=None):
            if stage == "after_move":
                self.put(path, b"new concurrent bytes")
                raise OSError("simulated concurrent write")
        with mock.patch.object(MOVE, "checkpoint", concurrent):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rollback_incomplete", result)
        self.assertEqual((self.vault / "Library/a.pdf").read_bytes(), b"new concurrent bytes")
        self.assertEqual((self.root / "recovery/originals/Incoming/a.pdf").read_bytes(), b"original")

    def test_cli_defaults_to_dry_run_and_returns_json(self):
        self.put("Incoming/a.pdf", b"a")
        plan = self.root / "plan.json"
        plan.write_text(json.dumps([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}]))
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        process = subprocess.run([sys.executable, str(Path(MOVE.__file__)), "--vault", str(self.vault),
                                  "--plan", str(plan)], env=environment, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["status"], "dry_run")
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_backup_inside_vault_is_refused(self):
        self.put("Incoming/a.pdf", b"a")
        result = MOVE.execute(self.vault, [{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}],
                              apply=True, backup_dir=self.vault / "backup")
        self.assertEqual(result["status"], "blocked", result)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())

    def test_unsupported_filesystem_does_not_copy_over_files(self):
        self.put("Incoming/a.pdf", b"a")
        with mock.patch.object(MOVE.os, "link", side_effect=OSError(errno.EXDEV, "cross-device")):
            result = self.run_moves([{"source": "Incoming/a.pdf", "destination": "Library/a.pdf"}])
        self.assertEqual(result["status"], "rolled_back", result)
        self.assertTrue((self.vault / "Incoming/a.pdf").exists())
        self.assertFalse((self.vault / "Library/a.pdf").exists())


if __name__ == "__main__":
    unittest.main()
