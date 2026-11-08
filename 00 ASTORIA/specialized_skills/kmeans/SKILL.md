---
name: kmeans
description: >-
  Implements one already approved scikit-learn full KMeans fit, predict,
  transform, score, or structural-verification operation on a fixed prepared
  neuroimaging feature matrix, then returns a centroid, label or distance,
  convergence, verification, and provenance record. Use when the request names
  this skill or neural-population-analysis-guide, fmri-coordinator, smri-coordinator, or
  scikit-learn routes one exact KMeans handoff. It makes row grain, feature
  meaning, scaling, Euclidean assumptions, cluster count, initialization,
  restart count, seed, convergence, inertia, label permutation, spatial
  disconnectedness, writes, and downstream boundaries visible. It does not
  choose clustering or cluster count, create features, install software, infer a
  parcellation from raw images, select a run from attractive maps, reconstruct
  label images, overwrite, name clusters, or interpret results. Triggers: k
  means on my neuroimaging features, sklearn KMeans.
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

# KMeans

Implement one approved full scikit-learn `KMeans` operation on an already
prepared neuroimaging representation without treating arbitrary cluster
labels or compact Euclidean groups as biological regions.

## Purpose

`kmeans` owns:

- one exact full `KMeans.fit`, `predict`, `transform`, `score`, or
  structural-verification operation;
- exact row identity, row grain, feature identity, scaling, matrix
  orientation, and input role;
- exact cluster count, initialization, restart count, algorithm, tolerance,
  maximum iterations, seed, copy behavior, and accepted defaults;
- preservation of fitted-state identity, centers, labels, inertia,
  iteration count, distances, warnings, failures, writes, and provenance;
- explicit label-permutation, initialization sensitivity, Euclidean-shape,
  and spatial-disconnectedness boundaries;
- a KMeans Operation Record and neutral label or distance handoff.

The user owns the scientific question, need for KMeans, unit of clustering,
feature construction, scaling, cluster count, initialization and sensitivity
plan, stability criteria, fitted-state reuse, downstream mapping, cluster
meaning, interpretation, and claims.

[neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md) owns clustering-method and latent-model
selection. [scikit-learn](../scikit-learn/SKILL.md) owns broader classical machine-learning pipelines
and generic non-neuroimaging clustering. [fmri-coordinator](../fmri-coordinator/SKILL.md) and [smri-coordinator](../smri-coordinator/SKILL.md)
route modality-specific preparation. [nilearn-tool](../nilearn-tool/SKILL.md) or [nibabel-skill](../nibabel-skill/SKILL.md)
owns any separately approved image-to-feature or label-to-image operation.
These are handoffs, not dependencies or an automatic chain.

This skill owns full scikit-learn `KMeans`. It does not silently substitute
`MiniBatchKMeans`, Nilearn `Parcellations(method="kmeans")`, spherical
k-means, constrained clustering, or another estimator.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `KMeans`, `K-means`, `k-means clustering`, `clustering`,
`parcellation`, `centroids`, `cluster the brain`, `brain atlas`, or another
broad method or output phrase.

Do not use this skill to:

- choose KMeans, cluster count, feature representation, scaling, or
  initialization;
- derive features from raw fMRI, sMRI, diffusion, surface, or other data;
- install, update, configure, or repair scikit-learn;
- select a seed, restart, cluster count, or fitted solution after inspecting
  preferred maps or downstream outcomes;
- reconstruct a label image, plot clusters, derive a connectome, train a
  downstream model, or run group statistics automatically;
- treat center proximity, low inertia, or visible separation as a validated
  biological state;
- overwrite or silently reuse a fitted estimator with incomplete provenance.

## Inputs

Obtain or mark missing:

- one approved KMeans Method Specification and one exact operation: fit,
  predict, transform, score, or structural verification;
- scientific purpose and exploratory, methodological, or prespecified status;
- immutable matrix with hash, dimensions, dtype, storage format, and
  finite-state evidence;
- exact row keys and grain, such as voxel, vertex, ROI, participant, trial,
  or another named unit;
- exact feature keys, definitions, units, provenance, missingness,
  preprocessing, centering, scaling, weighting, and acquisition timing;
- training, descriptive, validation, test, prediction, or projection role of
  each matrix;
- approved `n_clusters`, initialization form, `n_init`, seed, algorithm,
  tolerance, maximum iterations, and copy behavior;
- approved sensitivity or stability plan, including whether multiple
  prespecified fits are separate operations;
- exact scikit-learn release, environment, public signature, source, license,
  accepted defaults, and adapter;
- trusted fitted-state source, version, parameter, feature-order, center, and
  serialization identity for predict, transform, score, or verification;
- memory, threads, temporary, destination, collision, rollback, and failure
  policy;
- expected centers, labels, distances, inertia, score, iteration,
  convergence, diagnostic, metadata, log, and hash outputs;
