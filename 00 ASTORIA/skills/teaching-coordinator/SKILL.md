---
name: teaching-coordinator
description: >-
  Routes one bounded college-teaching task to its specialist and returns
  evidence, unresolved dependencies, and the completion condition to the
  invoking teaching companion. Internal router only.
metadata:
  level: coordinator
  system: Teaching Assistant System
  dependencies: teaching-assistant-builder, teaching-grader, teaching-office-hours, teaching-platform, teaching-lecture-review, teaching-assessment
  created: "2026-10-20"
  updated: "2026-11-01"
---

# Teaching Coordinator

Route one bounded teaching task and return its evidence to the session owner.

## Purpose

Act as the internal router for teaching-companion. Select the specialist that owns
the requested outcome, pass the existing context, and return its result. Make no
academic, grading, policy, or publishing decision. Do not start a second interview.

## Inputs

Require a handoff containing the offering, task, approved source locations and versions,
current permissions, inherited simulation/read-only scope, evidence already available,
and desired completion condition. Treat omitted facts as unknown, not verified.
For first setup, the request, root `me.md`, and layout reference are sufficient input;
Teaching AGENTS, MOC, and offering may not exist yet. Route to the builder without
requiring those outputs as prerequisites or inventing a course.
For filing-only maintenance of existing folders, the selected folders, owner
structure, action scope, holds and return point are sufficient; an offering
identity or syllabus is not required.

## Steps

1. Match the task's primary outcome to one specialist in the catalog. Read that
   skill completely. Resolve routine details from the handoff and supplied sources.
2. Pass the exact offering when applicable, or the selected folders for filing,
   and the action scope, including read-only or simulation limits.
   Include relevant source excerpts or links and known gaps. Do not expand permission
   because the receiving skill can perform more operations.
3. Have the specialist return its result in the return contract below. If a material
   decision or missing source prevents the task, return that specific gap to the
   companion. Continue only independent work within the existing task.
4. Return the result once. Identify a next owner when a dependency remains; let the
   companion sequence the next task. Do not recursively route back to this coordinator
   or create a parallel action list.

## Specialist Catalog

| Outcome | Owner |
| --- | --- |
| Teaching area or offering setup, syllabus intake, academic course migration | [teaching-assistant-builder](../teaching-assistant-builder/SKILL.md) |
| File existing course materials or tidy Area/content folders, with link/path-token repairs only | [folder-janitor](../folder-janitor/SKILL.md) |
| Apply approved rubric, calculate scores, draft grading feedback | [teaching-grader](../teaching-grader/SKILL.md) |
| Student questions, policy replies, announcements, email drafts and thread triage | [teaching-office-hours](../teaching-office-hours/SKILL.md) |
| Inspect or change configured course-platform state; verify student-facing effect | [teaching-platform](../teaching-platform/SKILL.md) |
| Review or revise teaching materials against supplied approved references | [teaching-lecture-review](../teaching-lecture-review/SKILL.md) |
| Design or check quizzes, exams, assignments, discussion prompts and proposed rubrics | [teaching-assessment](../teaching-assessment/SKILL.md) |

Content decisions remain with the relevant content specialist. Platform owns live LMS
execution, including approved grade entry and assessment settings. Office Hours owns
the communication draft; a platform announcement and a sent email are separate effects.

Folder filing is a conditional maintenance detour: verify folder-janitor when
requested, pass the existing folder scope, holds and any approved move/dependency
plan, and return to the same session owner. Honor its one checkpoint for very large moves or critical
operational changes; do not repeat approval for an already approved concrete
scope. Keep course creation with the builder and MOC prose, headings,
decisions and log narratives outside the filing task except exact active path
tokens needed by the move. A standalone filing request can go directly to folder-janitor without a teaching intake.

## Outputs

Return a concise result with:

- **Offering or selected folders and task:** the specific scope examined.
- **Evidence:** source locations and relevant current observations; partial access explicit.
- **Result:** findings, draft, or authorized operation and its verification.
- **Status:** verified complete, proposed/drafted, partially verified, or unresolved.
- **Next step:** any unmet completion condition, responsible next owner, and required input.

Do not create a report file or save task state. Return to the invoking companion.

## Boundaries

- No new intake form, task queue, gradebook, or source hierarchy.
- Never select a different academic answer or course policy to resolve source conflict.
- Do not treat old examples, missing evidence, or a specialist's confidence as verification.
- Preserve action restrictions in every handoff. Simulation and read-only work cannot
  change live emails, grades, assignments, groups, settings, or published material.
- Do not call every specialist for a narrow request. The companion owns sequencing
  and decides whether another bounded task is needed from the returned evidence.

## Handoffs

For a requested writing-assistance task, borrow the exact shared writing specialist or writing-coordinator using `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`. Preserve the offering, approved course sources, original return owner and permitted actions. The relevant teaching specialist keeps content and communication ownership; shared specialists can help with argument, structure, substance, citations and integration without changing an answer key, rubric or policy. Return technical or academic ambiguities to the existing content owner.

Receive from teaching-companion and return to the same session owner. A direct invocation
without a companion may return the same result contract to the caller; do not spawn a
replacement companion or a routing loop.

## Checks

- One specialist owns the requested outcome; dependent work has a named next owner.
- Offering, sources, authorization, and simulation/read-only scope survived unchanged.
- Evidence distinguishes inspected facts from inferred or inaccessible state.
- No extra interview, duplicate queue, unrequested operation, or false completion claim.
- Filing an established collection reaches folder-janitor without an offering
  intake; course setup still reaches the builder, and the detour returns once.
