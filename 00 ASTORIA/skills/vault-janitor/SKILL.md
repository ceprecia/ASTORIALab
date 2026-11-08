---
name: vault-janitor
description: >-
  Checks vault consistency: the layout reference against the folder tree and
  vocabulary, rules against me.md, active instructions for stale paths and
  wording, and wiki-links vault-wide. Preserves complete AI-log history and
  checks selective reading instead of reducing logs by entry count. Invokes
  installed folder-janitor for relevant filing findings within the requested
  scope and hands layout rebuilds to vault-builder. Triggers: audit the layout,
  are my folders and templates in sync, check for folder drift, check log
  preservation, clean up the agent notes.
metadata:
  level: skill
  system: Janitor System
  dependencies: vault-builder
  created: "2026-09-24"
  updated: "2026-11-02"
---

# Vault Janitor

Diff the layout reference against disk and the vocabulary, the rules against `me.md`, the active instructions against the retired-pattern list, and the log-preservation and selective-reading guidance. Report drift. Fix on approval.

Routine content filing and Area-folder tidying belong to [folder-janitor](../folder-janitor/SKILL.md) when it is installed. This skill audits consistency; it does not choose content destinations. If that optional capability was removed, report the gap without recreating it.

The folder tree decides what exists; the vocabulary and `me.md` decide what things are for and how notes are made. The layout reference is reconciled to them, never the other way. Vault-janitor pairs with [vault-builder](../vault-builder/SKILL.md): the builder writes the page, the janitor checks it and preserves useful history without loading it all into each session.

## Purpose

- After folders, templates, projects, or areas changed, or after note-creation rules in `me.md` changed.
- After vault-builder ran, to confirm the page matches disk.
- At the end of setup, called by [setup-my-vault](../setup-my-vault/SKILL.md) with fixes authorized for what the build produced.
- When log preservation or selective history retrieval needs checking, or as periodic hygiene.

## Inputs

- **Scope**: everything by default; the user can narrow to the layout, the instructions, the links, or the agent notes.
- **Mode**: report (default), or report then fix on approval. A request that says fix, update, or clean up authorizes the named unambiguous repairs without a second approval.

## Steps

Read `./references/checks.md` for the check lists and the search patterns. Resolve the recipient’s read exclusions before running an audit command or inspecting a collection. A hold on moving or editing files still permits authorized reading.

1. **Layout.** `build_layout.py` can read direct Project and Area note frontmatter and selected MOC bodies. If a read exclusion covers any input the generator may read and the command cannot honor it, skip the freshness check and report the affected scope as uninspected. Continue with checks that can honor the exclusion. When the generator’s read scope is allowed, run `python3 "00 ASTORIA/skills/vault-builder/scripts/build_layout.py" --check`. Exit 1 means the layout is missing or differs from a complete fresh build. Exit 2 means inaccessible project or area folders blocked the freshness check. Report the incomplete inspection and affected paths. The report also names folders and templates with no purpose line and note types with missing owners or templates. Also verify every path in the page's folder table exists and every root the vocabulary names is on disk.
2. **Rules.** Compare the page's Rules block (`layout_rules` in the vocabulary) with `me.md`: a rule the page states that `me.md` no longer states is drift; a placement rule `me.md` states that the page omits is drift.
3. **Active instructions.** Search `00 ASTORIA/skills/`, `00 ASTORIA/systems/`, `00 ASTORIA/Skill Map.md`, `me.md`, and `AGENTS.md` for retired paths, stale patterns, footers, missing security lines, and stray instruction files, using the patterns in the reference plus the terms of the current change. Classify hits before calling them drift: a pattern inside a janitor list, a report template, or an example is an instruction, not drift.
4. **Links.** Run `python3 ./scripts/links_audit.py` with the applicable read exclusions (add `--vault PATH` outside the vault). It lists unresolved wiki-links by target and file. Supply each recipient-designated read exclusion with repeatable `--exclude PATH` arguments; the audit prunes those paths, dotfolders and runtime caches before reading notes.
5. **Agent notes.** Check that AI-log guidance preserves every existing entry and directs readers to use headings, dates or keywords to locate relevant entries and read them in bounded chunks. Entry/file counts and dates are informational, not condensation or archiving thresholds.
6. **Folder filing when needed.** When the requested scope includes content placement, attachment intake or Project or Area structure, inspect the relevant folder entries for misplaced content or deviations from the verified owner layout. The default Project or Area root has one owning MOC, one AGENTS.md and one working files folder. Treat documented external workspaces and established operational layouts as valid working locations. Report unavailable external locations separately from missing entries. Resources has no entry-count rule. For a concrete filing finding, verify and load [folder-janitor](../folder-janitor/SKILL.md) completely and invoke it once for that bounded batch. A layout/schema issue alone does not invoke it. Pass the same read exclusions and the applicable handoff below. Invoke the skill directly when the existing request already covers that work.
7. **Report** in the requested form using the content below and the recipient's reporting policy. Wait for approval before changing anything, unless the request already authorized the fix.
8. **Fix on approval.**
   - Layout: hand approved repairs to Vault Builder with the same read exclusions. Keep the generated page unchanged if rebuilding cannot honor them.
   - Rules: update `layout_rules` in the vocabulary to match `me.md` when authorized. Rebuild only within the generator’s allowed read scope. Report rules missing from `me.md` for the recipient.
   - Instructions: correct a retired path when the current path is unambiguous; remove a footer; add a missing security section or loader paragraph from its template; report a stray instruction file, never create one. Drift that spans several files goes to [propagate](../propagate/SKILL.md) or [skills-janitor](../skills-janitor/SKILL.md).
   - Log reading: repair active guidance or templates that order count-based condensation. Keep every existing log entry verbatim. Working-context summaries never replace the originals.
   - Dated notes: move files only under an explicit user-selected archive scope, keeping their names and repairing links. Age or file count alone does not authorize a move.

