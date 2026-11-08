---
name: ica
description: >-
  Specifies and implements one bounded spatial independent component analysis of
  preprocessed fMRI through one selected exact-version backend, then returns a
  decomposition, stability, artifact, verification, and provenance record. Use
  when the request names this skill or fmri-coordinator,
  fmri-preprocessing-pipeline-guide, neural-population-analysis-guide, or a
  selected software adapter routes one exact ICA handoff. It makes subject and
  run pooling, space, mask, preprocessing, scaling, whitening, dimensionality,
  algorithm, initialization, randomness, thresholding, component indeterminacy,
  runtime, writes, and downstream-use boundaries visible. Triggers: run spatial
  ICA on my fmri, independent component decomposition.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: FSL MELODIC or nilearn CanICA
  gates: training or running on real data, accepting results
  created: "2026-07-23"
  updated: "2026-10-29"
---

# ICA

Specify and implement one bounded spatial ICA decomposition of already
preprocessed fMRI without treating components as automatically neural,
artifactual, stable, or biologically interpretable.

## Purpose

It does not choose ICA from a research goal, select component count from attractive results, install software, preprocess or denoise data, label components as neural or artifact, remove components, compute connectomes, perform group inference, overwrite, or chain downstream work.

`ica` owns:

- one subject-level, session-level, or group spatial-ICA specification for a
  fixed preprocessed fMRI input set;
- assessment of the selected ICA route and comparison only when a material
  choice remains open. The user selects the route.
- exact subject, run, volume, voxel or vertex, mask, space, and ordering
  control;
- explicit scaling, centering, whitening, PCA or dimensionality-reduction,
  component-count, independence, initialization, randomness, thresholding,
  and convergence control;
- translation of the selected specification into one exact Nilearn CanICA,
  FSL MELODIC, or other verified implementation;
- one approved decomposition execution without automatic back-reconstruction,
  denoising, classification, connectivity, statistics, or plotting;
- preservation of component maps, mixing or time-course artifacts, model
  state, stability evidence, failures, and provenance;
- an ICA Decomposition Record and neutral Component Review Packet.

The user owns the scientific question, need for ICA, subject or group target,
spatial versus temporal formulation, pooling, preprocessing, denoising,
filtering, mask, smoothing, resampling, scaling, whitening, dimensionality,
component count, algorithm, backend, stability criteria, component
classification, removal, downstream features, statistics, interpretation,
and claims.

