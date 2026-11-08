---
name: verify-computational-reproducibility
description: 'Tests whether specified research outputs regenerate from recorded inputs,
  code, configuration and environment through the existing technical owners. Reports
  comparison evidence and untested scope without equating execution with reproduced
  findings. Triggers: test whether these results regenerate, reproduce these reported
  outputs.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: analysis-coordinator
  requires: specified target outputs and user-selected data, code and comparison criteria
  created: '2026-11-02'
  updated: '2026-11-02'
  gates: ''
---
# Verify Computational Reproducibility

Test a defined result against the recorded inputs, computation and comparison rule.

## Purpose

Assess and, within the requested execution scope, test whether specified outputs
regenerate from the recorded data, code, configuration and environment. Coordinate
technical execution through the existing analysis/modality/software owners.
Distinguish preparation, successful execution, output agreement and independent
environment reconstruction; none establishes replication with new observations
or scientific validity.

## Inputs

Read the [current-source contract](../research-output-coordinator/references/source_verification.md).
Use the exact target outputs and versions, user-selected analysis and scope,
input data identifiers, code/configuration revisions, original environment,
manual steps, expected results and comparison criteria. Establish the current
execution authorization, resources and destination through existing project
instructions. Do not infer execution permission from a request to assess readiness.

## Steps

1. Define the reproduction target: selected values, tables, figures, models or
   a specified pipeline stage. Identify the starting inputs and what upstream
   processing is outside scope. A test starting at processed data must not be
   described as a complete reconstruction from raw observations.
2. Inspect the existing provenance and materials. Identify data and code versions,
   parameters, software dependencies, seeds where applicable, required licenses,
   hardware constraints, external services and manual steps. Record missing or
   inaccessible inputs rather than replacing them with a convenient dataset.
3. Establish the expected outputs and user/technical-owner comparison rule before
   judging agreement. If a consequential tolerance or scientific comparison is
   missing, obtain that smallest decision while continuing the materials check.
   Do not choose new exclusions, thresholds or criteria to obtain a pass.
4. Choose the requested assessment level: documentation/readiness only, rerun in
   an existing environment, or reconstruction in a clean environment. Describe
   which level is technically possible. A readiness assessment returns remaining
   dependencies and does not claim that results were reproduced.
5. Route an authorized execution through analysis-coordinator and the exact
   relevant technical owner. Pass the fixed inputs, commands/configuration,
   original environment, target outputs, resources, destination and comparison
   rule. Preserve scientific parameters and project layout. Missing runtime blocks
   that execution, not the independent inventory or planning work.
6. Retain the original analysis environment for historical reproduction. Current
   repository or publisher requirements still need current-source verification;
   updating those requirements does not authorize upgrading the analysis code or
   software. Any proposed compatibility change returns to the user/technical owner.
7. Use an authorized separate destination so the test does not replace the
   authoritative originals. Record whether required inputs were reconstructed
   or taken from existing caches, how randomness was controlled, and which
   manual steps were performed or remain documented but untested. Preserve
   intentional manual figure assembly unless automation was requested.
8. Collect actual commands, runtime status and outputs from the technical owner.
   Compare the specified outputs under the selected rule. Identify numerical,
   semantic or visual discrepancies and their tested scope. Successful exit
   status, plausible plots and a matching filename are insufficient evidence.
9. Report a failed execution separately from a completed run with discrepant
   outputs. Document unavailable inputs, untested stages, stochastic/hardware
   limitations and ambiguous comparisons. Do not select a favorable seed or
   substitute another analysis after seeing a mismatch.
10. Return the evidence and next owner. Repair a demonstrated implementation or
    packaging issue only within the current authorization; proposed scientific
    changes return to the user. Recheck only affected products after a repair.

## Outputs

Return the target and assessment level, inspected input/code/environment versions,
actual execution evidence, comparison criteria, per-output results and limitations.
Include the evidence fields below in the selected reporting form. Use the table when it helps.

| Target | Starting inputs and versions | Test level / execution | Expected versus observed | Comparison rule | Status and remaining issue |
| --- | --- | --- | --- | --- | --- |

Use statuses such as not tested, not executable with available materials,
execution failed, executed with discrepancy, reproduced within the stated rule,
or comparison unresolved. State whether the environment was independently
reconstructed. Limit every conclusion to the tested outputs, inputs and rule.
Report checks in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization. Return through the original session owner.

## Boundaries

- BIDS validation, a complete compendium, a DOI or a repository upload is not a
  test that the findings regenerate.
- Reproduced outputs do not establish methodological validity or accepted QC.
- Do not invent runtime results or describe an unexecuted command as a test.
- Preserve the original science, data and manual workflow under `me.md` and
  project instructions; avoid creating unrequested orchestration scripts.

## Handoffs

Analysis-coordinator selects the relevant technical execution owner; it does not
choose new scientific parameters. `verify-research-outputs` can resolve an
unclear lineage or reporting mismatch without running the analysis.
`prepare-research-release` assembles the compendium; `verify-repository-release`
checks the observed deposit. Shared methods writers may describe the actual
verified scope, and scientific inference questions return to the user and the
appropriate critique/analysis owner.

## Checks

- The reproduction target, starting point and comparison rule are explicit.
- Execution evidence is actual and the scope of authorization was preserved.
- Expected and observed outputs were compared rather than inferred from success.
- Missing inputs, cache use, manual work and environment limits are disclosed.
- The result does not certify untested stages, scientific validity or replication.

## References

- Kempner Institute at Harvard University. (n.d.). *Reproducible research*. https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html
- Stanford Data Science. (n.d.). *Publication phase*. https://stanforddatascience.github.io/best-practices/publication-phase.html
