#!/usr/bin/env python3
"""move_files.py | Move caller-selected files and repair supported local references.

Python standard library; dry-run by default. Supply --vault and a JSON --plan
of {source, destination} paths relative to the vault. Optional --path-edits selects
reviewed literal path spans. --apply keeps recoverable originals outside the vault.
This utility does not classify files or tidy a tree.
"""
import argparse
import errno
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import stat
import tempfile
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urlsplit


# 1. Supported reference surfaces; unrelated bytes are never reformatted.
REFERENCE_EXTENSIONS = {".md", ".markdown", ".html", ".htm", ".svg", ".canvas"}
OTHER_TEXT_EXTENSIONS = {".txt", ".py", ".r", ".sh", ".json", ".yaml", ".yml",
                         ".js", ".mjs", ".cjs", ".css", ".tex", ".bib", ".ino",
                         ".cpp", ".h", ".scad", ".m", ".ipynb", ".base"}
SKIP_DIRECTORIES = {".git", "node_modules", "__pycache__", ".venv", "venv"}
MAX_TEXT_BYTES = 16_000_000
WIKI = re.compile(r"(?<!\\)\[\[([^\]\n]+)\]\]")
INLINE_START = re.compile(r"!?\[[^\]\n]*\]\(")
REFERENCE_START = re.compile(r"(?m)^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*")
TAG = re.compile(r"<[^<>]+>")
ATTRIBUTE = re.compile(r"\b(?:href|src|xlink:href)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))", re.I)
QUOTED_PATH = re.compile(r"([\"'])([^\"'\n]+)\1")
CSS_URL = re.compile(r"url\(\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s)]+))\s*\)", re.I)
CANVAS_FILE = re.compile(r'"file"\s*:\s*("(?:\\.|[^"\\])*")')
INLINE_CODE = re.compile(r"(?<!`)(`+)(.+?)\1(?!`)", re.S)
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


class MoveError(Exception):
    """An operation cannot be completed safely within this utility's contract."""


@dataclass
class Token:
    start: int
    end: int
    kind: str
    raw: str


def key(path):
    return unicodedata.normalize("NFC", str(path)).casefold().rstrip("/")


def under(path, parent):
    return key(path) == key(parent) or key(path).startswith(key(parent) + "/")


def overlaps(first, second):
    return under(first, second) or under(second, first)


def relative_path(value):
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise MoveError("Paths must be nonempty POSIX paths relative to the vault.")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or str(path) == "." or SCHEME.match(value):
        raise MoveError("The vault root, absolute paths, and path escapes are not move entries: " + value)
    return str(path)


def checked_path(vault, relative):
    """Reject symlinks at every existing component below the chosen vault."""
    current = vault
    for component in PurePosixPath(relative).parts:
        current = current / component
        if current.is_symlink():
            raise MoveError("Symlink traversal is excluded: " + str(current.relative_to(vault)))
    return current


def digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def inventory(vault):
    paths, directories, skipped = [], [], []
    for root, names, files in os.walk(vault, followlinks=False):
        for name in list(names):
            path = Path(root) / name
            rel = path.relative_to(vault).as_posix()
            if path.is_symlink() or name in SKIP_DIRECTORIES or name.startswith("."):
                skipped.append(rel)
                names.remove(name)
        relative_root = Path(root).relative_to(vault).as_posix()
        if relative_root != ".":
            directories.append(relative_root)
        for name in files:
            path = Path(root) / name
            rel = path.relative_to(vault).as_posix()
            if path.is_symlink() or name.startswith("."):
                skipped.append(rel)
            elif path.is_file():
                paths.append(rel)
    return sorted(paths), sorted(directories), sorted(skipped)


def path_index(files, directories):
    exact = {}
    names = defaultdict(list)
    for path in files + directories:
        normal = key(path)
        if normal in exact and exact[normal] != path:
            raise MoveError("Case or Unicode path collision: " + path)
        exact[normal] = path
    for path in files:
        names[key(Path(path).name)].append(path)
        if path.lower().endswith(".md"):
            names[key(Path(path).stem)].append(path)
    return exact, names


def token_uri(token):
    if token.kind == "wiki":
        return token.raw.partition("|")[0]
    if token.kind == "html":
        return html.unescape(token.raw)
    if token.kind == "canvas":
        return json.loads(token.raw)
    return token.raw


def split_uri(uri):
    # Parse separators before URL decoding: an encoded '#' belongs to a filename.
    uri = re.sub(r"\\([ ()\[\]])", r"\1", uri)
    parts = urlsplit(uri)
    suffix = ("?" + parts.query if "?" in uri.split("#", 1)[0] else "")
    if "#" in uri:
        suffix += "#" + parts.fragment
    return parts, unquote(parts.path), suffix


