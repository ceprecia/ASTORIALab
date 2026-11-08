---
name: skills-janitor
description: >-
  Audits every skill folder in `00 ASTORIA/skills/` against the skill-builder
  schema and regenerates the views. Runs the lint (name equals folder, allowed
  frontmatter, description length, trigger count, self-name and overlap
  checks, vocabulary, dependencies, links, line counts, stray instruction
  files), compares related-skill contracts, and searches active instructions
  for stale wording. Reports findings before changes and fixes only within authorization; skill
  files are the source of truth and the Skill Map is rebuilt from them, never
  the other way. Triggers: audit my skills, are my skills in sync, rebuild the
  skill map, check for trigger overlaps, skill drift.
metadata:
  level: skill
  system: Janitor System
  dependencies: skill-builder, propagate
  created: "2026-04-11"
  updated: "2026-11-02"
---

# Skills Janitor

Scan the skill folders. Lint them against the schema, rebuild the generated views, compare sibling contracts, search for stale wording. Report drift. Fix on approval.

The skill folders in `00 ASTORIA/skills/` are the source of truth. The Skill Map registry and the part-coordinator catalogs are generated from them by `./scripts/build_views.py`, never edited by hand. The schema, the description recipe, the trigger policy, and the vocabulary belong to [skill-builder](../skill-builder/SKILL.md).

## Purpose

- After creating, renaming, deleting, or consolidating skills, or after [propagate](../propagate/SKILL.md) carried a rename or a convention change.
- After changing a convention shared by several skills.
- When the Skill Map or a coordinator catalog looks stale, or when a phrase routes to the wrong skill.
- As periodic hygiene.

## Inputs

- **Scope**: vault-wide by default; the user can narrow to one system or one part.
- **Mode**: *report* (default) or *report, then fix on approval*.

## Steps

### 1. Lint

Run `python3 ./scripts/lint.py` (add `--vault PATH` when not inside the vault). It is read-only and reports:

- folders without `SKILL.md`, single-file skills left in the skills root, frontmatter that does not parse;
- `name` not equal to the folder, folder names outside the standard, frontmatter keys outside `name`, `description`, `license`, `compatibility`, `allowed-tools`, `metadata`;
- empty descriptions, descriptions over 1,000 characters, more than one `Triggers:` sentence;
- `metadata` values outside `00 ASTORIA/skills/skill-builder/assets/vocabulary.md` (level, system, part, family, modality, population), dates not `YYYY-MM-DD`, dependencies that are not skills;
- trigger counts outside the level's range, a skill's own name used as a trigger, and every exact or containment overlap between two skills' phrases, reported as a pair with both owners;
- unresolved `[[...]]` links and `./references/...` links in SKILL.md, references folders nested deeper than one level, SKILL.md over 500 lines (warning);
- level-1 skills missing from the Skill Map registry, part skills missing from their coordinator catalog, map links to skills that no longer exist;
- stray agent instruction files anywhere in the vault (`CLAUDE.md`, `CLAUDE.local.md`, `codex.md`, `AGENTS.override.md`, `AGENTS.local.md`, `GEMINI.md`) and anything inside `.claude/` other than the `skills` shim.

Without a shell, do the same checks by reading: open each `SKILL.md` frontmatter, the vocabulary, the Skill Map registry, and the five coordinator catalogs, and compare.

### 2. Views

Run `python3 ./scripts/build_views.py --check` to see whether the Skill Map registry or any coordinator catalog is stale. Rebuilding is a safe fix (step 6), because the views carry nothing that is not in the frontmatter.

### 3. Trigger quality

Beyond the mechanical overlap check, read the phrases of any two skills that share a domain (both companions, a coordinator and its part skills, the capture helpers) and judge whether a natural request could reach the wrong one. Generic intent belongs to the companion or coordinator; specific intent to the specialized skill. Propose the narrower phrase for the specialized skill.

### 4. Stale wording

Search active instructions for the pattern families in `./references/contracts_and_patterns.md` plus the terms of the current change request. Use targeted searches (`rg -n`), not memory. Classify hits as the reference explains before calling anything drift.

