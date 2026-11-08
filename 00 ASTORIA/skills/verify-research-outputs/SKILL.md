---
name: verify-research-outputs
description: 'Traces reported numbers, figures, tables and files to identified analysis
  outputs and provenance, identifying inconsistencies and version mismatches. Checks
  traceability and agreement without deciding scientific validity. Triggers: trace
  these reported results, check manuscript output consistency.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: identified document/output versions and accessible analysis provenance
  created: '2026-11-02'
  updated: '2026-11-06'
  gates: ''
---
# Verify Research Outputs

Trace each reported result to the exact outputs and records that support it.

## Purpose

Check one bounded document/output set for agreement between reported numbers,
figures, tables, files and identified analysis records. Combine provenance tracing
with consistency checking. Establish where a reported result came from and whether
its presentation agrees with that source; scientific inference validity remains
with the user and the appropriate analysis or critique owner.

## Inputs

Read the [current-source contract](../research-output-coordinator/references/source_verification.md).
Use the invoking owner's question, current scientific frame and provisional
status, exact document/output versions, requested targets, analysis records,
source locations, definitions and available code/configuration/data identifiers.
Identify whether the audit covers a passage, selected results or an entire output
set. Ask only for information that prevents the requested comparison.

## Steps

1. Freeze the comparison scope in conversation: identify each document version,
   figure/table/panel or reported quantity and the proposed authoritative source.
   A filename such as `final` does not establish authority. Preserve unresolved
   source disagreements rather than selecting a convenient version.
2. Inspect the actual supplied outputs and relevant records. For each target,
   trace the input data version, code revision, configuration, processing step,
   analysis output and presentation transformation as far as available evidence
   permits. Distinguish a recorded lineage from an inferred one.
3. Build only the provenance chain needed for the requested targets. Note
   inaccessible data, missing intermediate records, undocumented manual steps,
   ambiguous run identifiers and outputs whose generating code cannot be found.
   Do not reconstruct scientific history from directory names or file dates alone.
4. Compare actual values and meanings: units, denominators, sample/trial counts,
   exclusions, outcome definitions, condition labels, uncertainty intervals,
   effect direction, analysis status and displayed precision where relevant.
   Check that a metric's name matches what its generating calculation measures.
5. Inspect figures/tables and their source outputs together. Compare panel and
   legend labels, plotted variables, transformation/normalization, uncertainty
   definitions, annotations and the manuscript's descriptions. Use the relevant
   artifact viewer and technical owner when a visual or methodological question
   cannot be resolved from accessible records.
6. Explain a match only within the inspected reporting precision or supplied
   comparison rule. Do not invent a numerical tolerance, relabel a discrepancy
   as rounding without evidence, change the reported metric or weaken a claim
   merely to make sources agree.
7. Classify each target as matched, inconsistent, provenance incomplete,
   inaccessible, uninspected or not applicable with a reason. Separate a wrong
   reported value, an unclear generating record and a scientific interpretation
   question because their repairs have different owners.
8. Return exact locators and the smallest supported correction or next check.
   Refer an uncertain method, transformation or interpretation to its existing
   owner. Do not refit a model, rerun a pipeline or revise the science as an
   automatic consequence of a consistency finding.
9. If a source or draft changes, recheck affected targets and their dependencies.
   Do not declare an unrelated output set invalid or repeat unaffected checks.

## Outputs

Report target status and supporting evidence in the current task's requested form or under the recipient's existing reporting policy. Use the table below when it fits the selected deliverable; retain relevant evidence fields in other formats. A separate saved report requires authorization.

| Reported target/version | Analysis source and lineage | Comparison performed | Status | Discrepancy or next owner |
| --- | --- | --- | --- | --- |

Include exact locators, uninspected scope and requirement source state where an
external reporting or publication rule matters. A complete return can contain
unresolved targets; completeness of inspection is not correctness of the science.

## Boundaries

- A traceable or internally consistent result is not necessarily a valid inference.
- This audit does not establish execution success, accepted QC or reproduction.
- Preserve source values, labels, exclusions and provisional scientific decisions.
- Use `me.md` for saving and action scope; do not create another project tracker.

## Handoffs

Return to the invoking companion or coordinator. `check-research-reporting` owns
required disclosure coverage; writing citation/substance/argument reasoning reviewers retain
their separate jobs. Analysis and critique owners resolve substantive scientific
questions. `verify-computational-reproducibility` tests regeneration when requested;
shared writers make authorized source-backed prose corrections.

For final figure/table presentation, pass the inspected versions, quantity
definitions, verification results and remaining gaps to `review-figures-tables`.
It owns APA formatting and readability and returns layout repairs to the builder.
Resolve source discrepancies it finds here; reuse unaffected verification.

## Checks

- Every match has an inspected source and a defined comparison.
- Provenance gaps and uninspected content remain visible.
- Metric meanings, units and denominators were checked where relevant.
- No scientific threshold, history or interpretation was silently changed.
- The return's claim of coverage matches the actual inspected scope.

## References

- Kempner Institute at Harvard University. (n.d.). *Reproducible research*. https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html
- Stanford Data Science. (n.d.). *Publication phase*. https://stanforddatascience.github.io/best-practices/publication-phase.html
