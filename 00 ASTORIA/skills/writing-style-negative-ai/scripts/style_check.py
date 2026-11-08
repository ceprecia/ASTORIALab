#!/usr/bin/env python3
"""Report unfinished draft markers and duplicate paragraphs.

Run: python3 style_check.py draft.md [--quiet] [--allow "phrase,phrase"]
The script skips recognized top-level and simple list fences, top-level
indented code, and some inline or quoted material. Nested containers and raw
HTML are outside the block scanner's scope. Interpret diagnostics in the
context of the document and recipient-supplied style guide.
"""
import re
import statistics
import sys

# Toggles
SOFT_LIMIT_PER_500_WORDS = 4
# Recipient-supplied phrases may be excluded with --allow.
DEFAULT_ALLOW = []

# family, severity, regex, hint. Regexes are case-insensitive and word-bounded where it matters.
RULES = [
    ("unfinished", "hard", r"\b(?:TODO|TBD|TK)\b", "resolve this draft placeholder from the task sources"),
    ("source", "hard", r"\[(?:citation|source) needed\]", "provide the source or retain the gap explicitly"),
]

COMPILED = [(fam, sev, re.compile(rx, re.IGNORECASE | re.MULTILINE), hint) for fam, sev, rx, hint in RULES]

FENCE_LINE = re.compile(r" {0,3}(\x60{3,}|~{3,})(.*)\Z")
LIST_ITEM = re.compile(r"( {0,3})([-+*]|[0-9]{1,9}[.)])(?:( +)(.*))?\Z")
BLOCK_BOUNDARY = re.compile(r" {0,3}(?:#{1,6}(?: |$)|(?:(?:- *){3,}|(?:\* *){3,}|(?:_ *){3,})$)")
SETEXT_UNDERLINE = re.compile(r" {0,3}(?:=+|-+) *$")


def opening_fence(content):
    match = FENCE_LINE.fullmatch(content)
    if match and (match[1][0] == "~" or "\x60" not in match[2]):
        return match[1]
    return None


def blank_code_blocks(text):
    """Mask supported fenced and top-level indented code with line endings intact."""
    output = []
    fence = None
    list_indent = 0
    nested_list = False
    paragraph = False
    for line in text.splitlines(keepends=True):
        body = line.splitlines()[0]
        expanded = body.expandtabs(4)
        indent = len(expanded) - len(expanded.lstrip(" "))
        blank = indent == len(expanded)
        masked = " " + line[len(body):]

        if fence and list_indent and not blank and indent < list_indent:
            # A fence with no explicit closer ends when its list item ends.
            fence = None
            list_indent = 0
        if fence:
            closing = FENCE_LINE.fullmatch(expanded[list_indent:])
            if (closing and closing[1][0] == fence[0] and len(closing[1]) >= len(fence)
                    and not closing[2].strip(" ")):
                fence = None
            output.append(masked)
            continue

        if blank:
            paragraph = False
        elif list_indent and indent >= list_indent:
            content = expanded[list_indent:]
            if LIST_ITEM.fullmatch(content):
                nested_list = True
            if not nested_list:
                fence = opening_fence(content)
            paragraph = not fence
        elif indent >= 4:
            if not paragraph:
                output.append(masked)
                continue
        elif BLOCK_BOUNDARY.match(expanded) or (
            paragraph and not list_indent and SETEXT_UNDERLINE.fullmatch(expanded)
        ):
            list_indent = 0
            paragraph = False
        else:
            fence = opening_fence(expanded)
            item = LIST_ITEM.fullmatch(expanded)
            if fence:
                list_indent = 0
                paragraph = False
            elif item and (
                list_indent or not paragraph or
                (item[4] and (not item[2][0].isdigit() or item[2][:-1] == "1"))
            ):
                padding = len(item[3] or "")
                list_indent = len(item[1]) + len(item[2]) + (padding if item[4] and padding <= 4 else 1)
                nested_list = bool(item[4] and LIST_ITEM.fullmatch(item[4]))
                if item[4] and padding <= 4 and not nested_list:
                    fence = opening_fence(item[4])
                paragraph = bool(item[4]) and not fence
            else:
                # A dedented line can still continue an open list paragraph.
                if not paragraph or expanded.lstrip(" ").startswith(">"):
                    list_indent = 0
                paragraph = True
        output.append(masked if fence else line)
    return "".join(output)


