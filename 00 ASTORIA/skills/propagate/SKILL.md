---
name: propagate
description: >-
  Carries one change through everything that depends on it. Two modes: a
  rename (a skill, note, folder, or map got a new name and every wiki-link,
  path string, frontmatter value, and instruction should follow) and a
  convention (a heading, label, field, or rule changed in one skill and its
  sibling skills, the maps, and the spec that defines the pattern should
  match). Finds every occurrence, separates what changes from protected history,
  reports first, edits on approval, verifies each edit. Hands
  drift it did not cause to the janitors. Triggers: propagate this rename, I
  renamed this, propagate this convention, make the family match, update every
  reference to.
metadata:
  level: skill
  system: Janitor System
  dependencies: ""
  created: "2026-09-24"
  updated: "2026-10-29"
---

# Propagate

A change in one place leaves stale copies everywhere else: links that point at an old name, path strings in skills, a heading that five sibling skills still spell the old way, a spec that still describes the shape from before. Propagate carries the change to every place that should follow and leaves alone every place that must not. It is the Janitor System's propagation tool; [skills-janitor](../skills-janitor/SKILL.md) and [vault-janitor](../vault-janitor/SKILL.md) find drift, propagate carries an intended change.

## Two modes

**Rename.** Something has a new name: a skill folder, a note, a MOC, a map, a folder path. Everything that referred to the old name should refer to the new one: wiki-links with and without aliases or headings, `dependencies` and other frontmatter values, path strings in skills and templates, examples and instructions that spell the old name, generated views. Run `./scripts/propagate_rename.py` for the search and the rewrite; read its report before applying.

**Convention.** A shape changed, not a name: a section heading, a label format, a frontmatter field's place, a workflow step, a rule two related skills must share. The change already lives in one or two files (the seed). Every sibling that carries the same pattern should follow, and so should the spec that defines it (skill-builder for skill shape, the project template's instruction comment for MOC shape, a system note or map when it describes the pattern). This mode is judgment work: read each candidate, change only what the convention touches, keep the file's own voice.

If the request mixes both (a rename that also changes a shared rule), do the rename first, then the convention, as two reports.

### Content moves for Folder Janitor

For an already chosen filing batch, use `./scripts/move_files.py` with a temporary JSON list of `{"source": "relative/path", "destination": "relative/path"}` entries, `--vault PATH`, and `--plan FILE`. Default execution is preflight; `--apply` executes within the existing request's authorization. Pass the configured `--system-root NAME` and every known `--hold PATH`.

This utility owns mechanical moves and supported reference repair, not classification. Active literal path tokens in instructions, MOCs, specifications, configuration and scripts also need repair; link-only success does not complete the batch. Use `--path-edits FILE` with an explicit reviewed path-edit map, selecting each active occurrence and preserving identical historical literals. Folder Janitor's Shared move tool section documents the `file`, character `start`, `old`, `new` and verified `base` fields. Do not pre-edit a consumer to a nonexistent destination outside the recoverable move operation. It preserves all bytes outside link/path tokens, including MOC prose, headings, decisions, labels and log narratives. Its result reports supported coverage, unchanged/updated references, holds, collisions, and required handoffs; do not claim broader coverage than it verifies. The excluded system root stays read-only, including through delegates. Keep an affected move outside the batch if it requires a repair there, while proceeding with independent supported items.

For the user's explicit structure/link/path cleanup, operational link and path targets in dated records may follow moved files while all surrounding narrative and historical provenance stay unchanged; this exception does not authorize historical rewriting or broaden ordinary convention/rename work. Return any owner-protected correction outside that scope. Do not add an AI-log or other system-root write as a side effect of Folder Janitor's excluded-root task. Folder Janitor supplies one brief concrete plan before very large moves or critical operational dependencies unless that same scope is already approved. Pass that approval through the move and all necessary path repairs; routine checks add no sign-offs. Broader logic or scientific changes require their technical owner and explicit expanded scope. The ordinary system-maintenance flow below retains its own scope.

## Inputs

- **The change.** Rename: old name and new name. Convention: before and after, in one line, plus the seed file where the new shape already lives. Ask only when this is not clear from the request or from the recent edits.
- **The family.** Rename: the whole active vault. Convention: the seed's `system` (or the part, for research skills) by default; say so before walking outside it.
- **Mode.** Report (default), or report then apply on approval. A request that says apply or update authorizes the named edits without a second approval.

## Steps

