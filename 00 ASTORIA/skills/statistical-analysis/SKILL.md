---
name: statistical-analysis
description: >-
  Plans, executes, and verifies one approved statistical analysis through an
  already available and pinned implementation. Use when the bounded request
  matches this description or names this skill, or a verified coordinator or
  Active method guide routes an exact Analysis Method Specification. It preserves source data, records code, commands, versions,
  diagnostics, sensitivity checks, deviations, and outputs, and returns a
  Statistical Analysis Execution Record after two approval gates. It does not
  choose the scientific question, estimand, method, model, threshold, prior,
  exclusion, correction, interpretation, or claim, install packages, repair
  failures silently, or turn exploratory work into confirmatory evidence.
  Triggers: run this statistical analysis, execute the approved analysis plan.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: analysis
  modality: any
  dependencies: ""
  requires: a pinned statistical implementation
  gates: running on real data, accepting results
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Statistical Analysis

Implement one already approved statistical method and preserve an inspectable
execution record.

## Purpose

`statistical-analysis` owns:

- translating one approved Analysis Method Specification into an exact
  execution plan;
- pinning the source data, code, environment, random state, command, output
  destination, and acceptance criteria;
- running one selected analysis step after explicit execution approval;
- capturing warnings, errors, convergence, diagnostics, sensitivity outputs,
  exclusions actually applied, and generated artifacts;
- verifying technical and specification conformance;
- reporting numerical outputs without scientific interpretation.

The user owns the question, hypothesis, estimand, confirmatory status, data-use
permission, method, model, variables, contrasts, exclusions, transformations,
priors, thresholds, corrections, sensitivity criteria, interpretation, and
claims.

[cogsci-statistics](../../specialized_skills/cogsci-statistics/SKILL.md) owns cognitive and neuroscience method comparison.
[exploratory-data-analysis](../exploratory-data-analysis/SKILL.md) owns descriptive structure and quality
inspection before an analysis plan is fixed.

Use this skill when the user names it or the bounded request matches its
frontmatter description and trigger meaning. A verified coordinator or
capability handoff may invoke the same matching task.

Do not trigger from `analyze`, `statistics`, `run this`, `significant`,
`regression`, `ANOVA`, `Bayesian`, a package name, or a dataset path alone.

Do not use this skill to:

- invent or select an analysis method;
- install, update, or choose a package because it is available;
- explore alternative models until one produces a preferred result;
- change exclusions, transformations, contrasts, priors, thresholds, or
  multiplicity after viewing outcomes;
- repair or retry a failure without a new visible plan;
- write a scientific conclusion or publication narrative.

## Inputs

Obtain or mark missing:

- approved Analysis Method Specification or equally exact method record;
- confirmatory, preregistered, deviated, or exploratory status;
- exact input dataset, version, processing state, hashes, and access boundary;
- variable dictionary, observation grain, joins, filters, exclusions, and
  missingness rules;
- model family, formula or equivalent specification, contrasts, priors,
  thresholds, multiplicity, and sensitivity rules;
- already available software, executable, packages, container, or environment;
- exact code state or proposed minimal script;
- random seeds and known nondeterminism;
- resource, privacy, logging, and external-access limits;
- technical and scientific-specification acceptance criteria;
- new output destination and artifact-retention plan.

If the method, data authority, environment, command, or acceptance criteria are
unresolved, stop with **Execution specification incomplete**.

## Steps

### 1. Build the Execution Brief

| Field | Required record |
|---|---|
| Method authority | Approved specification and user-owned decisions |
| Analysis status | Confirmatory, preregistered, deviated, or exploratory |
| Data state | Exact inputs, grain, processing, access, hashes, and exclusions |
| Implementation | Software, packages, code, command, seeds, and versions |
| Outputs | New destination, filenames, tables, figures, logs, and model objects |
| Diagnostics | Assumption, convergence, predictive, residual, influence, or sensitivity checks |
| Acceptance | Technical pass, specification pass, failure, and inconclusive criteria |
| Prohibitions | No install, method shopping, silent repair, overwrite, or claim |
| Stop point | One execution and verification record |

Record every mismatch between the method specification and available
implementation. Availability does not resolve the mismatch.

### 2. Gate 1: approve inspection and translation

Before reading observed data, code, or environment state, ask the user to approve:

- exact inputs and fields that may be read;
- exact implementation state to inspect;
- privacy and redaction boundaries;
- proposed code and command construction;
- diagnostics, sensitivity checks, artifacts, and acceptance criteria;
- output destination;
- no-install and no-execution boundary for Gate 1.

Gate 1 authorizes only the displayed read-only inspection and plan. It does not
authorize fitting, transformation, export, package changes, or saving outputs.

### 3. Implementation fit for the approved method

Compare eligible implementations only when a real choice remains. Otherwise use the approved implementation and report any material incompatibility before proceeding.

Offer only genuinely applicable implementation routes, such as:

- an existing verified analysis script;
- a minimal new script implementing the approved specification;
- a named active software adapter for the selected package.

For each route show:

- exact software and version state;
- specification coverage and gaps;
- commands and side effects;
- data access and memory behavior;
- deterministic and nondeterministic elements;
- diagnostics and artifacts;
- reproducibility strength;
- tradeoffs, limitations, and stop conditions.

