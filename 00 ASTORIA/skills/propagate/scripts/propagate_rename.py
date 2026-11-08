#!/usr/bin/env python3
"""propagate_rename.py: find and rewrite every reference to a renamed skill, note, or folder path.

Purpose: after a rename, links, frontmatter values, path strings, and plain
mentions across the active vault should follow. This script finds them,
separates them from the places that must not change (history, dated capture
logs, the log section of a project MOC, backups, the archive,
recipient-protected copies and runtime settings), reports, and rewrites on --apply.

Language: Python 3, standard library only.
Author: ASTORIA Janitor System. Date: 2026-09-24.

Usage (dry run unless --apply is given):
    python3 propagate_rename.py --skill old-name=new-name
        A skill folder rename: rewrites [[00 ASTORIA/skills/old-name/SKILL|...]] links, path
        strings, `dependencies` values, and whole-word mentions; on --apply also renames the
        folder, sets the name field in SKILL.md, and rebuilds the views.
    python3 propagate_rename.py --note "Old Title=New Title" [--move]
        A note rename: rewrites [[Old Title]], [[Old Title|alias]], [[Old Title#heading]], and
        path strings ending in Old Title.md; --move also renames the file on disk.
    python3 propagate_rename.py --path "old/folder=new/folder"
        A folder path rename: rewrites every path string that starts with old/folder.
    Add --links-only to rewrite links and path strings but not plain-word mentions (use it when
    the old name is also an ordinary word), --include-archive to treat 06 🪴 Archive/ as active,
    --vault PATH from outside the vault.

Scope: links and path strings are rewritten anywhere in the active vault. Plain-word mentions
are rewritten only inside 00 ASTORIA/ (skills, maps, systems, templates); elsewhere they are
listed under "needs judgment" for the user. Files whose name carries a date (YYYY-MM-DD) are
dated records and are left alone. Outside 00 ASTORIA/ only Markdown files are read.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path, PurePosixPath

# Toggles: what never changes
PROTECTED_PREFIXES = (
    # Current public record lanes are agent_notes and the configured Calendar.
    os.path.join("00 ASTORIA", "agent_notes"),
    os.path.join("02 📅 Calendar"),
    # Add verified recipient-selected protected folder prefixes here.
)
ARCHIVE_PREFIX = "06 🪴 Archive"
SKIP_DIR_NAMES = {"__pycache__", "node_modules"}
TEXT_EXTENSIONS = (".md", ".py", ".base", ".json", ".yaml", ".yml", ".txt")
LOG_HEADING = re.compile(r"^#{1,6} .*\bLog\b.*$", re.M)   # a MOC's log section starts here
DATED_NAME = re.compile(r"\d{4}-\d{2}-\d{2}")            # a dated record, never rewritten
SYSTEM_ROOT = "00 ASTORIA"


def validated_names(kind, old, new):
    """Validate the operation before reading or changing reference consumers."""
    for value in (old, new):
        if not value or old == new or any(ord(char) < 32 for char in value):
            raise ValueError("Rename needs two different nonempty names without control characters")
        if kind == "skill":
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value) or len(value) > 64:
                raise ValueError("Skill names use lowercase letters, digits and single hyphens, at most 64 characters")
        elif kind == "note":
            if value in {".", ".."} or any(char in value for char in '/\\<>:"|?*#^[]') or value.endswith((".", " ")):
                raise ValueError("Note titles must be simple filename stems without path or link separators")
        else:
            path = PurePosixPath(value)
            if (path.is_absolute() or ".." in path.parts or str(path) == "."
                    or "\\" in value or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", value)):
                raise ValueError("Path renames must remain relative to the vault without parent traversal")


def checked_path(vault, relative):
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError("Paths must remain inside the vault: " + relative)
    current = Path(vault)
    for component in Path(relative).parts:
        current = current / component
        if current.is_symlink():
            raise ValueError("Symlink paths are outside this rename: " + relative)
    return current


def validate_moves(vault, moves):
    """All destinations must be available before any reference write occurs."""
    for source, destination in moves:
        checked_path(vault, source)
        target = checked_path(vault, destination)
        if not os.path.exists(os.path.join(vault, source)):
            raise ValueError("Rename source missing: " + source)
        siblings = {unicodedata.normalize("NFC", name).casefold()
                    for name in os.listdir(target.parent)}
        if os.path.lexists(target) or unicodedata.normalize("NFC", target.name).casefold() in siblings:
            raise ValueError("Rename destination already exists: " + destination)


def apply_changes(vault, edits, moves):
    """Keep originals outside the vault and restore bounded changes on failure."""
    validate_moves(vault, moves)
    temporary_root, vault_root = Path(tempfile.gettempdir()).resolve(), Path(vault).resolve()
    if temporary_root == vault_root or vault_root in temporary_root.parents:
        raise ValueError("Recovery originals require a temporary location outside the vault")
    backup = Path(tempfile.mkdtemp(prefix="astoria_rename_"))
    backup.chmod(0o700)
    originals = {}
    for relative in edits:
        source = checked_path(vault, relative)
        originals[relative] = source.read_bytes()
        destination = backup / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    moved, written = [], []
    def relocated(relative):
        for old, new in moves:
            if relative == old or relative.startswith(old + os.sep):
                return new + relative[len(old):]
        return relative
    try:
        validate_moves(vault, moves)
        for source, destination in moves:
            os.rename(checked_path(vault, source), checked_path(vault, destination))
            moved.append((source, destination))
        for relative, text in edits.items():
            path = checked_path(vault, relocated(relative))
            if path.read_bytes() != originals[relative]:
                raise ValueError("Reference changed after preflight: " + relative)
            with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as staged:
                temporary = Path(staged.name)
                staged.write(text.encode("utf-8"))
            try:
                shutil.copymode(path, temporary)
                os.replace(temporary, path)
            finally:
                temporary.unlink(missing_ok=True)
            written.append(relative)
    except BaseException:
        for relative in reversed(written):
            path = checked_path(vault, relocated(relative))
            if path.read_bytes() == edits[relative].encode("utf-8"):
                path.write_bytes(originals[relative])
        for source, destination in reversed(moved):
            if not os.path.lexists(os.path.join(vault, source)):
                os.rename(os.path.join(vault, destination), os.path.join(vault, source))
        print("Rename failed; recovery originals: " + str(backup))
        raise
    print("Recovery originals: " + str(backup))


def argument(argv, flag):
    if flag in argv:
        i = argv.index(flag)
        if i + 1 < len(argv):
            return argv[i + 1]
    return None


def find_vault(argv):
    given = argument(argv, "--vault")
    if given:
        return os.path.abspath(given)
    p = os.getcwd()
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and os.path.isdir(os.path.join(p, "00 ASTORIA")):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            raise SystemExit("vault root not found (needs AGENTS.md and 00 ASTORIA); pass --vault PATH")
        p = parent


def classify(rel, include_archive):
    """Return None when the file is active, else the reason it is left alone."""
    parts = rel.split(os.sep)
    if parts[0].startswith(".") or any(p in SKIP_DIR_NAMES for p in parts):
        return "generated or exported"
    for pref in PROTECTED_PREFIXES:
        if rel == pref or rel.startswith(pref + os.sep):
            return "history or dated capture log"
    if (rel == ARCHIVE_PREFIX or rel.startswith(ARCHIVE_PREFIX + os.sep)) and not include_archive:
        return "archive (frozen; --include-archive to change)"
    if DATED_NAME.search(os.path.basename(rel)):
        return "dated record"
    return None


def rules_for(argv):
    """Build the list of (regex, replacement, label) for the requested rename."""
    rules = []
    spec = argument(argv, "--skill")
    if spec:
        old, new = [x.strip() for x in spec.split("=", 1)]
        rules.append((re.compile(r"00 ASTORIA/skills/%s/" % re.escape(old)), "00 ASTORIA/skills/%s/" % new, "path or link"))
        if "--links-only" not in argv:
            rules.append((re.compile(r"(?<![\w-])%s(?![\w-])" % re.escape(old)), new, "mention"))
        return ("skill", old, new, rules)
    spec = argument(argv, "--note")
    if spec:
        old, new = [x.strip() for x in spec.split("=", 1)]
        rules.append((re.compile(r"\[\[([^\]|#]*?/)?%s(?=[\]|#])" % re.escape(old)), lambda m: "[[%s%s" % (m.group(1) or "", new), "wiki-link"))
        rules.append((re.compile(r"(?<=/)%s\.md" % re.escape(old)), new + ".md", "path string"))
        return ("note", old, new, rules)
    spec = argument(argv, "--path")
    if spec:
        old, new = [x.strip().rstrip("/") for x in spec.split("=", 1)]
        rules.append((re.compile(re.escape(old) + "(?=/|`|\"|'|$)", re.M), new, "path string"))
        return ("path", old, new, rules)
    print(__doc__)
    raise SystemExit(1)


def main(argv):
    vault = find_vault(argv)
    kind, old, new, rules = rules_for(argv)
    validated_names(kind, old, new)
    include_archive = "--include-archive" in argv
    apply = "--apply" in argv

    update, left, judgment, edits, moves = [], [], [], {}, []
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in SKIP_DIR_NAMES]
        # Hidden directories and runtime caches are pruned above.
        for f in files:
            path = os.path.join(root, f)
            rel = os.path.relpath(path, vault)
            if os.path.islink(path):
                continue
            if kind == "note" and "--move" in argv and f == old + ".md" and not classify(rel, include_archive):
                moves.append((rel, os.path.join(os.path.dirname(rel), new + ".md")))
            inside_system = rel.startswith(SYSTEM_ROOT + os.sep)
            if not f.endswith(TEXT_EXTENSIONS) or (not inside_system and not f.endswith(".md")):
                continue
            try:
                with open(path, encoding="utf-8", newline="") as source:
                    text = source.read()
            except UnicodeDecodeError:
                continue
            hits = [(label, len(rx.findall(text))) for rx, _, label in rules]
            hits = [(l, n) for l, n in hits if n]
            if not hits:
                continue
            reason = classify(rel, include_archive)
            if reason:
                left.append((rel, sum(n for _, n in hits), reason))
                continue
            # outside 00 ASTORIA, plain mentions are a question for the user, not an edit
            file_rules = rules if inside_system else [r for r in rules if r[2] != "mention"]
            if not inside_system:
                n_mentions = sum(n for l, n in hits if l == "mention")
                if n_mentions:
                    judgment.append((rel, "%d plain mention(s) of %r outside 00 ASTORIA" % (n_mentions, old)))
                hits = [(l, n) for l, n in hits if l != "mention"]
                if not hits:
                    continue
            # a project or area MOC: only the part above its log heading is active
            head, tail = text, ""
            if re.search(r"\bMOC\b", f, re.I) and LOG_HEADING.search(text):
                i = LOG_HEADING.search(text).start()
                head, tail = text[:i], text[i:]
                log_hits = sum(len(rx.findall(tail)) for rx, _, _ in rules)
                if log_hits:
                    left.append((rel + " (Research Log section)", log_hits, "history"))
            new_head = head
            for rx, repl, _ in file_rules:
                new_head = rx.sub(repl, new_head)
            if new_head == head:
                continue
            update.append((rel, ", ".join("%s x%d" % (l, n) for l, n in hits)))
            edits[rel] = new_head + tail

    if kind == "skill":
        source = os.path.join("00 ASTORIA", "skills", old)
        destination = os.path.join("00 ASTORIA", "skills", new)
        source_path, destination_path = checked_path(vault, source), checked_path(vault, destination)
        if source_path.is_dir():
            moves.append((source, destination))
            skill_relative = os.path.join(source, "SKILL.md")
        elif destination_path.is_dir() and not source_path.exists():
            skill_relative = os.path.join(destination, "SKILL.md")
        else:
            raise ValueError("Neither the existing nor already-renamed skill folder exists")
        skill_path = checked_path(vault, skill_relative)
        if not skill_path.is_file():
            raise ValueError("Renamed skill must contain SKILL.md")
        text = edits.get(skill_relative, skill_path.read_text(encoding="utf-8"))
        edits[skill_relative] = re.sub(r"^name: %s$" % re.escape(old), "name: %s" % new, text, count=1, flags=re.M)
    if kind == "note" and "--move" in argv and not moves:
        raise ValueError("No active, unprotected note with this title is available to move")
    validate_moves(vault, moves)

    print("Propagate (rename): %s -> %s  [%s]" % (old, new, kind))
    print("\nUpdate (%d files):" % len(update))
    for rel, what in update:
        print("  - %s: %s" % (rel, what))
    print("\nLeft alone (%d files):" % len(left))
    for rel, n, reason in left:
        print("  - %s: %d occurrences, %s" % (rel, n, reason))
    if judgment:
        print("\nNeeds judgment (%d files):" % len(judgment))
        for rel, what in judgment:
            print("  - %s: %s" % (rel, what))

    if not apply:
        print("\ndry run; add --apply to rewrite")
        return 0

    apply_changes(vault, edits, moves)
    # Regenerate the views only after the requested rename succeeds.
    if kind == "skill":
        scripts = os.path.join(vault, "00 ASTORIA", "skills", "skills-janitor", "scripts")
        subprocess.run([sys.executable, os.path.join(scripts, "build_views.py"), "--vault", vault], check=True)
        print("views rebuilt; run lint.py next")
    elif kind == "note" and "--move" in argv:
        for unused_source, destination in moves:
            print("renamed file " + destination)
    print("done; verify with the links audit")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
