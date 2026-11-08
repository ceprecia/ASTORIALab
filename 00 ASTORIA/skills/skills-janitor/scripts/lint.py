#!/usr/bin/env python3
"""lint.py: read-only audit of every skill folder against the skill-builder schema.

Usage: python3 lint.py [--vault PATH] [--json] [--assume-notes "me"]
Prints a report to stdout and exits 1 when any error is found. Never edits.

Checks the live set in 00 ASTORIA/skills/ and, when the folder exists, the
catalog in 00 ASTORIA/specialized_skills/ (also retained after manual core setup). The
catalog gets the same per-skill checks, its dependencies may resolve into
either set, and it is exempt from the map and catalog parity checks.
--assume-notes lists note stems that do not exist yet but will (a starter
vault before setup has no me.md); links to them are not errors.
"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillkit as sk
import build_views as views

STRAY = ["CLAUDE.md", "CLAUDE.local.md", "codex.md", "AGENTS.override.md", "AGENTS.local.md", "GEMINI.md"]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKI = re.compile(r"(?<!\\)\[\[([^\]\[]+?)\]\]")
MDLINK = re.compile(r"\]\((\./[^)\s]+)\)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
H2 = re.compile(r"^## (.+)$", re.M)
FOOTER = re.compile(r"^(?:Back to \[\[|End of )", re.M)
# A path string in backticks that starts with a numbered root folder, e.g. `03 🌱 Projects/x`.
ROOTPATH = re.compile(r"`(\d{2} [^`/\n]+)/")


def owner_names(vocab):
    """The person's names, read from the starter replacements that turn them into "the user"."""
    reps = (vocab.get("starter") or {}).get("replacements") or {}
    return [k for k, v in reps.items() if str(v).strip().lower() == "the user" and re.fullmatch(r"[A-Z][\w-]*", k)]


