---
name: statsmodels
description: >-
  Implements one already approved statistical model through an available,
  version-verified Statsmodels API and returns a design-matrix, fit, diagnostic,
  and output record. Use when the request names this skill or a verified Active
  method or execution skill routes an exact Statsmodels handoff. It makes
  formula or matrix construction, coding, intercepts, weights, offsets,
  covariance, clustering, missingness, warnings, convergence, diagnostics, and
  predictions inspectable before fitting. It does not choose the model, install
  packages, change specification after outcomes are seen, repair failures
  silently, claim causality, or interpret scientific meaning. Triggers: fit this
  model in statsmodels, statsmodels regression.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, statsmodels
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Statsmodels

Implement one approved statistical specification with the exact Statsmodels
API available in the selected environment.

## Purpose

`statsmodels` owns:

- version and API preflight for one selected Statsmodels model;
- formula or explicit design-matrix construction;
- coding, intercept, weights, offset, exposure, covariance, clustering, and
  missingness implementation;
- one approved fit, selected diagnostics, contrasts, predictions, and neutral
  result extraction;
- warnings, convergence, rank, separation, and output verification;
- a Statsmodels Implementation Record.

The user owns the scientific question, estimand, model family, formula, coding,
contrasts, covariance, clustering, thresholds, diagnostics, remediation,
interpretation, and claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns method-family comparison.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software execution control.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `regression`, `time series`, `GLM`, `OLS`, `statistics`,
`fit this`, or another broad analysis term.

Do not use this skill to choose between OLS, GLM, mixed, discrete, count,
time-series, causal, or forecasting methods. Do not install or upgrade
Statsmodels, SciPy, Patsy, pandas, or any optional dependency.

## Inputs

Obtain or mark missing:

- approved Analysis Method Specification;
- exact Statsmodels model class and installed version;
- formula or explicit outcome and design matrices;
- variable types, categories, reference levels, contrasts, and intercept rule;
- weights, offset, exposure, link, family, covariance, cluster, group, and time
  settings where applicable;
- missingness and exclusion rules;
- fit arguments, optimizer, tolerances, iteration limits, and seeds where used;
- requested contrasts, marginal effects, predictions, intervals, and
  diagnostics;
- input data state, output destination, and acceptance criteria.

If the model, coding, dependence, API, or acceptance rules are unresolved,
stop with **Statsmodels specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python and Statsmodels versions;
- imported public module and model class;
- installed companion versions that affect formulas or arrays;
- relevant official documentation for that installed version;
- signature, defaults, warnings, and version-specific behavior;
- unavailable or experimental APIs.

Current source review found Statsmodels `0.14.6` current on 2026-07-23, but
invocation always checks the live environment and matching documentation.

### 2. Gate 1: approve design and read-only inspection

Show:

- exact data and fields to read;
- formula or matrix route;
- coding and intercept plan;
- model constructor and fit call;
- weights, offset, exposure, covariance, clustering, and missingness behavior;
- diagnostics, predictions, artifacts, and stop conditions.

Gate 1 authorizes only the displayed read-only inspection, design-matrix
preview, and code plan. It does not authorize fitting, writing, package
changes, or specification repair.

### 3. Implementation forms for the approved model

Compare eligible implementations only when a real choice remains. Otherwise use the approved implementation and report any material incompatibility before proceeding.

Where applicable, compare:

1. **Formula API** for explicit named terms and declared categorical coding.
2. **Matrix API** for an already constructed and audited design matrix.
3. **Existing pinned script** when it exactly implements the approved model.

For each show API coverage, coding transparency, reproducibility, version
risks, visible output, benefit, tradeoff, and limitation. These are
implementation forms, not competing statistical methods.

### 4. Audit the design before fitting

Provide:

| Element | Approved meaning | Implemented object | Default avoided or accepted | Verification |
|---|---|---|---|---|
| Outcome | | | | |
| Predictors and interactions | | | | |
| Categories and contrasts | | | | |
| Intercept | | | | |
| Weights, offset, exposure | | | | |
| Dependence and covariance | | | | |
| Missingness and exclusions | | | | |

Verify dimensions, column order, labels, rank, duplicated terms, constant
handling, reference levels, row loss, and alignment between arrays.

Never add a constant automatically when the approved specification excludes
one, and never omit it by accident.

