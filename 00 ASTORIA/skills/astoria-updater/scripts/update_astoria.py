"""Preview and apply a trusted ASTORIA release to an installed vault.

Verify the official release before supplying --verified-release.
Run with --source RELEASE --target VAULT and, when known, --baseline OLD_RELEASE.
Apply only the displayed plan with --apply PLAN_ID.
"""
import argparse
from dataclasses import dataclass
from datetime import date
import difflib
import hashlib
import importlib.util
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
LAYOUT = ASTORIA / "agent_notes/layout.md"
ACTIVE = ASTORIA / "skills"
OPTIONAL = ASTORIA / "specialized_skills"
VIEW_SCRIPT = ACTIVE / "skills-janitor/scripts/build_views.py"
LAYOUT_SCRIPT = ACTIVE / "vault-builder/scripts/build_layout.py"
LAYOUT_SECTIONS = re.compile(rb"^## (Files|Templates|Rules)\n.*?(?=^## |\Z)", re.M | re.S)
VOCABULARY = ACTIVE / "skill-builder/assets/vocabulary.md"
SELECTION = ASTORIA / "selection.json"
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


def resource_folder(files, parent, name):
    """Compare a complete release-owned resource folder by relative file and mode."""
    root = parent / name
    return {path.relative_to(root): content for path, content in files.items() if root in path.parents}


def recover_resource_ownership(current, baseline, target, names):
    """Recover only exact shipped resources omitted by an older selection record."""
    recovered = set()
    for name in names:
        actual = resource_folder(current, ACTIVE, name)
        original = resource_folder(baseline, ACTIVE, name)
        if not original:
            original = resource_folder(baseline, OPTIONAL, name)
        if not actual or actual != original:
            continue
        # The ordinary inventory skips hidden files. An extra supplied file,
        # including a hidden one, must not become official ownership by name.
        folder = safe_path(target, ACTIVE / name)
        complete = {}
        for path in folder.rglob("*"):
            info = path.lstat()
            if stat.S_ISDIR(info.st_mode):
                continue
            if not stat.S_ISREG(info.st_mode):
                raise ValueError("Resource ownership cannot include aliases or special files: " + str(path.relative_to(target)))
            complete[path.relative_to(folder)] = read_file(target, path.relative_to(target))
        if complete == original:
            recovered.add(name)
    return recovered


