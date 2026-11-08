---
name: fmri-task-design-guide
description: >-
  Compares, specifies, and validates task-timing schedules for one approved
  task-fMRI estimand and first-level model. Use when the request, or a stage
  coordinator, hands over an explicitly matching task. It maps neural events and
  states to regressors and contrasts, compares block, event-related, mixed, or
  other credible schedule architectures, exposes HRF, filtering,
  autocorrelation, nuisance, timing, behavioral, and acquisition assumptions,
  and produces only user-selected timing and schedule records after two approval
  gates. It does not choose the paradigm, contrast, model, acquisition, power
  target, or sample size; install optimizers; build a task runner; analyze
  images; search; or save without separate approval. Triggers: design my fmri
  task timing, event related or block design.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: fmri
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-10-29"
---

# fMRI Task Design Guide

Design task-fMRI timing around the estimand and planned model rather than around inherited timing recipes.

## Purpose

`fmri-task-design-guide` is the Part 3 canonical owner for prospective comparison, specification, and model-aware validation of task-timing schedules for one approved task-fMRI estimand.

It owns:

- mapping selected events, epochs, sustained states, responses, errors, and other task components to a proposed first-level design;
- comparing block, event-related, mixed block/event-related, and other credible schedule architectures;
- specifying timing, ordering, null or baseline periods, run segmentation, transitions, and scanner-synchronization requirements;
- generating bounded candidate schedules after Gate 1 from user-approved constraints;
- evaluating rank, estimability, contrast variance, regressor dependence, temporal balance, filtering overlap, and schedule reproducibility under explicit model and noise assumptions;
- producing a selection-bound fMRI Task Timing Specification, Schedule Manifest, and Design Matrix Validation Record.

The user owns the scientific question, hypothesis, prediction, task, neural estimand, conditions, event and state definitions, primary contrast, first-level model, HRF basis, nuisance strategy, acquisition, preprocessing assumptions, power target, sample size, schedule selection, interpretation, and scientific claims.

[cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) owns behavioral or cognitive paradigm selection. [experimental-design](../../skills/experimental-design/SKILL.md) owns the general design, conditions, units, allocation, assignment, and broad counterbalancing. Verify `fmri-glm-analysis-guide` for model specification and `fmri-preprocessing-pipeline-guide` for preprocessing design. Actual software execution uses the selected verified adapter and its own authorized scope. [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) owns MRI-specific power-method and input specification. [neuroimaging-sample-size-calculator](../neuroimaging-sample-size-calculator/SKILL.md) owns approved neuroimaging-specific calculations.

This skill designs timing against a proposed model. It does not select or execute that model.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `power my fMRI study`;
- `analyze this task-fMRI dataset`;
- `choose an fMRI paradigm`;
- `preprocess my fMRI`;
- `write my BIDS events file`;
- broad phrases such as `fMRI`, `BOLD`, `block design`, `jitter`, or `task timing`.

One run covers one primary within-subject task-fMRI estimand, one approved task architecture, one proposed first-level model family, and one acquisition-timing family.

Several linked contrasts may remain together only when they share the same task events, model, schedule, and optimization constraints and the user approves their joint treatment at Gate 1. Otherwise separate them.

Design efficiency is conditional on the exact contrast, design matrix, HRF basis, filtering, temporal covariance, censoring assumptions, acquisition timing, and objective. There is no universally most efficient schedule.

## Inputs

Gather:

- The user's exact question, hypothesis, prediction, neural estimand, and primary contrast;
- approved task or [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) specification;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) conditions, units, assignment, and counterbalancing;
- event, epoch, sustained-state, instruction, cue, stimulus, delay, response, feedback, error, and rest definitions;
- behavioral timing constraints, adaptive behavior, response windows, accuracy needs, practice, fatigue, learning, and burden;
- proposed first-level regressors, basis functions, durations, parametric or trialwise terms, derivatives, modulation and orthogonalization rules, nuisance terms, and intercept or drift model;
- proposed high-pass or temporal filtering and temporal-autocorrelation or whitening assumptions;
- acquisition TR or sampling times, run starts, trigger logic, dummy-volume handling, slice or volume timing assumptions, number and maximum duration of runs, and required breaks;
- expected motion, censoring, physiological, instruction, motor, error, and missed-response behavior;
- trial or block counts, rare events, condition proportions, order restrictions, transition-balance needs, stimulus-repetition constraints, and post hoc event definitions;
- candidate HRF assumptions and known population, region, vascular, medication, aging, or clinical differences;
- available verified runtime and exact permitted tools, or permission for a read-only availability check;
- outcome visibility, confirmatory status, protocol, preregistration, deviations, supplied evidence, desired output, and stop point.

Mark essential missing items `unknown`. Do not import timing or trial-count defaults from the external candidate.

## Steps

### 1. Build the fMRI Task Timing Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded task-fMRI study and Part 3 task |
| Scientific target | The user's exact question, hypothesis, or prediction |
| Neural estimand | Event, epoch, sustained state, modulation, adaptation, interaction, or other target |
| Primary contrast | Exact coefficient or function of coefficients |
| Approved task | Paradigm, conditions, trial structure, stimuli, responses, and behavioral constraints |
| Event and state map | Proposed onsets, durations, responses, errors, instructions, and sustained periods |
| Proposed first-level model | Regressors, basis, derivatives, modulators, nuisance, filtering, covariance, and censoring |
| Acquisition timing | TR or sample times, triggers, dummy volumes, runs, maximum duration, and breaks |
| Candidate architectures | Block, event-related, mixed, or another bounded set |
| Schedule constraints | Counts, proportions, order, transitions, spacing, null periods, and run rules |
| Optimization targets | Contrast variance, HRF estimation, predictability, transition balance, behavioral validity, or other selected metrics |
| Resources | Scanner time, fatigue, motion, equipment, staff, and participant burden |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied evidence that may be inspected |
| Excluded work | Paradigm, contrast, model, acquisition, power, sample-size, preprocessing, analysis, installation, task implementation, search, and saving |
| Stop point | Exact output or decision that ends the run |

If the task, primary estimand, contrast, first-level model, or acquisition timing is unresolved, return the decision to the user or prepare the appropriate handoff. Timing cannot be optimized against an unspecified target.

### 2. Gate 1: approve the model-aware comparison

Ask the user to approve or correct the fMRI Task Timing Brief, candidate schedule architectures, model assumptions, evaluation metrics, evidence boundary, candidate-count cap, and computation boundary.

Gate 1 authorizes only:

- inspection of the displayed supplied evidence;
- construction of the neural-event and model maps;
- generation of the displayed bounded candidate schedules using a verified existing runtime without installation;
- calculation of the displayed design-matrix diagnostics under the approved assumptions;
- comparison without automatic selection.

It does not authorize:

- choosing the task, estimand, contrast, model, HRF basis, filtering, covariance method, acquisition, power target, sample size, or final schedule;
- installing software, building the task runner, saving files, collecting data, preprocessing, or analyzing images.

If the task, estimand, contrast, model, HRF basis, filtering, covariance assumption, acquisition timing, schedule constraints, or comparison metrics change materially, rebuild the brief and repeat Gate 1.

### 3. Build the Neural Estimand and Regressor Map

| Field | Required content |
|---|---|
| Scientific event or state | Exact neural or cognitive target |
| Observable task component | Cue, stimulus, delay, response, error, feedback, block, or other event |
| Onset source | Scheduled, logged, scanner-triggered, participant-response-derived, or post hoc |
| Duration | Instantaneous, fixed epoch, variable epoch, sustained period, or unknown |
| Proposed regressor | Main effect, condition, interaction, modulation, derivative, nuisance, or unmodeled |
| Basis and convolution | Exact proposed HRF or flexible basis and time resolution |
| Primary contrast role | Weight and interpretation |
| Competing signal | Motor, visual, auditory, instruction, error, difficulty, arousal, motion, physiology, or drift |
| Identifiability need | Timing or variation required to separate it |
| Uncertainty | Onset, duration, HRF, response, classification, or missing-event uncertainty |

