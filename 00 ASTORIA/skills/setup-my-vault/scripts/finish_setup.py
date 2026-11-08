#!/usr/bin/env python3
"""finish_setup.py: verify the build and write the full AGENTS.md loader, retaining README.md.

Purpose: the last step of setup Stage 4. It checks that me.md, the layout reference, the AI log,
the Skill Map, and the root folders exist and that the specialized-skills
catalog is gone, replaces the draft AGENTS.md with the loader from
00 ASTORIA/templates/agents_loader_template.md, and retains README.md as the
participant guide. Passing the core checks and installing the full loader
mean setup is done; README presence is not a setup-state signal.

Language: Python 3 and PyYAML for the YAML vocabulary. Native skill mounting is not a completion condition.
Author: ASTORIA System Builder. Date: 2026-09-24.

Usage:
    python3 finish_setup.py            # dry run: the checks and what would change
    python3 finish_setup.py --apply    # write the loader and retain the README
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
    if os.path.isdir(os.path.join(vault, sk.CATALOG_REL)):
        problems.append("catalog still present: %s (run install_specialized.py with --remove-catalog)" % sk.CATALOG_REL)
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
    print("README.md: preserved; it is the participant guide, not setup state")
    if problems:
        print("fix the problems above before finishing")
        return 1
    if "--apply" not in argv:
        print("\ndry run; add --apply to finish")
        return 0

    # Step 2: write the loader without changing the participant guide.
    if current != loader:
        Path(agents_path).write_text(loader, encoding="utf-8")
    print("AGENTS.md is now the loader; README.md retained. Setup finished.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
