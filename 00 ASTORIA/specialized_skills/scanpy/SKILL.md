---
name: scanpy
description: >-
  Routes and implements one approved single-cell RNA-seq analysis checkpoint
  through an available verified Scanpy environment while preserving assay
  identity, QC, normalization, representation, splits, seeds, outputs, and
  interpretation boundaries. Triggers: analyze single cell data with Scanpy,
  scanpy clustering checkpoint.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, Scanpy
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Scanpy

Handle one approved single-cell analysis checkpoint without silently running a
full pipeline or converting an embedding into cell-type truth.

## Purpose

This is a conditional Part 4 single-cell workflow adapter. It separates input
and assay audit, QC, normalization, feature selection, representation,
neighbors, embedding, clustering, marker analysis, trajectory, and export.
It records versions, parameters, seeds, data state, and provenance, but does
not choose a biological question, QC thresholds, normalization, clustering,
annotation, or claim.

The user owns the estimand, assay, population, QC, normalization, model, labels,
and interpretation. [anndata](../anndata/SKILL.md) owns object structure and I/O. [cogsci-statistics](../cogsci-statistics/SKILL.md)
owns inferential decisions outside the adapter.

Activate only for exact `scanpy` or an approved handoff naming one checkpoint.
Do not trigger from generic single-cell, scRNA-seq, UMAP, clustering, or cell-
type requests. In scope: one QC, normalization, representation, neighbor,
embedding, clustering, marker, trajectory, or export operation. Out of scope:
automatic end-to-end pipelines, downloads, installs, clinical annotation, and
biological interpretation.

## Inputs

Obtain or mark missing: assay and count meaning, observation and gene units,
sample and batch structure, object state, QC fields, normalization, feature
selection, representation, operation, seed, split or cross-validation boundary,
environment, output, and claim. If assay meaning, checkpoint, or claim is
missing, return **Scanpy intake incomplete**.

## Steps

### Gate 1: approve the single-cell checkpoint

Show assay, object state, population and batch structure, checkpoint, QC and
normalization candidates, representation, parameters, seed, output, validation,
and claim. Gate 1 authorizes a method plan only.

### Gate 2: approve one bounded action

Ask the user to select the exact checkpoint, environment, parameters, output, and
verification. Gate 2 authorizes one action only. It does not authorize a full
pipeline, downloads, installs, unbounded clustering, annotation, or overwrites.

Return:

```text
Scanpy Checkpoint Record
Assay, object, observation, and gene units:
QC, filtering, normalization, and representation:
Operation, parameters, seed, and dependence:
Environment, output, and verification:
Sensitivity and biological-interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Keep raw counts, normalized layers, and transformed representations separate.
  Never infer counts from a layer name or overwrite source data.
- Make QC thresholds, mitochondrial or ribosomal features, filtering grain,
  normalization target, highly variable gene method, scaling, and regressors
  explicit and outcome-blind.
- Preserve sample, donor, batch, repeated-cell, and technical-dependence
  structure. Do not treat cells as independent biological replicates.
- Record neighbors, metric, embedding, clustering algorithm, resolution,
  random seed, and sensitivity. A UMAP or cluster is descriptive unless a
  separate inferential design supports the claim.
- Marker and trajectory outputs require prespecified contrasts, uncertainty,
  validation, and alternative explanations; do not auto-annotate cell types.

Stop for unknown assay or layer meaning; cells treated as independent donors;
outcome-dependent QC or clustering; missing batch or sample structure;
automatic cell-type annotation; unavailable environment; a request to install,
download, run a full pipeline, overwrite, or interpret clusters as biological
truth.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- scverse. (n.d.). *Scanpy documentation*. https://scanpy.readthedocs.io/en/stable/
