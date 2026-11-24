#!/usr/bin/env python3
r"""File: install_specialized.py | Purpose: Select ASTORIA options or import one ready-made skill.
Inputs/outputs: Existing active/shelf folders; recipient-owned selection.json.
Requires: Python 3 and PyYAML. Dry run by default; --apply performs the shown plan.
Examples:
    python3 -B install_specialized.py --list
    python3 -B install_specialized.py --systems study,teaching --groups eeg --apply
    python3 -B install_specialized.py --none --apply
    python3 -B install_specialized.py --import-skill https://github.com/owner/repo/tree/main/skills/example
    python3 -B install_specialized.py --register-skill example --source-kind workflow --source pasted --apply
GitHub references resolve to a commit before downloading. Imported code is never executed.
"""

# Step 0. Use the existing skill, view and lint machinery.
import argparse
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillkit as sk

DEFAULT_INCLUDE_MULTIMODAL = True
GENERAL_GROUP_NAME = "general"
SKIP_IMPORT = {".git", "__pycache__", ".DS_Store", ".venv", "node_modules"}
INSTALL_STATE = ".toolkit-install-in-progress.json"


def argument(argv, flag, default=None):
    if flag in argv:
        position = argv.index(flag)
        if position + 1 >= len(argv) or argv[position + 1].startswith("--"):
            raise ValueError("%s needs a value" % flag)
        return argv[position + 1]
    return default


def catalog_groups(catalog, vocab):
    return sk.research_groups(catalog, vocab)


def plan(catalog, vocab, chosen_groups, extra_names, include_multimodal):
    selected = sk.selection_plan(catalog, vocab, groups=chosen_groups, names=extra_names,
                                 include_multimodal=include_multimodal)
    return {name: "; ".join(reasons) for name, reasons in selected["reasons"].items()}, catalog_groups(catalog, vocab)


def import_files(folder):
    """Inventory every supplied supporting file, refusing aliases and escapes."""
    folder = Path(folder)
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError("Choose a real skill folder, not a directory alias")
    files = {}
    for parent, directories, names in os.walk(folder, followlinks=False):
        for name in directories + names:
            path = Path(parent) / name
            if name not in SKIP_IMPORT and path.is_symlink():
                raise ValueError("Imported supporting files must not be aliases: " + str(path))
        directories[:] = sorted(name for name in directories if name not in SKIP_IMPORT)
        for name in sorted(names):
            if name in SKIP_IMPORT:
                continue
            path = Path(parent) / name
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise ValueError("Imported support must be a regular file: " + str(path))
            relative = path.relative_to(folder).as_posix()
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    if "SKILL.md" not in files:
        raise ValueError("Choose a folder containing SKILL.md")
    return files


def preflight_tree(folder):
    """Check the complete installed/shelf tree before loading any metadata."""
    folder = Path(folder)
    if not folder.exists() and not folder.is_symlink():
        return
    if folder.is_symlink() or not folder.is_dir() or folder.resolve(strict=True) != folder:
        raise ValueError("Installation tree must not be a directory alias: " + str(folder))
    for parent, directories, names in os.walk(folder, followlinks=False):
        for name in directories + names:
            path = Path(parent) / name
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode) or path.resolve(strict=True) != path:
                raise ValueError("Installation tree contains an alias: " + str(path))
            if not stat.S_ISDIR(info.st_mode) and (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1):
                raise ValueError("Installation tree requires regular files without aliases: " + str(path))


def check_import_references(folder, skill=None, available=None):
    """Check explicit local support links and named scripts before installing."""
    root = Path(folder).resolve()
    problems = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        links = re.findall(r'!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)', text)
        links += re.findall(r'(?m)^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', text)
        links += re.findall(r'(?:href|src)=["\']([^"\']+)["\']', text)
        links += re.findall(r'(?<![A-Za-z0-9_/])((?:\./)?(?:scripts|references|assets)/[^\s`"\'<>),;]+)', text)
        for target in links:
            target = target.strip("<>").rstrip(".")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path or re.search(r"[{}<>]|\.\.\.|…", target):
                continue
            requested = (path.parent / unquote(parsed.path)).resolve()
            try:
                requested.relative_to(root)
            except ValueError:
                pieces = Path(unquote(parsed.path)).parts
                dependencies = skill.dependencies if skill is not None else []
                supported = False
                for index, piece in enumerate(pieces):
                    if piece in dependencies and available is not None and piece in available:
                        support_target = Path(available[piece].path).parent.joinpath(*pieces[index + 1:])
                        if support_target.is_file():
                            supported = True
                            break
                if supported:
                    continue
                problems.append(path.relative_to(root).as_posix() + ": support link escapes the imported folder: " + target)
                continue
            if not requested.exists():
                problems.append(path.relative_to(root).as_posix() + ": supporting file is missing: " + target)
    if problems:
        raise ValueError("Import is incomplete; preserve the supplied support or resolve its references:\n" + "\n".join(sorted(set(problems))))