### 5. Related-skill contracts

Compare the contracts listed in `./references/contracts_and_patterns.md`. Flag disagreement as contract drift even when every link resolves.

### 6. Report

Present the report in the requested deliverable or form; save a separate report only within the recipient's authorization:

```
# Skills Janitor Report YYYY-MM-DD

Skills: N (companions C, coordinators R, skills S, profiles P)

## Lint errors
- skill-name: message
## Lint warnings
- skill-name: message
## Stale views
- Skill Map registry / coordinator name (or "none")
## Trigger quality
- skill-a / skill-b: phrase X could reach the wrong skill; proposed narrower phrase
## Stale wording
- file: line: hit and classification
## Contract drift
- skills involved: what disagrees
## Health
one line: "in sync" or "N issues across M skills"
```

Wait for approval before changing anything.

### 7. Fix on approval

Safe fixes: rebuild the views with `./scripts/build_views.py`; remove stray instruction files that the user confirms; fix `updated` dates and vocabulary spelling drift when the intended value is obvious; narrow a trigger phrase when the user picks the wording.

Surface but do not auto-fix: `name` versus folder mismatches (a rename goes through propagate); descriptions over the limit (rewriting needs the user's voice); empty descriptions; contract disagreements where the intended convention is unclear (use [propagate](../propagate/SKILL.md) after the user chooses); any change to a skill body.

## Scripts beyond the audit

- `./scripts/install_specialized.py`: on a starter vault, lists the groups in `00 ASTORIA/specialized_skills/`, plans an installation from the chosen groups (modality coordinators and declared dependencies pulled in), moves the chosen folders into `00 ASTORIA/skills/`, rebuilds the views, lints, and removes the catalog folder. Links from installed skills to skills left in the repository are reported by the lint as "not installed", not as errors; the names live in the vocabulary's `starter.catalog_index`.
- `./scripts/rename_roots.py`: renames root folders (`--no-emoji`, `--no-numbers`, `--set role=name`, `--drop role`) and cascades every path string in `00 ASTORIA/`, `me.md`, `AGENTS.md`, the Obsidian settings, and the Base files, then updates the vocabulary `roots`. The lint flags any numbered root path that is not in `roots`.

## Outputs

Report in the form requested by the recipient or specified in their reporting policy. Saving a separate report requires authorization. The fix step writes only what the approved list names.

- If an approved fix changes the system and logging it falls within the protected-zone exception below, add one entry at the top of the existing `00 ASTORIA/agent_notes/ai_log.md` under its callout. Use three to six lines with the date and skill in the heading and record what was done, where and what is pending.

## Boundaries

Rules:

- **Skill folders are the source of truth.** Never edit a skill to make a view happy; rebuild the view.
- **Read first, write second.** The report always precedes any change.
- **Do not fix what needs judgment.** Renames and convention changes go through propagate; wording goes back to the user.
- **Be specific.** Name the skill, the field, the phrase, the line.
- **Protected zones stay untouched.** Dated capture logs and existing content in `00 ASTORIA/agent_notes/` are never edited by the janitor. The sole exception is adding the single entry described in Outputs after an approved fix changes the system and logging is within scope. Preserve earlier entries and other agent notes.
- **Check reporting follows the requested deliverable and recipient's reporting policy.** Creating a separate report requires authorization.
- **The catalog is uninstalled reference material.** `00 ASTORIA/specialized_skills/` ships with the starter and may remain after manual core setup so existing links work. Lint checks it separately from active skills. When scripted installation or removal is selected, `install_specialized.py --remove-catalog` repairs links and deletes the shelf after successful checks.

Edge cases:

- **Two folders with the same `name` field.** Hard conflict; one must rename through propagate.
- **A phrase is claimed by a companion and a specialized skill.** The companion keeps the generic phrase; propose the narrower one for the skill.
- **A coordinator catalog lists a skill whose part changed.** Rebuild the views; the catalog follows the frontmatter.
- **A description cannot fit 1,000 characters with its triggers.** Move capability prose into `## Purpose` in the body and keep the triggers; report it for the user to word.