1. **Pin the change.** State it in one line: old to new, or before to after with the seed file. For a rename, run the script without `--apply` to get the full report; for a convention, list the family from the seed's `system` or part and open each member.
2. **Find every occurrence.** Rename: the script covers links, frontmatter, path strings, and prose mentions with whole-token matching. Convention: search the family and the maps for the old shape and the new shape, and compare the exact wording of siblings that share a destination, format, or handoff, not just their headings.
3. **Sort.** Three groups: to update (active notes, the renamed file's own frontmatter, maps and views, the spec); left alone (protected places, with the reason); needs judgment (an ambiguous match, a sibling whose wording differs on purpose, a rule two seeds disagree on). Anything that is drift rather than the requested change goes to a fourth list for the janitors.
4. **Report** before editing in the current task's requested form or under the recipient's existing reporting policy. Wait for approval unless the request already gave it.
5. **Apply.** Exact replacements only; aliases keep their display text; quoted YAML stays quoted. For a skill rename, rename the folder and the `name` field, then run `00 ASTORIA/skills/skills-janitor/scripts/build_views.py` so the Skill Map and the coordinator catalogs follow. For a convention, update the spec in the same pass; a pattern that does not reach its spec drifts back with the next new skill.
6. **Verify.** Re-read every edited file; run `lint.py` after any skill edit; run the links audit after any note rename. Report what landed, what stayed, and what the janitors should look at.

## Outputs

Report the change, paths to update and their changes, protected paths and reasons, items needing judgment with proposed answers, and unrelated drift for the janitors. Present these groups in the current task's requested form or under the recipient's existing reporting policy. The fenced layout is an example.

```
Propagate (rename): old-name -> new-name        or        Propagate (convention): <pattern>, before -> after

Update (N files):
- path: what changes (link, path string, frontmatter, heading, label)
Left alone (M files):
- path: reason (history, capture log, backup, archive)
Needs judgment:
- path: the ambiguity and the proposed answer
Drift for the janitors (not part of this change):
- path: what looks stale
```

- Only for an actual authorized system-maintenance change within this role's logging scope, add one entry at the top of the existing `00 ASTORIA/agent_notes/ai_log.md` under its callout. Use three to six lines with the date and skill in the heading and record what was done, where and what is pending. Folder Janitor delegations and excluded-root work do not create this entry.

## Boundaries

Propagate edits the active vault and leaves the record alone:

- `00 ASTORIA/agent_notes/`, dated capture logs in `02 📅 Calendar/`, and the Research Log section of a project MOC (below its log heading): history, not instructions.
- Recipient-selected protected folders and recovery copies, `06 🪴 Archive/`, and `.obsidian/`: outside the requested change. Resolve protected paths from current instructions and add verified vault-relative prefixes to `PROTECTED_PREFIXES` for write protection. These prefixes prevent rewrites but do not prevent reads for reference reporting. Do not use this script for a scan that would read a prohibited location.

Old names inside those places are reported as "left alone" with the reason, never rewritten, unless the user asks for that historical correction by name.

Rules:

- **Report first.** The list precedes the edit unless the request authorized it.
- **Whole tokens.** `MOC` never matches `MOCs`; an ambiguous match is a question, not an edit.
- **Search past the links.** Triggers, examples, filenames, and plain instructions carry old names and old shapes too; a rename is not done while active instructions still say the old thing.
- **One change per pass.** Drift found on the way is reported, not fixed here.
- **The spec is part of the family.** Skill-shape conventions live in skill-builder; MOC shape in the project template; a rule two skills share belongs in both and in the contract list of skills-janitor.
- **Keep each file's voice.** Change what the convention touches and nothing around it.
- **Protected places stay protected.** See above.
- **Check reporting follows the requested deliverable and recipient's reporting policy.** Creating a separate report requires authorization.

Edge cases:

- **The renamed file's own frontmatter is stale.** The `name` field follows the folder; fix it in the same pass.
- **A note rename inside a project folder.** Links above the MOC's log heading update; entries below it are history and stay.
- **Two seeds disagree** on the new shape. Stop and ask which one is intended before walking the family.
- **The pattern has no spec.** Report it; the user may want a line in skill-builder or the template to lock it in.
- **The family is partly updated already.** The updated members are the seed; bring the rest forward.
- **A cross-vault reference** (another vault or a workspace outside this one). Out of scope; report it.
- **A scheduled automation prompt names the old thing.** Report it; update it on approval like any other active instruction.