def release_selection(source, current, baseline, target, helper):
    """Use the verified release planner without treating a helper as a chosen system."""
    skills = {}
    for path, content in source.items():
        if path.name != "SKILL.md" or path.parent.parent not in (ACTIVE, OPTIONAL):
            continue
        name = path.parent.name
        if name in skills:
            raise ValueError("The release contains two copies of skill " + name)
        text = content.data.decode("utf-8")
        frontmatter, body = helper.parse_frontmatter(text)
        if frontmatter is None:
            raise ValueError("Release skill has no frontmatter: " + name)
        skills[name] = helper.Skill(name, path.parent.as_posix(), path.as_posix(),
                                   frontmatter, body, text)
    vocabulary = source.get(VOCABULARY)
    if vocabulary is None:
        raise ValueError("The release is missing its vocabulary")
    block = re.search(r"```yaml\n(.*?)\n```", vocabulary.data.decode("utf-8"), re.S)
    if block is None:
        raise ValueError("The release vocabulary has no YAML configuration")
    vocab = helper.yaml.safe_load(block[1])
    record = read_file(target, SELECTION)
    state = helper.read_selection(str(target))
    if read_file(target, SELECTION) != record:
        raise ValueError("The selection record changed during preview")
    choices = state["choices"] if state else {}
    active = {path.parent.name for path in current
              if path.name == "SKILL.md" and path.parent.parent == ACTIVE}
    original = {path.parent.name for path in baseline
                if path.name == "SKILL.md" and path.parent.parent in (ACTIVE, OPTIONAL)}
    if state:
        imported = set(state["imports"])
        removed = set(state["removed_skills"]) | ((set(state["installed_skills"]) | imported) - active)
        resources = set(vocab.get("starter", {}).get("basics_resources", []))
        # Preserve deletion of an old shipped resource even when its old record
        # omitted ownership. New resources absent from the baseline remain new.
        removed.update(name for name in resources - active
                       if resource_folder(baseline, ACTIVE, name))
        if set(state["removed_skills"]) & active:
            raise ValueError("A removed skill is present again; review selection.json before updating")
        unrecorded = (resources & active) - set(state["installed_skills"]) - imported - removed
        recovered = recover_resource_ownership(current, baseline, target, unrecorded)
        if unrecorded - recovered:
            raise ValueError("Unrecorded Basics resources need verified original release ownership; preserve custom files: "
                             + ", ".join(sorted(unrecorded - recovered)))
        protected = imported | (active - set(state["installed_skills"]) - imported - recovered)
    else:
        removed = {path.parent.name for path in baseline
                   if path.name == "SKILL.md" and path.parent.parent == ACTIVE} - active
        protected = active - original if baseline else set()
        recovered = set()
    # Deletions override saved choices before either dependency traversal.
    selected = helper.selection_plan(
        skills, vocab, systems=choices.get("systems", ()),
        groups=choices.get("research_groups", ()), names=choices.get("skills", ()),
        include_multimodal=choices.get("include_multimodal", True),
        removed_skills=removed,
    )
    owned = (set(state["installed_skills"]) | recovered) if state else original
    retained_names = (active & owned & skills.keys()) - protected - removed
    # A dependency correction does not remove an installed official capability.
    # Retain those exact skills individually; it never chooses their whole system.
    retained_choices = sorted(set(choices.get("skills", ())) | (retained_names - set(selected["installed_skills"])))
    selected = helper.selection_plan(
        skills, vocab, systems=choices.get("systems", ()),
        groups=choices.get("research_groups", ()), names=retained_choices,
        include_multimodal=choices.get("include_multimodal", True),
        removed_skills=removed,
    )
    allowed = (set(selected["installed_skills"]) | active) - removed - protected
    helpers = selected["required_helpers"]
    return {"state": state, "record": record, "allowed": allowed,
            "protected": protected, "removed": removed, "active": active,
            "helpers": helpers, "recovered_resources": recovered, "retained_choices": retained_choices,
            "vocabulary": helper.selection_vocabulary(vocab, active | allowed),
            "available": sorted(set(skills) - active - allowed - protected)}


def selection_vocabulary_text(content, configured, helper):
    """Change only coordinator configuration, retaining other vocabulary text."""
    text = content.data.decode("utf-8")
    block = re.search(r"```yaml\n(.*?)\n```", text, re.S)
    raw = block[1]
    for path in (("system_coordinators",), ("starter", "available_system_coordinators")):
        wanted = configured
        for key in path:
            wanted = wanted[key]
        current = helper.yaml.safe_load(raw)
        if path == ("system_coordinators",):
            present = current.get(path[0])
        else:
            present = (current.get("starter") or {}).get(path[1])
        if present == wanted:
            continue
        node = helper.yaml.compose(raw)
        key = path[0]
        pair = next(((k, v) for k, v in node.value if k.value == key), None)
        if len(path) == 2 and pair and not pair[1].flow_style:
            node = pair[1]
            key = path[1]
            pair = next(((k, v) for k, v in node.value if k.value == key), None)
        elif len(path) == 2:
            wanted = configured["starter"]
        if pair:
            key_node, value_node = pair
            indent = key_node.start_mark.column
            start = key_node.start_mark.index - indent
            end = value_node.end_mark.index
            if value_node.end_mark.column and end < len(raw) and raw[end] != "\n":
                end = raw.find("\n", end)
                if end == -1:
                    end = len(raw)
            if value_node.end_mark.column and end < len(raw) and raw[end] == "\n":
                end += 1
        else:
            indent = node.value[0][0].start_mark.column if node.value else 0
            start = end = node.end_mark.index
        rendered = helper.yaml.safe_dump({key: wanted}, sort_keys=False, allow_unicode=True)
        rendered = "".join(" " * indent + line for line in rendered.splitlines(keepends=True))
        if start and raw[start - 1] != "\n":
            rendered = "\n" + rendered
        raw = raw[:start] + rendered + raw[end:]
    if helper.yaml.safe_load(raw) != configured:
        raise ValueError("Selected coordinator configuration could not be preserved exactly")
    return File((text[:block.start(1)] + raw.rstrip("\n") + text[block.end(1):]).encode("utf-8"),
                content.mode)


