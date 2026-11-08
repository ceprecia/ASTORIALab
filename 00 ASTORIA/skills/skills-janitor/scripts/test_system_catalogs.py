#!/usr/bin/env python3
# File: test_system_catalogs.py | Purpose: Check system catalog selection, generation and lint parity.
# Inputs/outputs: Temporary miniature vaults only; the working vault is never generated.
# Run: python3 -B test_system_catalogs.py (requires PyYAML).

# 1. Setup the existing builder and lint interfaces.
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

import build_views as views
import lint
import skillkit as sk


class SystemCatalogTests(unittest.TestCase):
    def setUp(self):
        # 2. Keep all generated fixtures outside the vault.
        self.scratch = tempfile.TemporaryDirectory(prefix="astoria_system_catalog_")
        self.addCleanup(self.scratch.cleanup)
        self.vault = Path(self.scratch.name)
        self.vocab = {
            "levels": {name: name for name in ("companion", "coordinator", "skill", "profile")},
            "trigger_counts": {"companion": [3, 5], "coordinator": [0, 5], "skill": [1, 5], "profile": [0, 0]},
            "systems": {name: {"tagline": name} for name in ("Engineering System", "ASTORIA System Builder")},
            "system_order": ["Engineering System", "ASTORIA System Builder"],
            "system_coordinators": {"Engineering System": "engineering-coordinator"},
            "parts": {}, "part_coordinators": {}, "families": {}, "modalities": [], "populations": [],
            "roots": {"system": "00 ASTORIA"}, "catalog_style": "full",
        }
        self.write_skill("skill-builder", "ASTORIA System Builder", "skill", "Inspect fixture scaffolding.")
        self.write_skill("mechanism-review", "Engineering System", "skill", "Inspect fixture mechanisms.")
        self.write_skill("wiring-review", "Engineering System", "skill", "Inspect fixture wiring.")
        self.write_skill("engineering-profile", "Engineering System", "profile")
        self.write_skill("engineering-companion", "Engineering System", "companion",
                         "Plan fixture work, review fixture choices, resume fixture session.")
        self.write_skill("engineering-coordinator", "Engineering System", "coordinator", body=(
            "## Specialist Catalog\n\n<!-- catalog:start -->\n<!-- catalog:end -->\n\n"
            "## Boundaries\n\nKeep this user-authored sentence.\n"))
        self.save_vocab()
        self.map_path = self.vault / sk.MAP_REL
        generated = views.registry(sk.load_skills(str(self.vault)), self.vocab)
        self.map_path.write_text("# Skill Map\n\n<!-- registry:start -->\n" + generated +
                                 "\n<!-- registry:end -->\n", encoding="utf-8")
        self.coordinator_path = self.vault / sk.SKILLS_REL / "engineering-coordinator" / "SKILL.md"

    def write_skill(self, name, system, level, triggers="", body="## Purpose\n\nFixture capability.\n"):
        folder = self.vault / sk.SKILLS_REL / name
        folder.mkdir(parents=True, exist_ok=True)
        description = "A fixture capability."
        if triggers:
            description += " Triggers: " + triggers
        metadata = {"level": level, "system": system, "dependencies": "",
                    "created": "2026-10-30", "updated": "2026-10-30"}
        (folder / "SKILL.md").write_text(sk.dump_frontmatter(name, description, metadata) + "\n" + body,
                                         encoding="utf-8")

    def save_vocab(self):
        path = self.vault / sk.VOCAB_REL
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Fixture vocabulary\n\n```yaml\n" + sk.yaml.safe_dump(self.vocab) + "```\n",
                        encoding="utf-8")

    def run_builder(self, check=False):
        output = io.StringIO()
        arguments = ["--vault", str(self.vault)] + (["--check"] if check else [])
        with contextlib.redirect_stdout(output):
            status = views.main(arguments)
        return status, output.getvalue()

    def run_lint(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = lint.main(["--vault", str(self.vault), "--json"])
        return status, json.loads(output.getvalue())

    # 3. Select exact-system specialists, preserving both supported entry styles.
    def test_exact_system_and_skill_level_filter(self):
        skills = sk.load_skills(str(self.vault))
        text = views.system_catalog("Engineering System", skills, self.vocab)
        self.assertIn(skills["mechanism-review"].link(), text)
        self.assertIn(skills["wiring-review"].link(), text)
        self.assertLess(text.index("|mechanism-review]]"), text.index("|wiring-review]]"))
        for name in ("engineering-companion", "engineering-coordinator", "engineering-profile", "skill-builder"):
            self.assertNotIn(skills[name].link(), text)
        self.assertIn("2 skills in this system.", text)
        self.assertIn("A fixture capability. Triggers:", text)
        compact = dict(self.vocab, catalog_style="compact")
        self.assertNotIn("A fixture capability.", views.system_catalog("Engineering System", skills, compact))

    def test_no_system_mapping_keeps_older_vaults_supported(self):
        vocab = copy.deepcopy(self.vocab)
        del vocab["system_coordinators"]
        self.assertEqual([], views.system_catalog_views({}, vocab, str(self.vault)))

    def test_grouped_registry_lists_members_once_without_changing_other_systems(self):
        skills = sk.load_skills(str(self.vault))
        original = views.registry(skills, self.vocab)
        vocab = copy.deepcopy(self.vocab)
        vocab["system_sections"] = {"Engineering System": {
            "Session owners": ["engineering-companion", "engineering-coordinator"],
            "Specialists and profiles": ["mechanism-review", "wiring-review", "engineering-profile"],
        }}
        grouped = views.registry(skills, vocab)
        self.assertIn("### Session owners", grouped)
        self.assertIn("### Specialists and profiles", grouped)
        for names in vocab["system_sections"]["Engineering System"].values():
            for name in names:
                self.assertEqual(1, grouped.count(skills[name].link()), name)
        other_system = "##  ASTORIA System Builder"
        self.assertEqual(original.partition(other_system)[2], grouped.partition(other_system)[2])

    # 4. Exercise actual generation and read-only checks in the miniature vault.
    def test_generate_check_and_idempotence_preserve_surrounding_text(self):
        before = self.coordinator_path.read_text(encoding="utf-8")
        self.assertEqual(1, self.run_builder(check=True)[0])
        self.assertEqual(before, self.coordinator_path.read_text(encoding="utf-8"))
        self.assertEqual(0, self.run_builder()[0])
        after = self.coordinator_path.read_text(encoding="utf-8")
        self.assertTrue(after.endswith("## Boundaries\n\nKeep this user-authored sentence.\n"))
        self.assertEqual(0, self.run_builder(check=True)[0])
        self.assertEqual(0, self.run_builder()[0])
        self.assertEqual(after, self.coordinator_path.read_text(encoding="utf-8"))
        status, report = self.run_lint()
        self.assertEqual(0, status, report)

    def test_marker_errors_stop_before_any_view_is_written(self):
        original = self.coordinator_path.read_text(encoding="utf-8")
        malformed = [
            "No markers.\n",
            "<!-- catalog:start -->\n",
            "<!-- catalog:end -->\n<!-- catalog:start -->\n",
            "<!-- catalog:start -->\n<!-- catalog:start -->\n<!-- catalog:end -->\n",
        ]
        for marker_text in malformed:
            with self.subTest(markers=marker_text):
                self.coordinator_path.write_text(original.split("## Specialist Catalog")[0] + marker_text,
                                                 encoding="utf-8")
                self.map_path.write_text("stale map must remain untouched\n", encoding="utf-8")
                status, output = self.run_builder()
                self.assertEqual(2, status)
                self.assertIn("exactly one ordered catalog marker pair", output)
                self.assertEqual("stale map must remain untouched\n", self.map_path.read_text(encoding="utf-8"))
                _, report = self.run_lint()
                self.assertTrue(any("catalog marker pair" in message for _, message in report["errors"]))

    def test_coordinator_configuration_errors_are_explicit(self):
        skills = sk.load_skills(str(self.vault))
        for name, expected in (("absent-coordinator", "not found"), ("mechanism-review", "must be a coordinator"),
                               ("skill-builder", "must be a coordinator")):
            with self.subTest(coordinator=name):
                vocab = dict(self.vocab, system_coordinators={"Engineering System": name})
                with self.assertRaisesRegex(ValueError, expected):
                    views.system_catalog_views(skills, vocab, str(self.vault))
        for mapping, expected in ((["engineering-coordinator"], "must map system names"),
                                  ({"Unknown System": "engineering-coordinator"}, "unknown system")):
            with self.subTest(mapping=mapping):
                vocab = dict(self.vocab, system_coordinators=mapping)
                with self.assertRaisesRegex(ValueError, expected):
                    views.system_catalog_views(skills, vocab, str(self.vault))

    def test_portable_links_use_the_coordinator_location(self):
        self.vocab["starter"] = {"portable_links": True}
        self.save_vocab()
        self.assertEqual(0, self.run_builder()[0])
        text = self.coordinator_path.read_text(encoding="utf-8")
        self.assertIn("[mechanism-review](../mechanism-review/SKILL.md)", text)
        self.assertNotIn("|mechanism-review]]", text)
        self.assertEqual(0, self.run_builder(check=True)[0])
        status, report = self.run_lint()
        self.assertEqual(0, status, report)

    # 5. Detect omissions and forbidden additions inside the generated region.
    def test_body_link_cannot_hide_missing_catalog_entry(self):
        self.assertEqual(0, self.run_builder()[0])
        text = self.coordinator_path.read_text(encoding="utf-8")
        entry = next(line for line in text.splitlines() if "|wiring-review]]" in line)
        self.coordinator_path.write_text(text.replace(entry + "\n", "") + "\n" + entry + "\n", encoding="utf-8")
        status, report = self.run_lint()
        self.assertEqual(1, status)
        self.assertIn(["engineering-coordinator", "system catalog differs from skill frontmatter (run build_views.py)"],
                      report["errors"])

    def test_excluded_role_entry_is_stale_even_with_all_specialists_present(self):
        self.assertEqual(0, self.run_builder()[0])
        skills = sk.load_skills(str(self.vault))
        text = self.coordinator_path.read_text(encoding="utf-8")
        extra = views.entry(skills["engineering-companion"])
        self.coordinator_path.write_text(text.replace("<!-- catalog:end -->", extra + "\n<!-- catalog:end -->"),
                                         encoding="utf-8")
        self.assertEqual(1, self.run_builder(check=True)[0])
        status, report = self.run_lint()
        self.assertEqual(1, status)
        self.assertTrue(any("system catalog differs" in message for _, message in report["errors"]))


if __name__ == "__main__":
    unittest.main()