def resolve(token, source, index, vault):
    uri = token_uri(token)
    if not uri or uri.startswith(("#", "^")):
        return None, []
    parts, path, unused_suffix = split_uri(uri)
    if parts.scheme and parts.scheme.lower() != "file":
        return None, []
    if parts.scheme == "file" and parts.netloc not in ("", "localhost"):
        return None, []
    absolute = False
    root_prefix = next((prefix for prefix in (str(vault), str(vault.resolve()))
                        if path.startswith(prefix + "/")), None)
    if root_prefix:
        path = path[len(root_prefix) + 1:]
        absolute = True
    elif path.startswith("/"):
        # A known vault-root path is supported; other absolute paths stay external.
        if key(path[1:]) in index[0]:
            path = path[1:]
            absolute = True
        else:
            return None, []
    if not path:
        return None, []
    relative = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
    choices = [path, relative] if token.kind in {"wiki", "canvas"} else ([path] if absolute else [relative])
    for candidate in choices:
        variations = [candidate, candidate + ".md"] if token.kind == "wiki" else [candidate]
        for variation in variations:
            if key(variation) in index[0]:
                return index[0][key(variation)], []
    if token.kind == "wiki":
        endings = ("/" + key(path), "/" + key(path) + ".md")
        candidates = list(dict.fromkeys(
            found for found in index[1].get(key(Path(path).name), [])
            if "/" not in path or key(found).endswith(endings)))
        if len(candidates) == 1:
            return candidates[0], []
        return None, candidates
    return None, []


def destination_span(text, start, end):
    """Locate a Markdown destination without changing wrappers or its title."""
    while start < end and text[start].isspace():
        start += 1
    while end > start and text[end - 1].isspace():
        end -= 1
    if start < end and text[start] == "<":
        close = text.find(">", start + 1, end)
        return (start + 1, close) if close >= 0 else None
    body = text[start:end]
    title = re.search(r"\s+(?:\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*'|\([^()]*\))\s*$", body)
    if title:
        end = start + title.start()
    return (start, end) if end > start else None


def literal_spans(text):
    """Code examples and inline provenance are content, not repairable links."""
    spans, opened, offset = [], None, 0
    for line in text.splitlines(keepends=True):
        fence = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)
            if opened is None:
                opened = (marker[0], len(marker), offset)
            elif marker[0] == opened[0] and len(marker) >= opened[1]:
                spans.append((opened[2], offset + len(line)))
                opened = None
        offset += len(line)
    if opened:
        spans.append((opened[2], len(text)))
    spans.extend((match.start(), match.end()) for match in INLINE_CODE.finditer(text))
    spans.extend((match.start(), match.end()) for match in re.finditer(
        r"<(?:pre|code)\b[^>]*>.*?</(?:pre|code)\s*>", text, re.I | re.S))
    return spans


def reference_tokens(text, extension):
    tokens = []
    if extension in {".md", ".markdown"}:
        for match in WIKI.finditer(text):
            tokens.append(Token(match.start(1), match.end(1), "wiki", match.group(1)))
        for match in INLINE_START.finditer(text):
            start = match.end()
            first_content = start
            while first_content < len(text) and text[first_content] in " \t":
                first_content += 1
            depth, cursor, escaped, angle, quoted = 0, start, False, False, None
            while cursor < len(text) and text[cursor] != "\n":
                char = text[cursor]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif quoted:
                    if char == quoted:
                        quoted = None
                elif char in "\"'" and cursor > first_content and text[cursor - 1].isspace():
                    quoted = char
                elif char == "<" and cursor == first_content:
                    angle = True
                elif char == ">" and angle:
                    angle = False
                elif not angle and char == "(":
                    depth += 1
                elif not angle and char == ")":
                    if depth == 0:
                        span = destination_span(text, start, cursor)
                        if span:
                            tokens.append(Token(*span, "markdown", text[slice(*span)]))
                        break
                    depth -= 1
                cursor += 1
        for match in REFERENCE_START.finditer(text):
            end = text.find("\n", match.end())
            span = destination_span(text, match.end(), len(text) if end < 0 else end)
            if span:
                tokens.append(Token(*span, "reference", text[slice(*span)]))
        for match in re.finditer(r"<(file:[^<>\n]+)>", text):
            tokens.append(Token(match.start(1), match.end(1), "markdown", match.group(1)))
    if extension in {".md", ".markdown", ".html", ".htm", ".svg"}:
        for tag in TAG.finditer(text):
            for match in ATTRIBUTE.finditer(tag.group()):
                group = next(number for number in (1, 2, 3) if match.group(number) is not None)
                start, end = tag.start() + match.start(group), tag.start() + match.end(group)
                tokens.append(Token(start, end, "html", text[start:end]))
    if extension == ".canvas":
        json.loads(text)
        for match in CANVAS_FILE.finditer(text):
            tokens.append(Token(match.start(1), match.end(1), "canvas", match.group(1)))
    # A path inside a link or tag is not also an inline-code token.
    selected = []
    protected = literal_spans(text) if extension != ".canvas" else []
    for token in sorted(tokens, key=lambda item: (item.start, -(item.end - item.start))):
        if any(token.start < end and token.end > start for start, end in protected):
            continue
        if not selected or token.start >= selected[-1].end:
            selected.append(token)
    return selected


