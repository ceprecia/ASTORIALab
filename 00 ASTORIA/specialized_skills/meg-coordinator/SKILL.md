---
name: meg-coordinator
description: >-
  Routes one approved nonclinical MEG analysis checkpoint while preserving
  acquisition format, sensor and head geometry, preprocessing, event timing,
  source, time-frequency, connectivity, QC, provenance, and claim boundaries.
  Triggers: route my MEG task, next step for my MEG analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: meg
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-24"
  updated: "2026-10-29"
---

# MEG Skill

Route one MEG checkpoint without silently selecting a source model, filter,
connectivity measure, or interpretation.

## Purpose

This conditional Part 4 modality coordinator distinguishes MEG formats and sensor
types, head position and anatomy, events, preprocessing, time-frequency,
connectivity, source, decoding, QC, and export. It does not choose the
estimand, forward model, inverse method, or claim.

The user owns acquisition, modality, question, method, parameters, anatomy,
inference, and claim. [mne-python-guide](../mne-python-guide/SKILL.md) owns method comparison;
[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI routing.

Activate only for exact `meg-coordinator` or an approved handoff naming one MEG
checkpoint. Do not trigger from generic MEG, magnetoencephalography, source,
or time-frequency requests. Out of scope: clinical use, automatic source
localization, full pipelines, downloads, installs, and interpretation.

## Inputs

Obtain or mark missing: format and system, sensor types, head position,
sampling, events, anatomy and coregistration, reference, preprocessing,
estimand, candidate source or sensor route, inference, environment, QC, output,
and claim. If format, geometry, anatomy, or estimand is missing, return **MEG
intake incomplete**.

## Steps

### Gate 1: approve the MEG checkpoint

Show format, sensors, geometry, anatomy, events, preprocessing, estimand,
candidate route, QC, output, alternatives, and claim. Gate 1 authorizes
routing and comparison only.

### Gate 2: approve one bounded handoff or action

Ask the user to select the checkpoint, owner, environment, output, and verification.
Gate 2 authorizes one bounded step only; it does not authorize installation,
downloads, full pipelines, or interpretation.

Return:

```text
MEG Checkpoint Record
Format, sensors, head position, anatomy, and coordinates:
Events, preprocessing, covariance, and QC:
Sensor, time-frequency, connectivity, decoding, or source route:
Handoff, output, provenance, and verification:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve acquisition format, sensor geometry, head-position indicators,
  anatomy, coordinate frames, and event timing. Do not infer them from file
  extensions.
- Keep sensor, time-frequency, connectivity, decoding, and source checkpoints
  separate. Source results require an explicit forward and inverse model.
- Record filters, Maxwell or other preprocessing, bad channels, epoching,
  covariance, coregistration, leakage, and multiplicity assumptions.
- Route implementation to a separately approved adapter. A source map or
  connectivity graph is not a causal or clinical result.

Stop for missing format, geometry, anatomy, events, or estimand; clinical use;
source claims without forward/inverse specification; unavailable owner;
unapproved installation, download, or full pipeline; or interpretation of MEG
maps as mechanism or clinical truth.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- MNE-Python developers. (n.d.). *MNE-Python documentation*. https://mne.tools/stable/
