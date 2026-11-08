---
name: vault-builder
description: >-
  Builds or refreshes the layout reference `00 ASTORIA/agent_notes/layout.md`,
  the one page an agent checks before placing, naming, or moving a file. Runs
  `scripts/build_layout.py`, which writes the folder table, the file-kind
  table, the template table, the rules block, and the active projects table
  from the vocabulary and the folder tree; resolves what the build reports
  (a folder or template with no purpose line, a note type whose owner is
  missing) by updating the vocabulary, never the page. Triggers: build my
  layout reference, refresh the layout, map my folders for AI, map my
  templates for AI.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: ""
  created: "2026-09-24"
  updated: "2026-10-27"
---

# Vault Builder

The layout reference is normally generated. Its inputs are the folder tree (what exists) and four lists in the YAML vocabulary at `00 ASTORIA/skills/skill-builder/assets/vocabulary.md` (what each thing is for): `purposes` (one line per folder), `note_types` (kind, location and name pattern, template, owner skill), `template_purposes`, and `layout_rules` (the hard rules, restating `me.md`). The active projects table needs no list; it comes from the MOCs on disk. Vault Builder can inspect the layout in a dry run or update it within an authorized write scope. The manual first-setup exception below provides the same reference when Python, PyYAML, or script execution is unavailable.

## Purpose

- During setup of a fresh vault, called by [setup-my-vault](../setup-my-vault/SKILL.md) after the root folders exist.
- After folders, templates, projects, or areas were added, renamed, or removed.
- When [vault-janitor](../vault-janitor/SKILL.md) reports that the page on disk differs from a fresh build.

A new project or renamed folder appears in the table after an authorized layout build. Use a dry run for inspection.

## Steps

Use these scripted steps when Python 3 and PyYAML are available in the same interpreter. During manual first setup without either dependency or script execution, use the exception below instead; do not install a runtime or package automatically.

1. **Dry run.** `python3 "00 ASTORIA/skills/vault-builder/scripts/build_layout.py"` (add `--vault PATH` from outside the vault). Read the findings. For inspection or review, report them using the requested form, then the verified applicable recipient or project reporting policy if the form is open. If neither specifies a form, return them in the current session. Leave the vocabulary, layout and AI log untouched during inspection.
2. **Resolve the findings within the authorized vocabulary scope.** Make only the changes the request authorizes.
   - *Folder on disk with no purpose line*: read the folder's MOC or its first note only as far as needed to say in one line what belongs there and who writes there, then add the line under `purposes`. Keep the user's wording when a line exists elsewhere (an older map, a MOC callout). A folder starting with an underscore is user scratch; leave it out and say so.
   - *Template with no purpose line*: read the template's frontmatter and first lines; add one line under `template_purposes`, or "purpose unclear, please describe" when it is not obvious.
   - *Note type skipped, owner not installed*: leave the row; it returns when the skill is installed. Say so in the report.
   - *Note type names a missing template*: fix the row or ask which template is meant.
   - *Vocabulary subfolder missing on disk*: create it only during setup; otherwise report it.
   - *Root missing on disk*: report it; never create a root outside setup.
3. **Build.** Run the script again with `--apply` only when the request authorizes writing the layout. After complete folder inspection, the script writes `00 ASTORIA/agent_notes/layout.md` if it is missing or its content differs after ignoring generator dates. Exit 2 means folder inspection was incomplete and the existing layout is preserved. Report the affected paths and the pending refresh. Include unresolved findings after step 2 in the requested report.
4. **Verify.** Every owner skill named on the page is installed (the script only prints installed ones); every path in the folder table exists; the page has the five sections.
5. **Report the build.** Use the current requested form, then the verified applicable recipient or project reporting policy. If neither specifies a form, return the findings in the current session. Include folders and templates counted, purpose lines added, note types skipped and unresolved items. Add one entry at the top of `00 ASTORIA/agent_notes/ai_log.md` only for an authorized maintenance run that changed the layout or vocabulary. Record the date, changes and pending items. During first setup, return these facts to Setup My Vault for its initial entry. A separate report file requires authorization.

## Manual first-setup exception

When setup-my-vault is building a fresh participant vault without Python, PyYAML, or script execution, write the existing `00 ASTORIA/agent_notes/layout.md` manually from the default folder tree, the YAML vocabulary read as text, installed skill folders, and the participant's `me.md`. Use the normal five sections: `## Folders`, `## Files`, `## Templates`, `## Rules`, and `## Active projects and areas`. Reuse the vocabulary's purposes and naming rules. Include only paths and owner skills verified on disk. For each project folder, use its single direct note with the explicit `astoria_role: project_moc` property. With no explicit role, use its verified `MOC <project>.md` or a lone familiar MOC filename. Report ambiguity and omit the project row when multiple explicit roles or unresolved legacy candidates remain. For each Area folder, use its single direct note with `astoria_role: area_moc`, or its verified exact `<Area> MOC.md` when no marker or conflict exists. Report and omit the row for missing or competing Area maps. An empty projects/areas list remains empty.

This exception creates the same owning reference, not another map or setup report. Preserve the shipped generated Skill Map and coordinator catalogs while the core skill set and paths remain unchanged. Re-read the layout and verify its paths manually. Return the manual setup facts and unrun scripted checks to Setup My Vault for its single initial AI-log entry. Describe the page as manually built and report lint, generator checks and mounts as unrun. If Python and PyYAML become available later, the normal vocabulary-driven build can regenerate this same file. Native mounts are optional and are never a prerequisite for this layout or a usable vault.

## Boundaries

- **Disk decides existence; the vocabulary decides meaning.** Never invent a folder, template, or path, and never write a purpose line the folder's contents do not support.
- **Generated layouts are not hand-edited.** A wanted change goes into the vocabulary and the page is rebuilt; hand edits are lost on the next build by design. The narrow exception is manual first setup without script execution, as described above.
- **Rules come from `me.md`.** `layout_rules` restate the rules an agent needs before placing a file; a rule that `me.md` no longer states comes out, and a new rule goes into `me.md` first.
- **Projects and areas are not annotated.** Their folders appear in the active projects table with the MOC and the newest dated entry; no purpose lines for them.
- **No phantom links.** The page carries paths and skill names in code spans, not wiki-links, except the frontmatter `related` link to the Skill Map.
- **Reporting policy:** Follow the task's requested reporting form, then the verified applicable recipient or project policy. Return counts and questions in the current session if both leave the form open. Keep the authorized operational log entry to three to six lines. A separate report file requires its own authorized scope.
