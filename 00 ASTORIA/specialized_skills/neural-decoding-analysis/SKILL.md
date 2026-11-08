---
name: neural-decoding-analysis
description: >-
  Compares neural decoding, encoding, representational-similarity, searchlight,
  and temporal-generalization method routes for one user-specified predictive or
  representational estimand. Use when the request, or a part coordinator, hands over
  that exact method-guidance handoff. It exposes sampling, dependence, leakage,
  feature, split, tuning, metric, null, exchangeability, confound, multiplicity,
  and interpretation limits, then produces a selection-bound Neural Decoding
  Method Specification without fitting a model, selecting features or
  classifiers, accessing a sealed test set, or interpreting decodability as
  mechanism or causation. Triggers: decode conditions from my neural data,
  representational similarity or searchlight plan.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: multimodal
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Neural Decoding Analysis

Specify one bounded neural decoding or representational analysis while keeping
prediction, representation, localization, mechanism, and causation distinct.

## Purpose

`neural-decoding-analysis` owns:

- distinguishing predictive decoding, encoding, representational similarity,
  searchlight, and temporal-generalization estimands;
- defining sampling units, dependence groups, features, labels, train-test
  generalization, metrics, baselines, nulls, and exchangeability;
- comparing applicable validation and model-family routes without choosing an
  estimator automatically;
- auditing leakage, confounds, multiplicity, uncertainty, and claim
  boundaries;
- producing one user-selected Neural Decoding Method Specification.

The user owns the question, hypothesis, prediction, confirmatory status,
representation claim, target, features, sampling unit, split, generalization
target, estimator family, metric, baseline, null, error criterion,
interpretation, and claims.

