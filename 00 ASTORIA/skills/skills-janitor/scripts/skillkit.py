#!/usr/bin/env python3
"""skillkit: shared helpers for the ASTORIA skill scripts.

PyYAML reads the YAML vocabulary configuration. Skill frontmatter uses
PyYAML when available or a small fallback parser for the skill schema.
Import from lint.py, build_views.py, and skill-builder/scripts/new_skill.py.
"""
from contextlib import contextmanager
import json, os, re, stat, sys, textwrap
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

SKILLS_REL = os.path.join("00 ASTORIA", "skills")
CATALOG_REL = os.path.join("00 ASTORIA", "specialized_skills")  # starter vault catalog, removed at the end of setup
MAP_REL = os.path.join("00 ASTORIA", "Skill Map.md")
SYSTEMS_REL = os.path.join("00 ASTORIA", "systems")
VOCAB_REL = os.path.join(SKILLS_REL, "skill-builder", "assets", "vocabulary.md")
ALLOWED_TOP = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
CORE_META = ["level", "system", "dependencies", "created", "updated"]
RESEARCH_META = ["part", "family", "modality", "population", "requires", "gates"]
META_ORDER = ["level", "system", "part", "family", "modality", "population",
              "dependencies", "requires", "gates", "created", "updated"]
TRIG_RE = re.compile(r"\bTriggers:\s*(.*?)\s*\.?\s*$", re.S)
FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)
MARK_START = "<!-- {name}:start -->"
MARK_END = "<!-- {name}:end -->"


def find_vault(start=None):
    """Walk up from start (or this file) until a folder holds AGENTS.md and 00 ASTORIA."""
    p = os.path.abspath(start or os.path.dirname(__file__))
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and os.path.isdir(os.path.join(p, "00 ASTORIA")):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            raise SystemExit("vault root not found (needs AGENTS.md and 00 ASTORIA); pass --vault")
        p = parent


def vault_from_argv(argv):
    for i, a in enumerate(argv):
        if a == "--vault" and i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
        if a.startswith("--vault="):
            return os.path.abspath(a.split("=", 1)[1])
    return find_vault()


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None, text
    raw = m.group(1)
    body = text[m.end():]
    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
        except Exception as e:
            return {"__error__": str(e)}, body
        return (data if isinstance(data, dict) else {"__error__": "frontmatter is not a mapping"}), body
    return _mini_yaml(raw), body


