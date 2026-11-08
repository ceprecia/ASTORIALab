#!/usr/bin/env python3
"""links_audit.py: count wiki-links vault-wide and list the unresolved targets.

Read-only. Skips dotfolders, runtime caches and recipient-selected exclusions.
Run from anywhere inside the vault, or pass --vault PATH. Resolve the current
me.md and task boundaries before running; this script does not infer prose rules.

Usage:
    python3 links_audit.py            # summary plus the unresolved targets
    python3 links_audit.py --files    # also the files with the most unresolved links
    python3 links_audit.py --exclude 'private/path' --exclude 'another/path'
        Exclusions are vault-relative files or folders, pruned before reading.
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict

# Pass recipient-selected protected paths with --exclude.
SKIP_DIR_NAMES = {"__pycache__", "node_modules"}
SKIP_PREFIXES = ()


def find_vault(argv):
    if "--vault" in argv:
        return os.path.abspath(argv[argv.index("--vault") + 1])
    p = os.getcwd()
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and os.path.isdir(os.path.join(p, "00 ASTORIA")):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            raise SystemExit("vault root not found (needs AGENTS.md and 00 ASTORIA); pass --vault PATH")
        p = parent


def exclusion_paths(vault, values):
    """Validate explicit vault-relative scope without reading excluded contents."""
    paths = []
    for value in values:
        path = value.replace("\\", "/")
        if (not path or path.startswith("/") or re.match(r"^[A-Za-z]:", path)
                or "\x00" in path or ".." in path.split("/")):
            raise ValueError("--exclude must be a vault-relative path without parent traversal")
        normalized = os.path.normpath(path)
        if normalized == ".":
            raise ValueError("--exclude must name a file or folder below the vault root")
        if normalized not in paths:
            paths.append(normalized)
    return paths


def within_exclusion(relative, exclusions):
    return any(relative == prefix or relative.startswith(prefix + os.sep)
               for prefix in exclusions)


def readable_path(vault, relative, exclusions):
    """Do not follow a file alias into excluded or external content."""
    resolved = os.path.relpath(os.path.realpath(os.path.join(vault, relative)),
                               os.path.realpath(vault))
    return (resolved != os.pardir and not resolved.startswith(os.pardir + os.sep)
            and not within_exclusion(relative, exclusions)
            and not within_exclusion(resolved, exclusions))


def inventory(vault, exclusions):
    """List only the represented scope; prune excluded directories before visiting."""
    stems = defaultdict(set)
    paths = set()
    notes = []
    for root, dirs, files in os.walk(vault):
        rel_root = os.path.relpath(root, vault)
        if rel_root != "." and within_exclusion(rel_root, exclusions):
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in SKIP_DIR_NAMES and not
                   within_exclusion(os.path.relpath(os.path.join(root, d), vault), exclusions)]
        for f in files:
            rel = f if rel_root == "." else os.path.join(rel_root, f)
            if not readable_path(vault, rel, exclusions):
                continue
            paths.add(rel)
            stems[os.path.splitext(f)[0]].add(rel)
            stems[f].add(rel)
            if f.endswith(".md"):
                notes.append(rel)
    return stems, paths, notes


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault")
    parser.add_argument("--files", action="store_true")
    parser.add_argument("--exclude", action="append", default=[], metavar="VAULT_RELATIVE_PATH")
    args = parser.parse_args(argv)
    vault = find_vault(["--vault", args.vault] if args.vault else [])
    try:
        explicit = exclusion_paths(vault, args.exclude)
    except ValueError as error:
        parser.error(str(error))
    exclusions = list(SKIP_PREFIXES) + explicit
    stems, paths, notes = inventory(vault, exclusions)

    # skills left in the ASTORIA repository at setup (catalog_index in the vocabulary); links to them are reported apart
    available = set()
    vocab_path = os.path.join(vault, "00 ASTORIA", "skills", "skill-builder", "assets", "vocabulary.md")
    if readable_path(vault, os.path.relpath(vocab_path, vault), exclusions) and os.path.isfile(vocab_path):
        with open(vocab_path, encoding="utf-8") as source:
            inline_catalog = re.search(r"catalog_index: \[([^\]]*)\]", source.read())
        if inline_catalog:
            available = {name.strip() for name in inline_catalog.group(1).split(",") if name.strip()}
    skills_rel = os.path.join("00 ASTORIA", "skills")
    skills_path = os.path.join(vault, skills_rel)
    installed = set(os.listdir(skills_path)) if readable_path(vault, skills_rel, exclusions) and os.path.isdir(skills_path) else set()
    not_installed = Counter()

    wiki = re.compile(r"(?<!\\)\[\[([^\]\[]+?)\]\]")
    code = re.compile(r"```.*?```|`[^`\n]*`", re.S)
    total = 0
    unresolved = Counter()
    uninspected = Counter()
    per_file = Counter()
    for n in notes:
        with open(os.path.join(vault, n), encoding="utf-8", errors="replace") as source:
            text = source.read()
        text = code.sub("", text)
        for m in wiki.finditer(text):
            target = m.group(1).split("|")[0].split("#")[0].split("^")[0].strip()
            if not target:
                continue
            total += 1
            if within_exclusion(target, exclusions) or within_exclusion(target + ".md", exclusions):
                uninspected[target] += 1
                continue
            base = os.path.basename(target)
            ok = (target in stems or target in paths or target + ".md" in paths
                  or any(p.endswith("/" + target) or p.endswith("/" + target + ".md") for p in stems.get(base, ())))
            if not ok:
                parts = target.split("/")
                if len(parts) == 4 and parts[1] == "skills" and parts[2] in available and parts[2] not in installed:
                    not_installed[parts[2]] += 1
                    continue
                unresolved[target] += 1
                per_file[n] += 1

    print("scope: %d explicit exclusions; excluded contents and links into them are unverified" % len(explicit))
    print("notes: %d  wiki-links: %d" % (len(notes), total))
    print("unresolved: %d occurrences, %d distinct targets" % (sum(unresolved.values()), len(unresolved)))
    if uninspected:
        print("unverified links into excluded scope: %d occurrences" % sum(uninspected.values()))
    if not_installed:
        print("links to %d skills not installed (available in the ASTORIA repository): %s" % (
            len(not_installed), ", ".join("%s (%d)" % (k, v) for k, v in not_installed.most_common())))
    print("\n-- unresolved targets (count) --")
    for t, c in unresolved.most_common():
        print("  %3d  [[%s]]" % (c, t))
    if args.files:
        print("\n-- files with the most unresolved --")
        for f, c in per_file.most_common(15):
            print("  %3d  %s" % (c, f))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