Do not compare statistical methods. Return method ambiguity to its owner.

### 4. Pin the starting state

Record:

- input paths or object identities and hashes;
- data dictionary and row or observation counts;
- code, configuration, environment, executable, and package versions;
- current working directory and path resolution;
- seed, thread, accelerator, and nondeterminism settings;
- network, telemetry, cache, temporary-file, and credential behavior;
- existing destination contents;
- warnings or unverified assumptions.

Do not expose secrets or participant identifiers in logs.

### 5. Review the command, side effects, and acceptance checks

Provide:

| Step | Input | Exact operation | Output | Diagnostic | Failure signal | Specification link |
|---|---|---|---|---|---|---|

Also show:

- every filter, exclusion, recode, transformation, join, and aggregation;
- every model term, contrast, prior, threshold, and correction;
- every default that the implementation would otherwise supply;
- expected warnings and stop conditions;
- what a successful run can and cannot establish.

Unapproved defaults remain unresolved, not accepted.

### 6. Gate 2: approve one exact execution

Ask the user to approve:

- one route, script, and exact command;
- pinned inputs, environment, seeds, and output destination;
- all model and preprocessing values;
- diagnostic, sensitivity, and acceptance rules;
- one-run, no-repair stop policy.

Gate 2 authorizes only the displayed operation. Do not infer permission for
alternative models, retries, tuning, additional contrasts, exports, or another
capability.

### 7. Run and verify the approved command

Run only the approved operation. Capture:

- start and end time;
- command, code hash, environment, versions, and seeds;
- input and output hashes;
- stdout, stderr, warnings, errors, convergence, and termination state;
- row counts and all applied exclusions or transformations;
- coefficients, uncertainty, test statistics, exact p-values, posterior
  summaries, or other approved numerical products;
- diagnostics and sensitivity results;
- differences from the approved specification.

Do not hide a warning or automatically rerun. If execution fails, preserve the
failure and return a bounded repair proposal for separate approval.

### 8. Return the Statistical Analysis Execution Record

```text
Statistical Analysis Execution Record
Approved method specification:
Analysis status:
Input data and hashes:
Implementation and versions:
Code and exact command:
Seeds and nondeterminism:
Operations actually applied:
Numerical outputs:
Diagnostics and sensitivity checks:
Warnings, errors, and deviations:
Technical verification:
Specification-conformance verification:
What the run does not establish:
user-owned interpretation and claims:
Artifacts and hashes:
Approved handoff or stop:
```

## Boundaries

- Source data are read-only. Write only into the approved new destination.
- `p > alpha` is not significant and is never marginal, approaching
  significance, a trend, or nearly supported.
- Nonsignificance does not establish absence.
- Report exact numerical results and uncertainty without choosing the story.
- An assumption check is evidence, not an automatic test-switch rule.
- Convergence, singularity, effective sample size, predictive checks,
  residuals, influence, and sensitivity must be interpreted against the
  approved criteria.
- A technically successful run does not establish model validity, causal
  identification, robustness, reproducibility, or a scientific conclusion.
- Outcome-dependent changes are recorded and the affected work remains
  exploratory.

## Statistical implementation records

Use the records relevant to the approved operation. Raise a material problem with the method owner before changing the scientific specification.

- **Exact Operation Table.** Show every operation, default, diagnostic, side effect, and specification link. This makes execution auditable before data contact. This requires detailed setup. This cannot predict every runtime failure.
- **Labeled execution routes.** Compare only existing script, minimal script, and exact active-adapter routes that implement the fixed method. This separates implementation from method choice. This may reveal no runnable route. This does not choose or improve the method.
- **Statistical Analysis Execution Record.** Run one exact command once and verify outputs against the specification. This preserves human control and failure evidence. Repairs require another approval. One run does not establish robustness.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Cross-implementation comparison.** Reproduce the operation in a second independent implementation. This can detect implementation-specific differences. This doubles implementation and review work. Agreement does not prove scientific validity.
- **Multi-run verification bundle.** Run prespecified sensitivity and reproduction sets. This tests approved robustness dimensions. This adds data contact, compute, and multiplicity. This requires separate explicit authorization.
- **Route cards plus reproducibility plans.** Add independently containerized reproductions for each route. This improves environment isolation. This adds build and storage burden. This requires separately approved environments.

## Checks

- **Positive:** an approved fixed model and pinned environment produce one
  exact command, diagnostic plan, run, and execution record.
- **Negative:** `which test should I use?` routes to [cogsci-statistics](../../specialized_skills/cogsci-statistics/SKILL.md) or
  another method guide.
- **Edge:** an unavailable package returns an implementation gap without an
  install.
- **Failure:** nonconvergence produces a preserved failure and a new repair
  proposal, not an automatic optimizer change.
- **Deviation:** an outcome-dependent exclusion is logged and the affected
  analysis is labeled exploratory.
- **Handoff:** publication prose and scientific interpretation remain outside
  this execution skill.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Sandve et al. (2013). Ten simple rules for reproducible computational research. https://doi.org/10.1371/journal.pcbi.1003285
- Wilson et al. (2017). Good enough practices in scientific computing. https://doi.org/10.1371/journal.pcbi.1005510
