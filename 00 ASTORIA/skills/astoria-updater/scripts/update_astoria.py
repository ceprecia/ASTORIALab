"""Preview and apply a trusted ASTORIA release to an installed vault.

Verify the official release before supplying --verified-release.
Run with --source RELEASE --target VAULT and, when known, --baseline OLD_RELEASE.
Apply only the displayed plan with --apply PLAN_ID.
"""
import argparse
from dataclasses import dataclass
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile

ASTORIA = Path("00 ASTORIA")
VERSION = ASTORIA / "version.json"
SKILL_MAP = ASTORIA / "Skill Map.md"
AI_LOG = ASTORIA / "agent_notes/ai_log.md"
ACTIVE = ASTORIA / "skills"
OPTIONAL = ASTORIA / "specialized_skills"
VIEW_SCRIPT = ACTIVE / "skills-janitor/scripts/build_views.py"
UPDATE_LOCK = ASTORIA / ".astoria-update-lock"
TOOLKIT_STATE = ASTORIA / ".toolkit-install-in-progress.json"
GENERATED = re.compile(
    rb"(<!-- (catalog|registry|systems):start -->).*?(<!-- \2:end -->)", re.S
)


@dataclass(frozen=True)
class File:
    data: bytes
    mode: int

    def digest(self):
        return hashlib.sha256(self.data).hexdigest()


def safe_path(root, relative):
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Linked path requires review: {relative}")
    return path


def read_file(root, relative):
    path = safe_path(root, relative)
    if not path.exists():
        return None
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"Expected an independent regular file: {relative}")
    return File(path.read_bytes(), stat.S_IMODE(info.st_mode) & 0o777)


def write_file(root, relative, content):
    path = safe_path(root, relative)
    if content is None:
        path.unlink()
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
        staged = Path(temporary.name)
        try:
            temporary.write(content.data)
            temporary.close()
            staged.chmod(content.mode)
            staged.replace(path)
        finally:
            staged.unlink(missing_ok=True)


def prune_empty_parents(root, relative, preserve=()):
    parent = safe_path(root, relative).parent
    while parent != root / ASTORIA and parent not in preserve and parent.is_dir():
        if any(parent.iterdir()):
            break
        parent.rmdir()
        parent = parent.parent


def scan_error(error):
    raise error


def inventory(root):
    files = {}
    for directory in (ACTIVE, OPTIONAL, ASTORIA / "systems", ASTORIA / "templates", ASTORIA / "assets"):
        start = safe_path(root, directory)
        if not start.exists():
            continue
        if not start.is_dir():
            raise ValueError(f"Expected a directory: {directory}")
        for parent, dirs, names in os.walk(start, onerror=scan_error):
            dirs[:] = sorted(name for name in dirs if not name.startswith(".") and name != "__pycache__")
            for name in dirs:
                safe_path(root, (Path(parent) / name).relative_to(root))
            for name in sorted(names):
                if name.startswith(".") or name.endswith((".pyc", ".env")):
                    continue
                relative = (Path(parent) / name).relative_to(root)
                files[relative] = read_file(root, relative)
    for relative in (SKILL_MAP, ASTORIA / "Skills.md", VERSION):
        content = read_file(root, relative)
        if content is not None:
            files[relative] = content
    return files


def version(files):
    content = files.get(VERSION)
    if content is None:
        return None
    record = json.loads(content.data)
    value = record.get("version") if isinstance(record, dict) else None
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", value):
        raise ValueError(f"Invalid ASTORIA version in {VERSION}")
    return value


def installed_paths(files, current, tools):
    """Render release links using the same installed options as the destination."""
    result = {}
    moves, absent = {}, set()
    for path, content in files.items():
        if path.is_relative_to(OPTIONAL):
            suffix = path.relative_to(OPTIONAL)
            name = suffix.parts[0]
            if ACTIVE / name / "SKILL.md" in current:
                moves[(OPTIONAL / name).as_posix()] = (ACTIVE / name).as_posix()
                path = ACTIVE / suffix
            elif OPTIONAL / name / "SKILL.md" not in current:
                absent.add(name)
                continue
        if path in result:
            raise ValueError(f"Two release files resolve to the same installed path: {path}")
        result[path] = content
    if not (moves or absent):
        return result

    with tempfile.TemporaryDirectory(prefix="astoria_links_") as folder:
        stage = Path(folder)
        for path, content in result.items():
            write_file(stage, path, content)
        add_stage_placeholders(stage)
        command = (
            "import json, sys; sys.path.insert(0, sys.argv[1]); import skillkit; "
            "changed, problems = skillkit.portable_vault_links("
            "sys.argv[2], json.loads(sys.argv[3]), json.loads(sys.argv[4])); "
            "sys.exit('\\n'.join(problems) if problems else 0)"
        )
        run_check([sys.executable, "-E", "-B", "-c", command, str(tools), str(stage),
                   json.dumps(moves), json.dumps(sorted(absent))], "Release links could not be adapted", stage)
        return inventory(stage)


