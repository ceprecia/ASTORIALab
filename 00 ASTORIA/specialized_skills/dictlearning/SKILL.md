---
name: dictlearning
description: >-
  Implements one already approved Nilearn DictLearning fit, transform, score, or
  structural-verification operation on a fixed neuroimaging input set, then
  returns an operation, component-identity, verification, and provenance record.
  Use when the request names this skill or neural-population-analysis-guide,
  fmri-coordinator, or nilearn-tool routes one exact DictLearning handoff. It makes
  subject and run identity, preprocessing, confounds, mask, space, component
  count, sparsity, temporal reduction, initialization, randomness, cache,
  fitted-state trust, loadings, writes, stability, and downstream boundaries
  visible. It does not choose dictionary learning, select components from
  attractive maps, install software, preprocess data, fit and transform
  automatically, export time series or connectomes without separate approval,
  overwrite, label components, perform group inference, or interpret results.
  Triggers: dictionary learning on my fmri, nilearn DictLearning.
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

# DictLearning

Implement one approved Nilearn `DictLearning` operation without turning a
sparse decomposition into an automatic resting-state network pipeline.

## Purpose

`dictlearning` owns:

- one exact `DictLearning.fit`, `transform`, `score`, or structural-verification
  operation;
- exact participant, session, run, image, confound, mask, space, and ordering
  identity for that operation;
- translation of an approved decomposition specification into one
  version-matched public API call;
- explicit component count, epoch, sparsity, temporal-reduction, coding,
  initialization, seed, preprocessing, resampling, cache, resource, and write
  behavior;
- preservation of fitted-state identity, component-map identity, loading
  shape, sign and order indeterminacy, warnings, failures, and provenance;
- a DictLearning Operation Record and neutral verification handoff.

The user owns the scientific question, need for dictionary learning, population,
input role, preprocessing, mask, component count, sparsity, temporal
reduction, initialization, sensitivity design, stability criteria, component
meaning, downstream features, inference, interpretation, and claims.

[neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md) owns comparison with ICA, PCA, factor,
manifold, and other latent-variable methods. [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md)
owns upstream denoising, filtering, detrending, smoothing, and nuisance
strategy. [nilearn-tool](../nilearn-tool/SKILL.md) owns separately approved generic image, masker,
signal, cache, and file operations. [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns any
later connectome. These are handoffs, not dependencies or an automatic chain.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `DictLearning`, `dictionary learning`, `sparse
components`, `resting-state network`, `network decomposition`, `component
time series`, `brain atlas`, or another broad method or output phrase.

Do not use this skill to:

- decide whether dictionary learning is scientifically appropriate;
- choose a component count, mask, preprocessing state, sparsity, seed, or
  stability rule after inspecting attractive maps;
- install, update, configure, or repair Nilearn or its dependencies;
- preprocess, resample, smooth, detrend, standardize, filter, or mask data
  unless those effects are already approved parts of the exact API operation;
- combine fitting, transformation, scoring, map export, time-series export,
  connectivity, plotting, and interpretation under one approval;
- call component maps validated networks or loadings neural activity;
- overwrite or silently reuse a cache or fitted estimator.

## Inputs

Obtain or mark missing:

- one approved DictLearning Method Specification and one exact operation:
  fit, transform, score, or structural verification;
- whether the work is descriptive, exploratory, methodological, or part of a
  prespecified downstream analysis;
- immutable participant, session, run, image, confound, and mask manifests
  with hashes and one-to-one order;
- training, validation, test, projection, or descriptive role of every input;
- acquisition and preprocessing provenance, including discarded volumes,
  motion handling, nuisance regression, censoring, temporal filtering,
  detrending, smoothing, resampling, scaling, and standardization;
- image or surface shape, affine or mesh, orientation, space, temporal units,
  usable samples, dtype, finite state, and common mask support;
- approved component count, epochs, `alpha`, `reduction_ratio`, batch size,
  coding method, dictionary initialization, seed, and sensitivity plan;
- approved mask object or strategy and every masking argument;
- approved standardization, confound standardization, detrending, filters,
  TR, smoothing, target affine, and target shape;
- selected exact Nilearn release, environment, public signature, source,
  license, dependency compatibility, and adapter;
- trusted fitted-state source, version, parameter, input, mask, component,
  and serialization identity for transform, score, or verification;
- memory, threads, jobs, cache, work, temporary, destination, collision,
  rollback, and failure policy;
- expected component, loading, score, state, diagnostic, metadata, log, and
  hash outputs;
- compute, destination, and outcome-contact authority.

If the operation, input role, preprocessing, mask, component specification,
fitted-state trust, randomness, stability plan, exact environment, or output
boundary is unresolved, stop with **DictLearning operation contract
incomplete**.

## Steps

### 1. Confirm one operation

Choose exactly one:

1. fit one approved dictionary on the enumerated training or descriptive
   images;
2. transform enumerated images through one already trusted, frozen fitted
   dictionary;
3. score enumerated images through one already trusted, frozen fitted
   dictionary;
4. inspect the structure and provenance of an existing fitted state or output
   without transforming data.

Do not use `fit_transform`, fit and then transform, or transform and then
export a connectome under one approval. A later operation receives a new
contract and Gate 2.

### 2. Preserve a genuine route or explain the fixed route

When the approved purpose leaves more than one valid operation or parameter
route, compare only those routes that remain scientifically in scope. Show:

- what changes in the decomposition or projection;
- evidence and assumptions;
- preprocessing, mask, component, stochastic, resource, and output effects;
- visible benefit, tradeoff, and limitation.

If the method specification fixes one route, state that fixed route and its
limitations. Do not create a model contest or choose the map that looks most
recognizable.

### 3. Build the DictLearning Operation Contract

Create:

| Element | Approved meaning | Exact API binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Operation and input role | | | | |
| Participants, runs, and order | | | | |
| Preprocessing and confounds | | | | |
| Space, mask, and geometry | | | | |
| Components and sparsity | | | | |
| Temporal reduction and coding | | | | |
| Initialization and randomness | | | | |
| Fitted-state identity | | | | |
| Cache, resources, and writes | | | | |
| Outputs and stop point | | | | |

Every API field must have an approved meaning or an explicitly reviewed
default. An inherited default is not a scientific decision.

### 4. Audit identity, preprocessing, and leakage

Verify:

- participant, session, run, image, and confound keys are unique and aligned;
- image and confound sample counts agree after discarded volumes and
  censoring;
- all inputs share the approved volume space or surface mesh, orientation,
  resolution, mask meaning, preprocessing state, and temporal units;
- smoothing, detrending, filtering, standardization, confound cleaning, and
  resampling are not applied twice or silently;
- a training dictionary never receives held-out or target-informed data;
- component count, seed, restart, mask, and initialization were not selected
  from target labels or test results;
- transform and score inputs use the exact frozen fitted state and compatible
  preprocessing and geometry;
- temporary arrays and cache fit the approved resources.

Equal shapes or successful loading do not establish common space or
comparable preprocessing.

### 5. Preflight the exact public API

For the reviewed Nilearn `0.14.0` API, `DictLearning` defaults include
`n_components=20`, `n_epochs=1`, `alpha=10`, `reduction_ratio='auto'`,
`batch_size=20`, `method='cd'`, `random_state=None`,
`smoothing_fwhm=4`, `standardize=True`, `standardize_confounds=True`,
`detrend=True`, automatic EPI masking when no mask is supplied, one job, and
no cache by default. Each applicable behavior is explicit.

`transform` returns one two-dimensional loading array per subject. Preserve
participant, session, run, sample, and component identities. Do not coerce the
list into one unlabeled table. `score` reports explained-variance-based
values; it is not a validation of component meaning or scientific truth.

Verify Nilearn in the selected participant runtime. Check the user-selected interpreter and required packages at invocation time. An absent or incompatible dependency stops the affected execution; it does not authorize installation, environment creation, or substitution.

### 6. Gate 1: approve contract and read-only preflight

Show:

- selected operation and fixed scientific scope;
- route comparison or explained fixed route;
- completed Operation Contract;
- input, preprocessing, confound, mask, geometry, leakage, and fitted-state
  audit;
- exact version, source, signature, license, environment, and dependency
  evidence to inspect;
- resources, caches, reads, writes, outputs, verification, and stop point;
- unresolved assumptions and downstream exclusions.

Gate 1 authorizes only bounded metadata, header, schema, version, signature,
resource, cache, collision, and destination inspection plus exact code
construction. It does not authorize full-array fitting, transformation,
scoring, cache creation, resampling, masking, smoothing, output creation, or
held-out access.

### 7. Construct and inspect the exact call

Display:

- exact interpreter, environment, Nilearn release, source, and adapter;
- exact API method and immutable ordered inputs;
- every constructor and method argument plus intentionally accepted defaults;
- confound list and sample alignment;
- component, sparsity, temporal-reduction, coding, seed, and initialization
  settings;
- mask, preprocessing, resampling, memory, cache, job, and thread behavior;
- destination, collision, temporary, atomic-write, rollback, and failure
  behavior;
- expected artifacts, shapes, identities, metadata, logs, and hashes;
- exact stop before another operation or downstream analysis.

Structure-only or synthetic validation may test call construction only when
its inputs and writes are separately approved. It does not validate observed
data or the scientific model.

### 8. Gate 2: approve one exact operation

Ask the user to approve the displayed API call, immutable inputs, fitted state,
parameters, accepted defaults, resources, cache, reads, writes, expected
artifacts, verification, and stop point.

Gate 2 authorizes only that one operation. A fit, transform, score,
inverse-transform, retry, changed component count, seed, mask, preprocessing
setting, input, fitted state, cache, destination, plot, map export, time-series
export, or connectome requires a new Gate 2.

### 9. Execute once and preserve evidence

Record:

- source and environment identities;
- exact code, parameters, inputs, fitted state, mask, and hashes;
- start and end time, process state, stdout, stderr, warnings, and failures;
- memory, threads, jobs, cache, temporary, and destination behavior;
- component, loading, score, estimator-state, diagnostic, metadata, and log
  inventories;
- implicit, missing, partial, or unexpected writes;
- deviations from the approved contract.

Do not retry, change a seed or parameter, clean partial state, transform after
fit, or continue to plotting or connectivity without new approval.

### 10. Verify and stop

Separate:

1. **Execution conformance:** exact call, inputs, parameters, environment,
   resources, writes, warnings, and deviations.
2. **Structural verification:** expected count, shape, affine or mesh, mask,
   dtype, finite state, subject and run identity, component and loading
   pairing, metadata, and hashes.
3. **Algorithm evidence:** convergence, objective or score, degenerate
   components, initialization, and prespecified stability evidence.
4. **Scientific decision:** the user decides adequacy, component meaning,
   sensitivity continuation, downstream use, inference, and claims.

Return:

```text
DictLearning Operation Record
Approved operation, purpose, and input role:
Participant, run, image, confound, mask, and order manifest:
Preprocessing, space, geometry, and leakage audit:
Component, sparsity, reduction, coding, seed, and initialization settings:
Trusted fitted-state identity, when applicable:
Exact environment, Nilearn version, source, API call, and accepted defaults:
Resources, cache, temporary files, destinations, and writes:
Exit state, warnings, failures, and deviations:
Component, loading, score, state, metadata, and hash inventory:
Execution-conformance and structural-verification result:
Stability evidence and limitations:
user-owned interpretation and next decision:
```

## Boundaries

- Stop when the method or one operation has not been selected.
- Stop on duplicate or unmatched identities, confound-row mismatch, mixed
  spaces or meshes, incompatible preprocessing, nonfinite inputs, or
  unapproved automatic masking or resampling.
- Stop when component count, sparsity, reduction, seed, initialization,
  preprocessing, cache, or sensitivity rules are implicit.
- Stop when transform or score receives an untrusted, version-mismatched, or
  provenance-incomplete fitted state.
- Stop before installation, environment creation, implicit cache creation,
  overwrite, cleanup, retry, or a second API operation.
- Preserve component sign and order indeterminacy. Component number is not a
  stable biological label across fits.
- A stable, sparse, recognizable, or high-scoring component does not prove a
  neural network, mechanism, clinical marker, or replicable finding.

## Checks

- **Positive fit:** one approved fixed-input fit produces only its component,
  fitted-state, verification, and provenance record.
- **Positive transform:** one trusted frozen fitted state transforms only the
  enumerated images and preserves subject, run, sample, and component keys.
- **Trigger:** only `dictlearning` loads this subskill.
- **Method selection:** `should I use ICA or dictionary learning?` routes to
  [neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md).
- **Missing environment:** absent Nilearn stops without installation.
- **Operation split:** a request for maps, time series, and a connectome is
  separated into independently approved operations.
- **Confounds:** missing or misaligned confounds stop rather than being
  silently ignored.
- **Defaults:** implicit 20 components, 4 mm smoothing, detrending,
  standardization, automatic mask, or temporal reduction stops.
- **Fitted state:** a pickled estimator without exact version, parameter,
  input, mask, and component provenance is not trusted.
- **Leakage:** held-out participants cannot enter dictionary fitting.
- **Output:** an existing destination or cache collision stops before writes.
- **Identity:** component sign or order changes do not become new network
  labels.
- **Chaining:** transform, inverse transform, CSV export, plotting,
  connectivity, clustering, group inference, and interpretation never follow
  automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Mensch, Varoquaux, & Thirion. (2016). Compressed online dictionary learning for fast resting-state fMRI decomposition. https://doi.org/10.1109/ISBI.2016.7493501
- Nilearn. (n.d.). *nilearn.decomposition.DictLearning*. https://nilearn.github.io/stable/modules/generated/nilearn.decomposition.DictLearning.html
- Nilearn. (2026). *Nilearn* (Version 0.14.0) [Computer software]. GitHub. https://github.com/nilearn/nilearn/releases/tag/0.14.0
