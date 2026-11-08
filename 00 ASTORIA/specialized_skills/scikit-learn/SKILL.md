---
name: scikit-learn
description: >-
  Implements one already approved classical machine-learning pipeline through an
  available, version-verified scikit-learn API. Use when the request names this
  skill or a verified Active method or execution skill routes an exact pipeline
  specification. It audits the prediction unit, feature timing, target,
  partitions, grouped or temporal dependence, preprocessing, estimator, tuning
  space, metrics, leakage, seeds, compute, and held-out evaluation. It does not
  choose the scientific task or estimator, install packages, search unbounded
  hyperparameters, reuse the test set, treat clusters or feature importance as
  scientific truth, or interpret results. Triggers: build a scikit-learn
  pipeline, cross validated classifier in sklearn.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, scikit-learn
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Scikit-learn

Implement and verify one approved classical machine-learning pipeline with
split-aware preprocessing and controlled evaluation.

## Purpose

`scikit-learn` owns:

- version and API preflight for one selected scikit-learn pipeline;
- split-aware preprocessing and feature composition;
- implementation of one approved estimator or bounded comparison set;
- grouped, stratified, nested, temporal, or ordinary validation exactly as
  approved;
- bounded tuning, metrics, baselines, calibration, and sensitivity checks;
- held-out evaluation only at the approved checkpoint;
- a Scikit-learn Pipeline Record.

The user owns the scientific target, prediction unit, features, acquisition-time
boundary, estimator family, partitions, tuning space, metrics, baselines,
thresholds, interpretation, and claims.

[exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns descriptive structure and quality review.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software execution control.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `machine learning`, `classification`, `regression`,
`clustering`, `predict`, `cross-validation`, or an estimator name alone.

Do not use this skill to select a research question, label, feature set,
estimator, metric, cluster count, or scientific subgroup. Do not install
scikit-learn or optional packages.

## Inputs

Obtain or mark missing:

- approved task and estimand;
- target, prediction unit, outcome timing, and use context;
- features, provenance, acquisition timing, and availability at prediction;
- participant, item, session, site, family, batch, and temporal dependencies;
- train, validation, tuning, and untouched test policy;
- approved preprocessing, missingness, encoding, scaling, and feature steps;
- selected estimator or bounded candidate set;
- hyperparameter space, search budget, stopping rule, and seeds;
- metrics, baselines, calibration, uncertainty, and failure criteria;
- installed scikit-learn version and compute limits;
- output destination and persistence policy.

If the prediction unit, target, feature timing, partition, leakage boundary, or
metric is unresolved, stop with **Machine-learning specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, scikit-learn, NumPy, SciPy, joblib, and relevant dataframe versions;
- estimator, transformer, splitter, search, and metric APIs;
- defaults, deprecations, metadata routing, randomness, and parallel behavior;
- installed versus documented version mismatch.

Scikit-learn `1.9.0` was current on 2026-07-23. Live use always verifies the
installed version and matching documentation.

### 2. Gate 1: approve partition and pipeline design

Show:

- exact data fields allowed for inspection;
- prediction unit and dependency structure;
- feature timing and leakage audit;
- partition, grouping, temporal, and holdout plan;
- pipeline and preprocessing graph;
- estimator set, metrics, baseline, tuning cap, compute, and artifacts;
- synthetic or structure-only validation plan.

Gate 1 authorizes only read-only structure review and a synthetic pipeline
check. It does not authorize observed-data fitting, tuning, holdout access,
package changes, writes, or scientific interpretation.

### 3. Pipeline forms for the approved evaluation

Compare eligible implementations only when a real choice remains. Otherwise use the approved implementation and report any material incompatibility before proceeding.

Where applicable, compare:

- one fixed baseline pipeline;
- one approved candidate estimator pipeline;
- one approved alternative representation or validation form.

For each show target and feature contract, split behavior, leakage controls,
metric meaning, tuning burden, compute, visible output, benefit, tradeoff, and
limitation. Do not add algorithms to make a larger contest.

### 4. Build the leakage and partition record

| Element | Scientific meaning | Availability time | Fit subset | Transform subset | Leakage risk | Verification |
|---|---|---|---|---|---|---|
| Target | | | | | | |
| Feature or transform | | | | | | |
| Participant or group key | | | | | | |
| Time or session key | | | | | | |
| Preprocessing statistic | | | | | | |
| Model-selection signal | | | | | | |

Check:

- duplicate or related observations across folds;
- preprocessing fitted outside training folds;
- target-derived, future, post-outcome, site, batch, or acquisition leakage;
- tuning and evaluation on the same resamples;
- repeated use of an untouched test set;
- class, group, and time support in every split;
- metric and threshold alignment with the intended use.

### 5. Document the exact preprocessing and computation

Show:

- `Pipeline` or equivalent ordered steps;
- `ColumnTransformer` and feature-name behavior where applicable;
- splitter, groups, seeds, folds, repeats, and nesting;
- estimator parameters and defaults;
- bounded search space and total fit count;
- scoring, refit behavior, calibration, and uncertainty;
- parallel jobs, memory, cache, and compute limits;
- warnings and failure criteria.

Unsupervised labels, components, embeddings, feature importance, partial
dependence, and error-analysis patterns are exploratory representations, not
scientific entities or causes.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- pipeline, splitter, estimator set, search space, fit budget, seeds, metrics,
  baseline, and output destination;
- training or tuning operation;
- no-test-contact boundary.

Reopen Gate 2 before first access to the untouched test set, a new tuning
space, threshold selection, calibration change, estimator addition, or model
refit on broader data.

### 7. Fit and verify the approved checkpoint

Run only the approved checkpoint. Capture:

- code, data, feature, split, environment, and version hashes;
- fold membership at the authorized disclosure level;
- pipeline and estimator parameters;
- fit count, compute, warnings, failures, and seeds;
- per-fold and aggregate metrics with variability;
- baseline comparison and approved sensitivities;
- held-out metrics only when separately approved;
- specification deviations and artifacts.

Return:

```text
Scikit-learn Pipeline Record
Approved task and prediction unit:
Versions and API:
Target, features, and provenance:
Partition and leakage record:
Pipeline and estimator:
Tuning space, compute, and seeds:
Validation and baseline results:
Held-out results, if approved:
Calibration and sensitivity checks:
Warnings, failures, and deviations:
Specification-conformance check:
What the results do not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never fit a transformer, selector, imputer, scaler, or model on the test set.
- Keep all learned preprocessing inside the approved resampling pipeline.
- Respect participant, family, item, site, session, batch, and time
  dependencies in splitting.
- A cross-validation score does not justify an unapproved model, metric, or
  search space.
- Do not call a cross-validation winner the best scientific model.
- Do not reuse an untouched test set for tuning, feature decisions, or
  narrative selection.
- Clusters, embeddings, components, and feature importance do not establish
  natural groups, mechanisms, causality, or anatomical meaning.
- Stop on unresolved leakage, insufficient fold support, incompatible API,
  unbounded search, or unapproved holdout access.

## Pipeline leakage and generalization checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled pipeline cards.** Compare only the fixed baseline and user-approved estimator or representation routes. This prevents automatic algorithm contests. This may leave performance opportunities unexplored. This depends on the approved candidate set.
- **Pipeline Decision Record.** Show leakage, split, preprocessing, metric, tuning, and compute records. This makes optimistic-bias risks visible. This requires detailed data-timing knowledge. Some leakage can remain undocumented upstream.
- **Scikit-learn Pipeline Record.** Execute one approved checkpoint and keep the holdout sealed until reapproval. This preserves a valid evaluation boundary. This slows iterative exploration. One validation design may be fragile.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended validity matrix.** Add negative controls, permutation tests, and external validation plans. This tests selected failure modes. This adds data access, compute, and scientific decisions. Negative controls cannot cover every bias.
- **Generalization verification bundle.** Run prespecified external, temporal, or multisite validation. This tests transport beyond internal folds. This requires additional governed data. External performance still does not prove mechanism.
- **Nested-validation comparison plan.** Add a prespecified nested comparison set. This improves comparative evaluation. This adds fits, compute, and multiplicity. This still reflects a bounded candidate library.

## Checks

- **Positive:** a grouped classification specification produces split-aware
  preprocessing, grouped folds, bounded tuning, and no test contact.
- **Negative:** `find the best classifier` does not trigger an automatic
  comparison.
- **Leakage:** a post-outcome feature stops the pipeline before fitting.
- **Edge:** sparse classes or groups that cannot support the approved splitter
  return a design failure.
- **Unsupervised:** cluster labels remain exploratory and are not named as
  scientific groups.
- **Handoff:** descriptive issues return to [exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md);
  general execution may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- scikit-learn. (n.d.-a). *Common pitfalls*. https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn. (n.d.-b). *Pipelines and composition*. https://scikit-learn.org/stable/modules/compose.html
- scikit-learn. (2026). *scikit-learn* (Version 1.9.0) [Computer software]. GitHub. https://github.com/scikit-learn/scikit-learn/releases/tag/1.9.0
