#!/usr/bin/env python3
"""wire_shims.py: plan skill mounts and report local registry evidence.

Every skill stays in `00 ASTORIA/skills/<name>`; the platforms get links, never copies.

Agent platforms discover skills in one of two ways, and the two need opposite treatment.

A SCAN platform reads a skill folder. This script previews relative links and reports
occupied destinations. If native discovery is requested, use the selected platform's
supported manual or host mount method with the reviewed paths. Codex reads
`.agents/skills/` and Claude Code reads `.claude/skills/`; both follow symlinked folders.

A REGISTRY platform keeps a catalog of its own and admits a skill only through its own
API, so no file written anywhere mounts a skill there. Its local catalog folder is the
copy it writes downward after registering something, not an inbox: a folder placed there
is ignored however it is built. The script reads the local catalog without modifying it. It
reports local verification leads, occupied names and possible inert links. With --emit-manifest
it prints the platform-neutral JSON for the selected set. That run is an agent step, described in ./references/registry_adapters.md, one
short adapter section per platform.

Both platform sets are declared in the two tables below. Adding or replacing a platform is
a table row, plus an adapter section in that reference file for a registry platform.

Usage: python3 wire_shims.py [--vault PATH] [--set core|all]
                             [--scan-only] [--catalog-glob PATTERN] [--emit-manifest]
--scan-only: skip the registry report (alias: --no-claude-science).
--catalog-glob: report a registry catalog at this glob instead of the declared one, for a
  mounted copy, another user, or a machine that installs the platform elsewhere.
  (Alias for the Claude Science row: --claude-science-root PATH.)
--emit-manifest: print name, description, vault-relative and absolute SKILL.md path of
  every chosen skill as JSON, last and with nothing after it, for the registration step.
Plan and report only. --set core selects companions and the five part coordinators;
--set all (the default) selects every level-1 skill (companions, part
coordinators, standalone skills). Profiles and the internal coordinator
are left out. Existing scan links stay in place.
Prints a configurable local listing-size preference, not a platform limit or a
guarantee about which descriptions an agent will show.
A registry platform that is not installed on this machine is reported and skipped.
"""
import sys

# The CLI must leave even a fresh vault free of import-generated cache files.
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    from contextlib import ExitStack, contextmanager
    import fnmatch, glob, json, os, re, stat
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(HERE, "..", "..", "skills-janitor", "scripts"))
    import skillkit as sk
finally:
    sys.dont_write_bytecode = previous_bytecode_setting


# ---- Platform tables: edit these, not the code below ------------------------

# Scan platforms: (mount folder relative to the vault root, platform name).
# The plan lists one relative link per selected skill.
SCAN_PLATFORMS = [
    (".agents/skills", "Codex"),
    (".claude/skills", "Claude Code"),
]

# Registry platforms: a catalog reached only through the platform's own API.
#   name          what to call it in the report and in registry_adapters.md
#   catalog_glob  where its local catalog copy lives, for read-only evidence.
#                 Optional: set it to "" when the platform keeps none locally.
#   stamp         the per-entry marker used to find possible local pointer matches.
#                 Verify registration and ownership through the platform.
#   root_alias    an older command-line flag kept working, or "" for none.
REGISTRY_PLATFORMS = [
    {"name": "Claude Science",
     "catalog_glob": "~/.claude-science/orgs/*/skills",
     "stamp": ".catalog_stamp",
     "root_alias": "--claude-science-root"},
]

BUDGET = 8000  # local listing-size preference; verify platform behavior separately
DEFAULT_SET = "all"


def safe_directory_access():
    """Check the primitives needed for descriptor-relative, no-follow access."""
    operations = {os.open, os.stat, os.readlink}
    return (all(hasattr(os, flag) for flag in ("O_DIRECTORY", "O_NOFOLLOW"))
            and operations <= os.supports_dir_fd
            and os.stat in os.supports_follow_symlinks and os.listdir in os.supports_fd)


def path_parts(path):
    """Return absolute path components without collapsing a parent traversal."""
    absolute = path if os.path.isabs(path) else os.path.join(os.getcwd(), path)
    parts = tuple(part for part in absolute.split(os.sep) if part not in ("", "."))
    if ".." in parts:
        raise ValueError("parent traversal in path")
    return parts