### Folder Janitor handoff

- **Report, audit, simulation or explicit read-only request:** invoke Folder Janitor in the same review-only mode. It returns findings and a finite proposed filing map; no files move and no MOC content is edited.
- **Authorized fix, tidy or cleanup request:** invoke it for the already authorized, unambiguous filing operations. Carry the selected folder scope, owner-chosen structure and intake, approved move/dependency plan when present, write exclusions, holds, scientific-layout exceptions, and return owner. Folder Janitor assesses active path dependencies as well as links and uses its one brief approval checkpoint for very large moves or critical operational changes not already covered by the concrete approval. Do not add another approval round for the same approved scope.
- **Missing or deliberately removed skill:** report that bounded capability gap and continue the remaining Vault Janitor audit. Do not recreate it or treat it as a mandatory dependency.
- **Return:** receive filed/proposed, unclear, held and reference-check results, then finish the current Vault Janitor report once. Do not invoke either janitor recursively or restart a full-vault audit. The child keeps the AI system root read-only and MOC headings, decisions, history and surrounding prose unchanged while repairing authorized active path tokens; any separate system-maintenance issue returns to its existing owner within that owner's authorization.

## Outputs

```
# Vault Janitor Report YYYY-MM-DD

## Layout
- in sync, missing or different after complete inspection, or inspection incomplete with the affected paths. List relevant report lines.
## Rules
- page says X, me.md says Y (or none)
## Active instruction drift
- file:line: hit, classification
## Stray instruction files, footers, security lines
- none, or each path found
## Links
- N unresolved across M files (targets listed)
## Folder filing
- not needed, or: delegated scope/mode and filed or proposed / unclear / held / reference results
## Agent notes
- ai_log.md: N preserved entries; selective-reading guidance in sync or named drift; dated notes: M files (informational)
## Health
one line: "in sync" or "N issues"
```

## Boundaries

- **Preserve handoff scope.** An audit cannot become a cleanup through delegation. Folder Janitor performs only the bounded requested work and returns once; no new permission, system-root write or MOC-content edit is implied.
- **Disk is the source of truth for existence; the vocabulary and `me.md` for meaning.** Never delete or move a folder or template to make the page right.
- **Read first, write second.** The report precedes any change unless the request authorized the fix.
- **Never edit `layout.md` by hand.** The builder rebuilds it.
- **Protected zones.** Never edit dated capture logs. Dated transcripts and summaries in `agent_notes/` are moved, never rewritten.
- **Preserve history.** Never replace, condense, truncate or delete log entries because of file size, age or count. Locate relevant entries by heading, date or keyword and read them in bounded chunks. Summarize only in the working context.
- **Be specific.** Name the folder, the row, the file, the line.
- **Check reporting follows the requested deliverable and recipient's reporting policy.** Creating a separate report requires authorization. Add one three-to-six-line entry at the top of the existing `ai_log.md` only after an actual authorized change within this role's logging scope. Read-only and unchanged runs leave the log untouched.
- **No phantom links.** Never introduce a link to a note that does not exist.
- **Dotfolders are out of scope**, except that `.claude/` and `.agents/` may hold only the `skills` shim folder.
- **Odd cases.** No `layout.md`: hand to vault-builder. Folders mid-move (both paths exist): report both and wait. A folder starting with an underscore: user scratch, report only.