def comparison(content, path):
    if content is None:
        return None
    if path.name == "SKILL.md" or path == SKILL_MAP:
        return GENERATED.sub(rb"\1\3", content.data)
    return content.data


def change_group(path):
    if path.is_relative_to(ACTIVE) or path.is_relative_to(OPTIONAL):
        return Path(*path.parts[:3])
    return path


def select_changes(current, source, baseline):
    changes = {}
    conflicts = {}
    groups = {change_group(path) for path in current}
    for path in sorted(source.keys() | baseline.keys()):
        if path in (SKILL_MAP, VERSION):
            continue
        before = comparison(baseline.get(path), path)
        live = comparison(current.get(path), path)
        after = comparison(source.get(path), path)
        if live == after or before == after:
            continue
        if live == before and (before is not None or change_group(path) not in groups):
            incoming = source.get(path)
            if incoming and path in current:
                incoming = File(incoming.data, current[path].mode)
            changes[path] = incoming
        elif live == before and before is None and path in source:
            owner = change_group(path) / "SKILL.md"
            if owner in baseline and comparison(current.get(owner), owner) == comparison(baseline[owner], owner):
                changes[path] = source[path]
            else:
                conflicts[path] = "New file would extend a skill whose original contents could not be verified"
        else:
            conflicts[path] = "Local file differs from the original release or was removed locally"
    for path, content in changes.items():
        if content is None and path.name == "SKILL.md" and path.is_relative_to(ACTIVE):
            extra = any(item.is_relative_to(path.parent) and item not in baseline for item in current)
            if extra:
                conflicts[path] = "Retiring the skill would leave local additions without a skill entry"
    held = {change_group(path) for path in conflicts}
    for path in list(changes):
        if change_group(path) in held:
            conflicts[path] = "Held with another file in the same skill"
            del changes[path]
    return changes, conflicts


def add_stage_placeholders(stage):
    for name in ("me.md", "AGENTS.md", "README.md", "LICENSE"):
        (stage / name).touch()
    (stage / AI_LOG.parent).mkdir(exist_ok=True)
    (stage / AI_LOG).touch()
    (stage / AI_LOG.parent / "layout.md").touch()


