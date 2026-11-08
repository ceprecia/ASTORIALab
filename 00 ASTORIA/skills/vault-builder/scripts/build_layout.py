#!/usr/bin/env python3
"""build_layout.py: write 00 ASTORIA/agent_notes/layout.md from the vocabulary and the disk.

Purpose: the layout reference is the one place an agent checks before placing
or naming a file. It has four generated tables and one rules block:
  Folders   every root and its documented subfolders, with a purpose line
            (from `purposes` in the vocabulary; a folder on disk with no line
            is listed with an empty purpose and reported, except flexible Resources collections)
  Files     kind of file, location, name pattern, template, owner skill
            (from `note_types` in the vocabulary; rows whose owner skill is
            not installed are skipped and reported)
  Templates every file in 00 ASTORIA/templates/ with its purpose
            (from `template_purposes`; unknown files are reported)
  Rules     `layout_rules` from the vocabulary, restating me.md
  Active projects and areas   the selected direct owning MOC in each project
            or Area folder, with the newest dated log heading

Automated output is rebuilt from the vocabulary. Manual first setup without
Python uses the narrow bootstrap exception in vault-builder/SKILL.md.

Language: Python 3 with PyYAML for the YAML configuration.
Author: ASTORIA System Builder.
Date: 2026-09-25.

Usage:
    python3 build_layout.py            # print the report and the diff summary, write nothing
    python3 build_layout.py --apply    # write 00 ASTORIA/agent_notes/layout.md
    python3 build_layout.py --check    # exit 1 when the file on disk differs from a fresh build (janitor use)
    Use --vault PATH when running outside the vault.
    Exit 2 means a project or area folder could not be inspected. The report
    covers accessible folders and the layout is preserved.
"""
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "skills-janitor", "scripts"))
import skillkit as sk

OUT_REL = os.path.join("00 ASTORIA", "agent_notes", "layout.md")
SKIP_DIRS = {".obsidian", ".trash", ".git", ".agents", ".claude", "__pycache__"}
DATE_HEADING = re.compile(r"^#{2,4}\s+(\d{4}-\d{2}-\d{2})", re.M)
# Spaces, punctuation, and underscores delimit the conventional MOC token.
MOC_RE = re.compile(r"(?:^|[\W_])MOC(?:$|[\W_])", re.I)
MOC_FRONTMATTER_LIMIT = 65536


def moc_role(path):
    """Inspect the direct role key in the first bounded YAML header."""
    name = os.path.basename(path)
    try:
        with open(path, "rb") as source:
            opener = source.readline(8)
            if opener not in (b"---\n", b"---\r\n",
                              b"\xef\xbb\xbf---\n", b"\xef\xbb\xbf---\r\n"):
                return None
            header = bytearray()
            while True:
                remaining = MOC_FRONTMATTER_LIMIT - len(header)
                line = source.readline(remaining + 1)
                if not line or len(line) > remaining:
                    raise ValueError("unclosed or oversized YAML frontmatter in %s" % name)
                if line in (b"---\n", b"---\r\n", b"---"):
                    break
                header.extend(line)
    except OSError as error:
        raise ValueError("could not read map role in %s" % name) from error

    yaml = sk.yaml
    try:
        document = yaml.compose(header.decode("utf-8"), Loader=yaml.SafeLoader)
    except RecursionError as error:
        raise ValueError("YAML frontmatter nesting is too deep in %s" % name) from error
    except (UnicodeError, yaml.YAMLError) as error:
        raise ValueError("invalid YAML frontmatter in %s" % name) from error
    if document is None:
        return None
    if not isinstance(document, yaml.MappingNode):
        raise ValueError("expected a YAML frontmatter mapping in %s" % name)
    roles = [(key, value) for key, value in document.value
             if isinstance(key, yaml.ScalarNode) and key.value == "astoria_role"]
    if not roles:
        return None
    if len(roles) == 1:
        key, value = roles[0]
        string_tag = "tag:yaml.org,2002:str"
        if (key.tag == string_tag and isinstance(value, yaml.ScalarNode)
                and value.tag == string_tag and value.value in ("project_moc", "area_moc")):
            return value.value
    raise ValueError("invalid or duplicate astoria_role property in %s" %
                     os.path.basename(path))


def map_folder_entries(folder):
    """List a folder after verifying its entries are reachable."""
    # Listing alone can succeed when the directory cannot be searched.
    os.stat(os.path.join(folder, "."))
    return sorted(os.listdir(folder))


