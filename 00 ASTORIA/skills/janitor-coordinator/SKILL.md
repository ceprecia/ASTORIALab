---
name: janitor-coordinator
description: >-
  Loads the installed specialists for a Janitor Companion request, coordinates
  evidence gathering and authorized repairs, and returns one owner per
  actionable fix. Use internally within Janitor Companion.
metadata:
  level: coordinator
  system: Janitor System
  dependencies: ""
  created: "2026-11-24"
  updated: "2026-11-24"
---

# Janitor Coordinator

Match each issue to the specialist that can check and fix it.

## Purpose

Run within Janitor Companion. Use the generated Specialist Catalog and the
selected skills' handoffs to find the current owners. Keep the companion
responsible for the user's scope choice, presentation, and approval.

## Inputs

- The requested outcome, mode, workspace, targets, evidence, exclusions,
  active writers, and relevant governing instructions.
- The current authorization, including the exact approved row and affected
  targets when applying a fix.

## Steps

1. **Choose the scope of the checks.** For triage, do the smallest read-only
   check that can inform the choice, using the supplied symptoms and readily
   verifiable, in-scope sources. For a targeted request, select the relevant
   owner. For an explicitly general audit, consider all installed specialists
   and use each that has an applicable check. For a skill that requires an
   exact target or a chosen change, such as removal or propagation, act only
   when the investigation establishes that target or change and carries the
   required scope. Report any material check that remains unavailable.
2. **Load the specialists.** Open each selected canonical `SKILL.md`
   completely and follow its required references and gates. Search the
   generated catalog and applicable handoffs when a finding crosses owners.
   If a catalog entry looks stale, verify the installed canonical folders
   before routing and return the stale view as a finding. Execute the selected
   workflows with the tools available to this chat, preserving the authority
   and limitations of each skill.
3. **Pass a concrete brief.** Include the question, exact evidence and source
   locations, approved targets, holds and exclusions, expected return, and
   existing authorizations. Pass read-only scope for triage, auditing, and
   proposal work. Carry those limits through handoffs. A broad review can
   identify filing, propagation, and removal candidates. Live changes to those
   targets require authorization for the specific operation.
4. **Consolidate findings.** Compare the actual specialist results and the
   evidence supporting them. Merge duplicate reports about the same cause and
   proposed change. Return separately approvable actions as separate findings.
   Name one owner for each concrete fix, with dependent checks, available
   reproductions, and any uncertainty. Return substantive disagreements for
   the companion to show where they affect the decision.
5. **Apply and verify approved rows.** Recheck the evidence and target
   immediately before the write. Pass the exact already-approved action and
   its limits to the owner. If new state changes the proposal, return the
   revised row and withhold that edit until approval. Sequence shared
   dependencies, keep one editor per file, and verify the approved surface
   and affected dependencies using the owning skill. Return concrete
   before-and-after evidence and any verification gaps to the companion.

## Specialist Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

- [agent-janitor](../agent-janitor/SKILL.md): Audits agent behavior, traces where context or instructions drift, and tests candidate fixes before proposing live changes. Triggers: audit agent drift, agents keep using old instructions, test an agent handoff.
- [bridge-maker](../bridge-maker/SKILL.md): Creates or updates a short project AGENTS.md pointing to the vault-root me.md. Triggers: make a project bridge, connect this project to obsidian, audit the project bridges, update this project AGENTS.md.
- [folder-janitor](../folder-janitor/SKILL.md): Organizes the requested content folders outside the AI system root using the owner’s verified structure and approved placements. Triggers: organize this folder, sort my resource intake, tidy my area folders, file these attachments.
- [propagate](../propagate/SKILL.md): Carries one change through everything that depends on it. Triggers: propagate this rename, I renamed this, propagate this convention, make the family match, update every reference to.
- [skills-janitor](../skills-janitor/SKILL.md): Audits every skill folder in `00 ASTORIA/skills/` against the skill-builder schema and regenerates the views. Triggers: audit my skills, are my skills in sync, rebuild the skill map, check for trigger overlaps, skill drift.
- [vault-janitor](../vault-janitor/SKILL.md): Checks vault consistency: the layout reference against the folder tree and vocabulary, rules against me.md, active instructions for stale paths and wording, and wiki-links vault-wide. Triggers: audit the layout, are my folders and templates in sync, check for folder drift, check log preservation, clean up the agent notes.
- [verify-removal](../verify-removal/SKILL.md): Removes named local items directly and verifies app uninstalls on macOS, Windows, and Linux. Triggers: uninstall this Mac app, check for uninstall leftovers, verify an app is gone, delete these specific files.

7 skills in this system.
<!-- catalog:end -->

## Outputs

- Triage returns the checked scope, the issue or symptom supported by
  evidence, and the best bounded specialist route.
- Audits return the issue, source and exact locator, observed behavior,
  proposed operation and scope, proposed effect, owner, applicable test or
  verification, and limits.
- Approved fixes return the row number, changed targets, verification
  evidence, and remaining gaps.

## Checks

- Each specialist return identifies the canonical skill body used and the
  sources or checks actually examined.
- Target-required workflows had concrete targets. Audit, protection, exclusion,
  and write limits survived every handoff.
- Each proposed change has one owner and each executed change matches the
  approved action.
