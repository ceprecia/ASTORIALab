---
name: teaching-lecture-review
description: >-
  Plans and reviews college teaching materials using approved sources,
  learning outcomes, current assessment targets and section learning checks.
  Makes requested revisions within the assigned lecture scope. Triggers:
  check my lecture slides, review my teaching materials.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: teaching-assessment
  created: "2026-10-20"
  updated: "2026-11-18"
---

# Teaching Lecture Review

Plan clear instruction, check student understanding, and preserve approved course content.

## Purpose

Review college lectures, slides, handouts, and related teaching materials for mechanical errors,
clarity, and agreement with supplied or instructor-approved content.
Own the instructional plan for new lectures and substantial teaching revisions, with
assessment alignment and student learning checks on by default.
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
- For lecture planning: required learning outcomes, audience knowledge, class time,
  relevant current quiz/exam items or assessment targets, and supplied reference lectures.
  Use available assessments by default; distinguish unavailable current items from old banks.
- Desired result: review in chat, proposed wording, edited material, teaching preparation, or simulation.
- The user's assigned slides, sections, or content owner when a deck is shared.

Use the existing source set. Ask only for a missing source or boundary that materially changes the work.

## Steps

1. **Define coverage.** Identify the current offering, deck version, lecture owner, and requested
   slides or sections. Separate a review of a shared deck from permission to edit it.
   Confirm the user's portion from available evidence before editing a shared presentation.
   Distinguish lecture planning or a full instructional review from a bounded correction.
   The learning-design defaults below apply to new lectures and substantial instructional
   revisions; a full instructional review checks for them without expanding edit authority.
2. **Read the requested material.** Inspect slide text, figures, labels, tables, captions, and
   relevant speaker notes. Use visual inspection where meaning depends on a diagram or layout.
   Record inaccessible images, missing notes, or unreadable pages as coverage gaps.
   Do not declare a whole deck checked when only extracted text or a selected subset was available.
   Read a supplied reference lecture for its teaching method as well as its visual style,
   including its actual speaker notes, question formats, worked examples, response
   opportunities and feedback. Respect the requested slide range. If only a PDF is
   available, mark note style unverified rather than inventing it.
3. **Establish the content basis.** Read the supplied or instructor-approved references needed
   for the claims under review. Keep source locations available for each substantive correction.
   Distinguish the course's intended account from other plausible perspectives.
   Do not search for outside academic sources to decide what this course should teach unless the
   user explicitly expands the approved source set.
   Before outlining a new lecture or substantial instructional revision, map required
   outcomes to relevant current assessment concepts and reasoning demands, approved source
   locations, explanations/examples and learning checks. Borrow teaching-assessment for
   this bounded map and questionable items. Prioritize emphasis and practice from those
   targets while retaining required coverage and explicitly preserved material. If current
   assessments are unavailable, continue from approved outcomes and sources and mark
   assessment alignment unverified; old banks remain historical evidence.
4. **Classify the findings.** Separate typos and mechanical errors, unclear wording or diagrams,
   internal inconsistencies, disagreement with an approved reference, and unresolved source conflicts.
   A claim absent from the supplied sources is unsupported by the reviewed set, not automatically false.
   Do not replace a contested claim by presenting general model knowledge as instructor approval.
