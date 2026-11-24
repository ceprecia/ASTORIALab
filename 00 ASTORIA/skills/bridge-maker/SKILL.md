---
name: bridge-maker
description: >-
  Creates or updates a short project AGENTS.md pointing to the vault-root me.md.
  Keeps project-specific instructions and verifies existing pointers. Triggers:
  make a project bridge, connect this project to obsidian, audit the project
  bridges, update this project AGENTS.md.
metadata:
  level: skill
  system: Janitor System
  dependencies: ""
  created: "2026-05-20"
  updated: "2026-11-22"
---

# Bridge Maker

A bridge points to the vault's single standing briefing, `me.md`. A project
bridge can also point to its verified owning MOC and carry rules specific to that
project. Keep inherited guidance in the briefing or the skill that owns it.

1. Identify the requested project and the open vault. Read the vault-root
   `me.md` completely and inspect the existing `AGENTS.md`. If the briefing
   cannot be read, report the problem before accessing or changing other user
   files.
2. For an audit, verify the pointer and task-relevant project paths. Report
   findings in the requested form. A missing bridge, stale pointer, or stray
   instruction file is a finding. An audit makes no edits or log entries.
3. For an authorized write, verify the destination and patch only the relevant
   content. Preserve supplied project-specific rules and scientific controls.
   Keep the owning MOC pointer when verified and useful for the task. A missing
   MOC does not require a new note. Resolve paths to vault files from that same root.
4. Re-read the edited file. Confirm the briefing pointer, any changed MOC
   pointer, and the preservation of project-specific rules. Report the change
   briefly.

## Pipeline bridges

Point the bridge to **Pipeline layout** in the vault-root `me.md`. Check that
project exceptions name the exact stage and outputs they cover. For an audit
of a configured pipeline, verify the output destination from the script or
selected configuration against the shared rule and any applicable exception.
Report conflicts before the pipeline is run.

## In-vault bridge

```markdown
# [Project name]

Read `me.md` at the root of the open vault completely and follow it as the
user's standing instructions. If it cannot be read, report that before
accessing or changing other user files.

For pipeline work, follow **Pipeline layout** in the vault-root `me.md`.

Project MOC: `[verified vault-relative MOC path]`.
```

Include the MOC line when applicable. Add necessary project-specific rules only.
For an external workspace use the marked fragment in
`00 ASTORIA/templates/global_codex_agents_template.md`. The vault-root loader
uses `00 ASTORIA/templates/agents_loader_template.md`.

Bridge Maker writes only the requested `AGENTS.md`. Keep the briefing, notes,
layouts, registrations, and reports in their existing workflows.
