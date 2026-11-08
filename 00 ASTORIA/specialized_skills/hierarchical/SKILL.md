---
name: hierarchical
description: >-
  Implements one already approved scikit-learn AgglomerativeClustering fit,
  fit-and-label, or structural-verification operation on a fixed prepared
  neuroimaging feature matrix, then returns a hierarchy, label, verification,
  and provenance record. Use when the request names this skill or
  neural-population-analysis-guide, fmri-coordinator, smri-coordinator, or scikit-learn
  routes one exact agglomerative-clustering handoff. It makes row grain, feature
  meaning, scaling, distance, linkage, spatial connectivity, cluster or distance
  cut, full-tree behavior, memory, labels, connectedness, writes, and
  no-prediction boundaries visible. It does not choose clustering, create
  features, install software, infer a parcellation from raw images, select a cut
  from attractive results, reconstruct label images, plot a dendrogram
  automatically, overwrite, predict new samples, or interpret clusters.
  Triggers: agglomerative clustering of my features, hierarchical clustering in
  sklearn.
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

# Hierarchical

Implement one approved agglomerative-clustering operation on an already
prepared neuroimaging representation without confusing time points, features,
voxels, vertices, regions, or participants.

## Purpose

`hierarchical` owns:

- one exact `AgglomerativeClustering.fit`, `fit_predict`, or
  structural-verification operation;
- exact row identity, row grain, feature identity, feature scale, matrix
  orientation, and input role;
- exact metric, linkage, connectivity graph, fixed cluster count or distance
  threshold, full-tree, distance-computation, cache, and memory behavior;
- compatibility checks between the selected linkage, metric, connectivity,
  and cut;
- preservation of labels, children, distances when requested, connected
  components, warnings, writes, failures, and provenance;
- a Hierarchical Clustering Operation Record and neutral label handoff.

The user owns the scientific question, need for clustering, unit of clustering,
feature construction, scaling, metric, linkage, spatial constraint, cut,
stability design, validation, downstream mapping, cluster meaning,
interpretation, and claims.

[neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md) owns latent-variable and clustering-method
selection. [scikit-learn](../scikit-learn/SKILL.md) owns broader classical machine-learning pipelines
and generic non-neuroimaging clustering. [fmri-coordinator](../fmri-coordinator/SKILL.md) and [smri-coordinator](../smri-coordinator/SKILL.md)
route modality-specific preparation. [nilearn-tool](../nilearn-tool/SKILL.md) or [nibabel-skill](../nibabel-skill/SKILL.md)
owns any separately approved image-to-feature or label-to-image operation.
These are handoffs, not dependencies or an automatic chain.

This skill implements scikit-learn `AgglomerativeClustering`. It does not
silently substitute Nilearn `HierarchicalKMeans`, feature agglomeration,
spectral clustering, or another algorithm.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `Hierarchical`, `hierarchical clustering`,
`agglomerative clustering`, `Ward clustering`, `parcellation`, `dendrogram`,
`cluster the brain`, `multi-scale atlas`, or another broad method or output
phrase.

Do not use this skill to:

- choose agglomerative clustering or its scientific target;
- derive a feature matrix from raw fMRI, sMRI, diffusion, surface, or tabular
  inputs;
- choose a cluster count, distance threshold, metric, linkage, connectivity,
  or tree cut after inspecting preferred results;
- install, update, configure, or repair scikit-learn;
- map labels back to an image or surface, plot a dendrogram, compute a
  connectome, or run downstream statistics automatically;
- predict labels for new samples, because this estimator has no out-of-sample
  prediction operation;
- treat cluster numbers as stable identities or anatomical truth.

## Inputs

Obtain or mark missing:

- one approved hierarchical-clustering specification and one exact operation:
  fit, fit-and-label, or structural verification;
- scientific purpose and exploratory, methodological, or prespecified status;
- immutable feature matrix with hash, dimensions, dtype, storage format, and
  finite-state evidence;
- exact row keys and row grain, such as voxel, vertex, ROI, participant,
  trial, or another named unit;
- exact column keys, feature definitions, units, provenance, acquisition
  timing, missingness, preprocessing, scaling, and weighting;
- training, descriptive, validation, test, or projection role of the matrix;
- approved metric, linkage, fixed `n_clusters` or `distance_threshold`, and
  whether a full tree and distances are required;
- approved connectivity graph when spatial or other adjacency constraints are
  part of the estimand, with row-key order, shape, directedness, weights,
  symmetry, self-edge, and connected-component semantics;
- approved cache and tree-reuse policy;
- exact scikit-learn version, environment, public signature, source, license,
  accepted defaults, and adapter;
- memory, threads, temporary, destination, collision, rollback, and failure
  policy;
- expected labels, children, distances, cluster sizes, connected-component,
  parameter, diagnostic, log, metadata, and hash outputs;
- stability or sensitivity plan and exact stop before mapping or
  interpretation;
- compute and destination authority.

If row grain, matrix orientation, feature meaning, scaling, metric, linkage,
cut, required connectivity, exact environment, or output boundary is
unresolved, stop with **hierarchical-clustering operation contract
incomplete**.

