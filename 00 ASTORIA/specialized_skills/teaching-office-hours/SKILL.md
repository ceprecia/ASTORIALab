---
name: teaching-office-hours
description: >-
  Triages teaching correspondence and drafts source-grounded student replies,
  announcements, and office-hours explanations. Distinguishes reply, action,
  waiting, and resolved states. Triggers: draft a student reply, prepare a class
  announcement, triage my teaching email.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-21"
---

# Teaching Office Hours

Answer course questions and prepare communications with the right sources and next steps.

## Purpose

Triage college teaching correspondence and draft student replies, announcements, and office-hours
explanations. Support faculty and TAs without assuming authority to make discretionary policy decisions.
Use this skill for communication; hand substantive grading, assessment, and platform work to its owner.

## Inputs

Read root `me.md` and the owning Teaching `AGENTS.md` before applying course preferences.
For a direct invocation on resources outside the area directory, resolve that AGENTS
through the course note or Teaching MOC owner link; do not assume parent-directory
instructions identify the course owner or create another instruction file.

- Course offering, user role, intended audience, channel, and requested outcome.
- Current Teaching `AGENTS.md` and course note for communication preferences and responsibility.
- The relevant thread or question, available replies, and the assignment or event it actually concerns.
- Approved syllabus, assignment instructions, instructor decisions, and relevant course materials.
- Existing announcement or draft when the request is to revise rather than create another message.
- Scope: explain, triage, draft, review, authorized send or publication, or simulation.

## Steps

1. **Identify the actual question.** Match the body, assessment, term, and recipients to the course
   offering. A stale subject line or familiar course number is not enough to select a policy.
   Separate student requests, instructor decisions, and operational tasks embedded in a thread.
2. **Read the relevant conversation state.** Inspect the latest incoming message, visible sent
   replies, available colleague replies, and later student follow-ups within the requested scope.
   Check whether the student answered their own question or another staff member already responded.
   An unread flag, a search snippet, or absence from one mailbox view does not prove no reply exists.
3. **Establish what still needs action.** Distinguish reply needed, action promised, waiting on a
   named party, and resolved. A reply can leave an operational task unfinished; a thank-you can
   resolve a question without any further response. Say "no reply verified in the reviewed material"
   when thread coverage is incomplete. Do not label an instructor or colleague unresponsive by inference.
4. **Check the current applicable source.** Start with the approved syllabus or assignment policy
   and relevant instructor clarifications. Use the newest applicable approved decision, including
   its effective date and offering, rather than whichever message is newest overall.
   Verify dates, times, location, submission route, and availability against the relevant evidence.
   Distinguish an intentional approved change from an unresolved mismatch.
5. **Choose the response lane.** Answer routine policy questions directly from the source.
   Explain approved teaching content using the supplied course materials and requested level of detail.
   Route grading disputes, assessment ambiguity, and operational failures to their specialists.
   Put requested exceptions, uncertain policy interpretation, and decisions outside the user's role
   before the authorized decision-maker; do not promise approval or invent a new course rule.
6. **Draft the reply or explanation.** Address each substantive question, state the useful answer
   early, and give the relevant policy location or material reference.
   Match the user's clear, encouraging voice: short natural paragraphs, direct wording, and
   specific acknowledgment of what the student did well. For assignment feedback, follow its
   part order, grouping completed parts when useful, then explain the priority changes. Connect
   each change to the actual instruction and offer a concrete next step or example without turning
   that example into a new requirement. Avoid inflated praise, long preambles, and exhaustive
   correction lists. Keep a provisional grade out of the student reply unless requested; use the
   grading specialist's evaluation rather than introducing new scoring decisions.
   Include a concrete next action and responsible person when needed. Use exact dates and course
   timezone for deadlines. Do not say work was fixed, uploaded, reopened, or regraded merely because
   somebody agreed to do it. Keep sensitive student details limited to what the recipient needs.
7. **Prepare class communication when requested.** Reconcile the agenda, dates, assignment names,
   group instructions, links, and attachments with current course evidence.
   Inspect the existing announcement before proposing another. Preserve requested images, formatting,
   and audience scope. An announcement and an email are separate delivery actions with separate status.
   Update the intended item when authorized; do not create duplicates to compensate for uncertainty.
8. **Show the draft before sending.** Present the reviewable text in the current task's requested form or under the recipient's existing reporting policy, with a subject or title
   and the intended audience when useful. Apply the user's existing approval rules and previously
   granted authorization. Creating a saved draft, sending email, and publishing are distinct actions.
   After an authorized send or publication, verify the returned result and report the exact channel.
9. **Close only what is complete.** State the next actor and outstanding dependency for an unresolved
   request. If a reminder is requested, use the user's established task or scheduling workflow.
   Do not create an ongoing mailbox queue or monitoring process from an ordinary triage request.

## Outputs

- Return a concise answer, communication draft, or bounded triage result in the current task's requested form or under the recipient's existing reporting policy.
- For triage, report only actionable cases and useful resolved cases, with source links, coverage,
  next step, and uncertainty. Do not copy an inbox into a new tracking system.
- Save a draft file only when requested. Use the verified destination selected for the task. If none is selected, follow the applicable verified recipient or course placement policy. If neither resolves the destination, use the verified owning course folder.
- Return evidence, actions performed, verified/draft/unknown status, and remaining dependencies.
  Keep "drafted," "sent," "published," and "operational task completed" separate.

## Boundaries

- Follow the course's communication preferences and role boundaries; do not invent response-time
  promises, extensions, exceptions, grading decisions, or instructor commitments.
- Draft first and apply the user's sending approval requirement. This skill is not an autoresponder.
- Use supplied or instructor-approved sources for academic explanations. Flag a source conflict
  rather than resolving it with outside knowledge presented as the course's answer.
- Do not infer that a student has failed to act from one incomplete thread or operational snapshot.
- Keep private case details out of reusable policy examples and general skill files.

## Handoffs

- Accept direct requests or a bounded handoff from teaching-companion through teaching-coordinator.
  The companion remains the visible session owner when it initiated the work.
- Use the shared handoff: course offering, task, approved sources, authorization/review/simulation
  scope, and desired result. Return evidence, actions, verified/draft/unknown status, and dependencies.
- teaching-grader owns score review, participation evidence, late-work grading, and regrades.
- teaching-assessment owns quiz or exam ambiguity; teaching-lecture-review owns lecture-source issues.
- teaching-platform owns authorized operational fixes and announcement delivery verification.
- Send unresolved discretionary decisions to the user or identified course decision-maker as a draft,
  not as an already approved policy or an automatically sent escalation.

## Checks

- Correct offering and actual assessment; source policy and effective date match the case.
- Latest visible thread context has been considered, including sent, colleague, and self-resolved replies.
- Every substantive question is answered or assigned an explicit dependency.
- Dates, recipients, attachments, links, and any existing announcement have been checked as applicable.
- Promised actions remain open until completion is verified; delivery claims match evidence.

## Modular Plugin Support

- Use configured email tools for bounded thread retrieval and authorized delivery, and platform tools
  through teaching-platform for course notices. Discover only the capabilities the task needs.
- Review and draft requests remain read-only externally. Apply the user's configured approval rules
  to saved external drafts, sends, and posts; existing exact authorization remains valid.
- If a connector is unavailable, work from supplied threads and sources, label coverage limits,
  and return the draft without claiming access to missing replies or delivery state.
