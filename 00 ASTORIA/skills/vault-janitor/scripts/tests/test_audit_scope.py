"""Verify explicit audit boundaries are pruned before inventory or note reads."""
import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import links_audit


class AuditScopeChecks(unittest.TestCase):
    def test_invalid_or_escaping_exclusions_are_rejected(self):
        for path in ['', '.', '..', '../private', 'a/../../private', '/private',
                     'C:\\private', '\\\\server\\private', 'private\x00']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                links_audit.exclusion_paths('/vault', [path])

    def test_exclusion_does_not_hide_a_similar_sibling(self):
        self.assertTrue(links_audit.within_exclusion('private/note.md', ['private']))
        self.assertFalse(links_audit.within_exclusion('private_notes/note.md', ['private']))

    def test_private_subtree_is_neither_visited_nor_read(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / '00 ASTORIA/skills').mkdir(parents=True)
            (root / 'private/nested').mkdir(parents=True)
            (root / 'private/nested/secret.md').write_text('[[secret_missing]]')
            (root / 'private_notes').mkdir()
            (root / 'private_notes/public.md').write_text('[[public_missing]] [[private/nested/secret]]')
            (root / 'single.md').write_text('[[single_missing]]')
            (root / 'alias.md').symlink_to(root / 'private/nested/secret.md')
            visited, opened = [], []
            real_walk, real_open = os.walk, open
            def track_walk(*args, **kwargs):
                for item in real_walk(*args, **kwargs):
                    visited.append(Path(item[0]).relative_to(root).as_posix())
                    yield item
            def track_open(path, *args, **kwargs):
                candidate = Path(path)
                opened.append(candidate.relative_to(root).as_posix())
                if candidate == root / 'single.md' or root / 'private' in candidate.parents:
                    raise AssertionError('Excluded content was read')
                return real_open(path, *args, **kwargs)
            output = io.StringIO()
            with patch.object(links_audit.os, 'walk', track_walk), \
                 patch('builtins.open', track_open), contextlib.redirect_stdout(output):
                result = links_audit.main(['--vault', temp, '--exclude', 'private', '--exclude', 'single.md'])
            self.assertEqual(result, 0)
            self.assertNotIn('private', visited)
            self.assertNotIn('private/nested', visited)
            self.assertNotIn('alias.md', opened)
            self.assertIn('private_notes/public.md', opened)
            self.assertIn('public_missing', output.getvalue())
            self.assertNotIn('secret_missing', output.getvalue())
            self.assertNotIn('single_missing', output.getvalue())
            self.assertIn('unverified links into excluded scope: 1', output.getvalue())


if __name__ == '__main__':
    unittest.main()