def rewrite_token(token, target, source, new_source, new_target, vault):
    uri = token_uri(token)
    parts, original_path, suffix = split_uri(uri)
    if token.kind == "wiki":
        base, separator, alias = token.raw.partition("|")
        bare = "/" not in original_path and not parts.scheme
        same_name = key(Path(target).name) == key(Path(new_target).name)
        if bare and same_name:
            return token.raw
        value = new_target
        if value.lower().endswith(".md") and not original_path.lower().endswith(".md"):
            value = value[:-3]
        if not separator and not same_name:
            old_name = Path(original_path).name
            separator, alias = "|", old_name[:-3] if old_name.lower().endswith(".md") else old_name
        return value + suffix + (separator + alias if separator else "")
    if token.kind == "canvas":
        return json.dumps(new_target + suffix, ensure_ascii=False)
    if parts.scheme == "file":
        value = (vault / new_target).as_uri()
    elif original_path.startswith(str(vault) + "/"):
        value = str(vault / new_target)
    elif original_path.startswith("/"):
        value = "/" + new_target
    else:
        value = posixpath.relpath(new_target, posixpath.dirname(new_source) or ".")
        if original_path.startswith("./") and not value.startswith("."):
            value = "./" + value
    if token.kind != "code" and parts.scheme != "file":
        value = quote(value, safe="/~:@!$&'*,;=+-._")
    value += suffix
    return html.escape(value, quote=True) if token.kind == "html" else value


def replace_tokens(text, replacements):
    for token, value in reversed(replacements):
        text = text[:token.start] + value + text[token.end:]
    return text


def relocate(path, moves):
    for source, destination in moves:
        if under(path, source):
            suffix = "/".join(PurePosixPath(path).parts[len(PurePosixPath(source).parts):])
            return destination if not suffix else destination + "/" + suffix
    return path


def owner_moves(path, moves):
    return [source for source, unused in moves if under(path, source)]


def literal_path_target(value, source, index, vault):
    """Literal filesystem paths do not URL-decode percent signs or '#'."""
    path = value
    prefix = next((item for item in (str(vault), str(vault.resolve()))
                   if path.startswith(item + "/")), None)
    if prefix:
        relative = path[len(prefix) + 1:]
    elif path.startswith("/") or SCHEME.match(path):
        return None
    else:
        relative = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
    return index[0].get(key(relative))


def reviewed_path_tokens(vault, entries, files, old_index, new_index, moves, system_root, holds):
    """Validate exact caller-selected literal paths without guessing their role."""
    if not isinstance(entries, list):
        raise MoveError("Path edits must be a JSON list.")
    selected = defaultdict(list)
    for entry in entries:
        if (not isinstance(entry, dict)
                or not {"file", "start", "old", "new"} <= set(entry)
                or set(entry) - {"file", "start", "old", "new", "base"}):
            raise MoveError("Each path edit needs file, start, old, new and optional base.")
        source = relative_path(entry["file"])
        source = old_index[0].get(key(source), source)
        if source not in files or Path(source).suffix.lower() not in REFERENCE_EXTENSIONS | OTHER_TEXT_EXTENSIONS:
            raise MoveError("Path edit must select a scanned UTF-8 text file: " + source)
        if under(source, system_root) or any(under(source, held) for held in holds):
            raise MoveError("Path edit touches a read-only or held file: " + source)
        start, old, new = entry["start"], entry["old"], entry["new"]
        if (type(start) is not int or start < 0 or not isinstance(old, str)
                or not isinstance(new, str) or not old or not new or old == new
                or any(ord(char) < 32 or char == "\\" for char in old + new)):
            raise MoveError("Path edit needs a character offset and two different POSIX path tokens.")
        path = checked_path(vault, source)
        if path.stat().st_size > MAX_TEXT_BYTES:
            raise MoveError("Path edit exceeds the text-size limit: " + source)
        text = path.read_bytes().decode("utf-8")
        end = start + len(old)
        if text[start:end] != old:
            raise MoveError("Selected path span changed or does not match: " + source)
        before, after = text[start - 1:start] if start else "", text[end:end + 1]
        if ((before and (before.isalnum() or before in "_./~%+-#?"))
                or (after and (after.isalnum() or after in "_/~%+-#?"))
                or (before in {"'", '"', "`"} and after != before)
                or (after == "." and text[end + 1:end + 2].isalnum())):
            raise MoveError("Select the complete path token, not a substring: " + source)
        base = entry.get("base", "document")
        if not isinstance(base, str) or base not in {"vault", "document"}:
            raise MoveError("Path-edit base must be vault or document.")
        if any(char in new for char in "'\"`"):
            raise MoveError("Path edit needs syntax escaping outside literal-path coverage: " + source)
        old_source = source if base == "document" else "_vault_path_base_"
        new_source = relocate(source, moves) if base == "document" else old_source
        old_token = Token(start, end, "code", old)
        target = literal_path_target(old, old_source, old_index, vault)
        new_target = literal_path_target(new, new_source, new_index, vault)
        if (target is None or new_target != relocate(target, moves)
                or (new_target == target and old_source == new_source)):
            raise MoveError("Path edit is not a verified move/rebase of the same local target: " + source)
        if any(start < token.end and end > token.start for token, unused in selected[source]):
            raise MoveError("Selected path edits overlap: " + source)
        selected[source].append((old_token, new))
    return selected