Do not describe a block regressor as purely sustained or an event regressor as purely transient unless the selected model and timing can support that separation.

### 4. Build the Timing and Model Assumption Register

Create one row per consequential assumption:

| Field | Required content |
|---|---|
| Assumption ID | Stable identifier |
| Assumption | Timing, basis, noise, filtering, censoring, nuisance, or behavior |
| Candidate value or structure | The user supplied, source supported, or `unknown` |
| Provenance | The user supplied, verified exact source, verified translation, external candidate, or AI-generated option |
| Applicability | Task, population, region, acquisition, model, contrast, and software match |
| Design consequence | Rank, contrast variance, collinearity, filtering loss, bias, or feasibility |
| Sensitivity need | Alternative value or model to inspect |
| Status | Eligible, eligible with translation, specialist-required, unresolved, or reject |

HRF timing and shape vary across regions, people, populations, tasks, and vascular conditions. A canonical HRF may be a chosen analysis assumption, but it is not a biological constant.

### 5. Build the Schedule Architecture Option Matrix

Generate two to four `AI-generated fMRI schedule architecture option` entries only when scientifically credible:

| Field | Required content |
|---|---|
| Option ID | Stable label |
| Architecture | Block, event-related, mixed, or another exact family |
| Estimand support | Which selected events, states, or contrasts it can estimate |
| Task flow | High-level timing and behavioral implications |
| Regressor separation | Expected dependencies and required variation |
| Contrast objective | Exact diagnostic or set of diagnostics |
| HRF and noise assumptions | Basis, filtering, covariance, and censoring assumptions |
| Predictability and sequence | Transition, expectation, habituation, and learning implications |
| Acquisition fit | TR, run duration, triggers, dummy volumes, and break constraints |
| Feasibility | Trial count, rare events, behavior, fatigue, motion, and scanner time |
| Evidence status | Exact verified source, translation, user source, or unresolved |
| Limitation | What cannot be estimated or distinguished |

If one architecture is credible, explain why and do not invent alternatives. Do not label block, event-related, rapid, slow, or mixed designs as universally more powerful or efficient.

### 6. Generate bounded candidate schedules after Gate 1

For each approved architecture:

1. display the exact candidate count, seed policy, runtime, generation rule, constraints, and stopping rule;
2. preserve every input and derived timing field;
3. generate only the approved bounded candidate set;
4. retain infeasible and failed candidates with reasons;
5. construct the proposed design matrix using the approved sampling, basis, filtering, and nuisance assumptions;
6. evaluate every approved diagnostic;
7. retain non-dominated candidates or the full bounded set rather than selecting one by an unapproved composite score;
8. verify deterministic regeneration.

Do not install optseq2, NeuroDesign, fMRIpower, or another optimizer. A currently available tool may be used only after its version, objective, parameter meaning, and output are verified and shown within Gate 1.

### 7. Build the Design Matrix Diagnostics

For each candidate show:

| Diagnostic | Required content |
|---|---|
| Matrix state | Dimensions, rank, singular values, scaling, and numerical tolerance |
| Contrast estimability | Whether the primary contrast is estimable and why |
| Contrast variance or efficiency | Exact formula, covariance assumption, normalization, and units |
| Regressor dependence | Correlations, variance inflation, condition index, or another approved diagnostic |
| Basis separation | Dependence among basis functions, derivatives, sustained terms, and transient terms |
| Filtering impact | Variance or signal removed by the selected high-pass and nuisance model |
| Temporal covariance | White, autoregressive, prewhitened, empirical, or unresolved assumption |
| Transition and order | Counts, lag balance, run effects, long runs, and predictability |
| Event counts | Scheduled, expected usable, rare, error, and post hoc classified events |
| Run structure | Duration, starts, ends, breaks, dummy volumes, and boundary imbalance |
| Behavioral feasibility | Response windows, overlap, fatigue, learning, and adaptive behavior |
| Sensitivity | Results under approved alternative HRF, filtering, covariance, censoring, or event-count scenarios |