def run_check(command, label, stage):
    # Import helper modules from the isolated staging context, not the user vault.
    result = subprocess.run(command, cwd=stage, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(label + ": " + (result.stderr or result.stdout).strip())


def generated_changes(current, planned, tools):
    """Generate the exact preview in scratch using the selected release tools."""
    with tempfile.TemporaryDirectory(prefix="astoria_views_") as folder:
        stage = Path(folder)
        staged = dict(current)
        for path, content in planned.items():
            if content is None:
                staged.pop(path, None)
            else:
                staged[path] = content
        for path, content in staged.items():
            write_file(stage, path, content)
        add_stage_placeholders(stage)
        run_check([sys.executable, "-E", "-B", str(tools / "build_views.py"), "--vault", str(stage)],
                  "Skill views could not be generated", stage)
        lint = subprocess.run(
            [sys.executable, "-E", "-B", str(tools / "lint.py"), "--vault", str(stage), "--json"],
            cwd=stage, capture_output=True, text=True
        )
        if not lint.stdout:
            raise ValueError("Skill verification could not run: " + lint.stderr.strip())
        # A scratch vault omits the user's notes. Check skill dependencies and
        # identity here, while leaving user-note link checks to the vault janitor.
        errors = json.loads(lint.stdout)["errors"]
        problems = [f"{skill}: {message}" for skill, message in errors
                    if message.startswith(("dependency ", "frontmatter error:", "name field ",
                                           "present in both", "folder has no SKILL.md"))]
        if problems:
            raise ValueError("Skill verification found conflicts: " + "; ".join(problems))
        rendered = inventory(stage)
        for path, content in rendered.items():
            if staged.get(path) != content:
                if path != SKILL_MAP and comparison(staged.get(path), path) != comparison(content, path):
                    raise ValueError(f"View generation tried to change a non-generated file: {path}")
                planned[path] = content


def preview(source_root, target, baseline_root):
    source = inventory(source_root)
    current = inventory(target)
    baseline = inventory(baseline_root) if baseline_root else {}
    incoming_version = version(source)
    installed_version = version(current)
    if incoming_version is None or SKILL_MAP not in source or VIEW_SCRIPT not in source:
        raise ValueError("Choose an extracted, versioned ASTORIA starter release")
    if installed_version and tuple(map(int, incoming_version.split("."))) < tuple(map(int, installed_version.split("."))):
        raise ValueError("The selected release is older than the installed version")
    if baseline_root and (SKILL_MAP not in baseline or VIEW_SCRIPT not in baseline):
        raise ValueError("The baseline must be an original ASTORIA release")
    baseline_version = version(baseline)
    # A second pass keeps the original baseline after the first pass records
    # the incoming version. Three-way comparison still protects local edits.
    if (baseline_root and installed_version and baseline_version != installed_version
            and installed_version != incoming_version):
        raise ValueError("The original release does not match the installed version")
    if baseline_version and tuple(map(int, baseline_version.split("."))) > tuple(map(int, incoming_version.split("."))):
        raise ValueError("The original release is newer than the selected update")
    if baseline_version and not installed_version:
        if tuple(map(int, baseline_version.split("."))) >= tuple(map(int, incoming_version.split("."))):
            raise ValueError("The original release must predate the selected update")
    with tempfile.TemporaryDirectory(prefix="astoria_tools_") as folder:
        tools = Path(folder)
        for name in ("build_views.py", "skillkit.py", "lint.py"):
            path = VIEW_SCRIPT.with_name(name)
            if path not in source:
                raise ValueError(f"The release is missing a view helper: {path}")
            write_file(tools, Path(name), source[path])
        desired = installed_paths(source, current, tools)
        baseline_required = baseline_root is None and installed_version != incoming_version
        if baseline_root:
            original = installed_paths(baseline, current, tools)
            planned, conflicts = select_changes(current, desired, original)
            if not conflicts and source[VERSION] != current.get(VERSION):
                planned[VERSION] = source[VERSION]
        else:
            planned, conflicts = {}, {}
            conflicts = {
                path: "Original release required to verify this difference"
                for path, content in desired.items()
                if path not in (VERSION, SKILL_MAP)
                and comparison(current.get(path), path) != comparison(content, path)
            }
            baseline_required = baseline_required or bool(conflicts)
        pending = bool(conflicts) or baseline_required
        if planned:
            generated_changes(current, planned, tools)
    rows = []
    for path, content in sorted(planned.items()):
        previous = current.get(path)
        action = "retire" if content is None else "add" if previous is None else "update"
        rows.append({"action": action, "path": path.as_posix(),
                     "before": previous.digest() if previous else None,
                     "after": content.digest() if content else None,
                     "mode": content.mode if content else None})
    if planned:
        previous_log = read_file(target, AI_LOG)
        if previous_log is None or b"# AI log\n" not in previous_log.data:
            raise ValueError("The working vault's existing ASTORIA AI log could not be verified")
        status = "Pending items remain. Installed version was retained." if pending else "Verified the installed version and refreshed skill views."
        entry = (f"\n## {date.today().isoformat()} astoria-updater: ASTORIA {incoming_version}\n\n"
                 f"- Applied {len(rows)} approved file changes.\n"
                 f"- Held {len(conflicts)} files for review. {status}\n")
        planned[AI_LOG] = File(previous_log.data.replace(b"# AI log\n", b"# AI log\n" + entry.encode(), 1),
                               previous_log.mode)
        current[AI_LOG] = previous_log
    optional = sorted({path.relative_to(OPTIONAL).parts[0] for path in source
                       if path.is_relative_to(OPTIONAL) and path.name == "SKILL.md"
                       and ACTIVE / path.relative_to(OPTIONAL) not in current
                       and path not in current})
    report = {"source": str(source_root), "target": str(target),
              "baseline": str(baseline_root) if baseline_root else None,
              "version": incoming_version, "installed_version": installed_version,
              "pending": pending, "baseline_required": baseline_required,
              "changes": rows, "optional_available": optional,
              "conflicts": [{"path": path.as_posix(), "reason": reason}
                            for path, reason in sorted(conflicts.items())]}
    fingerprints = {path.as_posix(): [current[path].digest(), current[path].mode]
                    for path in planned if path in current}
    report["plan_id"] = hashlib.sha256(
        json.dumps([report, fingerprints], sort_keys=True).encode()
    ).hexdigest()
    return report, current, planned


def apply(target, current, planned):
    if not planned:
        return
    backup = Path(tempfile.mkdtemp(prefix="astoria_rollback_"))
    originals = backup / "original"
    applied = []
    existing_dirs = {parent for path in planned for parent in (target / path).parents
                     if parent.is_relative_to(target / ASTORIA) and parent.is_dir()}
    try:
        for path in planned:
            if path in current:
                write_file(originals, path, current[path])
        (backup / "restore.json").write_text(json.dumps(
            {"target": str(target), "files": [p.as_posix() for p in planned]}, indent=2))
        print(f"Rollback copy: {backup}", file=sys.stderr, flush=True)
        for path, content in planned.items():
            if read_file(target, path) != current.get(path):
                raise ValueError(f"File changed after preview: {path}")
            applied.append(path)
            write_file(target, path, content)
            if content is None:
                prune_empty_parents(target, path)
        for path, content in planned.items():
            if read_file(target, path) != content:
                raise ValueError(f"Applied file could not be verified: {path}")
    except (OSError, ValueError, KeyboardInterrupt):
        for path in reversed(applied):
            if read_file(target, path) == planned[path]:
                write_file(target, path, current.get(path))
                if path not in current:
                    prune_empty_parents(target, path, preserve=existing_dirs)
        raise
    shutil.rmtree(backup, ignore_errors=True)


def require_release(root, label):
    agents = read_file(root, Path("AGENTS.md"))
    draft = read_file(root, ASTORIA / "templates/agents_draft_template.md")
    if os.path.lexists(root / "me.md") or not (agents and draft and agents.data == draft.data):
        raise ValueError(f"Choose an original, unconfigured ASTORIA release as the {label}")


def overlapping(first, second):
    return first.samefile(second) or first.is_relative_to(second) or second.is_relative_to(first)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--verified-release", action="store_true",
                        help="Confirm the caller verified the official release and its helper bytes")
    parser.add_argument("--apply", metavar="PLAN_ID")
    args = parser.parse_args()
    try:
        if not args.verified_release:
            raise ValueError("Verify the official release and its helper bytes before running the updater")
        source = args.source.expanduser().resolve(strict=True)
        target = args.target.expanduser().resolve(strict=True)
        baseline = args.baseline.expanduser().resolve(strict=True) if args.baseline else None
        if overlapping(source, target) or (baseline and (overlapping(baseline, target) or overlapping(baseline, source))):
            raise ValueError("Select separate, non-overlapping update, original release and working vault folders")
        require_release(source, "update")
        if baseline:
            require_release(baseline, "original release")
        if not all((target / path).is_file() for path in ("me.md", "AGENTS.md", SKILL_MAP)):
            raise ValueError("Choose an existing ASTORIA working vault with completed setup")
        agents = read_file(target, Path("AGENTS.md"))
        draft = read_file(target, ASTORIA / "templates/agents_draft_template.md")
        if (b"setup pending" in agents.data.split(b"\n", 1)[0].lower()
                or (draft and agents.data == draft.data) or (target / TOOLKIT_STATE).exists()):
            raise ValueError("Finish or recover the existing setup before updating ASTORIA")
        if (target / ASTORIA / "exporter").exists() or (source / ASTORIA / "exporter").exists():
            raise ValueError("Use an exported starter as the source and an installed starter as the destination")
        report, current, planned = preview(source, target, baseline)
        if args.apply:
            if report["baseline_required"]:
                raise ValueError("Select the original official ASTORIA release before applying changes")
            if args.apply != report["plan_id"]:
                raise ValueError("The displayed preview changed. Run a new preview before applying")
            if planned:
                lock = safe_path(target, UPDATE_LOCK)
                try:
                    lock.mkdir()
                except FileExistsError as error:
                    raise ValueError("Another update is active or needs recovery") from error
                try:
                    apply(target, current, planned)
                finally:
                    lock.rmdir()
            report["applied"] = True
            report["installed_version"] = version(inventory(target))
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyboardInterrupt) as error:
        print(f"ASTORIA update stopped: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
