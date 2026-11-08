---
name: eeg-preprocessing-pipeline-guide
description: >-
  Specifies one approved nonclinical scalp-EEG preprocessing and outcome-blind
  QC plan while preserving acquisition, reference, filters, artifacts, epochs,
  interpolation, provenance, and downstream-compatibility boundaries. Triggers:
  plan my EEG preprocessing, EEG artifact and QC plan.
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

# EEG Preprocessing Pipeline Guide

Specify one EEG preprocessing and QC route without turning software defaults or
artifact heuristics into a scientific decision.

## Purpose

This is a conditional Part 4 EEG method owner for preprocessing, denoising,
filtering, rereferencing, epoching, artifact handling, interpolation, and
outcome-blind QC. It does not choose the task, signal estimand, threshold,
software, or interpretation. [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) owns downstream EEG
measurement specification; [eeg-coordinator](../eeg-coordinator/SKILL.md) owns routing.

Activate only for exact `eeg-preprocessing-pipeline-guide` or an approved
handoff naming one nonclinical scalp-EEG preprocessing plan. Do not trigger
from generic EEG, ERP, filtering, or artifact requests. Out of scope: clinical
EEG, seizure diagnosis, automatic preprocessing, data execution, and result
interpretation.

## Inputs

Obtain or mark missing: acquisition, montage, channel types, sampling, event
markers, reference, line noise, filter and phase, resampling, bad-channel and
artifact policy, ICA or other denoising candidate, epoch and baseline, edge and
rejection rules, downstream estimand, QC, provenance, and outcome contact. If
acquisition, reference, event structure, or downstream compatibility is
missing, return **EEG preprocessing intake incomplete**.

## Steps

### Gate 1: approve the preprocessing specification

Show acquisition, reference, filters, resampling, artifact candidates, epochs,
baseline, rejection, downstream compatibility, QC, alternatives, and claim.
Gate 1 authorizes method comparison only.

### Gate 2: approve one bounded plan or action

Ask the user to select the route, exact environment, output, and verification. Gate
2 authorizes one plan or separately approved action only; it does not authorize
  installation, data execution, or automatic denoising.

Return:

```text
EEG Preprocessing Specification
Acquisition, montage, channels, and reference:
Filters, resampling, phase, and edge handling:
Artifact, ICA, epoch, baseline, and rejection rules:
Downstream compatibility and outcome-blind QC:
Provenance, sensitivity, and permitted claim:
Stop point:
```

## Boundaries

Method rules:

- Preserve raw data and acquisition metadata; preprocessing is not reversible
  merely because a file can be saved.
- Expose filter type, cutoff, order, phase, edge handling, resampling, and
  reference. Avoid leakage across trial or train/test boundaries.
- Separate bad-channel, bad-epoch, ocular, muscle, line-noise, and movement
  decisions. ICA or component rejection requires a prespecified evidence rule
  and sensitivity plan.
- QC is outcome-blind and reports exclusions, missingness, channel counts,
  event loss, and downstream effects. It does not certify scientific validity.

Stop for clinical or diagnostic use; missing acquisition or reference; unknown
event timing; outcome-dependent artifact rejection; irreversible overwrites;
unapproved automatic ICA or filtering; unavailable environment; or a request
to interpret preprocessing or QC as a scientific result.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- MNE. (n.d.). *MNE documentation*.
