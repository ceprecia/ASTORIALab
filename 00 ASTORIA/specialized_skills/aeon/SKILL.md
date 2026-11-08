---
name: aeon
description: >-
  Implements one already approved time-series machine-learning operation through
  an available, version-verified aeon API. Use when the request names this skill
  or a verified Active method or execution skill routes an exact temporal task,
  estimator, representation, validation, and metric specification. It audits
  series and case grain, time axis, sampling, windows, horizons, label timing,
  dependence, transformations, splits, estimator state, experimental APIs,
  seeds, compute, and held-out evaluation. It does not choose the task or
  estimator, install aeon or optional extras, tune automatically, leak future or
  related observations, turn clusters or anomalies into scientific entities, or
  interpret results. Triggers: time series classification with aeon, aeon time
  series operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, aeon
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Aeon

Implement and verify one approved time-series machine-learning operation while
preserving temporal and dependency boundaries.

## Purpose

`aeon` owns:

- version and API preflight for one selected aeon operation;
- implementation of an approved temporal representation and estimator;
- split-aware transformations, distances, windows, and horizons;
- bounded classification, regression, clustering, anomaly detection,
  segmentation, forecasting, similarity, or transformation execution;
- controlled validation and held-out evaluation;
- an Aeon Temporal Pipeline Record.

The user owns the scientific task, series and case grain, labels, horizons,
features, estimator, distance, window, threshold, split, metric, comparison,
interpretation, and claims.

[scikit-learn](../scikit-learn/SKILL.md) owns general classical machine-learning pipelines.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software execution control.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `time series`, `forecast`, `anomaly`, `segmentation`,
`classification`, `clustering`, `DTW`, or an estimator name alone.

Do not use this skill to choose a temporal task, algorithm, distance, window,
horizon, anomaly threshold, cluster count, or scientific label. Do not install
aeon or any optional dependency.

## Inputs

Obtain or mark missing:

- approved task and temporal estimand;
- case, series, channel, observation, participant, item, and session grain;
- time axis, units, sampling regularity, alignment, gaps, and clock provenance;
- target or event definition and the time at which it becomes knowable;
- approved windows, stride, horizon, context, padding, and boundary handling;
- train, validation, tuning, and untouched test policy;
- grouping, site, participant, session, trial, and temporal dependencies;
- transformations, normalization, missingness, distance, and feature steps;
- selected aeon estimator or bounded candidate set and whether its module is
  experimental;
- parameters, tuning cap, seeds, metrics, baselines, compute, and failure
  criteria;
- installed aeon, Python, scikit-learn, NumPy, SciPy, and optional-package
  versions;
- output destination and persistence policy.

If time, case, target, horizon, window, dependency, split, estimator, or metric
meaning is unresolved, stop with **Temporal specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, aeon, scikit-learn, NumPy, SciPy, numba, and relevant optional
  package versions;
- estimator, transformer, distance, splitter, and metric APIs;
- expected collection or series shape and data-container conversions;
- defaults, deprecations, randomness, parallel behavior, and experimental
  module status;
- installed versus documented version mismatch.

Aeon `1.5.0` was current on 2026-07-23. Its anomaly detection, forecasting,
segmentation, similarity search, visualisation, and selected transformation
modules were documented as experimental. Live use verifies the installed
version and matching API. The `1.5.0` documentation page reported Python
`3.9` through `3.12`, while the tagged package metadata and PyPI metadata
required Python `>=3.11,<3.15`. Use the tagged package metadata as execution
authority and preserve this documentation conflict.

### 2. Gate 1: approve the Temporal Pipeline Contract

Show:

- task, estimand, case and series grain, channels, and time axis;
- target timing, windows, horizon, stride, padding, and alignment;
- dependence map and split boundary;
- transformation, distance, estimator, metric, baseline, and tuning plan;
- experimental or optional API status, compute, and artifacts;
- synthetic or structure-only validation plan.

Gate 1 authorizes only read-only shape and timing review plus a synthetic
pipeline check. It does not authorize observed-data fitting, tuning, holdout
access, anomaly thresholding, observed-data forecasting, package changes,
writes outside the bounded synthetic check, or scientific interpretation.

### 3. Temporal pipeline forms

Where applicable, compare only user-supplied options such as:

- raw-series versus approved feature or distance representation;
- one fixed window or horizon versus another prespecified form;
- one approved aeon estimator versus a simple temporal baseline.

For each show changed timing assumptions, information availability, leakage
risk, metric meaning, experimental status, compute, visible output, benefit,
tradeoff, and limitation. Do not add algorithms automatically.

### 4. Build the temporal leakage record

| Element | Grain and timing | Fit subset | Apply subset | Future or group leakage risk | Verification |
|---|---|---|---|---|---|
| Target or event | | | | | |
| Window and horizon | | | | | |
| Transform or normalization | | | | | |
| Distance or feature extraction | | | | | |
| Participant, item, site, or session key | | | | | |
| Model-selection signal | | | | | |