def installed_paths(files, current, tools, allowed=(), protected=(), removed=(),
                    configured=None, helper=None):
    """Render release links using the same installed options as the destination."""
    result = {}
    moves, absent = {}, set()
    for path, content in files.items():
        root = next((root for root in (ACTIVE, OPTIONAL) if path.is_relative_to(root)), None)
        if root:
            suffix = path.relative_to(root)
            name = suffix.parts[0]
            if name in protected or name in removed:
                if ACTIVE / name / "SKILL.md" not in current:
                    absent.add(name)
                continue
            if ACTIVE / name / "SKILL.md" in current or name in allowed:
                destination = ACTIVE
            elif OPTIONAL / name / "SKILL.md" not in current:
                absent.add(name)
                continue
            else:
                destination = OPTIONAL
            if root != destination:
                moves[(root / name).as_posix()] = (destination / name).as_posix()
            path = destination / suffix
        if path in result:
            raise ValueError(f"Two release files resolve to the same installed path: {path}")
        result[path] = content
    if configured is not None:
        result[VOCABULARY] = selection_vocabulary_text(result[VOCABULARY], configured, helper)
    if not (moves or absent):
        return result

    with tempfile.TemporaryDirectory(prefix="astoria_links_") as folder:
        stage = Path(folder)
        for path, content in result.items():
            write_file(stage, path, content)
        for path, content in current.items():
            if path.is_relative_to(ACTIVE) and path.parts[2] in protected:
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
        return {path: content for path, content in inventory(stage).items()
                if not (path.is_relative_to(ACTIVE) and path.parts[2] in protected)}


