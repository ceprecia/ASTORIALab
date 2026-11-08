# Registry platform adapters (skill-mount)

Read this reference only when mounting into a registry platform.

For scan platforms, `wire_shims.py` reports proposed links for review. This reference covers registry platforms, where native discovery uses the platform's registration interface.

## What stays portable and what does not

Portable, and where the work belongs:

1. The choice of what to expose, which is the `--set` logic in `wire_shims.py`.
2. The manifest: `name`, `description`, `vault_root`, `skill_md_relative`, `skill_md`. No platform's format appears in it.
3. The pointer stub shape below, which holds no procedure.
4. The rule that the vault keeps the single copy of every procedure.

Platform-specific, and confined to one adapter section each:

1. The API or the screen that registers an entry.
2. The catalog location and its per-entry stamp file, declared in the `REGISTRY_PLATFORMS` table in `wire_shims.py`.
3. That registry's validation rules.

Keep a platform's API inside its own section. On a machine without that platform nothing outside the section needs editing, and `wire_shims.py` reports it as not installed and carries on with the rest.

## Setup and targeted refresh

Register only when native discovery is requested for the selected platform and environment. Verify whether its current registration is scoped to a project, machine, account, organization, or another boundary. Procedure-body edits need no copied procedure or registration refresh, because the pointer reads the canonical file. Refresh the affected entry when its exposed name or discovery description changes; reconcile additions and removals within the requested set.

Moving a vault can leave a pointer's absolute path stale. Review ownership explicitly before refreshing or retiring it. The same relative skill path can occur in several vaults, so it is a location hint rather than proof of registration ownership. Treat any local pointer match as a lead for review through the platform's own list and the user's context.

## The pointer stub

One registered entry per exposed skill. Frontmatter carries the manifest's `name` and `description` unchanged, apart from repairs a specific registry demands. The body routes and nothing more.

```
---
name: {name}
description: {description}
---

# {name} (ASTORIA vault skill)

This entry exists so the skill can be chosen from this platform's skill picker. It carries
no procedure of its own. The authoritative version is the vault file named below and is the
only copy; do not reconstruct the procedure from this stub or from memory.

## How to run this skill

1. Read this file completely and follow it: `{skill_md}`
2. If that path does not exist, the vault may have moved. The durable location is
   `{skill_md_relative}` inside the intended vault. Confirm which vault owns this pointer
   before locating it there; the relative path alone does not establish ownership.
3. If the path exists but cannot be read, the vault folder has not been granted to this
   session. Request access to `{vault_root}` and then read the file.
4. Check `requires` and `gates` in its frontmatter before running anything.
5. Read its `references/`, `scripts/`, or `assets/` files only when it routes you there.
6. Follow the vault's standing instructions in order: the vault-root `AGENTS.md`, then
   `me.md`, then the project `AGENTS.md` when the task is inside a project folder. `me.md`
   is the default and a project `AGENTS.md` supersedes it inside that project.
```

## Adapter: Claude Science

Catalog `~/.claude-science/orgs/{org}/skills/`, stamp `.catalog_stamp`. The catalog is a read-only local copy. Verify registration in the selected account through the platform's own interface. For local inspection, give the actual catalog path or a fixed-depth wildcard pattern. Symlinked path components are skipped.

The adapter below records one platform interface observed when this guide was written. Verify its current API, settings, and account scope before use. Registration may use a platform tool or a manual skill-settings screen; follow the authorization shown for each action. Approval for one action does not by itself approve later writes.

1. Run `python3 ../scripts/wire_shims.py --emit-manifest` and slice the JSON off the end of the output with `sed -n '/^\[/,$p'`. The report lists locally vacant names, occupied entries, linked candidates and local pointer leads for platform verification. The manifest lists the selected set for review.
2. Verify the name and vacancy or ownership in the selected account through the platform. Preserve occupied or uncertain entries. Treat local paths and stamps as verification leads. Use a separately authorized platform action for removal or retirement only after verifying the exact entry, its owner and the supported deletion behavior. Editing through a `SKILL.md` symlink could change the canonical vault file.
3. Two validation rules, both on the description. Angle-bracket placeholders are read as XML tags and rejected, so write them in braces. And frontmatter must hold literal text, so build it with `json.dumps(value, ensure_ascii=False)`; the default turns the emoji in a vault folder name into a `\uXXXX` escape, which is rejected.
4. For an authorized new registration, confirm the exact slot is vacant, then call `host.skills.edit(name, "SKILL.md", stub)` and `host.skills.publish(name)`. A refresh requires verified ownership and authorization for that entry. Keep unresolved slots out of the registration queue.
5. Confirm the authorized registrations with `host.skills.list()` and check for origin `personal`. Report unresolved or occupied names. That call is also the report to use when the catalog folder is unreadable from the shell, which is the normal case inside a sandboxed session.

Before a registration or refresh, state the visibility scope established by the current platform and the requested account or project. Follow its actual consent requirements and the user's existing authorization. Do not assume that one registration is account-wide, that one approval covers later writes, or that every environment presents the same approval interface.

## Adding a platform

1. If the platform discovers skills by scanning a folder, add a row to `SCAN_PLATFORMS` in `wire_shims.py` so the script can include that location in the link plan.
2. Otherwise add a row to `REGISTRY_PLATFORMS` with its catalog glob and stamp file, or an empty glob when it keeps no local copy, and write an adapter section here beside the Claude Science one.
3. Keep the stub shape above as it stands. Only the registration calls and the validation rules should differ between adapters.