[scikit-learn](../scikit-learn/SKILL.md) owns implementation of an already specified classical
machine-learning pipeline. [run-models](../run-models/SKILL.md) owns comparison of eligible
neuroimaging deep-model cards after the specification fixes the target,
inputs, validation, leakage, baseline, compute, and claim boundaries.
[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns upstream fMRI preprocessing
compatibility. A modality or software adapter owns execution only after the
decoding specification is approved.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `decode`, `MVPA`, `classifier`, `machine learning`,
`representation`, `RSA`, `searchlight`, `encoding model`, `EEG`, `fMRI`, or
another broad method or modality term.

Do not use this skill to:

- invent a representational hypothesis or target label;
- select a classifier, regularizer, feature set, searchlight radius, time
  window, metric, split, or threshold automatically;
- fit or tune a model, transform observed data, run a permutation, inspect a
  sealed test set, or create result maps;
- treat above-chance decoding as evidence of where, how, or why the brain
  represents information;
- treat a classifier's weight, feature importance, or searchlight peak as a
  direct neural code or causal mechanism.

## Inputs

Obtain or mark missing:

- approved question, prediction, estimand, claim boundary, and confirmatory or
  exploratory status;
- modality, acquisition, measurement limitations, preprocessing state, and
  required spatial, temporal, frequency, or population grain;
- participants, sessions, runs, blocks, trials, stimuli, conditions, time
  points, channels, sensors, sources, voxels, regions, or units;
- target or response definition, provenance, timing, class balance, continuous
  range, missingness, and potential proxies;
- feature source, selection, normalization, dimensionality, temporal window,
  ROI or searchlight independence, and outcome-contact history;
- dependence groups and the exact generalization claim across trials,
  exemplars, runs, sessions, participants, sites, modalities, or time;
- candidate train, validation, tuning, and sealed-test boundaries;
- candidate decoding, regression, encoding, RSA, searchlight, or temporal
  generalization route;
- estimator families only when scientifically in scope, plus hyperparameters
  and calibration requirements;
- primary metric, uncertainty unit, descriptive baseline, statistical null,
  permutation unit, exchangeability blocks, tails, and multiplicity family;
- nuisance and confound structure, balance, counterbalancing, motion,
  reaction-time, stimulus, run, site, and acquisition alternatives;
- sensitivity analyses, negative controls, computational limits, later
  implementation owner, and acceptance criteria.

If the estimand, target, sampling unit, dependence structure, split,
generalization target, metric, null, confound plan, multiplicity family, or
confirmatory status is unresolved, stop with **neural decoding intake
incomplete**.

## Steps

### 1. Build the Neural Decoding Intake Record

| Field | Record |
|---|---|
| user-owned target | Question, prediction, estimand, status, permitted claim |
| Measurement | Modality, acquisition, preprocessing, spatial and temporal grain |
| Observations | Participants, runs, trials, exemplars, time points, features |
| Target | Label or response, provenance, timing, balance, proxy risks |
| Generalization | What is held out and what population or context the score addresses |
| Dependence | Groups, repeats, blocks, sessions, sites, families |
| Pipeline | Feature construction, transformations, model, tuning, calibration |
| Evaluation | Metric, uncertainty unit, baseline, null, permutation, tails |
| Multiplicity | Models, ROIs, searchlights, times, frequencies, contrasts |
| Test boundary | No sealed-test or target-result contact during specification |
| Stop point | Method specification only |

Do not convert `can the brain decode this condition?` into an estimand.

### 2. Gate 1: approve the Decoding Estimand and Validation Contract

Show:

- the fixed predictive or representational estimand and permitted claim;
- observation, target, feature, dependence, split, and generalization map;
- the selected analysis route or eligible alternatives for an unresolved choice;
- leakage, confound, null, metric, uncertainty, multiplicity, and test-set
  risks;
- exact source lookups, excluded operations, and stop point.

Gate 1 authorizes only method comparison and read-only metadata or existing
pipeline inspection. It does not authorize observed-data transformation,
feature selection, model fitting, tuning, permutation, sealed-test access,
map creation, package changes, saving, or external writes.

### 3. Decoding choices for the approved estimand

Carry forward the selected method. Compare eligible routes only when the task leaves a material design choice open, or return a substantive problem with the chosen route to the decision owner.

Offer only routes that answer the approved estimand:

- **Cross-validated decoding or regression:** predicts a defined target under
  a prespecified held-out generalization boundary.
- **Encoding:** predicts neural responses from fixed stimulus or model
  features and evaluates generalization to held-out observations.
- **Representational similarity analysis:** compares neural
  representational dissimilarities with prespecified or explicitly
  exploratory model dissimilarities.
- **Searchlight:** local predictive or representational mapping when the
  spatial search family and localization limits are explicit.
- **Temporal decoding or generalization:** tests when information is
  predictive and whether a fitted decision function generalizes across
  prespecified times.

For every route state:

- exact estimand and held-out generalization claim;
- observation and uncertainty grains;
- feature, label, transformation, split, tuning, and test boundaries;
- metric, baseline, null, exchangeability, and multiplicity;
- confounds, negative controls, compute, benefit, tradeoff, and main
  limitation.

Do not recommend a route because a classifier is familiar or available.

### 4. Document split and leakage in the decision record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Estimand fit | Split and generalization | Leakage controls | Null and exchangeability | Multiplicity | Permitted claim | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- repeated trials, stimuli, participants, runs, families, or sites divided
  across folds in a way that violates the intended generalization;
- scaling, feature selection, imputation, nuisance removal, temporal
  filtering, alignment, or dimensionality reduction learned outside training
  folds;
- hyperparameter selection, model comparison, thresholding, or calibration
  performed on the sealed test set;
- chance level substituted for a valid statistical null or vice versa;
- class imbalance, unequal trial counts, temporal adjacency, run structure,
  and acquisition artifacts;
- stimulus, response, reaction-time, motion, difficulty, site, or session
  confounds that can predict the target;
- uncertainty calculated over a grain that does not support the population
  claim;
- entrywise RSA tests or permutations that ignore dependence among
  dissimilarities;
- crossvalidated distances used without independent partitions and a
  defensible noise-normalization model;
- time, frequency, sensor, voxel, searchlight, ROI, model-RDM, estimator, and
  hyperparameter multiplicity;
- classifier weights, searchlight peaks, temporal-generalization patterns, or
  model-RDM agreement overinterpreted as localization, mechanism, or
  causation.

Stop on leakage, an undefined holdout, invalid exchangeability, target
proxies that answer a different question, circular feature or ROI selection,
an undefined multiplicity family, or test-set contact that invalidates the
claimed confirmation.

### 5. Gate 2: The user selects one exact decoding specification

Ask the user to select, revise, or reject a route and approve:

- target, features, observation grain, dependence groups, and generalization
  target;
- preprocessing, within-fold transformations, feature selection, estimator,
  tuning, calibration, and sealed test;
- primary metric, uncertainty grain, baseline, statistical null,
  exchangeability blocks, tails, and multiplicity;
- confound controls, negative controls, sensitivity analyses, claim boundary,
  implementation owner, and stop point.

Do not infer selection from silence. If outcome or test-set contact changed a
confirmatory feature, model, split, ROI, time window, metric, or null, record
the deviation and label affected work exploratory.

### 6. Return the Neural Decoding Method Specification

Return:

```text
Neural Decoding Method Specification
Approved question, prediction, and estimand:
Confirmatory or exploratory status:
Permitted and prohibited claims:
Modality, preprocessing, and measurement limits:
Observation, participant, run, trial, feature, and time grains:
Target definition, provenance, timing, balance, and missingness:
Feature definition and independent selection:
Dependence groups and generalization target:
Train, validation, nested-tuning, and sealed-test boundaries:
Within-fold transformations:
Selected method and estimator family:
Primary metric, uncertainty unit, and descriptive baseline:
Statistical null, exchangeability, permutations, and tails:
Confound controls and negative controls:
Multiplicity family and error criterion:
Sensitivity and robustness checks:
Known limitations:
Implementation owner and acceptance criteria:
Stop conditions:
```

The specification does not authorize fitting. Route it to one verified
implementation adapter only through a separate invocation and approval.

## Boundaries

- Decodability establishes predictive information under the specified data,
  model, and generalization boundary. It does not establish where that
  information originated, how the brain uses it, or a causal mechanism.
- The split must match the claim. Trial-level cross-validation cannot support
  participant-, session-, site-, or exemplar-level generalization.
- Every transformation whose parameters are learned from the evaluation
  dataset belongs inside the training fold. A frozen externally pretrained
  transform requires independent provenance and no target-dataset fitting.
  Tuning requires an inner validation loop when an outer estimate is claimed.
- When a separate sealed test set is selected, contact it once under the
  approved plan. Reuse converts it into development data. Nested
  crossvalidation may be the complete evaluation without a separate holdout.
- Metric choice follows the estimand and imbalance structure. Accuracy is not
  universal, and chance level is not a substitute for a valid null.
- Permutation labels or residuals only under a justified exchangeability
  scheme and preserve the relevant dependence.
- RSA dissimilarities are dependent. Model-RDM selection, distance choice,
  noise ceiling, crossvalidation, and inference unit remain explicit.
- Crossvalidated distances require independent partitions and compatible
  noise estimation.
- Searchlight, time, frequency, sensor, ROI, model, and estimator searches
  belong to the multiplicity family.
- Classifier weights and feature importance are model-dependent and are not
  direct neural-importance maps.
- Above-chance prediction does not establish a uniquely localized
  representation, mechanism, or causation.
- Nonsignificant decoding does not establish absence of information.
- Successful execution does not establish construct validity or a scientific
  conclusion.

## Decoding design and validation

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **Labeled neural-analysis route cards.** Compare only decoding, encoding, RSA, searchlight, or temporal routes that answer the fixed estimand. This separates different predictive and representational questions. This requires a precise generalization target. This does not fit a model.
- **Neural Decoding Decision Record.** Show the split map, leakage audit, null, multiplicity, and claim limits. This makes hidden validation choices reviewable. Genuine estimator uncertainty remains. A prose audit cannot test implementation leakage.
- **Verified Neural Decoding Method Specification.** Integrate only user-selected fields into the method specification. This preserves scientific ownership and method-software separation. This defers fitting. This cannot verify actual leakage or performance.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Executed decoding bundle.** Fit, tune, evaluate, and run approved nulls under the sealed pipeline. This tests the actual model and data. This introduces outcome contact, compute, and artifact risks. This belongs to a separately approved adapter.
- **Extended robustness protocol.** Add blinded negative-control and cross-generalization analyses. This tests selected confounds and boundary failures. This adds models, compute, and multiplicity. Robustness does not prove mechanism.
- **Route cards plus recovery matrix.** Add prespecified synthetic leakage and confound-recovery scenarios. This reveals selected pipeline failures. This adds simulation assumptions and compute. Synthetic recovery does not validate neural meaning.

## Checks

- **Positive:** a fixed cross-participant EEG generalization question produces
  route cards with participant-grouped splits and within-fold transforms, not
  classifier scores.
- **Negative:** `train a classifier` does not trigger this skill.
- **Leakage:** feature selection performed before cross-validation stops the
  confirmatory route.
- **Test set:** repeated inspection of the holdout is recorded as development
  contact and invalidates a one-shot confirmatory claim.
- **RSA:** an entrywise permutation that ignores shared conditions is rejected.
- **Confound:** target labels perfectly track scanner site, run, or stimulus
  identity and cannot support the intended neural claim without redesign.
- **Interpretation:** above-chance decoding is not promoted to evidence of a
  mechanism or uniquely localized representation.
- **Handoff:** approved classical implementation may route to
  [scikit-learn](../scikit-learn/SKILL.md); an approved neuroimaging deep-model family comparison may
  route to [run-models](../run-models/SKILL.md); fMRI preprocessing returns to
  [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- King & Dehaene (2014). https://doi.org/10.1016/j.tics.2014.01.002
- Kriegeskorte et al. (2008). https://doi.org/10.3389/neuro.06.004.2008
- Naselaris et al. (2011). https://doi.org/10.1016/j.neuroimage.2010.07.073
- Nili et al. (2014). https://doi.org/10.1371/journal.pcbi.1003553
- Varoquaux et al. (2017). https://doi.org/10.1016/j.neuroimage.2016.10.038
- Walther et al. (2016). https://doi.org/10.1016/j.neuroimage.2015.12.012