@contextmanager
def directory_at(parent_fd, parts):
    """Pin a directory by opening each component without following links."""
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(os.sep, flags) if parent_fd is None else os.dup(parent_fd)
    try:
        for part in parts:
            if not part or part in (".", "..") or os.sep in part:
                raise ValueError("invalid directory component: %r" % part)
            child = os.open(part, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def valid_scan_source(vault_fd, name):
    try:
        with directory_at(vault_fd, ("00 ASTORIA", "skills", name)) as fd:
            return stat.S_ISREG(os.stat("SKILL.md", dir_fd=fd, follow_symlinks=False).st_mode)
    except OSError:
        return False


def usable_scan_target(fd, path, expected):
    try:
        raw = os.readlink(os.path.basename(path), dir_fd=fd)
    except OSError:
        return None
    if os.path.realpath(os.path.join(os.path.dirname(path), raw)) == expected:
        return raw
    return None


def scan_plan(vault_fd, vault, chosen):
    """Preflight selected destinations through the same no-follow path boundary."""
    plans, conflicts, notices = [], [], []
    if not chosen:
        return plans, conflicts, notices
    wanted = {s.name for s in chosen}
    skills = os.path.join(vault, "00 ASTORIA", "skills")
    for name in sorted(wanted):
        if not valid_scan_source(vault_fd, name):
            conflicts.append("selected canonical skill is missing or redirected: %s" % os.path.join(skills, name))
    if conflicts:
        return plans, conflicts, notices

    for shim, platform_name in SCAN_PLATFORMS:
        parts = tuple(shim.split(os.sep))
        destination = os.path.join(vault, shim)
        try:
            with ExitStack() as stack:
                try:
                    fd = stack.enter_context(directory_at(vault_fd, parts))
                except FileNotFoundError:
                    fd = None
                entries = set(os.listdir(fd)) if fd is not None else set()
                for entry in sorted(entries - wanted):
                    try:
                        mode = os.stat(entry, dir_fd=fd, follow_symlinks=False).st_mode
                    except FileNotFoundError:
                        continue
                    if stat.S_ISLNK(mode):
                        notices.append("unselected scan link preserved for separate review: %s"
                                       % os.path.join(destination, entry))
                for skill in chosen:
                    name = skill.name
                    target = os.path.join(*([".."] * len(parts)), "00 ASTORIA", "skills", name)
                    path = os.path.join(destination, name)
                    if name not in entries:
                        plans.append((parts, name, target))
                        continue
                    raw = usable_scan_target(fd, path, os.path.join(skills, name))
                    if raw is None:
                        conflicts.append("occupied scan destination preserved for separate review: %s" % path)
                    elif raw != target:
                        notices.append("usable existing scan link preserved: %s" % path)
        except (OSError, ValueError) as err:
            conflicts.append("%s mount directory cannot be safely inspected: %s (%s)"
                             % (platform_name, destination, err))
    return plans, conflicts, notices


def report_scan(vault, chosen):
    """Print a read-only preview of the selected scan mounts."""
    if not safe_directory_access():
        print("Safe scan preview is unavailable here. Use direct AGENTS.md access or review exact locations through the selected platform's supported mount method.")
        return True
    try:
        with directory_at(None, path_parts(vault)) as vault_fd:
            plans, conflicts, notices = scan_plan(vault_fd, vault, chosen)
    except (OSError, ValueError) as err:
        print("Scan preview stopped. Review the exact vault and mount locations: %s" % err)
        return False
    for message in notices:
        print(message)
    if conflicts:
        print("Mount conflicts; no mounts changed:")
        print("\n".join(conflicts))
        return False
    for parts, name, target in plans:
        print("link %s -> %s" % (os.path.join(vault, *parts, name), target))
    return True


def catalog_pattern(platform, argv):
    """The catalog glob to report, after any command-line override.

    --catalog-glob wins, then the platform's own older root flag if it declares one, then
    the pattern in the table. Keeping the override here means the platform table stays a
    plain description of where things live.
    """
    if "--catalog-glob" in argv:
        return argv[argv.index("--catalog-glob") + 1]
    alias = platform.get("root_alias") or ""
    if alias and alias in argv:
        # The older flag named an install root rather than a glob: swap it in for the
        # leading part of the declared pattern, up to the first wildcard.
        root = argv[argv.index(alias) + 1]
        head, sep, tail = platform["catalog_glob"].partition("/*")
        return os.path.join(root, os.path.basename(head)) + sep + tail if sep else root
    return platform["catalog_glob"]


def catalog_dirs(pattern, name):
    """Yield each matching catalog with its no-follow descriptor still open."""
    if not safe_directory_access() or not hasattr(os, "O_NONBLOCK"):
        print("%s: local catalog inspection unavailable; verify through the platform" % name)
        return
    expanded = os.path.expanduser(pattern)

    def visit(fd, parts, path):
        if not parts:
            yield path, fd
            return
        component, *tail = parts
        if glob.has_magic(component):
            entries = os.listdir(fd)
            if not component.startswith("."):
                entries = [entry for entry in entries if not entry.startswith(".")]
            entries = sorted(fnmatch.filter(entries, component))
        else:
            entries = [component]
        for entry in entries:
            selected = os.path.join(path, entry)
            try:
                with directory_at(fd, (entry,)) as child:
                    yield from visit(child, tail, selected)
            except FileNotFoundError:
                continue
            except (OSError, ValueError) as err:
                print("%s: catalog path skipped; verify through the platform: %s (%s)"
                      % (name, selected, err))

    try:
        with directory_at(None, ()) as root_fd:
            found = False
            for catalog in visit(root_fd, path_parts(expanded), os.sep):
                found = True
                yield catalog
            if not found:
                print("%s: no readable catalog at %s; verify through the platform" % (name, expanded))
    except (OSError, ValueError) as err:
        print("%s: local catalog could not be safely inspected: %s (%s)" % (name, expanded, err))


def registry_evidence(d, catalog_fd, vault, stamp):
    """Read bounded local evidence through the pinned catalog descriptor."""
    candidates, leads = [], []
    valid_stamp = stamp and os.path.basename(stamp) == stamp and stamp not in {".", ".."}
    vault_root = os.path.realpath(vault)
    try:
        occupied = set(os.listdir(catalog_fd))
        for entry in sorted(occupied):
            try:
                mode = os.stat(entry, dir_fd=catalog_fd, follow_symlinks=False).st_mode
                if stat.S_ISLNK(mode):
                    candidates.append(os.path.join(d, entry))
                    continue
                if not stat.S_ISDIR(mode):
                    continue
                with directory_at(catalog_fd, (entry,)) as entry_fd:
                    member = os.stat("SKILL.md", dir_fd=entry_fd, follow_symlinks=False)
                    if stat.S_ISLNK(member.st_mode):
                        if set(os.listdir(entry_fd)) == {"SKILL.md"}:
                            candidates.append(os.path.join(d, entry))
                        continue
                    if not valid_stamp or not stat.S_ISREG(member.st_mode):
                        continue
                    marker = os.stat(stamp, dir_fd=entry_fd, follow_symlinks=False)
                    if not stat.S_ISREG(marker.st_mode):
                        continue
                    file_fd = os.open("SKILL.md", os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                                      dir_fd=entry_fd)
                    with os.fdopen(file_fd, encoding="utf-8") as stream:
                        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                            continue
                        head = stream.read(4000)
            except (OSError, UnicodeError):
                continue
            expected = os.path.join(vault_root, "00 ASTORIA", "skills", entry, "SKILL.md")
            quoted_paths = re.findall(r"[`\"']([^`\"'\n]+)[`\"']", head)
            if expected in quoted_paths:
                leads.append(entry)
        return occupied, candidates, leads
    except OSError:
        return None


def report_registry(platform, d, catalog_fd, chosen, vault):
    """Report local occupancy and leads, with platform verification still required."""
    name = platform["name"]
    evidence = registry_evidence(d, catalog_fd, vault, platform.get("stamp", ""))
    if evidence is None:
        print("%s %s: local catalog could not be safely inspected; verify through the platform" % (name, d))
        return
    occupied, candidates, leads = evidence
    for path in candidates:
        print("registry link candidate; preserved without following it: %s" % path)
    wanted = {s.name for s in chosen}
    to_register = [s.name for s in chosen if s.name not in occupied]
    blocked = sorted(wanted & occupied)
    print("%s %s: %d local pointer lead(s), %d locally vacant, %d linked candidate(s)"
          % (name, d, len(leads), len(to_register), len(candidates)))
    if leads:
        print("  verify local pointer leads through the platform: %s" % " ".join(leads))
    if blocked:
        print("  occupied; preserved, no registration: %s" % " ".join(blocked))
    if to_register:
        print("  confirm vacancy before registration: %s" % " ".join(to_register))
    if candidates or blocked or to_register or leads:
        print("  use the %s adapter in ./references/registry_adapters.md for authorized platform actions" % name)



def main(argv):
    if any(flag == "--apply" or flag.startswith("--apply=") for flag in argv):
        print("--apply is unavailable. This helper only reports a plan. Run without --apply and review exact paths before any requested manual or host mount.")
        return 1
    if any(flag == "--remove" or flag.startswith("--remove=") for flag in argv):
        print("--remove is not supported. Review exact entries separately before any authorized cleanup; no mounts changed.")
        return 1
    value_flags = {"--vault", "--set", "--catalog-glob"} | {p["root_alias"] for p in REGISTRY_PLATFORMS if p.get("root_alias")}
    for i, flag in enumerate(argv):
        if flag in value_flags and (i + 1 >= len(argv) or argv[i + 1].startswith("--")):
            print("%s needs a value; no mounts changed" % flag)
            return 1
    vault = sk.vault_from_argv(argv)

    skills = sk.load_skills(vault)
    setname = DEFAULT_SET
    for i, a in enumerate(argv):
        if a == "--set" and i + 1 < len(argv):
            setname = argv[i + 1]
    if setname not in {"core", "all"}:
        print("--set must be core or all; no mounts changed")
        return 1
    chosen = []
    for s in skills.values():
        if s.level == "profile" or (s.level == "coordinator" and not s.part):
            continue
        if s.part and s.family != "part-coordinator":
            continue
        if setname == "core" and s.level == "skill":
            continue
        chosen.append(s)
    chosen.sort(key=lambda s: (0 if s.level == "companion" else 1 if s.level == "coordinator" else 2, s.name))
    total = sum(len(s.name) + len(s.description) + 4 for s in chosen)
    print("level-1 skills to mount: %d (set %s) | descriptions about %d characters (local listing preference %d)" % (len(chosen), setname, total, BUDGET))
    if total > BUDGET:
        print("over the local listing preference by %d characters; choose core or adjust BUDGET if useful. Verify each platform's current discovery and display behavior separately." % (total - BUDGET))
    # ---- Scan platforms: report only ----
    if not report_scan(vault, chosen):
        return 1
    # ---- Registry platforms: report only ----
    # Local catalog entries are evidence for review, not a platform action queue.
    scan_only = "--scan-only" in argv or "--no-claude-science" in argv      # older alias

    for platform in ([] if scan_only else REGISTRY_PLATFORMS):
        pattern = catalog_pattern(platform, argv)
        if not pattern:
            print("%s: keeps no local catalog; use the registration step to list it" % platform["name"])
            continue
        for d, catalog_fd in catalog_dirs(pattern, platform["name"]):
            report_registry(platform, d, catalog_fd, chosen, vault)

    print("Plan only. Use reviewed paths for any requested manual or host mount.")

    # The manifest the registration step consumes: one entry per chosen skill, in no
    # platform's format. Both paths are given on purpose. `skill_md_relative` is stable
    # across machines and is what a stub should quote as the durable location;
    # `skill_md` is this machine's resolved path and is the one to try first.
    # Printed last and nothing after it, so the JSON can be sliced off the end of the run
    # with sed -n '/^\[/,$p' and read directly.
    if "--emit-manifest" in argv:
        vault_root = os.path.realpath(vault)
        manifest = [{"name": s.name,
                     "description": " ".join(s.description.split()),
                     "vault_root": vault_root,
                     "skill_md_relative": os.path.join("00 ASTORIA", "skills", s.name, "SKILL.md"),
                     "skill_md": os.path.join(vault_root, "00 ASTORIA", "skills", s.name, "SKILL.md")}
                    for s in chosen]
        print("--- manifest json (%d skills) ---" % len(manifest))
        print(json.dumps(manifest, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
