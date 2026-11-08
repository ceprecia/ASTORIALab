---
name: teaching-platform
description: >-
  Inspects and performs authorized operations in the configured college course
  platforms, then verifies the affected student-facing outcome. Owns platform
  execution and operational checks. Triggers: check my LMS setup, verify my
  course groups, update my course platform.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-20"
---

# Teaching Platform

Verify the course operation and the student-facing result in the configured platform.

## Purpose

Inspect or perform authorized course-platform operations for instructors and TAs.
Own operational settings, group membership, assessment delivery, grade entry, and
publication verification. Receive academic decisions, approved scores, and communication
content from their owning skills or the user; do not decide them here.

## Inputs

- Offering: course, term, section, role, assigned responsibility, timezone, and platform links.
- Task and desired result, approved source versions, and known current evidence.
- Current permissions and explicit inherited simulation or read-only scope.
- The exact approved content or score payload when an operation would publish or enter it.

## Steps

1. **Resolve owner and context.** Read `me.md` and the course's owning Teaching AGENTS.md.
   When resources lie outside the area directory, follow the course owner/MOC link to
   that AGENTS file; do not create another. Match course, term, section, role, and target
   identifiers. If setup is missing, return the gap for teaching-assistant-builder rather
   than guessing an offering. Preserve the caller's exact task and permission scope.
2. **Select the mode.** For read-only work, inspect without changing state. In simulation,
   use supplied fixtures and mock outcomes; do not send messages, edit grades, modify
   assignments or groups, or change any live settings. If UI/tools are unavailable in
   simulation, report live state unverified instead of trying to exercise them.
3. **Inspect the specific target.** Use configured plugins as available. Read current
   settings, relevant source instructions, and dependencies before changing anything.
   Identify the existing object and its links so a duplicate is not created accidentally.
4. **Prepare the authorized operation.** For a bulk membership or grade change, obtain
   the platform's native export of the affected current state and preserve the relevant
   links/identifiers. Save requested backups in the verified owning course location.
   A simulation uses fixture exports only. If a required backup or preservation step
   cannot be completed, report that concrete limitation before the dependent change.
5. **Apply only the approved scope.** Follow the relevant procedure below. Resolve
   routine implementation choices within authorization. If content approval is still
   needed under the user's rules, prepare the concrete draft or change first.
6. **Verify the resulting effect.** Reopen or read back the affected object. Reconcile
   membership, settings, counts, links, scores, or content against the intended result.
   Use an available student preview to check access; teacher visibility alone is not
   proof of student access. Keep unobservable student state explicitly unverified.
7. **Return evidence and remaining work.** Report the target, changes or findings,
   observed outcome, and anything still unresolved. A successful simulated operation,
   export, save button, or request response alone is not evidence of live completion.

## Group Operations

- Identify the intended category, current eligible roster, enrollment method, target
  size, and any approved exceptions. Distinguish students from teaching-team members.
- Check roster coverage, unintended duplicate memberships within the category, empty
  groups, and undersized or oversized groups. Allow deliberate empty groups and an
  approved remainder distribution; group counts alone do not establish an error.
- Check after membership changes and before the first activity that uses the grouping.
  Refresh when withdrawals or additions could have changed a previously checked roster.
- Before authorized regrouping, preserve existing group identifiers, group storage
  links, associated assignments, submissions, and historical grades. Prefer membership
  changes within existing objects when that satisfies the user's request.
- Do not recreate or delete groups merely to make the list tidy. If preserving links
  cannot be established, keep the current state and return the specific unresolved choice.
- Verify every intended student has the appropriate membership, sizes match the approved
  rule, and the same linked submission/storage objects remain reachable afterward.
- Check applicable class instructions and existing announcements for changed group names,
  numbers, seating information, or directions. Return communication updates for drafting.

## Assessments and Submission Access

- Inspect the actual quiz or exam instance students receive, including fixed copies,
  pools, or selected bank versions. Never assume a bank correction propagated.
- Match questions by stable identifiers or wording rather than shuffled order or letters.
  Receive the corrected key/content from teaching-assessment; return content uncertainty.
- Compare the approved date, timezone, opening/closing windows, due date, attempt count,
  duration, scoring, visibility, release conditions, and feedback timing with live settings.
