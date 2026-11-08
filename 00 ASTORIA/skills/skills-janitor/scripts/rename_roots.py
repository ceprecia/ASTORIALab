#!/usr/bin/env python3
"""rename_roots.py: rename the vault's root folders and cascade every path string that names them.

Purpose: the seven root folders are named in the vocabulary (`roots`) and in
hundreds of path strings across skills, templates, the Skill Map, the loader, and the
Obsidian settings. Renaming one by hand breaks all of them. This script
computes the new names, rewrites the strings, updates the vocabulary, and
renames the folders on disk when they exist (on a starter vault before setup
they do not exist yet, and only the strings change).

Language: Python 3, standard library only (PyYAML through skillkit when present).
Author: ASTORIA System Builder. Date: 2026-09-24.

Usage (dry run unless --apply is given):
    python3 rename_roots.py --no-emoji                  # "03 🌱 Projects" becomes "03 Projects"
    python3 rename_roots.py --no-numbers                # "03 🌱 Projects" becomes "🌱 Projects"
    python3 rename_roots.py --no-emoji --no-numbers     # "Projects"
    python3 rename_roots.py --set "projects=03 Projects" --set "areas=04 Domains"
    python3 rename_roots.py --drop inbox --drop calendar
        Marks optional roots as dropped: setup does not create them and the
        skills that mention them are listed so the user knows.
    The decoration flags apply to working roots. The system root `00 ASTORIA` stays fixed.
    Add --apply to write. Pass --vault PATH from outside the vault.

Scope of the cascade: everything under 00 ASTORIA/ except agent_notes/, plus
me.md, AGENTS.md, README.md, the Obsidian settings files, the Skills Base,
and the Skill Map. Capture logs, agent notes, and backups are never
edited.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillkit as sk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "propagate", "scripts"))
from propagate_rename import apply_changes, checked_path, validate_moves

# Toggles
TEXT_EXTENSIONS = (".md", ".py", ".base", ".json", ".yaml", ".yml", ".txt")
SKIP_UNDER_SYSTEM = ("agent_notes",)   # folders under 00 ASTORIA never edited (the layout is rebuilt instead)
EXTRA_FILES = ("me.md", "AGENTS.md", "README.md")
OBSIDIAN_FILES = ("app.json", "templates.json", "daily-notes.json", "bookmarks.json")
EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿️]")


def strip_emoji(name):
    return re.sub(r"\s{2,}", " ", EMOJI.sub("", name)).strip()


def strip_number(name):
    return re.sub(r"^\d{2}\s+", "", name).strip()


def validate_root_names(names):
    """A root is one portable folder name, never a path or executable literal."""
    for name in names.values():
        if (not name or name in {".", ".."} or name.startswith(".")
                or any(char in name for char in '/\\<>:"|?*\'`')
                or any(ord(char) < 32 for char in name) or name.endswith((".", " "))):
            raise ValueError("Root names must be simple folder names without path or quoting separators")
    if len({unicodedata.normalize("NFC", value).casefold() for value in names.values()}) != len(names):
        raise ValueError("Two roots would collide by case or Unicode spelling")


def main(argv):
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    roots = dict(vocab.get("roots") or {})
    if not roots:
        raise SystemExit("the vocabulary has no roots map")

    # Step 1: compute the new names
    new = dict(roots)
    if "--no-emoji" in argv:
        new = {role: name if role == "system" else strip_emoji(name) for role, name in new.items()}
    if "--no-numbers" in argv:
        new = {role: name if role == "system" else strip_number(name) for role, name in new.items()}
    for i, a in enumerate(argv):
        if a == "--set" and i + 1 < len(argv):
            role, _, name = argv[i + 1].partition("=")
            if role.strip() not in new:
                raise SystemExit("unknown root role %r (roles: %s)" % (role, ", ".join(roots)))
            new[role.strip()] = name.strip()
    dropped = [argv[i + 1] for i, a in enumerate(argv) if a == "--drop" and i + 1 < len(argv)]
    for role in dropped:
        if role not in roots:
            raise SystemExit("unknown root role %r" % role)
        if role not in (vocab.get("optional_roots") or []):
            raise SystemExit("root %r is not optional; only %s can be dropped" % (role, ", ".join(vocab.get("optional_roots") or [])))
    validate_root_names(new)
    if new["system"] != roots["system"]:
        raise SystemExit("the system root (00 ASTORIA) cannot be renamed; every script path depends on it")

    changes = {k: (roots[k], new[k]) for k in roots if roots[k] != new[k]}
    moves = []
    for old, target in changes.values():
        source_path, target_path = checked_path(vault, old), checked_path(vault, target)
        if os.path.lexists(target_path):
            raise ValueError("Root rename destination already exists: " + target)
        # A fresh starter has no content roots yet; reference-only changes are valid.
        if source_path.exists():
            if not source_path.is_dir():
                raise ValueError("Root rename source is not a directory: " + old)
            moves.append((old, target))
        else:
            siblings = {unicodedata.normalize("NFC", value).casefold() for value in os.listdir(vault)}
            if unicodedata.normalize("NFC", target).casefold() in siblings:
                raise ValueError("Root rename destination collides with an existing vault entry: " + target)
    validate_moves(vault, moves)
    print("Root renames:")
    for k, (old, nw) in changes.items():
        print("  %-10s %r -> %r" % (k, old, nw))
    if not changes:
        print("  none")
    if dropped:
        print("Dropped optional roots: %s" % ", ".join(dropped))

    # Step 2: collect the files in scope
    files = []
    system_dir = os.path.join(vault, roots["system"])
    for root, dirs, fs in os.walk(system_dir):
        rel = os.path.relpath(root, system_dir)
        # This operation visits only the selected system tree.
        top = rel.split(os.sep)[0]
        if rel != "." and (top in SKIP_UNDER_SYSTEM or top.startswith(".")):
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for f in fs:
            if f.endswith(TEXT_EXTENSIONS):
                files.append(os.path.join(root, f))
    for f in EXTRA_FILES:
        p = os.path.join(vault, f)
        if os.path.isfile(p):
            files.append(str(p))
    for f in OBSIDIAN_FILES:
        p = os.path.join(vault, ".obsidian", f)
        if os.path.isfile(p):
            files.append(str(p))
    extra = (vocab.get("starter") or {}).get("extra_files") or {}
    for src in extra:
        p = checked_path(vault, src)
        if os.path.isfile(p):
            files.append(str(p))

    # Step 3: rewrite the strings, longest old name first
    order = sorted(changes.values(), key=lambda pair: -len(pair[0]))
    touched = 0
    total = 0
    edits = {}
    for path in dict.fromkeys(files):
        relative = os.path.relpath(path, vault)
        checked_path(vault, relative)
        try:
            with open(path, encoding="utf-8", newline="") as source:
                text = source.read()
        except UnicodeDecodeError:
            continue
        original = text
        for old, nw in order:
            # root names are distinctive strings (number, emoji, word), so every occurrence is a path mention
            text = text.replace(old, nw)
        if "inbox" in dropped and relative == os.path.join(".obsidian", "app.json"):
            previous = json.loads(original)
            inbox_names = (roots["inbox"], new["inbox"])
            if (previous.get("newFileLocation") == "folder"
                    and previous.get("newFileFolderPath") in inbox_names):
                settings = json.loads(text)
                settings["newFileLocation"] = "root"
                settings["newFileFolderPath"] = "/"
                text = json.dumps(settings, ensure_ascii=False, indent=2) + "\n"
                print("Obsidian new notes: vault root (Inbox omitted)")
        if text != original:
            touched += 1
            total += sum(original.count(old) for old, _ in order)
            edits[relative] = text
    print("files with path strings to rewrite: %d (about %d occurrences)" % (touched, total))

    # Step 4: report skills that mention dropped roots
    for role in dropped:
        name = roots[role]
        mentions = set()
        for path in files:
            if path.startswith(os.path.join(system_dir, "skills")):
                with open(path, encoding="utf-8", errors="replace") as source:
                    if name in source.read():
                        mentions.add(os.path.relpath(path, vault).split(os.sep)[2])
        mentions = sorted(mentions)
        print("skills that mention the dropped root %r: %s" % (name, ", ".join(mentions) or "none"))

    # Step 5: prepare the vocabulary update before any filesystem mutation.
    vocab_path = os.path.join(vault, sk.VOCAB_REL)
    with open(vocab_path, encoding="utf-8", newline="") as source:
        text = edits.get(sk.VOCAB_REL, source.read())
    for k, (old, nw) in changes.items():
        text = text.replace('  %s: "%s"' % (k, old), '  %s: "%s"' % (k, nw))
    if dropped:
        dropped = sorted(set(vocab.get("dropped_roots") or []) | set(dropped))
        if "dropped_roots:" in text:
            text = re.sub(r"dropped_roots: \[[^\]]*\]", "dropped_roots: [%s]" % ", ".join(dropped), text)
        else:
            text = text.replace("\noptional_roots:", "\ndropped_roots: [%s]\noptional_roots:" % ", ".join(dropped))
    if text != Path(vocab_path).read_text(encoding="utf-8"):
        edits[sk.VOCAB_REL] = text
    if "--apply" not in argv:
        print("\ndry run; add --apply to rename")
        return 0
    # Step 6: checked moves and bounded reference writes share recovery originals.
    apply_changes(vault, edits, moves)
    for old, nw in moves:
        print("renamed folder %r -> %r" % (old, nw))
    print("vocabulary updated; run lint.py to confirm every path uses a known root")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
