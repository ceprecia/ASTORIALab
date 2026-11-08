---
name: neuroimaging-sample-size-calculator
description: >-
  Executes one approved prospective MRI neuroimaging power, sample-size, MDE,
  sensitivity, precision, or related operating-characteristic calculation when
  the exact imaging model, spatial or multiplicity procedure, pipeline, and
  detection event materially determine the result. Use when the request, or a
  part coordinator, hands over a complete matching specification. It preflights a
  validated existing implementation, computes only user-selected scenarios after
  two approval gates, exposes numerical and Monte Carlo uncertainty, null
  calibration, failures, and sensitivity, and returns a reproducible Calculation
  Record. It does not choose scientific inputs, methods, software, thresholds,
  target power, or final N; install tools; substitute benchmark tables; analyze
  study outcomes; upload data; search; save; or start another capability without
  separate approval. Triggers: calculate my imaging sample size, MRI sample size
  calculation.
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

# Neuroimaging Sample Size Calculator

Execute an approved MRI neuroimaging calculation without letting software or inherited defaults choose the study.

## Purpose

`neuroimaging-sample-size-calculator` is the Part 3 canonical implementation owner for prospective MRI neuroimaging operating-characteristic calculations whose result depends materially on the exact imaging model, spatial or multiplicity procedure, pipeline, or detection event.

It owns:

- validating that an approved [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) specification is calculation-ready;
- comparing technically valid implementations only when the scientific calculation family is already approved;
- preflighting the exact existing runtime, tool, version, inputs, code or command, resource bound, and verification route;
- executing only user-selected candidate sample-size, effect, variance, reliability, acquisition, data-loss, or other sensitivity scenarios;
- estimating and reporting numerical or Monte Carlo uncertainty, null behavior, failures, and boundary stability;
- producing a reproducible Neuroimaging Calculation Record.

The user owns the question, hypothesis, prediction, modality, outcome, estimand, design, acquisition, preprocessing, model, ROI or search space, inference and multiplicity procedure, threshold, detection event, effect and noise basis, reliability assumptions, target operating characteristic, scenario grid, software selection when alternatives remain, resource ceiling, final sample size, interpretation, and scientific claims.

[neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) owns method comparison and MRI-specific input specification. [statistical-power](../../skills/statistical-power/SKILL.md) owns general scalar-endpoint calculations that do not need an imaging-specific spatial or pipeline implementation. [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) owns task-fMRI timing and schedule validation. Part 4 owns observed-data analysis.

This skill calculates from an approved specification. It does not repair an unresolved scientific specification by making choices.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route a complete, explicitly matching packet from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `how many subjects do I need`;
- `power my fMRI study`;
- `choose my correction`;
- `is this published result underpowered`;
- `analyze these images`;
- broad phrases such as `sample size`, `power`, `MRI`, `fMRI`, or `simulation`.

One run covers one approved primary MRI-derived estimand, one design-analysis specification, one inference family and detection event, one calculation family, and one bounded scenario grid.

Separate materially different estimands, models, correction procedures, detection events, modalities, or confirmatory families. A common sample-size axis does not make incompatible analyses one calculation.

Use this calculator only when at least one of these is true:

- the calculation uses a model tied to a specific fMRI first-level and group-level design;
- image, surface, edge, network, or map structure enters the calculation;
- spatial or multiple-comparison inference changes the detection event;
- the planned neuroimaging pipeline must be represented in simulation or resampling;
- MRI-specific measurement duration, reliability, censoring, site, or acquisition structure enters the approved model.

If one prespecified scalar endpoint can be calculated with an ordinary validated statistical model and no imaging-specific pipeline representation, route to [statistical-power](../../skills/statistical-power/SKILL.md).

## Inputs

Require an approved Neuroimaging Power Inputs Specification or equivalent packet containing:

- exact prospective decision and planning target;
- user-supplied question, prediction, and primary estimand;
- approved design, acquisition, timing, preprocessing, model, inference family, and confirmatory multiplicity family;
- exact success, null, and failure events;
- selected effect, variance, covariance, prevalence, reliability, smoothness, data-loss, and other inputs with units and provenance;
- independence, selection-bias, applicability, and transportability status of each empirical input;
- selected calculation family and any required cross-check;
- selected candidate sample sizes or search bounds;
- selected sensitivity grid;
- target operating characteristic and error rule;
- planned QC and fit-failure handling;
- implementation and data requirements;
- protected-data and external-action boundaries;
- desired output and stop point.

Mark the packet **Blocked** if an essential scientific input is missing. Do not substitute a candidate benchmark, conventional target, or package default.

## Readiness statuses

Assign exactly one:

- **Ready for validated execution**
- **Ready after technical clarification**
- **Blocked by a user-owned scientific input**
- **Blocked by evidence or transportability**
- **Blocked by implementation or resource availability**
- **Mismatched to this calculator**

Do not convert a blocked scenario into a runnable one by simplifying the scientific question, changing the ROI, loosening correction, or selecting a more convenient tool.

## Steps

### 1. Build the Calculation Intake Record

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and Part 3 status |
| Input owner | Approved [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) packet or equivalent |
| Planning target | Power, sample size, MDE, sensitivity, precision, reliability, prediction, replicability, or other approved characteristic |
| Estimand and detection event | Exact target and event counted as success |
| Design and analysis | Approved model levels, units, pipeline, inference, and correction |
| Selected inputs | Values, ranges, units, sources, and decision owner |
| Scenario grid | Exact bounded combinations requested |
| Implementation boundary | Existing local tool, project environment, or supplied outputs that may be used |
| Data boundary | Files and fields that may be read; protected material excluded |
| External actions | Network, upload, install, save, or service use, normally none |
| Resource ceiling | Time, memory, storage, repetitions, or cost bound |
| Verification requirement | Null, independent, limiting-case, or second-implementation check |
| Stop point | Exact calculation record that ends the run |

If the approved packet and proposed calculation differ, stop and return the discrepancy to the user or to [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md).

### 2. Gate 1: approve the calculation boundary

Before implementation inspection or computation, show the intake record and ask the user to approve:

- the exact specification and scenario boundary;
- files and fields that may be inspected;
- permitted read-only runtime and version checks;
- the implementation families that may be compared;
- resource and privacy limits;
- the required verification route.

Gate 1 authorizes only the displayed readiness and implementation preflight.

It does not authorize:

- choosing or changing a scientific input, model, threshold, correction, target, scenario, software, or final N;
- installing a package, using a network service, uploading data, running the calculation, saving, analyzing observed outcomes, or starting another capability.

Do not infer approval from silence.

### 3. Verify the input packet

Check:

- every unit, scale, and model level;
- analyzed versus recruited participants;
- subject, run, trial, frame, image, voxel, edge, ROI, site, or other counts;
- effect and noise inputs are compatible with the exact estimator;
- the ROI or feature basis is independent or its selection is validly represented;
- the error procedure and threshold match the intended confirmatory family;
- the detection event is computable and fixed;
- reliability and missingness assumptions match the intended use;
- the pipeline represents censoring, nuisance, covariance, site, and acquisition behavior where material;
- the scenario grid spans the approved uncertainty rather than only the favorable case;
- outcome-informed inputs are not mislabeled as prospective.

Return any scientific mismatch to the user. Correct only unambiguous transcription or unit errors after showing the correction.

### 4. Build the Implementation Preflight

For each technically credible implementation, show:

| Field | Required content |
|---|---|
| Method | Exact approved mathematical or simulation method |
| Implementation | Tool, package, script, service, or bounded in-chat implementation |
| Version and source | Exact version and authoritative documentation or methodological source |
| Runtime | Existing environment and verified availability |
| Inputs | Exact files, objects, formats, masks, maps, summaries, or parameters |
| Output semantics | Meaning and units of every result |
| Seeds | Seed values or deterministic policy for stochastic work |
| Repetitions | Selected count or adaptive precision rule |
| Resource estimate | Expected time, memory, storage, and output size |
| Failure behavior | What counts as invalid, failed, or censored execution |
| Null check | How nominal false-positive or error behavior will be assessed |
| Alternative check | How expected behavior under selected alternatives will be assessed |
| Numerical check | Independent implementation, benchmark, limiting case, or known identity |
| Privacy | Whether any data leave the approved local boundary |
| Status | Ready, conditional, blocked, or rejected |

Rules:

- Verify commands, parameters, APIs, defaults, and output meaning against the exact installed version and current authoritative documentation.
- A package's presence does not make its method appropriate.
- A repository example or pseudocode is not a validated implementation.
- Do not download, install, update, or activate software during preflight.
- Do not upload maps or participant data to a service without separate explicit approval.
- Stop when version behavior, parameterization, or output semantics cannot be verified.

### 5. Specify the computation and verification plan

For analytic or model-based calculations, define:

- formula or numerical inversion;
- parameterization and unit translation;
- integer rounding and allocation constraints;
- candidate boundaries;
- independent check and tolerances.

For simulations or resampling, define:

- aim;
- data-generating mechanism;
- estimand and detection event;
- analysis method and exact pipeline;
- performance measures;
- null and alternative scenarios;
- spatial, temporal, network, site, and missingness structure;
- seed and repetition plan;
- Monte Carlo precision criterion;
- fit and pipeline failures;
- candidate-sample search and boundary recheck;
- summaries that will be retained.

