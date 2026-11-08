---
name: eeg-paradigm-designer
description: >-
  Compares and specifies one already-selected event-related EEG task schedule
  for one user-approved cognitive task, EEG target, estimand, manipulation, and
  population, then produces a selection-bound EEG Paradigm Specification after
  two approval gates. Use when the request, or a part coordinator, hands over an
  explicitly matching design question. It makes event, trial, run, timing,
  response, marker, synchronization, balance, ocular, motor, overlap, break,
  hardware, and end-to-end validation assumptions visible without choosing the
  research question, task family, EEG feature, trial count, acquisition system,
  preprocessing, measurement window, electrodes, analysis, software, or
  scientific interpretation. It does not design resting, sleep, clinical,
  continuous, SSVEP, or BCI EEG; implement or run a task; collect or process
  data; copy task assets; or save without separate approval. Triggers: design my
  EEG task schedule, event related EEG paradigm timing.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: eeg
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-09-23"
---

# EEG Paradigm Designer

Specify one event-related EEG-compatible task schedule without turning a
named ERP or time-frequency feature into a fixed recipe or a scientific
conclusion.

## Purpose

`eeg-paradigm-designer` is the conditional Part 3 owner for translating one
already-approved cognitive task and user-supplied EEG target into an
event-related task schedule, marker dictionary, confound controls, and
end-to-end validation plan.

It owns event, trial, block, run, and session ontology; stimulus, response,
feedback, and inter-event timing routes; marker naming and synchronization;
condition balance; ocular and motor design threats; breaks; platform
constraints; and final-stack validation requirements.

It does not choose the cognitive construct, task family, hypothesis,
prediction, component, frequency feature, acquisition system, montage,
reference, sample rate, impedance rule, trial count, artifact method,
baseline correction, measurement window, electrode set, statistical model, or
interpretation.

Activate only when:

- The user invokes the exact trigger `eeg-paradigm-designer`; or
- a verified Active capability hands off one already-selected event-related
  EEG task with an explicit target, estimand, manipulation, and population.

Do not activate from `EEG`, `ERP`, `N400`, `P300`, `brain waves`, `design an
experiment`, `record EEG`, `preprocess EEG`, or `analyze EEG`.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the construct, task family, or EEG
versus another method remains undecided. Use [experimental-design](../../skills/experimental-design/SKILL.md) when
units, factors, conditions, allocation, or general counterbalancing remain
undecided. Route power to [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) or [statistical-power](../../skills/statistical-power/SKILL.md).

This skill supports one task or event-related EEG administration, including
ERP and event-related time-frequency questions.

It excludes:

- resting-state, sleep, ambulatory, clinical-monitoring, and continuous-stream
  EEG;
- SSVEP, frequency-tagging, neurofeedback, and BCI design;
- acquisition-hardware selection and recording procedures;
- preprocessing, artifact correction, component quantification, source
  localization, statistics, and software syntax;
- sample, participant, item, or retained-trial calculation;
- task programming, deployment, data collection, or BIDS packaging.

If the requested design crosses these boundaries, return the in-scope
event-schedule portion and a checkpointed handoff. Never absorb the later
owner.

## Inputs

Handle one already-selected task at a time.

| Field | Required content |
|---|---|
| Approved task | Task family and task structure already selected by the user |
| EEG target | user-supplied event-related feature and why it is relevant |
| Estimand and contrast | Exact event-locked or response-locked quantity and comparison |
| Manipulation | Approved conditions and intended physical/cognitive difference |
| Population | Intended participants and relevant sensory, motor, clinical, or accessibility constraints |
| Events | Candidate stimulus, cue, response, feedback, and task-state events |
| Hardware context | Known display, audio, response, amplifier-trigger, eye-tracking, or peripheral constraints |
| Evidence | Exact paradigm, methods, standards, or local documentation supplied or approved for review |
| Stop point | Chat-only specification or separately approved handoff |

If the task, EEG target, or estimand is absent, state the missing owner-level
decision and stop. Do not generate it for the user.

## Steps

### 1. Establish the design boundary

Restate the approved task, target, estimand, contrast, population, scientific
constraints, hardware context, source boundary, asset rights, unresolved
choices, and exclusions. Separate supplied facts from interpretation.

### 2. Gate 1: approve the evidence and comparison boundary

Present:

1. approved task, target, estimand, and contrast;
2. exact sources and rights state;
3. event, timing, response, marker, confound, and validation fields to inspect;
4. credible schedule routes;
5. fixed owner-level decisions and unresolved choices;
6. exclusions and later handoffs.

Gate 1 authorizes only the displayed design review. It does not authorize a
new hypothesis, task-family choice, power calculation, task code, asset use,
recording setup, acquisition, preprocessing, analysis, deployment, or saving.

Reopen Gate 1 after a material task, target, source, population, device, or
estimand change.

### 3. Build the Event Ontology

For every session, run, block, trial, and event, record:

- name and unique identifier;
- condition and role in the approved contrast;
- preceding and following event;
- physical onset, logged onset, duration, and response relationship;
- marker code and clock;
- balance, randomization, omission, invalidation, and restart behavior;
- later measurement requirement without choosing its implementation.

