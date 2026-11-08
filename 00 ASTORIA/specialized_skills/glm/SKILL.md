---
name: glm
description: >-
  Translates one already approved mass-univariate fMRI GLM Method Specification
  into one exact design-materialization, first-level fit-and-contrast, or
  second-level fit-and-contrast implementation through a selected
  version-verified software adapter, then returns a design, execution,
  map-semantics, verification, and provenance record. Use when the request names
  this skill or fmri-glm-analysis-guide, fmri-coordinator, or a selected software
  adapter routes one exact GLM implementation handoff. It makes events, columns,
  timing, filtering, confounds, censoring, rank, contrasts, noise and variance
  semantics, image geometry, map types, runtime, writes, and outcome-contact
  boundaries visible. Triggers: materialize and fit the fmri GLM, first level
  fit and contrast.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: FSL or nilearn; preprocessed BOLD
  gates: training or running on real data, accepting results
  created: "2026-07-23"
  updated: "2026-10-29"
---

# GLM

Translate one approved mass-univariate fMRI GLM specification into one exact,
inspectable implementation without allowing software defaults or observed
maps to revise the scientific design.

## Purpose

It does not choose regressors, contrasts, filters, covariance, group models, thresholds, correction, software, or claims; install software; invent events; inspect outcomes before the design is frozen; threshold maps; overwrite; or chain analysis levels.

`glm` owns:

- binding one approved fMRI GLM Method Specification to one selected software
  implementation;
- exact event, time-axis, design-column, contrast, run, subject, group, mask,
  image, and output identity;
- design materialization and structural validation before outcome contact;
- one approved design-only, first-level fit-and-contrast, or second-level
  fit-and-contrast operation;
- reconciliation of model-level semantics across the selected public API,
  command, batch, or design-file representation;
- explicit runtime, cache, report, temporary, output, collision, and
  side-effect control with the selected software adapter;
- separation of effect, variance, test-statistic, z-score, p-value, residual,
  and diagnostic artifacts;
- a GLM Implementation Record and neutral QC Handoff Packet.

The user owns the scientific question, hypothesis, prediction, confirmatory
status, estimand, events, durations, modulators, HRF basis, confounds,
censoring, filtering, temporal-noise model, run and group model, covariates,
contrast, variance assumptions, exchangeability, multiplicity, search space,
thresholds, exclusions, interpretation, and claims.

[fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md) owns method selection and the authoritative fMRI
GLM Method Specification. [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns upstream
filtering and detrending. [nilearn-tool](../nilearn-tool/SKILL.md) owns exact Nilearn API execution,
[fsl-tool](../fsl-tool/SKILL.md) owns exact FSL execution, and another verified software adapter
owns its own syntax and runtime. [statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns an approved
cross-software statistical implementation when no fMRI-specific owner
applies. This skill does not absorb software adapters or select among them
because one happens to be installed.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `GLM`, `general linear model`, `fMRI activation`,
`contrast`, `design matrix`, `first level`, `second level`, `task fMRI`,
`Nilearn GLM`, `FEAT`, `SPM`, `threshold map`, or another broad method,
software, or output phrase.

Do not use this skill to:

- formulate an estimand, event model, contrast, nuisance model, filter,
  temporal covariance, group model, search space, or correction procedure;
- invent or repair events, confounds, censoring indicators, subject metadata,
  or missing contrasts;
- choose Nilearn, FSL, SPM, AFNI, or another backend from availability;
- install, update, configure, license, or activate a backend;
- threshold, cluster, report, or interpret a statistical map;
- describe `p > alpha` as marginal, approaching significance, a trend, or
  nearly supported;
- run first and second levels under one approval.

## Inputs

Obtain or mark missing:

- one approved fMRI GLM Method Specification from
  [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md);
- one operation type: design materialization, first-level fit-and-contrast,
  or second-level fit-and-contrast;
- exact participant, session, run, subject, contrast, and group scope;
- immutable BOLD, surface, contrast-map, mask, events, confounds, censoring,
  and group-table manifests with hashes and one-to-one associations;
- TR, frame times, slice-time reference, discarded-volume history, run
  discontinuities, and time units;
- approved event onsets, durations, trial types, modulators, transformations,
  centering, orthogonalization, and missing-event policy;
- approved task, nuisance, drift, intercept, run, outlier, and covariate
  columns with lineage, units, and order;
- approved filtering and detrending state for data, task regressors, and
  nuisance regressors;
- approved HRF basis, convolution, oversampling, derivatives, FIR delays,
  temporal-noise model, prewhitening, signal scaling, variance model, and
  censoring representation;
- exact contrast vector or matrix, column order, tails, units, estimand,
  level mapping, and missing-run or subject policy;
- group dependence, exchangeability, repeated-measures, site, family,
  covariate, centering, interaction, missingness, and variance specification;
- image shape, dtype, affine, qform, sform, orientation, space, mask, and
  smoothing provenance;
- the approved backend and software adapter, if already selected. Record its
  exact release, public API or command, source state, license, accepted defaults
  and semantic translation before implementation. If the choice is still open,
  mark it for Step 5; keep the scientific specification fixed.
- rank, estimability, condition, residual-degrees-of-freedom, contrast-span,
  task-confound-correlation, and design-QC plan;
- resource, memory, threads, parallel, cache, report, temporary, work,
  destination, collision, rollback, and failure policy;
- expected unthresholded outputs, map types, units, headers, metadata, logs,
  diagnostics, provenance, and hashes;
- outcome-visibility boundary and compute and destination authority.

If the method specification, operation, inputs, timing, design columns,
filtering, contrast, noise model, group structure, outcome boundary, or output
contract is unresolved, stop with **fMRI GLM implementation contract incomplete**.
A still-open backend choice permits assessment of eligible routes only. Exact
backend semantics must be verified before execution.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one implementation transition

Choose exactly one:

1. materialize and validate one design matrix and contrast representation
   without fitting;
2. fit one approved first-level model for the enumerated run or subject scope
   and compute only the named approved contrast set;
3. fit one approved second-level model from one aligned first-level contrast
   family and compute only the named approved group contrast set.

A fit-and-contrast is one bounded operation only when the contrasts are frozen
before fitting and the selected backend requires the fitted object to compute
them. Do not inspect beta, residual, statistic, or contrast maps between fit
and contrast computation. Never proceed from first level to second level,
thresholding, ROI extraction, reporting, or interpretation automatically.

### 2. Start the method-to-implementation binding

Start a **GLM Binding Ledger** with the approved scientific choices. Carry open backend fields forward to complete and freeze during authorized Gate 1 preflight.

| Method element | Approved meaning | Exact implementation | Accepted default | Verification |
|---|---|---|---|---|
| Time axis and events | | | | |
| HRF and task columns | | | | |
| Confounds and censoring | | | | |
| Filter and drift terms | | | | |
| Noise and variance model | | | | |
| Run and group structure | | | | |
| Contrasts and estimands | | | | |
| Mask, geometry, and space | | | | |
| Output map types and units | | | | |

Every implementation field must map to an approved method element. A backend
default with no method-level meaning is unresolved, not accepted. A method
element that the selected backend cannot represent is a compatibility stop,
not permission to approximate it silently.

### 3. Audit inputs before outcome contact

Verify:

- BOLD volumes, frame times, events, confounds, censoring rows, and design
  rows have compatible counts and time origins;
- discarded volumes and slice-time reference are reflected consistently;
- event, duration, modulator, and confound units and missingness are explicit;
- run boundaries, discontinuities, intercepts, and concatenation behavior
  match the approved specification;
- data, task regressors, nuisance regressors, and censoring receive compatible
  filtering and detrending;
- no regressor was derived from the target outcome map;
- first-level contrast maps used at second level share contrast meaning,
  units, geometry, space, smoothing, and preprocessing provenance;
- subject rows and contrast maps are one-to-one and in the same explicit
  order;
- group covariates, interactions, and repeated observations preserve the
  approved population and dependence structure.

Do not repair a timing, row, contrast, or geometry mismatch. Return it to the
source owner or method guide.

### 4. Prepare the design audit

Use the approved scientific specification and available authorized evidence to
plan the design audit. Construct the exact backend-dependent design and
contrast representations only after selecting a compatible backend and
obtaining Gate 1 authorization for that work. Then construct them without
fitting and record:

- ordered column names, definitions, sources, units, and transformations;
- column-wise range, variance, missingness, and nonfinite state;
- rank, singular values or condition evidence, residual degrees of freedom,
  and aliases;
- task-confound and task-drift relationships;
- contrast vectors aligned by exact column name and order;
- whether each contrast lies in the estimable row space;
- backend-specific intercept, drift, scaling, orthogonalization, censoring,
  and prewhitening semantics;
- design and contrast hashes plus the exact code, command, or batch fields
  that produced them.

When design visualization is separately authorized, use only the design
matrix. Complete the rank, estimability, timing, and contrast checks
regardless of how the design looks.

### 5. Verify the selected backend or resolve an open choice

Check the user's approved backend against the fixed scientific specification.
Carry it forward if compatible. If it cannot represent the specification,
report the blocker and stop before preflight or execution. Leave any change
in route to the user.

When a material backend choice remains open and more than one verified backend
can represent the approved specification exactly, compare them on:

- model and covariance semantics;
- design and contrast encoding;
- filtering, drift, scaling, censoring, and prewhitening behavior;
- fixed-effects, mixed-effects, or permutation support required by the
  specification;
- image and surface support;
- version, source, license, runtime, cache, report, and write behavior;
- reproducibility, visible outputs, benefit, tradeoff, and limitation.

If the choice remains open and only one verified backend fits, explain its
limitation and seek the user's selection before preflight. Keep ranking and
selection with the user. A change in backend semantics returns to
[fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md) when it changes the scientific specification.

### 6. Plan preflight of the selected software adapter

Use available authorized evidence to identify the exact version, source,
license, public signature or command help, environment, executable,
configuration, resources, implicit writes, reports, caches, and failure
behavior. Carry any additional required inspection into the Gate 1 scope.

For Nilearn, the current release reviewed for this design is `0.14.0`, full
commit `0d0429a12efa131bf46bb30654f9d1630d950f73`, released 2026-07-02.
Current `FirstLevelModel` and `SecondLevelModel` APIs can create masks,
resample, smooth, scale, filter, generate reports, and retain or discard fit
details depending on parameters. Every such behavior is explicit. In
`0.14.0`, `SecondLevelModel(reports=True)` is a new default that retains data
for reports and can affect memory and outputs.

Nilearn examples often fetch datasets and use illustrative thresholds. Do
not copy their downloads, default drift cutoff, automatic mask, smoothing,
report, threshold, alpha, cluster size, or plotting choices.

FSL, SPM, AFNI, and other backends use only their exact selected software
adapter and current primary documentation. Verify the participant's selected backend, interpreter, packages and licenses at invocation time within the authorized Gate 1 scope. Treat availability as feasibility evidence. Use the user's approved choice to select the backend and the applicable gate to authorize work.

### 7. Gate 1: approve read-only preflight and frozen binding

Show:

- operation and scope;
- GLM Binding Ledger with the approved method fields, available verified
  implementation bindings, and open verification items;
- input, timing, geometry, and order evidence already available and checks
  proposed for preflight;
- proposed design and contrast encoding, rank, estimability, and condition
  checks, and any evidence already available;
- selected compatible implementation route and exact source and API evidence
  to inspect;
- expected reads, outcome boundary, resources, side effects, outputs, and
  stop point.

Gate 1 authorizes only the displayed bounded metadata, header, design,
contrast, version, API, resource, collision, and destination inspection plus
exact code, command, or batch construction. It does not authorize model
fitting, outcome-map access, package changes, cache or report creation,
thresholding, plotting, output writes, retries, or another analysis level.

After Gate 1 authorization, perform the approved inspections, construct and
audit the exact design and contrast without fitting, and complete and freeze
the binding ledger. Resolve preflight blockers before proposing the exact
Gate 2 action.

### 8. Construct the exact execution

Display:

- selected adapter and exact version or source identity;
- immutable input and design manifests;
- exact code, command, design files, batch fields, and configuration;
- every explicit parameter and intentionally accepted default;
- contrast vector or matrix with column alignment;
- mask, space, geometry, scaling, filtering, covariance, and output
  semantics;
- resources, threads, randomness, cache, report, work, temporary, and
  writable paths;
- expected unthresholded map and diagnostic inventory;
- collision, partial-state, failure, rollback, and verification behavior;
- exact stop point.

The implementation must not download example data, auto-create a scientific
mask without approval, derive a contrast from a string that was not checked
against exact columns, overwrite outputs, or open outcome maps before the
design and execution are frozen.

### 9. Gate 2: approve one exact fit or design action

Ask the user to approve the displayed execution, inputs, design, contrasts,
backend, parameters, accepted defaults, resources, reads, writes, reports,
caches, outputs, verification, and stop point.

Gate 2 authorizes only that operation. A changed event, confound, censoring
row, column, contrast, mask, model, backend, parameter, subject, destination,
retry, second analysis level, threshold, plot, ROI summary, or interpretation
requires a new contract and any applicable method-owner review.

### 10. Execute once and preserve evidence

Run through the selected software adapter only within the approved contract.
Capture:

- exact environment, source, API or executable, code, command, batch, and
  configuration;
- immutable input, design, contrast, mask, participant, and group manifests;
- resource, thread, cache, report, work, temporary, and destination state;
- start and end time, exit status, stdout, stderr, warnings, and failures;
- backend-generated design, model, contrast, residual, variance, statistic,
  report, and log artifacts;
- all implicit, unexpected, partial, or missing writes;
- deviations from the frozen binding.

Do not retry, resume, change a model option, weaken a check, remove a column,
drop a subject, alter a contrast, open a target map for redesign, threshold,
plot, clean, or continue to another level without new approval.

### 11. Verify and stop at the QC handoff

Separate:

1. **Execution conformance:** exact source, software, code, arguments, inputs,
   design, contrast, resources, writes, process state, and deviations.
2. **Structural verification:** artifact inventory, dimensions, geometry,
   space, header, dtype, units, finite and invalid state, column and contrast
   identity, and hashes.
3. **Model-QC handoff:** design rank and condition, residual and covariance
   diagnostics, warnings, failed voxels or vertices, registration and mask
   evidence, and prespecified outcome-blind QC criteria.
4. **Scientific decision:** the user decides validity, exclusions, remediation,
   inferential continuation, thresholding, interpretation, and claims.

Never describe an effect-size map as a test statistic, a t map as a z map, an
uncorrected p map as corrected evidence, or a thresholded display as the
inferential result.

Return:

```text
GLM Implementation Record
Approved operation, level, estimand, and scope:
Method Specification identity:
Input, timing, mask, geometry, and order manifest:
Design columns, rank, condition, and residual degrees of freedom:
Contrast definitions, vectors, units, and estimability:
Filtering, censoring, noise, scaling, and variance semantics:
Selected backend, exact version, source, and adapter:
Exact code, command, batch, configuration, and accepted defaults:
Resources, caches, reports, temporary files, and writes:
Exit state, warnings, failures, and deviations:
Unthresholded output and map-semantics inventory:
Execution-conformance and structural-verification result:
Model-QC evidence and limitations:
user-owned validity, inference, interpretation, and next decision:
```

## Boundaries

- Stop without an approved fMRI GLM Method Specification.
- Stop when one request combines design, first-level, second-level,
  thresholding, reporting, ROI extraction, and interpretation.
- Stop on unmatched time rows, event units, confound rows, censoring rows,
  subject rows, contrast maps, masks, geometry, spaces, or column order.
- Stop on rank deficiency, nonestimable contrasts, inadequate residual
  degrees of freedom, unresolved aliasing, or incompatible filtering.
- Stop when software orthogonalization, drift, scaling, prewhitening,
  censoring, fixed-effects, or group-variance semantics cannot represent the
  approved specification exactly.
- Stop if a design, contrast, threshold, ROI, or exclusion changed after
  target-map contact without an explicit exploratory deviation record.
- Stop before package installation, environment activation, license change,
  example-data fetch, automatic mask creation, report or cache write, or
  output creation that is not in Gate 2.
- Stop before overwrite, cleanup, retry, resume, subject removal, changed
  resources, or a second analysis level.
- Preserve unthresholded outputs, warnings, failures, invalid voxels or
  vertices, and exact map semantics.
- Do not accept a backend's conventional default as a scientific choice.
- Do not use outcome maps to repair design efficiency, select a contrast,
  choose a threshold, define an ROI, or relabel confirmatory work.
- A zero exit status, estimable contrast, plausible map, or complete report
  does not establish model validity or scientific support.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- BIDS. (n.d.). *BIDS specification* (Version 1.11.1). https://bids-specification.readthedocs.io/en/stable/
- Nichols et al. (2017). Best practices in data analysis and sharing in neuroimaging using MRI. https://doi.org/10.1038/nn.4500
- Nilearn. (n.d.). *First-level GLM guide*. https://nilearn.github.io/stable/glm/first_level_model.html
- Nilearn. (n.d.). *nilearn.glm.first_level.FirstLevelModel*. https://nilearn.github.io/stable/modules/generated/nilearn.glm.first_level.FirstLevelModel.html
- Nilearn. (n.d.). *nilearn.glm.second_level.SecondLevelModel*. https://nilearn.github.io/stable/modules/generated/nilearn.glm.second_level.SecondLevelModel.html
- Nilearn. (n.d.). *Second-level GLM guide*. https://nilearn.github.io/stable/glm/second_level_model.html
- Nilearn. (2026). *Nilearn* (Version 0.14.0) [Computer software]. GitHub. https://github.com/nilearn/nilearn/releases/tag/0.14.0
