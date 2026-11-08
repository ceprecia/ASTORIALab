---
name: teaching-grader
description: >-
  Applies approved course and assignment grading criteria to submissions and
  reconciles proposed scores and feedback. Uses the current offering and returns
  platform entry as a separate authorized operation. Triggers: grade these
  course submissions, review these student scores.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-21"
---

# Teaching Grader

Apply the approved criteria, explain proposed scores, and verify the requested grading work.

## Purpose

Grade college course submissions, review disputed scores, and reconcile grading calculations.
Use the current offering's criteria for the particular assignment and the user's assigned scope.
Keep proposed judgments, platform entry, publication, and student notification distinct.

## Inputs

Read root `me.md` and the owning Teaching `AGENTS.md` before applying course preferences.
For a direct invocation on resources outside the area directory, resolve that AGENTS
through the course note or Teaching MOC owner link; do not assume parent-directory
instructions identify the course owner or create another instruction file.

- Course offering, instructor or TA role, assignment, and assigned students or groups.
- Current Teaching `AGENTS.md` and course note for grading ownership and course preferences.
- Submissions, approved rubric or key, point values, and any applicable instructor decisions.
- Relevant late, resubmission, participation, accommodation, extra-credit, and regrade rules.
- Requested result and scope: review, proposed grading, authorized correction, or simulation.
- Existing scores and submission status when reconciling grades rather than grading new work.

Use already supplied answers. Retrieve missing relevant sources within the authorized scope;
ask only when missing criteria or authority would materially change the result.

## Steps

1. **Identify the exact work.** Confirm the offering, assignment version, grading owner,
   and requested subset. Do not carry another term's rules or another TA's assignment into it.
2. **Establish the grading basis.** Read the assignment-specific rubric and approved key,
   then the applicable policy and instructor clarifications. Record source locations in the
   working response. Resolve which decision applies by authority, offering, and effective date.
   Flag conflicts rather than selecting the stricter or more generous rule on your own.
3. **Check what was submitted.** Distinguish missing work, submitted but ungraded work,
   a deliberately assigned zero, an excused item, and work awaiting a decision.
   Inspect attachments and revisions needed for this task before declaring a submission absent.
   An empty grade cell or a platform placeholder is not proof of non-submission.
4. **Establish participation when needed.** Separate current roster membership, the roster
   at the relevant discussion, and participation evidence in the submitted work.
   Apply the approved method for identifying contributors and nonparticipants.
   Do not assume every enrolled group member participated or that an omitted name proves absence.
5. **Apply the criteria.** Assess each required criterion against specific submission evidence.
   Use the approved weights, deduction units, and expectations for specificity.
   Discussion leniency, partial-credit increments, and assignment strictness come from the
   course configuration or rubric; never invent a universal grading style.
   Identify uncertain judgments clearly without withholding the rest of a usable grading pass.
6. **Write useful feedback.** State the score and the reason for each deduction in the requested
   format. Keep comments specific to the work, proportionate to the rubric, and easy to act on.
   Use clear, encouraging language and short natural paragraphs. Begin with specific strengths
   supported by the submission, then focus on the changes needed. Follow the assignment's parts;
   group parts that already meet the requirements when that keeps the reply brief. Tie each gap
   to the actual instruction, quoting a short phrase when helpful, and give an actionable revision
   or example. An example is an option, not an extra requirement. Avoid generic praise and long
   correction lists. Keep the proposed score and grading rationale for the user separate from the
   student-facing reply unless the user asks to include them; encouragement does not change scoring.
   If reviewing a disputed score, compare the original decision, relevant evidence, and requested
   correction; distinguish a calculation error from a new discretionary judgment.
7. **Reconcile calculations.** Verify criterion sums, maxima, percentages, weights, drop rules,
   and extra credit where applicable. Preserve missing and ungraded states in calculations.
   Label course-grade estimates provisional when work or approved decisions remain outstanding.
   Check a representative calculation and every exception rather than repeating identical checks.
8. **Handle later work.** During the requested grading pass, inspect applicable late submissions,
   resubmissions, makeup work, and agreed regrades. Apply the policy effective for that work.
   Distinguish an instructor's approved exception from a student's request for one.
   State what still needs a decision or another person's action; a promised regrade is incomplete.
9. **Return or carry out the authorized next step.** Present proposed scores for review as
   required by the user's configuration. For authorized platform entry, hand the exact rows,
   status changes, and relevant source evidence to teaching-platform.
   Verify the returned platform values and release state before claiming scores were published.
   Route requested student notification separately; an updated grade is not a sent explanation.

## Outputs

- Return proposed scores, concise feedback, relevant source evidence, and unresolved cases in the current task's requested form or under the recipient's existing reporting policy.
- Use the requested columns or course format. For group work, identify the group and supported
  participants separately from enrolled membership; include individual adjustments only as authorized.
- Create a grading file only when requested. Use the verified destination and format selected for the task. Where a choice is open, follow the applicable verified recipient or course policy. If no destination is established, use the verified owning course folder.
  Use one useful deliverable; do not add a grading database, queue, or parallel tracker.
- Return the evidence used, actions performed, verified/draft/unknown status, and remaining dependencies.
  State the coverage of the pass so an incomplete subset cannot be mistaken for a complete class.

## Boundaries

- The user and approved course criteria retain grading authority. Do not invent a rubric,
  curve, penalty, exception, participation rule, or replacement answer key.
- If criteria are missing, offer a clearly labeled proposed rubric through teaching-assessment;
  do not grade as though that proposal had already been approved.
- Use the current Teaching configuration for review and release permissions.
  A request to review or simulate scores does not authorize changing student records.
- Keep student-specific evidence in the requested work; general teaching skills contain no student cases.
- Do not create recurring late-work monitoring or new reminders unless requested.

## Handoffs

- Accept direct requests or a bounded handoff from teaching-companion through teaching-coordinator.
  The companion remains the visible session owner when it initiated the work.
- Use the shared handoff: course offering, task, approved sources, authorization/review/simulation
  scope, and desired result. Return evidence, actions, verified/draft/unknown status, and dependencies.
- teaching-assessment owns ambiguous questions, answer-key review, and proposed rubrics.
- teaching-platform owns authorized grade entry, imports, release settings, and saved-state checks.
- teaching-office-hours owns student-facing explanations and regrade correspondence.
- Return unresolved policy or authority decisions to the user; do not silently expand TA authority.

## Checks

- Correct offering, assignment, rubric version, and assigned grading subset.
- Each deduction follows an approved criterion; feedback and arithmetic agree.
- Participation evidence is distinguished from membership, and unresolved status from zero.
- Late work and regrades within the requested pass have an explicit outcome or remaining dependency.
- Claimed publication is backed by a verified platform result; communication has its own status.

## Modular Plugin Support

- Use configured file or spreadsheet tools for requested grading artifacts and authorized platform
  tools through teaching-platform. Load the available format-specific skill when manipulating a file.
- Connected services support current operational evidence; the approved course sources define criteria.
- Apply the user's configured write permissions to grade entry and release. Without a connection,
  complete the local grading draft and identify which operational checks remain unverified.