Check overlapping windows, repeated cases, future-derived features, global
normalization, target-derived thresholds, train-test adjacency, irregular
sampling, unequal lengths, missing time points, and duplicated series.

### 5. Document time order, preprocessing, and the exact computation

Show:

- aeon classes, import paths, parameters, tags, and expected data shapes;
- preprocessing order and which subset fits each learned transform;
- distance, window, horizon, stride, padding, and missingness behavior;
- split membership, grouping, temporal order, folds, repeats, and seeds;
- bounded search space, total fits, metrics, baselines, and uncertainty;
- experimental interfaces, optional packages, warnings, compute, and failure
  criteria.

An anomaly score is not a scientific event, a change point is not necessarily
a mechanism, a cluster is not a natural group, and forecast accuracy does not
validate a causal explanation.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- temporal representation, split, estimator, parameters, search cap, seeds,
  metrics, baseline, and output destination;
- one fit, transform, distance, forecast, detection, segmentation,
  similarity, or evaluation operation;
- no-test-contact boundary.

Reopen Gate 2 before changing windows, horizons, thresholds, target timing,
representation, estimator, distance, split, experimental module, or first
access to the untouched test set.

### 7. Run the approved temporal checkpoint

Run only the approved checkpoint. Capture:

- source, code, temporal-schema, split, environment, and version hashes;
- input shapes, case counts, channels, lengths, gaps, and exclusions;
- exact estimator, transforms, distances, parameters, and seeds;
- fit count, compute, warnings, failures, and experimental API state;
- per-fold and aggregate metrics with approved uncertainty;
- baseline and approved window, horizon, threshold, or representation
  sensitivities;
- held-out results only when separately approved;
- deviations and artifacts.

Return:

```text
Aeon Temporal Pipeline Record
Approved task and temporal estimand:
Versions and API state:
Case, series, channel, and time grain:
Target timing, windows, and horizons:
Dependency, split, and leakage record:
Representation, transformations, and distance:
Estimator and parameters:
Search, compute, and seeds:
Validation and baseline results:
Held-out results, if approved:
Sensitivity results:
Warnings, failures, and deviations:
Specification-conformance check:
What the results do not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never let future, post-event, related-participant, repeated-session, or
  overlapping-window information cross an approved split boundary.
- Fit every learned transformation only inside the approved training fold.
- Never infer a sampling interval, time unit, target-availability time, window,
  horizon, or anomaly threshold.
- Treat every documented experimental module as drift-prone and reverify its
  exact installed API.
- Verify Python compatibility against the tagged package metadata rather than
  the conflicting prose installation range.
- Do not call clusters, anomalies, motifs, or change points confirmed
  scientific entities.
- Do not compare benchmark scores across incompatible datasets, splits,
  preprocessing, or metrics.
- Stop on unresolved temporal leakage, invalid shapes, inadequate fold
  support, incompatible API, missing optional package, unbounded search, or
  unapproved holdout access.

## Temporal validation and implementation

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Aeon Temporal Pipeline Record.** Execute one approved checkpoint and keep the holdout sealed until reapproval. This preserves temporal evaluation boundaries. This slows exploratory iteration. One temporal design may be fragile.
- **Labeled temporal pipeline cards.** Compare only the approved temporal representation, estimator, or baseline routes. This exposes timing and leakage consequences without automatic selection. This requires a bounded candidate set. Unproposed algorithms remain outside scope.
- **Temporal Pipeline Decision Record.** Show time grain, target timing, split, transform, experimental API, metric, and compute records. This makes future and dependence leakage visible. This requires detailed timing metadata. Upstream timestamps may still be wrong.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended temporal-validity matrix.** Add negative controls and prespecified temporal transport tests. This tests selected failure modes and generalization. This requires more data and compute. Negative controls cannot cover every leak.
- **Temporal sensitivity grid.** Add prespecified window, horizon, distance, and validation alternatives. This tests selected design dependence. This adds fits, compute, and multiplicity. This cannot resolve construct uncertainty.
- **Verified temporal-analysis bundle.** Run the prespecified window, horizon, or external temporal validation grid. This quantifies selected robustness and transport. This adds compute and governed data needs. Robustness does not establish mechanism.

## Checks

- **Positive:** an approved grouped time-series classification pipeline records
  target timing, windows, split-aware transforms, and no test contact.
- **Negative:** `find the best forecasting model` does not trigger automatic
  model selection.
- **Leakage:** normalization across all time points or overlapping train-test
  windows stops execution.
- **Experimental:** an anomaly detector with a drifted installed API returns an
  API mismatch rather than guessed code.
- **Edge:** unequal or irregular series incompatible with the chosen estimator
  return a representation failure.
- **Handoff:** generic classical ML returns to [scikit-learn](../scikit-learn/SKILL.md); general
  execution control may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- *aeon* (Version 1.5.0) [Computer software]. (n.d.). GitHub. https://github.com/aeon-toolkit/aeon/releases/tag/v1.5.0
- *aeon 1.5.0 documentation*. (n.d.). https://www.aeon-toolkit.org/en/stable/