def _mini_yaml(raw):
    """Minimal parser: scalars, `>-`/`|` block scalars, one nested mapping (metadata)."""
    data, cur, key, block, indent = {}, None, None, None, 0
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if block is not None:
            if line.startswith(" " * indent) or not line.strip():
                block.append(line[indent:] if len(line) >= indent else "")
                i += 1
                continue
            text = " ".join(x.strip() for x in block).strip() if block_kind == ">" else "\n".join(block).rstrip("\n")
            (cur if cur is not None else data)[key] = text
            block = None
        m = re.match(r"^(\s*)([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        sp, k, v = len(m.group(1)), m.group(2), m.group(3).strip()
        if sp == 0:
            cur = None
            if v in (">-", "|", ">", "|-"):
                key, block, indent, block_kind = k, [], 2, v[0]
            elif v == "":
                data[k] = {}
                cur = data[k]
            else:
                data[k] = _scalar(v)
        else:
            if cur is None:
                i += 1
                continue
            if v in (">-", "|", ">", "|-"):
                key, block, indent, block_kind = k, [], sp + 2, v[0]
            else:
                cur[k] = _scalar(v)
        i += 1
    if block is not None:
        text = " ".join(x.strip() for x in block).strip() if block_kind == ">" else "\n".join(block).rstrip("\n")
        (cur if cur is not None else data)[key] = text
    return data


def _scalar(v):
    if len(v) >= 2 and v[0] == v[-1] == '"':
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            return v[1:-1]
    if len(v) >= 2 and v[0] == v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


class Skill:
    def __init__(self, name, folder, path, fm, body, text, vault=""):
        self.name, self.folder, self.path, self.fm, self.body, self.text = name, folder, path, fm, body, text
        self.vault = vault
        self.description = " ".join(str(fm.get("description", "") or "").split())
        md = fm.get("metadata") or {}
        self.meta = {k: ("" if v is None else str(v)) for k, v in md.items()} if isinstance(md, dict) else {}
        self.level = self.meta.get("level", "")
        self.system = self.meta.get("system", "")
        self.part = self.meta.get("part", "")
        self.family = self.meta.get("family", "")
        self.lines = text.count("\n") + 1

    @property
    def summary(self):
        text = self.description_text
        first = re.split(r"(?<=[.!?])\s+", text, 1)[0]
        return first.strip()

    @property
    def description_text(self):
        m = TRIG_RE.search(self.description)
        return self.description[: m.start()].strip() if m else self.description

    @property
    def triggers(self):
        return split_triggers(self.description)

    @property
    def dependencies(self):
        return [d.strip() for d in self.meta.get("dependencies", "").split(",") if d.strip()]

    def link(self, alias=None):
        return "[[%s|%s]]" % (self.folder.replace(os.sep, "/") + "/SKILL", alias or self.name)

    def text_files(self):
        """SKILL.md plus every .md, .py, .yaml, and .txt file under the skill folder."""
        out = []
        for root, dirs, files in os.walk(os.path.join(self.vault, self.folder)):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
            for f in files:
                if f.endswith((".md", ".py", ".yaml", ".yml", ".txt")):
                    out.append(os.path.join(root, f))
        return out


def split_triggers(description):
    m = TRIG_RE.search(description)
    if not m:
        return []
    return [p.strip().rstrip(".") for p in m.group(1).split(",") if p.strip()]


def load_skills(vault, rel=None):
    """Load the skills under vault/rel (default the live set; pass CATALOG_REL for the catalog)."""
    skills = {}
    root = os.path.join(vault, rel or SKILLS_REL)
    if not os.path.isdir(root):
        return skills
    for entry in sorted(os.listdir(root)):
        folder = os.path.join(root, entry)
        p = os.path.join(folder, "SKILL.md")
        if not os.path.isdir(folder) or not os.path.isfile(p):
            continue
        text = open(p, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        if fm is None:
            fm = {"__error__": "no frontmatter"}
        rel = os.path.relpath(folder, vault)
        skills[entry] = Skill(entry, rel, p, fm, body, text, vault)
    return skills


SPECIALIZED_FAMILIES = {"modality-coordinator", "software-adapter", "model-adapter", "datasets",
                        "acquisition", "computing", "method-guide"}


def is_specialized(skill, vocab):
    """The basic-versus-specialized rule for the Research Assistant System.

    Specialized: a research skill whose family is in the vocabulary's
    starter.specialized_families, or whose modality is anything other than
    'any' or empty. Everything else (companions, coordinators, general
    literature, critique, hypothesis, design, power, analysis, writing,
    support) is basic and ships in the starter's live set.
    """
    if skill.system != "Research Assistant System":
        return False
    if skill.level in ("companion",) or skill.family == "part-coordinator":
        return False
    fams = set((vocab.get("starter") or {}).get("specialized_families") or SPECIALIZED_FAMILIES)
    if skill.family in fams:
        return True
    modality = skill.meta.get("modality", "") or ""
    return modality not in ("", "any")


def load_vocab(vault):
    text = open(os.path.join(vault, VOCAB_REL), encoding="utf-8").read()
    m = re.search(r"```yaml\n(.*?)\n```", text, re.S)
    if not m:
        raise SystemExit("vocabulary.md has no YAML configuration block")
    if yaml is None:
        raise SystemExit("PyYAML is needed to read vocabulary.md")
    vocabulary = yaml.safe_load(m.group(1))
    if not isinstance(vocabulary, dict):
        raise SystemExit("vocabulary.md configuration must be a mapping")
    return vocabulary


def fold(text, width=78, indent="  "):
    lines = textwrap.wrap(" ".join(text.split()), width=width, break_long_words=False, break_on_hyphens=False)
    return "\n".join(indent + l for l in lines)


def dump_frontmatter(name, description, meta, extra=None):
    """Write the standard frontmatter: name, description (folded), optional extras, metadata."""
    out = ["---", "name: %s" % name, "description: >-", fold(description)]
    for k, v in (extra or {}).items():
        out.append("%s: %s" % (k, v))
    out.append("metadata:")
    ordered = [k for k in META_ORDER if k in meta] + [k for k in meta if k not in META_ORDER]
    for k in ordered:
        v = meta[k]
        if v is None:
            v = ""
        out.append("  %s: %s" % (k, _yaml_str(str(v))))
    out.append("---")
    return "\n".join(out) + "\n"


def _yaml_str(v):
    if v == "":
        return '""'
    needs = (re.match(r"^[\d\-\.:]+$", v) is not None) or v.lower() in ("true", "false", "null", "yes", "no") \
        or ":" in v or v[0] in "#&*!|>'\"%@`[]{},-?" or v != v.strip()
    if needs:
        return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return v


def replace_between(text, marker, new_block):
    start, end = MARK_START.format(name=marker), MARK_END.format(name=marker)
    if start not in text or end not in text:
        return None
    pre = text[: text.index(start) + len(start)]
    post = text[text.index(end):]
    return pre + "\n" + new_block.rstrip("\n") + "\n" + post


def walk_notes(vault, include_hidden=False):
    for root, dirs, files in os.walk(vault):
        rel_root = os.path.relpath(root, vault)
        # Runtime dependency and bytecode trees are not vault notes.
        dirs[:] = [d for d in dirs if d not in {"__pycache__", "node_modules"}]
        if not include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f), (f if rel_root == "." else os.path.join(rel_root, f))


def portable_links_enabled(vocab):
    """Only the public starter opts in; private-vault views retain wiki links."""
    return (vocab.get("starter") or {}).get("portable_links") is True


def _markdown_prose(text, edit):
    """Edit prose spans while preserving frontmatter, fences, and inline code."""
    frontmatter = FM_RE.match(text)
    prefix = text[:frontmatter.end()] if frontmatter else ""
    text = text[len(prefix):]
    out, prose, fence = [prefix], [], None

    def flush():
        if not prose:
            return
        block = "".join(prose)
        # A closing code delimiter must have exactly the opening run's length.
        cursor = 0
        for opening in re.finditer(r"(?<!`)(`+)(?!`)", block):
            if opening.start() < cursor:
                continue
            closing = re.search(r"(?<!`)" + re.escape(opening.group()) + r"(?!`)", block[opening.end():])
            if not closing:
                continue
            end = opening.end() + closing.end()
            out.append(edit(block[cursor:opening.start()]))
            out.append(block[opening.start():end])
            cursor = end
        out.append(edit(block[cursor:]))
        prose.clear()

    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(?:>\s*)*(`{3,}|~{3,})", line)
        if marker and fence is None:
            flush()
            fence = marker.group(1)
            out.append(line)
        elif fence is not None:
            out.append(line)
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = None
        else:
            prose.append(line)
    flush()
    return "".join(out)


def logical_path(path):
    """Use slash-delimited names for link comparisons only."""
    return os.fspath(path).replace("\\", "/")


class PortableLinks:
    """Resolve actual package files, without reading outside the package root.

    Relocations map old to new vault-relative folders during optional install.
    Missing optional skills become explicit lookup labels; all other unresolved
    real links are reported rather than guessed. No registry is written.
    """
    WIKI = re.compile(r"(?<!\\)(!?)\[\[([^\]\n]+)\]\]")
    MARKDOWN = re.compile(r'(!?\[[^\]\n]*\]\()\s*(<[^>\n]+>|(?:[^\s()]|\([^\s()]*\))+)((?:\s+["\'][^\n]*?["\'])?\s*\))')
    REFERENCE = re.compile(r'(?m)^( {0,3}\[[^\]\n]+\]:[ \t]*)(<[^>\n]+>|[^\s]+)([^\n]*)$')

    def __init__(self, vault, relocations=None, unavailable_skills=()):
        self.root = Path(vault).resolve()
        self.moves = {logical_path(a).rstrip("/"): logical_path(b).rstrip("/")
                      for a, b in (relocations or {}).items()}
        self.unavailable = set(unavailable_skills)
        self.skills_prefix = logical_path(SKILLS_REL) + "/"
        self.catalog_prefix = logical_path(CATALOG_REL) + "/"
        self.files, self.names, self.identities = set(), {}, {}
        self.problems = []
        for p in sorted(self.root.rglob("*")):
            relative = p.relative_to(self.root).as_posix()
            if any(part.startswith(".") for part in p.relative_to(self.root).parts) or self._omitted(relative):
                continue
            try:
                mode = p.lstat().st_mode
                if stat.S_ISDIR(mode):
                    if p.resolve(strict=True) != p:
                        raise ValueError("Markdown tree contains a directory alias")
                    continue
                if stat.S_ISLNK(mode) and p.is_dir():
                    raise ValueError("Markdown tree contains a directory alias")
                if p.suffix.lower() == ".md":
                    self.identities[relative] = self._markdown_path_identity(p)
                    self.files.add(relative)
                elif not p.is_file() or not self._inside(p):
                    continue
            except (OSError, ValueError, RuntimeError) as error:
                self._problem(relative, relative, str(error))
                continue
            for name in {p.name, p.stem}:
                self.names.setdefault(name, set()).add(relative)

    @staticmethod
    def _markdown_identity(info):
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError("Markdown requires a regular file without aliases")
        return info.st_dev, info.st_ino

    def _markdown_path_identity(self, path):
        identity = self._markdown_identity(path.lstat())
        if path.resolve(strict=True) != path:
            raise ValueError("Markdown path crosses an alias")
        return identity

    @contextmanager
    def _open_markdown(self, relative, write=False):
        path = self.root / relative
        expected = self.identities[relative]
        if self._markdown_path_identity(path) != expected:
            raise ValueError("Markdown file identity changed")
        flags = os.O_RDWR if write else os.O_RDONLY
        flags |= getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0) | getattr(os, "O_NONBLOCK", 0)
        with os.fdopen(os.open(path, flags), "r+b" if write else "rb") as handle:
            self._verify_markdown_handle(handle, path, expected)
            yield handle

    def _verify_markdown_handle(self, handle, path, expected):
        if (self._markdown_identity(os.fstat(handle.fileno())) != expected
                or self._markdown_path_identity(path) != expected):
            raise ValueError("Markdown file identity changed")

    def read_markdown(self, relative):
        with self._open_markdown(relative) as handle:
            original = handle.read()
            self._verify_markdown_handle(handle, self.root / relative, self.identities[relative])
            return original

    def write_markdown(self, relative, original, replacement):
        with self._open_markdown(relative, write=True) as handle:
            if handle.read() != original:
                raise ValueError("Markdown content changed before link repair")
            self._verify_markdown_handle(handle, self.root / relative, self.identities[relative])
            handle.seek(0)
            handle.write(replacement)
            handle.truncate()

    def _inside(self, path):
        try:
            path.resolve().relative_to(self.root)
            return True
        except ValueError:
            return False

    def _omitted(self, target):
        return any(target == self.catalog_prefix + n or target.startswith(self.catalog_prefix + n + "/")
                   for n in self.unavailable)

    def _relocate(self, path):
        for old, new in sorted(self.moves.items(), key=lambda item: -len(item[0])):
            if path == old or path.startswith(old + "/"):
                return new + path[len(old):]
        return path

    def _original(self, document):
        for old, new in self.moves.items():
            if document == new or document.startswith(new + "/"):
                return old + document[len(new):]
        return document

    @staticmethod
    def _placeholder(target):
        return bool(re.search(r"[{}<>]|\.\.\.|…", target))

    @staticmethod
    def _slug(heading):
        # GitHub-style heading fragments preserve Unicode letters and numbers.
        heading = re.sub(r"<[^>]*>", "", heading).strip().lower()
        heading = re.sub(r"[^\w\-\s]", "", heading)
        return re.sub(r"\s", "-", heading)

    @staticmethod
    def _skill_name(target):
        m = re.search(r"(?:^|/)(?:skills|specialized_skills)/([^/]+)/SKILL(?:\.md)?$", target)
        return m.group(1) if m else None

    @staticmethod
    def _runtime(target):
        return target in {"me", "me.md", "00 ASTORIA/agent_notes/layout", "00 ASTORIA/agent_notes/layout.md",
                          "00 ASTORIA/agent_notes/ai_log", "00 ASTORIA/agent_notes/ai_log.md"}

    def _problem(self, document, target, reason):
        self.problems.append("%s: %s: %s" % (document, reason, target))

    def _relative(self, target, document):
        return quote(os.path.relpath(target, os.path.dirname(document) or ".").replace(os.sep, "/"), safe="/")

    def _resolve(self, target, document):
        candidates = []
        original = self._original(document)
        for base in (self.root / Path(original).parent, self.root):
            p = base / target
            if not self._inside(p):
                continue
            rel = p.resolve().relative_to(self.root).as_posix()
            candidates.extend([self._relocate(rel), self._relocate(rel + ".md")])
        # Canonical skill paths remain useful when a skill is still in the catalog.
        for candidate in list(candidates):
            if candidate.startswith(self.skills_prefix):
                candidates.append(self.catalog_prefix + candidate[len(self.skills_prefix):])
            elif candidate.startswith(self.catalog_prefix):
                candidates.append(self.skills_prefix + candidate[len(self.catalog_prefix):])
        for candidate in candidates:
            p = self.root / candidate
            if not self._omitted(candidate) and self._inside(p) and p.is_file():
                return candidate
        if "/" not in target:
            matches = self.names.get(target, set())
            if len(matches) == 1:
                return next(iter(matches))
            if len(matches) > 1:
                self._problem(document, target, "ambiguous local link")
                return None
        return None

    def rewrite(self, text, document):
        document = logical_path(document)
        if not self._inside(self.root / document):
            raise ValueError("document is outside portable root: " + document)

        def wiki(match):
            embed, contents = match.groups()
            lookup, separator, alias = contents.partition("|")
            target, anchor_separator, anchor = lookup.partition("#")
            if self._placeholder(lookup):
                return match.group()
            label = alias if separator else (Path(target).name or anchor)
            if embed and re.fullmatch(r"\d+(?:x\d+)?", alias):
                label = Path(target).name
            if target.startswith(("/", "\\")) or "\\" in target or any(p == ".." for p in Path(target).parts) and not self._inside(self.root / Path(self._original(document)).parent / target):
                self._problem(document, lookup, "local link escapes package")
                return match.group()
            if anchor.startswith("^"):
                self._problem(document, lookup, "block reference has no portable heading target")
                return match.group()
            name = self._skill_name(target)
            if name in self.unavailable:
                return "%s (optional skill `%s`; not installed)" % (label, name)
            resolved = self._resolve(target, document) if target else document
            if resolved is None:
                if self._runtime(target):
                    return "`%s` (created during setup)" % target
                self._problem(document, lookup, "unresolved local wiki link")
                return match.group()
            fragment = "#" + quote(self._slug(anchor), safe="-") if anchor_separator else ""
            escaped_label = label.replace("[", "\\[").replace("]", "\\]")
            return "%s[%s](%s%s)" % ("!" if embed else "", escaped_label,
                                      "" if not target else self._relative(resolved, document), fragment)

        def markdown(match, reference=False):
            prefix, raw, ending = match.groups()
            target = raw[1:-1] if raw.startswith("<") else raw
            parsed = urlsplit(target)
            if parsed.scheme.lower() == "file":
                self._problem(document, target, "file URI is not a portable local link")
                return match.group()
            if parsed.scheme or parsed.netloc or not parsed.path or self._placeholder(unquote(parsed.path)):
                return match.group()
            path = unquote(parsed.path)
            source = self.root / Path(self._original(document)).parent / path
            if Path(path).is_absolute() or not self._inside(source):
                self._problem(document, target, "local link escapes package")
                return match.group()
            old = source.resolve().relative_to(self.root).as_posix()
            name = self._skill_name(old)
            if name in self.unavailable:
                if reference:
                    self._problem(document, target, "optional skill reference definition needs an explicit prose label")
                    return match.group()
                label = prefix[prefix.index("[") + 1:-2]
                return "%s (optional skill `%s`; not installed)" % (label, name)
            resolved = self._relocate(old)
            if self._omitted(resolved) or not (self.root / resolved).is_file():
                if self._runtime(old):
                    return "`%s` (created during setup)" % old
                self._problem(document, target, "unresolved local Markdown link")
                return match.group()
            suffix = ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")
            return prefix + self._relative(resolved, document) + suffix + ending

        # Existing Markdown is rebased first, so new wiki replacements are not moved twice.
        def edit(prose):
            prose = self.REFERENCE.sub(lambda match: markdown(match, reference=True), prose)
            return self.WIKI.sub(wiki, self.MARKDOWN.sub(markdown, prose))
        return _markdown_prose(text, edit)


def portable_vault_links(vault, relocations=None, unavailable_skills=(), write=True):
    """Plan every edit first; unresolved real links prevent all writes."""
    links = PortableLinks(vault, relocations, unavailable_skills)
    originals, changed = {}, {}
    for rel in sorted(links.files):
        try:
            original = links.read_markdown(rel)
            originals[rel] = original
            rewritten = links.rewrite(original.decode("utf-8"), rel).encode("utf-8")
            if rewritten != original:
                changed[rel] = rewritten
        except (OSError, ValueError, RuntimeError) as error:
            links._problem(rel, rel, str(error))
    if write and not links.problems and changed:
        # Recheck the planned inputs before any write. Open each output without
        # truncation, then verify the original identity and bytes again.
        for rel, original in originals.items():
            try:
                if links.read_markdown(rel) != original:
                    raise ValueError("Markdown content changed before link repair")
            except (OSError, ValueError, RuntimeError) as error:
                links._problem(rel, rel, str(error))
        if not links.problems:
            for rel, replacement in changed.items():
                try:
                    links.write_markdown(rel, originals[rel], replacement)
                except (OSError, ValueError, RuntimeError) as error:
                    links._problem(rel, rel, str(error))
                    break
    return sorted(changed), links.problems
