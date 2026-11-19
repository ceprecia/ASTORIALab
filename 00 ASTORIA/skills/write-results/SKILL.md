---
name: write-results
description: 'Drafts or revises Results from actual analysis outputs, linking each
  result to its question while preserving estimates, uncertainty, and analysis status.
  Use for results prose; it does not run analyses or manufacture a supported outcome.
  Triggers: draft results prose, narrate these analysis outputs.'
metadata:
  level: skill
  system: Writing System
  created: '2026-11-01'
  updated: '2026-11-18'
---
# Write Results

Make the evidence and its boundaries visible without changing the analysis.

## Purpose

Draft or revise Results from actual outputs and an established analysis frame.
Connect findings to their questions and comparisons, while keeping interpretive
or mechanistic argument with its appropriate section and domain owner.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md)
and use its task-sized context. A clear bounded request can supply the brief
without loading Writing Companion or Writing Coordinator. Use the exact passage
or artifact, its purpose, source records, relevant definitions, constraints and
authorized edits. Carry the central claim and its status when this passage needs
that argument. Read MOC or recipient-supplied writing guidance only when needed context is
not already available, following the MOC reading policy in `me.md`.

Use the [cross-system handoff](../writing-coordinator/references/cross_system_handoff.md)
for missing domain detail or fidelity questions. Apply only a writing profile selected for this task or in the recipient's `me.md`, and only to prose being produced or revised. The available references include `writing-style-positive-scientific` and `writing-style-negative-ai`. Apply each independently when selected. Preserve source records and
frozen text. Ask only for missing information that changes the requested result
and continue independent supported work.

Read the actual approved output tables, figures, model summaries or specialist
returns that support the result statements. Obtain sample/unit definitions,
condition labels, contrast direction, estimates, uncertainty and statistical
reporting conventions. Recover which analyses were planned, secondary,
exploratory or changed; do not infer their status from presentation order.

## Steps

1. Map each requested result to its question, analysis and exact output locator.
   Match the current version, participant/trial/unit scope, conditions and
   exclusions. If the evidence is missing, request it; do not reconstruct a
   numerical finding from an aim, expectation or previous summary.
2. Choose a result sequence that lets the reader follow the current questions
   and analyses. Include the relevant preregistered or otherwise required
   outcomes even when they do not support the preferred narrative. Do not
   silently remove a null, conflicting, failed or inconclusive result.
3. Use the selected reporting format to present the actual results with the estimates, uncertainty, comparisons and scope needed to understand them. Choose passage structure for the reported material. Do not import explanatory mechanisms or Discussion-level significance into Results.
4. Define what the reported quantity measures before attaching its values:
   the relevant input/output or observed event, reference or target, and
   direction or interpretation of the metric. Similar units do not make
   measures interchangeable: response latency differs from duration error,
   and uncertainty about a mean differs from variability among observations.
   Keep this meaning in the prose, not only in private source notes.
   For a proportion or overlap score, identify what is counted in the numerator
   and denominator when the conclusion depends on that distinction. A label
   such as similarity or agreement plus a numeric range is not a definition.
   Preserve the operation when compressing: the reader should know what a
   higher value means without reconstructing the metric from the source.
   State the actual comparison and direction with supplied labels. Report
   estimates/effect sizes and their uncertainty when available, and the
   applicable test/model quantities. Preserve denominators, degrees of freedom,
   intervals, units and exact statistical values or the requested rounding rule.
   If a needed quantity is absent, ask the analysis owner rather than derive
   a new result under the guise of writing.
5. Distinguish statistical evidence, effect magnitude, uncertainty, descriptive
   differences and model performance. A nonsignificant result is not evidence
   of absence; describe absence/equivalence claims only when the analysis owner
   supplies the appropriate supporting analysis and bounds. Do not soften a
   nonsignificant test into marginal, near-significant or a supported trend.
6. Keep prediction target, evaluation partition, metric and baseline explicit
   where relevant. Do not report fitting performance as generalization or a
   successful decoder as proof of the computation or origin of a signal.
7. Match prose to displays. Identify the figure/table that contains the result
   without repeating every cell. Under a tight word limit retain the metric
   definition, result takeaway and material scope conditions before adding
   extra numeric or setup detail. Separate descriptive and adjusted/model-based
   quantities, and distinguish participant counts from observations or trials.
8. Check confirmatory/exploratory status, deviations and missing-data/exclusion
   statements against the current analysis record. A new presentation order
   cannot retrospectively change the status of a decision.
9. Audit each sentence against its actual output. Simplify overloaded sentences
   while preserving technical meaning, uncertainty and inconvenient evidence.
   Return a conflict to the analysis owner rather than choosing which number
   or analysis should be treated as authoritative.

## Outputs

Return Results prose and only consequential missing outputs or inconsistencies.
Maintain source-to-statement locators in the team return when needed for
independent verification. Do not append invented values or a fabricated completed
analysis to a requested scaffold. Save only within the assigned output ownership.

## Boundaries

- Do not run or change analyses, thresholds, exclusions or models to improve the prose.
- Do not infer an interaction from different significance labels, or evidence of
  sameness from one nonsignificant test.
- Do not report predictions as observed results or group descriptions as causal effects.
- Avoid selective summaries that misrepresent the complete supplied result set.
- Substantive interpretation belongs to the user/domain owner and the relevant writer.

## Handoffs

Return to the invoking owner. Missing outputs and scientific/statistical
conflicts go through the cross-system handoff to the actual analysis owner.
Send the result text and its limits to an assigned Discussion writer through an
already active coordinator. Independent substance review checks traceability
when assigned.

## Checks

- Does every result statement have an accessible matching output?
- Are comparison labels, direction, sample units, values and uncertainty accurate?
- Can the intended reader say what each important number measures from the
  passage itself, without borrowing definitions from the reviewer’s source notes?
- Are required negative and conflicting outcomes represented?
- Are evaluation performance and inferential status described correctly?
- Can the reader distinguish what was observed from what it might mean?
