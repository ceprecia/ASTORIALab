---
name: skill-mount
description: >-
  Optionally mounts the vault's skills where an agent platform looks for them, keeping one
  copy in `00 ASTORIA/skills`. A platform that scans a folder gets relative
  symlinks and no copy, which covers Codex and Claude Code. A platform that keeps
  a registry gets a one-time registration of pointer stubs that only route back to
  the vault file, which covers Claude Science. Both platform sets are tables in the
  script, and each registry platform has one short adapter in
  references/registry_adapters.md, so a machine without it needs no edit. Exposes
  every level-1 skill by default, preserves existing scan mounts, and reports a local
  listing-size preference.
  Use when native discovery is requested, including a requested refresh after
  changing skills, discovery descriptions, or machines. Triggers: mount my skills,
  remount the skills, make my skills show up in Codex, register my skills for
  Claude Science.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: skills-janitor
  created: "2026-09-23"
  updated: "2026-10-29"
---

# Skill Mount

An optional convenience for native skill discovery in Codex, Claude Code, and Claude Science, without moving or copying anything out of `00 ASTORIA/skills/`. Run it only when the user requests that convenience; skills existing on disk or a new vault setup do not require a mount.

## Purpose

The `AGENTS.md` path (read `me.md`, the map group, one `SKILL.md`) needs no mounts and works with an agent that can read the vault files. Mounting adds the discovery, skill selector, explicit invocation, and description matching supported by the selected platform. Check its current documentation and interface rather than assuming every platform exposes the same commands.

Core vault setup finishes before this optional work. Absent, declined, or failed mounts never invalidate a finished setup, require it to rerun, or block direct use of the skills. Do not install runtimes or packages automatically to make an optional mount possible.

Platforms discover skills in one of two ways, and the two need opposite treatment. Which platforms exist is a table in the script, not a fact baked into this skill: `SCAN_PLATFORMS` and `REGISTRY_PLATFORMS` in `./scripts/wire_shims.py`.

- A **scan platform** reads a skill folder. The supplied table uses `.agents/skills/` for Codex and `.claude/skills/` for Claude Code. The script reports proposed relative links and checks the selected destinations for conflicts. Verify the platform's current locations, symlink support, and discovery scope. `AGENTS.md` stays the instruction entry point.
- A **registry platform** maintains its own skill catalog. Use its supported registration interface; placing a folder in a local catalog is not proof of registration. The supplied Claude Science adapter records one implementation and must be checked against the current platform before use.
- A registry platform gets a **pointer stub**: a registered entry carrying the skill's `name` and `description`, with a body that routes to `00 ASTORIA/skills/{name}/SKILL.md` and contains no procedure. Procedure-body edits need no new copy. Adding, renaming, or removing a skill, changing its discovery description, or moving the vault requires the relevant registration refresh.
- Registration is optional setup for the requested account and environment. Its current API, validation, visibility, and consent requirements belong in `./references/registry_adapters.md`. Follow the platform's actual rules and the user's existing authorization; do not invent another approval flow. An absent or unreadable registry is reported without blocking unrelated scan mounts or direct skill use.
- `BUDGET = 8000` in `wire_shims.py` is a configurable **local listing-size preference**, not a universal platform limit. The script estimates the selected listing size for comparison. Choose `all` or `core` according to the user's preferred discovery scope; neither a larger listing nor an unchanged budget makes core vault setup incomplete. Verify current platform constraints separately.

## Steps