Use a contrast-variance calculation appropriate to the approved model, such as a form based on the inverse information matrix. Do not use the source candidate's dimensionally incomplete trace expression.

Do not turn several diagnostics into a single ranking unless the user supplies and approves the weights and decision rule. Preserve tradeoffs.

### 8. Build the fMRI Timing Threat Register

Assess:

- condition, event, response, difficulty, motor, sensory, instruction, error, or time confounding;
- rank deficiency, near-collinearity, poor contrast estimability, and basis dependence;
- sustained and transient regressors that the schedule cannot separate;
- post hoc outcome-defined cells with uncertain or imbalanced counts;
- rare events, errors, misses, or no-response trials that may be too sparse;
- HRF mismatch, regional or population variation, nonlinear response, and vascular confounding;
- temporal filtering or nuisance regressors removing task variance;
- temporal autocorrelation, censoring, motion spikes, and run loss;
- fixed, jittered, random, optimized, or predictable timing altering behavior;
- sequence, habituation, expectation, learning, fatigue, and carryover;
- acquisition changes, TR or trigger mismatch, dummy-volume handling, and run boundaries;
- scanner response-device delay, stimulus presentation delay, log-clock drift, and synchronization;
- optimizer overfitting to one assumed model or one scalar objective;
- scanner-time efficiency masking poor behavioral or construct validity.

For each threat show affected option, diagnostic evidence, severity, mitigation candidates, residual risk, owner, and unresolved decision.

### 9. Present response options

For each consequential issue, offer only applicable choices:

- retain an eligible architecture, assumption, or candidate schedule;
- return the scientific or model decision to the user;
- run an approved sensitivity analysis;
- revise the schedule constraint through its owner;
- collect a behavioral or scanner-timing pilot;
- request a bounded [research-literacy](../../skills/research-literacy/SKILL.md) audit or [paper-search](../../skills/paper-search/SKILL.md);
- prepare an acquisition, behavioral task, design, BIDS, power, GLM, preprocessing, implementation, or specialist handoff;
- defer the timing specification.

Do not recommend a schedule merely because it has the highest value under one assumed metric.

### 10. Gate 2: The user selects the schedule

Ask the user to select:

- schedule architecture and exact candidate schedule;
- HRF, filtering, covariance, censoring, nuisance, and sensitivity assumptions retained for design validation;
- timing, ordering, null periods, transitions, run segmentation, and trigger rules;
- unresolved assumptions that must remain visible;
- required pilot and verification steps;
- selected handoff packets.

Gate 2 authorizes only the selected fMRI Task Timing Specification, Schedule Manifest, validation record, and handoff packets.

It does not authorize changing the behavioral task, first-level model, acquisition protocol, power inputs, sample size, task-runner implementation, software installation, file saving, data collection, preprocessing, or image analysis.

Do not infer selection from silence.

### 11. Produce and verify the fMRI Task Timing Specification

Return:

| Field | Required content |
|---|---|
| Approved scope | Task, estimand, contrast, model, acquisition timing, evidence boundary, and intended use |
| Selected architecture | Exact family and the user's selection |
| Event and state model | Onsets, durations, response-derived events, errors, sustained periods, and omitted components |
| Schedule | Condition and event order, onsets, durations, gaps, null periods, and run boundaries |
| Acquisition synchronization | Trigger, dummy-volume, clock, TR or sampling, and logging requirements |
| Model assumptions | Basis, filtering, covariance, nuisance, censoring, and scaling used for validation |
| Diagnostics | Rank, estimability, contrast variance, dependence, filtering, transitions, and sensitivity |
| Behavioral constraints | Response, performance, fatigue, learning, practice, and adaptive behavior |
| Pilot and QA | Behavioral, scanner, timing, logging, synchronization, and design-matrix checks |
| Open items | Scientific, model, acquisition, power, BIDS, implementation, or analysis gaps |
| Handoffs | Only Gate 2 selected packets |
| Provenance | User decisions, source evidence, translations, candidate generation, seeds, and diagnostics kept separate |