def prepare(vault, rows, system_root="00 ASTORIA", holds=(), path_edits=None):
    """Build a verified in-memory transaction. No backup or vault write occurs."""
    original_vault = Path(vault).absolute()
    if original_vault.is_symlink() or not original_vault.is_dir():
        raise MoveError("The chosen vault must be an existing nonsymlink directory.")
    # Keep the caller's root spelling so file URIs using a normal OS alias such
    # as /var on macOS resolve consistently. Containment checks use resolve().
    vault = original_vault
    system_root = relative_path(system_root)
    holds = [relative_path(path) for path in holds]
    if not isinstance(rows, list) or not rows:
        raise MoveError("The plan must be a nonempty JSON list of move entries.")
    files, directories, skipped = inventory(vault)
    old_index = path_index(files, directories)
    moves = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"source", "destination"}:
            raise MoveError("Each plan entry must contain only source and destination.")
        source, destination = relative_path(row["source"]), relative_path(row["destination"])
        source = old_index[0].get(key(source), source)
        if Path(source).parts[0].startswith(".") or Path(destination).parts[0].startswith("."):
            raise MoveError("App-private or hidden vault roots are outside the reference scan: " + source)
        if overlaps(source, destination):
            raise MoveError("A move may not contain itself: " + source)
        for protected in [system_root] + holds:
            if overlaps(source, protected) or overlaps(destination, protected):
                raise MoveError("Move touches a read-only or held path: " + protected)
        source_path, destination_path = checked_path(vault, source), checked_path(vault, destination)
        if not source_path.exists():
            raise MoveError("Source missing: " + source)
        if os.path.lexists(destination_path) or key(destination) in old_index[0]:
            raise MoveError("Destination already exists: " + destination)
        for previous_source, previous_destination in moves:
            if any(overlaps(first, second) for first in (source, destination)
                   for second in (previous_source, previous_destination)):
                raise MoveError("Overlapping move entries are excluded: " + source)
        moves.append((source, destination))
    moved_files, moved_directories, snapshots = {}, {}, {}
    for source, destination in moves:
        source_path = vault / source
        if source_path.is_dir():
            for root, child_dirs, child_files in os.walk(source_path, followlinks=False):
                for name in child_dirs + child_files:
                    checked_path(vault, (Path(root) / name).relative_to(vault).as_posix())
                rel = Path(root).relative_to(vault).as_posix()
                moved_directories[rel] = relocate(rel, moves)
                for name in child_files:
                    item = (Path(root) / name).relative_to(vault).as_posix()
                    if not stat.S_ISREG((vault / item).stat().st_mode):
                        raise MoveError("A package contains a nonregular file: " + item)
                    moved_files[item] = relocate(item, moves)
        elif source_path.is_file():
            moved_files[source] = destination
        else:
            raise MoveError("Source is not a regular file or directory: " + source)
    destinations = list(moved_files.values()) + list(moved_directories.values())
    if len({key(path) for path in destinations}) != len(destinations):
        raise MoveError("Case or Unicode destination collision.")
    for source in moved_files:
        path = checked_path(vault, source)
        snapshots[source] = (digest(path), path.stat().st_mode)
    old_index = path_index(list(dict.fromkeys(files + list(moved_files))),
                           list(dict.fromkeys(directories + list(moved_directories))))
    new_files = [relocate(path, moves) for path in dict.fromkeys(files + list(moved_files))]
    new_directories = [relocate(path, moves) for path in dict.fromkeys(directories + list(moved_directories))]
    new_directories += list(moved_directories.values())
    new_index = path_index(list(dict.fromkeys(new_files)), list(dict.fromkeys(new_directories)))
    selected_paths = reviewed_path_tokens(vault, [] if path_edits is None else path_edits, files, old_index,
                                         new_index, moves, system_root, holds)
    edits, documents, blocked, unresolved = {}, {}, [], []
    resolved_count = 0
    old_literals = sorted({part for source, unused in moves
                           for part in (source, str(vault / source), quote(source, safe="/"))}, key=len, reverse=True)
    for source in list(dict.fromkeys(files + list(moved_files))):
        path = vault / source
        extension = path.suffix.lower()
        if extension not in REFERENCE_EXTENSIONS | OTHER_TEXT_EXTENSIONS:
            continue
        if path.stat().st_size > MAX_TEXT_BYTES:
            unresolved.append({"code": "text_size_limit", "file": source})
            continue
        original = path.read_bytes()
        try:
            text = original.decode("utf-8")
        except UnicodeDecodeError:
            unresolved.append({"code": "non_utf8_text", "file": source})
            continue
        replacements, edges = [], []
        tokens = reference_tokens(text, extension) if extension in REFERENCE_EXTENSIONS else []
        for selected, value in selected_paths.get(source, []):
            if any(selected.start < token.end and selected.end > token.start for token in tokens):
                raise MoveError("A selected path overlaps an automatically repaired link: " + source)
            replacements.append((selected, value))
        for token in tokens:
            target, ambiguous = resolve(token, source, old_index, vault)
            if not target:
                edges.append((token.kind, None))
                if ambiguous and any(relocate(candidate, moves) != candidate for candidate in ambiguous):
                    blocked.append({"code": "ambiguous_reference", "file": source,
                                    "target": token_uri(token), "candidates": ambiguous})
                continue
            resolved_count += 1
            new_source, new_target = relocate(source, moves), relocate(target, moves)
            value = rewrite_token(token, target, source, new_source, new_target, vault)
            if new_source == source and new_target == target:
                value = token.raw
            edges.append((token.kind, new_target))
            if value != token.raw:
                if under(source, system_root) or any(under(source, held) for held in holds):
                    blocked.append({"code": "system_handoff" if under(source, system_root) else "held_reference",
                                    "file": source, "target": target,
                                    "moves": owner_moves(target, moves) + owner_moves(source, moves)})
                else:
                    replacements.append((token, value))
        # System instructions and unsupported text can hold plain file-path strings.
        remainder = text
        masked_tokens = tokens + [token for token, unused in selected_paths.get(source, [])]
        for token in sorted(masked_tokens, key=lambda item: item.start, reverse=True):
            remainder = remainder[:token.start] + " " * (token.end - token.start) + remainder[token.end:]
        active_remainder = remainder
        protected_spans = literal_spans(text) if extension in REFERENCE_EXTENSIONS and extension != ".canvas" else []
        for start, end in sorted(protected_spans, reverse=True):
            active_remainder = active_remainder[:start] + " " * (end - start) + active_remainder[end:]
        context_literals = [old for old in old_literals
                            if any(old in remainder[start:end] for start, end in protected_spans)]
        if context_literals:
            unresolved.append({"code": "context_sensitive_path_reference", "file": source,
                               "paths": context_literals, "action": "example/provenance preserved; not treated as an operational dependency"})
        literals = [old for old in old_literals if old in active_remainder]
        if literals and (under(source, system_root) or extension not in REFERENCE_EXTENSIONS):
            blocked.append({"code": "system_handoff" if under(source, system_root) else "unsupported_path_reference",
                            "file": source, "paths": literals})
        elif literals:
            unresolved.append({"code": "context_sensitive_path_reference", "file": source,
                               "paths": literals, "action": "literal content preserved; review context before any separate repair"})
        # Relative paths in executable text need a maintainer, not guessed edits.
        # In Markdown these can instead be historical quotations, so report them.
        for match in QUOTED_PATH.finditer(active_remainder):
            value = match.group(2)
            if not ("/" in value or Path(value).suffix):
                continue
            target = literal_path_target(value, source, old_index, vault)
            if target and (relocate(target, moves) != target or relocate(source, moves) != source):
                issue = {"code": "system_handoff" if under(source, system_root) else "unsupported_path_reference",
                         "file": source, "target": target}
                if under(source, system_root) or extension not in REFERENCE_EXTENSIONS:
                    blocked.append(issue)
                else:
                    unresolved.append(dict(issue, code="context_sensitive_path_reference"))
        if extension in {".css", ".html", ".htm", ".svg"}:
            for match in CSS_URL.finditer(active_remainder):
                value = next(group for group in match.groups() if group is not None)
                target, unused = resolve(Token(0, len(value), "markdown", value), source, old_index, vault)
                if target and (relocate(target, moves) != target or relocate(source, moves) != source):
                    blocked.append({"code": "unsupported_css_reference", "file": source, "target": target})
        updated = replace_tokens(text, sorted(replacements, key=lambda pair: pair[0].start)).encode("utf-8")
        documents[source] = {"before": original, "after": updated, "edges": edges}
        if updated != original:
            edits[source] = updated
            snapshots.setdefault(source, (hashlib.sha256(original).hexdigest(), path.stat().st_mode))
    # 2. Verify all previously resolved supported tokens against the virtual new tree.
    for source, document in documents.items():
        extension = Path(source).suffix.lower()
        if extension not in REFERENCE_EXTENSIONS:
            continue
        found = []
        for token in reference_tokens(document["after"].decode("utf-8"), extension):
            target, unused = resolve(token, relocate(source, moves), new_index, vault)
            found.append((token.kind, target))
        if len(found) != len(document["edges"]) or any(
                expected_target is not None and (new_kind != expected_kind or new_target != expected_target)
                for (expected_kind, expected_target), (new_kind, new_target)
                in zip(document["edges"], found)):
            blocked.append({"code": "reference_verification_failed", "file": source})
    return {"vault": vault, "moves": moves, "holds": holds, "system_root": system_root,
            "files": files, "directories": directories, "skipped": skipped,
            "moved_files": moved_files, "moved_directories": moved_directories,
            "snapshots": snapshots, "edits": edits, "documents": documents,
            "blocked": blocked, "warnings": unresolved, "resolved": resolved_count,
            "path_edits": path_edits or []}