- exact stop before mapping, naming, downstream analysis, or interpretation;
- compute and destination authority.

If the operation, row grain, matrix orientation, scaling, cluster count,
initialization, restart count, fitted-state trust, exact environment, or
output boundary is unresolved, stop with **KMeans operation contract
incomplete**.

## Steps

### 1. Confirm the unit and one operation

State what every row and column means. Then choose exactly one:

1. fit one approved full KMeans estimator on the fixed training or descriptive
   matrix;
2. predict cluster labels for fixed rows using one trusted frozen estimator;
3. transform fixed rows into distances from one trusted frozen center set;
4. score fixed rows through one trusted frozen estimator;
5. inspect existing state or output structure without model execution.

Do not fit and then predict a new dataset, map labels, run sensitivity fits,
or name clusters under the same approval.

### 2. Preserve a genuine route or explain the fixed route

When the approved specification leaves applicable alternatives, compare only
those selected alternatives, such as:

- one initialization strategy versus another;
- one prespecified restart count or seed set versus another;
- one fixed cluster count sensitivity set when the scientific plan already
  authorizes it.

For each show workflow change, visible output, evidence, assumptions, benefit,
tradeoff, compute, and limitation. If the method specification fixes one
route, explain it. Do not automatically search cluster counts or select the
lowest-inertia map across unapproved runs.

### 3. Build the KMeans Operation Contract

Create:

| Element | Approved meaning | Exact API binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Operation and input role | | | | |
| Row grain and identity | | | | |
| Feature meaning and scaling | | | | |
| Cluster count | | | | |
| Initialization and restarts | | | | |
| Algorithm and convergence | | | | |
| Fitted-state identity | | | | |
| Resources and writes | | | | |
| Outputs and stop point | | | | |

KMeans clusters rows in Euclidean feature space. A row-grain, feature-scale,
or orientation error changes the operation even when dimensions are
technically accepted.

### 4. Audit the matrix and leakage boundary

Verify:

- row keys and feature keys are unique, complete, ordered, and immutable;
- features have compatible units or the approved scaling needed for
  Euclidean distances;
- missing, infinite, constant, duplicate, extreme, and near-duplicate rows
  and columns are visible;
- `n_clusters` is positive and does not exceed the number of distinct rows;
- no target, future value, held-out outcome, site proxy, or test result
  entered feature construction, scaling, cluster-count selection, seed
  selection, or fitted-solution selection contrary to the plan;
- preprocessing and scaling for prediction or transform match the exact
  frozen training state and feature order;
- sparse or high-dimensional input implications are explicit;
- matrix, center, and distance-array memory fit the approved environment.

For spatial-unit rows, record that unconstrained KMeans can assign
disconnected voxels or vertices to the same cluster. Do not silently call
those labels contiguous parcels.

### 5. Preflight exact estimator semantics

For scikit-learn `1.9.0`, full `KMeans` defaults to eight clusters,
greedy k-means++ initialization, `n_init='auto'`, 300 maximum iterations,
relative tolerance `1e-4`, no fixed random seed, copy-on-input, and Lloyd's
algorithm.

With k-means++ initialization, `n_init='auto'` performs one run. A one-run
default is not an approved stability plan. Make `n_init`, seed, and
sensitivity behavior explicit. Preserve `n_iter_`, convergence warnings,
centers, labels, and inertia. If the algorithm stops before convergence,
current documentation warns that centers may not equal the means implied by
the final reassigned labels.

Verify scikit-learn in the selected participant environment and use its exact installed signature and behavior. An absent package or incompatible API stops the selected operation; do not install, update or substitute versions automatically.

### 6. Gate 1: approve contract and read-only preflight

Show:

- fixed row grain, operation, and scientific scope;
- genuine route comparison or explained fixed route;
- completed Operation Contract;
- matrix, scaling, leakage, distinct-row, resource, and fitted-state audit;
- exact version, source, signature, license, and environment evidence to
  inspect;
- expected artifacts, writes, verification, and stop point;
- unresolved assumptions and downstream exclusions.

Gate 1 authorizes only bounded schema, metadata, version, signature,
resource, collision, and destination inspection plus exact code
construction. It does not authorize full-matrix fitting, prediction,
transformation, scoring, output creation, plotting, mapping, or held-out
access.

### 7. Construct and inspect the exact call

Display:

- exact interpreter, environment, scikit-learn version, source, and adapter;
- immutable matrix, row, feature, scaling, and fitted-state identities;
- exact constructor and operation arguments;
- cluster count, initialization, restart count, seed, algorithm, tolerance,
  iterations, copy behavior, and accepted defaults;
- memory, thread, temporary, destination, collision, atomic-write, rollback,
  and failure behavior;
- expected centers, labels, distances, inertia, score, convergence,
  diagnostic, metadata, log, and hash artifacts;
- exact stop before another fit, mapping, plotting, or downstream use.

