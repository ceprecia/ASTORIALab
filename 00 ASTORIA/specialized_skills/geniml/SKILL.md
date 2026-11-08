---
name: geniml
description: >-
  Implements one approved genomic-interval embedding, universe, or region-ML
  operation through an already available verified environment while preserving
  interval identity, genome build, labels, splits, leakage, seeds, outputs, and
  interpretation boundaries. Triggers: genomic interval embeddings with geniml.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, geniml
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Geniml

Implement one approved genomic-interval machine-learning checkpoint without
silently choosing a universe, embedding, split, or biological interpretation.

## Purpose

This conditional Part 4 data/model adapter audits BED or interval identity,
genome build, coordinate and strand conventions, universe, labels, embedding or
region operation, train/test grouping, seed, model, output, and provenance. It
does not choose the genomic question, feature representation, model, or claim.

The user owns the estimand, intervals, universe, labels, model, split, and claim.
[polars-bio](../polars-bio/SKILL.md) owns interval operations; [scikit-learn](../scikit-learn/SKILL.md) owns selected generic
ML operations.

Activate only for exact `geniml` or an approved handoff naming one genomic-
interval operation. Do not trigger from generic BED, embedding, chromatin, or
machine-learning requests. Out of scope: automatic region labeling, downloads,
installs, unbounded search, and biological interpretation.

## Inputs

Obtain or mark missing: interval source and build, coordinate and strand,
universe, labels, operation, embedding or model, split and grouping, seed,
environment, output, and claim. If build, interval unit, labels, or split is
missing, return **geniml intake incomplete**.

## Steps

### Gate 1: approve the interval-ML checkpoint

Show build, intervals, universe, labels, operation, representation, split,
seed, validation, output, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installs, downloads,
unbounded tuning, or interpretation.

Return:

```text
Geniml Operation Record
Genome build, intervals, coordinates, strand, and universe:
Labels, representation, model, split, grouping, and seed:
Environment, output, sensitivity, and verification:
Interpretation and leakage limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Validate build, coordinate convention, interval identity, overlaps, and
  universe before embedding or ML.
- Split by biological sample, donor, region collection, or other approved
  dependence group; do not let overlapping or neighboring intervals leak.
- Record representation, metric, parameters, seed, missingness, and sensitivity.
  An embedding or similarity is not a functional annotation or mechanism.
- Preserve source intervals and output provenance; do not download references or
  install optional ML backends.

Stop for build or coordinate mismatch; ambiguous interval unit; overlapping
train/test regions; missing labels; unavailable environment; a request to
install, download, auto-label, tune unboundedly, or interpret embeddings
biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Sheffield Computational Biology Lab. (n.d.). *Geniml documentation*. BEDbase. https://docs.bedbase.org/geniml/
