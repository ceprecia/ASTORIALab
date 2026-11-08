---
name: neuroimaging-power-guide
description: >-
  Builds a prospective MRI neuroimaging Power Inputs Specification for one
  approved estimand, design, analysis, and inference family without calculating
  or selecting sample size. Use when the request, or a part coordinator, hands over
  an explicitly matching task. It maps the detection event, spatial or
  multiplicity procedure, effect and variance evidence, measurement reliability,
  first-level and group-level assumptions, data loss, and sensitivity scenarios,
  then compares applicable calculation families through two approval gates. It
  does not choose an ROI, whole-brain strategy, effect basis, threshold,
  correction, power target, method, or final N; calculate power; install tools;
  inspect outcome data; search; save; or start another capability without
  separate approval. Triggers: power inputs for my imaging study, neuroimaging
  power specification.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: power
  modality: multimodal
  dependencies: ""
  requires: ""
  gates: choosing the sample size
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Neuroimaging Power Guide

Specify MRI neuroimaging power inputs without turning inherited sample-size rules into scientific decisions.

## Purpose

`neuroimaging-power-guide` is the Part 3 canonical owner for prospective MRI neuroimaging power-method comparison and input specification for one approved design-analysis target.

It owns:

- translating an approved MRI estimand and analysis into an explicit success or detection event;
- mapping ROI, voxel, vertex, edge, network, map, predictive, or other approved inference units;
- exposing first-level, group-level, spatial, multiplicity, reliability, measurement-time, site, and pipeline assumptions that affect operating characteristics;
- comparing only calculation families that can represent the approved estimand and inference procedure;
- evaluating effect and variance evidence for applicability, selection bias, transportability, and uncertainty;
- producing a selection-bound Neuroimaging Power Inputs Specification and calculator handoff packet.

The user owns the research question, hypothesis, prediction, imaging modality, outcome, estimand, ROI or search space, contrast, model, design, acquisition, preprocessing, denoising, censoring, site strategy, inference method, error rule, threshold, effect basis, target operating characteristic, resource bound, final sample size, interpretation, and scientific claims.

[experimental-design](../../skills/experimental-design/SKILL.md) owns the general design. [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) owns approved task-fMRI timing. [statistical-power](../../skills/statistical-power/SKILL.md) owns general quantitative calculations that do not require a neuroimaging-specific spatial or pipeline model. [neuroimaging-sample-size-calculator](../neuroimaging-sample-size-calculator/SKILL.md) owns numerical execution of an approved neuroimaging-specific specification. Part 4 owns observed-data analysis.

This guide compares and specifies inputs. It does not calculate power or sample size.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `calculate my fMRI sample size`;
- `power this behavioral outcome`;
- `analyze these images`;
- `choose my ROI`;
- `should I switch to ROI analysis because it is cheaper`;
- broad phrases such as `MRI`, `fMRI`, `power`, `sample size`, or `neuroimaging`.

One run covers one primary MRI-derived estimand, one approved design-analysis specification, one inferential family, and one prospective decision.

Several sensitivity scenarios may remain together only when they vary uncertain inputs within that same specification. Separate materially different estimands, ROIs or search spaces, models, correction procedures, detection events, modalities, or confirmatory families.

This skill covers task fMRI, resting-state fMRI, structural MRI, diffusion MRI, or another MRI-derived measure only to the extent that the supplied evidence supports the exact calculation family. It does not transfer task-fMRI assumptions to other modalities.

EEG, MEG, PET, optical imaging, and invasive electrophysiology require their own modality evidence and owner. Do not treat them as interchangeable with MRI because the external candidate grouped them together.

## Inputs

Gather:

- The user's exact question, hypothesis, prediction, primary imaging estimand, and prospective decision;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) Design Specification;
- approved task, timing, acquisition, preprocessing, and planned-analysis specifications when applicable;
- modality, sequence or measure, population, site structure, scanner or hardware family, sessions, runs, and measurement duration;
- participant, image, run, trial, frame, edge, voxel, vertex, ROI, network, or other sampling and inference units;
- primary contrast, test, model, nuisance structure, covariance assumptions, and generalization target;
- ROI definition or search space and evidence that it is independent of the outcome data used to estimate the effect;
- multiplicity or spatial-inference procedure, every threshold, and the exact family to which error control applies;
- a plain-language success or detection event;
- candidate effect, variance, prevalence, reliability, or prediction-performance evidence with exact provenance;
- candidate participant, run, trial, scan-time, site, or resource bounds;
- planned QC, motion, censoring, missingness, technical-failure, attrition, and analyzability rules;
- target power, precision, reliability, predictive performance, or other operating characteristic only if the user has selected it;
- outcome visibility, confirmatory status, preregistration, deviations, supplied evidence, desired output, and stop point.

Mark an essential missing item `unknown`. Do not fill it from the candidate's lookup tables or sample-size benchmarks.

## Distinguish the planning target

Do not call every planning problem power.

Classify the approved target as one of:

1. **Hypothesis-test operating characteristic**
   - Probability of the exact prespecified detection event under a stated alternative.

2. **Estimation precision**
   - Expected interval width, map uncertainty, or another selected precision criterion.

3. **Measurement reliability**
   - Stability or dependability of the exact derived measure for the intended use.

4. **Prediction performance**
   - Out-of-sample performance under a prespecified validation and sampling design.

5. **Replicability or stability**
   - A prespecified agreement, sign, rank, feature, or map-stability event across samples.

6. **Resource-constrained sensitivity**
   - What effects or performance levels remain detectable under fixed participant and measurement resources.

If the target is not yet selected, return it to the user. A significance-test power calculation cannot substitute for reliability, precision, prediction, or replicability.

## Steps

### 1. Build the Neuroimaging Power Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and Part 3 status |
| Prospective decision | What this planning work should inform |
| Question and prediction | user-supplied wording, unchanged |
| Primary estimand | Exact MRI-derived target and scale |
| Design | Approved units, allocation, dependence, and timing |
| Analysis | Proposed first-level and group-level model as applicable |
| Inference family | ROI, search-space, map, predictive, or other approved family |
| Planning target | Power, precision, reliability, prediction, replicability, or sensitivity |
| Evidence boundary | Supplied material that may be inspected |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Fixed decisions | user-owned choices that must not change |
| Missing inputs | User-owned or technical inputs still unknown |
| Excluded work | Scientific choice, calculation, search, installation, observed-data analysis, saving, and unapproved handoffs |
| Stop point | Exact output or decision that ends the run |

If the primary estimand, model, inference family, or planning target is unresolved, stop and return that decision to the user or prepare a separately approved handoff.

### 2. Gate 1: approve the comparison frame

Before building method options, show the brief and ask the user to approve:

- the one estimand and prospective decision;
- the design-analysis and inference boundary;
- the evidence that may be inspected;
- which uncertain inputs should become sensitivity scenarios;
- the option-comparison dimensions;
- any proposed bounded [research-literacy](../../skills/research-literacy/SKILL.md) or [paper-search](../../skills/paper-search/SKILL.md) handoff.

Gate 1 authorizes only the displayed comparison and supplied-evidence review.

It does not authorize:

- choosing an ROI, search space, model, correction, threshold, effect basis, target, method, sample size, or scientific conclusion;
- reading outcome data that are outside the approved evidence boundary;
- a network search, software installation, calculation, simulation, upload, save, or another capability.

Do not infer approval from silence.

### 3. Build the Inference and Detection Map

Map:

| Element | Required question |
|---|---|
| Estimand | What exact quantity is targeted? |
| Analysis unit | What independent or dependent units enter each model level? |
| Inference unit | ROI mean, voxel, vertex, edge, network, map, prediction, or other unit? |
| Search family | What locations, contrasts, models, or outcomes belong to the family? |
| Error procedure | How is the selected error criterion controlled? |
| Detection event | What exact simulated or analytic event counts as success? |
| Direction and sidedness | What did the user select and why? |
| Model levels | Which first-level, subject-level, group-level, site-level, or validation levels matter? |
| Generalization | To which participants, stimuli, sites, scanners, sessions, or populations? |
| Failure event | What fit, QC, missingness, or computational failure does not count as a valid test? |

Never define success after seeing the candidate results. For spatial analyses, distinguish at least:

- detecting any signal somewhere in the search space;
- detecting a signal in an independent target region;
- detecting a particular voxel, vertex, edge, or cluster;
- recovering a map or spatial pattern to a selected criterion;
- controlling false positives under the exact null.

These are not equivalent power metrics.

### 4. Build the Evidence and Transportability Register

For every candidate input, record:

| Field | Required content |
|---|---|
| Parameter | Effect, variance, covariance, prevalence, smoothness, reliability, data loss, performance, or other input |
| Value or range | Exact value, interval, distribution, or `unknown` |
| Metric and scale | What the number means and where it was measured |
| Source | Pilot, independent dataset, literature, meta-analysis, smallest effect of interest, or explicit scenario |
| Independence | Whether selection and estimation used the same data |
| Design match | Population, task, contrast, acquisition, preprocessing, model, and inference match |
| Precision | Sampling uncertainty or evidence gap |
| Selection risk | Thresholding, peak or ROI selection, winner's curse, publication filtering, or researcher flexibility |
| Transportability | Reasons the input may differ in the planned study |
| Status | Directly usable, sensitivity-only, needs bounded audit, incompatible, or unknown |
| Decision owner | The user or technical verification |

Rules:

- Prefer a scientifically meaningful target or sensitivity range over one selected published point estimate.
- Do not extract an effect from a peak, significant cluster, or ROI selected on the same data and treat it as unbiased.
- Do not apply a universal percentage reduction to a pilot or published effect.
- Do not reuse pilot observations in a final analysis when the sample-size rule makes inclusion outcome-dependent unless the prespecified design and inferential method validly support that reuse.
- Do not convert a thresholded statistic map into an effect-size map without the required model, degrees of freedom, variance, scaling, and selection information.
- Do not treat a coordinate-based meta-analytic association or term map as a direct effect-size estimate.
- Preserve uncertainty about future acquisition, preprocessing, denoising, motion, site, and population differences.

### 5. Build the Measurement and Data-Loss Map

Separate:

- analyzed participants from recruited participants;
- usable sessions, runs, frames, images, trials, or connections from collected amounts;
- participant-level exclusion from within-participant censoring;
- missing at random assumptions from informative data loss;
- measure reliability for group-average contrasts from reliability for individual differences or prediction;
- scan duration and trial count from participant count;
- site and scanner variability from biological variability.

Use local QC history only when the user supplies or separately approves access to it. Otherwise compare labeled data-loss and reliability scenarios rather than inserting a conventional percentage.

### 6. Compare applicable calculation families

Offer only methods that could represent the approved target:

| Family | Appropriate only when | Required evidence | Main limitation |
|---|---|---|---|
| Summary-endpoint analytic | One prespecified scalar endpoint and ordinary test adequately represent the confirmatory target | Approved effect, variance, dependence, test, multiplicity, and units | Does not represent image-wide spatial detection |
| Model-based fMRI group calculation | The future task, first-level design, contrast, group test, and ROI summary match an independently estimated pilot basis | Compatible pilot mean and variance terms plus exact design and model | Transportability and selection bias can dominate |
| Full pipeline simulation | The data-generating process, spatial or network structure, analysis, correction, and detection event can be encoded and verified | Effect and noise model, mask, pipeline, thresholds, failures, and resource plan | Model misspecification and computation cost |
| Empirical resampling or subsampling | A sufficiently relevant independent dataset supports the intended resampling target | Access, sampling frame, independence, pipeline, and validation plan | Estimates performance within the source population and pipeline |
| Precision or sensitivity justification | No defensible point alternative exists or resources are fixed | Meaningful precision target or plausible input grid | Does not yield one guaranteed required N |
| Specialist or unresolved route | The proposed method cannot yet be validated | Exact gap and required owner | No numerical result until resolved |

For each option, report:

- inferential target and detection event;
- inputs and their provenance;
- assumptions;
- what it represents and omits;
- sensitivity dimensions;
- verification plan;
- implementation and data requirements;
- status: **Credible candidate**, **Conditional**, **Blocked**, or **Rejected as mismatched**.

Do not rank methods by convenience, available package, lower N, or apparent power.

### 7. Build the Neuroimaging Power Threat Register

At minimum inspect:

