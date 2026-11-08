---
name: teaching-lecture-review
description: >-
  Reviews college teaching materials for clarity, mechanical errors, and
  agreement with instructor-approved references. Makes requested revisions
  within the assigned lecture scope. Triggers: check my lecture slides, review
  my teaching materials.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-20"
---

# Teaching Lecture Review

Make teaching materials clear and consistent with the instructor's approved references.

## Purpose

Review college lectures, slides, handouts, and related teaching materials for mechanical errors,
clarity, and agreement with supplied or instructor-approved content.
Make authorized revisions within the user's assigned portion and prepare source-grounded explanations.
This skill supports the instructor's teaching choices rather than replacing them with outside positions.

## Inputs

Read root `me.md` and the owning Teaching `AGENTS.md` before applying course preferences.
For a direct invocation on resources outside the area directory, resolve that AGENTS
through the course note or Teaching MOC owner link; do not assume parent-directory
instructions identify the course owner or create another instruction file.

- Course offering, lecture version, file or deck, and the exact requested review or editing scope.
- Current Teaching `AGENTS.md` and course note for teaching preferences and material ownership.
- Supplied or instructor-approved references, relevant lecture materials, and any applicable decisions.
- Related quiz or exam items when consistency with an assessment is part of the request.
- Desired result: review in chat, proposed wording, edited material, teaching preparation, or simulation.
- The user's assigned slides, sections, or content owner when a deck is shared.

Use the existing source set. Ask only for a missing source or boundary that materially changes the work.

## Steps

1. **Define coverage.** Identify the current offering, deck version, lecture owner, and requested
   slides or sections. Separate a review of a shared deck from permission to edit it.
   Confirm the user's portion from available evidence before editing a shared presentation.
2. **Read the requested material.** Inspect slide text, figures, labels, tables, captions, and
   relevant speaker notes. Use visual inspection where meaning depends on a diagram or layout.
   Record inaccessible images, missing notes, or unreadable pages as coverage gaps.
   Do not declare a whole deck checked when only extracted text or a selected subset was available.
3. **Establish the content basis.** Read the supplied or instructor-approved references needed
   for the claims under review. Keep source locations available for each substantive correction.
   Distinguish the course's intended account from other plausible perspectives.
   Do not search for outside academic sources to decide what this course should teach unless the
   user explicitly expands the approved source set.
4. **Classify the findings.** Separate typos and mechanical errors, unclear wording or diagrams,
   internal inconsistencies, disagreement with an approved reference, and unresolved source conflicts.
   A claim absent from the supplied sources is unsupported by the reviewed set, not automatically false.
   Do not replace a contested claim by presenting general model knowledge as instructor approval.
5. **Check meaning and teaching use.** Confirm definitions, sequence, causality, labels, examples,
   and any stated limits against the approved sources. Check that figures and speaker notes agree
   with the visible slide and that simplified wording does not change the intended concept.
   Preserve deliberate terminology and pedagogical choices unless the request calls for alternatives.
6. **Check assessment consistency when requested.** Match lecture statements to the relevant item
   stem and answer text, not a shuffled question number alone.
   Flag contradictions between the lecture, supplied references, and expected answer.
   Hand ambiguity in the item or key to teaching-assessment rather than silently changing both.
7. **Propose or make the bounded correction.** For review, give the slide or section, issue,
   proposed wording, source basis, and any decision still needed.
   For authorized edits, make the smallest useful changes within the assigned scope and preserve
   the rest of the deck. Follow the course's original-file and revision conventions.
   Existing edit authorization is enough; do not add another approval checkpoint for routine fixes.
8. **Verify the result.** Use the appropriate document tools to render and inspect changed slides
   or pages and their surrounding context. Check diagrams, text fit, notes, links, and the retained
   content that the edit could affect. Apply any format-specific whole-document verification rules.
   Report what was actually inspected and distinguish a saved file from a published student copy.
9. **Prepare teaching support if requested.** Give likely student questions, short explanations,
   and examples grounded in the same approved material. Identify unresolved concepts before class.
   Hand authorized upload and student-visibility verification to teaching-platform with the exact
   revised artifact and destination. A local correction alone does not update every distributed copy.

## Outputs

- A review in the current task's requested form or under the recipient's existing reporting policy, with exact locations, proposed changes and source evidence. A separate saved report requires authorization.
- Separate definite mechanical fixes from content decisions needing instructor clarification.
  State the reviewed coverage and any inaccessible material.
- Deliver an edited file only within the requested scope, in the owning course folder or existing
  authorized target. Follow established file conventions. Do not add a review log or redundant hub. A separate report requires specific authorization and belongs to its proper owner.
- Return evidence, actions performed, verified/draft/unknown status, and remaining dependencies.
  Return teaching notes and explanations in the current task's requested form or under the recipient's existing reporting policy. Any additional saved artifact requires authorization and a verified destination.

## Boundaries

- Evaluate academic correctness only against supplied or instructor-approved references and decisions.
  Outside sources become part of the review only when the user authorizes that expansion.
- Flag conflicts among approved sources without silently choosing a preferred theory or perspective.
- Edit only the authorized slides or sections, including when a colleague owns the remaining deck.
- A request to inspect, explain, or simulate does not authorize changing a presentation or publishing it.
- Keep reusable skill instructions free of course-specific names, scientific answers, and personal style rules.

## Handoffs

- Accept direct requests or a bounded handoff from teaching-companion through teaching-coordinator.
  The companion remains the visible session owner when it initiated the work.
- Use the shared handoff: course offering, task, approved sources, authorization/review/simulation
  scope, and desired result. Return evidence, actions, verified/draft/unknown status, and dependencies.
- teaching-assessment owns item validity, expected answers, and assessment-side corrections.
- teaching-platform owns authorized uploads, replacement copies, and student access checks.
- teaching-office-hours owns requested class explanations and announcements about corrected materials.
- Return unresolved source or teaching decisions to the user; continue independent mechanical review.

## Checks

- The correct offering, version, and assigned section were reviewed; edit scope stayed intact.
- Each substantive correction has an approved source location or is clearly marked unresolved.
- No academic conclusion was imported from unapproved external material.
- Visual inspection supports claims about diagrams and formatting; inaccessible material is disclosed.
- Saved revisions and student-visible versions are reported as separate states.

## Modular Plugin Support

- Use configured presentation or document tools for reading, rendering, and authorized edits.
  Load the available format-specific skill before manipulating its supported file type.
- Use only the requested deck or files; apply the user's configuration to cloud edits and publishing.
  Route learning-platform delivery through teaching-platform.
- If editing or rendering tools are unavailable, complete the supported review and provide precise
  proposed changes. Do not claim visual verification or successful editing without evidence.
