"""Check how the layout extracts and compares activity dates."""
import contextlib
import io
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_layout import OUT_REL, comparison_text, main, newest_log_date


class LayoutDateChecks(unittest.TestCase):
    def setUp(self):
        self.text = ('---\ncreated: 2026-01-01\n---\n\n# Layout\n'
                     '| Study | MOC | 2026-01-02 |\n'
                     '- Rule effective 2026-01-03.\n\nBuilt 2026-01-01.\n')

    def test_generated_dates_alone_do_not_report_drift(self):
        updated = self.text.replace('2026-01-01', '2026-02-01')
        self.assertEqual(comparison_text(self.text), comparison_text(updated))

    def test_new_moc_log_date_is_detected(self):
        updated = self.text.replace('2026-01-02', '2026-02-02')
        self.assertNotEqual(comparison_text(self.text), comparison_text(updated))

    def test_date_in_a_rule_is_not_masked(self):
        updated = self.text.replace('2026-01-03', '2026-02-03')
        self.assertNotEqual(comparison_text(self.text), comparison_text(updated))

    def test_created_fields_in_body_still_matter(self):
        original = self.text + '\ncreated: 2026-01-04\n'
        updated = original.replace('2026-01-04', '2026-02-04')
        self.assertNotEqual(comparison_text(original), comparison_text(updated))

    def test_newest_activity_comes_from_existing_log_headings(self):
        for heading in ('Log', '🗓️ Logs', 'Research Log', '🗓️ Research Log'):
            with self.subTest(heading=heading):
                moc = (f'# {heading}\n'
                       '## 2032-04-06 09:25 - Stock count\n'
                       '### 2032-04-10 - Shelf repair\n'
                       '# 🤖 AI Notes\n'
                       '## 2032-04-12 - Excluded maintenance entry\n')
                self.assertEqual(newest_log_date(moc), '2032-04-10')

    def test_fenced_examples_do_not_supply_headings_or_close_the_log(self):
        moc = ('# Log\n'
               '## 2032-04-06 - Earlier event\n'
               '````markdown\n'
               '```\n'
               '# AI Notes\n'
               '## 2032-04-18 - Fenced example\n'
               '````\n'
               '## 2032-04-10 - Recent event\n'
               '~~~markdown\n'
               '## 2032-04-19 - Unclosed example\n')
        self.assertEqual(newest_log_date(moc), '2032-04-10')

    def test_dated_headings_without_a_top_level_log_are_ignored(self):
        moc = '# Workbench\n## Research Log\n### 2032-04-10 - References\n'
        self.assertEqual(newest_log_date(moc), '')


    def test_apply_writes_only_when_the_generated_layout_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            vault = Path(temporary)
            vocabulary = vault / "00 ASTORIA/skills/skill-builder/assets/vocabulary.md"
            vocabulary.parent.mkdir(parents=True)
            vocabulary.write_text('```yaml\nroots:\n  system: "00 ASTORIA"\n'
                                  'layout_rules:\n  - Original layout rule.\n```\n', encoding="utf-8")
            output = vault / OUT_REL
            output.parent.mkdir()

            def run(*flags):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    code = main(["--vault", str(vault), *flags])
                return code, stream.getvalue()

            self.assertEqual(run()[0], 0)
            self.assertEqual(run("--check", "--apply")[0], 1)
            self.assertFalse(output.exists())
            code, report = run("--apply")
            self.assertEqual(code, 0)
            self.assertIn("wrote ", report)

            dated = output.read_text(encoding="utf-8")
            dated = re.sub(r"(?m)^created: \d{4}-\d{2}-\d{2}$", "created: 2000-01-01", dated)
            dated = re.sub(r"(?m)^Built \d{4}-\d{2}-\d{2}\.$", "Built 2000-01-01.", dated)
            output.write_text(dated, encoding="utf-8")
            stamp = 946684800_000_000_000
            os.utime(output, ns=(stamp, stamp))
            before = (output.read_bytes(), output.stat().st_mtime_ns)
            for flags in ((), ("--check",), ("--apply",), ("--apply",)):
                with self.subTest(flags=flags):
                    code, report = run(*flags)
                    self.assertEqual(code, 0)
                    self.assertIn("file unchanged", report)
                    self.assertNotIn("wrote ", report)
                    self.assertEqual((output.read_bytes(), output.stat().st_mtime_ns), before)

            config = vocabulary.read_text(encoding="utf-8")
            vocabulary.write_text(config.replace("Original layout rule.", "Revised layout rule."),
                                  encoding="utf-8")
            self.assertIn("differs from a fresh build", run()[1])
            self.assertEqual(run("--check")[0], 1)
            self.assertEqual((output.read_bytes(), output.stat().st_mtime_ns), before)
            code, report = run("--apply")
            self.assertEqual(code, 0)
            self.assertIn("wrote ", report)
            self.assertIn("Revised layout rule.", output.read_text(encoding="utf-8"))
            self.assertEqual(run("--check")[0], 0)


if __name__ == '__main__':
    unittest.main()