Verify that:

- the scientific target, estimand, contrast, model, and acquisition assumptions were supplied or selected by the user;
- every event or state has an exact onset and duration source;
- the primary contrast is estimable under the displayed model;
- rank, numerical tolerance, filtering, covariance, nuisance, and censoring assumptions are explicit;
- schedule and candidate seeds regenerate deterministically;
- no fixed source timing, trial count, jitter distribution, null fraction, run length, HRF value, or efficiency table became a default;
- no unapproved composite ranking selected the schedule;
- post hoc event counts and design changes remain labeled;
- no power, sample-size, acquisition, task implementation, saving, preprocessing, or image analysis occurred.

## Schedule Manifest

Preserve at minimum:

- study, session, run, trial, block, and event identifiers;
- condition, event type, onset, duration, expected response, and stimulus or item ID;
- null or baseline periods and run boundaries;
- scanner trigger and clock reference;
- candidate seed, generator, runtime, algorithm, objective, and version;
- selected design-matrix specification and contrast IDs;
- order, transition, counterbalancing, and stimulus-assignment fields;
- expected versus post hoc event labels kept separate;
- validation status, deviations, and provenance.

A Schedule Manifest is not automatically a BIDS `events.tsv`, task-runner file, or first-level analysis specification. Those require their own schema and owner.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the recipient's applicable reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **fMRI Task Timing Brief**
- **Neural Estimand and Regressor Map**, after Gate 1
- **Timing and Model Assumption Register**
- **Schedule Architecture Option Matrix**
- **Candidate Schedule Set**
- **Design Matrix Diagnostics**
- **fMRI Timing Threat Register**
- **Response Options**
- **fMRI Task Timing Specification**, only after Gate 2
- **Schedule Manifest**
- **Design Matrix Validation Record**
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return the task design results in the current task's requested form or under the recipient's existing reporting policy. Gate 1 may authorize the displayed bounded candidate generation and diagnostics, but neither gate authorizes installing software, writing files, building a task, creating BIDS records, changing a source, collecting data, preprocessing, analyzing images, searching, or starting another capability.

Before any separately approved save or external action:

1. show the exact destination or action;
2. show the exact files, rows, duration, size, runtime, software, and overwrite behavior;
3. show validation and recovery behavior;
4. ask for approval;
5. verify the result afterward.

For an authorized save, use the destination selected for the task. Otherwise use the established project or area destination when the recipient's placement policy calls for it. Keep skill and system work in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved.

## Boundaries

