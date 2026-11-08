---
name: folder-janitor
description: >-
  Organizes the requested content folders outside the AI system root using the
  owner’s verified structure and approved placements. Each Project or Area
  has one owning MOC and one AGENTS.md. Use a local files folder or a documented
  external workspace. Resources keeps its chosen organization. Repairs links
  and active path references in instructions, MOCs and code without rewriting
  substantive content; preserves scientific layouts and leaves unclear files
  in configured intake. Presents one brief plan for approval before large moves
  or critical operational changes unless that concrete scope is already approved.
  Use for bounded folder or attachment cleanup, including a returnable detour
  from another session. Triggers: organize this folder, sort my resource intake,
  tidy my area folders, file these attachments.
metadata:
  level: skill
  system: Janitor System
  dependencies: propagate, vault-builder, bridge-maker
  created: "2026-10-29"
  updated: "2026-10-29"
---

# Folder Janitor

Keep selected folders organized, preserve their content, and keep path dependencies working.

## Purpose

Own routine content filing and folder tidying across the user's selected
organizational folders, outside the AI system root. Follow the owner's actual
names and useful existing structure. Keep navigation through MOCs and links,
with working content in its Project or Area and reusable references in Resources. Follow the recipient's verified placement policy and approved destinations.

- Sort a named intake, attachments, or selected folder.
- Check and repair Project and Area folder structure in the requested scope.
- Bring scattered supporting material together under its established owner.
- Identify unnecessary folder layers or duplicate navigation scaffolding.
- Accept a structural detour and return the resulting paths to the invoking session.

Examples illustrate decisions, not required names. The owner may change these
defaults or edit or remove this skill.

## Inputs

Use the current request and existing context before asking anything.

- Requested folder and action: review/propose, or organize/fix.
- Current `AGENTS.md`, root `me.md`, existing layout reference, and relevant
  project instructions. Resolve root roles from the current configuration.
- Actual files, declared content locations, course/offering identity, incoming
  links and active path references, and enough document context to establish ownership.
- Configured intake and attachment destination, explicit holds, active writers,
  scientific layouts, retention rules, and write exclusions.
- Invoking session and return point, if this is a handoff.

Ask only when no scope can be identified or a consequential filing choice
remains unresolved. Do not require a new setup interview, research question,
course record, companion session, native mount, or attachment plugin.

## Steps

1. **Resolve roles and scope.** Treat the AI system root, including a renamed
   equivalent of `00 ASTORIA`, as read-only. Read its layout/instructions as
   needed; do not reorganize it or add notes there. Keep Inbox, Calendar,
   Projects, Areas, Resources, and Archive roles distinct where they exist.
   Do not create missing role roots simply to match an example.

2. **Inventory the requested batch.** Identify files, MOCs, collections, and
   complete operational packages. Read selected content only as far as needed
   for filing. Search both links and literal path dependencies, including in
   `AGENTS.md`, MOCs, specifications, frontmatter, configuration and scripts.
   A mechanical dependency search may extend outside the selected folder
   within the permitted workspace; it does not expand write authorization.
   Do not read unrelated personal material for semantic classification.

3. **Choose one supported home.** Prefer the owner's explicit destination,
   then an established project/course/lab collection, then purpose supported
   by content and links. Several backlinks do not establish several copies or
   ownership by the most-linked project. Reuse existing collections, keep
   related notes and supporting files together, and preserve filenames,
   meaningful variants, package relationships, and useful depth.

4. **Apply the Project and Area rule.** The owner root holds its one existing
   MOC, one `AGENTS.md`, and one `files/` folder (or the configured equivalent).
   File other owned working notes and coherent subfolders inside that existing
   folder. Verify the owning Area MOC using the single direct `astoria_role: area_moc`
   note, or the verified exact `<Area> MOC.md` when no marker or conflict exists.
   Distinguish it from project, course, lab, and topic maps. Report missing or
   competing MOCs and preserve their contents and properties.
   A documented external working folder in the owner's AGENTS.md or MOC
   satisfies the files requirement. Verify that it is the working destination.
   If it is offline, report workspace availability separately. Preserve its
   layout and keep the vault hub lean.
   Report other missing or competing entries as well. Offer creation when useful and wait
   for a request before creating any of the three; Bridge Maker handles a
   requested missing bridge. Retain established operational layouts under
   the owner's project instructions. Resources uses flexible topic folders.
   Leave its structure alone in ordinary cleanup except for requested
   attachment organization or reference repairs.

5. **Account for uncertainty and holds.** Leave unclear items in configured
   intake when that is in scope. Without a configured intake, retain their
   current location and report the unresolved group. Do not invent `00_to_sort`
   because an example uses it. Keep held or actively written packages in place
   and continue independent clear items.

6. **Prepare a finite move and dependency map.** List sources, destinations,
   affected reference files and exact path-token repairs. Classify literal
   matches using the active-path rules below. Before adding a folder, say what
   belongs there and why no existing collection suffices. Create it for a
   distinct present purpose or demonstrated browsing need. Avoid empty
   taxonomies, per-file folders, new MOCs, parallel indexes, and permanent
   classification registries. Read matching cases in ./references/examples.md
   when judgment is needed.

