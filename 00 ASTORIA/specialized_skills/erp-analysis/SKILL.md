---
name: erp-analysis
description: >-
  Specifies one approved nonclinical event-related-potential estimand,
  component, time window, electrode region, amplitude measure, and inference
  handoff without choosing the component, running preprocessing, fitting data,
  or interpreting a waveform as a cognitive process. Triggers: specify my ERP
  component analysis, ERP time window and electrode choice.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: eeg
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# ERP Analysis

Specify one ERP measurement and inference boundary without converting familiar
component labels or parameter defaults into a post hoc scientific decision.

## Purpose

This is a conditional Part 4 ERP method owner. It compares component and
estimand definitions, time windows, electrode or source regions, amplitude and
latency measures, baseline, trial and participant aggregation, mass-univariate
or summary routes, and claim limits. It does not choose the user's construct,
preprocess data, inspect outcomes to select a window, or interpret a waveform.

The user owns the question, prediction, component, window, region, measure,
baseline, confirmatory status, and claim. [eeg-preprocessing-pipeline-guide](../eeg-preprocessing-pipeline-guide/SKILL.md)
owns preprocessing; [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) owns broader EEG measurement routes.

Activate only for exact `erp-analysis` or an approved handoff naming one ERP
estimand. Do not trigger from generic EEG, ERP, waveform, or component requests.
Out of scope: clinical EEG, automatic component identification, post hoc window
selection, data execution, and person-level interpretation.

## Inputs

Obtain or mark missing: acquisition and event structure, preprocessing state,
component construct, polarity, time window, electrode or source region, measure
(mean, peak, area, latency), baseline, trial and participant grain, exclusions,
statistical handoff, outcome contact, and permitted claim. If component,
window, region, or baseline is missing, return **ERP intake incomplete**.

## Steps

### Gate 1: approve the ERP estimand

Show the scientific contract, component and alternatives, polarity, window,
region, measure, baseline, aggregation, statistical route, outcome contact,
and limitations. Gate 1 authorizes method comparison only.

### Gate 2: approve one complete specification

Ask the user to select, revise, or reject the component, window, region, measure,
baseline, aggregation, inference, reporting fields, and claim. Gate 2
authorizes a specification only; it does not authorize data access, execution,
or interpretation.

Return:

```text
ERP Analysis Method Specification
Question, prediction, component construct, and status:
Event and preprocessing state:
Polarity, time window, electrode/source region:
Amplitude or latency measure and baseline:
Trial, participant, condition, and dependence grain:
Statistical handoff, multiplicity, and sensitivity:
Outcome-contact and deviation state:
Reporting fields and permitted claim:
Known limitations and stop point:
```

## Boundaries

Method rules:

- Component names are descriptive labels, not proof of a single process. State
  the construct-to-measure argument and competing interpretations.
- Select windows and regions prospectively or label outcome-informed choices
  exploratory. Do not use the largest observed peak as the confirmatory window.
- Compare mean amplitude, peak amplitude, area, fractional or adaptive latency
  only when their assumptions and sensitivity are explicit.
- Preserve electrode, reference, baseline, trial, participant, and condition
  dependence. Route multiplicity, cluster permutation, and uncertainty to the
  statistical owner.
- Report preprocessing, missingness, rejected trials, effect estimates,
  intervals, and deviations. A significant waveform difference does not by
  itself identify a cognitive process.

Stop for clinical use; missing events, preprocessing, window, region, or
baseline; outcome-selected component or window without exploratory labeling;
automatic component naming; pooled data that destroys dependence; a request to
run software or interpret a waveform as a person-level trait or mechanism.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
