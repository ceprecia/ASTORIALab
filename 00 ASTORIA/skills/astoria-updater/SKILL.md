---
name: astoria-updater
description: >-
  Updates an existing ASTORIA vault and follows up with two janitor audits and
  an update recheck. Identifies both folders, previews changes, and applies
  approved updates and audit repairs while keeping local work and settings.
  Triggers: update my astoria, upgrade my astoria vault.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: skills-janitor
  created: "2026-11-08"
  updated: "2026-11-13"
---

# ASTORIA Updater

Preview and apply a release to the vault the user already works in.

## Purpose

Own the update branch of Setup My Vault.
Update the ASTORIA files in an existing vault and preserve the user's work.
Complete two audit passes in the same chat, with approval of proposed repairs
after each audit. The audits start automatically after the update.

## Inputs

- The existing working vault, with its root `AGENTS.md` and `me.md`.
- A separate, trusted ASTORIA starter release with setup still pending. If the
  user chooses a ZIP, unpack it in a temporary folder outside both vaults. Use
  an extractor that rejects unsafe paths and links.
- The original unconfigured release as a comparison when available. Use the
  original download or a verified official release snapshot.
  ASTORIA release v1.0.0 was tagged at `e68ddeb` even though its ZIP name
  contains `v0.1.0`. Treat an unidentified installation as unknown.
- Skills Janitor remains a required update dependency. Missing required support
  is an update prerequisite finding; removed optional audit skills are audit gaps.

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
   If this chat began with the working vault's updater, load the verified
   release's `00 ASTORIA/skills/astoria-updater/SKILL.md` completely and
   continue under those instructions, including their post-update checks.
   Keep the confirmed folders, original comparison release and prior decisions.
   With Python 3.9 or later and PyYAML, run the verified release's
   `scripts/update_astoria.py` with
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
5. **Janitor audit, pass 1.** Load the complete installed instructions for
   [Skills Janitor](../skills-janitor/SKILL.md),
   [Vault Janitor](../vault-janitor/SKILL.md), and
   [Folder Janitor](../folder-janitor/SKILL.md). Invoke all three in audit-only
   mode on the working vault, using its instructions, chosen structure, read
   exclusions and holds. Audit skills and generated views, vault/layout and
   instruction consistency, links and active paths, and Project/Area structure.
   Limit content reading to what those checks need. Reuse Folder Janitor's
   result if Vault Janitor already invoked it for the same scope in this pass.
   If an optional janitor was deliberately removed or cannot run, report that gap and
   continue the available checks without reinstalling it.

   Use `lint.py`, `build_views.py --check`, `build_layout.py --check` and the
   supported link audit with the verified target and exclusions. Run Python
   audit commands with `-B` to avoid creating bytecode caches in the vault. Use reading
   for checks without a suitable script. Audit mode leaves the working vault
   unchanged, including its log. Do not rebuild views/layout, move files or
   repair instructions during the audit. The request to update does not
   authorize the newly discovered janitor repairs.
6. **Approve and apply audit repairs.** Combine the findings from all three
   janitors into one concrete proposal with affected paths, exact edits or
   moves, and any uncertainty. Ask **"Can I make these changes?"** before
   implementing it. Apply only the selected repairs through their existing
   owners and verify those changes. If there are no repairs, continue without
   asking. Keep declined findings visible and proceed with the remaining checks.
7. **Recheck the update.** Run the updater preview again using the same
   verified source, working vault and original comparison release from the
   first pass, including when the installed version now equals the source
   version. Re-read current files and obtain a new plan ID. Check for omissions
   and remaining conflicts; a version match alone does not establish completion.
   Apply a remaining delta only when its exact changes are already approved
   or the user approves the new preview. Preserve declined repairs, deliberate
   deletions and local customizations. Do not use the second pass to bypass a
   decision or replace the original comparison with the updated vault.
8. **Janitor audit, pass 2.** Run the same three audit-only checks again after
   the second update check and any approved changes. Present new or remaining
   findings. Obtain approval for any additional proposed repairs before applying
   them, then verify the approved fixes. Finish with the status of both audit
   passes and unresolved or uninspected items. Stop after these two passes;
   further work follows the user's direction.

## Outputs

Present the preview and verified result in the format requested for this update
or specified by the vault's reporting policy.
A successful change appends an entry
to the existing AI log. An update with conflicts or an unverified baseline
keeps the prior installed version and reports the pending work.
Distinguish the applied update, each janitor audit, approved or declined
repairs, the second update check, and remaining gaps. A completed file update
does not imply that the post-update audits ran.

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