def check_skill(name, s, vocab, all_skills, stems, paths, assumed, E, W, all_phrases, root_names, catalog_names=(), pending=None):
    """Per-skill checks shared by the live set and the catalog."""
    maxlen = int(vocab.get("description_max_chars", 1000))
    levels, systems = vocab["levels"], vocab["systems"]
    families, mods, pops = vocab["families"], set(vocab["modalities"]), set(vocab["populations"])
    counts = vocab["trigger_counts"]
    if "__error__" in s.fm:
        E(name, "frontmatter error: %s" % s.fm["__error__"]); return
    if s.fm.get("name") != name:
        E(name, "name field %r does not match folder" % s.fm.get("name"))
    if not NAME_RE.match(name) or len(name) > 64:
        E(name, "folder name breaks the standard (lowercase, digits, single hyphens, 64 max)")
    extra = set(s.fm) - sk.ALLOWED_TOP
    if extra:
        E(name, "frontmatter keys outside the standard: %s" % ", ".join(sorted(extra)))
    if not s.description:
        E(name, "description is empty")
    elif len(s.description) > maxlen:
        E(name, "description is %d characters (max %d)" % (len(s.description), maxlen))
    if s.description.count("Triggers:") > 1:
        E(name, "more than one Triggers: sentence")
    if not s.meta:
        E(name, "metadata block missing"); return
    lvl = s.level
    if lvl not in levels:
        E(name, "metadata.level %r not in vocabulary" % lvl)
    if s.system not in systems:
        E(name, "metadata.system %r not in vocabulary" % s.system)
    for k in ("created", "updated"):
        v = s.meta.get(k, "")
        if v and not DATE_RE.match(v):
            E(name, "metadata.%s %r is not YYYY-MM-DD" % (k, v))
    for d in s.dependencies:
        if d not in all_skills:
            E(name, "dependency %r is not a skill" % d)
    research = s.system == "Research Assistant System" and lvl in ("skill", "coordinator")
    if research:
        if s.part and s.part not in vocab["parts"]:
            E(name, "metadata.part %r not in vocabulary" % s.part)
        if s.family and s.family not in families:
            E(name, "metadata.family %r not in vocabulary" % s.family)
        if s.part and not s.family:
            E(name, "part skill without metadata.family")
        for m in [x.strip() for x in s.meta.get("modality", "").split(",") if x.strip()]:
            if m not in mods:
                E(name, "metadata.modality %r not in vocabulary" % m)
        for pth in [x.strip() for x in s.meta.get("population", "").split(",") if x.strip()]:
            if pth not in pops:
                E(name, "metadata.population %r not in vocabulary" % pth)
    trig = s.triggers
    lo, hi = counts.get(lvl, [0, 5])
    if len(trig) < lo:
        E(name, "%d trigger phrases, level %s needs at least %d" % (len(trig), lvl, lo))
    if len(trig) > hi:
        E(name, "%d trigger phrases, level %s allows at most %d" % (len(trig), lvl, hi))
    spaced = name.replace("-", " ")
    for t in trig:
        tl = t.lower()
        if tl in (name, spaced) or tl.startswith("run " + name) or tl.startswith("run " + spaced):
            E(name, "trigger %r is the skill's own name" % t)
        words = len(t.split())
        if words < 2 or words > 8:
            W(name, "trigger %r has %d words (aim for 2 to 6)" % (t, words))
        if re.search(r"[;:!?]", t):
            W(name, "trigger %r contains punctuation" % t)
        all_phrases.append((tl, name))
    if s.lines > 500:
        W(name, "SKILL.md is %d lines (guideline 500); move depth to references/" % s.lines)
    text = CODE.sub("", s.body)
    # body sections: retired skeleton names come back as warnings, footers as errors, References stays last
    sections = vocab.get("sections") or {}
    retired = {str(x).strip().lower() for x in (sections.get("retired") or [])}
    h2 = [h.strip() for h in H2.findall(text)]
    back = [h for h in h2 if h.lower() in retired]
    if back:
        W(name, "retired section name(s): %s; use the canonical set in the vocabulary" % ", ".join(back))
    if h2 and "References" in h2 and h2[-1] != "References" and not h2[-1].lower().startswith("appendix"):
        W(name, "References is not the last section (%s follows it)" % h2[-1])
    if FOOTER.search(text):
        E(name, "footer line (Back to / End of) is not allowed")
    owners = owner_names(vocab)
    if owners:
        hits = sorted({m.group(0) for m in re.finditer(r"\b(?:%s)\b" % "|".join(map(re.escape, owners)), s.text)})
        if hits:
            W(name, "names the person (%s); say \"the user\" and keep the name in me.md" % ", ".join(hits))
    for m in WIKI.finditer(text):
        tgt = m.group(1).split("|")[0].split("#")[0].split("^")[0].strip()
        if not tgt or tgt in assumed:
            continue
        ok = (tgt in stems) or (tgt in paths) or (tgt + ".md" in paths) \
            or any(p.endswith("/" + tgt) or p.endswith("/" + tgt + ".md") for p in stems.get(os.path.basename(tgt), []))
        if not ok and catalog_names:
            # a link to 00 ASTORIA/skills/<name>/SKILL where <name> is still in the catalog resolves after installation
            parts = tgt.split("/")
            if len(parts) == 4 and parts[0] == "00 ASTORIA" and parts[1] == "skills" and parts[2] in catalog_names:
                pending.add(parts[2]); ok = True
        if not ok:
            E(name, "unresolved link [[%s]]" % tgt)
    for m in MDLINK.finditer(text):
        rel = m.group(1)[2:].split("#")[0]
        if not os.path.exists(os.path.join(s.vault, s.folder, rel)):
            E(name, "relative link %s does not exist" % m.group(1))
    # every numbered root path in the skill's files must start with a known root
    if root_names:
        for fpath in s.text_files():
            ftext = open(fpath, encoding="utf-8", errors="replace").read()
            for m in ROOTPATH.finditer(ftext):
                if m.group(1) not in root_names:
                    E(name, "%s uses an unknown root folder %r" % (os.path.relpath(fpath, os.path.join(s.vault, s.folder)), m.group(1)))
                    break
    refs = os.path.join(s.vault, s.folder, "references")
    if os.path.isdir(refs):
        for r in os.listdir(refs):
            if os.path.isdir(os.path.join(refs, r)):
                W(name, "references/%s is a folder; keep references one level deep" % r)