def checkpoint(stage, path=None):
    """A no-op boundary allows synthetic tests to inject failures or concurrent edits."""
    return None


def make_directories(vault, path, created):
    missing = []
    current = path
    while current != vault and not current.exists():
        missing.append(current)
        current = current.parent
    checked_path(vault, path.relative_to(vault).as_posix())
    for directory in reversed(missing):
        directory.mkdir()  # Exclusive: an unexpected concurrent creation fails.
        created.append(directory)


def move_file_exclusive(source, destination):
    # A hard link creates the destination exclusively and preserves file bytes and
    # metadata. Unsupported filesystems fail safely; nothing is copied over a name.
    try:
        os.link(source, destination, follow_symlinks=False)
    except OSError as error:
        if error.errno in {errno.EXDEV, errno.EPERM, errno.ENOTSUP}:
            raise MoveError("Exclusive hard-link moves are unsupported on this filesystem.") from error
        raise
    try:
        source.unlink()
    except BaseException:
        # Source still exists; remove only the new link we created.
        if destination.exists() and source.exists() and os.path.samefile(source, destination):
            destination.unlink()
        raise


def atomic_bytes(path, data, expected_digest, mode):
    if path.is_symlink() or not path.is_file() or digest(path) != expected_digest:
        raise MoveError("Concurrent reference edit detected: " + str(path))
    descriptor, temporary = tempfile.mkstemp(prefix=".move_files_", dir=path.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, stat.S_IMODE(mode))
        if path.is_symlink() or digest(path) != expected_digest:
            raise MoveError("Concurrent reference edit detected: " + str(path))
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def result_summary(transaction):
    return {"status": "blocked" if transaction["blocked"] else "dry_run",
            "moves": [{"source": source, "destination": destination}
                      for source, destination in transaction["moves"]],
            "file_count": len(transaction["moved_files"]),
            "reference_updates": [{"file": relocate(source, transaction["moves"])}
                                  for source in transaction["edits"]],
            "resolved_references_checked": transaction["resolved"],
            "reviewed_path_edits": len(transaction["path_edits"]),
            "blocked": transaction["blocked"], "warnings": transaction["warnings"],
            "scope": {"supported": "wiki, inline/reference Markdown, HTML href/src, Canvas file fields, and exact reviewed literal path spans",
                      "excluded": "unselected literals and unselected fenced paths, binary-embedded links, CSS/srcset, app-private data, external files, and skipped directories",
                      "skipped_paths": transaction["skipped"]}}


