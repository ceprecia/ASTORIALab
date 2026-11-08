---
name: svm
description: >-
  Implements one already approved scikit-learn SVC or LinearSVC outer-evaluation
  or final-refit checkpoint on fixed keyed tabular or ROI features, then returns
  a split, pipeline, prediction or model-state, convergence, verification, and
  provenance record. Use when the request names this skill or
  neural-decoding-analysis, fmri-coordinator, smri-coordinator, or scikit-learn routes one
  exact SVM handoff. It makes one-to-one joins, feature timing, scaling,
  imputation, groups, outer and inner partitions, estimator form, kernel, C,
  gamma, penalty, loss, class order, decision scores, calibration, metrics,
  compute, writes, and sealed-test boundaries visible. It does not choose SVM or
  a target, install software, create features, ignore dependence, use pooled
  cross_val_predict metrics by default, enable hidden probability calibration,
  diagnose people, treat weights as neural effects, overwrite, or automatically
  refit after evaluation. Triggers: train an SVM on my features, SVC outer
  evaluation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: multimodal
  dependencies: ""
  requires: Python, scikit-learn
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# SVM

Implement one approved support-vector classification checkpoint without
turning cross-validation output or model weights into diagnostic, causal, or
neurobiological evidence.

## Purpose

`svm` owns:

- one exact outer-evaluation checkpoint with inner tuning and optional
  approved calibration, or one final-refit and model-export checkpoint after
  evaluation decisions are frozen;
- exact sample, participant, session, feature, target, class, group, fold,
  and ordering identity;
- exact `SVC` or `LinearSVC` implementation, kernel, `C`, `gamma`, degree,
  coefficient offset, penalty, loss, dual formulation, class weighting,
  tolerance, iteration, cache, and compute behavior;
- placement of scaling, imputation, feature selection, and calibration inside
  the applicable training folds;
- preservation of fold-specific predictions, decision scores, class order,
  metrics, selected parameters, coefficients or support-vector state,
  warnings, failures, writes, and provenance;
- an SVM Operation Record and neutral decoding-QC handoff.

The user owns the scientific question, target, prediction unit, estimand,
confirmatory status, feature set, confounds, groups, split hierarchy,
estimator candidates, hyperparameter bounds, preprocessing, calibration,
metrics, thresholds, nulls, multiplicity, final-refit decision,
interpretation, and claims.