7. **Use one checkpoint when warranted.** A review remains read-only. Routine,
   bounded filing proceeds under a clear cleanup request. For a very large
   move or critical operational dependency, prepare the concrete plan below
   and pause that batch for approval unless the same plan is already approved.
   Preflight and verification are internal checks, not further sign-offs.

8. **Apply the complete authorized operation.** For a move the owner already
   made, verify old and new identities and repair references in place. For a
   pending move, move files and repair active
   links and literal path tokens together, using Propagate's shared tool and
   reviewed path edits below. Exclude uncertain, colliding, held, or unsupported
   operations from the executable batch; keep an affected item in place if
   its necessary repair cannot be completed within scope. Follow the owner's
   existing backup and retention rules; never overwrite to resolve a collision.

9. **Verify and return.** Check every moved file, incoming dependency and
   rebased outbound path, plus the content-preservation conditions below.
   Search for the old path forms again and account for every remaining hit.
   Stop when the requested batch is organized, unclear items are accounted
   for, and active dependencies resolve. Report deferred batches, unrun checks and other findings in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization and its appropriate owner. Return changed paths, remaining issues,
   and the return point without taking over scientific, teaching or study work.

### Active path dependencies

A link-only repair is incomplete when an instruction or program still names the
old location. Update exact active path tokens wherever the authorized move
requires them: `AGENTS.md` workspace/MOC pointers, MOC file locations and runnable
commands, specifications, frontmatter, manifests, configuration, and script
input/output paths. Plain prose, inline code and fenced commands can all hold
active paths. Determine the consuming program's path base; relative paths in
code are not necessarily relative to the script or note. Moving a referring
file can require rebasing its outgoing paths even when its target stays put.

Classify each hit as an active dependency to repair, an intentionally historical
source/provenance/example to preserve, or unresolved. Identical old strings can
have different roles in the same file. Record the exact occurrence selected;
never globally replace names or treat every fenced path as either active or
historical. Ambiguous dependencies keep the affected move pending. An excluded
system-root or external-workspace dependency needs its own authorized owner;
do not move the affected item and leave that dependency stale.

These edits remain structure work when only the path token changes. Preserve
surrounding prose, MOC sections/headings/decisions, script logic, scientific
parameters and data. If a move needs logic, schema, environment or scientific
changes, explain that expansion in the plan and hand it to the relevant
technical owner after approval. Do not disguise it as routine filing.

### One checkpoint for consequential moves

Assess breadth and consequence, not a fixed file-count cutoff. A broad
reorganization spanning collections or project/Area owners, a wide dependency
cascade, or changes to operational scripts, pipeline configuration, loaders or
other critical infrastructure warrant the checkpoint. Critical dependencies
can make even a small move consequential. A
routine exact MOC or `AGENTS.md` pointer repair alone does not make a small
filing operation critical.

Before mutation, give one brief plan with the moved groups and counts,
source/destination structure, affected instruction/configuration/script files,
path-only versus any broader edits, holds/exclusions, and verification/recovery
approach. Ask once whether to proceed. Existing approval of that concrete scope
carries through moves, dependency repairs and checks, including coordinator
handoffs. Do not ask again for dry runs, individual files or final verification.
Pause again only for a materially new consequence or expanded scope; explain
that specific difference instead of restarting the approval sequence.

### Shared move tool

[propagate](../propagate/SKILL.md) owns
`scripts/move_files.py`. It executes a chosen move map; it does not choose a
taxonomy. Use a temporary JSON plan outside the vault:

```json
[
  {"source": "Incoming/paper.pdf", "destination": "Library/methods/paper.pdf"}
]
```

Resolve the actual system-root name. From the vault root:

```sh
python3 "00 ASTORIA/skills/propagate/scripts/move_files.py" \
  --vault "/path/to/vault" --plan "/temporary/path/moves.json" \
  --system-root "00 ASTORIA"
```

For reviewed active literals, also pass `--path-edits /temporary/path/paths.json`.
Each entry selects one path occurrence in the original document; for a document
beginning `Input: Incoming/paper.pdf`, the path starts at character 7:

```json
[
  {"file": "AGENTS.md", "start": 7, "old": "Incoming/paper.pdf",
   "new": "Library/methods/paper.pdf", "base": "vault"}
]
```

Derive `start` from the current decoded UTF-8 text, not from this example or a
byte count. `base: "vault"` means the documented launch root is the vault;
`base: "document"` means the referring file's directory, rebased when moved.
Choose only a verified base. Other working directories or computed paths need
a supported repair method; leave the affected move pending when unresolved.
The tool validates that the replacement still identifies the same target under
the move map, refuses stale/overlapping spans, and includes these edits in its
recovery and concurrency checks. It does not decide which literals are active.
Select active occurrences and preserve identical historical ones. This map
supports literal, unescaped POSIX paths. Escaped strings, file URIs in code,
computed paths or changes requiring language-specific quoting need another
verified repair method. The conservative code/configuration scan can also
block a move when an unselected old path remains in a historical comment;
report that limitation and defer the affected move rather than changing history
or bypassing the scan. Ordinary link URIs retain the tool's existing coverage.