### 4. Build the Timing Route Matrix

| Route | Scientific support | Event overlap | Predictability | Motor and ocular load | Device constraints | Unknowns |
|---|---|---|---|---|---|---|
| Route A | | | | | | |
| Route B | | | | | | |
| Fixed route | | | | | | |

Compare only plausible routes. Do not rank them.

### 5. Build the Marker Dictionary

| Event | Code | Condition fields | Clock | Expected physical relation | Failure checks |
|---|---|---|---|---|---|
| | | | | | |

Include pause, abort, omission, invalid response, and restart states when they
can affect the data. Do not overload one code with several scientific events.

### 6. Build the Confound Register

At minimum assess:

- low-level visual or auditory differences;
- probability, novelty, relevance, and expectancy;
- motor requirement, response hand, speech, and feedback;
- eye position, blink opportunity, retinal input, and head movement;
- temporal overlap and condition-dependent preceding context;
- practice, fatigue, learning, breaks, and run order;
- unequal valid-event counts and differential artifacts;
- device, display, audio, trigger, and clock behavior;
- component overlap and reverse-inference risk;
- population-specific sensory, motor, clinical, medication, and accessibility
  constraints.

For each threat, show evidence, affected contrast, possible control, residual
risk, and the user's retained decision.

### 7. Build the final-stack Validation Plan

Specify:

1. exact task build and device stack to test;
2. external timing measurement when justified;
3. marker completeness, uniqueness, order, latency, jitter, and drift checks;
4. condition, event, response, and valid-trial balance checks;
5. ocular and motor behavior checks;
6. pause, abort, dropped-frame, dropped-marker, and restart tests;
7. pilot observables and failure thresholds to be chosen by the user;
8. evidence and logs that must survive handoff.

Validation may use synthetic or pilot events, but this skill does not execute
the test.

### 8. Gate 2: select the paradigm

Present the ontology, route matrix, marker dictionary, confound register,
validation plan, evidence labels, limitations, and handoffs.

The user selects the event schedule, timing route, response and feedback behavior,
marker scheme, balance and break rules, confound controls, validation scope,
unresolved items, and next stop.

Gate 2 authorizes only the selected EEG Paradigm Specification. It does not
authorize task programming, acquisition settings, sample size, recording,
preprocessing, component measurement, statistics, deployment, or saving.

### 9. Produce the EEG Paradigm Specification

Return:

1. approved task, target, estimand, contrast, and population;
2. scope, exclusions, and source state;
3. session, run, block, trial, and event ontology;
4. selected event timing and distribution;
5. response, feedback, practice, break, and stopping behavior;
6. marker dictionary and synchronization assumptions;
7. condition, event, and response balance;
8. ocular, motor, sensory, expectancy, fatigue, and overlap controls;
9. final-stack validation plan;
10. evidence labels, assumptions, unknowns, and residual risks;
11. user-selected choices and rejected routes;
12. separately approved handoff or explicit stop.

### 10. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- task, target, and estimand came from the user or an approved handoff;
- event, trial, run, and later epoch remain distinct;
- markers and physical timing remain distinct;
- no universal EEG parameter entered as a default;
- no component is treated as one cognitive process;
- motor and ocular threats include changed-input risk;
- the exact final stack requires validation;
- both gates bound their authorization;
- no implementation, acquisition, processing, analysis, or scientific choice
  was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The user owns the question, hypothesis, prediction, confirmatory status, task,
manipulation, EEG target, estimand, scientific contrast, population,
acquisition choice, power inputs, preprocessing and measurement plan,
interpretation, and final selections.

This skill:

- never infers one cognitive process from a named waveform or scalp pattern;
- never treats a component label, polarity, latency, or topography as a fixed
  neural mechanism;
- never selects timing or trial counts from an unverified table;
- never copies stimuli, task code, fonts, sounds, images, or proprietary
  materials;
- records asset source, license, population, language, and modification state;
- stops when task assets or implementation rights are unresolved.

For every proposed parameter:

1. label it `direct evidence`, `bounded adaptation`, `design-derived`,
   `candidate for pilot`, or `unknown`;
2. record source, version, population, task, device, acquisition context, and
   applicability;
3. distinguish scientific timing from software timestamps and physical
   stimulus timing;
4. preserve conflicting recommendations;
5. give a range or candidate routes only when evidence supports them;
6. route sample and retained-trial calculations to the power owner;
7. require final-stack validation before deployment.

Do not use universal defaults for SOA, ISI, jitter, stimulus duration, response
window, practice, breaks, block length, trial count, attrition, error rate,
epoch, baseline, channel count, electrode, reference, filter, sample rate,
impedance, ocular threshold, component window, or scalp site.

Edge cases:

- **Only `EEG` is supplied:** do not activate or invent a task and target.
- **A fixed table supplies timings or trials:** relabel them as unverified
  source examples and compare only after applicability review.
- **A difference wave is called one process:** restore component overlap and
  construct limits.
