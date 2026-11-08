---
name: nilearn-tool
description: >-
  Implements one already approved Nilearn image, masker, signal, confound,
  feature, or connectivity operation through an available,
  version-and-API-verified environment and returns an exact parameter,
  data-contact, cache, output, verification, and provenance record. Use when the
  request names this skill or a verified Active method or modality skill routes
  one exact Nilearn handoff. It makes the public API, versions, inputs, shapes,
  geometry, masks, confounds, sample masks, filtering, standardization,
  resampling, estimator, memory, cache, network, writes, outputs, and
  verification limits visible before execution. It does not choose
  preprocessing, denoising, atlas, connectivity, GLM, decoding, parcellation,
  threshold, model, or interpretation; install packages; fetch data; silently
  chain operations; accept defaults as scientific decisions; overwrite; or treat
  finite outputs as valid results. Triggers: run this in Nilearn, masker or
  connectivity operation in nilearn.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: fmri
  dependencies: ""
  requires: Python, Nilearn
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Nilearn Tool

Implement one approved Nilearn operation with the exact public API and
software state available for the selected research project.

## Purpose

`nilearn-tool` owns:

- exact Python, Nilearn, NiBabel, NumPy, SciPy, pandas, scikit-learn, and
  optional-backend preflight;
- translation of one approved operation into inspectable public-API code;
- explicit input, geometry, mask, confound, sample-mask, time, estimator,
  memory, cache, output, and side-effect control;
- one approved image, masker, signal-cleaning, feature-extraction, or
  connectivity implementation at a time;
- structural verification and a method-owner QC handoff;
- a Nilearn API Operation Record.

The user owns the scientific question, preprocessing and denoising design, dummy
volumes, censoring, confounds, temporal filters, standardization, smoothing,
resampling, interpolation, atlas and labels, masks, seeds, features,
connectivity definition, covariance estimator, model, cross-validation,
contrasts, thresholds, multiplicity, QC criteria, interpretation, and claims.

