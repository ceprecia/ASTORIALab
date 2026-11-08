---
name: bridge-maker
description: >-
  Creates or updates only the requested project AGENTS.md, pointing to the user's
  single authoritative vault-root me.md and keeping necessary supplied project
  instructions. Returns requested read-only bridge audits in the recipient's chosen reporting form without creating notes,
  profiles, registries, or other startup files, and never creates CLAUDE.md,
  codex.md, or any other agent instruction file. Preserves existing approved
  rules and optional research routing when patching. Triggers: make a project
  bridge, connect this project to obsidian, audit the project bridges, update
  this project AGENTS.md.
metadata:
  level: skill
  system: Janitor System
  dependencies: ""
  created: "2026-05-20"
  updated: "2026-11-04"
---

# Bridge Maker

Connect a project to the user's standing instructions through its existing or
requested `AGENTS.md`. The default is a short pointer to the single
authoritative vault-root `me.md`, plus necessary project instructions the user
supplies. A bridge is not a new context system.

This skill has two outputs:

- A requested project `AGENTS.md` creation or update.
- A requested read-only bridge audit in the recipient's chosen reporting form.

Bridge Maker's file writes are limited to the requested `AGENTS.md`. It does not create or update project notes, profiles, loaders, registry files or maps, and never creates, copies or edits a `me.md`. Any separate report artifact remains with its original owner under that owner's separately authorized scope.
Existing source or template copies are not live standing instructions and are
not deleted merely because a bridge is being repaired.

## Purpose

Use for a requested project bridge, a project-local `AGENTS.md`, or a check of
its standing-context pointer after a folder move. Existing natural-language
triggers such as "add external workspace" start this bounded bridge task;
they do not authorize an automatic layout entry or companion note.

## Steps

### 1. Locate the requested project and standing context

- Read the single standing briefing completely:
  `me.md`.
  If it cannot be read, report the problem before accessing or changing
  the user's files.
- Resolve the exact project folder from the user's request and verified current
  paths. Read the existing project `AGENTS.md` before changing it.
- Read `00 ASTORIA/templates/global_codex_agents_template.md` for the direct
  standing-context instruction used by external workspaces. The vault-root
  `AGENTS.md` uses `00 ASTORIA/templates/agents_loader_template.md`.
- Consult the Working Locations section of `me.md` read-only when its known workspace paths help locate
  the target. An index row, project note, workflow classification, or
  separate contract mode is not a prerequisite for a valid bridge.
- Check applicable ancestor instructions when needed for the target.
  A nested project contract does not erase inherited standing instructions.
- Ask only when the target or a consequential edit choice remains unresolved.
  Do not repeat an intake when the user has already supplied the information.

### 2. Audit or prepare the smallest corresponding change

For an audit, verify the project folder, direct root-me pointer, and any
existing task-relevant paths. Report broken or stale references separately
from historical examples. Missing storage is an unavailable resource, not
proof that its files are corrupt.

A short project `AGENTS.md` pointing to current root `me.md` is healthy.
It does not need a project note, a layout row, a direct Skill Map pointer,
a workflow-type field, or a research-routing fragment. A known workspace
without an `AGENTS.md` is an unconfigured bridge, not an instruction to
create one unless the request includes that action.

For a requested creation, include the MOC and continuity policy paragraph
below in each new project bridge. Add only the project-specific instructions needed for the
user's stated task. Do not invent
scientific settings, safety rules, approval gates, a project history,
or a copied list of skills.

For a requested update:

- Patch the relevant content rather than replacing the whole contract.
- Preserve existing approved project rules, scientific controls,
  task-relevant pointers, and optional research fragments unless the user asks
  to change them.
- Keep project notes, maps and profiles out of required startup reads. Add or
  repair a continuity pointer only when the requested scope covers it and the
  selected or configured location is verified. Update MOC writing instructions
  only when the requested change covers them. The central `me.md` supplies skill
  discovery.
- Existing optional research routing may remain. Copy it from the template
  only when the user explicitly requests that routing; do not add it merely
  because a workspace contains research.
- A missing optional context note does not block unrelated project work.
  Use a verified replacement when the request authorizes that repair, or
  report the missing reference without inventing a new note.

### 3. Write only the requested AGENTS.md

A clear create or update request authorizes that specific edit. Do not add
another approval round. Verify the destination, then create or patch only
the requested project's `AGENTS.md`.

Resolve the absolute path to this vault's authoritative `me.md` before filling the pattern. Substitute that verified path in every external bridge; do not leave the placeholder or a project-relative `me.md`. The project heading may use the supplied name:

```markdown
# [Project name]

Before work that depends on the user's preferences, files, or projects, read
`[verified absolute path to this vault's me.md]`
completely and follow it as the user's standing instructions.

If that file cannot be read, report the problem before accessing or changing
The user's files. Before creating or moving a file, verify its destination against
`me.md` and applicable project instructions.

Follow the MOC conventions in `me.md`. Save project memory and technical
context only when authorized, at the verified location selected for the task
or established by the applicable project continuity policy. When that
location is AI Notes, use its verified heading. Edit other MOC sections only
when the user explicitly requests that change.

Project MOC: `[verified vault-relative MOC path]`.
Continuity: `[verified vault-relative path and exact heading, when applicable]`.
Read relevant entries only when the task needs continuity or technical details.
```

Include the MOC and continuity policy paragraph in each new bridge. For an
external workspace, use the paragraph in the marked global fragment once.

Include an owning MOC pointer when relevant and verified. Add a separate
continuity pointer only when the requested bridge scope includes it and the
recipient or applicable project policy identifies its location. Verify each
vault-relative path against actual entries, including spelling and case.
When the location is a section, use the exact rendered heading, including
AI Notes when selected. Ignore headings inside examples and comments. If a
target is missing, unreadable or ambiguous, report the unresolved pointer,
omit it from a new bridge and preserve existing instructions on an update.
Read technical paths and environments only as needed from their verified
continuity location.

Append necessary project-specific instructions only when supplied or already
approved. Do not append empty sections or a standard project-context scaffold.

Keep the vault-root `AGENTS.md` as the vault's own loader, using
`00 ASTORIA/templates/agents_loader_template.md` as its source. The marked
global fragment is for external workspaces. Optional project instructions
never belong in the vault-root file. A project bridge request changes only
its named `AGENTS.md`.

Other requested file changes belong to their owning workflow. They are not
automatic side effects of Bridge Maker.

### 4. Verify and report

- Re-read the edited file and confirm the direct root-me path resolves.
- Check that the requested change landed and existing approved project
  instructions remain intact. For a new bridge, check that the MOC writing
  default appears once and that any MOC path resolves.
- Verify any path actually changed; do not scan a project or the vault
  recursively just to complete a bridge.
- Confirm that any Bridge Maker file changes are limited to the requested `AGENTS.md` and that it created no duplicate standing profile, loader, note or index entry. A separate report artifact belongs to its original owner under that owner's authorized scope.
- For an audit, report only. For an edit, briefly state the file changed
  and any remaining path-specific limitation.

## Boundaries

Rules:

- There is one authoritative root `me.md`. Reference it directly;
  never copy its contents into a project or create another briefing.
- Do not edit `me.md` to resolve a project-level conflict. Surface the
  conflict and keep project-specific decisions in the requested
  `AGENTS.md` without inventing instructions.
- Resolve startup from the verified workspace path and its existing authorized
  instructions. Preserve relevant project-specific environments in their project scope.
- Do not create project context notes or update the layout reference, Skill Map,
  system notes, application settings, or external-workspace registrations as
  part of a bridge request.
- Preserve source files, project data, completed projects, historical
  captures, and backups. A path repair is not authority to move or delete them.
- Use the recipient's requested reporting form for audits and completion summaries. The bridge task authorizes only the named `AGENTS.md` changes; creating any separate report file requires explicit authorization and its owning workflow.
- `AGENTS.md` is the only instruction file. Never create `CLAUDE.md`,
  `CLAUDE.local.md`, `.claude/CLAUDE.md`, `.claude/rules/`, `codex.md`,
  `AGENTS.override.md`, or `AGENTS.local.md` (the vault root's
  `.claude/skills/` and `.agents/skills/` symlink shims are skill-mount's
  and are not bridge files). On Claude Code versions with AGENTS support enabled,
  the default reads `AGENTS.md` when neither `CLAUDE.md` nor `CLAUDE.local.md`
  exists in the working directory or above it; settings and versions can change
  this behavior. Verify the actual session, or ask the assistant to read the
  file explicitly. Do not create extra instruction files as a workaround.
  A bridge audit lists any such file in or above the workspace as drift. Route separately approved stray-file removal to its authorized owner. Bridge Maker writes only the requested `AGENTS.md`.
- Keep each `AGENTS.md` self-sufficient and short. A project contract must point directly to the user's authoritative `me.md` rather than assuming the vault-root instruction file will be loaded.
- Do not automatically load companions, Coordinator, or any other skill
  merely because the project exists.

Edge cases:

- **Unavailable drive or folder:** Report the exact gap and continue unrelated
  work. Never invent a replacement location or recreate the project.
- **Finished project:** Preserve its Finished status and historical
  instructions. Do not revive it or register it as active during a bridge audit.
- **Existing approved research fragment:** Preserve it during a pointer-only
  repair. Absence of that fragment is not a bridge failure.
- **Stale optional note link:** Repair only the authorized reference using
  an existing verified target; do not create a note to satisfy the old scaffold.
- **Conflicting local rules:** Preserve unrelated instructions and ask only
  if the requested edit cannot be completed without a consequential
  unresolved replacement decision.

- Return read-only audit findings in the requested form. After an actual authorized `AGENTS.md` edit, report the verified change and any pending item to the existing log owner. Bridge Maker writes only the requested `AGENTS.md`.

## References

- OpenAI. (n.d.). *Custom instructions with AGENTS.md*. https://learn.chatgpt.com/docs/agent-configuration/agents-md

- Anthropic. (n.d.). *How Claude remembers your project: AGENTS.md*. https://code.claude.com/docs/en/memory#agents-md