def github_json(url):
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "ASTORIA-skill-import"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def github_location(url):
    """Validate the original URL without resolving a moving reference."""
    parsed = urlsplit(url)
    parts = [unquote(part) for part in parsed.path.strip("/").split("/")]
    if parsed.scheme != "https" or parsed.netloc != "github.com" or len(parts) < 2 or parsed.query or parsed.fragment:
        raise ValueError("Use an HTTPS GitHub repository or folder link")
    owner, repository = parts[:2]
    repository = repository.removesuffix(".git")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", owner) or not re.fullmatch(r"[A-Za-z0-9_.-]+", repository):
        raise ValueError("Invalid GitHub repository link")
    if len(parts) != 2 and (parts[2] != "tree" or len(parts) < 4):
        raise ValueError("Choose a repository or tree/folder URL, not a file URL")
    return owner, repository, parts


def validate_github_pin(url, pin):
    """Require a complete saved import snapshot from this exact repository."""
    owner, repository, unused = github_location(url)
    fields = {"owner", "source_kind", "source", "revision", "source_path", "files"}
    if (not isinstance(pin, dict) or set(pin) != fields or pin["owner"] != "user"
            or pin["source_kind"] != "github"
            or pin["source"] != "https://github.com/" + owner + "/" + repository
            or not isinstance(pin["revision"], str) or not re.fullmatch(r"[0-9a-f]{40}", pin["revision"])):
        raise ValueError("The interrupted GitHub import has no valid saved repository and commit")

    def relative_path(value, allow_root=False):
        if not isinstance(value, str):
            return False
        if allow_root and value == "":
            return True
        path = Path(value)
        return (bool(value) and bool(path.parts) and not path.is_absolute() and "\\" not in value
                and path.as_posix() == value and all(part not in {".", ".."} for part in path.parts))

    files = pin["files"]
    if (not relative_path(pin["source_path"], allow_root=True)
            or not isinstance(files, dict) or "SKILL.md" not in files
            or any(not relative_path(path) or not isinstance(digest, str)
                   or not re.fullmatch(r"[0-9a-f]{64}", digest) for path, digest in files.items())):
        raise ValueError("The interrupted GitHub import has invalid saved paths or file hashes")