[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns whether ICA is used for
preprocessing or denoising and the order of all signal operations.
[neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md) owns general latent-variable and
dimensionality-reduction method comparison. [nilearn-tool](../nilearn-tool/SKILL.md) owns exact
Nilearn API execution, and [fsl-tool](../fsl-tool/SKILL.md) owns exact MELODIC or FSL execution.
[brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns any later component-connectivity
estimand. This skill does not classify or remove components and does not
absorb FIX, AROMA, dual regression, or connectome construction.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `ICA`, `independent component analysis`, `resting-state
network`, `intrinsic connectivity network`, `MELODIC`, `CanICA`, `component
map`, `component time series`, `artifact removal`, `denoise fMRI`, or another
broad method, software, or output phrase.

Do not use this skill to:

- choose ICA over seed-based connectivity, dictionary learning, clustering,
  a GLM, or another method;
- select component count, threshold, mask, smoothing, filtering,
  standardization, or backend from convention or attractive components;
- install, update, configure, or license Nilearn, FSL, scikit-learn, or
  another implementation;
- preprocess, register, resample, filter, detrend, nuisance-regress, or
  denoise the input;
- label a component as neural signal, resting-state network, artifact, or
  disease marker;
- regress components from data, derive a connectome, test groups, or make
  clinical claims.

## Inputs

Obtain or mark missing:

- approved scientific purpose and whether the decomposition is exploratory,
  methodological, or part of a prespecified downstream plan;
- one operation scope: subject or session spatial ICA, fixed group spatial
  ICA, or structure-only verification of an existing decomposition;
- exact participant, session, run, and image manifest with hashes and order;
- acquisition and preprocessing provenance, including motion correction,
  distortion correction, registration, resampling, smoothing, temporal
  filtering, detrending, nuisance regression, censoring, and discarded
  volumes;
- image shape, time points, dtype, scaling, affine, orientation, space,
  voxel or vertex order, mask, and temporal units;
- approved subject and run pooling, weighting, concatenation, time-point
  balancing, and missing-run policy;
- approved spatial-versus-temporal ICA orientation;
- approved centering, standardization, percent-signal change, confound
  standardization, whitening, PCA or CCA, variance normalization, and
  dimensionality policy;
- approved component number or data-driven dimensionality method, including
  its selection evidence and outcome-contact boundary;
- approved algorithm, objective, tolerance, maximum iterations,
  initialization count, random seeds, convergence, sign and order handling,
  and stability plan;
- approved map thresholding or sparsification, or explicit unthresholded
  output;
- the approved backend, if already selected. Before execution record the exact
  backend, release, source, license, public API or command, accepted defaults
  and software adapter. Mark any open backend choice for Step 2.
- memory, threads, parallelism, cache, report, work, temporary, destination,
  collision, rollback, and failure policy;
- expected component maps, mixing matrices, time courses, model state,
  masks, diagnostics, reports, logs, metadata, and hashes;
- component-review and downstream-use boundary;
- compute and destination authority.

If the purpose, required formulation, pooling, preprocessing, mask,
dimensionality, algorithm, randomness, thresholding, stability plan, or
downstream boundary is unresolved, stop with **ICA decomposition contract incomplete**.
When the scientific prerequisites are approved and only the backend choice
remains open, use Step 2 to assess compatible implementations of the fixed
formulation. Obtain the user's backend selection before preflight. Verify
its exact semantics before execution.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Fix the decomposition question

State:

- what data are to be decomposed and at what subject or group grain;
- whether the target is spatial components and what independence assumption
  is being made;
- whether the purpose is descriptive decomposition, source separation,
  exploratory network discovery, or a separately specified denoising input;
- what outputs may be created;
- what is explicitly outside scope.

Do not convert `find the brain networks` into a validated scientific target.
ICA components can include neural, physiological, motion, scanner,
registration, and other structured sources.

### 2. Verify the selected backend or assess compatible backends

Carry forward the approved spatial ICA formulation, pooling, dimensionality
policy, and other scientific requirements. If a required decision such as
subject versus group formulation, group pooling, or fixed count versus a
prespecified dimensionality rule is unresolved, stop with **ICA decomposition
contract incomplete** and return the missing decision to its owner.

Assess the selected backend against the criteria below. If it is incompatible,
report the blocker before preflight or execution and reopen the affected
backend choice with the user. When only the backend remains open, compare
exact routes such as CanICA and MELODIC only when both implement the same
approved specification. If one verified route fits, explain its limitation.
The user selects the backend before preflight.

For the selected route or each eligible backend being compared, show the following.

- estimand and decomposition orientation;
- subject and time-point pooling or weighting;
- preprocessing, mask, space, smoothing, scaling, whitening, and dimension
  assumptions;
- stochastic behavior, identifiability, convergence, and stability plan;
- map thresholding and output meanings;
- backend semantics, resources, writes, benefit, tradeoff, and limitation.

Do not rank routes by package availability, runtime, visual crispness, or
whether a default produces recognizable components.

### 3. Build the ICA Specification

Create:

| Element | Selected meaning | Evidence or assumption | Backend binding | Verification |
|---|---|---|---|---|
| Subjects, runs, and pooling | | | | |
| Space, mask, and preprocessing | | | | |
| Data orientation and scaling | | | | |
| Whitening and dimension reduction | | | | |
| Component count or rule | | | | |
| ICA algorithm and objective | | | | |
| Initializations, seeds, and convergence | | | | |
| Thresholding and output semantics | | | | |
| Stability and component review | | | | |
| Downstream stop boundary | | | | |

Component count is a scientific and modeling choice. Do not copy the
candidate's `20`, accept a backend's automatic dimensionality estimate
without review, or tune count after viewing which result looks most
recognizable without labeling that exploration.

### 4. Audit data identity and comparability

Verify:

- each image belongs to the named participant, session, and run;
- all inputs have compatible space, grid or surface, mask meaning, temporal
  units, preprocessing, filtering, smoothing, and intensity handling;
- subject and run order is explicit and stable;
- the number of usable volumes and censoring differ neither silently nor in a
  way that violates the selected weighting or pooling plan;
- no target label or group outcome entered preprocessing, component-number
  selection, initialization selection, or map selection;
- the group mask does not silently exclude participants or reflect outcome
  information;
- memory and temporary-array requirements fit the approved environment.

Equal image shapes do not establish common space, preprocessing, or mask
support.

### 5. Preflight exact backend semantics

For Nilearn `CanICA`, inspect the exact selected release and public signature.
The current reviewed release is Nilearn `0.14.0`, full commit
`0d0429a12efa131bf46bb30654f9d1630d950f73`, released 2026-07-02.
Its current defaults include `n_components=20`, `smoothing_fwhm=6`,
`do_cca=True`, `threshold='auto'`, `n_init=10`, `random_state=None`,
`standardize=True`, `standardize_confounds=True`, `detrend=True`, automatic
masking when no mask is supplied, and optional filtering and resampling.
Every applicable behavior is explicit and approved. Current boolean
standardization forms are deprecated for a future `0.15.0` semantic change,
so use the exact selected version's named form.

For FSL MELODIC, distinguish:

- the command-line decomposition from the GUI's wider preprocessing and
  registration workflow;
- single-session, temporal-concatenation, and tensor formulations;
- fixed versus automatic dimensionality;
- variance normalization, thresholding, report, browser, and output-tree
  behavior;
- MELODIC decomposition from later `fsl_regfilt`, FIX, or dual regression.

The official current FSL release reviewed is `6.0.7.22`. Verify the participant's installed release independently. Exact component build and `melodic --help` remain
execution authorities. Verify FSL's applicable license boundary for the participant's intended use.

Verify Nilearn in the selected environment if that backend is chosen. Missing dependencies do not authorize installation, updates, source cloning or backend substitution.

### 6. Gate 1: approve specification and read-only preflight

Show:

- fixed decomposition question and scope;
- compatibility of the selected route and its limits, with a comparison
  only if an open material choice required one;
- completed ICA Specification;
- input, preprocessing, space, mask, and pooling audit;
- exact source and API evidence to inspect;
- stability, component-review, resources, writes, outputs, and stop point;
- unresolved assumptions and prohibited downstream actions.

Gate 1 authorizes only the displayed bounded metadata, header, array-schema,
version, API, resource, collision, and destination inspection plus exact
code or command construction. It does not authorize full-array fitting,
software changes, preprocessing, automatic masking, smoothing, filtering,
report or cache writes, decomposition, plotting, classification, removal,
connectivity, or output creation.

### 7. Construct and audit exact execution

Display:

- selected backend, exact release or commit, adapter, API or command;
- immutable ordered input and mask manifests;
- pooling, scaling, whitening, dimensionality, algorithm, threshold, seed,
  initialization, convergence, and stability parameters;
- every explicit option and intentionally accepted default;
- memory, threads, parallelism, cache, report, work, temporary, and writable
  paths;
- expected maps, matrices, time courses, model state, diagnostics, logs, and
  hashes;
- collision, partial-state, failure, rollback, and verification behavior;
- exact stop before component labeling or downstream analysis.

Do not choose the best initialization from appearance. If the algorithm
selects among restarts, record the exact objective and selection behavior.

### 8. Gate 2: approve one exact decomposition

Ask the user to approve the displayed formulation, inputs, mask, preprocessing
state, pooling, dimensionality, backend, parameters, accepted defaults,
randomness, resources, writes, outputs, verification, and stop point.

Gate 2 authorizes only that decomposition. A changed participant, run, mask,
space, preprocessing step, component number, initialization, seed,
threshold, backend, destination, retry, stability analysis, component
classification, removal, time-series reconstruction, dual regression,
connectome, group test, or interpretation requires a new contract.

### 9. Execute once and preserve evidence

Run only the approved operation through the selected software adapter.
Capture:

- exact source, environment, API or executable, code or command, and working
  directory;
- ordered input, mask, preprocessing, space, and pooling manifests;
- all model parameters, defaults, seeds, restart behavior, and convergence
  state;
- resources, threads, cache, report, work, temporary, and destination state;
- start and end time, exit status, stdout, stderr, warnings, and failures;
- component maps, mixing or time-course artifacts, model state, mask,
  dimensionality, diagnostics, report, and log inventories;
- implicit, unexpected, partial, missing, or version-divergent outputs;
- deviations from the approved contract.

Do not rerun with a different seed, count, threshold, mask, or preprocessing
choice; remove components; create a denoised image; match components to a
template; compute connectivity; or continue after failure without new
approval.

### 10. Verify and stop at component review

Verify:

- exact input and model conformance;
- output dimensions, geometry, space, mask, component count, dtype, finite
  and invalid state, and hashes;
- reconstruction or model invariants available from the exact backend;
- convergence warnings and failed initializations;
- component spatial maps and corresponding time-course or mixing order;
- sign and order indeterminacy;
- approved stability evidence across starts or resamples;
- unexpected writes and report or cache behavior.

Separate:

1. **Structural verification:** artifact integrity and exact pairing.
2. **Algorithm verification:** convergence, objective, restart, and stability
   evidence.
3. **Component Review Packet:** all components, unthresholded source maps,
   display parameters if later approved, and known limitations.
4. **Scientific decision:** the user decides component meaning, adequacy,
   classification, removal, downstream analysis, interpretation, and claims.

Return:

```text
ICA Decomposition Record
Approved purpose, formulation, and scope:
Input, preprocessing, mask, space, and pooling manifest:
Scaling, whitening, dimension, and component-count specification:
Algorithm, threshold, initialization, seed, and convergence settings:
Selected backend, exact source, version, and adapter:
Exact code or command and accepted defaults:
Resources, cache, reports, temporary files, and writes:
Exit state, warnings, failures, and deviations:
Component, mixing, time-course, model, and diagnostic inventory:
Structural and algorithm-verification result:
Stability evidence and limitations:
Component Review Packet:
user-owned classification, removal, downstream use, and next decision:
```

## Boundaries

- Require the approved ICA formulation and scientific purpose before
  implementation or backend assessment. When only the backend remains open,
  limit the work to Step 2 until the user selects a compatible implementation.
- Stop on mixed spaces, grids, surfaces, masks, preprocessing, filtering,
  smoothing, temporal units, or unexplained subject and run order.
- Stop when pooling, time-point weighting, whitening, scaling, thresholding,
  or stability criteria are implicit. Require an approved component count or
  prespecified dimensionality rule with its evidence and outcome boundary.
- Stop if a target label or observed group result influences preprocessing,
  dimensionality, restart selection, component selection, or mask creation.
- Stop when the selected backend cannot represent the approved formulation.
- Stop on a nonconverged fit, failed restart, missing component-timecourse
  pairing, output-count mismatch, or unverified component order.
- Stop before any installation, automatic mask, resampling, smoothing,
  filtering, report, browser, cache, or write not shown at Gate 2.
- Stop before overwrite, cleanup, retry, rerun with a new seed, component
  matching, labeling, removal, denoising, dual regression, connectivity,
  statistics, or interpretation.
- Preserve component sign and order indeterminacy; do not assign stable
  biological identity from component index.
- A recognizable default-mode-like map, high stability score, convergence,
  or complete report does not prove neural origin, truth, or replicability.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Beckmann & Smith. (2004). Probabilistic independent component analysis for functional magnetic resonance imaging. https://doi.org/10.1109/TMI.2003.822821
- *FSL* (Version 6.0.7.22) [Computer software]. (2026, March 27). https://fsl.fmrib.ox.ac.uk/fsl/docs/development/history/index.html
- *MELODIC*. (n.d.). FSL documentation. https://fsl.fmrib.ox.ac.uk/fsl/docs/resting_state/melodic.html
- *Nilearn* (Version 0.14.0) [Computer software]. (2026, July 2). GitHub. https://github.com/nilearn/nilearn/releases/tag/0.14.0
- *nilearn.decomposition.CanICA*. (n.d.). Nilearn. https://nilearn.github.io/stable/modules/generated/nilearn.decomposition.CanICA.html
- Varoquaux et al. (2010). A group model for stable multi-subject ICA on fMRI datasets. https://doi.org/10.1016/j.neuroimage.2010.02.010