def main(argv):
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    skills = sk.load_skills(vault)
    catalog = sk.load_skills(vault, sk.CATALOG_REL) if os.path.isdir(os.path.join(vault, sk.CATALOG_REL)) else {}
    assumed = set()
    if "--assume-notes" in argv:
        assumed = {x.strip() for x in argv[argv.index("--assume-notes") + 1].split(",") if x.strip()}
    errors, warnings = [], []
    E = lambda s, m: errors.append((s, m))
    W = lambda s, m: warnings.append((s, m))
    root_names = set(str(v) for v in (vocab.get("roots") or {}).values())

    # stray files in the skills roots and folders without SKILL.md
    for rel in ([sk.SKILLS_REL] + ([sk.CATALOG_REL] if catalog else [])):
        root = os.path.join(vault, rel)
        for entry in sorted(os.listdir(root)):
            p = os.path.join(root, entry)
            if os.path.isfile(p) and entry.endswith(".md"):
                E(entry, "single-file skill in %s; skills are folders with SKILL.md" % rel)
            elif os.path.isdir(p) and not os.path.isfile(os.path.join(p, "SKILL.md")) and not entry.startswith("."):
                E(entry, "folder has no SKILL.md")
    for name in catalog:
        if name in skills:
            E(name, "present in both the live set and the catalog")

    # note stems for link resolution
    stems, paths = {}, set()
    for abs_p, rel in sk.walk_notes(vault):
        paths.add(rel.replace(os.sep, "/"))
        stems.setdefault(os.path.splitext(os.path.basename(rel))[0], []).append(rel.replace(os.sep, "/"))

    all_skills = dict(skills); all_skills.update(catalog)
    # names that resolve after installation: the catalog folder, plus the catalog index the exporter
    # writes into the vocabulary (skills left in the ASTORIA repository after setup)
    available = set(catalog) | (set((vocab.get("starter") or {}).get("catalog_index") or []) - set(skills))
    all_phrases = []
    pending = set()
    for name, s in skills.items():
        check_skill(name, s, vocab, all_skills, stems, paths, assumed, E, W, all_phrases, root_names, available, pending)
    for name, s in catalog.items():
        check_skill(name, s, vocab, all_skills, stems, paths, assumed, E, W, all_phrases, root_names, available, pending)

    # overlaps across all skills (exact or containment, case-insensitive)
    seen = set()
    for i, (a, sa) in enumerate(all_phrases):
        for b, sb in all_phrases[i + 1:]:
            if sa == sb:
                continue
            if a == b or a in b or b in a:
                key = tuple(sorted([(a, sa), (b, sb)]))
                if key in seen:
                    continue
                seen.add(key)
                E("%s / %s" % (sa, sb), "trigger overlap: %r and %r" % (a, b))

    # view parity for the live set only
    map_path = os.path.join(vault, sk.MAP_REL)
    map_text = open(map_path, encoding="utf-8").read() if os.path.isfile(map_path) else ""
    coords = vocab.get("part_coordinators", {})
    skills_root = os.path.join(vault, sk.SKILLS_REL)
    portable = sk.PortableLinks(vault) if sk.portable_links_enabled(vocab) else None

    def view_link(skill, document):
        return portable.rewrite(skill.link(), document) if portable else skill.link()

    for name, s in skills.items():
        if "__error__" in s.fm:
            continue
        if view_link(s, sk.MAP_REL) not in map_text:
            E(name, "missing from the Skill Map registry (run build_views.py)")
        if s.system == "Research Assistant System" and s.part and s.family != "part-coordinator":
            r = coords.get(s.part)
            rp = os.path.join(skills_root, r or "", "SKILL.md") if r else None
            if not rp or not os.path.isfile(rp):
                E(name, "part %s has no coordinator" % s.part)
            elif view_link(s, os.path.relpath(rp, vault)) not in open(rp, encoding="utf-8").read():
                E(name, "missing from the %s catalog (run build_views.py)" % r)
    if portable:
        for problem in portable.problems:
            E("generated view", problem)
    for m in re.finditer(r"\[\[00 ASTORIA/skills/([^/|\]]+)/SKILL(?:\|[^\]]*)?\]\]", map_text):
        if m.group(1) not in skills:
            E("Skill Map", "links to a skill that does not exist: %s" % m.group(1))

    # System catalogs must match their generated region, not an incidental body link.
    try:
        for coordinator, text, updated in views.system_catalog_views(skills, vocab, vault):
            if text != updated:
                E(coordinator.name, "system catalog differs from skill frontmatter (run build_views.py)")
    except ValueError as error:
        E("system catalogs", str(error))

    # Stray instruction files include hidden instruction folders; runtime caches are skipped.
    for rroot, dirs, files in os.walk(vault):
        rel_root = os.path.relpath(rroot, vault)
        if rel_root.startswith((".obsidian", ".trash")) or os.path.basename(rroot) in {"__pycache__", "node_modules"}:
            dirs[:] = []; continue
        for f in files:
            if f in STRAY:
                E(os.path.join(rel_root, f) if rel_root != "." else f, "stray agent instruction file (AGENTS.md is the only one)")
        if os.path.basename(rroot) in (".claude", ".agents"):
            for x in dirs + files:
                if x != "skills":
                    E(os.path.join(rel_root, x), "%s/ may hold only the skills shim folder" % os.path.basename(rroot))
            sh = os.path.join(rroot, "skills")
            if os.path.isdir(sh):
                for x in os.listdir(sh):
                    xp = os.path.join(sh, x)
                    if not os.path.islink(xp):
                        E(os.path.join(rel_root, "skills", x), "shim is not a symlink; run skill-mount")
                    elif not os.path.isfile(os.path.join(xp, "SKILL.md")):
                        E(os.path.join(rel_root, "skills", x), "shim points at a missing skill; run skill-mount")
            dirs[:] = []

    report = {"skills": len(skills), "catalog": len(catalog), "errors": errors, "warnings": warnings}
    if "--json" in argv:
        print(json.dumps(report, ensure_ascii=False, indent=1)); return 1 if errors else 0
    cat = (", %d in the catalog" % len(catalog)) if catalog else ""
    print("Skills lint: %d skills%s, %d errors, %d warnings" % (len(skills), cat, len(errors), len(warnings)))
    if pending:
        where = "the catalog" if catalog else "the ASTORIA repository"
        print("links to %d skills not installed (available in %s): %s" % (len(pending), where, ", ".join(sorted(pending))))
    for label, items in (("ERRORS", errors), ("WARNINGS", warnings)):
        if items:
            print("\n%s" % label)
            for s, msg in items:
                print("  %s: %s" % (s, msg))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
