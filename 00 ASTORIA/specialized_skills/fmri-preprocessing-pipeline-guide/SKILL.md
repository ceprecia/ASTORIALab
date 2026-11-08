---
name: fmri-preprocessing-pipeline-guide
description: >-
  Specifies one analysis-compatible fMRI preprocessing, denoising, filtering,
  detrending, and outcome-blind QC plan for a user-approved acquisition and
  downstream estimand. Use when the request, or a part coordinator, hands over that
  exact method-guidance handoff. It compares bounded pipeline routes, exposes
  metadata, distortion, resampling, interpolation, space, population, motion,
  confound, temporal-order, exclusion, and provenance threats, and produces a
  selection-bound fMRI Preprocessing and QC Specification without running
  software, changing data, setting universal thresholds, or interpreting
  outcomes. Triggers: plan my fmri preprocessing, denoising and QC plan for
  fmri.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: fmri
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# fMRI Preprocessing Pipeline Guide

Specify one bounded fMRI preprocessing and QC route that is compatible with
the approved downstream analysis. Keep raw-data preservation, preprocessing,
denoising, QC, analysis, and scientific interpretation as distinct layers.

## Purpose

`fmri-preprocessing-pipeline-guide` owns:

- comparing applicable fMRI preprocessing and resampling routes for one
  approved acquisition and downstream estimand;
- specifying motion, slice-timing, susceptibility-distortion, anatomical,
  registration, normalization, surface, smoothing, denoising, filtering, and
  detrending requirements when applicable;
- defining outcome-blind visual and quantitative QC, exclusion, provenance,
  and recovery requirements;
- producing one user-selected fMRI Preprocessing and QC Specification.

The user owns the downstream question, hypothesis, prediction, confirmatory
status, spaces, smoothing, denoising, filtering, censoring, exclusion rules,
QC acceptance criteria, implementation, interpretation, and claims.

[exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns general structure, quality, missingness,
and distribution review. [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md) owns the downstream
mass-univariate GLM specification. A selected fMRI software adapter owns
execution only after this specification is approved.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `preprocess`, `fMRI`, `motion correction`, `fMRIPrep`,
`smoothing`, `confounds`, `quality control`, `denoise`, or another broad
method or software term.

Do not use this skill to:

- choose preprocessing because one package is installed;
- modify raw data, metadata, derivatives, or existing outputs;
- run conversion, validation, preprocessing, denoising, smoothing, filtering,
  or QC software;
- select universal motion, tSNR, DVARS, registration, exclusion, smoothing,
  or filter thresholds;
- inspect task effects, group differences, clinical labels, or downstream
  outcomes to tune preprocessing or exclusion;
- treat cleaner-looking data as evidence that the scientific signal is more
  valid.

## Inputs

Obtain or mark missing:

- approved downstream estimand, analysis family, spatial grain, temporal
  grain, confirmatory status, and required output representation;
- source type, immutable raw-data location, derivative state, provenance,
  checksums, prior processing, and overwrite boundary;
- BIDS or equivalent metadata completeness, scanner, sequence, TR, echo time,
  slice timing, multiband, phase-encoding direction, total readout time,
  fieldmaps, reversed phase encoding, and multiecho status;
- T1w and optional T2w quality, lesions, implants, resection, age, species,
  development, pathology, template suitability, and surface requirements;
- runs, sessions, discarded volumes, nonsteady-state volumes, missing scans,
  discontinuities, and acquisition failures;
- candidate motion estimation, slice-timing, distortion correction,
  coregistration, normalization, resampling, output spaces, resolution,
  interpolation, surface, and smoothing routes;
- candidate nuisance, physiology, global-signal, CompCor, ICA, censoring,
  interpolation, filter, detrend, and regression order;
- downstream GLM, connectivity, decoding, population, surface, ROI, or
  visualization compatibility constraints;
- outcome-blind visual checks, quantitative summaries, exclusion rules,
  reviewer roles, artifact retention, and deviation policy;
- selected implementation tool and exact version only as a later feasibility
  constraint;
- compute, storage, container, license, credential, network, and external
  write boundaries.

If raw provenance, prior processing, acquisition metadata, distortion inputs,
population or template compatibility, downstream estimand, output space,
denoising order, QC independence, or overwrite policy is unresolved, stop
with **fMRI preprocessing intake incomplete**.

## Steps

### 1. Build the Preprocessing Compatibility Intake

| Field | Record |
|---|---|
| user-owned target | Downstream estimand, analysis, status, spatial and temporal grain |
| Source | Immutable raw source, derivative state, provenance, checksums |
| Acquisition | Sequence, timing, encoding, fieldmaps, echoes, missing metadata |
| Anatomy and population | T1w/T2w, lesions, age, species, template and surface limits |
| Geometry | Distortion, motion, registration, spaces, resolution, interpolation |
| Temporal handling | Nonsteady state, slice timing, censoring, filtering, detrending |
| Denoising | Confounds, physiology, CompCor, ICA, global signal, operation order |
| Smoothing | Downstream compatibility, kernel semantics, volume or surface |
| QC | Outcome-blind images, metrics, criteria, reviewer, exclusions |
| Outputs | Derivatives, reports, provenance, collisions, retention |
| Stop point | Specification only |

Do not convert `clean these scans` into a preprocessing specification.

### 2. Gate 1: approve the Preprocessing Compatibility Contract

Show:

- immutable input and derivative boundaries;
- missing, inconsistent, or suspect metadata and required validation;
- the selected analysis-compatible pipeline or eligible alternatives for an unresolved material choice;
- exact ordering differences, output spaces, resampling count, smoothing,
  denoising, filtering, detrending, and QC consequences;
- current tool-version evidence to inspect and every excluded operation.

Gate 1 authorizes only method comparison, read-only metadata inspection, and
review of already existing reports or representative images. It does not
authorize data modification, conversion, preprocessing, resampling,
denoising, filtering, smoothing, package or container changes, downloads,
output writes, overwrite, or external actions.

### 3. Preprocessing choices for the approved acquisition

Carry forward the selected method. Compare eligible routes only when the task leaves a material design choice open, or return a substantive problem with the chosen route to the decision owner.

Offer only routes compatible with the approved acquisition and analysis:

- **Validated minimal derivative route:** a version-pinned workflow that
  performs anatomical and BOLD preprocessing while leaving analysis-specific
  denoising and smoothing to a later approved stage.
- **Analysis-specific extension route:** the same provenance-preserving base
  plus a separately specified denoising, filtering, smoothing, surface, or
  native-space extension required by the approved estimand.
- **Existing-derivative compatibility route:** retain an already processed
  dataset only if its provenance, operations, spaces, interpolation, confounds,
  and QC can be established and are compatible with the downstream analysis.
- **Special-population or acquisition route:** a bounded alternative when
  lesions, development, species, multiecho acquisition, fieldmap limitations,
  severe distortion, or surface requirements invalidate ordinary assumptions.

For every route state:

- included, skipped, and deferred operations in exact order;
- required metadata, files, templates, and software semantics;
- transform composition, resampling count, interpolation, spaces, resolution,
  and smoothing;
- denoising, censoring, filtering, detrending, and confound consequences;
- QC evidence, exclusion policy, provenance, artifacts, resources, benefit,
  tradeoff, and main limitation.

Do not rank by convenience or installed software.

### 4. Document the Preprocessing Decision Record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Acquisition fit | Downstream fit | Ordering and resampling | Denoising and filtering | QC and exclusions | Provenance | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- prior preprocessing that cannot be reconstructed or may be applied twice;
- missing or contradictory phase-encoding, readout, slice-timing, echo, or
  fieldmap metadata;
- susceptibility correction inputs that do not match the BOLD acquisition;
- anatomical registration, template, or surface assumptions invalid for the
  population or pathology;
- repeated interpolation, inappropriate reference images, or incompatible
  output resolution;
- smoothing that destroys the spatial grain needed for decoding, laminar,
  small-ROI, or surface analyses;
- censoring or interpolation that breaks timing, temporal dependence, or
  downstream estimability;
- nuisance regression, temporal filtering, and detrending performed in an
  order that reintroduces removed frequencies or makes regressors
  mathematically inconsistent;
- CompCor components used without the corresponding filtering basis required
  by the exact workflow that produced them;
- motion or data quantity differences that confound group or condition
  comparisons;
- too little usable time or too many exclusions to support the target
  analysis;
- QC criteria tuned against task effects, outcomes, diagnosis, group, or
  desired results;
- silent version drift, partial outputs, collisions, missing provenance, or
  overwrite risk.

Keep an observed failure visible. Do not solve it by changing an exclusion
rule after outcome contact.

### 5. Gate 2: The user selects one exact preprocessing and QC specification

Ask the user to select, revise, or reject a route and approve:

- source boundary, metadata corrections, anatomical and distortion route;
- motion, slice-timing, registration, normalization, spaces, resolution,
  interpolation, resampling, surface, and smoothing;
- denoising, confounds, physiology, censoring, filtering, detrending, and
  exact operation order;
- outcome-blind visual checks, quantitative summaries, acceptance criteria,
  exclusions, reviewer, and deviation handling;
- version-pinned implementation owner, artifacts, provenance, compute,
  storage, and stop point.

Do not infer selection from silence. If outcome contact changed a
confirmatory preprocessing or exclusion decision, record the deviation and
label affected analyses exploratory.

### 6. Return the fMRI Preprocessing and QC Specification

Return:

```text
fMRI Preprocessing and QC Specification
Approved downstream estimand and analysis:
Confirmatory or exploratory status:
Immutable input source and provenance:
Acquisition and metadata requirements:
Anatomical, population, lesion, and template constraints:
Nonsteady-state and reference handling:
Motion and slice-timing route:
Susceptibility-distortion route:
Coregistration, normalization, and transform composition:
Output spaces, resolution, interpolation, and resampling:
Surface and smoothing specification:
Denoising, confounds, physiology, and global-signal policy:
Censoring, interpolation, filtering, and detrending order:
Outcome-blind visual QC:
Quantitative QC summaries and acceptance criteria:
Exclusion, missingness, deviation, and review policy:
Outputs, reports, provenance, retention, and collision policy:
Implementation owner, exact version, and acceptance tests:
Known limitations:
Stop conditions:
```

The specification does not authorize execution. Route it to one verified
software adapter only through a separate invocation and approval.

## Boundaries

- Preprocessing is analysis-dependent. No universal sequence, parameter set,
  motion cutoff, exclusion threshold, smoothing kernel, or output space is
  valid for every fMRI study.
- Preserve immutable raw inputs and complete provenance. Never overwrite the
  only copy of source data or silently process an existing derivative again.
- Slice-timing decisions depend on metadata, acquisition, analysis, and exact
  workflow behavior. Fast TR alone is not a universal reason to skip it.
- Susceptibility correction must match the acquisition and its metadata.
- Compose spatial transforms and minimize interpolation when the selected
  workflow permits, while preserving the exact interpolation history.
- Current fMRIPrep `25.2.5` estimates BOLD motion before optional
  slice-timing correction, performs slice-timing only when supported by
  `SliceTiming` metadata, and composes transforms for one-shot BOLD
  resampling. Verify these behaviors again for the execution version.
- fMRIPrep provides minimally processed derivatives and confound estimates;
  it does not choose the scientifically appropriate denoising strategy.
- In current fMRIPrep behavior, CompCor estimation follows high-pass
  filtering. If those components are selected downstream, preserve the
  corresponding cosine regressors or otherwise prove mathematical
  compatibility with the selected temporal model.
- Regression, censoring, interpolation, filtering, and detrending can interact
  and reintroduce artifacts. Specify and verify the joint operation.
- Smoothing must match the downstream spatial estimand. It is not a universal
  preprocessing requirement.
- QC combines visual evidence, quantitative summaries, acquisition context,
  and prespecified decisions. One metric does not establish acceptability.
- Exclusions and preprocessing changes must not be tuned to produce a desired
  task effect or group result.
- Cleaner images do not establish valid neural measurement or inference.
- Successful software completion does not establish registration quality,
  denoising adequacy, or scientific validity.

## Preprocessing fit and QC evidence

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **Labeled preprocessing route cards.** Show the selected or sole eligible route. Compare alternatives only when a material choice remains and each route fits the fixed acquisition and downstream estimand. The cards make analysis-dependent choices visible and require complete metadata and analysis requirements. They do not run preprocessing.
- **Preprocessing Decision Record.** Show the compatibility intake, operation-order ledger, QC plan, and provenance risks. This makes hidden acquisition and downstream dependencies reviewable. Some tool behavior remains version-specific. A plan cannot reveal all image artifacts.
- **Verified fMRI Preprocessing and QC Specification.** Integrate only user-selected operations into the specification. This preserves scientific ownership and method-software separation. This defers execution and image QC. This cannot certify data quality.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended QC and robustness protocol.** Add blinded multi-reviewer visual QC and selected preprocessing-sensitivity analyses. This reduces dependence on one reviewer or route. This adds reviewer time, compute, and multiplicity. Agreement does not prove measurement validity.
- **Route cards plus recovery and sensitivity matrix.** Add a bounded synthetic or representative-file transform and denoising sensitivity plan. This reveals selected interpolation and temporal-order risks. This adds data handling and compute. Representative behavior may not generalize across the study.
- **Verified derivative and QC bundle.** Execute the pinned pipeline and complete prespecified visual and quantitative QC. This tests the actual data and software path. This introduces data, compute, storage, and exclusion risks. This belongs to a separately approved adapter.

## Checks

- **Positive:** a BIDS task-fMRI dataset with a fixed decoding analysis
  produces analysis-compatible route cards and an outcome-blind QC plan, not
  derivatives.
- **Negative:** `preprocess my scans` does not trigger this skill.
- **Metadata:** missing phase-encoding or readout information blocks a
  susceptibility route that requires it.
- **Prior processing:** an undocumented derivative stops before any repeated
  correction.
- **Order:** filtering after nuisance regression that reintroduces removed
  frequencies is flagged and must be redesigned.
- **Population:** a standard adult template is not silently chosen for a
  lesion, developmental, animal, or otherwise incompatible population.
- **Outcome contact:** changing motion exclusion after viewing a group effect
  is recorded as post hoc and the affected work becomes exploratory.
- **Report review:** existing fMRIPrep reports and image observations belong
  to [review-fmriprep-qc](../review-fmriprep-qc/SKILL.md) with the approved
  criteria, selected scope and remaining decisions. A report-reading request
  need not restart this skill's full preprocessing specification.
- **Handoff:** downstream mass-univariate design returns to
  [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md); general data-quality review returns to
  [exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Ciric et al. (2017). https://doi.org/10.1016/j.neuroimage.2017.03.020
- Esteban et al. (2019). https://doi.org/10.1038/s41592-018-0235-4
- NiPreps. (n.d.). *fMRIPrep outputs* (Version 25.2.5). https://fmriprep.org/en/25.2.5/outputs.html
- NiPreps. (n.d.). *fMRIPrep workflows* (Version 25.2.5). https://fmriprep.org/en/25.2.5/workflows.html
- Poldrack et al. (2008). *Guidelines for reporting an fMRI study*. https://doi.org/10.1016/j.neuroimage.2007.11.048
- Power et al. (2012). https://doi.org/10.1016/j.neuroimage.2011.10.018
