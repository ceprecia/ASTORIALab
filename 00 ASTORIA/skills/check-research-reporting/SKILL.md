---
name: check-research-reporting
description: >-
  Audits a bounded research document against the applicable current reporting
  guideline and identifies missing or ambiguous disclosures. Use for reporting
  completeness; a filled checklist does not establish methodological validity,
  accepted quality control or computational reproducibility. Triggers: audit
  research reporting completeness, check required method disclosures.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: writing-coordinator
  created: "2026-11-01"
  updated: "2026-11-01"
---
# Check Research Reporting

Identify the information a reader needs that the report has not yet disclosed.

## Purpose

Audit a bounded research text against its applicable current reporting
guideline. Separate missing reporting from defects in study design or execution.
A complete checklist establishes coverage of reporting items only, not
scientific validity, accepted QC or reproducibility.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md).
Use the brief, relevant MOC and recipient-supplied writing guidance, manuscript version,
study design, target venue, current checklist if supplied, protocol or
preregistration and available technical records. Confirm the assigned section
and whether the request covers text alone or supporting materials too.

## Steps

1. Identify the applicable reporting standard from the study design and venue.
   Verify the current version and requirements with official sources. If fit
   is uncertain, state the alternatives and ask only the question needed to
   select the relevant standard.
2. Obtain the checklist or reporting items themselves. Record title, version,
   source and scope. A guideline's acronym or a secondary summary is not a
   sufficient basis for claiming a full audit.
3. Map each applicable item to an exact passage, table, figure or supplement.
   Keep present, incomplete, absent, unverified and not applicable distinct;
   justify not applicable rather than using it to hide missing information.
4. Check methods disclosures such as design, sample and eligibility, procedure,
   outcomes, exclusions, missing data, preprocessing, models, uncertainty,
   multiplicity, software, preregistration and deviations where the guideline
   requires them. Do not impose every item on every study.
5. Compare the report with available approved methods and execution records.
   Identify planned-versus-executed discrepancies or missing explanations;
   do not repair them by editing the scientific history.
6. Check that confirmatory, secondary and exploratory analyses are labeled
   consistently and that quantitative disclosures have denominators, units
   and definitions where needed.
7. Separate three findings: information exists but is not reported, information
   is unclear in source records, and an underlying methodological question
   needs a domain decision. Each requires a different next action.
8. Return exact missing disclosures and available source-backed repairs.
   Do not fill missing sample sizes, thresholds, exclusions, registrations or
   data-availability statements from common practice.
9. Recheck revised reporting against the affected items. Retain unresolved
   source gaps and explicitly limit any completeness statement to the inspected
   standard, version, document and material.

## Outputs

Report the standard item, document location, coverage status, missing information and source or owner needed in the selected reporting form. Use the table below when it helps.

| Standard item | Document location | Coverage status | Missing information | Source or owner needed |
| --- | --- | --- | --- | --- |

Provide concise replacement text only when requested and supported. Apply
the writing profiles specified in `me.md` when producing formal prose.
Return the audit in the current task's requested form or under the recipient's existing reporting policy. A separate checklist or report artifact requires authorization and an owning destination.

## Boundaries

- Reporting completeness is not a test that code regenerates the results.
- A recorded preprocessing command is not evidence of reviewed image quality.
- A valid data format is not evidence that a repository release is approved.
- Do not choose study designs, exclusions, analysis thresholds or interpretations.
- Do not claim compliance beyond the inspected text and accessible materials.

## Handoffs

Return through writing-coordinator. keep-writing-structure owns template and
layout fidelity; write-methods or the relevant writer adds verified disclosures.
Domain ambiguities return through
[cross-system handoffs](../writing-coordinator/references/cross_system_handoff.md).
Scientific critique, execution and reproducibility checks stay with their
appropriate existing capabilities rather than being performed by this audit.

## Checks

- The checklist version and authoritative source are identified.
- Every completed item has an actual content locator.
- Incomplete access is visible, and not-applicable items are justified.
- No reporting repair invents work or implies a stronger validation state.