def owning_moc(folder, owner, kind, report):
    """Choose a direct owning note under the role's verified convention."""
    files = [name for name in map_folder_entries(folder)
             if name.endswith(".md") and not name.startswith(".")
             and not os.path.islink(os.path.join(folder, name))
             and os.path.isfile(os.path.join(folder, name))]
    try:
        roles = {name: moc_role(os.path.join(folder, name)) for name in files}
    except ValueError as error:
        report.append("%s %r: %s" % (kind, owner, error))
        return None
    marked = [name for name in files if roles[name] == kind + "_moc"]
    if marked:
        if len(marked) == 1:
            return marked[0]
        report.append("%s %r has multiple explicit %s MOCs: %s" %
                      (kind, owner, kind, ", ".join(marked)))
        return None
    if kind == "area":
        familiar = "%s MOC.md" % owner
        if familiar in roles:
            if roles[familiar] is None:
                return familiar
            report.append("area %r: conventional MOC has a different explicit role: %s" %
                          (owner, familiar))
        else:
            report.append("area %r has no verified owning MOC" % owner)
        return None
    familiar = "MOC %s.md" % owner
    legacy = [name for name in files if roles[name] is None and MOC_RE.search(name)]
    if familiar in legacy:
        return familiar
    if len(legacy) == 1:
        return legacy[0]
    if legacy:
        report.append("project %r has ambiguous MOC filenames: %s" %
                      (owner, ", ".join(legacy)))
    return None


def cell(s):
    return str(s or "").replace("|", "\\|").strip()


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(cell(c) for c in r) + " |")
    return out


def subfolders(path):
    """First-level folders under path, sorted, skipping dotfolders."""
    if not os.path.isdir(path):
        return []
    out = []
    for n in sorted(os.listdir(path)):
        p = os.path.join(path, n)
        if os.path.isdir(p) and n not in SKIP_DIRS and not n.startswith("."):
            out.append(n)
    return out


def newest_date(path):
    with open(path, encoding="utf-8") as source:
        dates = DATE_HEADING.findall(source.read())
    return max(dates, default="")


