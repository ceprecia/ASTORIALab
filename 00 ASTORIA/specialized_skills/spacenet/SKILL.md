---
name: spacenet
description: >-
  Implements one already approved Nilearn SpaceNetClassifier outer-evaluation or
  final-refit checkpoint on fixed aligned volumetric neuroimaging inputs, then
  returns a split, parameter, prediction or coefficient, convergence,
  verification, and provenance record. Use when the request names this skill or
  neural-decoding-analysis, fmri-coordinator, smri-coordinator, or nilearn-tool routes one
  exact SpaceNet handoff. It makes sample and class identity, common space,
  mask, outer and inner partitions, groups, screening, standardization, penalty,
  alpha path, L1 ratio, solver, compute, coefficient-map semantics, package
  compatibility, writes, and sealed-test boundaries visible. It does not choose
  SpaceNet or a target, install packages, preprocess images, use in-sample
  predictions as validation, inspect a holdout early, diagnose people, treat
  weights as neural effects, overwrite, or automatically refit after evaluation.
  Triggers: SpaceNet classifier on my volumes, nilearn SpaceNet.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: Python, Nilearn
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# SpaceNet

Implement one approved spatially structured classification checkpoint without
turning a sparse coefficient map into a diagnostic or neurobiological claim.

## Purpose

`spacenet` owns:

- one exact outer-evaluation checkpoint with inner model selection, or one
  final-refit and coefficient-export checkpoint after evaluation decisions
  are frozen;
- exact sample, participant, session, image, class, group, fold, mask, space,
  and ordering identity;
- exact Graph-Net or TV-L1 penalty, loss, alpha path, L1 ratios, screening,
  standardization, intercept, solver, convergence, memory, cache, and compute
  behavior;
- version and dependency compatibility between Nilearn, scikit-learn, and
  their runtime environment;
- preservation of fold-specific predictions, decision scores, class order,
  selected parameters, coefficient maps, warnings, failures, writes, and
  provenance;
- a SpaceNet Operation Record and neutral decoding-QC handoff.

The user owns the scientific question, target, prediction unit, estimand,
confirmatory status, input images, mask, confounds, groups, split hierarchy,
penalty candidates, hyperparameter bounds, screening, standardization,
metrics, thresholds, nulls, multiplicity, refit decision, coefficient use,
interpretation, and claims.

