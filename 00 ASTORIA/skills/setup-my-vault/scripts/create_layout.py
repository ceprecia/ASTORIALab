#!/usr/bin/env python3
"""create_layout.py: create the vault's root folders and their subfolders from the vocabulary.

Purpose: a starter vault ships only 00 ASTORIA/. Setup Stage 4 runs this script
to create the other roots (`roots` in the vocabulary, minus `dropped_roots`)
and the subfolders listed under `layout`. Existing folders are left alone.

Language: Python 3 and PyYAML for the YAML vocabulary.
Author: ASTORIA System Builder. Date: 2026-09-24.

Usage:
    python3 create_layout.py            # dry run: what would be created
    python3 create_layout.py --apply    # create
    Add --vault PATH from outside the vault.
"""
import os
import sys
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "skills-janitor", "scripts"))
import skillkit as sk


def layout_path(vault, relative):
    """Configured folders stay inside this vault, including resolved symlinks."""
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("invalid layout folder: %r" % relative)
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("layout folder must be vault-relative: %s" % relative)
    root = Path(vault).resolve()
    path = root / rel
    try:
        path.resolve().relative_to(root)
    except ValueError:
        raise ValueError("layout folder escapes the vault: %s" % relative)
    if path.exists() and not path.is_dir():
        raise ValueError("layout folder conflicts with a file: %s" % relative)
    return path


def main(argv):
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    roots = vocab.get("roots") or {}
    dropped = set(vocab.get("dropped_roots") or [])
    layout = vocab.get("layout") or {}
    if not roots:
        raise SystemExit("the vocabulary has no roots map")

    # Step 1: the list of folders to create, roots first, then subfolders
    wanted = []
    for role, name in roots.items():
        if role in dropped:
            continue
        if not isinstance(name, str) or not name:
            print("invalid root folder: %r" % name)
            return 1
        wanted.append(name)
        for sub in layout.get(role, []):
            if not isinstance(sub, str) or Path(sub).is_absolute() or ".." in Path(sub).parts:
                print("invalid layout subfolder: %r" % sub)
                return 1
            wanted.append(os.path.join(name, sub))

    # Validate the whole plan before creating even the first folder.
    try:
        destinations = [(rel, layout_path(vault, rel)) for rel in wanted]
    except (ValueError, TypeError) as error:
        print(error)
        return 1

    # Step 2: create what is missing
    created, existing = [], []
    for rel, path in destinations:
        if os.path.isdir(path):
            existing.append(rel)
        else:
            created.append(rel)
            if "--apply" in argv:
                os.makedirs(path, exist_ok=True)

    verb = "created" if "--apply" in argv else "would create"
    print("%s %d folders, %d already existed" % (verb, len(created), len(existing)))
    for rel in created:
        print("  + %s" % rel)
    if dropped:
        print("dropped roots skipped: %s" % ", ".join(roots[r] for r in dropped if r in roots))
    if "--apply" not in argv:
        print("\ndry run; add --apply to create")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
