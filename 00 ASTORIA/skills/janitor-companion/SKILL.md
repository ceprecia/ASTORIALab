---
name: janitor-companion
description: >-
  Leads vault cleanup and audit sessions, routes checks through Janitor
  Coordinator, and turns findings into specific fixes for the user to approve.
  Use for broad maintenance requests or the standalone invocation “janitor”.
  Triggers: load the janitor system, fix my vault, clean up my vault.
metadata:
  level: companion
  system: Janitor System
  dependencies: janitor-coordinator
  created: "2026-11-24"
  updated: "2026-11-24"
---

# Janitor Companion

Find what is wrong, show the changes in plain language, and verify the fixes the user chooses.

## Purpose

Own the user-facing session for maintaining the vault and its AI workflows.
Use this entry point for a broad cleanup, a general audit, a mixed request,
or the standalone request “janitor”. Open the canonical
[Janitor Coordinator](../janitor-coordinator/SKILL.md) for
triage, specialist routing, and execution. A clearly named specialist keeps
its direct route and its existing rules.

## Inputs

- The request, available workspace, selected projects or folders, and any
  reported symptoms or evidence.
- Any protection, exclusion, hold, or explicit authorization already given
  for a concrete operation.

## Steps

1. **Route the request.** For a clear target or symptom, send the bounded
   question to the coordinator immediately. For an explicitly general review,
   have the coordinator run a read-only general audit with every applicable
   installed specialist. For a vague request, including “janitor” by itself,
   start with a brief read-only triage. Use its evidence to offer a specific
   cleanup with a named target, or a general audit. If triage identifies no
   issue, describe the limited check and offer a focused audit of a relevant
   named area or the general review. Give the evidence and ask only for the
   remaining scope choice. Present the findings after the selected review in the reporting form resolved under Outputs.
2. **Review the specialist findings.** Present each independently actionable proposal with its stable finding ID in the human-facing form resolved under Outputs. Explain how the observed issue affects the user or agent and what changes in practice if fixed. Associate evidence with the finding ID. Label simulated effects as simulated and expected effects as expected. For an unresolved finding, state the evidence or decision still needed in that form.
3. **Apply the selected fixes.** Treat a broad request such as “fix my vault”
   as authorization to find and propose. Ask which numbered rows the user
   wants applied and wait before editing live files. Bind the approval to the
   exact proposal shown in this conversation. On resume, recover that proposal
   and the user’s approval before acting. Carry any earlier exact authorization
   forward without a second gate. Send only the selected fixes
   and their covered dependencies to the coordinator. If current evidence
   changes the operation, affected targets, or consequences of an approved
   proposal, present the changed row for fresh approval and continue any
   independent authorized work.
4. **Verify and close.** Collect evidence on the approved targets and their
   affected dependencies. Reuse the original symptom or reproduction when
   available. Mark each selected row as applied and checked, applied with a
   named verification limit, or blocked with the reason. Leave other rows as
   proposals. Keep Janitor Companion responsible for the session and follow the existing system log
   workflow for authorized system changes.

## Outputs

Use the current request's reporting form. For choices left open, follow the recipient's applicable verified reporting policy, with chat as the fallback. Honor explicit current chat-only, no-save and read-only limits. Create or save a report only within authorized output and destination scope; a reporting preference alone supplies no save, capture/log or external-send authority. Reuse applicable existing authorization without another gate. Keep stable finding IDs through reporting, approval and verification. Reporting does not approve live fixes.

Retain Issue found, Behavior, Fix and New behavior as semantic fields, with stable finding IDs, in internal Coordinator packets. Convey that information in the selected human-facing form. The following table is an optional template when table output is selected.

| Issue found | Behavior | Fix | New behavior |
| --- | --- | --- | --- |
| 1. Evidence and affected target | What happens now | Exact operation and scope | Expected effect, or verified effect with evidence |

If there are no findings, report which areas were checked and any access or
verification gaps.

## Checks

- A vague request received a bounded triage before the scope choice. A
  specific or explicitly general request proceeded directly.
- A broad review stayed read-only until the user chose concrete fixes.
- The selected specialists inspected the evidence. Each approved change
  reached its owner and was verified to the extent reported.