- **A software timestamp is called stimulus onset:** require final-stack
  physical timing validation.
- **Conditions differ in eye or motor behavior:** surface changed input and
  contrast contamination, not only artifact correction.
- **Rest, sleep, clinical, continuous, SSVEP, or BCI EEG:** route out of scope.
- **Trial count is requested:** hand off the design inputs to the power owner.
- **Preprocessing or analysis is requested:** stop at the design handoff.
- **EEG plus reading:** require a joint checkpoint with the reading owner.
- **No defensible schedule:** return a blocked specification.

This skill cannot establish that an ERP or time-frequency feature uniquely
indexes a construct, predict recording quality, choose acquisition or
preprocessing settings, calculate power, prove physical timing without a
validated stack, or guarantee that an implemented task matches the
specification.

## Design facts that control the review

### Event and timing ontology

- Define session, run, block, trial, event, response, and later analysis epoch
  as separate grains. A trial may contain several separately marked events.
- Exact event order, duration, timing distribution, response mapping,
  feedback, randomization, practice, breaks, and termination conditions must
  be explicit.
- A software event log does not prove physical display, audio, or response
  timing. The exact final hardware, operating system, display or audio path,
  response device, trigger path, and task build require end-to-end validation.
- Use a photodiode, microphone, loopback, or other external timing measure when
  the target timing and device make it relevant. Do not prescribe one when it
  is unnecessary.

### Markers and synchronization

- Every event needed for the approved estimand needs an unambiguous marker,
  condition coding, event grain, clock source, expected ordering, and
  verification rule.
- Marker codes must distinguish events that could otherwise share a timestamp
  or label, including stimulus onset, response, feedback, omission, invalid
  trial, pause, and restart when relevant.
- Record latency, jitter, dropped-marker, duplicate-marker, clock-drift, and
  restart checks. A clean marker file is not evidence that the physical event
  occurred at that time.
- BIDS event naming and packaging occur later. This skill produces a marker
  dictionary, not a BIDS dataset.

### Confounds and interpretation

- Eye movements, blinks, head motion, speech, and button presses can change
  both the recorded signal and the participant's sensory or cognitive input.
  Offline correction cannot undo a changed retinal image or task strategy.
- Conditions that differ in motor demands, response probability, low-level
  sensory properties, event probability, temporal predictability, or task
  relevance may support a different contrast than the intended one.
- Event-related components overlap in time. A named component or difference
  wave is not generated by one process and does not prove a unique mechanism.
- Baseline context must not contain an anticipated condition difference.
  Exact baseline correction, filter, measurement window, and electrode choice
  belong to the later measurement and analysis plan.
- Participant and retained-trial needs depend jointly on design, feature,
  effect, noise, artifacts, reliability, analysis, and population. There is no
  universal EEG trial or participant count.

## Event timing and marker validation

Use the Event Ontology and Marker Dictionary to tie the event schedule,
synchronization, and response behavior to identifiable events. Record
assumptions, gaps, and confounds in the Timing Route Matrix and Confound
Register. Specify in the Validation Plan how the selected event, marker,
synchronization, and response routes will be checked. Compare only routes
compatible with the evidence when a decision remains open. If one route is
defensible, explain why it fits.

After Gate 2, record only the user's selections in the EEG Paradigm
Specification. Stop before implementation, acquisition, preprocessing,
measurement, or analysis.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) for task-family or method comparison.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, or general
  counterbalancing.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) and then [statistical-power](../../skills/statistical-power/SKILL.md) for participant,
  item, trial, reliability, attrition, and operating-characteristic planning.
- Route acquisition, preprocessing, component measurement, statistics,
  implementation, and BIDS packaging only after the relevant design is
  selected.
- For an EEG plus self-paced-reading study, coordinate with
  [self-paced-reading-designer](../self-paced-reading-designer/SKILL.md): reading owns reveal and region structure;
  EEG owns event markers, physical onset validation, and EEG-specific motor
  and ocular timing.

Never chain automatically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- BIDS. (n.d.). *Brain Imaging Data Structure specification* (Version 1.10.1).
- Boudewyn et al. (2018). https://doi.org/10.1111/psyp.13049
- Bridges et al. (2020). https://doi.org/10.7717/peerj.9414
- [EEG-BIDS]. (n.d.). https://doi.org/10.1038/s41597-019-0104-8
- Kappenman et al. (2021). [ERP CORE]. https://doi.org/10.1016/j.neuroimage.2020.117465
- Keil et al. (2014). Committee report: Publication guidelines and recommendations for studies using EEG and MEG. *Psychophysiology*. https://doi.org/10.1111/psyp.12147
- Lepauvre et al. (2024). https://doi.org/10.3758/s13428-024-02508-y
- Pernet et al. (2020). [COBIDAS]. https://doi.org/10.1038/s41593-020-00709-0
- Picton et al. (2000). Guidelines for using human event-related potentials to study cognition. https://doi.org/10.1111/1469-8986.3720127
- Soskić et al. (2025). [ARTEM-IS] (Version 2.1). https://doi.org/10.1111/psyp.70187