Do not treat a smooth power curve or monotonic sequence as guaranteed. Stochastic error and pipeline failures can obscure boundaries.

### 6. Present execution options

Offer only applicable choices:

- run one ready implementation and the selected verification route;
- run two compatible implementations as a cross-check;
- reduce or stage the scenario grid within the approved scientific boundary;
- revise the Monte Carlo precision or resource plan;
- return a scientific input to the user;
- return the specification to [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md);
- route a scalar calculation to [statistical-power](../../skills/statistical-power/SKILL.md);
- defer or stop because implementation is unavailable.

Do not recommend the method that yields the smallest N.

### 7. Gate 2: The user authorizes exact computation

Show:

- selected implementation and version;
- exact inputs and files;
- exact scenario grid;
- code, command, or operation summary;
- seed and numerical-precision plan;
- resource ceiling;
- null and independent checks;
- expected outputs;
- prohibited external actions.

Ask the user to select the exact computation and verification plan.

Gate 2 authorizes only those displayed computations in the approved environment.

It does not authorize a scientific-input change, broader grid, package installation, network service, data upload, output save, observed-data analysis, final sample-size selection, or another capability.

Do not infer approval from silence.

### 8. Execute only the approved calculation

During execution:

- preserve exact inputs, versions, seeds, and commands or code;
- keep scenario order deterministic;
- distinguish invalid pipeline runs from valid nonsignificant outcomes;
- retain failure counts, causes, and handling;
- do not silently relax convergence, QC, correction, mask, threshold, or detection rules;
- do not add scenarios because an interim result is surprising;
- stop at the resource ceiling;
- preserve partial results with their status if execution stops.

For sample-size searches:

- evaluate the selected grid or algorithm only;
- report numerical and Monte Carlo uncertainty at candidate boundaries;
- recheck the proposed boundary with the approved precision rule;
- apply the approved integer, group, block, site, or allocation constraints;
- distinguish required analyzed N from recruited N;
- do not label the smallest passing simulated point as definitive when uncertainty overlaps the target.

### 9. Run verification

As applicable:

- verify null error behavior under the exact pipeline;
- compare a simpler limiting case with a trusted analytic result;
- compare a second validated implementation;
- reproduce a documented benchmark with matching inputs;
- confirm seed reproducibility;
- test parameter and unit perturbations;
- check that a zero-effect or null scenario does not produce claimed alternative power;
- inspect sensitivity to effect, variance, reliability, smoothness, data loss, site, correction, and detection-event assumptions;
- report Monte Carlo standard errors or intervals using the selected method;
- report fit, numerical, pipeline, and resource failures separately.

If a material check fails, label the result **Not validated** and stop before proposing a boundary.

### 10. Produce the Neuroimaging Calculation Record

Include:

| Section | Required content |
|---|---|
| Prospective target | Exact decision, estimand, and detection event |
| Approved specification | Design, acquisition, pipeline, model, inference, correction, and thresholds |
| Inputs | Every value, range, unit, source, translation, and decision owner |
| Implementation | Method, tool, version, environment, code or command record, and seed |
| Scenarios | Exact evaluated grid and completed, failed, or skipped status |
| Results | Power, sample size, MDE, sensitivity, precision, reliability, prediction, or other approved measures |
| Numerical uncertainty | Analytic tolerance, Monte Carlo SE or interval, and boundary uncertainty |
| Null behavior | Estimated error behavior and uncertainty |
| Failures | Counts, causes, handling, and sensitivity |
| Verification | Independent checks, results, and unresolved discrepancies |
| Sensitivity | Approved alternative assumptions and their consequences |
| Analyzed versus recruited | Exact conversion and data-loss assumptions |
| Limitations | Model, evidence, transportability, implementation, and resource limits |
| The user's remaining decision | Final sample size or scientific choice not made by this skill |
| Provenance | User inputs, source evidence, code, outputs, and decisions kept separate |

Result labels:

- **Validated within stated assumptions**
- **Validated with limited cross-check**
- **Not validated**
- **Blocked before execution**
- **Partially completed**

Never report only one sample-size number without the assumptions, sensitivity, and validation record.

## Outputs

Always distinguish:

- **Approved input**
- **Technical translation**
- **Computed result**
- **Numerical uncertainty**
- **Failed or invalid run**
- **Unresolved limitation**
- **user-owned decision**

Return:

1. Calculation Intake Record;
2. readiness status;
3. verified input record;
4. Implementation Preflight;
5. computation and verification plan;
6. Gate decisions;
7. execution record;
8. verification results;
9. Neuroimaging Calculation Record;
10. The user's remaining decision.

Do not use numeric confidence scores or a composite ranking of implementations.