def plan_selection_refresh(scope, current, planned):
    """Keep existing choices and imported ownership while recording this transaction."""
    state = scope["state"]
    if state is None:
        return
    updated = json.loads(json.dumps(state))
    active = set(scope["active"])
    added = set()
    for path, content in planned.items():
        if path.name == "SKILL.md" and path.parent.parent == ACTIVE:
            if content is None:
                active.discard(path.parent.name)
            else:
                active.add(path.parent.name)
                added.add(path.parent.name)
    previous = set(state["installed_skills"])
    owned = ((previous | added | scope["recovered_resources"]) & active) - scope["protected"] - scope["removed"]
    updated["installed_skills"] = sorted(owned)
    updated["choices"]["skills"] = scope["retained_choices"]
    updated["removed_skills"] = sorted(set(state["removed_skills"]) | scope["removed"] | (previous - active))
    reasons = {name: values for name, values in scope["helpers"].items() if name in owned}
    updated["required_helpers"] = reasons
    if updated != state:
        record = scope["record"]
        current[SELECTION] = record
        planned[SELECTION] = File((json.dumps(updated, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
                                  record.mode)


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


def merge_vocabulary(original, current, incoming, imported_skills=()):
    """Keep disjoint configuration edits without rewriting recipient comments."""
    try:
        import yaml
    except ImportError:
        return None, "PyYAML is required to compare customized vocabulary configuration"

    class UniqueKeys(yaml.SafeLoader):
        pass

    def mapping(loader, node):
        values = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=True)
            if not isinstance(key, str) or key in values:
                raise ValueError("Vocabulary configuration has a duplicate or unsupported mapping key")
            values[key] = loader.construct_object(value_node, deep=True)
        return values

    UniqueKeys.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

    def configuration(text):
        blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
        if len(blocks) != 1:
            raise ValueError("Vocabulary must contain one YAML configuration block")
        value = yaml.load(blocks[0], Loader=UniqueKeys)
        if not isinstance(value, dict):
            raise ValueError("Vocabulary configuration must be a mapping")
        return value

    missing = object()

    def combine(before, live, after):
        if live == before:
            return after
        if after == before or live == after:
            return live
        if all(isinstance(value, dict) for value in (before, live, after)):
            result = {}
            for key in before.keys() | live.keys() | after.keys():
                value = combine(before.get(key, missing), live.get(key, missing), after.get(key, missing))
                if value is not missing:
                    result[key] = value
            return result
        # Lists are a single choice; do not infer how to combine two changed orders.
        raise ValueError("Local and release vocabulary configuration changes overlap")

    def writing_group_items(text, group):
        block = re.search(r"```yaml\n(.*?)\n```", text, re.S)
        node = yaml.compose(block[1])
        for name in ("system_sections", "Writing System", group):
            node = next(value for key, value in node.value if key.value == name)
        if not isinstance(node, yaml.SequenceNode) or node.flow_style:
            raise ValueError("Customized Writing groups need block lists for a safe import merge")
        return block.start(1), node.value

    def item_line(text, offset, node):
        start = text.rfind("\n", 0, offset + node.start_mark.index) + 1
        end = text.find("\n", offset + node.end_mark.index)
        return start, len(text) if end == -1 else end + 1

    try:
        before, live, after = (content.data.decode("utf-8") for content in (original, current, incoming))
        configurations = [configuration(text) for text in (before, live, after)]
        sections = []
        for value in configurations:
            groups = value.get("system_sections")
            writing = groups.get("Writing System") if isinstance(groups, dict) else None
            sections.append(writing if isinstance(writing, dict) else {})
        preserved, removals = {}, []
        for group, old_names in sections[0].items():
            live_names, new_names = sections[1].get(group), sections[2].get(group)
            if not all(isinstance(names, list) for names in (old_names, live_names, new_names)):
                continue
            if any(not isinstance(name, str) for names in (old_names, live_names, new_names) for name in names):
                continue
            extra = set(live_names) & set(imported_skills) - set(old_names)
            if (not extra or new_names == old_names or extra.intersection(new_names)
                    or [name for name in live_names if name not in extra] not in (old_names, new_names)):
                continue
            # Only recipient-owned imported additions can be set aside. Any
            # local change to official membership or order still conflicts.
            for text in (before, after):
                writing_group_items(text, group)
            offset, items = writing_group_items(live, group)
            retained = []
            for index, node in enumerate(items):
                if node.value in extra:
                    start, end = item_line(live, offset, node)
                    retained.append((node.value, live[start:end], live_names[index + 1:]))
                    removals.append((start, end))
            preserved[group] = retained
        for start, end in sorted(removals, reverse=True):
            live = live[:start] + live[end:]
        live_configuration = configuration(live)
        expected = combine(configuration(before), live_configuration, configuration(after))
        base_lines = before.splitlines(keepends=True)
        edits = []
        for text in (live, after):
            lines = text.splitlines(keepends=True)
            for tag, start, end, other_start, other_end in difflib.SequenceMatcher(
                    None, base_lines, lines, autojunk=False).get_opcodes():
                if tag == "equal":
                    continue
                edit = (start, end, lines[other_start:other_end])
                if edit in edits:
                    continue
                for previous_start, previous_end, _ in edits:
                    overlap = max(start, previous_start) < min(end, previous_end)
                    insertion = ((start == end and previous_start <= start <= previous_end)
                                 or (previous_start == previous_end and start <= previous_start <= end))
                    if overlap or insertion:
                        raise ValueError("Vocabulary text changes overlap; review the configuration before updating")
                edits.append(edit)
        for start, end, replacement in sorted(edits, reverse=True):
            base_lines[start:end] = replacement
        merged = "".join(base_lines)
        for group, retained in preserved.items():
            names = expected["system_sections"]["Writing System"][group]
            for name, line, following in retained:
                offset, items = writing_group_items(merged, group)
                anchor = next((value for value in following if value in names), None)
                if anchor is None:
                    position = item_line(merged, offset, items[-1])[1]
                    names.append(name)
                else:
                    node = next(item for item in items if item.value == anchor)
                    position = item_line(merged, offset, node)[0]
                    names.insert(names.index(anchor), name)
                indent = items[0].start_mark.column - 2
                merged = merged[:position] + " " * indent + line.lstrip(" ") + merged[position:]
        if configuration(merged) != expected:
            raise ValueError("Combined vocabulary does not preserve both configuration changes")
        return File(merged.encode("utf-8"), current.mode), None
    except (UnicodeError, ValueError, yaml.YAMLError, RecursionError) as error:
        return None, str(error)


def select_changes(current, source, baseline, imported_skills=()):
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
        if path == VOCABULARY and all(path in files for files in (baseline, current, source)) and live != before:
            merged, reason = merge_vocabulary(baseline[path], current[path], source[path], imported_skills)
            if reason:
                conflicts[path] = reason
            elif merged != current[path]:
                changes[path] = merged
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
    if VOCABULARY in conflicts:
        # Coordinators and their vocabulary form one coherent installation.
        # Report the conflict before trying incoming catalogs against old settings.
        for path in changes:
            conflicts[path] = "Held until the vocabulary configuration conflict is resolved"
        changes.clear()
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
                                           "present in both", "folder has no SKILL.md",
                                           "metadata.system "))]
        if problems:
            raise ValueError("Skill verification found conflicts: " + "; ".join(problems))
        rendered = inventory(stage)
        for path, content in rendered.items():
            if staged.get(path) != content:
                if path != SKILL_MAP and comparison(staged.get(path), path) != comparison(content, path):
                    raise ValueError(f"View generation tried to change a non-generated file: {path}")
                planned[path] = content


