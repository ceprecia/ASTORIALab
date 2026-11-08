---
name: neural-population-analysis-guide
description: >-
  Compares linear and latent-variable neural-population method families for one
  user-specified population estimand and recording design. Use when the request,
  or a part coordinator, hands over that exact conditional method-guidance handoff.
  It distinguishes variance, shared covariance, single-trial trajectories,
  task-demixed structure, dynamics, and visualization; exposes simultaneity,
  pseudo-population, normalization, trial, unit, session, alignment,
  dimensionality, stability, and inference limits; and produces a
  selection-bound Neural Population Method Specification without preprocessing
  signals, fitting a model, choosing dimensions, or interpreting a latent space.
  Triggers: analyze neural population activity, latent variable model for
  spiking data.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: ephys
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Neural Population Analysis Guide

Specify one bounded dimensionality-reduction or latent-variable analysis for
neural population signals. Preserve the difference among data compression,
shared covariance, task demixing, single-trial trajectories, dynamics,
visualization, and scientific explanation.

## Purpose

`neural-population-analysis-guide` owns:

- distinguishing PCA, factor-analysis, GPFA, dPCA, jPCA, latent-state, and
  bounded nonlinear-visualization roles;
- checking whether simultaneously or sequentially recorded data can support
  the selected population estimand;
- defining unit, trial, time, condition, session, participant, normalization,
  alignment, dimension, validation, null, and stability requirements;
- comparing applicable method routes without automatic selection;
- producing one user-selected Neural Population Method Specification.

The user owns the question, hypothesis, prediction, confirmatory status,
population estimand, inclusion and preprocessing rules, normalization,
condition factors, time binning, method family, dimensionality, alignment,
validation, interpretation, and claims.