Return calculation results in the current task's requested form or under the recipient's existing reporting policy. Persistent files require the approval below.

Before saving code or outputs, using a network service, uploading data, installing software, or starting another capability:

1. show the exact proposed action;
2. show every source and destination;
3. explain what will change or leave the machine;
4. ask for separate approval;
5. verify afterward.

For an authorized save, use the verified destination selected for the task. If none is selected, use the workflow's established project-owned scientific destination where it applies. For other supporting content, use a destination established by the recipient's placement policy, including Resources when that policy selects it. Skill and system work stays in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved. Add a verified link at the selected location only when the authorized scope includes that edit.

## Boundaries

- **No approved input specification**: Route to [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) and stop.
- **Scalar independent ROI summary**: Route to [statistical-power](../../skills/statistical-power/SKILL.md) unless the approved model is materially tied to the MRI pipeline.
- **Circular ROI or feature selection**: Stop; computation cannot repair the scientific bias.
- **Thresholded map presented as an effect map**: Reject the translation unless the exact required information and valid method are supplied.
- **Package default conflicts with the specification**: Override only through an explicitly verified parameter; otherwise stop.
- **Implementation missing**: Return a complete blocked record; do not install or substitute benchmark tables.
- **Only candidate pseudocode exists**: Treat it as unvalidated and stop.
- **External web calculator proposed**: Require separate approval, current service verification, exact data-disclosure review, and an independent check.
- **Participant-level data or identifiable metadata**: Keep local and within the approved boundary; do not upload.
- **Null calibration fails**: Mark the result Not validated.
- **Simulation failures**: Report rate, reason, handling, and sensitivity; do not count every failure as a negative detection.
- **Nonmonotone estimated power**: Increase precision or evaluate the boundary according to the approved plan; do not silently smooth.
- **Resource limit reached**: Return partial results with numerical uncertainty and no definitive boundary.
- **Only favorable scenario reaches target**: Report the full sensitivity grid; do not elevate that scenario.
- **Required analyzed N conflicts with allocation or site blocks**: Apply only user-approved rounding and design constraints.
- **Data-loss estimate unknown**: Report analyzed N only or selected scenarios; do not insert a conventional buffer.
- **Completed or partly observed study**: Do not derive observed post hoc power from the observed effect.
- **EEG, MEG, PET, or other modality**: Route to the appropriate modality owner or disclose the gap.
- **Context compaction or model switch**: Reload this skill and the approved calculation packet before continuing.

## Handoffs

- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) when the estimand, detection event, effect basis, reliability, data loss, analysis, correction, method, or scenario grid is unresolved.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) for a general scalar-endpoint calculation that does not need an MRI-specific spatial or pipeline model.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) when task-fMRI timing, event mapping, first-level schedule assumptions, or design-matrix efficiency is unresolved.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when units, allocation, clustering, repeated structure, or site design is unresolved.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for one bounded methodological or effect-basis claim.
- Use [research-critique](../../skills/research-critique/SKILL.md) for retrospective design or inference critique.
- Route observed-data fitting, imaging analysis, and scientific inference to Part 4.

Each destination begins its own workflow and gates. Calculator approval does not authorize another capability.

This skill does not choose the scientific design, estimand, modality, ROI, pipeline, model, correction, threshold, effect, target, method, tool, or final sample size; calculate observed post hoc power; install software; upload data; search; save; analyze study outcomes; or make a scientific conclusion for the user.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Cox, R. W., Chen, G., Glen, D. R., Reynolds, R. C., & Taylor, P. A. (2017). FMRI clustering in AFNI: False-positive rates redux. *Brain Connectivity, 7*(3). https://doi.org/10.1089/brain.2016.0475
- Eklund, A., Nichols, T. E., & Knutsson, H. (2016). Cluster failure: Why fMRI inferences for spatial extent have inflated false-positive rates. *PNAS, 113*(28). https://doi.org/10.1073/pnas.1602413113
- Hayasaka, S., Peiffer, A. M., Hugenschmidt, C. E., & Laurienti, P. J. (2007). Power and sample size calculation for neuroimaging studies by non-central random field theory. *NeuroImage, 37*(3). https://doi.org/10.1016/j.neuroimage.2007.06.009
- Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11). https://doi.org/10.1002/sim.8086
- Mumford, J. A. (2012). A power calculation guide for fMRI studies. *Social Cognitive and Affective Neuroscience, 7*(6). https://doi.org/10.1093/scan/nss059
- Mumford, J. A., & Nichols, T. E. (2008). Power calculation for group fMRI studies accounting for arbitrary design and temporal autocorrelation. *NeuroImage, 39*(1). https://doi.org/10.1016/j.neuroimage.2007.07.061