- Distinguish an availability window from a per-attempt duration. Determine effective
  accommodations from inherited and assessment-specific settings; do not add multipliers
  blindly or count each override as a separate student. Apply only approved accommodations.
- For assignments and discussions, verify the intended submission tool, group versus
  individual setting, deadline, linked grade item, and student access. A visible resource
  page does not prove that its submission location is open or correctly linked.
- Do not rebuild an assessment, delete attempts, or change released work as an incidental
  repair. Identify the exact issue and stay within the user's authorized operation.

## Grade Entry

- Require the approved score/feedback payload, student or group mapping, assignment,
  maximum points, and assigned grading scope. Return calculation or rubric decisions to
  teaching-grader. Never infer authority to release grades from a request to calculate them.
- Compare the payload with current entries and obtain a native backup before bulk writes.
  Preserve historical scores outside scope, release state, extra-credit treatment, and
  approved late-work or exception decisions. Do not replace unrelated values with blanks.
- Enter only the authorized rows and fields. Group grade posting and any approved
  individual participation adjustments are distinct operations; verify both if requested.
- Read back and reconcile counts, identifiers, points, comments, and publication state.
  Report mismatches without claiming success for the affected entries.

## Announcements and Communications

- Receive an approved draft from teaching-office-hours or the user. Identify whether
  the task updates an existing announcement or creates one, and use the existing object
  when an update is requested. Preserve requested images, links, formatting, and dates.
- Verify the title, body, course audience, visibility/release state, and retained media.
  Do not create multiple announcements to achieve one requested update.
- Announcement publication and class email delivery are separate effects. Verify each
  only when explicitly authorized and performed. Do not infer one from the other.
- If changed platform details contradict an existing message, return the exact difference
  for a draft correction. Do not silently send or publish an extra communication.

## Outputs

Return offering and target; relevant evidence; proposed or performed operation; status
(verified complete, proposed, partially verified, or unresolved); and next owner/action.
Return the check report in the current task's requested form or under the recipient's existing reporting policy. Save authorized native backups in the verified owning course location. For an authorized separate report or deliverable, use the verified eligible destination selected for the task. If none was selected, follow the applicable verified recipient or course placement policy. If neither resolves it, use the verified owning course location when eligible. Apply course access and privacy requirements to each save and resolve any outstanding destination before writing. LMS changes, publication and delivery each require their own action authorization. Do not create separate dashboards, databases or per-provider skills as a side effect.

## Boundaries

- Follow `me.md`, the user's current authorization, and the inherited execution mode.
  Approval for one audience, item, or course does not expand to another.
- Platform documentation explains operation, not academic correctness or course policy.
  Use current official help for unfamiliar settings and cite the relevant instruction.
- Treat source disagreement, inaccessible settings, and missing student preview as
  unresolved evidence. Do not convert teacher access or a screenshot into a broader claim.
- Do not guess private accommodation details, student identities, participation, or grades.
  Request only the specific missing information that affects the authorized task.

## Handoffs

Return academic content and key issues to teaching-assessment, score/rubric issues to
teaching-grader, and communication wording to teaching-office-hours through the caller.
Preserve offering, task, sources, permissions, simulation/read-only scope, and desired
result in each handoff. Return setup gaps to teaching-assistant-builder. The invoking
companion owns sequencing and saved course continuity; do not create another task queue.

## Modular Plugin Support

Configure the provider per offering, such as D2L/Brightspace, Top Hat, Canvas, Moodle,
or another institution service. Prefer the provider's native export and purpose-built
connector or supported API when available; use permitted browser/UI automation when
needed. Keep provider-specific instructions in the course configuration or current
help documentation, not separate skills. Verify access with the available capability.
Configured email tools perform separately approved mail delivery. A missing integration
allows review of supplied exports or screenshots, with live state explicitly unverified.
Apply the user's exact write/send/publish permissions; unavailable tools in a simulation
are not a reason to open a live service or substitute an unapproved execution route.

## Checks

- Correct offering, target objects, role, scope, and execution mode?
- Required native backup obtained before a bulk live change, with existing links preserved?
- Intended membership, actual assessment version, effective settings, or score payload verified?
- Published content and student access checked separately where observable?
- Every completion claim supported; partial access and simulation clearly labeled?