- **No approved task or neural estimand**: Stop or route to [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md).
- **No approved primary contrast or first-level model**: Preserve the gap; do not optimize timing.
- **One credible architecture**: Explain the constraint and do not invent alternatives.
- **No null or rest events**: Do not declare the design invalid automatically. Evaluate the exact contrast, intercept, temporal structure, filtering, and model.
- **Fixed timing**: Do not declare it invalid automatically. Evaluate estimability, behavioral consequences, aliasing, and the selected objective.
- **Very short event spacing**: Require an explicit HRF and nonlinearity sensitivity plan rather than a universal cutoff.
- **Canonical HRF assumed**: Preserve population and regional mismatch risk and inspect a flexible-basis sensitivity when selected.
- **Mixed design**: Test block, transition, and event regressor dependence explicitly.
- **Subsequent-memory or outcome-defined event types**: Preserve uncertain cell counts, missingness, performance dependence, and post hoc classification.
- **Rare errors or misses are modeled**: Simulate plausible count ranges and retain infeasible scenarios.
- **Adaptive task**: Define which onsets and durations are fixed, response-dependent, or state-dependent and simulate the approved range.
- **Trialwise or parametric modulation**: Require the exact modulation, centering, scaling, orthogonalization, and correlation plan.
- **Run loss or censoring**: Evaluate the selected loss scenarios without silently adding scanner time.
- **TR or acquisition timing changes**: Repeat Gate 1 because the sampled design matrix changes.
- **Optimizer returns one best scalar score**: Return the full approved metrics and non-dominated alternatives unless the user approved that scalar rule.
- **Candidate matrix is singular or near singular**: Report the exact dependency and stop; do not remove a regressor silently.
- **Behavioral timing and BOLD efficiency conflict**: Preserve the tradeoff for the user.
- **Runtime or optimizer unavailable**: Return the specification and stop. Do not install software.
- **Outcomes already inspected**: Label schedule changes post hoc or exploratory as appropriate.
- **MRI power inputs requested**: Route to [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md).
- **Neuroimaging-specific numerical calculation requested**: Route to [neuroimaging-sample-size-calculator](../neuroimaging-sample-size-calculator/SKILL.md) only with an approved complete specification.
- **Observed images supplied**: Route to Part 4. Do not analyze them here.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the behavioral or cognitive task architecture, manipulation, comparator, outcome, or task validity is unresolved.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when conditions, units, allocation, assignment, broad counterbalancing, or general trial structure is unresolved.
- Use [visual-search-array-generator](../visual-search-array-generator/SKILL.md) for deterministic array layouts after a controlled-array visual-search task is approved.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) for separable behavioral-outcome power inputs.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only for a general calculation after the relevant domain inputs are approved.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) for MRI-specific power-method and input specification.
- Use [neuroimaging-sample-size-calculator](../neuroimaging-sample-size-calculator/SKILL.md) after an MRI-specific Power Inputs Specification is approved and ready for numerical execution.
- Use [research-critique](../../skills/research-critique/SKILL.md) to critique an existing task-fMRI protocol rather than prospectively build timing options.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for one bounded methodological claim and [paper-search](../../skills/paper-search/SKILL.md) for a separately approved evidence search.
- Use [bids](../bids/SKILL.md) after timing and scientific event meanings are approved when the
  unresolved work is version-pinned BIDS event, entity, metadata, provenance,
  privacy, or compliance specification.
- Route acquisition protocol, task-runner implementation, display timing,
  scanner synchronization, fMRI GLM method, preprocessing, image quality
  control, BIDS file transformation, and observed-data analysis to their
  approved owners.

Each destination begins its own workflow and gates. fMRI Task Design approval does not authorize another capability.

This skill does not choose the scientific task, estimand, contrast, first-level model, acquisition, power target, sample size, optimizer, or final interpretation; install software; build a task runner; create BIDS files; collect data; preprocess or analyze images; search; save; or make a scientific conclusion for the user.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Handwerker, D. A., Ollinger, J. M., & D'Esposito, M. (2004). Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. *NeuroImage, 21*(4). https://doi.org/10.1016/j.neuroimage.2003.11.029
- Liu, T. T., Frank, L. R., Wong, E. C., & Buxton, R. B. (2001). Detection power, estimation efficiency, and predictability in event-related fMRI. *NeuroImage, 13*(4). https://doi.org/10.1006/nimg.2000.0728
- Nichols, T. E., Das, S., Eickhoff, S. B., et al. (2017). Best practices in data analysis and sharing in neuroimaging using MRI. *Nature Neuroscience, 20*(3). https://doi.org/10.1038/nn.4500
- Petersen, S. E., & Dubis, J. W. (2012). The mixed block/event-related design. *NeuroImage, 62*(2). https://doi.org/10.1016/j.neuroimage.2011.09.084
- Poldrack, R. A., Fletcher, P. C., Henson, R. N. A., Worsley, K. J., Brett, M., & Nichols, T. E. (2008). Guidelines for reporting an fMRI study. *NeuroImage, 40*(2). https://doi.org/10.1016/j.neuroimage.2007.11.048
