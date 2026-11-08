"""Test rename preflight and bounded recovery in synthetic temporary vaults."""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import propagate_rename as PROPAGATE
ROOT_SPEC = importlib.util.spec_from_file_location(
    'test_root_rename', SCRIPTS.parents[1] / 'skills-janitor/scripts/rename_roots.py')
ROOTS = importlib.util.module_from_spec(ROOT_SPEC)
ROOT_SPEC.loader.exec_module(ROOTS)


class RenamePreflightTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.parent = Path(self.temporary.name)
        self.vault = self.parent / 'vault'
        self.vault.mkdir()
        (self.vault / '00 ASTORIA').mkdir()
        self.vocab = {'roots': {'system': '00 ASTORIA', 'projects': 'Projects',
                               'areas': 'Areas', 'inbox': 'Inbox', 'calendar': 'Calendar'},
                      'optional_roots': ['inbox', 'calendar'], 'dropped_roots': []}
        self.put(ROOTS.sk.VOCAB_REL, '```yaml\nroots:\n  system: "00 ASTORIA"\n'
                 '  projects: "Projects"\n  areas: "Areas"\n  inbox: "Inbox"\n'
                 '  calendar: "Calendar"\noptional_roots: [inbox, calendar]\n```\n')
        self.real_mkdtemp = tempfile.mkdtemp
        self.backups = patch.object(PROPAGATE.tempfile, 'mkdtemp',
                                   side_effect=lambda **kwargs: self.real_mkdtemp(dir=self.parent, **kwargs))
        self.backups.start()

    def tearDown(self):
        self.backups.stop()
        self.temporary.cleanup()

    def put(self, relative, text):
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode('utf-8'))
        return path

    def snapshot(self):
        return {path.relative_to(self.vault).as_posix(): path.read_bytes() if path.is_file() else None
                for path in self.vault.rglob('*')}

    def propagate(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), patch.object(PROPAGATE.subprocess, 'run'):
            return PROPAGATE.main(['--vault', str(self.vault), *args])

    def roots(self, *args):
        with patch.object(ROOTS.sk, 'load_vocab', return_value=self.vocab), \
             patch.object(ROOTS.sk, 'vault_from_argv', return_value=str(self.vault)), \
             contextlib.redirect_stdout(io.StringIO()):
            return ROOTS.main(list(args))

    def test_invalid_skill_and_path_names_do_not_write(self):
        self.put('README.md', '[[Old]] old-skill old/path\n')
        before = self.snapshot()
        for flag, value in [('--skill', 'old-skill=../escape'), ('--skill', '../old=new'),
                            ('--skill', 'old-skill=/absolute'), ('--note', 'Old=../New'),
                            ('--path', 'old/path=../../escape'), ('--path', '/old=new'),
                            ('--skill', 'same=same')]:
            with self.subTest(flag=flag, value=value), self.assertRaises(ValueError):
                self.propagate(flag, value, '--apply')
            self.assertEqual(self.snapshot(), before)

    def test_note_collision_is_refused_before_reference_changes(self):
        self.put('Projects/Old.md', 'Original\n')
        self.put('Projects/New.md', 'Keep new\n')
        self.put('README.md', '[[Old]]\n')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.propagate('--note', 'Old=New', '--move', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_skill_collision_is_refused_before_reference_changes(self):
        self.put('00 ASTORIA/skills/old-skill/SKILL.md', '---\nname: old-skill\n---\n')
        self.put('00 ASTORIA/skills/new-skill/SKILL.md', 'Keep existing\n')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.propagate('--skill', 'old-skill=new-skill', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_protected_note_copies_never_move(self):
        self.put('Projects/Old.md', 'Active\n')
        protected = ['06 🪴 Archive/Old.md', '02 📅 Calendar/Old.md',
                     '00 ASTORIA/agent_notes/Old.md', 'dated/2026-01-01 Old.md']
        for relative in protected:
            self.put(relative, 'Protected [[Old]]\n')
        self.put('README.md', '[[Old|Keep label]]\n')
        self.propagate('--note', 'Old=New', '--move', '--apply')
        self.assertTrue((self.vault / 'Projects/New.md').exists())
        for relative in protected:
            self.assertEqual((self.vault / relative).read_text(), 'Protected [[Old]]\n')
        self.assertEqual((self.vault / 'README.md').read_text(), '[[New|Keep label]]\n')

    def test_only_protected_source_does_not_rewrite_references(self):
        self.put('06 🪴 Archive/Old.md', 'Frozen\n')
        self.put('README.md', '[[Old]]\n')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.propagate('--note', 'Old=New', '--move', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_area_moc_log_tail_is_preserved(self):
        original = '# Area\n[[Old]]\n## Research Log\n### 2026-01-01\n[[Old]] stays historical.\n'
        self.put('Areas/Example MOC.md', original)
        self.propagate('--note', 'Old=New', '--apply')
        self.assertEqual((self.vault / 'Areas/Example MOC.md').read_text(), original.replace('[[Old]]', '[[New]]', 1))

    def test_note_move_failure_does_not_rewrite_references(self):
        self.put('Projects/Old.md', 'Original\n')
        self.put('README.md', '[[Old]]\n')
        before = self.snapshot()
        with patch.object(PROPAGATE.os, 'rename', side_effect=OSError('synthetic rename failure')):
            with self.assertRaises(OSError):
                self.propagate('--note', 'Old=New', '--move', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_already_renamed_skill_updates_its_field_and_views(self):
        self.put('00 ASTORIA/skills/new-skill/SKILL.md', '---\nname: old-skill\n---\n')
        self.put('00 ASTORIA/pointer.md', 'old-skill\n')
        self.propagate('--skill', 'old-skill=new-skill', '--apply')
        self.assertIn('name: new-skill', (self.vault / '00 ASTORIA/skills/new-skill/SKILL.md').read_text())
        self.assertEqual((self.vault / '00 ASTORIA/pointer.md').read_text(), 'new-skill\n')

    def test_invalid_root_names_do_not_write(self):
        self.put('README.md', 'Projects and Areas\n')
        before = self.snapshot()
        for name in ['../outside', '/absolute', 'nested/name', '.', 'Bad"Name', "Bad'Name", 'C:drive']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.roots('--set', 'projects=' + name, '--apply')
            self.assertEqual(self.snapshot(), before)

    def test_all_root_moves_preflight_before_any_cascade(self):
        self.put('Projects/a.md', 'Projects\n')
        self.put('Areas/a.md', 'Areas\n')
        (self.vault / 'Existing').mkdir()
        self.put('README.md', 'Projects and Areas\n')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.roots('--set', 'projects=Renamed', '--set', 'areas=Existing', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_case_colliding_root_name_is_refused(self):
        self.put('Projects/a.md', 'Keep\n')
        (self.vault / 'renamed').mkdir()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.roots('--set', 'projects=Renamed', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_successful_root_rename_updates_folder_and_references(self):
        self.put('Projects/a.md', 'Content stays\n')
        self.put('README.md', 'Projects/a.md\n')
        self.roots('--set', 'projects=Work', '--apply')
        self.assertFalse((self.vault / 'Projects').exists())
        self.assertEqual((self.vault / 'Work/a.md').read_text(), 'Content stays\n')
        self.assertEqual((self.vault / 'README.md').read_text(), 'Work/a.md\n')
        self.assertIn('projects: "Work"', (self.vault / ROOTS.sk.VOCAB_REL).read_text())

    def test_fresh_starter_can_rename_uncreated_content_roots(self):
        self.put('README.md', 'Projects/example.md\n')
        self.roots('--set', 'projects=Work', '--apply')
        self.assertFalse((self.vault / 'Work').exists())
        self.assertEqual((self.vault / 'README.md').read_text(), 'Work/example.md\n')

    def test_second_root_move_failure_restores_first_move_and_references(self):
        self.put('Projects/a.md', 'Project\n')
        self.put('Areas/a.md', 'Area\n')
        self.put('README.md', 'Projects and Areas\n')
        before = self.snapshot()
        rename = os.rename
        def fail_second(source, destination):
            if Path(destination).name == 'NewAreas':
                raise OSError('synthetic second move failure')
            return rename(source, destination)
        with patch.object(PROPAGATE.os, 'rename', side_effect=fail_second):
            with self.assertRaises(OSError):
                self.roots('--set', 'projects=NewProjects', '--set', 'areas=NewAreas', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_reference_write_failure_restores_move_and_prior_writes(self):
        self.put('Projects/Old.md', '[[Old]]\n')
        self.put('README.md', '[[Old]]\n')
        before = self.snapshot()
        replace = os.replace
        count = 0
        def fail_second(source, destination):
            nonlocal count
            count += 1
            if count == 2:
                raise OSError('synthetic second write failure')
            return replace(source, destination)
        with patch.object(PROPAGATE.os, 'replace', side_effect=fail_second):
            with self.assertRaises(OSError):
                self.propagate('--note', 'Old=New', '--move', '--apply')
        self.assertEqual(self.snapshot(), before)

    def test_symlink_move_path_is_refused(self):
        outside = self.parent / 'outside'
        outside.mkdir()
        (self.vault / 'Projects').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.roots('--set', 'projects=Work', '--apply')
        self.assertTrue((self.vault / 'Projects').is_symlink())
        self.assertFalse((self.vault / 'Work').exists())

    def test_new_optional_drop_preserves_existing_dropped_roles(self):
        self.vocab['dropped_roots'] = ['inbox']
        self.roots('--drop', 'calendar', '--apply')
        text = (self.vault / ROOTS.sk.VOCAB_REL).read_text()
        self.assertIn('dropped_roots: [calendar, inbox]', text)


if __name__ == '__main__':
    unittest.main()
