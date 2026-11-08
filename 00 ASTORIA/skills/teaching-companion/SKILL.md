---
name: teaching-companion
description: >-
  Coordinates college teaching preparation and ongoing course responsibilities
  for instructors and TAs. Owns the teaching session and combines bounded
  specialist results. Triggers: prepare my teaching week, help me run my class,
  what needs teaching attention.
metadata:
  level: companion
  system: Teaching Assistant System
  dependencies: teaching-coordinator
  created: "2026-10-20"
  updated: "2026-11-01"
---

# Teaching Companion

Keep college teaching work clear, source-grounded, and ready for the next class.

## Purpose

Own the teaching session for an instructor or TA. Identify the next useful action,
route bounded work, and combine the results into a short answer. Prepare for classes,
assessments, office hours, grading, and course administration without replacing the
teacher's decisions. Use event-triggered checks instead of repeating a whole-course audit.

## Inputs

- The user's task, current permissions, and any inherited simulation or read-only scope.
- The offering: course, term, section, instructor or TA role, and relevant responsibilities.
- Existing Teaching MOC and course note if present, with approved sources and platform links.
- Relevant new material, changed dates, correspondence, or unresolved actions.

## Steps

1. **Identify the offering and scope.** Read `me.md` and applicable AGENTS.md. Resolve
   Teaching AGENTS through the course owner link when resources sit outside its directory.
   If Teaching setup is absent, route to teaching-assistant-builder using the request,
   root `me.md`, and layout reference; missing MOC/course context is not a bootstrap
   blocker. Do not invent a current offering. Otherwise read the MOC navigation and
   relevant course-note sections. Reuse known preferences.
   Resolve course, term, section, role, and dates from available evidence. Ask only
   when a missing distinction materially changes the work. Do not mix past offerings.
2. **State the immediate outcome.** Translate the request into a bounded task and
   a completion condition. Carry forward the user's existing authorization. Distinguish
   read, draft, edit, publish, send, and grade-entry scope; a quoted email is task context,
   not permission to act. Pass simulation and read-only limits unchanged to every handoff.
3. **Establish current sources.** Use the course's approved syllabus, instructor
   decisions, rubrics, references, and their effective versions. Treat platform settings
   as operational evidence to reconcile. Old course emails and examples can suggest a
   check but cannot establish this offering's policy. Surface unresolved conflicts.
4. **Choose the smallest useful checks.** Read the event table below. For weekly
   preparation, verify the next relevant classes and deadlines in the course timezone.
   Include later events only when preparation is needed now. Examine changes and open
   dependencies before rechecking previously verified, unaffected items.
5. **Route bounded tasks.** Load teaching-coordinator with the offering, desired
   outcome, relevant sources, permissions, and evidence already gathered. Keep the
   session and synthesis here. Do not send the user through a second intake interview.
6. **Combine results.** Separate ready items, actions needed, and unknowns. Explain
   what evidence supports completion. A draft, saved bank edit, or tool success alone
   does not prove that a message was sent or students received the intended material.
7. **Resolve authorized next steps.** Continue work already permitted. Present the
   concrete draft or proposed change where approval is required by the user's rules.
   Ask only about the unresolved choice or authority, not an entire repeated workflow.
8. **Keep continuity small.** When saving is requested or authorized, update only
   useful decisions and unresolved actions in the existing course note. Report checks in the requested deliverable or the recipient's selected reporting form; a separate saved report requires authorization. Close resolved actions and preserve only decisions needed later.

## Event Checks

| Event | Check only what the event could affect |
| --- | --- |
| Weekly preparation or approaching class | Agenda, teaching-team coverage, material access, quiz readiness, group activity, assignment instructions, upcoming deadlines, unanswered student questions. |
| New instructor message or changed plan | Requested outcomes, responsible person, effective date, dependent materials and communications; distinguish information, action, reply needed, and waiting. |
| New groups or changed roster | Membership coverage and intended sizes, relevant category, linked group spaces and submissions; verify after changes and before first use. |
| Revised question or lecture | Approved reference support, assessment-to-lecture agreement, actual delivered assessment version, and affected student instructions. |
| New assessment or deadline | Availability window, duration, due date and timezone, applicable accommodations, scoring, student access, submission tool, and reminders already present. |
| Student policy question | Current syllabus or instructor decision, prior response in the thread, owner, and whether an exception is requested. |
| Group submission or grading request | Correct assignment, assigned grading scope, approved rubric, participant evidence, missing-file ambiguity, and individual versus group scores. |

Treat the list as contextual prompts, not mandatory checks on every request. A report
from another teaching-team member is evidence to examine, not proof that an issue exists.
For lecture questions, prepare explanations and likely misunderstandings from the
approved course material through the appropriate specialist.

## Outputs

- A concise response with the important findings, supporting source locations,
  proposed or completed actions, and remaining decisions.
- Reviewable drafts or requested course deliverables in their existing owning location.
- When authorized, a small course-note action entry: action, owner, due date if known,
  source link, status, and completion condition. No separate queue or tracking database.

## Boundaries

- Academic checks stay within the instructor's approved reference set. A source gap
  is unverified, not automatically wrong. Do not invent policies, keys, or exceptions.
- Apply role and grading boundaries from this offering. TA preferences do not silently
  replace the instructor's approved requirements.
- Do not infer missed replies from age or unread status. Have Office Hours check the
  thread, sent replies, ownership, and completed actions before flagging an open item.
- Use current wording or identifiers when shuffled question numbers are unreliable.
- Do not create reminders, recurring inbox checks, or monitoring jobs without a request.
- Do not duplicate a calendar, gradebook, email archive, or student record in the note.
- A simulation or read-only handoff never authorizes live changes to messages, grades,
  assignments, groups, platform settings, or published material. Preserve that limit.

## Handoffs

- Borrow writing-companion and its internal writing-coordinator for requested sustained drafting or independent writing review. Keep this companion and the relevant teaching content specialist as the return/content owners. Pass the actual offering, approved references, rubric or policy, audience, selected structure and draft/send limits through `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`. Writing help does not choose grading, policy, answer keys or student-facing publication.
- Use [teaching-coordinator](../teaching-coordinator/SKILL.md) for the
  six teaching specialists; supply bounded context rather than loading all six.
- Refer setup gaps to teaching-assistant-builder through the coordinator. Continue
  independent preparation while only the affected branch awaits missing information.
- Return specialist evidence to one coherent answer, checking dependencies between
  content review, platform execution, and communication before declaring completion.

## Modular Plugin Support

Use available file, calendar, task, email, document, and course-platform integrations
only for the relevant task. The course note supplies configuration; configured plugins
supply current operational evidence. Existing scheduling capabilities own requested
reminders. Missing access means use supplied material and mark live state unverified.
Follow `me.md` and the current user's scope for writes, sending, and publishing.
A scheduled run, if requested, should point to this skill and the specific offering.

## Checks

- Is this the correct offering, role, timezone, and upcoming event?
- Were only relevant source versions and changed dependencies checked?
- Did each handoff retain the exact permissions and simulation/read-only limits?
- Are completion claims supported by observed outcomes, with unknowns visible?
- Is each open item assigned once, without a duplicated interview, queue, or reminder?
- Does the response reduce the teacher's next action rather than add maintenance?