def github_folder(url, destination, pin=None):
    """Extract one complete skill, reusing a verified saved commit during recovery."""
    owner, repository, parts = github_location(url)
    api = "https://api.github.com/repos/" + owner + "/" + repository
    subpath = ""
    if pin is not None:
        validate_github_pin(url, pin)
        commit, subpath = pin["revision"], pin["source_path"]
    elif len(parts) == 2:
        reference = github_json(api)["default_branch"]
        commit = github_json(api + "/commits/" + quote(reference, safe=""))["sha"]
    else:
        commit = None
        # Branch names may contain slashes. Resolve the longest real ref first.
        for count in range(len(parts) - 3, 0, -1):
            reference = "/".join(parts[3:3 + count])
            try:
                commit = github_json(api + "/commits/" + quote(reference, safe=""))["sha"]
                subpath = "/".join(parts[3 + count:])
                break
            except HTTPError as error:
                if error.code != 404:
                    raise
        if commit is None:
            raise ValueError("The GitHub branch, tag or commit could not be resolved")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise ValueError("GitHub did not return a pinned commit")
    commit = commit.lower()
    with urlopen(Request("https://codeload.github.com/" + owner + "/" + repository + "/zip/" + commit,
                         headers={"User-Agent": "ASTORIA-skill-import"}), timeout=30) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        members = archive.infolist()
        roots = {member.filename.split("/")[0] for member in members}
        if len(roots) != 1:
            raise ValueError("Unexpected GitHub archive layout")
        root = next(iter(roots)) + "/"
        prefix = root + (subpath.rstrip("/") + "/" if subpath else "")
        skills = sorted(member.filename[len(root):-len("/SKILL.md")] for member in members
                        if member.filename.startswith(prefix) and member.filename.endswith("/SKILL.md")
                        and not any(part in SKIP_IMPORT for part in Path(member.filename).parts))
        exact = subpath if prefix + "SKILL.md" in archive.namelist() else None
        if pin is not None and exact is None:
            raise ValueError("The saved GitHub skill folder is missing at its pinned commit")
        if exact is not None:
            selected = exact
        elif len(skills) == 1:
            selected = skills[0]
        else:
            choices = ["https://github.com/" + owner + "/" + repository + "/tree/" + commit + "/" + name for name in skills]
            raise ValueError("Choose one actual skill folder from this repository:\n" + ("\n".join(choices) or "No SKILL.md folders found"))
        prefix = root + (selected.rstrip("/") + "/" if selected else "")
        destination = Path(destination)
        for member in members:
            if not member.filename.startswith(prefix):
                continue
            mode = member.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError("The GitHub skill contains a supporting-file alias")
            if member.is_dir():
                continue
            relative = member.filename[len(prefix):]
            path = Path(relative)
            if path.is_absolute() or ".." in path.parts or "\\" in relative or not path.parts:
                raise ValueError("The GitHub archive contains an escaping path")
            if any(part in SKIP_IMPORT for part in path.parts):
                continue
            target = destination / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(member))
            if mode & 0o111:
                target.chmod(0o755)
        # Repository-wide rights accompany a nested skill even when not repeated there.
        for member in members:
            relative = member.filename[len(root):]
            if "/" in relative or not re.match(r"(?i)^(LICENSE|COPYING|NOTICE)(?:[._-].*)?$", relative):
                continue
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError("The upstream rights file must not be an alias")
            content = archive.read(member)
            target = destination / relative
            if target.exists() and target.read_bytes() != content:
                target = destination / "references" / "upstream_rights" / relative
            if target.exists() and target.read_bytes() != content:
                raise ValueError("Upstream rights collision; preserve both existing notices and choose a distinct destination: " + relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    return {"owner": "user", "source_kind": "github", "source": "https://github.com/" + owner + "/" + repository,
            "revision": commit, "source_path": selected}


def candidate_skill(folder, vocabulary, available, registering=False):
    folder = Path(folder)
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    frontmatter, body = sk.parse_frontmatter(text)
    if not frontmatter or "__error__" in frontmatter:
        raise ValueError("Imported skill needs valid Agent Skills frontmatter")
    name = frontmatter.get("name", "")
    if not isinstance(name, str) or not sk.SKILL_NAME_RE.fullmatch(name) or len(name) > 64:
        raise ValueError("Imported skill needs a standard skill name")
    if name in available and not registering:
        raise ValueError("A skill named " + name + " already exists; resolve naming/ownership before importing")
    if set(frontmatter) - sk.ALLOWED_TOP:
        raise ValueError("Normalize imported frontmatter through Skill Builder; preserve its workflow and rights")
    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict) or any(key not in metadata for key in sk.CORE_META):
        raise ValueError("Skill Builder must supply the ASTORIA metadata before installation")
    if any(not isinstance(value, str) for value in metadata.values()):
        raise ValueError("Imported metadata values must be strings")
    skill = sk.Skill(name, "", str(folder / "SKILL.md"), frontmatter, body, text)
    if skill.level not in vocabulary["levels"] or skill.system not in vocabulary["systems"]:
        raise ValueError("Choose an existing level and system through Skill Builder")
    if not skill.description or len(skill.description) > int(vocabulary.get("description_max_chars", 1000)):
        raise ValueError("Imported description must contain 1 to 1,000 characters")
    low, high = vocabulary["trigger_counts"][skill.level]
    if not low <= len(skill.triggers) <= high or skill.description.count("Triggers:") > 1:
        raise ValueError("Imported trigger count does not match its level")
    for trigger in skill.triggers:
        normalized = trigger.lower()
        if normalized in {name, name.replace("-", " ")} or normalized.startswith("run " + name):
            raise ValueError("Imported trigger repeats its skill name")
        for other in available.values():
            if registering and other.name == name:
                continue
            if any(normalized in phrase.lower() or phrase.lower() in normalized for phrase in other.triggers):
                raise ValueError("Imported trigger overlaps " + other.name + ": " + trigger)
    for dependency in skill.dependencies:
        if dependency not in available and dependency != name:
            raise ValueError("Resolve imported dependency before installation: " + dependency)
    if skill.system == "Research Assistant System" and skill.level in {"skill", "coordinator"}:
        for field, values in (("part", vocabulary.get("parts", {})), ("family", vocabulary.get("families", {})),
                              ("modality", vocabulary.get("modalities", [])), ("population", vocabulary.get("populations", []))):
            for value in metadata.get(field, "").split(","):
                if value.strip() and value.strip() not in values:
                    raise ValueError("Imported research " + field + " is outside the vocabulary")
    for field in ("created", "updated"):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", metadata[field]):
            raise ValueError("Imported dates must use YYYY-MM-DD")
    return skill