def layout_sections(files, source):
    """Render the release-controlled layout sections without reading vault notes."""
    with tempfile.TemporaryDirectory(prefix="astoria_layout_") as folder:
        stage = Path(folder)
        for path, content in files.items():
            if (path == VOCABULARY or path.is_relative_to(ASTORIA / "templates")
                    or (path.is_relative_to(ACTIVE) and path.name == "SKILL.md")):
                write_file(stage, path, content)
        for helper in (LAYOUT_SCRIPT, VIEW_SCRIPT.with_name("skillkit.py")):
            write_file(stage, helper, source[helper])
        add_stage_placeholders(stage)
        run_check([sys.executable, "-E", "-B", str(stage / LAYOUT_SCRIPT),
                   "--vault", str(stage), "--apply"], "Layout sections could not be generated", stage)
        matches = list(LAYOUT_SECTIONS.finditer((stage / LAYOUT).read_bytes()))
        sections = {match[1]: match[0] for match in matches}
        if len(matches) != 3 or sections.keys() != {b"Files", b"Templates", b"Rules"}:
            raise ValueError("The release layout uses an unexpected section format. Check the installed layout separately.")
        return sections


def plan_layout_refresh(target, current, planned, source):
    """Preview only layout sections changed by the package transaction."""
    if not any(path == VOCABULARY or path.is_relative_to(ASTORIA / "templates")
               or (path.is_relative_to(ACTIVE) and path.name == "SKILL.md") for path in planned):
        return []
    if LAYOUT_SCRIPT not in source:
        return ["The release has no layout helper. Check the installed layout separately."]
    installed = dict(current)
    for path, content in planned.items():
        if content is None:
            installed.pop(path, None)
        else:
            installed[path] = content
    try:
        before = layout_sections(current, source)
        after = layout_sections(installed, source)
        changed = {name: text for name, text in after.items() if text != before.get(name)}
        if not changed:
            return []
        existing = read_file(target, LAYOUT)
    except (OSError, ValueError) as error:
        return [str(error)]
    if existing is None:
        return ["The installed layout is absent. Run the layout audit before rebuilding it."]
    sections = list(LAYOUT_SECTIONS.finditer(existing.data))
    refresh, review = {}, []
    for name, replacement in changed.items():
        matches = [match for match in sections if match[1] == name]
        if len(matches) == 1 and matches[0][0] == before.get(name):
            refresh[name] = replacement
        elif len(matches) != 1 or matches[0][0] != replacement:
            review.append("The installed layout section differs from expected generated text: "
                          + name.decode("ascii"))
    if refresh:
        current[LAYOUT] = existing
        planned[LAYOUT] = File(LAYOUT_SECTIONS.sub(lambda match: refresh.get(match[1], match[0]),
                                                 existing.data), existing.mode)
    return review


