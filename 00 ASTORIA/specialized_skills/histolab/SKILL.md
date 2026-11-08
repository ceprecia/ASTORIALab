---
name: histolab
description: >-
  Performs one approved histology-slide tiling, region, thumbnail, or
  preprocessing operation through an already available verified environment
  while preserving slide identity, scale, stain, coordinates, tile provenance,
  outputs, and clinical-interpretation boundaries. Triggers: tile histology
  slides with histolab.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: pathology
  dependencies: ""
  requires: Python, histolab, whole-slide images
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Histolab

Perform one approved whole-slide image preparation operation without silently
changing scale, stain, regions, or diagnostic meaning.

## Purpose

This conditional Part 4 pathology-imaging adapter audits slide format,
scanner metadata, magnification, stain, coordinate system, tissue mask, tile
size and overlap, region selection, color transforms, output, and provenance.
It does not choose a diagnostic target, segmentation, classifier, threshold,
or clinical interpretation.

The user owns the operation, slide cohort, scale, stain, regions, output, and
claim. [pathml](../pathml/SKILL.md) owns selected pathology-model operations.

Activate only for exact `histolab` or an approved handoff naming one slide
operation. Do not trigger from generic pathology, histology, microscopy, or
diagnosis requests. In scope: inspect, thumbnail, tissue mask, tile, crop,
stain, or bounded export operation. Out of scope: diagnosis, automatic tissue
classification, downloads, installs, and clinical interpretation.

## Inputs

Obtain or mark missing: slide identity and format, scanner and magnification,
pixel spacing, stain, tissue and background policy, coordinate system, tile
size/overlap, region, operation, environment, output, collision policy, and
claim. If scale, region, or slide identity is missing, return **Histolab intake
incomplete**.

## Steps

### Gate 1: approve the slide operation

Show slide, scanner, scale, stain, coordinates, tissue policy, tile or region,
operation, output, verification, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installation,
downloads, classification, overwrite, or clinical interpretation.

Return:

```text
Histolab Operation Record
Slide, scanner, scale, stain, and coordinate system:
Tissue, region, tile, overlap, and transform choices:
Environment, output, provenance, and verification:
Limitations and clinical-use boundary:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve original slide identity, pyramid level, physical scale, orientation,
  coordinate system, stain, and scanner metadata.
- Make tissue-mask, background, tile, overlap, and stain-transform choices
  explicit and outcome-blind. Do not infer tissue from thumbnail appearance.
- Keep tile provenance to slide, level, coordinates, and preprocessing. Never
  overwrite the source slide or silently drop tiles.
- A tile, stain normalization, or visual crop is not a diagnosis or biomarker.

Stop for missing slide or scale metadata; coordinate mismatch; unreviewed stain
or tissue transform; failed tile provenance; unavailable environment; a request
to install, download, classify, diagnose, overwrite, or interpret tiles
clinically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- histolab developers. (n.d.). *histolab documentation*. https://histolab.readthedocs.io/en/latest/