def protected_stripped(text):
    """Blank supported protected surfaces before applying diagnostics."""
    text = blank_code_blocks(text)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"^>.*$", "", text, flags=re.M)
    text = re.sub(r"\([A-Z][^()]{0,80}\d{4}[a-z]?(; [^()]{0,80}\d{4}[a-z]?)*\)", "()", text)   # (Author, 2020; Other et al., 2021)
    text = re.sub(r"\[\d+(,\s*\d+)*\]", "", text)                                              # [3] or [3, 4]
    text = re.sub(r"https?://\S+", "", text)
    # wiki-links become their display text; headings and leading list emoji are labels, not prose
    text = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", text)
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    text = re.sub(r"^([ \t]*[-*] )[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2705\u274C\uFE0F]+[ \t]*", r"\1", text, flags=re.M)
    return text


def apply_allow(text, allow):
    for phrase in allow:
        if phrase:
            text = re.sub(re.escape(phrase), lambda m: "…" * 0 + " " * len(m.group(0)), text, flags=re.IGNORECASE)
    return text


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def structural(text, words):
    """Report exact duplicate prose paragraphs for contextual review."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    seen, duplicates = set(), set()
    for paragraph in paragraphs:
        if paragraph in seen and not paragraph.startswith(("#", "|", ">")):
            duplicates.add(paragraph)
        seen.add(paragraph)
    return [("repetition", "soft", "an exact paragraph appears more than once")
            for paragraph in sorted(duplicates)]


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    allow = list(DEFAULT_ALLOW)
    if "--allow" in argv:
        allow += [x.strip() for x in argv[argv.index("--allow") + 1].split(",")]
    quiet = "--quiet" in argv
    # the source is the first argument that is not an option or an option's value; options may come in any order
    positional = [a for i, a in enumerate(argv) if not a.startswith("--") and not (i > 0 and argv[i - 1] == "--allow")]
    if not positional:
        print("style_check: no draft given (a file path, or - for stdin)")
        return 2
    source = positional[0]
    raw = sys.stdin.read() if source == "-" else open(source, encoding="utf-8").read()

    text = apply_allow(protected_stripped(raw), allow)
    lines = text.splitlines()
    words = len(re.findall(r"\b\w+\b", text))
    hits = []
    for fam, sev, rx, hint in COMPILED:
        for i, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                frag = m.group(0).strip(" ,.")
                if not frag:
                    continue
                hits.append((i, fam, sev, frag, hint))
    hits.sort()
    struct = structural(text, words)

    hard = [h for h in hits if h[2] == "hard"]
    soft = [h for h in hits if h[2] == "soft"] + [(0, f, s, "", m) for f, s, m in struct if s == "soft"]
    soft_rate = len(soft) / max(words, 1) * 500
    allowed_soft = max(2, round(SOFT_LIMIT_PER_500_WORDS * words / 500))   # short texts get two soft hits
    failed = bool(hard) or len(soft) > allowed_soft

    if not quiet:
        for i, fam, sev, frag, hint in hits:
            print("line %d  [%s/%s]  %r: %s" % (i, fam, sev, frag, hint))
        for fam, sev, msg in struct:
            print("text    [%s/%s]  %s" % (fam, sev, msg))
        if hits or struct:
            print()
    by_family = {}
    for h in hits:
        by_family[h[1]] = by_family.get(h[1], 0) + 1
    for f, s, m in struct:
        by_family[f] = by_family.get(f, 0) + 1
    summary = ", ".join("%s %d" % (k, v) for k, v in sorted(by_family.items())) or "none"
    print("style check: %d words, %d hard, %d soft (allowed %d, %.1f per 500 words): %s -> %s" % (
        words, len(hard), len(soft), allowed_soft, soft_rate, summary, "FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