[fmri-coordinator](../fmri-coordinator/SKILL.md) owns functional-MRI routing. [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md)
owns preprocessing and denoising methods. [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns
connectivity estimands and inference. [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md) and
[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) own GLM and decoding designs. [nibabel-skill](../nibabel-skill/SKILL.md)
owns lower-level file, header, affine, coordinate, and format operations.
Later model-specific adapters retain their own algorithms. This adapter does
not select among those owners or absorb their methods.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `Nilearn`, `masker`, `connectivity`, `clean the signal`,
`extract ROIs`, `GLM`, `decoding`, `parcellation`, `resample`, `plot the
brain`, `fMRI`, or another broad software, method, or output term.

Do not use this skill to:

- choose or revise a scientific method;
- combine several Nilearn calls into a preprocessing or analysis pipeline;
- install, upgrade, fetch, download, or license software, atlases, templates,
  or datasets;
- implement GLM, ICA, dictionary learning, k-means, hierarchical
  parcellation, SpaceNet, SVM, or another model before its method owner and
  specialized adapter approve the handoff;
- interpret maps, matrices, regions, effects, predictions, or anatomy;
- make clinical, diagnostic, treatment, or patient-specific decisions.

## Inputs

Obtain or mark missing:

- an approved method-owner handoff and Nilearn Implementation Specification;
- one exact public Nilearn operation and stop point;
- input files or arrays, hashes, participant and run grain, shapes, dtypes,
  geometry, spaces, time axis, units, and immutable source state;
- mask, atlas, labels, lookup table, seed, confounds, sample mask, events,
  design, or estimator already selected for the operation;
- exact preprocessing status and prior transforms;
- every public API, argument, accepted default, version-sensitive behavior,
  and expected return shape;
- Python and package versions plus the active environment identity;
- memory, cache, temporary-file, thread, parallel, and random-state plan;
- network and dataset-fetch boundary;
- output format, destination, collision policy, implicit report or cache
  writes, and rollback boundary;
- structural invariants and method-specific QC handoff;
- compute and destination authority.

If the method, operation, data grain, API, version, geometry, temporal
semantics, parameter, side effect, or verification plan is unresolved, stop
with **Nilearn operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one method-to-API handoff

State:

- the already approved scientific operation;
- one public Nilearn API or one inseparable same-operation call;
- fixed inputs and parameters;
- expected return object and artifacts;
- one stop point before a new method or scientific transition.

Treat confound selection, signal cleaning, masker extraction, resampling,
connectivity calculation, model fitting, reporting, and plotting as separate
transitions unless the approved owner explicitly defines one as an
inseparable operation. Do not inherit the candidate's wrapper pipeline.

### 2. Preflight the exact API and data semantics

Read only bounded metadata and record:

- Python and package versions, environment path, and import origin;
- installed public signature, deprecations, changelog, and matching official
  documentation;
- input hashes, image class, array shape, dtype, affine, orientation, voxel
  size, space, mask and atlas geometry, and time points;
- confound columns, rows, missing values, numerical types, sample-mask indices,
  run boundaries, and alignment with the image time axis;
- repetition time and temporal-filter units;
- standardization, detrending, filtering, censoring, interpolation, and
  confound-regression order;
- masker resampling target, interpolation, label values, lookup-table
  alignment, background handling, and empty regions;
- connectivity kind, covariance estimator, standardization, vectorization,
  diagonal policy, and subject grain where relevant;
- full-array and intermediate memory, joblib cache location and level,
  process count, thread state, and random state;
- output, report, cache, temporary, and collision paths;
- any dataset fetcher or template loader that could contact the network or
  write to the default Nilearn data directory.

Current official review found Nilearn `0.14.0`, released 2026-07-02, current
on 2026-07-23. Verify Nilearn in the participant's selected interpreter; absence stops execution without authorizing installation. Every invocation checks the exact
environment and matching stable documentation.

### 3. Gate 1: approve inspection and the API contract

Show a **Nilearn API Contract**:

| Element | Approved meaning | Observed state | Risk or side effect | Verification |
|---|---|---|---|---|
| Method handoff and operation | | | | |
| Inputs, grain, geometry, and spaces | | | | |
| Masks, labels, confounds, and sample mask | | | | |
| Temporal and signal semantics | | | | |
| Public API, versions, and parameters | | | | |
| Estimator, random, and parallel state | | | | |
| Memory, cache, network, and writes | | | | |
| Outputs and return shapes | | | | |
| Structural checks and QC handoff | | | | |

Gate 1 authorizes only displayed metadata inspection, version and signature
checks, bounded header and table review, memory estimation, and code
construction. It does not authorize a full data load, fit, transform,
resampling, filtering, network access, cache creation, output write, or
scientific decision.

### 4. Public API forms for the approved operation

Carry forward the selected API form and its fitted-state requirements.
Compare forms only when the user's approved scope leaves a material
implementation choice open and more than one already available form
preserves the same operation and semantics. The following forms may qualify.

1. one direct public Nilearn function;
2. one fitted public masker or estimator with explicit parameters;
3. one existing reviewed project function that calls the same public API.

For each show API stability, data contacts, fitted state, memory, cache,
parallelism, outputs, reproducibility, visible result, benefit, tradeoff, and
limitation. These are implementation forms, not alternative preprocessing,
atlas, connectivity, GLM, decoding, or parcellation methods. Do not propose an
installation route.

### 5. Audit operation-specific semantics

#### Confounds and sample masks

- Use only the approved confound strategy and literal columns.
- Confirm the fMRIPrep derivative naming and version expected by
  `load_confounds` or `load_confounds_strategy`.
- Pass the BIDS-named preprocessed derivative expected by `load_confounds`,
  not the associated confounds TSV as the `img_files` argument. Treat an
  approved manual confound matrix as a different explicit route.
- Pass the returned sample mask to the approved masker or `signal.clean`
  operation when censoring or nonsteady-state removal is part of the
  specification.
- Preserve sample-mask entries as kept original-volume indices in the
  Operation Record.
- Verify time-point alignment after censoring and across every run.
- Do not inherit the candidate's `motion`, `wm_csf`, detrending, or
  standardization choices.
- Do not use the removed fMRIPrep `--use-aroma` route as a current
  ICA-AROMA source.

#### Signal cleaning and maskers

- Display the exact order of detrending, filtering, censoring,
  confound regression, and standardization for the installed version.
- Use explicit standardization values rather than version-sensitive Boolean
  shorthand.
- Require an approved `t_r` for temporal filtering and confirm evenly sampled
  data where the filter requires it.
- Do not replace nonfinite values with zero unless that transformation is
  separately approved.
- Make the mask source, resampling target, interpolation, background label,
  empty-region behavior, and returned feature order explicit.
- Preserve fitted lookup-table and region-ID metadata rather than relying on
  a positional text-file label list.
- Treat `inverse_transform` as spatial reconstruction from features, not an
  inverse of preprocessing or information loss.

#### Connectivity and features

- Fix the input grain, connectivity kind, covariance estimator, centering and
  scaling, vectorization, diagonal policy, and Fisher transformation.
- Record that the default `ConnectivityMeasure` covariance estimator uses
  shrinkage; do not describe its correlation as an unmodified sample
  correlation.
- Verify region count and label identity without truncating a mismatched label
  table.
- Treat symmetry, diagonal, bounds, finite values, and array shape as
  structural observations, not scientific validation.
- Keep train, validation, test, participant, family, site, and run boundaries
  outside any data-driven fit and cache according to the approved method.

#### Resampling, fetching, caching, and outputs

- Fix source and target geometry, transform meaning, interpolation, fill
  value, clipping, dtype, and output header before resampling.
- Record that `resample_to_img` performs interpolation and does not estimate
  registration. Target-template geometry alone never establishes MNI
  alignment.
- Do not call a template or atlas fetcher unless a separate approved network
  and destination action supplies source, version, license, and checksum
  requirements.
- Treat `memory`, `memory_level`, reports, and dataset directories as writes
  with explicit locations and collision policies.
- Do not create deterministic filenames in a fixed project folder merely
  because the candidate does so.
- Do not overwrite a source or existing output.

The selected candidate scripts are examples, not executable dependencies.
Their fixed TR, smoothing, temporal filters, dummy scans, resampling target,
standardization, detrending, atlas-label truncation, missing-confound route,
directory creation, and output names are rejected.

### 6. Review geometry, timing, and verification limits

Show:

- differences among the approved specification, candidate example, installed
  signature, and current stable documentation;
- version drift, deprecations, changed defaults, and dependency compatibility;
- input geometry, temporal alignment, mask, label, confound, estimator, and
  subject-grain assumptions;
- filtering and confound-regression order plus censoring consequences;
- resampling, interpolation, standardization, covariance shrinkage, caching,
  randomness, and parallelism effects;
- leakage and double-processing risks;
- every explicit and implicit read, cache, download, report, and output;
- which shapes, labels, matrices, metadata, and numerical invariants can be
  structurally checked;
- which preprocessing quality, model validity, regional meaning, effect,
  prediction, or inference remains for the user and the method owner.

Do not infer a valid preprocessing strategy, atlas, connection, group,
prediction, activation, or scientific conclusion because an API completed or
a value is finite.

### 7. Gate 2: approve one exact API operation

Ask the user to approve:

- environment, versions, public API, and literal code;
- files or arrays, hashes, participant and run grain, data regions, and
  geometry;
- masks, labels, confounds, sample masks, temporal semantics, and parameters;
- estimator, random, thread, process, memory, and cache state;
- network-off boundary or separately approved network action;
- output, report, cache, temporary, and collision paths;
- structural checks, QC handoff, and stop point;
- no-install, no-fetch, no-method-change, no-default-inference, no-overwrite,
  no-repair, no-retry, and no-chaining boundary.

Gate 2 authorizes only the displayed operation and verification. A changed
parameter, second operation, new run or participant, model fit, cache, report,
plot, download, overwrite, or downstream transition requires a new approval.

### 8. Run one approved Nilearn operation

Run only the approved code. Capture:

- environment identity, versions, import paths, signatures, and deprecations;
- exact code and parameters;
- input identities, hashes, shapes, dtypes, geometry, spaces, and time axis;
- masks, labels, confounds, sample masks, run boundaries, and alignment;
- temporal, resampling, standardization, estimator, random, and parallel
  semantics;
- memory, cache, temporary, network, report, and output activity;
- return type, shape, labels, metadata, outputs, warnings, exceptions,
  runtime, and deviations;
- structural-verification results and artifacts.

On warning escalation, mismatch, exception, or unexpected write, stop and
preserve evidence. Do not change a parameter, version, input, mask, label,
confound, sample mask, estimator, memory route, cache, destination, or method;
retry; or continue.

Return:

```text
Nilearn API Operation Record
Approved method handoff and operation:
Environment, versions, API, and code:
Inputs, hashes, grain, geometry, and spaces:
Masks, labels, confounds, and sample masks:
Temporal, cleaning, resampling, and feature semantics:
Estimator, random, thread, and process state:
Memory, cache, network, report, and write activity:
Return objects and output artifacts:
Structural-verification result:
Method-owner QC handoff:
Warnings, failures, deviations, and limitations:
Artifacts and hashes:
user-owned QC, next operation, interpretation, and claim decision:
```

## Boundaries

- Stop if the method or API is selected only because Nilearn is available.
- Stop on an unresolved environment, version, public signature, dependency,
  deprecation, or changed-default issue.
- Stop on image-mask-atlas geometry mismatch, undefined space, label-table
  mismatch, empty region, ambiguous run grain, or time-axis misalignment.
- Stop when confounds, sample masks, filtering, censoring, standardization,
  resampling, interpolation, estimator, or diagonal behavior is unresolved.
- Stop before any unapproved data fetch, template download, cache, report,
  output write, directory creation, or overwrite.
- Stop on leakage across participant, family, site, run, train, validation, or
  test boundaries.
- Never treat `standardize=True`, a preset confound strategy, a default
  covariance estimator, or candidate constant as a scientific default.
- Never truncate labels to make a mismatched atlas and matrix appear aligned.
- Never treat `inverse_transform` as recovery of discarded information.
- Never use shape, symmetry, finite values, or correlation bounds as a QC pass.
- Never infer anatomy, activation, connectivity, group difference,
  prediction, diagnosis, or causal meaning from the output.

## Nilearn operation evidence and QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled direct-function, fitted-estimator, or reviewed-function forms.** Compare only public API forms that preserve one approved Nilearn operation. This makes fitted state, memory, cache, and write behavior visible without reopening method choice. This adds an implementation review. This cannot resolve an undefined scientific operation or missing environment.
- **Nilearn API Contract.** Audit versions, signatures, geometry, temporal order, confounds, masks, parameters, estimator, cache, writes, and verification limits. This prevents silent preprocessing, label, and estimator assumptions. This requires detailed method handoff. Runtime and method-specific QC failures may remain.
- **Nilearn API Operation Record.** Execute one approved API operation once, preserve evidence, verify structure, and stop at the method-owner QC handoff. This preserves exact authorization and data semantics. Any second operation needs new approval. Structural checks cannot accept a scientific result.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and batch-readiness comparison.** Run the approved operation on one fixture or canary before a separately approved batch. This can expose alignment, memory, and cache problems early. This adds a checkpoint and compute. A passing canary does not guarantee cohort-wide validity.
- **Cross-implementation comparison.** Add independent code review and a second approved reader or implementation on a fixture. This improves detection of version-sensitive and geometry errors. This adds review and compute. Agreement does not establish scientific validity.
- **Fixture execution plan.** Add a synthetic or nonstudy fixture with known geometry, time series, labels, and expected shape. This can expose API, alignment, and output defects before observed-data contact. This adds fixture and compute work. This does not validate the study method or biological meaning.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Nilearn. (n.d.-a). *0.14.0 changelog*. https://nilearn.github.io/stable/changes/whats_new.html
- Nilearn. (n.d.-b). *nilearn.connectome.ConnectivityMeasure*. https://nilearn.github.io/stable/modules/generated/nilearn.connectome.ConnectivityMeasure.html
- Nilearn. (n.d.-c). *nilearn.datasets*. https://nilearn.github.io/stable/modules/datasets.html
- Nilearn. (n.d.-d). *nilearn.image.resample_to_img*. https://nilearn.github.io/stable/modules/generated/nilearn.image.resample_to_img.html
- Nilearn. (n.d.-e). *nilearn.interfaces.fmriprep.load_confounds*. https://nilearn.github.io/stable/modules/generated/nilearn.interfaces.fmriprep.load_confounds.html
- Nilearn. (n.d.-f). *nilearn.interfaces.fmriprep.load_confounds_strategy*. https://nilearn.github.io/stable/modules/generated/nilearn.interfaces.fmriprep.load_confounds_strategy.html
- Nilearn. (n.d.-g). *nilearn.maskers.NiftiMasker*. https://nilearn.github.io/stable/modules/generated/nilearn.maskers.NiftiMasker.html
- Nilearn. (n.d.-h). *nilearn.signal.clean*. https://nilearn.github.io/stable/modules/generated/nilearn.signal.clean.html
- Nilearn. (2026). *Nilearn* (Version 0.14.0) [Computer software]. PyPI. https://pypi.org/project/nilearn/
