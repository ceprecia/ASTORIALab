---
name: check-writing-substance
description: >-
  Independently checks writing for specific content, source traceability,
  unsupported additions, construct drift and claims that exceed available
  evidence. Use when fluent prose obscures missing substance; it diagnoses the
  missing facts without inventing repairs. Triggers: find empty fluent prose,
  check writing specificity.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: writing-coordinator
  created: "2026-11-01"
  updated: "2026-11-02"
---
# Check Writing Substance

Find sentences that sound finished while leaving the reader without content.

## Purpose

Independently check specificity, traceability, technical meaning and fidelity to
the assignment. Identify fluent but underspecified statements and invented
details as different problems. This is a dedicated review role, separate from
argument reasoning logic, citation identity, template fidelity and style filtering.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md).
Use the current brief, relevant MOC and recipient-supplied writing guidance, exact draft
version, intended audience, central claim and status, supplied sources,
specialist returns and the user's requested changes. Do not rely on a writer's
claim that it already fixed the passage.

## Steps

1. Recover what the passage must tell its reader. State the actual requested
   repair: a method, distinction, comparison, explanation, interpretation or
   rationale. Compare the returned passage directly with that request. First
   make a brief read-back from the draft alone: what was done or measured,
   what was found, and why it matters for the assigned question. Record what
   the intended reader cannot recover before using detailed sources. A fact
   can be clear in the source yet undefined in the draft; private reviewer
   knowledge must not fill that writing gap.
2. Extract its consequential propositions. Ask what each sentence contributes
   beyond announcing importance, complexity, rigor, innovation or integration.
   Flag phrases whose meaning disappears when their rhetorical emphasis is
   removed.
3. Test operational specificity where needed: who or what, which quantity,
   input, procedure, comparison, output, timing, units, decision rule or
   interpretation. Require only details necessary for this audience and job.
   When several metrics share units, check that their measured events, targets
   and interpretation are distinguishable. More numbers cannot substitute for
   explaining what those numbers measure.
4. Trace each factual or technical addition to the supplied sources or current
   user decisions. Distinguish a transparent proposed choice from an assertion
   that a choice has been made or a procedure completed.
   Check whether relevant descriptions elsewhere in the same source disagree.
   Inspect a linked table, footnote or protocol when it bears on the specific
   discrepancy; distinguish unavailable context from a verified conflict.
5. Check constructs and task definitions. Preserve distinctions such as concentration
   versus total amount, a model's predicted capacity versus measured throughput,
   and a completed validation check versus an adopted scientific conclusion.
6. Test claim scope: does the wording add causality, mechanism, generalization,
   prediction, successful validation or certainty beyond its source?
   Identify the exact extra inference without deciding the science.
7. Classify each finding using the most accurate description below. Quote the
   short problem span, explain what the reader cannot determine and identify
   the missing evidence or decision needed.
8. Suggest a concrete repair using verified content. If the content is absent,
   ask the precise missing-information question or return the affected clause
   as unresolved. Never supply plausible numbers, methods or mechanisms.
9. Review the revision against the original finding. Passing requires restored
   content or an explicit justified limitation, not a smoother paraphrase.

## Finding distinctions

| Finding | Meaning |
| --- | --- |
| Underspecified | The sentence may be true, but essential meaning or operations are absent |
| Unsupported addition | The draft adds a fact or choice absent from the supplied evidence |
| Contradicted | An inspected source or current decision conflicts with the statement |
| Conflicting source accounts | Relevant source passages or records disagree; preserve the disagreement rather than select whichever makes the draft complete |
| Unverified | Necessary source access or technical evidence is unavailable |
| Construct drift | Wording changes what a measure, condition, comparison or mechanism means |
| Explicitly provisional | A proposal is labeled honestly; the unresolved choice still needs an owner |

For example, “we will rank documents using term counts” needs the input,
ranking target, evaluation reference and interpretable success criterion
when those are the assignment. “An additional shared bias” needs the specific
distortion and its consequences. Neither phrase alone proves hallucination.

## Outputs

A short, prioritized list of location, problem, evidence/status, missing content
and exact repair question. Include sound passages when needed to distinguish
acceptable concision from missing substance. State review coverage and any
remaining source gaps.

## Boundaries

- Do not call every vague sentence a hallucination.
- Do not force exhaustive technical detail into every paragraph.
- Do not invent a repair to make the document look complete.
- Do not certify scientific validity or accepted QC; return such questions to
  the existing technical owner.
- Review independently from the drafting assignment where workers are available.

## Handoffs

Return to writing-coordinator. The domain owner supplies missing specifics
through [cross-system handoffs](../writing-coordinator/references/cross_system_handoff.md);
the relevant writer revises. check-writing-cerl is available when the recipient selects that named framework; otherwise use reasoning review suited to the task;
verify-writing-citations tests cited support; integrate-writing handles prose.

## Checks

- Each finding identifies an observable deficiency rather than a vague dislike.
- A proposed repair preserves the source's precision and uncertainty.
- Passing language answers the actual requested question.
- No missing input has been silently converted into an asserted fact.
