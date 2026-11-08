---
name: pathml
description: >-
  Implements one approved computational-pathology preprocessing, feature, or
  model operation through an already available verified environment while
  preserving slide and cohort identity, tiling, labels, splits, leakage,
  checkpoints, outputs, and clinical-interpretation boundaries. Triggers:
  computational pathology with PathML.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: pathology
  dependencies: ""
  requires: Python, PathML
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-11-02"
---

# PathML

Implement one approved pathology-imaging checkpoint without silently selecting
a model, label, tile policy, split, or diagnostic interpretation.

## Purpose

This conditional Part 4 pathology-imaging adapter audits slide and cohort
identity, stain and scale, tiles, labels, augmentations, train/validation/test
splits, patient dependence, model or feature operation, checkpoints, metrics,
outputs, and provenance. It does not choose the target, architecture, labels,
thresholds, or clinical claim.

The user owns the scientific target, cohort, labels, tiles, model, split, metrics,
and claim. [histolab](../histolab/SKILL.md) owns slide preparation; [pytorch-lightning](../pytorch-lightning/SKILL.md) owns
selected training orchestration.

Activate only for exact `pathml` or an approved handoff naming one operation.
Do not trigger from generic pathology, histology, classification, or diagnosis
requests. In scope: one preprocessing, tile, feature, augmentation, model,
or evaluation operation. Out of scope: automatic diagnosis, patient-level
label inference, downloads, installs, and end-to-end pipelines.

## Inputs

Obtain or mark missing: slide and patient identity, stain, scale, tile policy,
label provenance, cohort and class balance, split and grouping, operation,
model, checkpoint, metrics, environment, output, and claim. If patient unit,
label provenance, or split is missing, return **PathML intake incomplete**.

## Steps

### Gate 1: approve the pathology operation

Show cohort, patient unit, labels, slide and tile identity, stain, scale,
operation, model, split, metrics, checkpoint, output, validation, and claim.
Gate 1 authorizes a method plan only.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installs, downloads,
unbounded tuning, patient-level inference, overwrites, or diagnosis.

Return:

```text
PathML Operation Record
Cohort, patient unit, slides, stains, and labels:
Tiles, splits, augmentations, model, and checkpoint:
Environment, metrics, output, and verification:
Leakage, external-validity, and clinical-use limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Split by patient or biological unit before tiling or augmentation. Never let
  tiles from one patient cross train and test partitions.
- Preserve slide, tile coordinates, stain, scanner, and label provenance. Do
  not infer labels from filenames or directories.
- Make augmentation, normalization, class weighting, sampling, checkpoint,
  metric, and threshold choices explicit and outcome-blind.
- Treat tile-level predictions and attention as model outputs, not diagnoses,
  biomarkers, or causal explanations. Patient-level aggregation and external
  validation must match the approved research estimand; neither authorizes
  clinical interpretation or patient care.

Stop for missing label provenance or patient unit; tile leakage; unknown stain
or scale; unapproved model or threshold; failed external validation; unavailable
environment; a request to install, download, diagnose, or interpret tile output
clinically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- PathML developers. (n.d.). *PathML documentation*. https://pathml.readthedocs.io/en/latest/
