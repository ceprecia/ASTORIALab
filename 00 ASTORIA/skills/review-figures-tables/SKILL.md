---
name: review-figures-tables
description: >-
  Reviews finished research figures and tables for APA presentation, readability
  and unnecessary complexity, returning practical corrections to their builders.
  Use for a final display review alongside verified research outputs; numerical
  provenance stays with verify-research-outputs. Triggers: check APA display
  formatting, review figure and table readability, simplify these research
  displays.
metadata:
  level: skill
  system: Research Assistant System
  part: "5"
  family: support
  modality: any
  population: ""
  dependencies: verify-research-outputs, write-figure-table-text
  requires: identified figures or tables with readable views
  gates: ""
  created: "2026-11-06"
  updated: "2026-11-06"
---

# Review Figures and Tables

Keep the simplest display that communicates the result accurately.

## Purpose

Review finished research figures and tables for APA presentation, readability
and unnecessary complexity. Return confusing or overengineered displays to
their builders with specific, practical corrections. Pass a clear display
without inventing cosmetic work. This is a final display review; numerical
provenance, scientific validity and artifact construction retain their owners.

## Inputs

Use the actual figure/table and version, its purpose and intended audience,
final placement size if known, analysis definitions, and any existing
`verify-research-outputs` return. Use the selected venue's instructions when
supplied; otherwise use APA 7 guidance and identify that basis. Ask only for
missing information that changes a required correction. Continue independent
checks when a source, export or placement size is unavailable.

Read the [APA guide](references/apa_guide.md) and
[worked examples](references/worked_examples.md) completely. Read the
[current-source contract](../research-output-coordinator/references/source_verification.md)
for requirement-dependent advice. Reuse current checks; verify a disputed rule
or changed venue/stage against the controlling official source. Distinguish
APA guidance, venue requirements and optional design suggestions.

## Steps

1. Identify the exact displays and requested review scope. Inspect rendered
   views, including titles, notes and every assigned panel or table page.
   Source code or an export setting alone does not establish visual quality.
2. Check the APA structure: number and italic title above; clear labels,
   units, headings, necessary legend and concise notes below. For tables,
   inspect organization, rules, alignment, precision and page continuation.
   Apply the reference guide without turning an optional design into a rule.
3. Check understanding at the intended size. Can the audience identify the
   quantity, comparison and uncertainty without decoding crowded algebra or
   repeated text? Flag tiny lettering, collisions, weak contrast, confusing
   order, redundant panels and overcomplicated encoding. Give the smallest
   useful repair. If placement size is unknown, qualify the size check rather
   than silently choosing a width.
4. Reconcile visible labels, units, counts, intervals, corrections, missingness
   and transformations with supplied definitions and verified outputs. Reuse
   existing verification instead of repeating its provenance audit. Send a
   suspected discrepancy to `verify-research-outputs` or the analyst. Preserve
   source values, planned positions, missing entries and exploratory status.
5. Return the outcome and necessary fixes. Each fix names its location, what
   prevents understanding or violates an applicable rule, the practical repair
   and its owner. Group repeated defects. Keep optional suggestions separate;
   do not require them for a pass.
6. After repair, inspect the revised display and affected dependencies. Close
   resolved items and return remaining problems to their owners. A change to
   values or definitions needs renewed output verification; an unchanged
   analysis does not need a rerun because the layout changed.

## Outputs

Follow the current request's reporting format and destination, then the applicable recipient policy. Identify the display and version in a short review.

- **Ready:** requested presentation checks passed; state what was checked.
- **Needs revision:** give only the necessary, actionable repairs.
- **Not fully checked:** name the missing evidence/view and include any known
  repairs. Continue the checks that are possible.

For each distinct problem, give its location, the practical repair and the responsible role.
State uninspected scope and numerical verification status when relevant.
Ready describes the inspected presentation; it does not certify scientific validity or unchecked numbers.
Save a review artifact only within authorized scope. Use the verified destination from the request or applicable recipient policy.

## Boundaries

- Keep review and feedback simple and practical. Do not use scores, cosmetic
  wish lists or compulsory redesign when a display already communicates well.
- Do not silently repair labels, back-transform contrasts, replace missing
  values with zero, force diagonals or alter scales to manufacture a finding.
  Shared limits apply to comparable panels, not every analysis family or level.
- Review and hand back corrections; artifact edits, caption drafting and
  analytical changes follow their own assigned scope and owners.

## Handoffs

Return to the invoking research owner. `verify-research-outputs` owns source
agreement and provenance; this skill owns final APA presentation and readability.
The figure/table builder repairs layout. `write-figure-table-text` repairs
captions and notes from established definitions. The integration editor owns
document-wide numbering and cross-references. `prepare-publication-package`
owns the selected venue's package and file checks. A reviewer return is a repair
assignment, not another approval request or a new team intake.

## Checks

- Were the actual assigned displays inspected at a stated size or qualified?
- Does each required fix have an observed problem, applicable basis and owner?
- Are missing evidence and unchecked numbers visible without blocking other checks?
- Can a clean display pass with no suggested changes?

## References

- American Psychological Association. (2021, December). *Figure setup*. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/figures
- American Psychological Association. (2021, December). *Table setup*. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables
- American Psychological Association. (2024, June). *Sample tables*. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/sample-tables