5. **Check meaning and teaching use.** Confirm definitions, sequence, causality, labels, examples,
   and any stated limits against the approved sources. Check that figures and speaker notes agree
   with the visible slide and that simplified wording does not change the intended concept.
   Preserve deliberate terminology and pedagogical choices unless the request calls for alternatives.
   Include a brief student learning check after each major conceptual section by default.
   Choose recall, prediction, application or figure interpretation to match the intended
   outcome and assessment demand. Specify the question, student response method, supported
   answer and reasoning, likely misconception, explanatory feedback and response/debrief time.
   This is a private planning brief, not a template to paste into speaker notes.
   Let students commit to an answer before its reveal; keep the initial question display
   free of answer marks and give the presenter an answer, rationale and reveal cue.
   Default to one simple question slide, usually a clear A–D application or distinction.
   Give its answer and short explanation in the same slide's notes for oral feedback;
   an optional same-slide reveal also fits. Add separate answer/review slides only when
   the user requests a multi-slide check; explanatory feedback alone is not a reason to split it.
   Distinguish this response/feedback cycle from rhetorical questions, presenter-only
   prompts and final Q&A. Preserve planned checks and reference-lecture pedagogy unless
   the user requests a change. Fit interaction time into the class schedule.
   Prepare explanations in a Feynman style: a familiar case, plain mechanism, necessary
   terminology and a useful takeaway. Repair jargon, missing steps and misleading analogy
   mappings. Notes should give the explanation in natural spoken language, with only
   useful brief presenter cues. Keep bibliographies, source/version audits, agent workflow
   and repeated clock schedules outside notes. Keep audience source captions unobtrusive
   and separate from the narration; retain private source checking and uncertainty.
6. **Check assessment consistency.** For lecture planning and substantial instructional
   revisions, this check is on by default; for bounded work, use only the relevant items.
   Match lecture statements to the relevant item stem and answer text, not a shuffled position.
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
   For instructional work, verify the outcome/assessment map, major-section checks,
   student response opportunities, answer/reveal cues and feedback in the exported artifact.
   Check that interaction time fits and retained course coverage remains present.
   Compare actual note passages and check slides against the supplied exemplar. Verify
   that notes explain rather than merely direct someone to explain; one-slide checks
   retain their answer/rationale in the notes. Empty notes are fine when nothing is needed.
9. **Prepare teaching support if requested.** Give likely student questions, short explanations,
   and examples grounded in the same approved material. Identify unresolved concepts before class.
   Hand authorized upload and student-visibility verification to teaching-platform with the exact
   revised artifact and destination. A local correction alone does not update every distributed copy.

## Outputs

- A review in the current task's requested form or under the recipient's existing reporting policy, with exact locations, proposed changes and source evidence. A separate saved report requires authorization.
- For lecture planning: a compact outcome/assessment/source map, instructional sequence,
  emphasis priorities and section checks with answers, feedback and timings. Keep staff
  assessment identifiers and keys in private working context; student-facing practice
  follows teaching-assessment's reuse rules. No separate planning file is required.
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
- Keep typo, citation and other bounded corrections within scope; the lecture-design default
  does not automatically add questions, change timings or rebuild those artifacts.
- A request to inspect, explain, or simulate does not authorize changing a presentation or publishing it.
- Keep reusable skill instructions free of course-specific names, scientific answers, and personal style rules.

## Handoffs

- Accept direct requests or a bounded handoff from teaching-companion through teaching-coordinator.
  The companion remains the visible session owner when it initiated the work.
- Use the shared handoff: course offering, task, approved sources, authorization/review/simulation
  scope, and desired result. Return evidence, actions, verified/draft/unknown status, and dependencies.
- teaching-assessment owns item validity, source-supported answers and the bounded
  assessment-to-instruction map. This skill owns the resulting teaching sequence and checks.
- Pass outcomes, assessment emphasis, source locations, section checks, answers/reveal cues,
  feedback, timings and preserved content to research-presentation-builder or the selected
  artifact capability. Public-speaking-coach rehearses that teaching plan when requested.
  Label source maps and timing plans as working context. Pass the user's note style and
  citation placement explicitly so the production tool does not dump that context into notes.
- teaching-platform owns authorized uploads, replacement copies, and student access checks.
- teaching-office-hours owns requested class explanations and announcements about corrected materials.
- Return unresolved source or teaching decisions to the user; continue independent mechanical review.

## Checks

- The correct offering, version, and assigned section were reviewed; edit scope stayed intact.
- Each substantive correction has an approved source location or is clearly marked unresolved.
- New/substantially revised lectures use current assessment evidence when available, preserve
  required outcomes and include purposeful checks after major sections with response and feedback.
- The exported artifact retains the planned checks and answer/reveal cues, with interaction
  time included; rendering success alone does not establish instructional readiness.
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
