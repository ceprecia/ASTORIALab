#!/usr/bin/env python3
"""finish_setup.py: verify the build and write the full AGENTS.md loader.

Purpose: the last step of setup. It checks me.md, the layout, AI log, Skill Map,
root folders and any recorded installed selection. A verified uninstalled
catalog may remain. It replaces only the exact draft AGENTS.md with the loader from
00 ASTORIA/templates/agents_loader_template.md, leaving supplied guides, notices
and user documents at their actual locations. Passing the core checks and
installing the full loader mean setup is done; a root README, tutorial and
example files are not required and their presence is not a setup-state signal.

Language: Python 3 and PyYAML for the YAML vocabulary. Native skill mounting is not a completion condition.
Author: ASTORIA System Builder. Date: 2026-09-24.

Usage:
    python3 finish_setup.py            # dry run: the checks and what would change
    python3 finish_setup.py --apply    # write the loader; leave existing documents unchanged
    Add --vault PATH from outside the vault.
"""
import os
import sys
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "skills-janitor", "scripts"))
import skillkit as sk

LOADER_TEMPLATE = os.path.join("00 ASTORIA", "templates", "agents_loader_template.md")
DRAFT_TEMPLATE = os.path.join("00 ASTORIA", "templates", "agents_draft_template.md")


def inside_vault(vault, path):
    try:
        Path(path).resolve().relative_to(Path(vault).resolve())
        return True
    except ValueError:
        return False


def main(argv):
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    roots = vocab.get("roots") or {}
    dropped = set(vocab.get("dropped_roots") or [])

    # Step 1: the checks
    problems = []
    for rel in ("me.md", os.path.join("00 ASTORIA", "agent_notes", "layout.md"), os.path.join("00 ASTORIA", "agent_notes", "ai_log.md"), sk.MAP_REL, LOADER_TEMPLATE):
        if not inside_vault(vault, os.path.join(vault, rel)):
            problems.append("required file escapes the vault: %s" % rel)
        elif not os.path.isfile(os.path.join(vault, rel)):
            problems.append("missing file: %s" % rel)
    for role, name in roots.items():
        if role not in dropped:
            path = os.path.join(vault, name)
            if not inside_vault(vault, path):
                problems.append("root folder escapes the vault: %s" % name)
            elif not os.path.isdir(path):
                problems.append("missing root folder: %s" % name)
    catalog_path = os.path.join(vault, sk.CATALOG_REL)
    catalog_present = os.path.lexists(catalog_path)
    catalog_safe = not catalog_present or (not os.path.islink(catalog_path)
                                          and os.path.isdir(catalog_path)
                                          and inside_vault(vault, catalog_path))
    if not catalog_safe:
        problems.append("uninstalled catalog is not a regular vault directory")
    selection_path = os.path.join(vault, sk.SELECTION_REL)
    if catalog_present or os.path.lexists(selection_path):
        if os.path.islink(selection_path) or not inside_vault(vault, selection_path):
            problems.append("selection record is not a regular vault file")
        elif not os.path.isfile(selection_path):
            problems.append("missing selection record: %s (apply the confirmed installer selection)" % sk.SELECTION_REL)
        elif catalog_safe:
            problems.extend("selection: " + problem for problem in sk.validate_selection(vault))
    agents_path = os.path.join(vault, "AGENTS.md")
    loader_path = os.path.join(vault, LOADER_TEMPLATE)
    draft_path = os.path.join(vault, DRAFT_TEMPLATE)
    loader = Path(loader_path).read_text(encoding="utf-8") if inside_vault(vault, loader_path) and os.path.isfile(loader_path) else None
    draft = Path(draft_path).read_text(encoding="utf-8") if inside_vault(vault, draft_path) and os.path.isfile(draft_path) else None
    current = None
    if os.path.lexists(agents_path):
        if os.path.islink(agents_path) or not os.path.isfile(agents_path) or not inside_vault(vault, agents_path):
            problems.append("AGENTS.md is not a regular vault file")
        else:
            current = Path(agents_path).read_text(encoding="utf-8")
            if current != loader and (draft is None or current != draft):
                problems.append("custom AGENTS.md would be overwritten; preserve it and review setup manually")
    agents_is_draft = draft is not None and current == draft

    print("Checks: %s" % ("all passed" if not problems else "%d problems" % len(problems)))
    for p in problems:
        print("  - %s" % p)
    print("AGENTS.md: %s" % ("draft, will be replaced" if agents_is_draft else "already the loader" if current == loader and current is not None else "custom or unsafe, preserved" if os.path.lexists(agents_path) else "missing, will be written"))
    print("Existing guides, notices and user documents: unchanged; no root guide is required")
    if problems:
        print("fix the problems above before finishing")
        return 1
    if "--apply" not in argv:
        print("\ndry run; add --apply to finish")
        return 0

    # Step 2: write the loader without changing existing documents.
    if current != loader:
        Path(agents_path).write_text(loader, encoding="utf-8")
    print("AGENTS.md is now the loader; existing documents unchanged. Setup finished.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
