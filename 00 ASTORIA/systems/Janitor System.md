---
related:
  - "[[ASTORIA System Builder]]"
  - "[[Productivity and Study System]]"
  - "[[Research Assistant System]]"
created: 2026-01-01
updated: 2026-11-02
---

# Janitor System

![Janitor System](../assets/banner_system_janitor.png)

The Janitor System maintains system consistency and keeps requested content folders aligned with the owner's chosen organization.

It has three jobs:

- Propagate intentional changes, such as renames or convention changes.
- Audit drift, such as stale map entries, deleted skill links, old template references, and broken workspace paths.
- Organize requested content folders and repair links and active paths while preserving substantive MOC content and the owner's useful structure.

Janitors check both structure and meaning. A file can be present, linked, and valid while still carrying stale workflow instructions. The job is not done until active instructions agree with the current system behavior.

## Skills

Content filing has its own bounded owner:

- [folder-janitor](../skills/folder-janitor/SKILL.md) organizes selected folders outside the AI system root. The default Project or Area root has one owning MOC and one AGENTS.md. Working content goes in a local files folder or a documented external workspace. Honor the recipient's established operational layout and report genuine missing entries separately from offline workspaces. Resources collections keep their own organization. It repairs active path tokens in AGENTS.md, MOCs, specifications, configuration and scripts as well as links, while preserving surrounding prose, headings, decisions and historical provenance. Very large moves or critical operational dependencies receive one brief concrete plan for approval unless already approved; checks and repairs then complete within that scope. It returns to an invoking session after a structural detour. Its detailed examples are fictional illustrations rather than mandatory categories.

Each builder in the [ASTORIA System Builder](ASTORIA%20System%20Builder.md) has its janitor:

- [vault-janitor](../skills/vault-janitor/SKILL.md) checks the layout reference against a fresh build from disk and the vocabulary, its rules against `me.md`, the active instructions for retired paths and footers, the links vault-wide, and log-preservation/selective-reading guidance (the full history stays on disk; newest entries and relevant older chunks supply current context). Pairs with vault-builder. It conditionally invokes installed Folder Janitor for concrete filing findings: audits preserve review-only mode, authorized cleanup carries its existing scope, and the child returns once to the current audit.
- [skills-janitor](../skills/skills-janitor/SKILL.md) lints every skill folder against the skill-builder schema (`lint.py`), regenerates the Skill Map registry and the coordinator catalogs (`build_views.py`), compares related-skill contracts, and searches active instructions for stale wording. Its scripts also install specialized skills from the catalog and rename root folders with a cascade; repository release preparation is a separate task with its own authorized sources and destination. Pairs with skill-builder.

The propagation skill:

- [propagate](../skills/propagate/SKILL.md) carries one intended change through everything that depends on it: a rename (every link, path string, frontmatter value, and instruction follows, with `scripts/propagate_rename.py`) or a convention (sibling skills, the maps, and the spec that defines the pattern follow). It leaves history, capture logs, backups, and the archive alone, and hands drift it did not cause to the janitors.
- [bridge-maker](../skills/bridge-maker/SKILL.md) audits, creates, or repairs only the requested `AGENTS.md`, pointing at the one vault-root `me.md` and preserving approved project instructions. It creates no other files and writes no maps.

## Rules

- Report first, then edit only after the user approves the specific fix. A request that says fix or update authorizes the named unambiguous repairs without a second approval.
- Run structural checks and targeted pattern searches. Do not rely only on map registration, file existence, or frontmatter validity.
- Search active instructions for stale workflow terms after any rename, deletion, or convention change. Exclude protected dated capture logs unless the user explicitly asks to correct history.
- Check related skills as a contract family. If two skills touch the same destination, file format, path authority, or workflow handoff, compare their exact instructions.
- Surface semantic drift separately from structural drift.
- Never delete project data, raw data, scripts, derivatives, backups, or capture logs as a janitor cleanup. Never rewrite dated capture logs unless the user asks for that exact historical correction.
- Do not recreate purged systems because an old reference appears somewhere.
- Follow the current owner's placement rules and existing layout. Put owned working content in the Project or Area files folder or documented external workspace. Resources holds reusable information and stays outside routine cleanup except for requested attachment organization and reference repairs. MOCs provide navigation. Configured attachment intake is temporary and separate from agent scratch or build storage; system work has its own owner. `01 📥 Inbox/` is the user's human inbox: never an AI destination, read only when the user asks to process it. Compare vault-root output and staging folders with the owner's verified placement rules. Report undeclared locations as drift. Report other undeclared staging folders without filing or deleting their contents.
- Finished projects are not broken active workspaces. Do not recreate active registrations for them.
- Treat project MOC Research Log entries and `02 📅 Calendar/capture-logs/` records as protected progress history.
- Verify the current workspace and its paths directly against the request and existing configuration. Use the established loader and applicable project instructions.
- `AGENTS.md` is the only agent instruction file. A `CLAUDE.md`, `CLAUDE.local.md`, `.claude/CLAUDE.md`, `.claude/rules/`, `codex.md`, or `AGENTS.override.md` anywhere in the vault or a workspace is drift to report, never something a janitor or builder creates. The `.agents/skills/` and `.claude/skills/` shim folders written by skill-mount are the one exception.
- The vault-root `AGENTS.md` is the loader written from `00 ASTORIA/templates/agents_loader_template.md`; external workspaces get the marked global fragment from `00 ASTORIA/templates/global_codex_agents_template.md`. Project-local `AGENTS.md` files stay short: the central `me.md` pointer and the project's own instructions.
- Folder tidying changes structure, links and active path tokens only: preserve all substantive MOC content and script logic. Link repair alone is incomplete when instructions or code still use the old location. The AI system root is read-only for that skill and its delegates; any required system maintenance is returned to the existing owner as a separate scope. User-chosen names and examples never become a mandatory private taxonomy.
- Report checks in the requested deliverable or according to the recipient's reporting policy. A separate saved report requires authorization.

## When to use

- When the user requests filing, intake sorting, or Area-folder tidying, use Folder Janitor directly; a research or course session is not a prerequisite.
- After deleting, renaming, or consolidating skills.
- After moving folders, changing templates, or changing note-creation rules.
- After moving drives, sync locations, or external project folders.
- After changing a convention shared by several skills.
- At the end of setup, when setup-my-vault calls both janitors with fixes authorized for what the build produced.
- When the user asks whether the vault is drifting.

## Examples

- "Sort my resource intake" or "tidy my area folders" uses folder-janitor with the current scope, holds and return owner. It files content, repairs references, and preserves MOC text.
- "Audit my skills" runs skills-janitor and reports lint errors, stale generated views, trigger overlaps, and frontmatter drift.
- "Audit the vault map" runs vault-janitor and compares the folder tree, the templates, the workspaces, and the links with the map.
- "Audit bridges" runs bridge-maker to check requested `AGENTS.md` files and their central `me.md` pointers.