## Steps

### 1. Confirm the unit and one operation

State exactly what each row is and what each column measures. Then choose:

1. fit and retain one hierarchy without exporting labels beyond the fitted
   state;
2. fit once and return labels for the supplied rows;
3. inspect the structure and provenance of an existing fitted state or label
   output.

Do not combine fitting with image reconstruction, dendrogram plotting,
stability resampling, connectivity analysis, or interpretation.

### 2. Compare only genuine cut or linkage routes

When the approved specification permits alternatives, compare only applicable
routes, such as:

- one fixed cluster count versus one approved distance-threshold cut;
- one selected linkage and compatible metric versus another selected pair;
- one approved spatial-connectivity graph versus an explicitly unstructured
  fit.

For each show the workflow change, output, evidence, assumptions, benefit,
tradeoff, computational effect, and limitation. If the specification fixes
one route, explain the fixed route. Do not invent alternatives or rank cuts
from visual appeal.

### 3. Build the Hierarchical Operation Contract

Create:

| Element | Approved meaning | Exact API binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Operation and input role | | | | |
| Row grain and identity | | | | |
| Feature meaning and scale | | | | |
| Metric and linkage | | | | |
| Connectivity graph | | | | |
| Cluster or distance cut | | | | |
| Full tree and distances | | | | |
| Cache, memory, and writes | | | | |
| Outputs and stop point | | | | |

The label vector always indexes rows. A row-grain error invalidates the
operation even when the estimator exits successfully.

### 4. Audit the matrix and graph

Verify:

- row keys are unique and complete, and their ordering is immutable;
- columns have stable meanings, units, provenance, and approved scaling;
- no target, held-out outcome, site proxy, or future information entered
  feature construction or cut selection contrary to the specification;
- missing, infinite, constant, duplicate, and near-duplicate rows and columns
  are visible;
- sample-to-feature orientation matches the intended clustering unit;
- a precomputed distance matrix is square, ordered, finite, symmetric when
  required, and semantically compatible with the selected metric route;
- connectivity shape is exactly rows by rows and its ordering matches row
  keys;
- connectivity symmetry, connected components, isolated nodes, and
  neighborhood definition match the approved spatial or structural meaning;
- supplied edge values are classified explicitly as adjacency support rather
  than assumed distance weights, and any symmetrization or component
  completion that scikit-learn would perform is shown before approval;
- matrix and tree memory estimates fit the approved environment.

Do not average time series across participants merely to force equal shape.
Do not infer spatial adjacency from row order.

### 5. Preflight exact estimator semantics

For scikit-learn `1.9.0`, `AgglomerativeClustering` defaults to two clusters,
Euclidean metric, Ward linkage, no connectivity constraint, automatic
full-tree behavior, no distance threshold, and no stored merge distances.

Enforce:

- Ward linkage accepts only Euclidean or L2 distance;
- `n_clusters` must be `None` when `distance_threshold` is used;
- a distance threshold requires `compute_full_tree=True`;
- dendrogram distances require the threshold route or
  `compute_distances=True`, with its memory cost;
- `connectivity=None` is unstructured and is not a spatial-parcellation
  constraint;
- every supplied connectivity is symmetrized by adding its transpose; stop
  unless that effective undirected support is the approved graph;
- a graph with more than one connected component is automatically completed
  with added intercomponent edges and a warning; stop unless that exact
  change is scientifically acceptable and explicitly approved;
- supplied nonzero edge values define adjacency support and are replaced by
  estimator-computed distances where distances are needed; stop if the
  intended method requires the supplied values to remain edge weights;
- the fitted estimator has no `predict` method for new rows.

Verify scikit-learn in the selected participant environment and use its exact installed signature and behavior. An absent package or incompatible API stops the selected operation; do not install, update or substitute versions automatically.

### 6. Gate 1: approve contract and read-only preflight

Show:

- fixed row grain, operation, and scientific scope;
- genuine route comparison or explained fixed route;
- completed Operation Contract;
- matrix, feature, leakage, connectivity, and memory audit;
- exact version, source, signature, license, environment, and cache evidence
  to inspect;
- expected labels, tree artifacts, writes, verification, and stop point;
- unresolved assumptions and prohibited downstream actions.

Gate 1 authorizes only bounded schema, metadata, version, signature, cache,
resource, collision, and destination inspection plus exact code
construction. It does not authorize full-matrix fitting, cache creation,
label creation, image reconstruction, plotting, output writing, or held-out
access.

### 7. Construct and inspect the exact call

Display:

- exact interpreter, environment, scikit-learn version, source, and adapter;
- immutable matrix and connectivity identities;
- exact row and column manifests;
- metric, linkage, cluster count or threshold, full-tree, distance, cache,
  and all accepted defaults;
- memory, threads, temporary, destination, collision, atomic-write,
  rollback, and failure behavior;
- expected fitted attributes, labels, dimensions, metadata, logs, and hashes;
- exact stop before mapping, plotting, stability analysis, or downstream use.

A small synthetic matrix may test call construction only when separately
approved. It does not validate the observed representation or chosen
clustering.

### 8. Gate 2: approve one exact operation

