#!/usr/bin/env python3
"""build_views.py: regenerate the Skill Map registry and configured coordinator catalogs
from skill frontmatter. Also mirrors version.json in the Skill Map properties.

Usage: python3 build_views.py [--vault PATH] [--check]
--check prints what would change and exits 1 if any view is stale.
"""
import json
import os, re, sys
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillkit as sk


def entry(s, tags=None, style="full"):
    line = "- %s" % s.link()
    if tags:
        line += " (%s)" % "; ".join(t for t in tags if t)
    trig = s.triggers
    if style == "compact":
        line += ": Triggers: %s." % ", ".join(trig) if trig else ": %s" % s.summary
        return line
    line += ": %s" % s.summary
    if trig:
        line += " Triggers: %s." % ", ".join(trig)
    return line


def system_groups(system, members, vocab):
    """Select configured groups once; reject missing or duplicate ownership."""
    groups = vocab.get("system_sections", {}).get(system)
    if not groups:
        return None
    by_name = {s.name: s for s in members}
    assigned, result = set(), []
    for heading, names in groups.items():
        if not isinstance(names, list):
            raise ValueError("%s section %s must list skill names" % (system, heading))
        selected = []
        for name in names:
            if name in assigned:
                raise ValueError("%s is assigned to two %s sections" % (name, system))
            if name not in by_name:
                # Optional skills may be absent from a reduced installed catalog.
                if name not in vocab.get("starter", {}).get("catalog_index", {}):
                    raise ValueError("%s section %s names missing member %s" % (system, heading, name))
                continue
            assigned.add(name)
            selected.append(by_name[name])
        result.append((heading, selected))
    missing = set(by_name) - assigned
    if missing:
        raise ValueError("%s members need a section: %s" % (system, ", ".join(sorted(missing))))
    return result


def system_navigation(skills, vocab):
    """Keep the opening navigation in the same order as installed systems."""
    present = {skill.system for skill in skills.values()}
    out = ["> [!example] 🗺️ Systems"]
    for name in vocab["system_order"]:
        if name not in present:
            continue
        cfg = vocab["systems"][name]
        heading = "%s %s" % (cfg.get("emoji", ""), name)
        out.append("> - %s [[#%s|%s]]: %s." % (
            cfg.get("emoji", ""), heading, name, cfg.get("tagline", "")))
    return "\n".join(out)


def registry(skills, vocab, vault=None):
    """Skills grouped by system, the original Skill Map shape. The Research Assistant
    System shows its whole hierarchy: companions and coordination, then one section per part with the
    coordinator first and the part skills grouped by family."""
    systems, order = vocab["systems"], vocab["system_order"]
    coords, part_names, fam_labels = vocab["part_coordinators"], vocab["parts"], vocab["families"]
    level_tag = {"companion": "companion", "coordinator": "coordinator", "profile": "profile"}
    comp_order = {n: i for i, n in enumerate(vocab.get("companion_order", []))}
    def line(s, extra=None):
        tags = []
        if s.level in level_tag and not (extra and extra[0].startswith("part coordinator")):
            tags.append(level_tag[s.level])
        if extra:
            tags.extend(x for x in extra if x != "any")
        return entry(s, tags)
    def by_level_then_name(items):
        rank = {"companion": 0, "coordinator": 1, "skill": 2, "profile": 3}
        return sorted(items, key=lambda x: (rank.get(x.level, 9), comp_order.get(x.name, 99), x.name))
    out = []
    for sysname in order:
        cfg = systems[sysname]
        members = [s for s in skills.values() if s.system == sysname]
        if not members:
            continue
        out.append("## %s %s" % (cfg.get("emoji", ""), sysname))
        if cfg.get("banner"):
            banner = cfg["banner"]
            if not isinstance(banner, str) or os.path.isabs(banner) or ".." in banner.split("/"):
                raise ValueError("%s banner must be a vault-relative path" % sysname)
            if vault:
                target = os.path.realpath(os.path.join(vault, banner))
                if os.path.commonpath([os.path.realpath(vault), target]) != os.path.realpath(vault) or not os.path.isfile(target):
                    raise ValueError("%s banner is missing or outside the vault: %s" % (sysname, banner))
            relative = os.path.relpath(banner, os.path.dirname(sk.MAP_REL)).replace(os.sep, "/")
            out.extend(["", "![%s](%s)" % (sysname, quote(relative, safe="/")), ""])
        if cfg.get("note"):
            out.append("[[%s]]: %s." % (sysname, cfg.get("tagline", "")))
        elif vocab.get("system_sections", {}).get(sysname):
            for heading, selected in system_groups(sysname, members, vocab):
                if out[-1] != "":
                    out.append("")
                out.append("### %s" % heading)
                for s in by_level_then_name(selected):
                    out.append(line(s))
        else:
            out.append("%s." % cfg.get("tagline", ""))
        if sysname == "Research Assistant System":
            top = [s for s in members if not s.part]
            out.extend(["", "- [[#Companions and coordination|Companions and coordination]]"])
            for pt in sorted(coords):
                heading = "%s. %s" % (pt, part_names.get(pt, ""))
                out.append("- [[#%s|%s]]" % (heading, heading))
            out.append("")
            out.append("### Companions and coordination")
            out.append("The public research entry point and its internal research-coordinator. Research Companion stays the visible session owner; research-coordinator verifies bounded assignments through the five part coordinators below (1 to 5, in any order) or an exact named capability, dispatches the needed research workers, and returns their evidence to the companion. PhD and career support has its own system; shared services preserve the original owner and task scope.")
            for s in by_level_then_name(top):
                out.append(line(s, ["internal, no triggers"] if s.name == "research-coordinator" else None))
            for pt in sorted(coords):
                r = skills.get(coords[pt])
                part_members = [s for s in members if s.part == pt and s.family != "part-coordinator"]
                out.append("")
                out.append("### %s. %s" % (pt, part_names.get(pt, "")))
                if r:
                    out.append(line(r, ["part coordinator, read first"]))
                by_fam = {}
                for s in part_members:
                    by_fam.setdefault(s.family or "other", []).append(s)
                fam_order = [f for f in fam_labels if f in by_fam] + [f for f in by_fam if f not in fam_labels]
                for fam in fam_order:
                    out.append("")
                    out.append("#### %s" % fam_labels.get(fam, fam))
                    for s in by_level_then_name(by_fam[fam]):
                        tags = []
                        if s.meta.get("modality"):
                            tags.append(s.meta["modality"])
                        if s.meta.get("population"):
                            tags.append(s.meta["population"])
                        out.append(line(s, tags))
        elif not vocab.get("system_sections", {}).get(sysname):
            for s in by_level_then_name(members):
                out.append(line(s))
        out.append("")
        out.append("---")
    if out and out[-1] == "---":
        out.pop()
    return "\n".join(out)