Default execution is preflight. Add `--apply` when the existing request
authorizes the moves, and pass each known hold through `--hold`. The utility
uses Python 3's standard library; keep the vault's YAML configuration unchanged.
The utility uses exclusive hard-link file moves; unsupported or cross-device
filesystems stop with recovery originals retained and an explicit result.

Read its coverage and unsupported-reference findings. Automatic link discovery
excludes inline code and fences; that does not exempt active paths there from
repair. Review those occurrences and supply explicit path edits with the moves.
Keep historical examples and quoted provenance unchanged. Binary-embedded or
other unsupported dependencies need a verified repair method before the affected
move can proceed. If a repair requires writing inside the excluded system root,
return that affected item for separately scoped maintenance and file independent
supported items.
Without execution tools, report the finite plan and unrun checks rather than
claiming files moved.

## Outputs

- Organized content and necessary folder/link/path changes within scope.
- A result in the requested reporting form: filed, unclear, held, references checked, and unresolved ownership or maintenance items.
- No substantive MOC rewrites, new summaries, automatic schedules or permanent classification records. A separate report artifact is not a filing side effect; its creation belongs to an appropriate owner under separately authorized scope and the same write exclusions.
- No automatic AI-log, layout, skill, export, or other system-root writes.

## Boundaries

- **Structure, links and path tokens only.** Preserve all surrounding MOC
  prose, headings, section order, scientific claims, decisions, annotations and
  log narratives. Active file-path tokens may change even inside prose or code.
  Preserve visible link labels and historical source paths. A move does not
  authorize summarizing, improving the note or changing script behavior beyond
  resolving the same intended files at their new locations.
- **Preserve role differences.** Follow the owner's human-Inbox rules.
  Calendar records retain chronology and identity. Projects and Areas use the owner-root rule above, with
  established operational layouts preserved. Resources holds reusable information and follows its own organization. Archives retain finished identity and preservation rules.
- **Avoid cosmetic uniformity.** Keep coherent structures, including deep
  packages. Keep useful nesting inside the working folder and avoid imposing
  unrelated numbering, emoji, chronology, or extension categories.
- **Preserve useful differences.** Keep distinct scientific variants and
  provenance. Missing backlinks do not establish that a file is unused.
  Filing does not authorize deletion, deduplication, reactivation, or moving
  protected data.
- **Carry scope through handoffs.** Preserve review-only/simulation status,
  write exclusions, holds, and return ownership. Do not bypass the read-only
  system root through a delegate or start background monitoring or messaging.

## Handoffs

| Need | Owner and boundary |
| --- | --- |
| Routine content filing | Folder Janitor chooses destinations for the requested batch. |
| Supported moves and reference repair | [propagate](../propagate/SKILL.md) supplies the shared tool; preserve write exclusions. |
| Layout-reference maintenance | [vault-builder](../vault-builder/SKILL.md) owns it; report needed changes when the system root is excluded. |
| Missing/broken project or Area bridge | [bridge-maker](../bridge-maker/SKILL.md) owns requested bridge creation or instruction repairs; Folder Janitor updates existing path pointers only. Carry exclusions and never generate MOC content. |
| System or skill consistency | [vault-janitor](../vault-janitor/SKILL.md) or [skills-janitor](../skills-janitor/SKILL.md) owns that separate task. |
| Research, study, or teaching work | Return changed paths and remaining structural issues to the invoking owner. |

The handoff carries selected folders, chosen structure, action authorization,
approved move/dependency plan, write exclusions, holds, ambiguity, and return point. A recipient must respect
that same scope; report an incompatible side effect instead of invoking it.

This is system maintenance, not a scientific inquiry part. Verify availability
when invoked. If the owner removed the skill, return the capability gap without
recreating it or blocking unrelated work.

## Checks

- Scope and exclusions match the executed batch.
- Each Project or Area in scope has one owning MOC, one `AGENTS.md`, and
  a local working-files folder, documented external workspace, or established
  operational layout under the applicable verified convention. Report genuine gaps separately from unavailable drives.
  Resources has no three-entry check.
- Files have supported homes and preserved content and package relationships.
- Links and active path dependencies in instructions, MOCs, specifications,
  configuration and scripts resolve to the same intended files after the move.
  Distinguish pre-existing unresolved references from new failures.
- Re-scan old absolute, relative and encoded path forms, including literal code
  paths; classify remaining history/examples rather than reporting them fixed.
- For approved script/configuration path edits, run appropriate syntax/config
  checks and inspect target resolution without launching analyses or workloads.
  Report any unrun check or unresolved path base.
- Diff edited files: only selected link/path tokens changed; MOC headings,
  surrounding prose, scientific settings, script logic and historical provenance
  remain unchanged. Recovery covers the move and its dependency repairs together.
- Excluded system-root and held-package content is unchanged.
- Unclear items follow the owner's configured intake policy.
- Report tool coverage, deferred repairs, and unrun checks accurately.
