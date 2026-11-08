---
name: astoria-updater
description: >-
  Updates an existing ASTORIA vault from a separate starter release. Identifies
  the two folders, previews supported changes, and applies the approved changes
  while keeping local work and settings. Triggers: update my astoria, upgrade my
  astoria vault.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: skills-janitor
  created: "2026-11-08"
  updated: "2026-11-08"
---

# ASTORIA Updater

Preview and apply a release to the vault the user already works in.

## Purpose

Own the update branch of Setup My Vault.
Update the ASTORIA files in an existing vault and preserve the user's work.

## Inputs

- The existing working vault, with its root `AGENTS.md` and `me.md`.
- A separate, trusted ASTORIA starter release with setup still pending. If the
  user chooses a ZIP, unpack it in a temporary folder outside both vaults. Use
  an extractor that rejects unsafe paths and links.
- The original unconfigured release as a comparison when available. Use the
  original download or a verified official release snapshot.
  ASTORIA release v1.0.0 was tagged at `e68ddeb` even though its ZIP name
  contains `v0.1.0`. Treat an unidentified installation as unknown.

## Steps

1. **Locate both folders.** If the chat is open in the new download, ask which
   existing vault to update. If it is open in the working vault, ask for the
   release ZIP or extracted folder. Downloads is a useful place to look when
   the user indicates they put it there. Use the folder picker or the user's
   supplied location. Obtain read access to the release and write access to the
   working vault. When only one workspace can be opened for editing, use the
   working vault. Resolve multiple matches before proceeding.
2. **Show the direction.** Give the user both paths as **Read from** and
   **Update**, with their known versions. Read the working vault's root
   instructions and briefing before acting on it. Treat the download as a
   source and keep the working vault as the destination.
3. **Verify and preview.** Before launching Python, verify the update folder
   against the official release ZIP or tagged tree. For a ZIP, verify the
   published asset checksum when available and check that the extracted
   updater and view helpers match the verified package. For an extracted
   folder, compare those files with the verified ZIP or tagged source.
   The automated preview runs the release's `build_views.py`, `skillkit.py`,
   and `lint.py` helpers in scratch with the assistant's normal permissions.
   If their origin or bytes cannot be verified, give a read-only comparison
   without running them. Verify the comparison release's provenance too.
   With Python 3.9 or later and PyYAML, run `scripts/update_astoria.py` with
   `--source RELEASE --target VAULT --verified-release`. Use that flag only
   after verifying the release. Add `--baseline OLD_RELEASE` when a matching
   official baseline is available.
   If the comparison release is missing, preview differences only. Obtain the
   original release before applying changes or recording a new version.
   Summarize the resulting adds, replacements, retirements, generated changes,
   and conflicts. Identify optional skills available separately. Keep the
   exact plan ID for apply. Ask the user once whether to apply the displayed
   changes. Explain any conflict or unavailable prerequisite in plain language.
4. **Apply and verify.** Repeat the same command with `--apply PLAN_ID` after
   approval. The script checks the preview again and saves a rollback copy of
   affected files before writing. If the plan changed, show the revised preview.
   Review the verification result, applied version, and pending items.
   Use the same assistant chat from either starting folder. If the assistant
   lacks the runtime or write access, give a read-only comparison and say what
   is needed to complete apply.

## Outputs

Present the preview and verified result in the format requested for this update
or specified by the vault's reporting policy.
A successful change appends an entry
to the existing AI log. An update with conflicts or an unverified baseline
keeps the prior installed version and reports the pending work.

## Boundaries

- Preserve `me.md`, root and project `AGENTS.md` files, notes, Obsidian settings,
  plugins and themes, and unrelated custom files.
- Compare shipped files against the selected original release before replacing
  or retiring them. When local changes or intentional deletions are ambiguous,
  keep them and show the user the conflict. Keep optional toolkit choices.
- Regenerate the Skill Map and coordinator catalogs from the destination's
  installed skills. Native skill mounting remains optional.

## Checks

Verify the destination, recorded version, generated views, and any unresolved
items. If the script reports rollback trouble or an interrupted run, retain its
backup and inspect the affected paths before retrying.