- mismatch between the planning estimand and final analysis;
- circular ROI or feature selection;
- thresholded or winner-selected effect evidence;
- model, contrast, HRF, denoising, censoring, or covariance mismatch;
- spatial smoothness, mask, resolution, site, scanner, and preprocessing mismatch;
- multiplicity family or correction mismatch;
- undefined or overly permissive detection event;
- low measurement reliability for the intended use;
- participant-only planning that ignores runs, trials, scan time, or site structure;
- fixed data-loss percentages without local basis;
- unstable pilot variance or effect estimates;
- power optimized by changing the scientific question, ROI, threshold, or correction;
- Monte Carlo and numerical uncertainty;
- optimistic failure handling;
- post hoc use after outcomes are inspected;
- treating a brain-wide association result as a universal sample-size rule for all neuroimaging.

For each threat, show evidence, consequence, mitigation options, residual uncertainty, and decision owner.

### 8. Present response options

Offer only applicable choices:

- select one calculation family and its sensitivity scenarios;
- combine compatible methods as cross-checks;
- return an input, detection event, or inference decision to the user;
- gather independent pilot or reliability evidence;
- request a bounded evidence audit or search;
- prepare a calculator or general-power handoff;
- defer because no defensible calculation is currently possible.

Do not recommend a final N or change the analysis to obtain a smaller N.

### 9. Gate 2: The user selects the specification

Ask the user to:

- select the planning target and detection event;
- select the calculation family or cross-check;
- select effect, variance, reliability, data-loss, and sensitivity inputs;
- confirm the analysis, correction, thresholds, and failure handling;
- preserve unresolved assumptions that must remain visible;
- select any handoff packet.

Gate 2 authorizes only the selected Neuroimaging Power Inputs Specification and selected handoff packets.

It does not authorize numerical calculation, simulation, installation, data upload, outcome inspection, design change, search, saving, or a final sample-size decision.

Do not infer selection from silence.

### 10. Produce and verify the Neuroimaging Power Inputs Specification

Include:

1. exact prospective decision and planning target;
2. user-supplied question, prediction, and primary estimand;
3. approved design, acquisition, timing, preprocessing, model, and inference family;
4. exact success and failure events;
5. every selected input, unit, range, source, and translation;
6. independence, selection, and transportability status;
7. selected calculation family and rejected alternatives;
8. sensitivity grid;
9. QC, data-loss, reliability, site, and measurement-time assumptions;
10. required implementation, version, data, and computational resources;
11. null, alternative, numerical, and independent verification plan;
12. known limitations and unresolved gaps;
13. The user's remaining decisions;
14. selected handoff packets;
15. provenance separating user input, source evidence, AI comparison, and the user's selections.

Verify:

- units and model levels are explicit;
- the detection event matches the planned inference;
- effect evidence is not circular or silently generalized;
- spatial and multiplicity assumptions are not omitted;
- reliability and data loss match the intended use;
- no universal benchmark or candidate default became an input;
- no calculation, search, installation, save, or observed-data analysis occurred.

## Outputs

Always distinguish:

- **Documented input**: directly supplied or verified;
- **user-selected assumption**: a scientific planning choice;
- **AI-generated comparison**: a labeled option or threat;
- **Unknown**: not currently supported;
- **Blocked**: required evidence or implementation is missing.

Return:

1. Neuroimaging Power Brief;
2. Inference and Detection Map;
3. Evidence and Transportability Register;
4. Measurement and Data-Loss Map;
5. Calculation Family Option Matrix;
6. Neuroimaging Power Threat Register;
7. Gate decisions;
8. Neuroimaging Power Inputs Specification;
9. verification and limitation record;
10. selected handoff packets.

Use ordinal statuses, not numeric confidence scores or composite rankings.

Return findings in the current task's requested form or under the recipient's existing reporting policy. Saving remains subject to the approval and destination rules below.

Before saving, searching, uploading data, executing a calculator, installing software, or starting another capability:

1. show the exact proposed action;
2. show the source and destination;
3. explain what will change or leave the machine;
4. ask for separate approval;
5. verify afterward.

For an authorized save, use the verified destination selected for the task. If none is selected, use the workflow's established project-owned scientific destination where it applies. For other supporting content, use a destination established by the recipient's placement policy, including Resources when that policy selects it. Skill and system work stays in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved. Add a verified link at the selected location only when the authorized scope includes that edit.

