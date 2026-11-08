#!/usr/bin/env python3
"""Exercise installer recovery, path safety, and portable installation state.

Requirements: Python 3.9+, the manager's local toolchain, and macOS sandbox-exec.
Date: 2026-10-14. Run: python3 -B scripts/test_manage_runtime.py

All fixtures and build outputs use a temporary directory outside the vault.
Acquisition is replaced by a bounded local archive response; build execution,
offline verification, manifest checks, and activation use the actual manager.
The source recipe's separate tests cover the REA analysis itself.
"""

from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import unittest
import unicodedata
from unittest import mock
import zipfile


sys.dont_write_bytecode = True
MODULE_SPEC = importlib.util.spec_from_file_location("rea_manager", Path(__file__).with_name("manage_runtime.py"))
manager = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(manager)


FAKE_RECIPE = '''import argparse
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("--source-root", type=Path)
parser.add_argument("--runtime-root", type=Path, required=True)
args = parser.parse_args()
if args.action == "build":
    mode = (args.source_root / "mode.txt").read_text().strip()
    if mode == "build_failure":
        sys.exit(41)
    (args.runtime_root / "bin").mkdir()
    (args.runtime_root / "bin" / "rea.mjs").write_text("console.log('local fixture');\\n")
    if mode == "verification_failure":
        (args.runtime_root / "reject").write_text("reject")
elif args.action == "verify":
    if (args.runtime_root / "reject").exists():
        sys.exit(42)
    if not (args.runtime_root / "bin" / "rea.mjs").is_file():
        sys.exit(43)
else:
    sys.exit(44)
'''


class LocalArchiveResponse(io.BytesIO):
    def geturl(self):
        return "https://example.invalid/pinned.zip"


class RuntimeManagerTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="rea_manager_test_")
        self.test_root = Path(self.temporary_directory.name).resolve()
        self.addCleanup(self.temporary_directory.cleanup)
        self.recipe = self.test_root / "build_runtime.py"
        self.recipe.write_text(FAKE_RECIPE)
        self.archive_path = self.make_source_archive("success")
        self.spec_path = self.test_root / "runtime_spec.json"
        self.specification = self.make_spec(self.archive_path)
        self.runtime_root = self.test_root / "external_runtime"

    def make_source_archive(self, mode):
        archive_path = self.test_root / f"{mode}.zip"
        with zipfile.ZipFile(archive_path, "w") as archive:
            archive.writestr("source/mode.txt", mode)
        return archive_path

    def make_spec(self, archive_path, version="fixture.1"):
        specification = {
            "schema_version": 1,
            "version": version,
            "source": {"url": "https://example.invalid/pinned.zip", "sha256": manager.file_sha256(archive_path)},
            "recipe": {"path": self.recipe.name, "sha256": manager.file_sha256(self.recipe)},
            "entrypoint": "bin/rea.mjs",
            "commands": ["analyze-javascript-application", "inspect-analysis-view"],
        }
        manager.write_json(self.spec_path, specification)
        return specification

    def install(self, action="install", specification=None, archive_path=None):
        selected_specification = specification or self.specification
        selected_archive = archive_path or self.archive_path
        archive_bytes = selected_archive.read_bytes()
        with mock.patch.object(manager.urllib.request, "urlopen", side_effect=lambda *args, **kwargs: LocalArchiveResponse(archive_bytes)):
            return manager.install_runtime(action, self.runtime_root, selected_specification, self.recipe)

    def assert_no_staging(self):
        self.assertEqual(list(self.test_root.glob(".rea_build_*")), [])

    def test_clean_install_reinstall_and_relocation(self):
        manager.load_spec(self.spec_path)
        self.assertEqual(self.install()["status"], "installed")
        first_entrypoint = manager.installed_runtime(self.runtime_root, self.specification)
        first_digest = manager.file_sha256(first_entrypoint)
        self.assertEqual(self.install()["status"], "already_installed")
        self.assertEqual(self.install("reinstall")["status"], "installed")
        self.assertEqual(manager.file_sha256(manager.installed_runtime(self.runtime_root, self.specification)), first_digest)
        self.assertTrue((self.runtime_root / "previous" / "bin" / "rea.mjs").is_file())
        relocated = self.test_root / "relocated_runtime"
        shutil.copytree(self.runtime_root, relocated)
        manager.ensure_managed_root(relocated, create=False)
        relocated_entrypoint = manager.installed_runtime(relocated, self.specification)
        manager.verify_recipe(self.recipe, relocated / "current")
        self.assertEqual(manager.file_sha256(relocated_entrypoint), first_digest)
        self.assert_no_staging()

    def test_failed_build_and_failed_verification_retain_current(self):
        self.install()
        original_metadata = (self.runtime_root / "current" / manager.RUNTIME_METADATA).read_bytes()
        for mode in ("build_failure", "verification_failure"):
            with self.subTest(mode=mode):
                archive = self.make_source_archive(mode)
                proposed_spec = self.make_spec(archive, version="fixture.2")
                with self.assertRaises(manager.RuntimeProblem):
                    self.install("update", proposed_spec, archive)
                self.assertEqual((self.runtime_root / "current" / manager.RUNTIME_METADATA).read_bytes(), original_metadata)
                manager.installed_runtime(self.runtime_root, self.specification)
                self.assert_no_staging()

    def test_failed_atomic_promotion_restores_current(self):
        self.install()
        original_metadata = (self.runtime_root / "current" / manager.RUNTIME_METADATA).read_bytes()
        actual_replace = manager.os.replace

        def fail_candidate_promotion(source, destination):
            if Path(source).name == "candidate":
                raise OSError("simulated activation failure")
            return actual_replace(source, destination)

        with mock.patch.object(manager.os, "replace", side_effect=fail_candidate_promotion):
            with self.assertRaisesRegex(OSError, "activation failure"):
                self.install("reinstall")
        self.assertEqual((self.runtime_root / "current" / manager.RUNTIME_METADATA).read_bytes(), original_metadata)
        manager.installed_runtime(self.runtime_root, self.specification)
        self.assert_no_staging()

    def test_runtime_tamper_and_extra_file_are_rejected(self):
        self.install()
        unexpected_file = self.runtime_root / "current" / "unexpected.txt"
        unexpected_file.write_text("unexpected runtime content")
        with self.assertRaisesRegex(manager.RuntimeProblem, "unexpected files"):
            manager.installed_runtime(self.runtime_root, self.specification)
        unexpected_file.unlink()
        entrypoint = manager.installed_runtime(self.runtime_root, self.specification)
        entrypoint.write_text("changed executable")
        with self.assertRaisesRegex(manager.RuntimeProblem, "have changed"):
            manager.installed_runtime(self.runtime_root, self.specification)

    def test_running_analysis_prevents_replacement_and_lock_releases(self):
        manager.ensure_managed_root(self.runtime_root, create=True)
        with manager.installation_lock(self.runtime_root, exclusive=False):
            with self.assertRaisesRegex(manager.RuntimeProblem, "Another REA analysis"):
                with manager.installation_lock(self.runtime_root, exclusive=True):
                    self.fail("Replacement entered while an analysis held the runtime")
        with manager.installation_lock(self.runtime_root, exclusive=True):
            self.assertEqual((self.runtime_root / ".install_lock").read_bytes(), b"")

    def test_symlink_and_unmanaged_roots_are_rejected(self):
        linked_root = self.test_root / "linked_runtime"
        linked_root.symlink_to(self.test_root, target_is_directory=True)
        with self.assertRaisesRegex(manager.RuntimeProblem, "Symbolic links"):
            manager.runtime_root_path(str(linked_root))
        unmanaged_root = self.test_root / "unmanaged_runtime"
        unmanaged_root.mkdir()
        (unmanaged_root / "unrelated.txt").write_text("keep")
        with self.assertRaisesRegex(manager.RuntimeProblem, "unmanaged files"):
            manager.ensure_managed_root(unmanaged_root, create=True)
        self.assertEqual((unmanaged_root / "unrelated.txt").read_text(), "keep")

    def test_case_and_unicode_vault_aliases_are_rejected(self):
        actual_vault = manager.vault_root_for_skill()
        if actual_vault:
            alias = actual_vault.with_name(actual_vault.name.swapcase())
            if manager.same_existing_location(alias, actual_vault):
                with self.assertRaisesRegex(manager.RuntimeProblem, "outside the vault"):
                    manager.runtime_root_path(str(alias / "rea_test_never_created"))
                self.assertFalse((actual_vault / "rea_test_never_created").exists())
        simulated_vault = self.test_root / "simulated_vault_caf\u00e9"
        simulated_vault.mkdir()
        unicode_alias = simulated_vault.with_name(unicodedata.normalize("NFD", simulated_vault.name))
        if manager.same_existing_location(unicode_alias, simulated_vault):
            with self.assertRaisesRegex(manager.RuntimeProblem, "outside the vault"):
                manager.runtime_root_path(str(unicode_alias / "new_runtime"), str(simulated_vault))
        self.assertFalse((simulated_vault / "new_runtime").exists())

    def test_zip_traversal_and_symlinks_are_rejected(self):
        for index, filename in enumerate(("../escape.txt", "/absolute.txt", "source/../../escape.txt")):
            with self.subTest(filename=filename):
                archive_path = self.test_root / "traversal.zip"
                with zipfile.ZipFile(archive_path, "w") as archive:
                    archive.writestr(filename, "do not extract")
                with self.assertRaises(manager.RuntimeProblem):
                    manager.safe_extract_archive(archive_path, self.test_root / f"extract_{index}")
        linked_archive = self.test_root / "linked.zip"
        with zipfile.ZipFile(linked_archive, "w") as archive:
            member = zipfile.ZipInfo("source/linked")
            member.create_system = 3
            member.external_attr = (stat.S_IFLNK | 0o777) << 16
            archive.writestr(member, "../../escape")
        with self.assertRaisesRegex(manager.RuntimeProblem, "nonregular"):
            manager.safe_extract_archive(linked_archive, self.test_root / "linked_extract")

    def test_tar_links_are_rejected(self):
        archive_path = self.test_root / "linked.tar"
        with tarfile.open(archive_path, "w") as archive:
            member = tarfile.TarInfo("source/linked")
            member.type = tarfile.SYMTYPE
            member.linkname = "../../escape"
            archive.addfile(member)
        with self.assertRaisesRegex(manager.RuntimeProblem, "nonregular"):
            manager.safe_extract_archive(archive_path, self.test_root / "tar_extract")

    def test_upstream_agent_configuration_is_not_materialized(self):
        archive_path = self.test_root / "instructions.zip"
        forbidden_entries = ["source/CLAUDE.md", "source/AGENTS.md", "source/.claude/rules/local.md", "source/.agents/skills/example/SKILL.md", "source/codex.md"]
        with zipfile.ZipFile(archive_path, "w") as archive:
            archive.writestr("source/needed.js", "const value = 1;")
            for filename in forbidden_entries:
                archive.writestr(filename, "upstream configuration")
        extracted = self.test_root / "filtered_extract"
        manager.safe_extract_archive(archive_path, extracted)
        self.assertTrue((extracted / "source" / "needed.js").is_file())
        for filename in forbidden_entries:
            self.assertFalse((extracted / filename).exists())

    def test_wrong_source_and_recipe_digest_fail(self):
        source_bytes = self.archive_path.read_bytes()
        with mock.patch.object(manager.urllib.request, "urlopen", return_value=LocalArchiveResponse(source_bytes + b"changed")):
            with self.assertRaisesRegex(manager.RuntimeProblem, "pinned SHA-256"):
                manager.download_archive(self.specification, self.test_root / "download.archive")
        self.recipe.write_text(FAKE_RECIPE + "\n# changed\n")
        with self.assertRaisesRegex(manager.RuntimeProblem, "recipe is missing or does not match"):
            manager.load_spec(self.spec_path)

    def test_node_patch_versions_are_enforced(self):
        for version, accepted in (
            ("v22.0.0", False), ("v22.18.0", False), ("v22.19.0", True),
            ("v23.0.0", False), ("v24.0.0", False), ("v24.11.0", True),
            ("v25.0.0", False), ("v26.0.0", True),
            ("v22.19.0-rc.1", False), ("v24.11.0-rc.1", False),
            ("v26.0.0-nightly", False),
        ):
            with self.subTest(version=version), mock.patch.object(manager.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, version + "\n", "")):
                if accepted:
                    self.assertTrue(manager.require_node(self.specification))
                else:
                    with self.assertRaises(manager.RuntimeProblem):
                        manager.require_node(self.specification)

    def test_unsupported_platform_does_not_silently_run(self):
        with mock.patch.object(manager.platform, "system", return_value="Linux"):
            with self.assertRaisesRegex(manager.RuntimeProblem, "requires macOS"):
                manager.offline_command(["node", "example.mjs"])

    def test_offline_isolation_checks_parent_and_child_socket_operations(self):
        self.assertEqual(manager.verify_offline_isolation(), {"denied_operations": 6, "processes": 2})

    def test_missing_offline_enforcement_fails_self_test(self):
        with mock.patch.object(manager, "offline_command", side_effect=lambda command: command):
            with self.assertRaisesRegex(manager.RuntimeProblem, "unexpectedly succeeded"):
                manager.verify_offline_isolation()


if __name__ == "__main__":
    unittest.main(verbosity=2)