[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns target, generalization, estimator-family,
partition, metric, null, multiplicity, and claim design. [scikit-learn](../scikit-learn/SKILL.md)
owns broader pipelines, non-SVM estimators, and mixed-model comparisons.
[fmri-coordinator](../fmri-coordinator/SKILL.md) and [smri-coordinator](../smri-coordinator/SKILL.md) route modality preparation. This skill owns
only SVM-specific implementation after the method is selected. These are
handoffs, not dependencies or an automatic chain.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `SVM`, `support vector machine`, `support vector
classifier`, `linear classifier`, `kernel classifier`, `disease
classification`, `diagnosis`, `ROI decoding`, `feature importance`, or
another broad method or output phrase.

Do not use this skill to:

- choose SVM, `SVC`, `LinearSVC`, a target, features, splits, metrics, or
  interpretation;
- install, update, configure, or repair scikit-learn or another package;
- create, select, harmonize, residualize, scale, or impute features outside
  the approved training-fold pipeline;
- align features and labels by row order or use an unchecked many-to-many
  join;
- ignore repeated participant, site, family, session, or longitudinal
  dependence;
- pool `cross_val_predict` outputs into a metric by default;
- use `SVC(probability=True)` as hidden calibration;
- combine outer evaluation with final refit under one approval;
- classify a person clinically or treat coefficients, support vectors, or
  decision scores as neural effects, mechanisms, causes, or diagnostic
  markers;
- overwrite or silently reuse an incompatible fitted state.

## Inputs

Obtain or mark missing:

- one approved SVM Decoding Specification from
  [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md);
- one checkpoint: outer evaluation with inner tuning, or final refit and
  model export;
- scientific purpose, exploratory or confirmatory status, prediction unit,
  target timing, class ontology, positive class, and intended generalization
  population;
- immutable keyed feature-label-group manifest with participant, session,
  run, acquisition, feature-row, target, class, site, family, repeat, and
  split keys;
- exact feature allowlist, names, units, provenance, acquisition timing,
  missingness, transformations, target-proxy audit, and ordering;
- exact outer, inner, validation, calibration, and sealed-test partitions
  with hashes;
- approved `SVC` or `LinearSVC` form and applicable kernel, `C`, `gamma`,
  degree, `coef0`, shrinking, penalty, loss, dual, intercept, class weight,
  tolerance, maximum iterations, cache, and multiclass behavior;
- approved scaling, imputation, feature-selection, harmonization, and
  nuisance-adjustment placement inside folds;
- approved tuning bounds and selection rule;
- whether calibrated probabilities are scientifically required, with
  calibration method, partition, grouping, metric, and threshold plan;
- approved per-fold and aggregate metrics, uncertainty, class-support,
  threshold, null, and multiplicity plan;
- selected exact scikit-learn version, environment, public signatures,
  source, license, accepted defaults, and adapter;
- memory, threads, jobs, cache, temporary, destination, collision, rollback,
  and failure policy;
- expected fitted states, predictions, decision scores, probabilities when
  approved, fold metrics, selected parameters, coefficients or support
  vectors, diagnostics, metadata, logs, and hashes;
- sealed-test, model-review, compute, and destination authority.

If the checkpoint, target, sample join, feature provenance, dependence,
partition hierarchy, estimator form, parameter bounds, calibration,
environment, metric, sealed-test boundary, or output contract is unresolved,
stop with **SVM operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one checkpoint

Choose exactly one:

1. **Outer evaluation:** execute the full prespecified outer folds. Perform
   scaling, imputation, feature selection, hyperparameter tuning, and
   calibration only within each outer training partition. Return fold-keyed
   out-of-sample predictions, decision scores, and metrics. Do not final-refit.
2. **Final refit and export:** after estimator, preprocessing,
   hyperparameters, calibration, threshold, and training population are
   frozen, fit once on that approved population and export the fitted
   pipeline. Do not claim new validation performance.

Do not combine the two. Do not use predictions on fitted rows as
generalization evidence.

### 2. Preserve genuine SVM routes

Compare `SVC` and `LinearSVC` only when both remain approved candidates in the
Decoding Specification. Compare bounded kernel, `C`, gamma, penalty, loss,
dual, or calibration routes only when the specification authorizes them.

For each route show:

- workflow and partition change;
- visible outputs;
- mathematical and implementation assumptions;
- compute, scaling, convergence, calibration, coefficient, and
  interpretation effects;
- benefit, tradeoff, and limitation.

If one estimator is fixed, explain it. Do not run an automatic classifier
contest or choose by package convenience.

### 3. Build the SVM Operation Contract

Create:

| Element | Approved meaning | Exact API binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Checkpoint and estimand | | | | |
| Samples, target, and classes | | | | |
| Feature allowlist and timing | | | | |
| Outer, inner, group, and calibration partitions | | | | |
| Scaling, imputation, and feature selection | | | | |
| Estimator, kernel, penalty, and parameters | | | | |
| Scores, calibration, threshold, and metrics | | | | |
| Environment, resources, and writes | | | | |
| Outputs and stop point | | | | |

Every output remains keyed by sample, class, fold, fitted pipeline, and exact
feature order.

### 4. Reconcile identities without silent loss or multiplication

Verify:

- participant, session, feature-row, label, group, and split keys are unique;
- the proposed join is one-to-one and its left-only, right-only, duplicate,
  and conflicting rows are displayed before modeling;
- no inner join silently removes unmatched participants;
- feature and target rows cannot be aligned only by position;
- repeated observations, sites, scanners, families, and sessions stay in the
  approved partition groups;
- every fold preserves the required class and group support;
- the target timing matches the prediction claim;
- class labels and the positive class are explicit.

Any duplicate multiplication, unexplained row loss, or order ambiguity stops.

### 5. Audit features and leakage

For every feature record:

- scientific definition, unit, source, acquisition time, processing history,
  and allowlist status;
- whether it can proxy the target, post-outcome state, site, scanner,
  treatment, enrollment, exclusion, or data-collection artifact;
- missingness and whether missingness can reveal the target or split;
- scaling, imputation, residualization, harmonization, feature selection, and
  dimensionality-reduction state;
- whether each learned transform is fitted only within the applicable
  training fold;
- numeric type, finite state, constant state, and range.

Pre-scaled or outcome-selected features require auditable train-only
provenance. If that cannot be established, stop.

### 6. Preflight estimator and calibration semantics

For scikit-learn `1.9.0`:

- `SVC` defaults to `C=1`, RBF kernel, `gamma='scale'`, 200 MB kernel cache,
  no iteration limit, and one-versus-one training with an OVR-shaped decision
  output by default. Fit time scales at least quadratically with samples.
- `LinearSVC` defaults to L2 penalty, squared-hinge loss, automatic
  primal-versus-dual choice, `C=1`, OVR multiclass, and 1000 maximum
  iterations. It is not numerically identical to linear-kernel `SVC`.
- `SVC(probability=True)` uses additional internal five-fold calibration and
  is deprecated in `1.9.0` for removal in `1.11`. The current documented
  replacement is an explicitly configured `CalibratedClassifierCV` route.

Probability calibration is a separate selected design element. Its splits,
groups, estimator state, and evaluation remain inside the outer training
boundary. Decision scores and probabilities are not interchangeable.

Inspect the participant's selected scikit-learn version and API before execution. Use matching primary documentation; missing or incompatible dependencies do not authorize installation, updates or silent version substitution.

### 7. Audit evaluation semantics

Use per-fold scoring or one explicitly approved out-of-fold aggregation rule.
Current scikit-learn documentation warns that metrics computed from
`cross_val_predict` outputs can differ from valid foldwise evaluation unless
test folds are equal in size and the metric decomposes over samples.

Therefore:

- do not pool out-of-fold predictions for AUC by default;
- do not call `cross_val_predict` separately for predictions and
  probabilities, which refits the pipeline twice;
- record the exact class order for every decision-score or probability
  column;
- keep threshold selection and calibration inside training data;
- keep the sealed outer test inaccessible until the exact Gate 2 checkpoint.

### 8. Gate 1: approve contract and read-only preflight

Show:

- fixed checkpoint, estimand, target, population, and claim boundary;
- genuine route comparison or explained fixed route;
- completed Operation Contract;
- identity-join, feature-timing, leakage, group, split, class-support,
  calibration, environment, resource, and collision audit;
- exact version, source, signatures, license, and local availability evidence
  to inspect;
- metrics, outputs, verification, and stop point;
- unresolved assumptions and prohibited clinical or biological claims.

Gate 1 authorizes only bounded manifest, schema, version, signature, resource,
collision, and destination inspection plus exact code construction. It does
not authorize fitting, tuning, calibration, output writing, model viewing, or
sealed-test access.

### 9. Construct and inspect the exact checkpoint

Display:

- exact interpreter, environment, scikit-learn version, source, and adapter;
- immutable keyed feature, target, group, and partition manifests;
- exact preprocessing pipeline and fold placement;
- estimator class, kernel, penalty, loss, `C`, gamma, degree, dual,
  intercept, class weight, tolerance, iterations, cache, randomness, and
  accepted defaults;
- tuning and calibration partitions and selection rules;
- class order, decision-score, probability, threshold, per-fold metric, and
  uncertainty semantics;
- memory, jobs, threads, cache, temporary, destination, collision,
  atomic-write, rollback, and failure behavior;
- expected fitted pipelines, artifacts, metadata, logs, and hashes;
- exact stop before refit, retuning, holdout access, feature attribution,
  interpretation, or clinical use.

Structure-only or synthetic tests may check pipeline and split wiring only
when separately approved. They do not validate observed-data performance.

### 10. Gate 2: approve one exact checkpoint

Ask the user to approve the displayed checkpoint, immutable inputs and splits,
pipeline, parameters, accepted defaults, resources, reads, writes, outputs,
verification, sealed-test rule, and stop point.

Gate 2 authorizes only the full enumerated outer-evaluation set or one final
refit, never both. A changed feature, target, join, group, fold, estimator,
kernel, `C`, gamma, penalty, loss, scaling, imputation, calibration, metric,
threshold, environment, destination, retry, holdout access, or refit requires
a new Gate 2.

### 11. Execute once and preserve evidence

Record:

- environment, feature, target, join, group, and split identities;
- exact code, pipeline, parameters, accepted defaults, and hashes;
- start and end time, process state, stdout, stderr, warnings, and failures;
- per-fold training, tuning, calibration, validation, and test membership;
- selected parameters, convergence, cache, memory, jobs, temporary, and
  write behavior;
- sample-and-class-keyed predictions, decision scores, and approved
  probabilities;
- fold metrics, uncertainty, fitted state, coefficients or support-vector
  state, diagnostics, metadata, logs, and hashes;
- partial, missing, implicit, or unexpected artifacts;
- deviations from the approved contract.

Do not rerun a fold, change a feature or parameter, inspect the holdout,
remove a participant, recalibrate, change a threshold, or final-refit after
evaluation without new approval.

### 12. Verify and stop

Separate:

1. **Execution conformance:** exact environment, join, features, partitions,
   pipeline, resources, writes, warnings, and deviations.
2. **Structural verification:** sample and class identities, fold coverage,
   feature order, prediction and score shapes, fitted-state integrity,
   coefficient or support-vector semantics, finite state, and hashes.
3. **Evaluation evidence:** fold-specific metrics, approved aggregation,
   uncertainty, class support, convergence, calibration, and sealed-test
   integrity.
4. **Scientific decision:** the user decides adequacy, refit, sensitivity work,
   threshold use, interpretation, and claims.

Return:

```text
SVM Operation Record
Approved checkpoint, estimand, population, target, and class ontology:
Feature-label-group join and sample manifest:
Feature allowlist, timing, preprocessing, and leakage audit:
Outer, inner, calibration, validation, and sealed-test partitions:
Estimator, kernel, penalty, parameters, class weight, and convergence:
Exact environment, version, source, pipeline, and accepted defaults:
Resources, cache, temporary files, destinations, and writes:
Exit state, warnings, failures, and deviations:
Fold-keyed predictions, scores, probabilities, metrics, and uncertainty:
Fitted-state, coefficient or support-vector, diagnostic, metadata, and hash inventory:
Execution-conformance and structural-verification result:
Generalization, calibration, weight-interpretation, and clinical limitations:
user-owned interpretation and next decision:
```

## Boundaries

- Stop without an approved SVM Decoding Specification and one checkpoint.
- Stop on duplicate, missing, reordered, multiplied, or silently dropped
  sample identities.
- Stop when feature timing, allowlist, scaling, missingness, or train-only
  preprocessing provenance is unresolved.
- Stop when partitions ignore participant, site, family, session, or other
  approved dependence.
- Stop when estimator form, kernel, `C`, gamma, penalty, loss, class order,
  calibration, threshold, metric, or exact package version is implicit.
- Stop before installation, overwrite, cleanup, retry, hidden calibration,
  early holdout access, retuning, or final refit.
- Preserve decision-score, probability, prediction, and threshold
  distinctions.
- Linear coefficients and support vectors are conditional model parameters,
  not direct feature importance, neural effects, mechanisms, causes, or
  diagnostic markers.
- Predictive discrimination does not establish diagnosis, clinical utility,
  construct validity, causality, or transport.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Cortes & Vapnik. (1995). Support-vector networks. https://doi.org/10.1007/BF00994018
- Haufe et al. (2014). On the interpretation of weight vectors of linear models in multivariate neuroimaging. https://doi.org/10.1016/j.neuroimage.2013.10.067
- *scikit-learn* (Version 1.9.0) [Computer software]. (2026, June 2). GitHub. https://github.com/scikit-learn/scikit-learn/releases/tag/1.9.0
- *sklearn.model_selection.cross_val_predict*. (n.d.). scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html
- *sklearn.svm.LinearSVC*. (n.d.). scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
- *sklearn.svm.SVC*. (n.d.). scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