## Boundaries

- **Primary estimand unresolved**: Return it to the user; do not choose one that is easiest to power.
- **ROI selected from the same pilot effect**: Mark circular and require an independent definition or valid selection-adjusted method.
- **Only a significant peak is reported**: Do not treat the peak effect as an unbiased planning input.
- **Thresholded map only**: Record the information loss and do not invent subthreshold effects.
- **No pilot or comparable evidence**: Offer meaningful-effect, precision, resource-constrained sensitivity, or blocked routes.
- **Small pilot**: Preserve uncertainty; do not apply a fixed deflation percentage.
- **Pilot participants may enter the final study**: Require a valid prespecified reuse rule or keep the samples separate.
- **Marek et al. invoked**: Apply its findings to matching brain-wide association targets, not task activation, interventions, lesions, or every MRI study.
- **Reliability unknown**: Show it as an unresolved input and sensitivity dimension, especially for individual differences.
- **Multiple ROIs or contrasts**: Require the exact confirmatory family and correction; one ROI shortcut does not apply silently.
- **Whole-brain correction unspecified**: The calculation family is not ready.
- **Cluster-based inference proposed**: Require the exact cluster-forming rule, null procedure, smoothness assumptions, detection event, and software behavior.
- **Prediction model**: Require the complete validation scheme, leakage controls, sampling unit, performance metric, and null comparator.
- **Fixed budget**: Produce sensitivity or precision scenarios; do not promise adequate power.
- **Completed study**: Do not compute observed post hoc power from the observed effect.
- **Outcomes partly seen**: Label affected choices post hoc or exploratory and preserve deviations.
- **EEG or MEG request**: Route to the appropriate modality owner or disclose the gap.
- **Package unavailable**: Preserve the specification and stop; do not install or substitute an unverified implementation.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) when the design, units, allocation, clustering, repeated structure, or site structure is unresolved.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) when task-fMRI timing, event mapping, or design-matrix efficiency is unresolved.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) only for a separable cognitive or behavioral outcome.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) when the approved target is a general scalar-endpoint calculation without neuroimaging-specific spatial or pipeline assumptions.
- Use [neuroimaging-sample-size-calculator](../neuroimaging-sample-size-calculator/SKILL.md) when an approved specification requires model-based or full-pipeline neuroimaging calculation.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) to audit one explicit methodological or effect-basis claim.
- Use [paper-search](../../skills/paper-search/SKILL.md) only through a separately approved bounded search brief.
- Use [research-critique](../../skills/research-critique/SKILL.md) for critique of an existing study or protocol.
- Route observed-image analysis to Part 4.

Each destination begins its own workflow and gates. Neuroimaging Power Guide approval does not authorize another capability.

This skill does not choose or change the scientific design, modality, ROI, search space, model, preprocessing, correction, threshold, effect, target, method, or final sample size; calculate power; analyze observed data; install software; search; save; or make a scientific conclusion for the user.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Elliott, M. L., Knodt, A. R., Ireland, D., et al. (2020). What is the test-retest reliability of common task-functional MRI measures? *Psychological Science, 31*(7). https://doi.org/10.1177/0956797620916786
- Marek, S., Tervo-Clemmens, B., Calabro, F. J., et al. (2022). Reproducible brain-wide association studies require thousands of individuals. *Nature, 603*. https://doi.org/10.1038/s41586-022-04492-9
- Mumford, J. A. (2012). A power calculation guide for fMRI studies. *Social Cognitive and Affective Neuroscience, 7*(6). https://doi.org/10.1093/scan/nss059
- Mumford, J. A., & Nichols, T. E. (2008). Power calculation for group fMRI studies accounting for arbitrary design and temporal autocorrelation. *NeuroImage, 39*(1). https://doi.org/10.1016/j.neuroimage.2007.07.061
- Turner, B. O., Paul, E. J., Miller, M. B., & Barbey, A. K. (2018). Small sample sizes reduce the replicability of task-based fMRI studies. *Communications Biology, 1*, Article 62. https://doi.org/10.1038/s42003-018-0073-z