def check_late_references(transaction):
    """Notice affected links added during apply without blocking unrelated work."""
    vault, moves = transaction["vault"], transaction["moves"]
    files, directories, unused = inventory(vault)
    current_index = path_index(files, directories)
    original_index = path_index(
        list(dict.fromkeys(transaction["files"] + list(transaction["moved_files"]))),
        list(dict.fromkeys(transaction["directories"] + list(transaction["moved_directories"]))))
    inverse = {destination: source for source, destination in transaction["moved_files"].items()}
    for current in files:
        extension = Path(current).suffix.lower()
        if extension not in REFERENCE_EXTENSIONS | OTHER_TEXT_EXTENSIONS or (vault / current).stat().st_size > MAX_TEXT_BYTES:
            continue
        source = inverse.get(current, current)
        data = checked_path(vault, current).read_bytes()
        baseline = transaction["documents"].get(source)
        if baseline and data == baseline["after"]:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        before = baseline["after"].decode("utf-8") if baseline else ""
        # Exact reviewed paths and detectable literal references added by another
        # writer must not be left behind while a related move is being committed.
        literals = {value for old, unused in moves
                    for value in (old, str(vault / old), quote(old, safe="/"))}
        if transaction["path_edits"]:
            literals.update(entry["old"] for entry in transaction["path_edits"])
        for match in QUOTED_PATH.finditer(text):
            value = match.group(2)
            target = literal_path_target(value, source, original_index, vault)
            if target and (relocate(target, moves) != target or relocate(source, moves) != source):
                literals.add(value)
        if any(text.count(value) > before.count(value) for value in literals):
            raise MoveError("An affected literal path appeared during apply: " + current)
        for token in reference_tokens(text, extension) if extension in REFERENCE_EXTENSIONS else []:
            old_target, unused = resolve(token, source, original_index, vault)
            if old_target and relocate(old_target, moves) != old_target:
                actual, unused = resolve(token, current, current_index, vault)
                if actual != relocate(old_target, moves):
                    raise MoveError("An affected incoming reference appeared during apply: " + current)


