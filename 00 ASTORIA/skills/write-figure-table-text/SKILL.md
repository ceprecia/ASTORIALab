---
name: write-figure-table-text
description: 'Drafts or revises figure legends, table notes, and associated display
  text from the actual artifact and analysis definitions. Use for self-contained display
  explanations; it does not redraw figures, compute results, or guess missing annotations.
  Triggers: draft figure captions, write table notes.'
metadata:
  level: skill
  system: Capture and Writing Helpers
  created: '2026-11-01'
  updated: '2026-11-06'
---
# Write Figure and Table Text

Let readers understand the display and its evidence without guessing its definitions.

## Purpose

Draft or revise figure legends/captions, table titles/notes, panel labels and
associated explanatory text from an actual display. Make the artifact
interpretable on its own while preserving the exact results, definitions and
analysis status. Figure design and statistical execution remain with their owners.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md)
completely. Use the [cross-system handoff](../writing-coordinator/references/cross_system_handoff.md)
when domain-specialist material or requirements are involved.

Read the relevant MOC by the default in `me.md`, then the sections needed for
this assignment. Read any recipient-supplied writing guidance identified in the brief. If none is supplied, use the document-purpose and evidence requirements and the actual task sources. Writing preferences are not evidence for the project's scientific claims.

Recover the current writing brief: exact document/version, audience, section
purpose, central argument and its provisional or adopted status, any recipient-selected organizational requirements,
source locators, protected terminology, claim ceiling, required structure and
length, and authorized edits. Apply only a writing profile selected for this task or in the recipient's `me.md`. The available references include `writing-style-positive-scientific` and `writing-style-negative-ai`. Apply each independently when selected. Ask only for missing information that changes the
requested wording; continue unaffected work without inventing an answer.

Inspect the current figure or table, including visible panels, axes, units,
row/column headings, symbols and annotations. Use its source data/analysis
summary and plotting/table definitions where needed. Obtain definitions of
sample/unit, summary statistics, error bands, tests, corrections, transformations
and exclusions from the relevant owner; appearance alone cannot establish them.

## Steps

1. Identify the exact artifact/version and its intended contribution to the
   document. Check whether the assigned text is a legend, table note, label,
   display title or nearby prose. Do not recreate or alter the artifact itself
   as part of a text-only assignment.
2. Inventory what the display actually shows: panels, conditions/comparisons,
   plotted quantities, units, scales, sample units, grouping and annotations.
   Identify missing definitions before writing; do not infer a standard error,
   confidence interval, statistical test or sample count from visual convention.
3. Draft a concise orientation explaining the display's subject. Use a neutral
   descriptive opening or a supported result takeaway as the brief/venue allows.
   Do not add an explanatory mechanism or broader interpretation absent from
   the approved result and central argument.
4. For figures, explain panels in their actual order and identify the plotted
   quantities, encoding, summary/uncertainty, relevant sample and necessary
   transformations or exclusions. Define statistical annotations and the
   associated comparison/test/correction from supplied evidence. Distinguish
   representative examples from group summaries.
5. For tables, write a precise title and notes that define abbreviations,
   symbols, units, models, summary statistics, samples/denominators, adjustments
   and statistical annotations as relevant. Clarify whether entries are raw,
   normalized, descriptive, model-estimated or contrasts. Do not repeat every cell.
6. For labels or short display text, preserve exact construct and condition names.
   Compress explanatory wording without changing the quantity or reference frame.
   Use parallel labels where the underlying quantities are actually comparable.
7. Use the selected caption, legend or table-note format to explain what the reader needs to interpret the display. Preserve the actual quantities, definitions and relevant limits. Choose an information order appropriate to the artifact without requiring argumentative paragraph components.
8. Reconcile text with the actual image/table and Results. Check panel letters,
   direction, values, sample units, intervals, symbols and analysis status.
   Return inconsistencies to the plot/analysis owner instead of silently changing
   the prose to rationalize a mismatched artifact.
9. Read the text without the surrounding manuscript. Retain the information
   needed to understand the display but move unnecessary full methods or
   Discussion prose back to their appropriate owners. Check length/style constraints.

## Outputs

Return the requested legend, caption, table notes or labels, identified by the
actual figure/table and version. Include only consequential missing definitions
or artifact-text inconsistencies. Keep the canonical artifact/document with
its assigned owner; no invented statistical note fills an unknown.

## Boundaries

- Do not compute results, draw a new figure or infer unseen underlying data.
- Do not invent an error-bar definition, statistical test, significance rule,
  sample size, correction, preprocessing choice or abbreviation expansion.
- Preserve supplied quantitative values, condition names and annotation meanings.
- Different sample denominators or scales must remain visible when they matter.

## Handoffs

Use the cross-system handoff for display/analysis definitions or fidelity
questions. Return text to the invoking writing owner and pass artifact mismatches
to the actual builder/analyst. The integration editor reconciles numbering and
cross-references; independent substance/structure reviewers retain their checks.

Use `review-figures-tables` for the requested final APA/readability pass on the
rendered display with its text. Pass exact versions and definitions. Revise
caption/note wording from its concrete feedback; layout stays with the builder
and disputed quantities return to `verify-research-outputs`.

## Checks

- Does the text describe the actual artifact and correct panels/columns?
- Can a reader identify the quantity, units, sample and summary/uncertainty?
- Are all necessary symbols and statistical annotations defined from evidence?
- Do the legend/table notes agree with Results and the underlying definitions?
- Is the local takeaway bounded and distinct from an untested interpretation?