[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns target, estimator-family, generalization,
partition, metric, null, multiplicity, and claim design. [fmri-coordinator](../fmri-coordinator/SKILL.md) and
[smri-coordinator](../smri-coordinator/SKILL.md) route modality preparation. [nilearn-tool](../nilearn-tool/SKILL.md) owns separately
approved generic image, masker, cache, and file operations. This skill owns
only SpaceNet-specific implementation after the method is selected. These are
handoffs, not dependencies or an automatic chain.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `SpaceNet`, `spatial classifier`, `Graph-Net`, `TV-L1`,
`voxel-wise decoding`, `disease classification`, `diagnosis`, `coefficient
map`, `brain prediction`, or another broad method or output phrase.

Do not use this skill to:

- choose SpaceNet, the prediction target, image representation, mask, split,
  penalty, metric, or interpretation;
- install, update, configure, or repair Nilearn, scikit-learn, or another
  dependency;
- preprocess, register, resample, smooth, harmonize, residualize, or create
  input images;
- fit all samples and predict those same samples as evidence of
  generalization;
- select features, penalties, alphas, L1 ratios, or thresholds using sealed
  test labels;
- combine outer evaluation with final refit and coefficient export under one
  approval;
- classify a person clinically, claim diagnosis support, or treat
  coefficient weights as neural effects, mechanisms, causes, or anatomical
  localization;
- overwrite or silently reuse caches or fitted states.

## Inputs

Obtain or mark missing:

- one approved SpaceNet Decoding Specification from
  [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md);
- one checkpoint: outer evaluation with inner selection, or final refit and
  coefficient export;
- scientific purpose, exploratory or confirmatory status, prediction unit,
  target timing, class ontology, positive class, and intended generalization
  population;
- immutable keyed image-label-group manifest with participant, session, run,
  acquisition, image, target, class, group, site, family, and repeat keys;
- exact outer, inner, validation, and sealed-test partitions with hashes and
  indices relative to each current training subset;
- acquisition and preprocessing provenance, including registration,
  resampling, smoothing, filtering, scaling, confound handling,
  harmonization, feature selection, and target-access history;
- image shape, affine, orientation, space, resolution, dtype, finite state,
  and common-mask evidence;
- approved mask source and geometry, with train-only or fixed-external
  provenance;
- selected Graph-Net or TV-L1 penalty, loss, alphas or alpha-grid rule,
  `n_alphas`, L1 ratios, path length, intercept, positivity, debiasing,
  maximum iterations, tolerance, and convergence policy;
- approved standardization, temporal filtering, TR, target affine, target
  shape, and screening policy;
- selected exact Nilearn and compatible scikit-learn releases, environment,
  public signatures, sources, licenses, dependency state, and adapter;
- approved per-fold and aggregate metrics, uncertainty, class-support,
  calibration, threshold, null, and multiplicity plan;
- memory, threads, jobs, cache, temporary, destination, collision, rollback,
  and failure policy;
- expected fitted states, predictions, decision scores, fold metrics,
  selected parameters, coefficient maps, class mapping, diagnostics, logs,
  metadata, and hashes;
- sealed-test, coefficient-review, compute, and destination authority.

If the checkpoint, target, sample identity, geometry, split hierarchy,
groups, screening, penalty, hyperparameter path, compatible environment,
metric, sealed-test boundary, or output contract is unresolved, stop with
**SpaceNet operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one checkpoint

Choose exactly one:

1. **Outer evaluation:** run the complete preapproved outer folds, with all
   preprocessing, screening, and parameter selection confined to the
   corresponding outer training data. Return fold-keyed out-of-sample
   predictions and metrics. Do not final-refit.
2. **Final refit and coefficient export:** after evaluation choices and the
   intended training population are frozen, fit once on that approved
   population and export the fitted state and class-mapped coefficient maps.
   Do not claim new validation performance.

Do not combine the two. Do not treat predictions on the fitted data as
evaluation.

### 2. Preserve genuine SpaceNet routes

Compare Graph-Net and TV-L1 only when both remain approved candidates in the
Decoding Specification. Compare bounded alpha, L1-ratio, screening, or
standardization routes only when the specification authorizes them.

For each route show:

- exact workflow and partition change;
- visible outputs;
- evidence and assumptions;
- leakage, compute, convergence, coefficient, and interpretation effects;
- benefit, tradeoff, and limitation.

If one route is fixed, explain it. Do not run an automatic classifier contest
or choose the visually sparsest map.

### 3. Build the SpaceNet Operation Contract

Create:

| Element | Approved meaning | Exact API binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Checkpoint and estimand | | | | |
| Samples, target, and classes | | | | |
| Outer, inner, and group partitions | | | | |
| Images, space, and mask | | | | |
| Preprocessing and standardization | | | | |
| Penalty, loss, and parameter path | | | | |
| Screening and leakage control | | | | |
| Metrics and sealed test | | | | |
| Environment, resources, and writes | | | | |
| Outputs and stop point | | | | |

Every prediction and score must remain keyed by sample, class, outer fold,
and fitted state.

### 4. Audit identity, geometry, and target timing

Verify:

- image, label, participant, session, group, and split keys form a strict
  one-to-one manifest with no silent row-order alignment;
- repeated observations, families, sites, scanners, and sessions remain in
  the correct partition groups;
- targets were measured at the approved time and cannot be reconstructed from
  acquisition or preprocessing artifacts;
- all images share the approved volume shape, affine, orientation, space,
  resolution, preprocessing, and mask meaning;
- the mask is fixed externally or learned only inside the applicable
  training boundary;
- no target-informed feature selection, harmonization, scaling, nuisance
  adjustment, exclusion, or mask creation occurred before partitioning;
- every inner and outer fold contains the approved class and group support;
- surface inputs stop because the reviewed `SpaceNetClassifier.fit` path
  accepts volumetric Niimg-like inputs, not a surface workflow; fitted
  prediction methods may also accept a correctly shaped matrix;
- memory and cache estimates fit the approved environment.

Equal array shape does not prove common anatomical space.

### 5. Audit screening and nested evaluation

The reviewed Nilearn `0.14.0` source applies target-aware univariate screening
to the full data supplied to one internal SpaceNet fit before it slices that
data into its internal train and validation indices.

Therefore:

- an outer evaluation must pass only the current outer-training subset to
  each fitted SpaceNet model, keeping the outer test sealed;
- the built-in internal CV scores can still be biased by screening that saw
  all outer-training labels, including each inner validation subset;
- strict inner leakage control requires an approved route, commonly
  disabling built-in screening with `screening_percentile=100` and accepting
  the compute cost, or implementing an explicitly nested alternative outside
  this fixed estimator path;
- `screening_percentile=20` is a target-aware feature-selection choice, not a
  harmless speed default;
- any screening sensitivity set is prespecified and remains inside the outer
  boundary.

Do not weaken this boundary because the output is called cross-validated.

### 6. Preflight exact API and compatibility

Nilearn `0.14.0` `SpaceNetClassifier` defaults include Graph-Net, logistic
loss, L1 ratio `0.5`, ten automatically generated alphas, 200 iterations,
tolerance `1e-4`, `memory_level=1`, standardization enabled, one job, path
ratio `1e-3`, eight-fold internal CV, an intercept, 20-percent screening, no
debiasing, and unconstrained signs. Every applicable value is explicit.

Use a version-matched explicit standardization form because the Boolean
default is deprecated for a planned `0.15.0` semantic change. Record
`classes_`, `cv_`, `cv_scores_`, `best_model_params_`, `coef_`,
`coef_img_`, mask, corrected screening percentage, warnings, and fitted
state. Preserve binary and multiclass score and coefficient mappings.

Nilearn `0.14.0` declares
`scikit-learn!=1.7.0,!=1.9.0,>=1.5.0`. The current scikit-learn `1.9.0`
release is therefore incompatible with that Nilearn release. Check the participant's selected Python environment against the exact dependency requirements. Missing or incompatible packages stop this route without authorizing installation or environment resolution.

### 7. Gate 1: approve contract and read-only preflight

Show:

- fixed checkpoint, estimand, target, population, and claim boundary;
- genuine route comparison or explained fixed route;
- completed Operation Contract;
- identity, target-timing, geometry, mask, partition, group, screening,
  leakage, class-support, resource, and collision audit;
- exact package versions, source, signatures, licenses, and compatibility
  evidence to inspect;
- metrics, outputs, verification, and stop point;
- unresolved assumptions and prohibited clinical or biological claims.

Gate 1 authorizes only bounded manifest, header, schema, version, signature,
compatibility, resource, cache, collision, and destination inspection plus
exact code construction. It does not authorize full image loading, fitting,
screening, cache creation, output writing, coefficient viewing, or sealed-test
access.

### 8. Construct and inspect the exact checkpoint

Display:

- exact interpreter, compatible environment, package versions, sources, and
  adapter;
- immutable keyed image, target, group, mask, and split manifests;
- exact outer and inner indices, relative-index translation, and sealed-test
  rule;
- penalty, loss, alphas, L1 ratios, screening, standardization, filtering,
  mask, affine, shape, solver, convergence, and accepted defaults;
- per-fold metrics, class order, prediction, decision-score, coefficient-map,
  and final-refit semantics;
- memory, jobs, threads, cache, temporary, destination, collision,
  atomic-write, rollback, and failure behavior;
- expected fitted states, artifacts, metadata, logs, and hashes;
- exact stop before refit, retuning, holdout access, visualization,
  interpretation, or clinical use.

Structure-only or synthetic tests may check the call and split wiring only
when separately approved. They do not validate observed-data performance.

### 9. Gate 2: approve one exact checkpoint

Ask the user to approve the displayed checkpoint, immutable inputs and splits,
parameters, accepted defaults, resources, caches, reads, writes, outputs,
verification, sealed-test rule, and stop point.

Gate 2 authorizes only the full enumerated outer-evaluation set or one final
refit, never both. A changed image, target, group, fold, mask, penalty, alpha,
L1 ratio, screening, standardization, metric, threshold, environment,
destination, retry, test access, coefficient transformation, or refit
requires a new Gate 2.

### 10. Execute once and preserve evidence

Record:

- package, environment, image, target, group, mask, and split identities;
- exact code, parameters, accepted defaults, and hashes;
- start and end time, process state, stdout, stderr, warnings, and failures;
- per-fold training, validation, and test membership;
- selected parameters, convergence, cache, memory, jobs, temporary, and
  write behavior;
- sample-and-class-keyed predictions and decision scores;
- fold-and-class-keyed coefficient maps and fitted states when authorized;
- metrics, uncertainty, diagnostics, metadata, and logs;
- partial, missing, implicit, or unexpected artifacts;
- deviations from the approved contract.

Do not rerun a fold, alter screening, inspect the holdout, drop a participant,
select a coefficient map, or final-refit after evaluation without new
approval.

### 11. Verify and stop

Separate:

1. **Execution conformance:** exact environment, inputs, partitions,
   parameters, resources, writes, warnings, and deviations.
2. **Structural verification:** sample and class identities, fold coverage,
   image and mask geometry, prediction and score shape, coefficient and class
   mapping, finite state, artifacts, and hashes.
3. **Evaluation evidence:** fold-specific metrics, approved aggregation,
   uncertainty, class support, convergence, screening, and sealed-test
   integrity.
4. **Scientific decision:** the user decides adequacy, refit, sensitivity work,
   coefficient use, interpretation, and claims.

Return:

```text
SpaceNet Operation Record
Approved checkpoint, estimand, population, target, and class ontology:
Image, label, group, mask, space, and sample manifest:
Outer, inner, validation, and sealed-test partitions:
Preprocessing, target-timing, geometry, and leakage audit:
Penalty, loss, alpha, L1-ratio, screening, standardization, and solver state:
Exact compatible environment, versions, sources, call, and defaults:
Resources, cache, temporary files, destinations, and writes:
Exit state, warnings, failures, and deviations:
Fold-keyed predictions, scores, metrics, selected parameters, and uncertainty:
Class-keyed coefficient, fitted-state, diagnostic, metadata, and hash inventory:
Execution-conformance and structural-verification result:
Generalization, coefficient-interpretation, and clinical limitations:
user-owned interpretation and next decision:
```

## Boundaries

- Stop without an approved SpaceNet Decoding Specification and one checkpoint.
- Stop on duplicate, missing, reordered, or multiplied sample identities.
- Stop on mixed image spaces, affines, masks, preprocessing states, or surface
  inputs.
- Stop when partitions ignore repeated participant, site, family, session, or
  other approved dependence.
- Stop when screening, standardization, penalty, alpha path, L1 ratios,
  convergence, class mapping, or compatible package versions are implicit.
- Stop if Nilearn `0.14.0` is paired with scikit-learn `1.9.0`.
- Stop before installation, environment repair, automatic mask creation,
  cache creation, overwrite, retry, early holdout access, retuning, or refit.
- Preserve out-of-sample and in-sample distinctions.
- Coefficient maps are conditional decoder parameters, not direct effects,
  anatomical sources, mechanisms, causes, or diagnostic regions.
- Predictive discrimination does not establish diagnosis, clinical utility,
  construct validity, causality, or transport to another population.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Grosenick et al. (2013). Interpretable whole-brain prediction analysis with GraphNet. https://doi.org/10.1016/j.neuroimage.2012.12.062
- Haufe et al. (2014). On the interpretation of weight vectors of linear models in multivariate neuroimaging. https://doi.org/10.1016/j.neuroimage.2013.10.067
- *Nilearn* (Version 0.14.0) [Computer software]. (2026). GitHub. https://github.com/nilearn/nilearn/releases/tag/0.14.0
- Nilearn. (n.d.). *nilearn.decoding.SpaceNetClassifier*. https://nilearn.github.io/stable/modules/generated/nilearn.decoding.SpaceNetClassifier.html
- Nilearn. (n.d.). *SpaceNet*. https://nilearn.github.io/stable/decoding/space_net.html
