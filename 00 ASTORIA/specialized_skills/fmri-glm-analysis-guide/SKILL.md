---
name: fmri-glm-analysis-guide
description: >-
  Specifies one user-approved mass-univariate fMRI GLM, from estimand and
  design-matrix columns through contrasts, temporal noise, group model, and
  multiplicity control. Use when the request, or a part coordinator, hands over that
  exact method-guidance handoff. It exposes estimability, filtering, confound,
  censoring, exchangeability, search-space, and software-semantics threats;
  produces a selection-bound fMRI GLM Method Specification; and does not fit a
  model, create design files, choose a contrast or threshold, inspect outcome
  maps, or interpret results. Triggers: specify my fmri GLM, design matrix and
  contrasts for my task.
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

# fMRI GLM Analysis Guide

Specify one bounded mass-univariate fMRI general linear model without allowing
software defaults or observed outcomes to choose the scientific analysis.

## Purpose

`fmri-glm-analysis-guide` owns:

- translating a user-specified fMRI estimand into a conceptual first-level
  design and contrast;
- comparing applicable hemodynamic, nuisance, temporal-noise, censoring,
  run-combination, and group-model routes;
- auditing rank, estimability, residual degrees of freedom, dependence,
  exchangeability, multiplicity, and search-space boundaries;
- producing one user-selected fMRI GLM Method Specification.