### 5. Review fitting and diagnostics

Show:

- constructor and fit arguments;
- optimization and convergence criteria;
- covariance estimator and its assumptions;
- prespecified tests, contrasts, intervals, marginal effects, or predictions;
- model-specific residual, influence, calibration, time, count, or
  dependence diagnostics;
- failure conditions such as rank deficiency, separation, nonconvergence,
  singularity, invalid support, or incompatible weights;
- what each output can and cannot establish.

Do not automatically switch families, covariance estimators, optimizers,
time-series orders, or model classes in response to diagnostics.

### 6. Gate 2: approve one exact fit

Ask the user to approve:

- exact model class, code, and command;
- audited design matrix;
- fit and covariance arguments;
- diagnostics, contrasts, predictions, and output destination;
- no-retry and no-remediation boundary.

Gate 2 authorizes only the displayed fit and verification.

### 7. Fit and verify the approved Statsmodels operation

Capture:

- source data and code hashes;
- Python, Statsmodels, and companion versions;
- formula, matrix columns, shapes, and row disposition;
- constructor, fit call, arguments, and runtime warnings;
- convergence and termination state;
- coefficients, uncertainty, requested statistics, contrasts, predictions, and
  diagnostics;
- artifact hashes and specification deviations.

Return:

```text
Statsmodels Implementation Record
Approved method and model:
Installed version and API:
Data, formula, and design matrix:
Coding, intercept, weights, offsets, and covariance:
Fit call and arguments:
Warnings and convergence:
Neutral numerical outputs:
Diagnostics and sensitivity results:
Predictions or contrasts:
Specification-conformance check:
Unresolved failures and limitations:
Artifacts and hashes:
user-owned interpretation:
```

## Boundaries

- Stop on unapproved row loss, coding, intercept, covariance, or default.
- Stop on rank deficiency, perfect or quasi-separation, nonconvergence,
  singularity, or unsupported API behavior unless the approved criteria
  already define the outcome.
- Do not convert a diagnostic signal into an automatic model change.
- A lower AIC, BIC, error metric, or p-value does not authorize selection.
- Marginal effects and transformed coefficients require the approved scale and
  estimand.
- Forecasting, Granger tests, or regression coefficients do not establish
  causality.
- Report `p > alpha` as not significant and never as marginal or trending.

## Model fitting and sensitivity checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Design and Fit Decision Record.** Audit the design matrix, defaults, fit arguments, diagnostics, and failures. This prevents silent API choices. This requires explicit low-level inputs. Runtime behavior may still fail.
- **Labeled implementation forms.** Compare formula, matrix, and exact existing-script forms only when applicable. This improves transparency without reopening method choice. This adds an implementation review. This cannot resolve an unselected model.
- **Statsmodels Implementation Record.** Fit one approved model once and verify outputs. This preserves the exact specification and failure evidence. Remediation needs new approval. One fit does not establish robustness.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Cross-software verification plan.** Compare against an independent software implementation. This detects some implementation-specific differences. This requires another adapter and environment. Differences may remain scientifically ambiguous.
- **Dual-formulation plan.** Add a second Statsmodels formulation of the same model. This can expose coding mismatches. This adds duplicate implementation work. Agreement does not validate the model.
- **Sensitivity bundle.** Execute approved sensitivity and cross-version checks. This tests selected robustness dimensions. This adds data contact and compute. This requires separate explicit authorization.

## Checks

- **Positive:** a fixed GLM specification produces an audited design matrix,
  exact API call, one fit, and neutral output record.
- **Negative:** `which regression should I use?` routes to a method guide.
- **Edge:** an installed version mismatch stops before code execution.
- **Failure:** perfect separation or nonconvergence is preserved without an
  automatic family or optimizer change.
- **Coding:** an ambiguous categorical reference level stops before fitting.
- **Handoff:** general execution may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md), while
  method changes return to [cogsci-statistics](../cogsci-statistics/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Statsmodels. (n.d.). *Diagnostics*. https://www.statsmodels.org/stable/diagnostic.html
- Statsmodels. (n.d.). *Statsmodels 0.14.6 release notes*. https://www.statsmodels.org/stable/release/version0.14.6.html
- Statsmodels. (n.d.). *Statsmodels stable documentation*. https://www.statsmodels.org/stable/
