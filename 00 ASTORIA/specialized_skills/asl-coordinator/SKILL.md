---
name: asl-coordinator
description: >-
  Routes one approved nonclinical arterial-spin-labeling perfusion MRI
  checkpoint while preserving labeling strategy, acquisition, M0, CBF estimand,
  registration, partial-volume, QC, provenance, and claim boundaries. Triggers:
  route my ASL perfusion task, next step for my ASL analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: asl
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-24"
  updated: "2026-09-23"
---

# ASL Skill

Route one ASL perfusion-MRI checkpoint without silently selecting a CBF model,
reference, correction, or interpretation.

## Purpose

This is a conditional Part 4 ASL modality coordinator. It distinguishes pCASL,
CASL, and PASL acquisition, label/control and M0 state, calibration, motion,
registration, partial-volume correction, CBF estimand, QC, and export. It does
not choose the scientific estimand, parameters, software, or clinical claim.

The user owns labeling, acquisition, M0, reference, correction, estimand, and claim.
[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI routing; [nibabel-skill](../nibabel-skill/SKILL.md) owns selected
low-level file operations.

Activate only for exact `asl-coordinator` or an approved handoff naming one ASL
checkpoint. Do not trigger from generic perfusion, MRI, CBF, or clinical
requests. Out of scope: clinical diagnosis, automatic pipeline execution,
downloads, installs, and tracer or perfusion interpretation.

## Inputs

Obtain or mark missing: labeling strategy, acquisition metadata, label/control,
M0, timing, background suppression, field of view, structural reference,
registration, correction candidates, CBF estimand, QC, environment, output,
and claim. If strategy, timing, M0, or estimand is missing, return **ASL
intake incomplete**.

## Steps

### Gate 1: approve the ASL checkpoint

Show strategy, acquisition, M0, timing, structural reference, corrections, CBF
estimand, QC, output, alternatives, and claim. Gate 1 authorizes routing only.

### Gate 2: approve one bounded handoff or action

Ask the user to select the checkpoint, owner, environment, output, and verification.
Gate 2 authorizes one bounded step only; it does not authorize installation,
downloads, or clinical interpretation.

Return:

```text
ASL Checkpoint Record
Labeling strategy, acquisition, label/control, and M0:
Timing, calibration, motion, registration, and correction:
CBF estimand, units, QC, and structural reference:
Handoff, output, provenance, and verification:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve raw label/control, M0, calibration, timing, and orientation. Do not
  infer pCASL or PASL from filenames.
- Separate motion, registration, partial-volume, and calibration decisions;
  record assumptions and sensitivity, not universal defaults.
- Keep CBF units and reference explicit. A perfusion map is not a diagnosis or
  evidence of regional function without a separate design.
- Route implementation to separately approved modality or file adapters;
  category membership does not authorize chaining.

Stop for missing strategy, timing, M0, orientation, or estimand; clinical use;
unapproved corrections; unavailable owner or environment; a request to install,
download, run a full pipeline, or interpret perfusion clinically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
