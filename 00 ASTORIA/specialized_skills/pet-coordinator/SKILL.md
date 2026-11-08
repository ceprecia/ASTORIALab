---
name: pet-coordinator
description: >-
  Routes one approved nonclinical PET imaging checkpoint while preserving tracer
  identity, acquisition, attenuation, registration, reference region, SUVR or
  kinetic estimand, partial-volume correction, QC, provenance, and claim
  boundaries. Triggers: route my PET task, next step for my PET analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: pet
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-24"
  updated: "2026-09-23"
---

# PET Skill

Route one PET checkpoint without silently selecting a tracer model, reference
region, correction, or interpretation.

## Purpose

This conditional Part 4 PET modality coordinator distinguishes tracer and scan
identity, acquisition and attenuation, motion, reconstruction, registration,
reference region, SUVR or kinetic estimand, partial-volume correction, QC, and
export. It does not choose the tracer, model, reference, correction, software,
or claim.

The user owns tracer, acquisition, reference, estimand, correction, and claim.
[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI routing; [nibabel-skill](../nibabel-skill/SKILL.md) owns selected
low-level file operations.

Activate only for exact `pet-coordinator` or an approved handoff naming one PET
checkpoint. Do not trigger from generic PET, SUVR, amyloid, FDG, tau, or
clinical requests. Out of scope: clinical diagnosis, automatic tracer
interpretation, full pipelines, downloads, and installs.

## Inputs

Obtain or mark missing: tracer and radiochemistry, acquisition timing,
attenuation and reconstruction, decay correction, motion, structural reference,
registration, reference region, SUVR or kinetic estimand, partial-volume
candidate, QC, environment, output, and claim. If tracer, timing, reference,
or estimand is missing, return **PET intake incomplete**.

## Steps

### Gate 1: approve the PET checkpoint

Show tracer, acquisition, timing, attenuation, reconstruction, reference,
registration, correction, estimand, QC, output, alternatives, and claim. Gate 1
authorizes routing only.

### Gate 2: approve one bounded handoff or action

Ask the user to select the checkpoint, owner, environment, output, and verification.
Gate 2 authorizes one bounded step only; it does not authorize installation,
downloads, full pipelines, or clinical interpretation.

Return:

```text
PET Checkpoint Record
Tracer, scan, timing, decay, attenuation, and reconstruction:
Structural reference, registration, reference region, and correction:
SUVR or kinetic estimand, units, QC, and provenance:
Handoff, output, verification, and permitted claim:
Stop point:
```

## Boundaries

Method rules:

- Preserve tracer, scan, timing, decay, attenuation, reconstruction, and
  units. Do not infer tracer or reference region from filenames.
- Separate registration, partial-volume, reference-region, SUVR, and kinetic
  decisions; expose assumptions and sensitivity rather than universal defaults.
- Keep regional values and units explicit. A PET signal is not a diagnosis or
  proof of pathology without a separate validated design.
- Route implementation to separately approved adapters; category membership does
  not authorize chaining.

Stop for missing tracer, timing, units, reference region, registration, or
estimand; clinical use; unapproved correction; unavailable owner or environment;
a request to install, download, run a full pipeline, or interpret PET clinically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