def build(vault, vocab, installed, *, folder_errors=None):
    if folder_errors is None:
        folder_errors = []
    roots = vocab.get("roots") or {}
    dropped = set(vocab.get("dropped_roots") or [])
    layout = vocab.get("layout") or {}
    purposes = vocab.get("purposes") or {}
    report = []

    # Folders: every root that exists, its vocabulary subfolders, then anything else one level down
    rows = []
    for role, name in roots.items():
        if role in dropped:
            continue
        root = os.path.join(vault, name)
        if not os.path.isdir(root):
            report.append("root missing on disk: %s" % name)
            continue
        rows.append(("`%s/`" % name, purposes.get(name, ""), ""))
        if not purposes.get(name):
            report.append("no purpose line for %s" % name)
        # Verify the human-owned Inbox root without inventorying its contents.
        if role == "inbox":
            continue
        listed = []
        for sub in layout.get(role, []):
            rel = os.path.join(name, sub)
            listed.append(sub.split("/")[0])
            if os.path.isdir(os.path.join(vault, rel)):
                rows.append(("`%s/`" % rel, purposes.get(rel, ""), "vocabulary"))
            else:
                report.append("vocabulary subfolder missing on disk: %s" % rel)
        if role in ("projects", "areas"):
            continue   # their folders are the Active projects and areas table
        for sub in subfolders(root):
            if sub in listed:
                continue
            rel = os.path.join(name, sub)
            purpose = purposes.get(rel) or ("Reference collection." if role == "resources" else "")
            rows.append(("`%s/`" % rel, purpose, ""))
            if not purpose:
                report.append("folder on disk with no purpose line: %s" % rel)
    folder_rows = [(f, p) for f, p, _ in rows]

    # Files: note types whose owner skills are installed
    file_rows = []
    for nt in vocab.get("note_types") or []:
        owners = [o.strip() for o in str(nt.get("owner") or "").split(",") if o.strip()]
        missing = [o for o in owners if o not in installed]
        if missing:
            report.append("note type %r skipped: owner skill not installed (%s)" % (nt.get("kind"), ", ".join(missing)))
            continue
        tpl = nt.get("template") or ""
        if tpl and not os.path.exists(os.path.join(vault, "00 ASTORIA", "templates", tpl)):
            report.append("note type %r names a template that does not exist: %s" % (nt.get("kind"), tpl))
        loc = str(nt.get("location", ""))
        loc_cell = "`%s`" % loc if re.match(r"^\d\d ", loc) else loc   # a path gets backticks, a description stays prose
        file_rows.append((nt.get("kind", ""), loc_cell, "`%s`" % tpl if tpl else "none",
                          ", ".join("`%s`" % o for o in owners) or ""))   # names, not links: a pipe inside a table cell breaks link parsers

    # Templates on disk
    tdir = os.path.join(vault, "00 ASTORIA", "templates")
    tpurp = vocab.get("template_purposes") or {}
    template_rows = []
    if os.path.isdir(tdir):
        for n in sorted(os.listdir(tdir)):
            if not n.endswith(".md"):
                continue
            template_rows.append(("`%s`" % n, tpurp.get(n, "")))
            if n not in tpurp:
                report.append("template with no purpose line: %s" % n)

    # Active projects and areas
    proj_rows = []
    for role in ("projects", "areas"):
        name = roots.get(role)
        if not name or role in dropped:
            continue
        root = os.path.join(vault, name)
        if os.path.islink(root) or not os.path.isdir(root):
            continue
        kind = "project" if role == "projects" else "area"
        try:
            entries = map_folder_entries(root)
        except OSError as error:
            folder_errors.append("could not inspect %s root %r: %s" %
                                 (kind, name, error.strerror or type(error).__name__))
            continue
        for entry in entries:
            p = os.path.join(root, entry)
            if entry.startswith(".") or entry in SKIP_DIRS or os.path.islink(p):
                continue
            if os.path.isdir(p):
                try:
                    selected = owning_moc(p, entry, kind, report)
                except OSError as error:
                    folder_errors.append("could not inspect %s folder %r: %s" %
                                         (kind, os.path.join(name, entry),
                                          error.strerror or type(error).__name__))
                    continue
                if selected is None:
                    continue
                owner = entry
                rel = os.path.join(name, entry, selected)
            elif role == "projects" and entry.endswith(".md") and MOC_RE.search(entry) and os.path.isfile(p):
                owner = entry[:-3]
                rel = os.path.join(name, entry)
            else:
                continue
            try:
                date = newest_date(os.path.join(vault, rel))
            except (OSError, UnicodeError):
                report.append("%s %r: could not read owning MOC %r" % (kind, owner, rel))
                continue
            proj_rows.append((owner, "`%s`" % rel, date or "no dated entry"))

    today = datetime.date.today().isoformat()
    lines = ["---", "related:", '  - "[[Skill Map]]"', "created: %s" % today, "---", "",
             "> [!NOTE] Generated by `00 ASTORIA/skills/vault-builder/scripts/build_layout.py` from the vocabulary and the folder tree. Do not edit by hand: change `purposes`, `note_types`, `template_purposes`, or `layout_rules` in `00 ASTORIA/skills/skill-builder/assets/vocabulary.md` and rebuild. Check this file before placing, naming, or moving a file.",
             "", "# Layout", "", "## Folders", ""]
    lines += table(["Folder", "Purpose"], folder_rows)
    lines += ["", "## Files", "", "Where each kind of file goes, what it is called, which template starts it, and which skill owns the format.", ""]
    lines += table(["Kind of file", "Location and name pattern", "Template", "Owner"], file_rows)
    lines += ["", "## Templates", ""]
    lines += table(["Template", "Purpose"], template_rows)
    lines += ["", "## Rules", "", "Restated from `me.md`, which stays the authority.", ""]
    for r in vocab.get("layout_rules") or []:
        lines.append("- %s" % r)
    lines += ["", "## Active projects and areas", "", "Verified project and Area MOCs, with the date of each newest dated heading. In each project or Area folder, the matching explicit role selects one direct note before the verified filename fallback. Follow the recipient's approved, applicable MOC reading policy in `me.md` within the current task scope. If no applicable policy governs the reading sequence, use the opening section and heading outline to orient, then read only the recent log entries and sections needed for the task.", ""]
    lines += table(["Project or area", "MOC", "Newest dated entry"], proj_rows)
    lines += ["", "Built %s." % today, ""]
    return "\n".join(lines), report + folder_errors


def comparison_text(text):
    """Ignore this generator's dates while retaining dated project facts and rules."""
    frontmatter = re.match(r"\A---\n.*?\n---(?=\n|$)", text, re.S)
    if frontmatter:
        original = frontmatter.group(0)
        normalized = re.sub(r"(?m)^created: *[\"']?\d{4}-\d{2}-\d{2}[\"']? *$",
                            "created: BUILD_DATE", original)
        text = normalized + text[len(original):]
    return re.sub(r"(?m)^Built \d{4}-\d{2}-\d{2}\.(?=\s*\Z)",
                  "Built BUILD_DATE.", text)


def main(argv):
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    installed = set(sk.load_skills(vault).keys()) if hasattr(sk, "load_skills") else set()
    folder_errors = []
    text, report = build(vault, vocab, installed, folder_errors=folder_errors)
    for r in report:
        print("  " + r)
    if folder_errors:
        print("layout: incomplete inspection; refresh and freshness check require folder access")
        return 2
    out = os.path.join(vault, OUT_REL)
    current = open(out, encoding="utf-8").read() if os.path.exists(out) else ""
    same = bool(current) and comparison_text(current) == comparison_text(text)
    print("layout: %d report lines; file %s" % (len(report), "unchanged" if same else ("differs from a fresh build" if current else "does not exist yet")))
    if "--check" in argv:
        return 0 if same else 1
    if "--apply" in argv:
        if same:
            return 0
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
        print("wrote " + OUT_REL)
    else:
        print("dry run; add --apply to write " + OUT_REL)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