[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns predictive decoding, encoding, RSA, and
temporal-generalization specifications. [cogsci-statistics](../cogsci-statistics/SKILL.md) owns general
statistical-method comparison. A modality or software adapter owns signal
processing and model execution only after this method specification is
approved.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `population analysis`, `PCA`, `latent space`, `neural
manifold`, `trajectory`, `GPFA`, `dPCA`, `jPCA`, `Neuropixels`, `calcium
imaging`, or another broad method or modality term.

Do not use this skill to:

- invent a population hypothesis or task factor;
- perform spike sorting, event detection, source reconstruction,
  deconvolution, preprocessing, unit selection, or trial exclusion;
- choose normalization, time bins, method, dimensions, variance cutoff,
  alignment, rotations, or visualization parameters automatically;
- fit a latent model, create an embedding, select units from results, or
  inspect target outcomes;
- call a visually compact manifold a biological state, attractor, mechanism,
  cluster, or low-dimensional neural code without separate evidence.

## Inputs

Obtain or mark missing:

- approved question, prediction, population estimand, claim boundary, and
  confirmatory or exploratory status;
- recording modality, simultaneity, acquisition, preprocessing, unit-quality,
  event-alignment, and measurement limitations;
- participant, session, population, unit, trial, condition, event, time-bin,
  and observation grains;
- whether the data are simultaneous, sequential, or a constructed
  pseudo-population and which covariance claims are therefore permitted;
- unit inclusion, stability, dropout, drift, missingness, repeated units,
  session identity, and cross-session correspondence;
- trial counts and balance by condition, factorial cells, reaction time,
  behavioral covariates, and missing cells;
- rate, count, event, fluorescence, or other response representation,
  baseline, smoothing, binning, variance stabilization, centering,
  normalization, and averaging candidates;
- candidate variance-compression, shared-covariance, single-trial trajectory,
  task-demixing, dynamical, alignment, or visualization routes;
- candidate dimension-selection, crossvalidation, held-out prediction,
  reconstruction, stability, null, shuffle, and negative-control criteria;
- repeated-session or cross-condition generalization, alignment, and
  comparability goals;
- uncertainty grain, multiplicity family, computational limit, later
  implementation owner, and acceptance criteria.

If the population estimand, simultaneity, unit and trial grains, preprocessing,
condition structure, normalization, validation target, permitted covariance
claim, or confirmatory status is unresolved, stop with **neural population
intake incomplete**.

## Steps

### 1. Build the Neural Population Intake Record

| Field | Record |
|---|---|
| user-owned target | Question, prediction, estimand, status, permitted claim |
| Recording | Modality, simultaneous or sequential, preprocessing, limits |
| Observations | Participants, sessions, units, trials, conditions, time bins |
| Population integrity | Unit stability, dropout, drift, missingness, correspondence |
| Representation | Counts, rates, events, fluorescence, averaging, binning |
| Factors | Task variables, interactions, behavioral covariates, balance |
| Candidate role | Variance, shared covariance, trajectories, demixing, dynamics, visualization |
| Validation | Held-out target, dimensions, reconstruction, stability, null |
| Inference | Uncertainty grain, multiplicity, permitted population claim |
| Outcome boundary | No target-result contact during specification |
| Stop point | Method specification only |

Do not convert `find the neural manifold` into an estimand.

### 2. Gate 1: approve the Population Estimand and Data Contract

Show:

- the fixed estimand and permitted population claim;
- simultaneity, observation, factor, missingness, drift, and preprocessing
  record;
- the selected method route or eligible alternatives for an unresolved choice;
- normalization, dimension, validation, alignment, null, and interpretation
  risks;
- exact source lookups, excluded operations, and stop point.

Gate 1 authorizes only method comparison and read-only metadata or existing
design inspection. It does not authorize signal preprocessing, unit
selection, normalization, averaging, model fitting, dimensionality selection,
alignment, visualization, package changes, saving, or external writes.

### 3. Population analysis choices for the approved estimand

Carry forward the selected method. Compare eligible routes only when the task leaves a material design choice open, or return a substantive problem with the chosen route to the decision owner.

Offer only routes supported by the data and estimand:

- **PCA or related linear compression:** describes axes of high variance
  under the selected centering and scaling, without a latent-noise model.
- **Factor analysis:** models shared covariance at the defined observation
  grain when simultaneous data and distributional assumptions support it.
- **GPFA or another latent trajectory model:** estimates smooth
  low-dimensional single-trial population trajectories under an explicit
  observation and temporal model.
- **dPCA or another supervised demixing route:** separates variance associated
  with prespecified task factors when factorial support and regularization are
  defensible.
- **jPCA or another constrained dynamical summary:** evaluates a prespecified
  rotational or dynamical structure under explicit preprocessing, alignment,
  and null comparisons.
- **Nonlinear embedding:** serves only as exploratory visualization and
  sensitivity analysis, never as standalone inferential evidence for clusters
  or biological manifolds.

For every route state:

- estimand and method role;
- required simultaneity and observation grain;
- centering, scaling, normalization, binning, averaging, and missingness
  consequences;
- condition and trial requirements;
- dimension selection, validation, null, stability, and alignment;
- permitted claim, compute, benefit, tradeoff, and main limitation.

Do not rank by visual appeal or explained variance alone.

### 4. Document preprocessing and dimension in the decision record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Estimand fit | Simultaneity and trials | Preprocessing sensitivity | Dimension and validation | Stability and alignment | Permitted claim | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- pseudo-populations used to estimate trial-by-trial shared covariance or
  dynamics not present in simultaneously observed activity;
- trial averaging that removes variability needed for a single-trial claim;
- single-trial methods applied to condition means or sparse, unbalanced cells;
- unit normalization that changes whether high-rate, low-rate, or variable
  units dominate the estimand;
- fixed rate, count, smoothing, bin, neuron, trial, or session thresholds
  treated as universal;
- unit dropout, waveform or response drift, unstable correspondence, and
  session-specific preprocessing;
- condition imbalance, missing factorial cells, reaction-time structure, and
  repeated-trial dependence;
- dimensions selected by arbitrary cumulative variance rather than a
  prespecified validation and stability criterion;
- crossvalidation that splits dependent trials or tunes dimensions on the
  evaluation data;
- dPCA marginals or axes interpreted as pure task processes;
- rotational structure assessed without matching nulls and sensitivity to
  alignment, time window, and preprocessing;
- cross-session alignment that forces similarity or erases meaningful change;
- nonlinear embeddings treated as metric spaces, clusters, inferential tests,
  or mechanistic evidence.

Stop when the recording cannot support the selected covariance or dynamics
claim, when pseudo-population limitations are hidden, when condition cells
cannot identify the selected factor, when alignment lacks correspondence or
validation, or when outcome contact invalidates confirmatory dimension or
method selection.

### 5. Gate 2: The user selects one exact population specification

Ask the user to select, revise, or reject a route and approve:

- population, unit, trial, condition, session, and time grains;
- preprocessing, binning, averaging, centering, normalization, inclusion,
  missingness, and drift rules;
- method family, task factors, dimension criterion, regularization, and
  alignment;
- held-out target, crossvalidation, nulls, shuffles, stability, uncertainty,
  multiplicity, and negative controls;
- permitted interpretation, implementation owner, and stop point.

Do not infer selection from silence. If outcomes changed a confirmatory unit,
time window, normalization, method, factor, dimension, or alignment choice,
record the deviation and label affected work exploratory.

### 6. Return the Neural Population Method Specification

Return:

```text
Neural Population Method Specification
Approved question, prediction, and estimand:
Confirmatory or exploratory status:
Permitted and prohibited claims:
Recording modality, simultaneity, and measurement limits:
Participant, session, unit, trial, condition, and time grains:
Unit inclusion, stability, dropout, drift, and missingness:
Response representation, binning, averaging, centering, and normalization:
Task factors, balance, covariates, and factorial support:
Selected method family and model role:
Dimensionality and regularization criterion:
Crossvalidation, held-out target, and uncertainty grain:
Nulls, shuffles, negative controls, and multiplicity:
Cross-session or cross-condition alignment:
Stability and sensitivity analyses:
Known limitations:
Implementation owner and acceptance criteria:
Stop conditions:
```

The specification does not authorize fitting. Route it to one verified
implementation adapter only through a separate invocation and approval.

## Boundaries

- PCA, factor analysis, GPFA, dPCA, jPCA, and nonlinear embeddings answer
  different questions. One is not a universal upgrade over another.
- A pseudo-population may support selected mean-response questions but cannot
  recreate unobserved simultaneous trial-by-trial covariance.
- Trial-averaged and single-trial analyses have different estimands and noise
  structures.
- Centering, scaling, soft normalization, rate transforms, smoothing, and
  binning change the population geometry. None is universally correct.
- Simultaneous shared-variability models require data and observation
  assumptions that support the covariance being estimated.
- Dimensionality is not established by a universal explained-variance cutoff.
  Use a prespecified held-out, predictive, reconstruction, stability, or
  inferential criterion appropriate to the question.
- dPCA components are model-dependent demixed summaries, not pure neural
  processes.
- Rotational or dynamical structure depends on alignment, time window,
  preprocessing, model constraints, and the selected null.
- Cross-session alignment can impose similarity. Preserve unmatched and
  unaligned sensitivity results.
- Nonlinear embeddings are exploratory visualizations unless a separately
  validated inferential method supports the exact claim. Visible clusters are
  not confirmed neural groups.
- Low-dimensional structure does not by itself establish a neural manifold,
  attractor, mechanism, or causal computation.
- Successful fitting does not establish biological validity or a scientific
  conclusion.

## Population analysis design and validation

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **Labeled population-method route cards.** Compare only population methods that answer the fixed estimand and are supported by the recording design. This separates variance, covariance, trajectory, demixing, dynamics, and visualization. This requires detailed recording and trial structure. This does not fit a latent model.
- **Neural Population Decision Record.** Show simultaneity, preprocessing, dimension, validation, stability, and claim audits. This makes hidden geometry and sampling assumptions reviewable. Genuine model ambiguity remains. A prose audit cannot inspect fitted residuals.
- **Verified Neural Population Method Specification.** Integrate only user-selected fields into the method specification. This preserves scientific ownership and method-software separation. This defers fitting. This cannot verify dimensionality or stability.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Executed population-analysis bundle.** Fit the selected models and run approved recovery, null, and stability checks. This tests the actual model and recording. This introduces outcome contact, compute, and artifact risks. This belongs to a separately approved adapter.
- **Extended robustness protocol.** Add held-out recovery, matched nulls, and unaligned sensitivity analyses. This tests selected model and alignment dependence. This adds models, compute, and multiplicity. Robustness does not prove mechanism.
- **Route cards plus recovery matrix.** Add prespecified synthetic recovery, dimension, and alignment scenarios. This reveals selected identifiability and alignment failures. This adds simulation assumptions and compute. Synthetic recovery does not establish biological meaning.

## Checks

- **Positive:** simultaneous multi-unit recordings with a fixed single-trial
  trajectory estimand produce applicable PCA, FA, or GPFA route cards, not a
  fitted latent space.
- **Negative:** `plot a neural manifold` does not trigger this skill.
- **Pseudo-population:** sequential units cannot support an unqualified
  trial-by-trial shared-covariance claim.
- **Trials:** condition-averaged data cannot silently become a single-trial
  GPFA analysis.
- **Dimensions:** `keep 90 percent variance` is treated as a candidate
  descriptive rule, not a universal dimension criterion.
- **Demixing:** missing factorial cells block a confirmatory dPCA
  interpretation unless a valid revised design is approved.
- **Visualization:** a UMAP or t-SNE cluster is not promoted to a biological
  population state.
- **Handoff:** predictive questions return to
  [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md); general method questions return to
  [cogsci-statistics](../cogsci-statistics/SKILL.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Churchland et al. (2012). https://doi.org/10.1038/nature11129
- Cunningham & Yu. (2014). https://doi.org/10.1038/nn.3776
- Kobak et al. (2016). https://doi.org/10.7554/eLife.10989
- Yu et al. (2009). https://doi.org/10.1152/jn.90941.2008