def catalog(part, skills, vocab):
    fam_labels = vocab["families"]
    members = [s for s in skills.values() if s.part == part and s.family != "part-coordinator"]
    out = ["Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first."]
    by_fam = {}
    for s in members:
        by_fam.setdefault(s.family or "other", []).append(s)
    order = [f for f in fam_labels if f in by_fam] + [f for f in by_fam if f not in fam_labels]
    for fam in order:
        out.append("")
        out.append("### %s" % fam_labels.get(fam, fam))
        for s in sorted(by_fam[fam], key=lambda x: x.name):
            tags = []
            if s.level == "coordinator":
                tags.append("coordinator")
            if s.meta.get("modality"):
                tags.append(s.meta["modality"])
            if s.meta.get("population"):
                tags.append(s.meta["population"])
            out.append(entry(s, tags, vocab.get("catalog_style", "full")))
    out.append("")
    out.append("%d skills in this part." % len(members))
    return "\n".join(out)


def system_catalog(system, skills, vocab):
    """A nonresearch coordinator lists only its system's bounded skills."""
    members = [s for s in skills.values() if s.system == system]
    groups = system_groups(system, members, vocab)
    selected_section = vocab.get("system_catalog_sections", {}).get(system)
    if selected_section:
        matches = [items for heading, items in groups or [] if heading == selected_section]
        if len(matches) != 1:
            raise ValueError("%s catalog section %s is missing" % (system, selected_section))
        members = matches[0]
    members = [s for s in members if s.level == "skill"]
    out = ["Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.", ""]
    for s in sorted(members, key=lambda x: x.name):
        out.append(entry(s, style=vocab.get("catalog_style", "full")))
    out.extend(["", "%d skills in this %s." % (len(members), "section" if selected_section else "system")])
    return "\n".join(out)


def system_catalog_views(skills, vocab, vault):
    """Read and validate configured system views without changing any file."""
    updates = []
    configured = vocab.get("system_coordinators") or {}
    if not isinstance(configured, dict):
        raise ValueError("system_coordinators must map system names to coordinator names")
    for system, name in sorted(configured.items()):
        if system not in vocab["systems"]:
            raise ValueError("system coordinator %s uses unknown system %s" % (name, system))
        coordinator = skills.get(name)
        if not coordinator:
            raise ValueError("%s coordinator %s not found" % (system, name))
        if coordinator.system != system or coordinator.level != "coordinator":
            raise ValueError("%s must be a coordinator in %s" % (name, system))
        with open(coordinator.path, encoding="utf-8") as source:
            text = source.read()
        start = sk.MARK_START.format(name="catalog")
        end = sk.MARK_END.format(name="catalog")
        if text.count(start) != 1 or text.count(end) != 1 or text.index(start) >= text.index(end):
            raise ValueError("%s needs exactly one ordered catalog marker pair: %s and %s" % (name, start, end))
        rendered = render_links(system_catalog(system, skills, vocab), os.path.relpath(coordinator.path, vault), vault, vocab)
        updates.append((coordinator, text, sk.replace_between(text, "catalog", rendered)))
    return updates