1. Run `python3 ./scripts/wire_shims.py` to preview planned links, conflicts, the local listing estimate, and registry evidence.
2. Choose `all` (default) or `--set core` for a smaller set of requested mounts. Existing mounts stay in place. Add `--scan-only` to skip registry reporting, or `--catalog-glob PATTERN` when the requested registry is elsewhere.
3. If native discovery is requested, review the exact source and destination paths in the report. Use a supported manual or host mount method in the requested scope. Recheck the path and confirm that the slot is vacant before creating each relative link. Preserve usable, occupied, obsolete, and unselected entries. Verify ownership before any separately authorized cleanup. The helper only reports a plan and rejects `--apply`.
4. Use the Registry platforms section for separately authorized platform work. Verify that the selected registry slot is vacant before registering, and preserve occupied or uncertain entries.
5. Verify discovery through each selected platform's current skill interface and test that one natural phrase reaches the intended skill. Use the user's platform confirmation when its interface is unavailable here; report unverified discovery explicitly.
6. Report the set used, links written per platform, platform-confirmed registrations or removals, listing size and anything unresolved in the current task's requested form or under the recipient's existing reporting policy. Save a separate report only when authorized.

## New machine or new account

When mounting is requested on a new machine, preview the local mounts and refresh only the requested, available registry integrations. Otherwise use the direct `AGENTS.md` route. ASTORIA adds no separate mount ledger: scan links and the platform's own registry show the current state. Existing valid mounts are idempotent; conflicts are reported without replacing foreign material.

A moved vault can leave registrations pointing to its previous absolute path. A shared vault-relative path does not establish which vault owns an entry. Explicitly review ownership before changing or removing those pointers, then refresh the confirmed entries when requested. The relative path helps locate the intended skill after that review; it does not authorize modifying another vault's registration.

## Registry platforms

Read `./references/registry_adapters.md` only when a requested registry platform needs registration or refresh. It holds the manifest fields, pointer stub, refresh rules, and platform adapter. Registration uses the platform's supported interface and current consent requirements.

Run `wire_shims.py --emit-manifest` for the selected manifest and registration report. Review ownership, unresolved entries, current visibility, and the requested changes; build the pointers from that manifest; use the verified adapter; then confirm against the platform's own list. Do not clear an occupied name merely because a new pointer needs it.

## Boundaries

- One copy of every procedure, in `00 ASTORIA/skills/{name}`. A scan platform gets a link. A registry platform cannot take a link, so it gets a pointer stub that carries no procedure at all: the stub is a routing entry and must never be filled with the skill's steps, because a second copy would drift. If a platform can use neither, the fallback is the `AGENTS.md` path.
- New vault scan mounts are relative symlinks to `../../00 ASTORIA/skills/{name}`, never outside the vault. Registry pointers name the resolved absolute location and a durable vault-relative path; moved pointers require ownership review before refresh.
- Before registration, state the verified visibility scope: project, machine, account, organization, or whatever the current platform actually supports. Keep the requested set to level-1 skills unless the user chooses another supported exposure.
- Nothing platform-specific outside its own row in the script's platform table and its own adapter section in `./references/registry_adapters.md`. A platform that is missing on a machine is reported and skipped, never a failed run, and never a reason to edit the rest of the skill.
- `.agents/` and `.claude/` hold the `skills` mount folder and nothing else; the lint flags anything else there. Keep local registry catalogs read-only. Use the authorized platform adapter for scoped changes to this vault's verified entries. Preserve entries from the platform, the user or other vaults.
- Use the actual vault path when a shortcut or filesystem alias points to it. When safe preview or supported mounting is unavailable, use the direct `AGENTS.md` route.
- Never change a skill's scientific or workflow description merely to fit a listing preference. Expose fewer skills or adjust the local preference; handle actual platform limits through its verified rules.
- If this run makes an authorized mount or registration change and logging it is within this role's authorized scope, add one entry at the top of the existing `00 ASTORIA/agent_notes/ai_log.md` under its callout. Use three to six lines with the date and skill in the heading and record what was done, where and what is pending.

## References

- Anthropic. (n.d.). *Claude Code skills documentation*. https://code.claude.com/docs/en/skills
- Anthropic. (n.d.). *Claude Science connectors and skills documentation*. https://claude.com/docs/claude-science/connectors-and-skills
- OpenAI. (n.d.). *Build skills*. https://learn.chatgpt.com/docs/build-skills