def apply_transaction(transaction, backup_dir=None):
    """Execute a prepared transaction; rollback never replaces a concurrent edit."""
    result = result_summary(transaction)
    if transaction["blocked"]:
        return result
    vault = transaction["vault"]
    if backup_dir is None:
        temporary_root = Path(tempfile.gettempdir()).resolve()
        if temporary_root == vault.resolve() or vault.resolve() in temporary_root.parents:
            raise MoveError("Specify an outside-vault --backup-dir for this vault location.")
        backup = Path(tempfile.mkdtemp(prefix="astoria_file_moves_"))
    else:
        backup = Path(backup_dir).absolute()
        if backup.resolve() == vault.resolve() or vault.resolve() in backup.resolve().parents:
            raise MoveError("Recovery originals must be outside the vault.")
        backup.mkdir(parents=True, exist_ok=False)
    backup.chmod(0o700)
    result["backup_dir"] = str(backup)
    moved, written, created, removed_directories = [], [], [], []
    try:
        # 3. Keep originals outside the vault before the first mutation.
        originals = set(transaction["moved_files"]) | set(transaction["edits"])
        for relative in sorted(originals):
            destination = backup / "originals" / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(checked_path(vault, relative), destination)
        recovery = {"moves": transaction["moves"], "file_moves": transaction["moved_files"],
                    "reference_updates": list(transaction["edits"])}
        (backup / "recovery.json").write_text(json.dumps(recovery, ensure_ascii=False, indent=2))
        checkpoint("after_backup")
        fresh = prepare(vault, [{"source": source, "destination": destination}
                                for source, destination in transaction["moves"]],
                        transaction["system_root"], transaction["holds"], transaction["path_edits"])
        if (fresh["blocked"] or fresh["edits"] != transaction["edits"]
                or fresh["moved_files"] != transaction["moved_files"]
                or fresh["moved_directories"] != transaction["moved_directories"]):
            raise MoveError("Affected files or incoming references changed after preflight; rerun the dry-run.")
        for source, (expected, unused_mode) in transaction["snapshots"].items():
            if digest(checked_path(vault, source)) != expected:
                raise MoveError("A source or reference changed after preflight: " + source)
        for unused_source, destination in transaction["moves"]:
            if os.path.lexists(checked_path(vault, destination)):
                raise MoveError("Destination appeared after preflight: " + destination)
        # Folder entries preserve every internal path, including empty folders.
        for source, destination in sorted(transaction["moved_directories"].items(), key=lambda pair: len(Path(pair[1]).parts)):
            if os.path.lexists(vault / destination) and vault / destination not in created:
                raise MoveError("Destination directory appeared during apply: " + destination)
            make_directories(vault, vault / destination, created)
        for source, destination in transaction["moved_files"].items():
            source_path, destination_path = checked_path(vault, source), checked_path(vault, destination)
            make_directories(vault, destination_path.parent, created)
            if digest(source_path) != transaction["snapshots"][source][0]:
                raise MoveError("Source changed before move: " + source)
            move_file_exclusive(source_path, destination_path)
            moved.append((source, destination))
            checkpoint("after_move", destination)
        # Only the located tokens are rewritten; prose, headings, and logs remain.
        for source, data in transaction["edits"].items():
            destination = relocate(source, transaction["moves"])
            path = checked_path(vault, destination)
            expected, mode = transaction["snapshots"][source]
            atomic_bytes(path, data, expected, mode)
            written.append((source, destination, hashlib.sha256(data).hexdigest()))
            checkpoint("after_write", destination)
        for source, destination in sorted(transaction["moved_directories"].items(), key=lambda pair: len(Path(pair[0]).parts), reverse=True):
            source_path, destination_path = checked_path(vault, source), checked_path(vault, destination)
            shutil.copystat(source_path, destination_path, follow_symlinks=False)
            source_path.rmdir()  # Concurrent additions prevent deletion.
            removed_directories.append(source)
        # 4. Verify moved bytes and every planned reference update before success.
        for source, destination in transaction["moved_files"].items():
            expected = (hashlib.sha256(transaction["edits"][source]).hexdigest()
                        if source in transaction["edits"] else transaction["snapshots"][source][0])
            if digest(checked_path(vault, destination)) != expected:
                raise MoveError("Post-move content verification failed: " + destination)
        for source, data in transaction["edits"].items():
            if checked_path(vault, relocate(source, transaction["moves"])).read_bytes() != data:
                raise MoveError("Post-write reference verification failed: " + source)
        check_late_references(transaction)
        result.update(status="applied", verified=True)
        return result
    except BaseException as error:
        conflicts = []
        # 5. Restore only bytes/names still matching this transaction's writes.
        for source, destination, expected in reversed(written):
            try:
                path = checked_path(vault, destination)
                if not path.is_file() or digest(path) != expected:
                    raise MoveError("Concurrent reference edit retained.")
                original = (backup / "originals" / source).read_bytes()
                atomic_bytes(path, original, expected, transaction["snapshots"][source][1])
            except (OSError, MoveError) as rollback_error:
                conflicts.append({"file": destination, "reason": str(rollback_error)})
        for source, destination in reversed(moved):
            try:
                source_path, destination_path = checked_path(vault, source), checked_path(vault, destination)
                expected = transaction["snapshots"][source][0]
                if os.path.lexists(source_path) or not destination_path.is_file() or destination_path.is_symlink() or digest(destination_path) != expected:
                    conflicts.append({"file": destination, "reason": "concurrent bytes or source path retained"})
                    continue
                make_directories(vault, source_path.parent, [])
                move_file_exclusive(destination_path, source_path)
            except (OSError, MoveError) as rollback_error:
                conflicts.append({"file": destination, "reason": str(rollback_error)})
        for source in sorted(removed_directories, key=lambda relative: len(Path(relative).parts)):
            try:
                make_directories(vault, vault / source, [])
            except (OSError, MoveError) as rollback_error:
                conflicts.append({"file": source, "reason": str(rollback_error)})
        for directory in sorted(created, key=lambda path: len(path.parts), reverse=True):
            try:
                checked_path(vault, directory.relative_to(vault).as_posix())
                directory.rmdir()
            except (OSError, MoveError):
                pass  # Nonempty directories may contain a concurrent file.
        result.update(status="rollback_incomplete" if conflicts else "rolled_back", verified=False,
                      error=str(error), rollback_conflicts=conflicts)
        return result