def render_links(text, document, vault, vocab):
    """Public views use each generated document's actual relative location."""
    if not sk.portable_links_enabled(vocab):
        return text
    links = sk.PortableLinks(vault)
    rendered = links.rewrite(text, document)
    if links.problems:
        raise ValueError("\n".join(links.problems))
    return rendered


def with_astoria_version(text, vault):
    """Mirror the version record in the map, preserving other frontmatter."""
    path = os.path.join(vault, "00 ASTORIA", "version.json")
    if not os.path.lexists(path):
        return text
    if os.path.islink(path):
        raise ValueError("version.json must be a regular file in the vault")
    with open(path, encoding="utf-8") as record:
        data = json.load(record)
    version = data.get("version") if isinstance(data, dict) else None
    if not isinstance(version, str) or not re.fullmatch(r"(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}", version):
        raise ValueError("version.json must provide a version in major.minor.patch form")
    frontmatter = re.match(r"\A---\n(.*?)^---(?=\n|$)", text, re.M | re.S)
    if frontmatter is None:
        raise ValueError("the Skill Map is missing its YAML properties")
    properties = frontmatter.group(1)
    key = re.compile(r"^astoria_version:[^\n]*\n", re.M)
    if len(key.findall(properties)) > 1:
        raise ValueError("the Skill Map has more than one astoria_version property")
    line = "astoria_version: %s\n" % json.dumps(version)
    updated, count = key.subn(line, properties)
    if not count:
        updated += line
    return text[:frontmatter.start(1)] + updated + text[frontmatter.end(1):]


def main(argv):
    vault = sk.vault_from_argv(argv)
    check = "--check" in argv
    vocab = sk.load_vocab(vault)
    skills = sk.load_skills(vault)
    stale = []
    # Validate system catalogs before writing the map or any other view.
    try:
        system_views = system_catalog_views(skills, vocab, vault)
    except ValueError as error:
        print("Invalid generated system catalog: %s" % error); return 2
    # Skill Map registry
    mp = os.path.join(vault, sk.MAP_REL)
    text = open(mp, encoding="utf-8").read()
    try:
        rendered = render_links(registry(skills, vocab, vault), sk.MAP_REL, vault, vocab)
    except ValueError as error:
        print("Invalid generated view: %s" % error); return 2
    new = sk.replace_between(text, "registry", rendered)
    if new is None:
        print("Skill Map has no registry markers"); return 2
    if sk.MARK_START.format(name="systems") in text or sk.MARK_END.format(name="systems") in text:
        navigation = render_links(system_navigation(skills, vocab), sk.MAP_REL, vault, vocab)
        new = sk.replace_between(new, "systems", navigation)
        if new is None:
            print("Skill Map has invalid systems markers"); return 2
    try:
        new = with_astoria_version(new, vault)
    except (OSError, ValueError) as error:
        print("Invalid ASTORIA version: %s" % error); return 2
    if new != text:
        stale.append(sk.MAP_REL)
        if not check:
            open(mp, "w", encoding="utf-8").write(new)
    # coordinator catalogs
    for st, rname in sorted(vocab["part_coordinators"].items()):
        r = skills.get(rname)
        if not r:
            print("part %s coordinator %s not found" % (st, rname)); continue
        rt = open(r.path, encoding="utf-8").read()
        try:
            rendered = render_links(catalog(st, skills, vocab), os.path.relpath(r.path, vault), vault, vocab)
        except ValueError as error:
            print("Invalid generated catalog: %s" % error); return 2
        newr = sk.replace_between(rt, "catalog", rendered)
        if newr is None:
            print("%s has no catalog markers" % rname); continue
        if newr != rt:
            stale.append(r.folder)
            if not check:
                open(r.path, "w", encoding="utf-8").write(newr)
    # Nonresearch system catalogs use the same markers and output style.
    for coordinator, text, updated in system_views:
        if updated != text:
            stale.append(coordinator.folder)
            if not check:
                with open(coordinator.path, "w", encoding="utf-8") as destination:
                    destination.write(updated)
    if check:
        print("stale views: %s" % (", ".join(stale) if stale else "none"))
        return 1 if stale else 0
    print("rebuilt: %s" % (", ".join(stale) if stale else "nothing changed"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
