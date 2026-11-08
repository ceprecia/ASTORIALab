---
name: prepare-publication-package
description: 'Assembles the required files, declarations, metadata and availability
  statements for one selected publication stage. Returns a verified package inventory
  while preserving contributor decisions and submission authority. Triggers: assemble
  this journal submission, check these submission files.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: selected venue, article type, stage and identified submission materials
  created: '2026-11-02'
  updated: '2026-11-06'
  gates: ''
---

# Prepare Publication Package

Assemble one publication package from identified files and verified requirements.

## Purpose

Prepare or inspect the materials for one selected publication stage. Reconcile
required files, metadata, declarations and availability information with the
actual materials. Return a package inventory and localized repairs without
taking over scientific decisions, authorship or the submission itself.

## Inputs

- Selected journal, article type and stage, with current requirements if available.
- Current manuscript and identified figures, tables, supplements and related outputs.
- Contributor-supplied names, affiliations, identifiers, roles and declarations.
- Actual data/code locations and their verified access or release state.
- Requested assembly or inspection scope, destination and original return owner.

## Steps

1. Fix the target and source versions. Identify which manuscript is current,
   which materials are authoritative and whether assembly, repair or a
   read-only inspection was requested. Resolve conflicting source copies
   before replacing a deliverable.
2. Read [current primary-source verification](../research-output-coordinator/references/source_verification.md)
   completely. Apply its method to the selected journal, article type and
   stage rather than copying requirements from a previous package.
3. Build a bounded item list from the applicable instructions. For each
   required or conditional item, identify its source, actual file/version,
   contributor, inspected state and remaining dependency. A listed filename
   does not establish that a file exists or is complete.
4. Inspect the actual manuscript, display files and supplements with tools
   appropriate to their formats. Check required organization, limits, file
   types, figure resolution where applicable, captions, references and
   names. Use artifact owners for conversions and rendered layout inspection;
   mark surfaces not inspected.
5. Reconcile manuscript metadata with the supplied authoritative records.
   Check names, affiliations, identifiers and contributions across relevant
   files. Preserve unknown declarations and author confirmations as unknown;
   do not infer assent or contribution from inclusion in a document.
6. Check availability information against actual identifiers, links, versions
   and access states. Distinguish a planned deposit, private reviewer access
   and a public release. Borrow release-verification evidence where needed.
7. Obtain any required cover-letter, statement or other prose through the
   shared writing capabilities using the current claim, evidence and exact
   requirements. This skill checks the requested item and its consistency;
   it does not invent scientific content or institutional commitments.
8. If assembly is requested, use the established destination and preserve
   source materials. Keep one canonical package, with artifact owners making
   necessary format repairs. Reinspect changed files and compare any clean
   and marked-up versions against the same scientific content.
9. Reconcile the final inventory with the files actually present. Resolve
   citations to absent supplements, outdated figures, contradictory counts
   and stale access statements through their owners. Do not quietly edit
   analysis outputs to make the package agree.
10. Return the prepared or inspected state, unresolved items and source state.
    Distinguish material ready for the requested next handoff from items
    merely present, not inspected or awaiting contributor input.

## Outputs

Return the actual package location when one was assembled, plus an inventory
containing only useful fields: requirement, source, file/version, inspected
state, discrepancy, contributor and next action. Include the scope of format
inspection and any dependency that prevents a requested item being complete.

Report check results in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization. Follow me.md
for saving the package and preserve the owning project's canonical layout.

## Boundaries

- Preparation and verification do not establish submission or public release.
- Contributor confirmations and declarations come from their actual owners.
- File presence, a reporting checklist or successful document conversion does
  not establish scientific validity or computational reproducibility.
- Do not change the research design, interpretation, results or availability
  state to satisfy a format requirement.
- Inspect only the authorized package; do not collect unrelated private
  records or create another project index.

## Handoffs

- Preserve the invoking session and return owner.
- Use [plan-publication](../plan-publication/SKILL.md) for an
  unresolved venue or requirements question.
- Borrow shared writers, document/artifact owners and
  [check-research-reporting](../check-research-reporting/SKILL.md)
  for their respective bounded work.
- Use [verify-research-outputs](../verify-research-outputs/SKILL.md)
  for result/provenance inconsistencies and
  [verify-repository-release](../verify-repository-release/SKILL.md)
  for observed repository release state.
- Leave the submission action with its authorized human or institutional owner.
- Use `review-figures-tables` for final display APA/readability review within
  the requested package scope. Supply actual figures/tables, the venue rules,
  intended placement size and existing verification. Keep numerical, layout
  and caption repairs with their owners and reinspect affected package files.

## Checks

- Every applicable required item is accounted for or explicitly unresolved.
- Final inventory entries identify actual files and inspected versions.
- Captions, display references and supplementary links match present materials.
- Metadata and availability claims agree with inspected evidence.
- Uninspected surfaces and missing contributor input are visible in the return.

## References

- University of Cambridge Libraries. (n.d.). *The submission process*. https://libguides.cam.ac.uk/writing-for-publication/submission-process
- PLOS. (n.d.). *Submission guidelines: PLOS One*. https://journals.plos.org/plosone/s/submission-guidelines
- PLOS. (n.d.). *Accepted manuscripts: PLOS One*. https://journals.plos.org/plosone/s/accepted-manuscripts