def execute(vault, rows, apply=False, system_root="00 ASTORIA", holds=(), backup_dir=None, path_edits=None):
    try:
        transaction = prepare(vault, rows, system_root, holds, path_edits)
        return apply_transaction(transaction, backup_dir) if apply else result_summary(transaction)
    except (MoveError, OSError, ValueError) as error:
        return {"status": "blocked", "blocked": [{"code": "preflight", "reason": str(error)}]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--plan", required=True, help="JSON list of caller-selected relative source/destination paths")
    parser.add_argument("--path-edits", help="JSON list of reviewed file/start/old/new spans; optional base vault or document")
    parser.add_argument("--system-root", default="00 ASTORIA")
    parser.add_argument("--hold", action="append", default=[], help="Held relative file or package; repeat as needed")
    parser.add_argument("--backup-dir", help="New recovery directory outside the vault; apply only")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        rows = json.loads(Path(args.plan).read_text())
        path_edits = json.loads(Path(args.path_edits).read_text()) if args.path_edits else None
        result = execute(args.vault, rows, args.apply, args.system_root, args.hold, args.backup_dir, path_edits)
    except (OSError, ValueError) as error:
        result = {"status": "blocked", "blocked": [{"code": "plan", "reason": str(error)}]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"dry_run", "applied"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