The user owns the question, hypothesis, prediction, confirmatory status, estimand,
events and modulators, HRF assumptions, contrasts, confounds, censoring rule,
filter, temporal-noise model, run and group model, covariates, exclusions,
error criterion, search space, interpretation, and claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns general statistical-method comparison.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns cross-software execution of an already approved
statistical specification. [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns the
upstream preprocessing and QC specification, including filter and detrend
selection and operation order. This guide owns only their compatibility with
the GLM design, confounds, and temporal-noise model. A selected fMRI software
adapter owns design-file creation and model execution through a separate
approval.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `GLM`, `fMRI`, `contrast`, `design matrix`, `activation`,
`cluster correction`, `task analysis`, or another broad statistical or
neuroimaging term.

Do not use this skill to:

- invent a hypothesis, task contrast, ROI, or group comparison;
- select regressors, filters, censoring thresholds, covariance structures, or
  correction methods from observed outcomes;
- create events, confounds, design, contrast, or model files;
- fit a voxelwise model, threshold a map, inspect a statistical image, or
  characterize a result;
- describe `p > alpha` as marginal, approaching significance, a trend, or
  nearly supported.

## Inputs

Obtain or mark missing:

- approved scientific question, prediction, estimand, contrast direction, and
  confirmatory or exploratory status;
- participant, session, run, trial, event, volume, voxel, ROI, and group
  inference grains;
- events, onsets, durations, condition coding, parametric modulators, missing
  trials, behavioral values, and units;
- TR, run lengths, acquisition discontinuities, discarded or censored
  volumes, and missing runs;
- preprocessing, interpolation, spatial normalization, smoothing, temporal
  filtering, and denoising already performed or planned;
- candidate HRF basis, temporal or dispersion derivatives, nonlinearities,
  duration assumptions, and software-specific orthogonalization behavior;
- confounds, motion summaries, physiological regressors, outlier indicators,
  censoring or interpolation policy, and any task-confound correlation;
- temporal autocorrelation and prewhitening route plus target software and
  exact version as a later feasibility constraint;
- conceptual first-level columns, intercepts, run effects, contrasts, and how
  every contrast maps across runs, sessions, and group levels;
- group dependence structure, repeated measures, covariates, centering,
  interactions, missingness, variance model, and population target;
- voxelwise, clusterwise, independently defined ROI, small-volume, or other
  mass-univariate search space; route multivariate prediction or
  representational work to [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md);
- multiplicity family, error criterion, thresholding candidates, and
  independent ROI or small-volume definition;
- negative controls, sensitivity analyses, acceptance criteria, and later
  implementation owner.

If the estimand, event coding, contrast, preprocessing state, filtering,
dependence, group target, search space, or confirmatory status is unresolved,
stop with **fMRI GLM intake incomplete**.

## Steps

### 1. Build the GLM Estimand and Design Intake

| Field | Record |
|---|---|
| user-owned target | Question, prediction, estimand, direction, status |
| Measurement | Acquisition, TR, runs, discontinuities, BOLD limitations |
| Events | Onsets, durations, conditions, modulators, units, missingness |
| Preprocessing | Resampling, smoothing, filtering, denoising, censoring |
| First-level columns | Task, basis, nuisance, outlier, run, intercept |
| Contrast | Weights, units, reference, estimand, mapping across levels |
| Error model | Autocorrelation, prewhitening, variance, software semantics |
| Group model | Population, dependence, covariates, interactions, missingness |
| Inference | Search space, family, error criterion, exchangeability |
| Outcome boundary | No statistical-map contact during specification |
| Stop point | Method specification only |

Do not convert `where does this task activate the brain?` into an estimand.

### 2. Gate 1: approve the GLM Estimand and Design Contract

Show:

- the fixed estimand and every unresolved scientific choice;
- a conceptual column ledger with source, units, timing, transformation, and
  intended role for each column;
- the planned contrast at each analysis level;
- selected or eligible HRF, nuisance, censoring, temporal-noise, or group routes
  and why each is in scope;
- exact documentation or paper lookups, excluded operations, and stop point.

Gate 1 authorizes only method comparison and read-only metadata or existing
design inspection. It does not authorize observed-outcome access, design-file
creation, model fitting, package or software changes, thresholding, saving,
or external writes.

### 3. Design choices for the fixed estimand

Carry forward the selected method. Compare eligible routes only when the task leaves a material design choice open, or return a substantive problem with the chosen route to the decision owner.

Offer only routes that answer the fixed estimand. Depending on the design,
these may vary:

- canonical HRF versus an explicitly justified basis set;
- event, epoch, finite-impulse-response, or parametric specification;
- nuisance-regression and censoring representations;
- run-specific versus appropriately pooled first-level effects;
- parametric, robust, mixed-effects, or permutation-based group inference;
- voxelwise, clusterwise, or independently defined ROI search spaces.

For every route state:

- exact estimand and contrast;
- conceptual columns and their units;
- HRF and temporal assumptions;
- filtering, censoring, and confound consequences;
- rank, estimability, residual degrees of freedom, and efficiency;
- temporal-noise and group-dependence assumptions;
- multiplicity family, search space, error criterion, and exchangeability;
- benefit, tradeoff, implementation burden, and main limitation.

Do not rank routes by package availability.

### 4. Audit rank, estimability, and inferential assumptions

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Estimand fit | Rank and estimability | Temporal assumptions | Dependence and exchangeability | Multiplicity | Software semantics | Main limitation |
|---|---|---|---|---|---|---|---|

Run these audits:

- **Column lineage:** every task, modulation, nuisance, outlier, intercept, and
  run column has a defined source and transformation.
- **Timing:** onsets, durations, reference time, slice-time reference, deleted
  volumes, and discontinuities are consistent.
- **Filtering:** data, task regressors, and nuisance regressors receive
  mathematically compatible filtering. A cutoff is not accepted because it
  is conventional.
- **Estimability:** rank, collinearity, contrast span, residual degrees of
  freedom, and task-confound correlation are reviewed before fitting.
- **Orthogonalization:** modulator ordering and any implicit software
  orthogonalization are explicit.
- **Censoring:** deletion, spike regressors, scrubbing, or interpolation is
  compatible with the temporal model and leaves enough usable information.
- **Noise:** temporal autocorrelation and prewhitening are software- and
  acquisition-specific; nominal defaults are not assumed adequate.
- **Levels:** first-level contrasts map coherently to run, session, and group
  estimands. Fixed-effects pooling is not promoted to population inference.
- **Group structure:** repeated observations, site, family, longitudinal, or
  heteroscedastic dependence is represented or declared unsupported.
- **Permutation:** exchangeability and any exchangeability blocks are
  justified for the actual design.
- **Search space:** ROI independence, voxel or cluster search volume,
  contrasts, tails, thresholds, and all tested families are visible.
- **Outcome contact:** no design, contrast, covariate, threshold, or ROI was
  chosen after viewing the target result without an exploratory label.

Stop on rank deficiency, a nonestimable contrast, incompatible filtering,
invalid exchangeability, circular ROI definition, unmodeled dependence, an
undefined multiplicity family, or a group model that cannot support the
claimed population target.

### 5. Gate 2: The user selects one exact GLM specification

Ask the user to select, revise, or reject a route and approve:

- events, basis functions, modulators, nuisance columns, intercepts, and run
  effects;
- the approved upstream filter and detrend specification, its compatible
  treatment of data, design, and confounds, plus censoring, temporal-noise,
  and variance assumptions;
- the exact contrast and estimand at every level;
- group dependence, covariates, missingness, and population target;
- search space, multiplicity family, error criterion, and sensitivity checks;
- implementation owner, software-semantics verification, and stop point.

Do not infer selection from silence. If observed outcomes changed a
confirmatory element, record the deviation and label affected work
exploratory.

### 6. Return the fMRI GLM Method Specification

Return:

```text
fMRI GLM Method Specification
Approved question, prediction, and estimand:
Confirmatory or exploratory status:
Acquisition and preprocessing state:
Events, timing, durations, and modulators:
First-level conceptual column ledger:
HRF and basis specification:
Filtering, nuisance, censoring, and interpolation:
Temporal-noise and prewhitening assumptions:
First-level contrast and units:
Run and session combination:
Group model, dependence, covariates, and population target:
Search space and independent ROI definitions:
Multiplicity family, error criterion, and thresholds:
Exchangeability and permutation restrictions:
Negative controls and sensitivity analyses:
Software-specific semantics to verify:
Known limitations:
Implementation owner and acceptance criteria:
Stop conditions:
```

The specification does not authorize fitting. Route it to one verified
software adapter only through a separate invocation and approval.

## Boundaries

- A design matrix is a claim about the data-generating structure, not merely
  a software input.
- A canonical HRF, derivative, FIR basis, high-pass period, confound set,
  smoothing kernel, censoring rule, or prewhitening model is not universal.
- Filtering must preserve the target signal and be compatible across data,
  design, and nuisance regressors.
- Correlation or VIF is diagnostic evidence, not a universal acceptance
  threshold. Estimability and uncertainty remain design-specific.
- A derivative basis changes parameter meaning. A contrast rule must match
  the selected basis and estimand.
- Software packages can scale columns, orthogonalize modulators, estimate
  autocorrelation, and form variance estimates differently. Verify the exact
  version and semantics before execution.
- Permutation inference still requires justified exchangeability.
- An uncorrected cluster-forming threshold is not, by itself, corrected
  cluster inference.
- Cluster correction, voxel correction, ROI testing, and multiple contrasts
  belong to explicit error families.
- A significant voxel or cluster does not establish a uniquely localized
  cognitive process.
- `p > alpha` is not marginal support, a trend, or evidence of absence.
- Evidence for absence requires an appropriate prespecified method.
- Successful model execution does not establish model adequacy or a
  scientific conclusion.

## GLM design diagnostics and deliverables

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **GLM Decision Record.** Show the column ledger, estimability audit, dependence map, and multiplicity record. This makes hidden design and inference assumptions reviewable. Some package behavior remains version-specific. A prose audit cannot inspect residuals.
- **Labeled GLM route cards.** Compare only GLM routes that answer the fixed estimand and contrast. This separates scientific and software choices. This requires a complete estimand. This does not fit a model.
- **Verified fMRI GLM Method Specification.** Integrate only user-selected fields into the method specification. This preserves scientific ownership and method-software separation. This defers execution. This cannot verify residual behavior.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Executed GLM bundle.** Build and fit the selected design, inspect residuals, and run approved inference. This tests the actual implementation. This introduces outcome contact, software, and artifact risks. This belongs to a separately approved adapter.
- **Extended design-validation bundle.** Add blinded design-matrix diagnostics and simulated-null calibration. This tests selected rank and false-positive risks. This adds code, compute, and another gate. Calibration depends on the simulated noise model.
- **Route cards plus recovery matrix.** Add prespecified design-efficiency and synthetic-recovery comparisons. This reveals selected collinearity and timing failures. This adds simulation assumptions and compute. Synthetic recovery does not validate real noise.

## Checks

- **Positive:** a fixed task contrast with supplied events and group estimand
  produces route cards and a conceptual column ledger, not a fitted model.
- **Negative:** `run an fMRI analysis` does not trigger this skill.
- **Estimability:** stop before integration if the contrast coefficient vector
  lies outside the row space of the design matrix. An estimable vector is
  orthogonal to the design matrix's null space.
- **Filtering:** a high-pass choice that removes the task frequency stops or
  requires a revised route.
- **Dependence:** repeated observations treated as independent stop before
  group specification.
- **Inference:** `use cluster p < .001` without a corrected family, search
  space, and error criterion is rejected as incomplete.
- **Outcome contact:** a contrast chosen from the activation map is recorded
  as post hoc and exploratory.
- **Handoff:** preprocessing questions return to
  [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md); general method questions return to
  [cogsci-statistics](../cogsci-statistics/SKILL.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Eklund, A., Nichols, T. E., & Knutsson, H. (2016). Cluster failure: Why fMRI inferences for spatial extent have inflated false-positive rates. *PNAS, 113*(28). https://doi.org/10.1073/pnas.1602413113
- Nichols & Holmes (2002). https://doi.org/10.1002/hbm.1058
- Nichols et al. (2017). https://doi.org/10.1038/nn.4500
- Olszowy et al. (2019). https://doi.org/10.1038/s41467-019-09230-y
- Poldrack et al. (2008). *Guidelines for reporting an fMRI study*. https://doi.org/10.1016/j.neuroimage.2007.11.048