def imported_writing_group(vocabulary, skill, requested=None):
    """Assign one configured Writing group without duplicating existing ownership."""
    if skill.system != "Writing System":
        if requested:
            raise ValueError("--writing-group applies only to a Writing System import")
        return vocabulary, None
    result = copy.deepcopy(vocabulary)
    groups = result.get("system_sections", {}).get("Writing System")
    if not groups:
        if requested:
            raise ValueError("This vault has no configured Writing groups; use its actual vocabulary")
        return result, None  # Older flat registries do not require grouped ownership.
    owners = [heading for heading, names in groups.items() if skill.name in names]
    if len(owners) > 1:
        raise ValueError("The imported Writing skill is already assigned to multiple groups")
    if owners:
        if requested and requested != owners[0]:
            raise ValueError("The skill already belongs to Writing group " + owners[0])
        return result, owners[0]
    if skill.level == "profile":
        inferred = "Writing style"
    elif skill.level in {"companion", "coordinator"}:
        inferred = "Companion and coordination"
    else:
        inferred = "Writing assistance"
    group = requested or inferred
    if group not in groups or not isinstance(groups[group], list):
        raise ValueError("Choose an existing Writing group: " + ", ".join(groups))
    groups[group].append(skill.name)
    return result, group


def save_vocabulary(vault, vocabulary):
    path = Path(vault) / sk.VOCAB_REL
    text = path.read_text(encoding="utf-8")
    block = "```yaml\n" + sk.yaml.safe_dump(vocabulary, sort_keys=False, allow_unicode=True) + "```"
    rewritten, count = re.subn(r"```yaml\n.*?\n```", lambda match: block, text, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Vocabulary configuration block is missing")
    path.write_text(rewritten, encoding="utf-8")


def directory_identity(path):
    info = path.lstat()
    if not stat.S_ISDIR(info.st_mode):
        raise ValueError("Expected an actual directory at %s" % path)
    return [info.st_dev, info.st_ino]


def digest_entries(entries):
    return hashlib.sha256(json.dumps(entries, sort_keys=True).encode("utf-8")).hexdigest()


def tree_digest(root, ignore=()):
    entries = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts[0] in ignore:
            continue
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            entries[relative.as_posix()] = None
        elif stat.S_ISREG(info.st_mode):
            if path.suffix.lower() == ".md" and info.st_nlink != 1:
                raise ValueError("Cannot verify a hard-linked Markdown file at %s" % path)
            entries[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            raise ValueError("Cannot verify non-regular catalog or skill entry at %s" % path)
    return digest_entries(entries)


def relocation_map(names):
    return {os.path.join(sk.CATALOG_REL, name): os.path.join(sk.SKILLS_REL, name)
            for name in sorted(names)}


def document_digest(vault, relocations, unavailable):
    """Hash the pre-repair Markdown at its projected final paths."""
    links = sk.PortableLinks(vault, relocations, unavailable)
    if links.problems:
        raise ValueError("\n".join(links.problems))
    entries = {}
    for relative in sorted(links.files & set(documents(vault))):
        target = links._relocate(relative)
        if target in entries:
            raise ValueError("Two documents resolve to the same install path: %s" % target)
        original = links.read_markdown(relative)
        entries[target] = [links.identities[relative], hashlib.sha256(original).hexdigest()]
    return digest_entries(entries)


def state_record(path):
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError("The install-state path is not a regular file without aliases")
    return json.loads(path.read_text(encoding="utf-8")), [info.st_dev, info.st_ino]


def write_state(path, data):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    with os.fdopen(os.open(path, flags, 0o600), "w", encoding="utf-8") as handle:
        json.dump(data, handle, sort_keys=True)
        handle.flush()
        os.fsync(handle.fileno())
    return state_record(path)[1]


def verify_state(data, request, catalog_dir, live_dir, vault):
    if (not isinstance(data, dict) or data.get("version") != 2
            or data.get("request") != request or not isinstance(data.get("selected"), dict)):
        raise ValueError("Retry requires the exact originally approved selection and options")
    selected = data["selected"]
    if not selected or any(not name or name.startswith(".") or "/" in name or "\\" in name
                           for name in selected):
        raise ValueError("The recorded skill names are invalid")
    relocations = relocation_map(selected)
    if relocations != data.get("relocations"):
        raise ValueError("The recorded relocations are invalid")
    if (directory_identity(catalog_dir) != data.get("catalog_dir")
            or directory_identity(live_dir) != data.get("live_dir")):
        raise ValueError("The catalog or live directory identity changed")
    if tree_digest(catalog_dir, selected) != data.get("catalog_remaining"):
        raise ValueError("The remaining catalog changed since the approved move plan")

    moved = set()
    for name, expected in selected.items():
        src, dst = catalog_dir / name, live_dir / name
        candidates = [path for path in (src, dst) if os.path.lexists(path)]
        if len(candidates) != 1:
            raise ValueError("Expected exactly one catalog or live folder for %s" % name)
        path = candidates[0]
        actual = [directory_identity(path), tree_digest(path)]
        if actual != expected:
            raise ValueError("Folder identity or content changed for %s" % name)
        if path == dst:
            moved.add(name)
    if document_digest(vault, relocations, data["unavailable"]) != data.get("documents"):
        raise ValueError("Pre-link document identity or bytes changed; verify the install state")
    return moved


def start_state(path, request, catalog_dir, live_dir, vault, install, unavailable):
    # Verify all selected destinations before recording or moving any folder.
    catalog_identity = directory_identity(catalog_dir)
    live_identity = directory_identity(live_dir)
    if any(name.startswith('.') for name in install):
        raise ValueError("Hidden catalog folders cannot be selected")
    live_names = {entry.name.casefold() for entry in live_dir.iterdir()}
    for name in install:
        if name.casefold() in live_names or os.path.lexists(live_dir / name):
            raise ValueError("Live destination is already occupied for %s" % name)
    selected = {name: [directory_identity(catalog_dir / name), tree_digest(catalog_dir / name)]
                for name in install}
    relocations = relocation_map(install)
    data = {"version": 2, "request": request, "selected": selected,
            "catalog_dir": catalog_identity, "live_dir": live_identity,
            "catalog_remaining": tree_digest(catalog_dir, selected), "relocations": relocations,
            "unavailable": unavailable,
            "documents": document_digest(vault, relocations, unavailable)}
    return data, write_state(path, data)


def stop_install(error):
    print("Toolkit installation stopped: %s" % error)
    print("Keep the catalog and existing files. Retry only with the exact approved options "
          "and verified install state, or use manual recovery after inspecting the files.")
    return 1



def documents(vault):
    """Only ASTORIA installation documents are eligible for link/view changes."""
    root = Path(vault)
    selected = [root / sk.MAP_REL, root / "README.md", root / "AGENTS.md"]
    for relative in (sk.SKILLS_REL, sk.CATALOG_REL, sk.SYSTEMS_REL):
        folder = root / relative
        if folder.is_symlink():
            raise ValueError("The installation must not use directory aliases: " + relative)
        if folder.exists():
            selected.extend(folder.rglob("*.md"))
    for path in selected:
        if path.exists() and (path.is_symlink() or path.resolve(strict=True) != path or path.stat().st_nlink != 1):
            raise ValueError("Installation document must not be an alias: " + str(path))
    return sorted({path.relative_to(root).as_posix() for path in selected if path.is_file()})


def main(argv):
    # Step 1. Resolve the requested choices before any write.
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ("systems", "groups", "names", "vault", "import-skill", "register-skill", "source-kind", "source", "revision", "source-path", "writing-group", "assume-notes"):
        parser.add_argument("--" + flag)
    for flag in ("list", "none", "apply", "no-multimodal", "remove-catalog"):
        parser.add_argument("--" + flag, action="store_true")
    try:
        options = parser.parse_args(argv)
        request_options = {key: value for key, value in vars(options).items()
                           if key not in {"apply", "list", "vault"}}
        if options.none and any((options.systems, options.groups, options.names, options.import_skill, options.register_skill)):
            raise ValueError("--none cannot be combined with optional choices or imports")
        if options.import_skill and options.register_skill:
            raise ValueError("Choose one imported folder or one existing workflow skill")
        if not options.list and not any((options.none, options.systems, options.groups, options.names, options.import_skill, options.register_skill)):
            raise ValueError("Choose --systems, --groups, --names, --import-skill, --register-skill or --none")
        vault = Path(options.vault or sk.find_vault()).resolve()
        preflight_tree(vault / sk.SKILLS_REL)
        preflight_tree(vault / sk.CATALOG_REL)
        state_path = vault / "00 ASTORIA" / INSTALL_STATE
        pending = pending_identity = None
        if os.path.lexists(state_path):
            if not options.apply or options.list:
                return stop_install("An interrupted install is recorded; the remaining shelf cannot supply a fresh preview")
            pending, pending_identity = state_record(state_path)
            saved = pending.get("request") if isinstance(pending, dict) else None
            saved_options = saved.get("options") if isinstance(saved, dict) else None
            if (not isinstance(pending, dict) or pending.get("version") != 2 or not isinstance(saved, dict)
                    or set(saved) != {"options", "import"} or saved_options != request_options
                    or any(type(saved_options[key]) is not type(value) for key, value in request_options.items())):
                raise ValueError("Retry requires the exact originally approved selection and options")
            if options.import_skill and options.import_skill.startswith("https://"):
                validate_github_pin(options.import_skill, saved["import"])
        vocabulary = sk.load_vocab(str(vault))
        active = sk.load_skills(str(vault))
        catalog = sk.load_skills(str(vault), sk.CATALOG_REL)
        if set(active) & set(catalog):
            raise ValueError("A skill is present in both active and optional folders")
        observed = dict(catalog, **active)
        previous = sk.read_selection(vault)
        available = sk.release_selection_skills(observed, vocabulary, previous["installed_skills"] if previous else [])
        if previous:
            available.update({name: active[name] for name in previous["imports"] if name in active})
        if options.list:
            for identifier, system in (vocabulary.get("starter", {}).get("optional_systems") or sk.OPTIONAL_SYSTEMS).items():
                print("system %s (%d): %s" % (identifier, sum(skill.system == system for skill in available.values()), system))
            for group, members in catalog_groups(available, vocabulary).items():
                print("research group %s (%d): %s" % (group, len(members), ", ".join(members)))
            return 0
        with tempfile.TemporaryDirectory(prefix="astoria_skill_import_") as temporary:
            import_folder, imported, candidate, writing_group = None, None, None, None
            registering = bool(options.register_skill)
            if options.import_skill:
                if options.import_skill.startswith("https://"):
                    import_folder = Path(temporary) / "skill"
                    pin = pending["request"]["import"] if pending is not None else None
                    imported = github_folder(options.import_skill, import_folder, pin=pin)
                else:
                    import_folder = Path(options.import_skill).expanduser().absolute()
                    imported = {"owner": "user", "source_kind": options.source_kind or "local",
                                "source": options.source or str(import_folder), "revision": options.revision or "",
                                "source_path": options.source_path or import_folder.name}
                candidate = candidate_skill(import_folder, vocabulary, observed)
                if not options.import_skill.startswith("https://") and candidate.name != import_folder.name:
                    raise ValueError("Imported folder name must equal its skill name")
            elif registering:
                import_folder = vault / sk.SKILLS_REL / options.register_skill
                if options.source_kind != "workflow" or not options.source:
                    raise ValueError("Workflow registration needs --source-kind workflow --source pasted (or its supplied source label)")
                if previous and options.register_skill in previous["installed_skills"]:
                    raise ValueError("A release-owned skill cannot be registered as a user import")
                imported = {"owner": "user", "source_kind": "workflow", "source": options.source,
                            "revision": options.revision or "", "source_path": options.source_path or options.register_skill}
                candidate = candidate_skill(import_folder, vocabulary, observed, registering=True)
                if candidate.name != options.register_skill:
                    raise ValueError("Registered folder name must equal its skill name")
            if candidate is not None:
                imported["files"] = import_files(import_folder)
                check_import_references(import_folder, candidate, available)
                vocabulary, writing_group = imported_writing_group(vocabulary, candidate, options.writing_group)
                available[candidate.name] = candidate
            elif options.writing_group:
                raise ValueError("--writing-group needs an imported or registered Writing skill")
            imports = dict(previous["imports"]) if previous else {}
            if candidate is not None:
                imports[candidate.name] = imported
            removed = set(previous["removed_skills"]) if previous else set()
            if previous:
                removed.update(name for name in set(previous["installed_skills"]) | set(previous["imports"]) if name not in active)
            explicit_names = [name.strip() for name in (options.names or "").split(",") if name.strip()]
            removed.difference_update(explicit_names)
            choices = previous["choices"] if previous else {"systems": [], "research_groups": [], "skills": []}
            systems = sorted(set(choices["systems"]) | {value.strip() for value in (options.systems or "").split(",") if value.strip()})
            groups = sorted(set(choices["research_groups"]) | {value.strip() for value in (options.groups or "").split(",") if value.strip()})
            names = sorted(set(choices["skills"]) | set(explicit_names))
            if candidate is not None:
                removed.discard(candidate.name)
            imported_names = set(imports) - removed
            selected = sk.selection_plan(available, vocabulary, systems, groups, sorted((set(names) | imported_names) - removed),
                                         choices.get("include_multimodal", DEFAULT_INCLUDE_MULTIMODAL) and not options.no_multimodal,
                                         removed_skills=removed)
            installed = set(selected["installed_skills"]) - removed
            for name in installed:
                missing = set(available[name].dependencies) - installed
                if missing:
                    raise ValueError(name + " needs removed dependency " + ", ".join(sorted(missing)) + "; explicitly reselect it with --names")
            selected["choices"]["skills"] = sorted(set(names) - set(imports))
            state = {"schema_version": 1, "choices": selected["choices"],
                     "installed_skills": sorted(installed - set(imports)),
                     "required_helpers": {name: reasons for name, reasons in selected["required_helpers"].items()
                                          if name in installed and name not in imports},
                     "removed_skills": sorted(removed), "imports": imports}
            sk._validate_selection_state(state)
            request = {"options": request_options, "import": imported}
            if pending is not None:
                moved_before = verify_state(pending, request, vault / sk.CATALOG_REL, vault / sk.SKILLS_REL, vault)
                if state_record(state_path) != (pending, pending_identity):
                    return stop_install("The install-state record changed during recovery verification")
                # A verified interrupted move can return to its original location,
                # then the same approved command calculates its complete plan again.
                for name in sorted(moved_before):
                    (vault / sk.SKILLS_REL / name).rename(vault / sk.CATALOG_REL / name)
                state_path.unlink()
                catalog = sk.load_skills(str(vault), sk.CATALOG_REL)
                active = sk.load_skills(str(vault))
            install = sorted(installed & set(catalog))
            print("Basics and chosen options: %d release skills, %d user imports" % (len(state["installed_skills"]), len(imported_names)))
            for name in install:
                print("  + %s: %s" % (name, "; ".join(selected["reasons"][name])))
            if candidate is not None:
                print("  %s %s: %d complete supporting files; source %s; revision %s" %
                      ("register" if registering else "import", candidate.name, len(imported["files"]), imported["source"], imported["revision"] or "local snapshot"))
                if writing_group:
                    print("  Writing group: " + writing_group)
            if removed:
                print("Deliberate removals preserved: " + ", ".join(sorted(removed)))
            if options.none and previous:
                print("Basics requested; existing recorded choices and custom folders are preserved.")
            print("Unselected catalog remains available and inactive (%d folders)." % (len(set(catalog) - set(install))))
            if options.remove_catalog:
                print("Legacy --remove-catalog accepted; the available shelf is retained.")
            if not options.apply:
                print("Dry run; add --apply to install this plan.")
                return 0

            # Step 2. Snapshot only installation surfaces for ordinary failure rollback.
            tracked = documents(vault) + [sk.SELECTION_REL]
            originals = {relative: ((vault / relative).read_bytes(), stat.S_IMODE((vault / relative).stat().st_mode))
                         for relative in tracked if (vault / relative).is_file()}
            moved, created = [], None
            journal = journal_identity = None
            try:
                if install:
                    journal, journal_identity = start_state(state_path, request, vault / sk.CATALOG_REL,
                                                            vault / sk.SKILLS_REL, vault, install, [])
                # Step 3. Install exact folders; imported scripts remain unexecuted.
                for name in install:
                    source, target = vault / sk.CATALOG_REL / name, vault / sk.SKILLS_REL / name
                    if source.is_symlink() or os.path.lexists(target):
                        raise ValueError("Unsafe or colliding installation path: " + name)
                    import_files(source)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    source.rename(target)
                    moved.append((source, target))
                if journal is not None:
                    if verify_state(journal, request, vault / sk.CATALOG_REL, vault / sk.SKILLS_REL, vault) != set(install):
                        raise ValueError("The selected folders did not all reach the active directory")
                    if state_record(state_path) != (journal, journal_identity):
                        raise ValueError("The install-state record changed before document writes")
                if candidate is not None and not registering:
                    target = vault / sk.SKILLS_REL / candidate.name
                    target.mkdir(exist_ok=False)
                    created = target
                    shutil.copytree(import_folder, created, dirs_exist_ok=True,
                                    ignore=shutil.ignore_patterns(*SKIP_IMPORT))
                    if import_files(created) != imported["files"]:
                        raise ValueError("Imported source changed after its verified preview snapshot")
                configured = sk.selection_vocabulary(vocabulary, set(active) | installed)
                save_vocabulary(vault, configured)
                relocations = {source.relative_to(vault).as_posix(): target.relative_to(vault).as_posix() for source, target in moved}
                if sk.portable_links_enabled(configured):
                    changed, problems = sk.portable_vault_links(vault, relocations, documents=documents(vault))
                    if problems:
                        raise ValueError("Portable link repair failed:\n" + "\n".join(problems))
                if journal is not None and state_record(state_path) != (journal, journal_identity):
                    raise ValueError("The install-state record changed before selection/view writes")
                # Generated views consume choices as well as installed frontmatter.
                # Publish this transaction's choices before generating those views;
                # the ordinary failure path restores the prior record and documents.
                sk.write_selection(vault, state)
                here = Path(__file__).parent
                for script in ("build_views.py", "lint.py"):
                    command = [sys.executable, "-B", str(here / script), "--vault", str(vault)]
                    if script == "lint.py" and options.assume_notes:
                        command += ["--assume-notes", options.assume_notes]
                    result = subprocess.run(command, capture_output=True, text=True)
                    if result.returncode:
                        raise ValueError(script + " failed:\n" + result.stdout + result.stderr)
                if candidate is not None:
                    state["imports"][candidate.name]["files"] = import_files(vault / sk.SKILLS_REL / candidate.name)
                problems = sk.validate_selection(vault, state)
                if problems:
                    raise ValueError("Installation is incomplete:\n" + "\n".join(problems))
                # Step 4. Save only the recipient-owned choices, after verification.
                if journal is not None and state_record(state_path) != (journal, journal_identity):
                    raise ValueError("The install-state record changed during installation")
                sk.write_selection(vault, state)
                consistency = subprocess.run([sys.executable, "-B", str(here / "build_views.py"), "--vault", str(vault), "--check"],
                                             capture_output=True, text=True)
                if consistency.returncode:
                    raise ValueError("Generated views do not match the completed selection:\n" + consistency.stdout + consistency.stderr)
                if journal is not None:
                    state_path.unlink()
            except BaseException:
                if journal is not None and state_record(state_path) != (journal, journal_identity):
                    raise ValueError("The install-state record changed; files and pending state were preserved for review")
                for source, target in reversed(moved):
                    if target.exists() and not source.exists():
                        shutil.move(target, source)
                if created is not None and created.exists():
                    shutil.rmtree(created)
                for relative, (content, mode) in originals.items():
                    path = vault / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(content)
                    path.chmod(mode)
                if sk.SELECTION_REL not in originals:
                    (vault / sk.SELECTION_REL).unlink(missing_ok=True)
                if journal is not None:
                    state_path.unlink()
                raise
            print("Installed choices verified; selection.json saved. No native mounts were changed.")
            return 0
    except SystemExit as error:
        return error.code
    except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile) as error:
        print(str(error))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