Ask the user to approve the displayed call, immutable matrix and graph,
parameters, accepted defaults, resources, cache, reads, writes, expected
artifacts, verification, and stop point.

Gate 2 authorizes only that operation. A changed row set, feature, scaling,
metric, linkage, graph, cut, tree option, cache, destination, retry,
dendrogram, label map, sensitivity run, or downstream analysis requires a
new Gate 2.

### 9. Execute once and preserve evidence

Record:

- source, environment, matrix, row, feature, and connectivity identities;
- exact code, parameters, accepted defaults, and hashes;
- start and end time, process state, stdout, stderr, warnings, and failures;
- memory, cache, temporary, destination, and write behavior;
- fitted-state, label, children, distance, connected-component, diagnostic,
  metadata, and log inventories;
- partial, missing, implicit, or unexpected artifacts;
- deviations from the approved contract.

Do not retry, change a cut, create a dendrogram, map labels, or continue to
another analysis without new approval.

### 10. Verify and stop

Verify:

- label count equals row count;
- fitted feature count equals the contract;
- children shape and leaf count are coherent;
- distances exist only when requested and align with children;
- the recorded effective symmetrized graph, any explicitly approved
  component-completion edges, and the estimator's original connected-
  component count reconcile with the preflight record;
- labels are finite integers in the expected range, every required cluster is
  represented, and cluster sizes reconcile;
- no output is called a spatial parcel unless rows are spatial units and the
  approved spatial constraints support that claim;
- hashes and provenance reproduce the exact operation.

Return:

```text
Hierarchical Clustering Operation Record
Approved operation, purpose, and input role:
Row grain, row keys, feature definitions, and matrix identity:
Scaling, missingness, leakage, and graph audit:
Metric, linkage, connectivity, cut, and tree specification:
Exact environment, version, source, API call, and accepted defaults:
Resources, cache, temporary files, destinations, and writes:
Exit state, warnings, failures, and deviations:
Label, children, distance, connected-component, and size inventory:
Execution-conformance and structural-verification result:
Stability, prediction, mapping, and interpretation limits:
user-owned interpretation and next decision:
```

## Boundaries

- Stop if the method, row grain, or one operation is not selected.
- Stop on ambiguous orientation, duplicate or missing row keys, unexplained
  scaling, nonfinite values, target leakage, or feature provenance gaps.
- Stop when Ward is paired with an incompatible metric.
- Stop when `n_clusters` and `distance_threshold` are both set, or a distance
  threshold lacks a full tree.
- Stop when a spatially constrained parcellation lacks a verified
  connectivity graph.
- Stop when automatic connectivity symmetrization would change the approved
  adjacency, or disconnected-component completion has not been explicitly
  approved.
- Stop when numeric connectivity values are intended as persistent edge
  weights rather than adjacency support.
- Stop before installation, cache creation, overwrite, cleanup, retry,
  prediction, mapping, plotting, stability resampling, or downstream use.
- Preserve label permutation. Cluster 0 or cluster 1 is not a stable entity
  across fits.
- A hierarchy, compact cluster, stable cut, or connected parcel does not
  establish anatomy, function, mechanism, group difference, or clinical
  validity.

## Checks

- **Positive:** one approved matrix with explicit row grain, feature scale,
  compatible linkage and metric, verified graph, and fresh destination
  produces one label and tree record.
- **Trigger:** only `hierarchical` loads this subskill.
- **Generic work:** ordinary tabular clustering routes to
  [scikit-learn](../scikit-learn/SKILL.md).
- **Method selection:** `which parcellation algorithm should I use?` routes to
  the method owner.
- **Raw imaging:** raw fMRI or sMRI routes to the modality and preprocessing
  owners before this adapter.
- **Orientation:** a time-by-voxel matrix intended to cluster voxels stops
  until orientation is corrected upstream.
- **Ward:** Ward with cosine distance stops.
- **Cut:** simultaneous fixed cluster count and distance threshold stops.
- **Connectivity:** an explicitly spatial parcellation with no adjacency
  graph, an asymmetric graph whose symmetrization is unapproved, a
  disconnected graph whose completion is unapproved, or numeric values
  intended as persistent edge weights stops.
- **Prediction:** a request to assign new rows through the fitted estimator
  stops because the API has no prediction operation.
- **Dendrogram:** a promised dendrogram without stored distances is rejected.
- **Mapping:** label-image reconstruction is a separate approved operation,
  and zero-valued background cannot silently absorb cluster label zero.
- **Version:** an installed release is not treated as a different release.
- **Output:** collision, retry, changed cut, or sensitivity analysis reopens
  Gate 2.
- **Interpretation:** cluster labels are not called anatomical or functional
  regions automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Bellec et al. (2010). Multi-level bootstrap analysis of stable clusters in resting-state fMRI. https://doi.org/10.1016/j.neuroimage.2010.02.082
- scikit-learn. (n.d.). *sklearn.cluster.AgglomerativeClustering*. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html
- *scikit-learn* (Version 1.9.0) [Computer software]. (2026). GitHub. https://github.com/scikit-learn/scikit-learn/releases/tag/1.9.0
