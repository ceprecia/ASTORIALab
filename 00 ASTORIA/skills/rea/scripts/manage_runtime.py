#!/usr/bin/env python3
"""Install and run the filtered, local REA runtime.

Requirements: Python 3.9+, Node.js, npm for builds, and macOS sandbox-exec.
Date: 2026-10-14.

The skill carries the pinned source specification and build recipe. This script
keeps acquisition, dependencies, and builds outside the vault, verifies a fresh
candidate, and only then replaces the current runtime. Analysis creates no usage
history. Examples:

    python3 manage_runtime.py install
    python3 manage_runtime.py verify --runtime-root /external/path/rea-local
    python3 manage_runtime.py run -- analyze-javascript-application /path/app --json
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.parse
import urllib.request
import zipfile


# Installation identity and limits are deliberately separate from analysis data.
ROOT_MARKER = ".rea_local_root.json"
RUNTIME_METADATA = ".rea_runtime.json"
POLICY_VERSION = 1
MAX_ARCHIVE_BYTES = 256 * 1024 * 1024
MAX_EXTRACTED_BYTES = 1024 * 1024 * 1024
MAX_ARCHIVE_MEMBERS = 100_000
SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = SKILL_ROOT / "assets" / "runtime_spec.json"
DEFAULT_RUNTIME_ROOT = Path.home() / ".local" / "share" / "rea-local"

OFFLINE_PROBE = '''import errno
import json
from pathlib import Path
import socket
import subprocess
import sys

probe_root = Path(sys.argv[-1])
denied_errors = {errno.EPERM, errno.EACCES}

def expect_denied(label, family, operation):
    connection = None
    try:
        connection = socket.socket(family, socket.SOCK_STREAM)
        connection.settimeout(1)
        operation(connection)
    except OSError as error:
        if error.errno not in denied_errors:
            raise RuntimeError(label + " did not receive a permission denial: " + str(error))
        return
    finally:
        if connection is not None:
            connection.close()
    # A successful bind is closed before listen can create a listener.
    raise RuntimeError(label + " unexpectedly succeeded")

unix_path = probe_root / ("child.sock" if "--child" in sys.argv else "parent.sock")
try:
    expect_denied("TCP listener bind", socket.AF_INET, lambda connection: connection.bind(("127.0.0.1", 0)))
    expect_denied("Unix listener bind", socket.AF_UNIX, lambda connection: connection.bind(str(unix_path)))
    expect_denied("outbound localhost connection", socket.AF_INET, lambda connection: connection.connect(("127.0.0.1", 9)))
    if "--child" not in sys.argv:
        child = subprocess.run([sys.executable, "-I", __file__, "--child", str(probe_root)],
                               capture_output=True, text=True, timeout=10)
        if child.returncode:
            raise RuntimeError("Child isolation probe failed: " + child.stderr.strip())
        if json.loads(child.stdout).get("denied_operations") != 3:
            raise RuntimeError("Child did not verify all socket operations")
        print(json.dumps({"denied_operations": 6, "processes": 2}))
    else:
        print(json.dumps({"denied_operations": 3, "processes": 1}))
finally:
    if unix_path.exists():
        unix_path.unlink()
'''


class RuntimeProblem(Exception):
    """An actionable installation or runtime failure."""


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source_file:
        for block in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    content = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(content).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise RuntimeProblem(f"Cannot read {path}: {error}") from error
    if not isinstance(value, dict):
        raise RuntimeProblem(f"Expected a JSON object in {path}")
    return value


def reject_symlink_components(path: Path) -> None:
    """Refuse a linked runtime path rather than following it during replacement."""
    absolute_path = Path(os.path.abspath(path.expanduser()))
    for component in (absolute_path, *absolute_path.parents):
        if component.is_symlink():
            raise RuntimeProblem(f"Symbolic links are not allowed in this managed path: {component}")


def inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def same_existing_location(first: Path, second: Path) -> bool:
    try:
        return first.samefile(second)
    except (FileNotFoundError, OSError):
        return False


def inside_filesystem(path: Path, parent: Path) -> bool:
    """Respect case/Unicode aliases even when the final directory is new."""
    if inside(path, parent):
        return True
    # Existing ancestors reveal the actual filesystem identity. String-based
    # comparisons alone miss case and Unicode aliases on common macOS volumes.
    for ancestor in (path, *path.parents):
        if same_existing_location(ancestor, parent):
            return True
    return False


def vault_root_for_skill() -> Path | None:
    for directory in SKILL_ROOT.parents:
        if directory.name == "00 ASTORIA":
            return directory.parent
        if (directory / "me.md").is_file() and (directory / "AGENTS.md").is_file():
            return directory
    return None


def runtime_root_path(raw_path: str | None, explicit_vault: str | None = None) -> Path:
    runtime_root = Path(raw_path).expanduser() if raw_path else DEFAULT_RUNTIME_ROOT
    runtime_root = Path(os.path.abspath(runtime_root))
    reject_symlink_components(runtime_root)
    if (runtime_root in (Path(runtime_root.anchor), Path.home().resolve())
            or same_existing_location(runtime_root, Path.home()) or len(runtime_root.parts) < 3):
        raise RuntimeProblem("Choose a dedicated runtime directory, not a root or home directory.")
    if inside_filesystem(runtime_root, SKILL_ROOT) or inside_filesystem(SKILL_ROOT, runtime_root):
        raise RuntimeProblem("The runtime must be outside the skill and its parent directories.")
    vault_root = Path(explicit_vault).expanduser().resolve() if explicit_vault else vault_root_for_skill()
    if vault_root and (inside_filesystem(runtime_root, vault_root) or inside_filesystem(vault_root, runtime_root)):
        raise RuntimeProblem("The runtime must be outside the vault. Choose an external runtime directory.")
    if runtime_root.exists() and not runtime_root.is_dir():
        raise RuntimeProblem(f"The runtime destination is not a directory: {runtime_root}")
    return runtime_root


def relative_file(directory: Path, raw_name: str) -> Path:
    archive_name = PurePosixPath(raw_name)
    if not raw_name or "\\" in raw_name or archive_name.is_absolute() or ".." in archive_name.parts:
        raise RuntimeProblem(f"Unsafe relative file name: {raw_name!r}")
    selected_file = directory.joinpath(*archive_name.parts)
    if not inside(selected_file.resolve(), directory.resolve()):
        raise RuntimeProblem(f"File escapes its containing directory: {raw_name!r}")
    reject_symlink_components(selected_file)
    return selected_file


def load_spec(spec_path: Path) -> tuple[dict, Path]:
    spec_path = spec_path.expanduser().resolve()
    specification = read_json(spec_path)
    if specification.get("schema_version") != 1:
        raise RuntimeProblem("Unsupported runtime specification. Expected schema_version 1.")
    for field in ("version", "source", "recipe", "entrypoint"):
        if not specification.get(field):
            raise RuntimeProblem(f"Runtime specification is missing {field}.")
    source = specification["source"]
    if not isinstance(source, dict) or not source.get("url") or not source.get("sha256"):
        raise RuntimeProblem("The source archive needs its exact URL and SHA-256 digest.")
    if urllib.parse.urlparse(source["url"]).scheme != "https":
        raise RuntimeProblem("The source archive URL must use HTTPS.")
    for digest in (source["sha256"], specification["recipe"].get("sha256", "")):
        if not isinstance(digest, str) or len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest):
            raise RuntimeProblem("Source and recipe digests must be lowercase SHA-256 values.")
    recipe = relative_file(spec_path.parent, specification["recipe"].get("path", ""))
    if not recipe.is_file() or file_sha256(recipe) != specification["recipe"]["sha256"]:
        raise RuntimeProblem("The filtered build recipe is missing or does not match its pinned digest.")
    for recipe_input in specification["recipe"].get("inputs", []):
        input_path = relative_file(spec_path.parent, recipe_input["path"])
        if not input_path.is_file() or file_sha256(input_path) != recipe_input["sha256"]:
            raise RuntimeProblem(f"A pinned recipe input is missing or changed: {recipe_input['path']}")
    commands = specification.get("commands", specification.get("required_commands", []))
    if not isinstance(commands, list) or not commands or not all(isinstance(command, str) for command in commands):
        raise RuntimeProblem("The specification must list the supported local commands.")
    relative_file(Path(tempfile.gettempdir()).resolve(), specification["entrypoint"])
    return specification, recipe


def tool_path(name: str) -> str:
    executable = shutil.which(name)
    if not executable:
        raise RuntimeProblem(f"Required local program is unavailable: {name}")
    return executable


def require_node(specification: dict) -> str:
    node_path = tool_path("node")
    result = subprocess.run([node_path, "--version"], capture_output=True, text=True)
    version_match = re.fullmatch(r"v?(\d+)\.(\d+)\.(\d+)", result.stdout.strip())
    if result.returncode or not version_match:
        raise RuntimeProblem("Cannot determine the installed Node.js version.")
    node_version = tuple(int(value) for value in version_match.groups())
    supported_ranges = specification.get("node_version_ranges", [
        {"minimum": "22.19.0", "maximum_exclusive": "23.0.0"},
        {"minimum": "24.11.0", "maximum_exclusive": "25.0.0"},
        {"minimum": "26.0.0"},
    ])
    for supported_range in supported_ranges:
        minimum = tuple(int(value) for value in supported_range["minimum"].split("."))
        maximum_text = supported_range.get("maximum_exclusive")
        maximum = tuple(int(value) for value in maximum_text.split(".")) if maximum_text else None
        if node_version >= minimum and (maximum is None or node_version < maximum):
            return node_path
    raise RuntimeProblem(
        "The installed Node.js version is outside the pinned supported ranges: "
        + json.dumps(supported_ranges, sort_keys=True)
    )


def offline_command(command: list[str]) -> list[str]:
    """Deny network access for the entire analysis/verification process tree."""
    if platform.system() == "Darwin":
        sandbox_path = shutil.which("sandbox-exec")
        if sandbox_path:
            return [sandbox_path, "-p", "(version 1)(allow default)(deny network*)", *command]
    raise RuntimeProblem(
        "This local adaptation currently requires macOS sandbox-exec to deny "
        "network access and listeners for the full process tree. This environment "
        "needs a platform adapter with the same verified behavior."
    )


def verify_offline_isolation() -> dict:
    """Check OS denial in the launched process and its independently spawned child."""
    with tempfile.TemporaryDirectory(prefix="rea_offline_probe_") as directory:
        probe_root = Path(directory).resolve()
        probe_file = probe_root / "offline_probe.py"
        probe_file.write_text(OFFLINE_PROBE, encoding="utf-8")
        command = offline_command([sys.executable, "-I", str(probe_file), str(probe_root)])
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        except subprocess.TimeoutExpired as error:
            raise RuntimeProblem("Offline process isolation self-test timed out.") from error
        if result.returncode:
            detail = (result.stderr or result.stdout).strip()
            raise RuntimeProblem(f"Offline process isolation self-test failed: {detail}")
        try:
            checks = json.loads(result.stdout)
        except ValueError as error:
            raise RuntimeProblem("Offline process isolation self-test returned an invalid result.") from error
        if checks != {"denied_operations": 6, "processes": 2}:
            raise RuntimeProblem("Offline process isolation did not verify every parent and child operation.")
        return checks


def ensure_managed_root(runtime_root: Path, create: bool) -> None:
    marker_path = runtime_root / ROOT_MARKER
    if not runtime_root.exists():
        if not create:
            raise RuntimeProblem(f"REA is not installed at {runtime_root}. Run install first.")
        runtime_root.mkdir(parents=True)
    reject_symlink_components(runtime_root)
    if marker_path.is_symlink():
        raise RuntimeProblem("The installation marker cannot be a symbolic link.")
    if not marker_path.exists():
        if not create or any(runtime_root.iterdir()):
            raise RuntimeProblem("The destination contains unmanaged files. Choose a fresh runtime directory.")
        write_json(marker_path, {"kind": "rea-local-runtime", "schema_version": 1})
    if read_json(marker_path) != {"kind": "rea-local-runtime", "schema_version": 1}:
        raise RuntimeProblem("The destination does not have the expected managed-runtime marker.")
    for directory_name in ("current", "previous"):
        directory = runtime_root / directory_name
        if directory.is_symlink() or (directory.exists() and not directory.is_dir()):
            raise RuntimeProblem(f"Unsafe installed-runtime directory: {directory}")


@contextlib.contextmanager
def installation_lock(runtime_root: Path, exclusive: bool):
    """An empty OS lock file prevents simultaneous replacement and execution."""
    try:
        import fcntl
    except ImportError as error:
        raise RuntimeProblem("This manager currently requires a macOS filesystem lock.") from error
    lock_path = runtime_root / ".install_lock"
    if lock_path.is_symlink():
        raise RuntimeProblem("The installation lock cannot be a symbolic link.")
    descriptor = os.open(lock_path, os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
        try:
            fcntl.flock(descriptor, operation | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeProblem("Another REA analysis or installation is using this runtime. Retry after it exits.") from error
        yield
    finally:
        os.close(descriptor)


def download_archive(specification: dict, archive_path: Path) -> None:
    request = urllib.request.Request(specification["source"]["url"], headers={"User-Agent": "rea-local-installer"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, archive_path.open("wb") as archive_file:
            if urllib.parse.urlparse(response.geturl()).scheme != "https":
                raise RuntimeProblem("The archive download redirected to an insecure URL.")
            total_bytes = 0
            while True:
                block = response.read(1024 * 1024)
                if not block:
                    break
                total_bytes += len(block)
                if total_bytes > MAX_ARCHIVE_BYTES:
                    raise RuntimeProblem("The source archive exceeds the installer size limit.")
                archive_file.write(block)
    except OSError as error:
        raise RuntimeProblem(f"Source download failed: {error}") from error
    if file_sha256(archive_path) != specification["source"]["sha256"]:
        raise RuntimeProblem("The downloaded source archive does not match the pinned SHA-256 digest.")


def excluded_source_entry(name: str) -> bool:
    """Do not materialize upstream assistant configuration during acquisition."""
    parts = [part.casefold() for part in PurePosixPath(name).parts]
    if any(part in (".claude", ".agents") for part in parts):
        return True
    excluded_names = {
        "agents.md", "agents.override.md", "agents.local.md", "claude.md",
        "claude.local.md", "codex.md", "gemini.md",
    }
    return bool(parts and parts[-1] in excluded_names)


def safe_extract_archive(archive_path: Path, destination: Path) -> None:
    """Extract regular files only, refusing traversal, links, devices, and bombs."""
    destination.mkdir()
    extracted_bytes = 0
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as archive:
            members = archive.infolist()
            if len(members) > MAX_ARCHIVE_MEMBERS:
                raise RuntimeProblem("Too many files in the source archive.")
            for member in members:
                target = relative_file(destination, member.filename)
                if excluded_source_entry(member.filename):
                    continue
                unix_mode = member.external_attr >> 16
                file_type = stat.S_IFMT(unix_mode)
                if file_type not in (0, stat.S_IFREG, stat.S_IFDIR):
                    raise RuntimeProblem(f"Archive contains a nonregular file: {member.filename}")
                if member.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                extracted_bytes += member.file_size
                if extracted_bytes > MAX_EXTRACTED_BYTES:
                    raise RuntimeProblem("Extracted source exceeds the installer size limit.")
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source_file, target.open("xb") as target_file:
                    shutil.copyfileobj(source_file, target_file)
                target.chmod(0o755 if unix_mode & 0o111 else 0o644)
        return
    try:
        with tarfile.open(archive_path, mode="r:*") as archive:
            member_count = 0
            for member in archive:
                member_count += 1
                if member_count > MAX_ARCHIVE_MEMBERS:
                    raise RuntimeProblem("Too many files in the source archive.")
                target = relative_file(destination, member.name)
                if excluded_source_entry(member.name):
                    continue
                if member.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                if not member.isfile():
                    raise RuntimeProblem(f"Archive contains a nonregular file: {member.name}")
                extracted_bytes += member.size
                if extracted_bytes > MAX_EXTRACTED_BYTES:
                    raise RuntimeProblem("Extracted source exceeds the installer size limit.")
                target.parent.mkdir(parents=True, exist_ok=True)
                source_file = archive.extractfile(member)
                if source_file is None:
                    raise RuntimeProblem(f"Cannot read archive member: {member.name}")
                with source_file, target.open("xb") as target_file:
                    shutil.copyfileobj(source_file, target_file)
                target.chmod(0o755 if member.mode & 0o111 else 0o644)
    except tarfile.TarError as error:
        raise RuntimeProblem(f"The source archive is not a supported ZIP or tar archive: {error}") from error


def source_root_for_archive(extracted_path: Path, specification: dict) -> Path:
    archive_root = specification["source"].get("archive_root")
    if archive_root:
        source_root = relative_file(extracted_path, archive_root)
    else:
        children = list(extracted_path.iterdir())
        source_root = children[0] if len(children) == 1 and children[0].is_dir() else extracted_path
    if not source_root.is_dir():
        raise RuntimeProblem("The source archive does not contain its specified root directory.")
    return source_root


def runtime_manifest(runtime_directory: Path) -> dict[str, str]:
    manifest = {}
    for path in sorted(runtime_directory.rglob("*")):
        if path.is_symlink():
            raise RuntimeProblem(f"Runtime contains a symbolic link: {path}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise RuntimeProblem(f"Runtime contains a nonregular file: {path}")
        relative_name = path.relative_to(runtime_directory).as_posix()
        if relative_name != RUNTIME_METADATA:
            manifest[relative_name] = file_sha256(path)
    if not manifest:
        raise RuntimeProblem("The filtered build produced no runtime files.")
    return manifest


def verify_recipe(recipe: Path, runtime_directory: Path) -> None:
    command = [sys.executable, "-B", str(recipe), "verify", "--runtime-root", str(runtime_directory)]
    result = subprocess.run(offline_command(command), capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeProblem(f"Filtered-runtime verification failed: {detail}")


def installed_runtime(runtime_root: Path, specification: dict) -> Path:
    current = runtime_root / "current"
    if not current.is_dir():
        raise RuntimeProblem(f"REA has no active installation at {runtime_root}. Run install first.")
    metadata_path = current / RUNTIME_METADATA
    if metadata_path.is_symlink():
        raise RuntimeProblem("Runtime metadata cannot be a symbolic link.")
    metadata = read_json(metadata_path)
    if metadata.get("policy_version") != POLICY_VERSION or metadata.get("spec_sha256") != canonical_sha256(specification):
        raise RuntimeProblem("The installed runtime does not match this skill's filtered specification. Reinstall or complete the reviewed update.")
    if metadata.get("version") != specification["version"] or metadata.get("entrypoint") != specification["entrypoint"]:
        raise RuntimeProblem("Installed-runtime metadata does not match the specification.")
    if metadata.get("files") != runtime_manifest(current):
        raise RuntimeProblem("Installed runtime files have changed or unexpected files were added. Reinstall the pinned build.")
    entrypoint = relative_file(current, specification["entrypoint"])
    if not entrypoint.is_file():
        raise RuntimeProblem("The verified local entrypoint is missing.")
    return entrypoint


def promote_candidate(runtime_root: Path, candidate: Path) -> None:
    current = runtime_root / "current"
    previous = runtime_root / "previous"
    if previous.exists():
        shutil.rmtree(previous)
    had_current = current.exists()
    if had_current:
        os.replace(current, previous)
    try:
        os.replace(candidate, current)
    except BaseException:
        if had_current and previous.exists():
            os.replace(previous, current)
        raise


def install_runtime(action: str, runtime_root: Path, specification: dict, recipe: Path) -> dict:
    require_node(specification)
    tool_path("npm")
    # Fail before downloading if offline verification cannot be enforced here.
    verify_offline_isolation()
    ensure_managed_root(runtime_root, create=True)
    with installation_lock(runtime_root, exclusive=True):
        if action == "install" and (runtime_root / "current").exists():
            entrypoint = installed_runtime(runtime_root, specification)
            verify_recipe(recipe, entrypoint.parent.parent)
            return {"status": "already_installed", "version": specification["version"], "runtime_root": str(runtime_root)}
        # Staging shares the destination filesystem so final renames stay atomic.
        # Source, package caches, and build dependencies disappear with the stage.
        with tempfile.TemporaryDirectory(prefix=".rea_build_", dir=runtime_root.parent) as temporary_directory:
            stage = Path(temporary_directory)
            archive_path = stage / "source.archive"
            extracted_path = stage / "source"
            candidate = stage / "candidate"
            download_archive(specification, archive_path)
            safe_extract_archive(archive_path, extracted_path)
            source_root = source_root_for_archive(extracted_path, specification)
            candidate.mkdir()
            command = [sys.executable, "-B", str(recipe), "build", "--source-root", str(source_root), "--runtime-root", str(candidate)]
            result = subprocess.run(command)
            if result.returncode:
                raise RuntimeProblem(f"The filtered build failed with exit code {result.returncode}. The current runtime was retained.")
            entrypoint = relative_file(candidate, specification["entrypoint"])
            if not entrypoint.is_file():
                raise RuntimeProblem("The filtered build did not produce its expected local entrypoint.")
            verify_recipe(recipe, candidate)
            metadata = {
                "schema_version": 1,
                "policy_version": POLICY_VERSION,
                "version": specification["version"],
                "spec_sha256": canonical_sha256(specification),
                "entrypoint": specification["entrypoint"],
                "files": runtime_manifest(candidate),
            }
            write_json(candidate / RUNTIME_METADATA, metadata)
            promote_candidate(runtime_root, candidate)
        installed_runtime(runtime_root, specification)
    return {"status": "installed", "version": specification["version"], "runtime_root": str(runtime_root), "entrypoint": str(runtime_root / "current" / specification["entrypoint"])}


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="action", required=True)
    for action in ("install", "reinstall", "update", "verify", "run"):
        subparser = subparsers.add_parser(action)
        subparser.add_argument("--runtime-root", help="Dedicated directory outside the vault; default: ~/.local/share/rea-local")
        subparser.add_argument("--vault-root", help="Vault root to keep runtime/builds outside when automatic discovery is unavailable")
        subparser.add_argument("--spec", type=Path, default=DEFAULT_SPEC, help="Reviewed, pinned runtime specification; default: skill assets/runtime_spec.json")
        if action == "run":
            subparser.add_argument("arguments", nargs=argparse.REMAINDER, help="Use -- followed by a supported REA command and arguments")
    return parser


def main() -> int:
    arguments = make_parser().parse_args()
    try:
        runtime_root = runtime_root_path(arguments.runtime_root, arguments.vault_root)
        specification, recipe = load_spec(arguments.spec)
        if arguments.action in ("install", "reinstall", "update"):
            result = install_runtime(arguments.action, runtime_root, specification, recipe)
            print(json.dumps(result, sort_keys=True))
            return 0
        ensure_managed_root(runtime_root, create=False)
        with installation_lock(runtime_root, exclusive=False):
            entrypoint = installed_runtime(runtime_root, specification)
            node_path = require_node(specification)
            if arguments.action == "verify":
                verify_offline_isolation()
                verify_recipe(recipe, runtime_root / "current")
                print(json.dumps({"status": "verified", "version": specification["version"], "runtime_root": str(runtime_root)}, sort_keys=True))
                return 0
            command_arguments = arguments.arguments
            if command_arguments and command_arguments[0] == "--":
                command_arguments = command_arguments[1:]
            if not command_arguments:
                raise RuntimeProblem("Supply a supported REA command after --. Use run -- --help to list commands.")
            commands = specification.get("commands", specification.get("required_commands", []))
            if command_arguments[0] not in [*commands, "--help", "--version"]:
                raise RuntimeProblem(f"This filtered runtime does not support {command_arguments[0]!r}. Use run -- --help.")
            return subprocess.run(offline_command([node_path, str(entrypoint), *command_arguments])).returncode
    except (RuntimeProblem, OSError, ValueError, KeyError) as error:
        print(f"REA local: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("REA local: interrupted; an unfinished candidate was not activated.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
