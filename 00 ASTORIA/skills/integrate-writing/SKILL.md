---
name: integrate-writing
description: >-
  Integrates bounded section drafts into one coherent document while preserving
  argument, scientific meaning, terminology and authorial voice. Use for
  document-level synthesis and final prose editing; it does not replace
  independent citation, substance, argument reasoning or technical review. Triggers: integrate
  these section drafts, reconcile document wording.
metadata:
  level: skill
  system: Writing System
  dependencies: writing-coordinator
  created: "2026-11-01"
  updated: "2026-11-18"
---
# Integrate Writing

Bring specialist drafts together while preserving the reasoning and details.

## Purpose

Own one canonical document's prose integration, coherence, transitions,
terminology and authorial voice. Combine bounded section returns after
appropriate technical and writing reviews. This is editing and synthesis, not
a substitute for the separate citation, substance, argument reasoning or structure reviewers.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md)
and use its task-sized context. Use the canonical document/version, assigned
section returns, selected structure, source locators, protected text and review
findings. Include the central claim and its status for argument-bearing material.
Read MOC or recipient-supplied writing guidance when it supplies needed context. Identify
the sole editor of the canonical artifact. A bounded integration request may
return directly to its caller without another lead or team.

## Steps

1. Verify each return belongs to the current assignment and document version.
   Compare overlaps and contradictions before merging. Preserve provenance for
   proposed variants without treating them as adopted text.
2. Build a section-level reverse outline: each section's job, controlling
   message and relation to the whole. Restore missing connections before
   polishing individual sentences.
3. Merge only authorized content into the canonical document. Reconcile
   duplicate passages by retaining the best-supported necessary detail;
   do not compress away units, operational steps, uncertainty or qualifications.
4. Harmonize exact terminology, definitions, condition labels, tense, notation,
   abbreviations, cross-references and citation form. If two terms imply
   different constructs, return the conflict to the owner rather than choosing
   the smoother synonym.
5. Check transitions for their actual relation: continuation, contrast,
   consequence, qualification or a new question. Remove transition words that
   disguise an unsupported jump.
   For a link between sources, identify what the combined evidence actually
   establishes. A study of varied workflows does not isolate one component's
   effect merely because the preceding paragraph described that component.
   Distinguish evidence that motivates a proposed test from evidence that
   directly answers it; adjacent accurate statements can imply an unsupported
   causal or mechanistic connection after integration.
6. Read for voice and proportion. Replace empty emphasis with the supported
   specific point, remove redundant announcements and ensure paragraphs do
   distinct work. Preserve technical language when precision requires it.
7. Check document-wide consistency among title, abstract, aims, methods,
   results, interpretation, figures and conclusion as applicable.
   A changed method or outcome must not remain stale elsewhere.
8. Route consequential new claims, changed technical descriptions or changed
   citation relationships back to the relevant independent reviewer. Review
   the stable merged version; reuse unaffected findings and rerun affected
   checks after subsequent content changes.
9. Apply the formal-prose profiles required by `me.md` to the final integrated
   text. Follow their complete final review procedure after all merges and
   revisions; a lexical style pass does not establish substance or accuracy.
10. Verify the requested artifact with its document capability when layout
    matters. Return the integrated draft and only material unresolved questions
    or changes that need the user's scientific judgment.

## Outputs

Return one integrated draft. Write to the existing canonical destination only
when the current edit is authorized. Otherwise return the draft in the current task's requested response form or under the recipient's existing reporting policy, including clean paste-ready text when requested.
Provide a brief account of consequential changes and remaining gaps when needed.
Do not produce a second canonical document or unsolicited review files.

## Boundaries

- Exactly one worker modifies a canonical mutable document at a time.
- Do not silently settle competing interpretations or provisional aims.
- Do not trade reproducibility detail for a better readability score.
- Preserve quotations, mandated wording, statistics and protected terms under
  the applicable writing contract.
- Do not claim independent review of a passage solely because its author
  performed a self-check.

## Handoffs

Return the integrated draft to the invoking owner, through writing-coordinator
when it is already coordinating the task.
Use the relevant content writer for substantial section redevelopment.
Technical fidelity follows
[cross-system handoffs](../writing-coordinator/references/cross_system_handoff.md).
check-writing-substance, verify-writing-citations and keep-writing-structure retain their independent review jobs. Add check-writing-cerl only for a recipient-selected named paragraph framework.

## Checks

- The current central claim and section purposes remain connected.
- No merge introduces unsupported details, construct drift or stale terminology.
- Each material review finding is resolved or visibly outstanding.
- Final prose and artifact checks concern the actual returned version.