A synthetic matrix may test call construction only when separately approved.
It does not validate the observed clusters.

### 8. Gate 2: approve one exact operation

Ask the user to approve the displayed call, immutable inputs, fitted state,
parameters, accepted defaults, resources, reads, writes, expected artifacts,
verification, and stop point.

Gate 2 authorizes only that operation. A changed matrix, feature order,
scaling, cluster count, initialization, restart count, seed, tolerance,
fitted state, destination, retry, sensitivity fit, label map, plot, or
downstream analysis requires a new Gate 2.

### 9. Execute once and preserve evidence

Record:

- source, environment, matrix, row, feature, and fitted-state identities;
- exact code, parameters, accepted defaults, and hashes;
- start and end time, process state, stdout, stderr, warnings, and failures;
- memory, threads, temporary, destination, and write behavior;
- center, label, distance, inertia, score, iteration, convergence,
  diagnostic, metadata, and log inventories;
- partial, missing, implicit, or unexpected artifacts;
- deviations from the approved contract.

Do not retry, change a seed, increase iterations, select another fit, map
labels, or continue downstream without new approval.

### 10. Verify and stop

Verify:

- fitted feature count, center shape, label count, and distance shape match
  the contract;
- centers and labels are finite and every expected cluster is represented;
- inertia and score semantics are recorded without treating them as
  biological validity;
- iteration count and warnings support the stated convergence status;
- prediction or transform inputs preserve the frozen feature order and
  scaling;
- for spatial rows, connected-component counts per label remain visible;
- label permutation prevents direct cluster-number comparison across fits;
- hashes and provenance reproduce the exact operation.

Return:

```text
KMeans Operation Record
Approved operation, purpose, and input role:
Row grain, row keys, feature definitions, scaling, and matrix identity:
Leakage, distinct-row, and fitted-state audit:
Cluster count, initialization, restarts, seed, algorithm, and convergence:
Exact environment, version, source, API call, and accepted defaults:
Resources, temporary files, destinations, and writes:
Exit state, warnings, failures, and deviations:
Center, label, distance, inertia, score, iteration, and hash inventory:
Execution-conformance and structural-verification result:
Stability, spatial, label-identity, and interpretation limits:
user-owned interpretation and next decision:
```

## Boundaries

- Stop if KMeans, one operation, row grain, or cluster count is not selected.
- Stop on ambiguous orientation, duplicate or missing row keys, unexplained
  scaling, nonfinite values, insufficient distinct rows, or target leakage.
- Stop when initialization, restart count, seed policy, tolerance, or
  sensitivity plan is implicit.
- Stop before installation, overwrite, cleanup, retry, automatic cluster-count
  search, mapping, plotting, naming, or downstream analysis.
- Stop when predict, transform, or score receives an untrusted or
  feature-incompatible fitted state.
- Preserve label permutation and seed sensitivity.
- Low inertia, convergence, compactness, or visually coherent labels do not
  establish anatomical, functional, mechanistic, group, or clinical meaning.

## Checks

- **Positive fit:** one approved fixed matrix, cluster count, explicit
  initialization, restart count, seed, and fresh destination produces one
  fitted-state and label record.
- **Positive transform:** one trusted estimator returns distances with row and
  center identities preserved.
- **Trigger:** only `kmeans` loads this subskill.
- **Generic work:** ordinary tabular clustering routes to
  [scikit-learn](../scikit-learn/SKILL.md).
- **Raw imaging:** raw fMRI or sMRI routes to the modality and preprocessing
  owners before this adapter.
- **Orientation:** a time-by-voxel matrix intended to cluster voxels stops.
- **Scaling:** mixed-unit features with no approved scaling decision stop.
- **Distinct rows:** `n_clusters` greater than distinct rows stops.
- **Defaults:** `n_init='auto'` is exposed as one run under k-means++ in the
  reviewed release, not accepted as a stability design.
- **Convergence:** reaching the iteration limit remains a warning and does not
  trigger an automatic retry.
- **Spatial labels:** disconnected units with one label remain visible and
  are not silently called a parcel.
- **Mapping:** label-image reconstruction is separate, and label zero cannot
  disappear into background.
- **Estimator identity:** Nilearn `Parcellations(method="kmeans")` is not
  treated as full `KMeans`.
- **Version:** an installed release is not treated as a different release.
- **Output:** collisions, new seeds, sensitivity fits, or retries reopen Gate
  2.
- **Interpretation:** cluster numbers and centers are not named as biological
  entities automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- scikit-learn. (n.d.). *sklearn.cluster.KMeans*. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
- scikit-learn. (2026). *scikit-learn* (Version 1.9.0) [Computer software]. GitHub. https://github.com/scikit-learn/scikit-learn/releases/tag/1.9.0
- Thirion et al. (2014). Which fMRI clustering gives good brain parcellations? https://doi.org/10.3389/fnins.2014.00167