def preview(source_root, target, baseline_root):
    source = inventory(source_root)
    current = inventory(target)
    baseline = inventory(baseline_root) if baseline_root else {}
    selection_record = read_file(target, SELECTION)
    if selection_record is not None:
        current[SELECTION] = selection_record
    selection_review = []
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
        spec = importlib.util.spec_from_file_location("astoria_verified_release_skillkit", tools / "skillkit.py")
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        scope = None
        try:
            scope = release_selection(source, current, baseline, target, helper)
            if scope["record"] != selection_record:
                raise ValueError("The selection record changed during preview")
            desired = installed_paths(source, current, tools, scope["allowed"],
                                      scope["protected"], scope["removed"],
                                      scope["vocabulary"], helper)
        except (OSError, ValueError, KeyError, TypeError) as error:
            selection_review.append(str(error))
            desired = {}
        baseline_required = baseline_root is None and installed_version != incoming_version
        if selection_review:
            planned, conflicts = {}, {SELECTION: selection_review[0]}
        elif baseline_root:
            original = installed_paths(baseline, current, tools,
                                       protected=scope["protected"], removed=scope["removed"])
            imports = scope["state"]["imports"] if scope["state"] else ()
            planned, conflicts = select_changes(current, desired, original, imports)
            plan_selection_refresh(scope, current, planned)
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
            if not conflicts:
                plan_selection_refresh(scope, current, planned)
        pending = bool(conflicts) or baseline_required
        if planned:
            try:
                generated_changes(current, planned, tools)
            except ValueError as error:
                # Retained local skills may still use the older catalog schema.
                # Keep the installation coherent and show the conflict, not a partial apply.
                conflicts[SKILL_MAP] = "Generated skill views require review before this update: " + str(error)
                for path in planned:
                    conflicts.setdefault(path, "Held until the generated skill-view conflict is resolved")
                planned.clear()
                pending = True
    layout_review = plan_layout_refresh(target, current, planned, source)
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
                 f"- Held {len(conflicts)} files for review. {status}\n"
                 + ("- Refreshed release-controlled sections of the generated layout.\n" if LAYOUT in planned else "")
                 + ("- Some generated layout sections need a separate audit.\n" if layout_review else ""))
        planned[AI_LOG] = File(previous_log.data.replace(b"# AI log\n", b"# AI log\n" + entry.encode(), 1),
                               previous_log.mode)
        current[AI_LOG] = previous_log
    optional = scope["available"] if scope else []
    report = {"source": str(source_root), "target": str(target),
              "baseline": str(baseline_root) if baseline_root else None,
              "version": incoming_version, "installed_version": installed_version,
              "pending": pending, "baseline_required": baseline_required,
              "changes": rows, "optional_available": optional,
              "selection_sha256": selection_record.digest() if selection_record else None,
              "selection_review": selection_review,
              "layout_review": layout_review,
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
    if read_file(target, SELECTION) != current.get(SELECTION):
        raise ValueError(f"File changed after preview: {SELECTION}")
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
        if SELECTION not in planned and read_file(target, SELECTION) != current.get(SELECTION):
            raise ValueError(f"File changed during apply: {SELECTION}")
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
