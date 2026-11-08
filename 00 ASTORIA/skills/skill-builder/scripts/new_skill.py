#!/usr/bin/env python3
"""new_skill.py: scaffold one skill folder from the template and check it before it exists.

Usage:
  python3 new_skill.py NAME --level skill --system "Janitor System" \
      --description "What it owns. When to use it." --triggers "phrase one; phrase two" \
      [--part 4 --family method-guide --modality any --population general] \
      [--dependencies "a, b" --requires "..." --gates "..."] [--vault PATH] [--apply]

Dry run by default: prints the frontmatter and the trigger-overlap check.
--apply writes 00 ASTORIA/skills/NAME/SKILL.md from assets/SKILL_template.md.
"""
import os, re, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "skills-janitor", "scripts"))
import skillkit as sk


def arg(argv, key, default=""):
    for i, a in enumerate(argv):
        if a == key and i + 1 < len(argv):
            return argv[i + 1]
    return default


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__); return 2
    name = argv[0]
    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    skills = sk.load_skills(vault)
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
        print("name must be lowercase letters, digits, single hyphens, 64 max"); return 1
    if name in skills:
        print("a skill named %s already exists" % name); return 1
    level = arg(argv, "--level", "skill")
    system = arg(argv, "--system")
    if level not in vocab["levels"] or system not in vocab["systems"]:
        print("level or system not in vocabulary.md"); return 1
    desc = " ".join(arg(argv, "--description").split())
    triggers = [t.strip() for t in arg(argv, "--triggers").split(";") if t.strip()]
    lo, hi = vocab["trigger_counts"][level]
    if not (lo <= len(triggers) <= hi):
        print("level %s takes %d to %d triggers" % (level, lo, hi)); return 1
    full = desc + (" Triggers: %s." % ", ".join(triggers) if triggers else "")
    if len(full) > int(vocab["description_max_chars"]):
        print("description with triggers is %d characters (max %s)" % (len(full), vocab["description_max_chars"])); return 1
    today = datetime.date.today().isoformat()
    meta = {"level": level, "system": system}
    if system == "Research Assistant System" and level in ("skill", "coordinator"):
        for k in ("part", "family", "modality", "population"):
            meta[k] = arg(argv, "--" + k)
    for k in ("dependencies", "requires", "gates"):
        v = arg(argv, "--" + k)
        if v or k == "dependencies":
            meta[k] = v
    meta["created"], meta["updated"] = today, today
    # overlap check against every existing skill
    problems = []
    for t in triggers:
        tl = t.lower()
        if tl in (name, name.replace("-", " ")):
            problems.append("trigger %r is the skill's own name" % t)
        for other in skills.values():
            for o in other.triggers:
                ol = o.lower()
                if tl == ol or tl in ol or ol in tl:
                    problems.append("trigger %r overlaps %r in %s" % (t, o, other.name))
    fm = sk.dump_frontmatter(name, full, meta)
    print(fm)
    if problems:
        print("OVERLAPS:\n  " + "\n  ".join(problems)); return 1
    if "--apply" not in argv:
        print("dry run; add --apply to write the folder"); return 0
    tpl = open(os.path.join(HERE, "..", "assets", "SKILL_template.md"), encoding="utf-8").read()
    body = tpl.split("---\n", 2)[2]
    body = body.replace("# Skill Name", "# " + name.replace("-", " ").title())
    folder = os.path.join(vault, sk.SKILLS_REL, name)
    os.makedirs(folder, exist_ok=False)
    open(os.path.join(folder, "SKILL.md"), "w", encoding="utf-8").write(fm + body)
    print("wrote %s/SKILL.md; now fill the body and run skills-janitor/scripts/build_views.py" % folder)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
