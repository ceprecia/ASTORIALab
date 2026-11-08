---
name: teaching-assessment
description: >-
  Designs and reviews college assessments, answer keys, and proposed rubrics
  against instructor-approved sources and lectures. Identifies ambiguity and
  hands delivery verification to the platform specialist. Triggers: review my
  exam questions, check my quiz answers, design a course assessment.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-20"
---

# Teaching Assessment

Check assessment content against approved teaching sources and verify the intended answer.

## Purpose

Design and review college quizzes, exams, answer keys, and proposed rubrics using the instructor's
approved materials. Check ambiguity, coverage, scoring logic, and agreement with lectures.
Keep content review separate from verification of the assessment actually delivered to students.

## Inputs

Read root `me.md` and the owning Teaching `AGENTS.md` before applying course preferences.
For a direct invocation on resources outside the area directory, resolve that AGENTS
through the course note or Teaching MOC owner link; do not assume parent-directory
instructions identify the course owner or create another instruction file.

- Course offering, assessment version, item bank or delivered copy, and requested subset or full scope.
- Current Teaching `AGENTS.md` and course note for assessment preferences and responsibilities.
- Supplied or instructor-approved references, lectures, syllabus requirements, and later decisions.
- Stems, every answer option, images, scoring rules, and the stored key when available.
- For design: learning objectives, content coverage, format, points, difficulty, and approved constraints.
- Requested result and authorization: review, proposed items, approved edits, delivery check, or simulation.

Retrieve discoverable details first; ask only when a missing source or decision changes the result.

## Steps

1. **Identify the assessment and its copies.** Confirm the offering, current version, and scope.
   Use an existing stable item ID where available. Otherwise identify each item by assessment plus
   a distinctive stem and answer text. Number and letter positions alone are unreliable when shuffled.
   Distinguish a shared bank item, an independent quiz copy, and an exam copy when evidence permits.
2. **Establish the approved content basis.** Read the supplied references and relevant lectures.
   Determine which current approved requirements apply to coverage, points, or question count.
   A previous exam's length is not a requirement for the next exam.
   Flag source conflicts and missing coverage instead of resolving them with unapproved outside sources.
3. **Derive the answer before consulting the key.** Answer from the stem, options, and approved
   sources first, recording the supporting location and reasoning. Then compare with the stored key.
   If the key was already visible, say so; do not claim the judgment was blind.
   Separate the source-supported answer, the stored answer, and an unresolved instructor decision.
4. **Test every option.** For each distractor, explain why it is wrong under the stem and approved
   material. Check whether another option is also defensible, whether none is fully correct, and
   whether a necessary assumption is unstated. Review NOT/EXCEPT wording, overlapping alternatives,
   absolute claims, double negatives, category errors, and differences in specificity.
   Apply the intended single-answer, multiple-answer, or partial-credit format explicitly.
   An option absent from the reference is unverified, not disproved. One supported option
   does not establish a unique answer when other options lack a source-based verdict.
   Do not certify replacement distractors until the approved material establishes why
   they are wrong under the revised stem; otherwise return that specific source gap.
5. **Inspect the whole item.** Read figures and labels visually when the answer depends on them.
   Check that images load, the stem describes the pictured case, and wording does not confuse
   preserved function with lost function or another consequential distinction.
   Mark inaccessible or ambiguous images unresolved rather than inferring their contents from filenames.
6. **Check lecture alignment and coverage.** Compare the correct answer and rationale with the
   approved lecture account. Identify contradictions among slides, references, and keys.
   For requested design work, draft items from the approved learning objectives and coverage plan.
   Offer proposed rubrics or scoring rules as proposals until approved; do not silently make policy.
7. **Prepare the smallest useful correction.** Preserve the intended concept and original structure
   where requested. Make distractors clearly wrong for substantive reasons and ensure the revised item
   still tests the objective. Re-evaluate every option after rewriting, not only the changed answer.
   Use item IDs and answer text in the correction so shuffling cannot redirect the edit.
8. **Check assessment-level settings within scope.** Reconcile count, point totals, weights, timing,
   attempts, due date, availability start/end, course timezone, feedback release, and applicable
   approved exceptions against the sources. Distinguish requirements from suggested improvements.
   Hand operational settings inspection to teaching-platform; do not infer them from a pasted question list.
9. **Verify the delivered copy.** After authorized edits, ask teaching-platform to check the actual
   quiz or exam, its stored key, images, and relevant student preview, plus affected bank copies.
   Verify whether copies are linked or independent before assuming propagation.
   A corrected question bank, saved file, or staff edit screen alone does not establish what students see.
   Use a supported preview or test route that does not create a student attempt or grade record.
10. **Handle corrections to used assessments explicitly.** Identify the affected item and scope.
    Separate a proposed correction, authorized key change, regrading decision, completed regrade,
    and student notification. Route approved score consequences to teaching-grader and communication
    to teaching-office-hours. Do not treat a promise to fix an item as completion of all those steps.

## Outputs

- Return a compact review in the current task's requested form or under the recipient's existing reporting policy, identifying each item by stable ID or distinctive stem.
  Give the source-supported answer text, stored-key comparison when available, evidence, and any issue.
- Present exact replacement wording for proposed fixes and mark instructor decisions still needed.
  State which items and sources were reviewed and which operational checks remain unknown.
- Save an item set, rubric or review file only when requested. Use the verified destination selected for the task. If none is selected, follow the applicable verified recipient or course placement policy. If neither resolves the destination, use the verified owning course folder.
  Do not build a second question bank, assessment database, or persistent issue queue.
- Return evidence, actions performed, verified/draft/unknown status, and remaining dependencies.
  Content correctness, saved edits, and delivery verification have separate outcomes.

## Boundaries

- Judge academic correctness only from supplied or instructor-approved material.
  Unsupported by the reviewed set is different from false; flag conflicts instead of inventing certainty.
- Do not browse for outside academic answers unless the user explicitly expands the approved sources.
- Do not assume numbered questions or option letters are stable across copies or students.
- Review or design requests authorize reviewable work, not publication, changed grades, or new policy.
  Follow the user's actual authorization for edits and the course's review requirements.
- Preserve instructor decisions about content, difficulty, and scoring unless changes are requested.

## Handoffs

- Accept direct requests or a bounded handoff from teaching-companion through teaching-coordinator.
  The companion remains the visible session owner when it initiated the work.
- Use the shared handoff: course offering, task, approved sources, authorization/review/simulation
  scope, and desired result. Return evidence, actions, verified/draft/unknown status, and dependencies.
- teaching-lecture-review owns lecture-side corrections within the authorized teaching portion.
- teaching-platform owns authorized item/settings edits and verification of the delivered assessment.
- teaching-grader owns applying approved regrades; teaching-office-hours owns correction messages.
- Return unresolved source conflicts or policy decisions to the user while completing independent items.

## Checks

- Source-based answer was formed before the key comparison, or prior key visibility was disclosed.
- Every option was checked; the answer count and scoring format are unambiguous.
- Item identity survives shuffling, and affected bank versus delivered copies are distinguished.
- Requirements about length, points, and timing come from current applicable approved sources.
- Content and delivery claims match the actual coverage and evidence; unresolved dependencies are named.

## Modular Plugin Support

- Use configured document tools for item files and approved sources, loading the relevant format skill.
  Use configured platform tools through teaching-platform for authorized changes and previews.
- Apply the user's configured write and review permissions; simulation stays within its stated scope.
- Without platform access, finish the source-based review and exact proposed changes, and leave
  bank propagation, saved settings, student visibility, and scoring behavior explicitly unverified.
