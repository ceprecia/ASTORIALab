---
name: umap-learn
description: >-
  Implements one approved UMAP dimensionality-reduction operation through an
  already available verified environment while preserving feature, metric,
  split, seed, sensitivity, leakage, and interpretation boundaries. Triggers:
  reduce dimensions with UMAP, UMAP embedding.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, umap-learn
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# UMAP Learn

Implement one approved UMAP embedding or transform without treating a visible
cluster as a confirmed group or selecting parameters from the outcome.

## Purpose

This is a conditional Part 4 software adapter for one approved UMAP operation.
It owns API and environment checks, feature and metric audit, fit/transform
boundaries, seed recording, sensitivity plan, and neutral output verification.
It does not choose the scientific representation, tune from outcomes, fit
against a sealed test set, or interpret geometry as a discovered population.

The user owns the estimand, features, distance metric, parameters, split, seed,
comparison, and claim. [exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns structure inspection;
[scikit-learn](../scikit-learn/SKILL.md) owns a selected classical ML pipeline.

Activate only for exact `umap-learn` or an approved handoff naming the input
matrix, operation, metric, and output use. Do not trigger from generic
embedding, clustering, visualization, or dimensionality-reduction requests.

In scope: unsupervised, supervised, semi-supervised, DensMAP, aligned, or
parametric UMAP only when the user selects the variant. Out of scope: automatic
clustering, causal interpretation, biomarker claims, data download, package
installation, and treating a 2D plot as inferential evidence.

## Inputs

Obtain or mark missing: source and feature provenance, row and prediction unit,
missingness, preprocessing, metric, UMAP variant, `n_neighbors`, `min_dist`,
components, seed, train/test or cross-fitting boundary, supervision labels,
compute and version, sensitivity grid, output path, collision policy, and
permitted claim. If feature meaning, metric, fit scope, or claim is missing,
return **UMAP intake incomplete**.

## Steps

### Gate 1: approve the embedding boundary

Show source, unit, features, preprocessing, metric, UMAP variant, parameters,
fit scope, seed, sensitivity plan, downstream use, limitations, and claim.
Gate 1 authorizes a method specification only.

### Gate 2: approve one implementation action

Ask the user to select the operation, exact environment, bounded parameter set,
sensitivity grid, exact output files and destinations, collision policy,
verification, and permitted claim. Gate 2 authorizes one action through an
existing environment and only the enumerated new output writes. A chat-only
action creates no files. It does not authorize installation, download,
unbounded tuning, sealed-test access, additional writes, overwrites, or
interpretation.

Return:

```text
UMAP Implementation Record
Source and row unit:
Features, preprocessing, and metric:
Variant and parameters:
Fit scope, seed, and sensitivity grid:
Environment and API:
Output and verification:
Stability and interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Match preprocessing to the selected metric. Never standardize, impute, or
  encode silently.
- Record all parameters and seeds. Compare a bounded prespecified sensitivity
  set across seeds, neighborhood scales, metrics, preprocessing, and
  components when geometry is used for a scientific claim.
- Fit transforms only on the approved training scope. Do not leak labels,
  held-out observations, repeated measures, or future data into construction.
- Distances and apparent clusters are embedding-dependent. A visible group is
  not a confirmed cluster, class, mechanism, or biological subtype.
- Report instability, disconnected components, metric mismatch, missingness,
  and sensitivity results before any downstream use.

Stop for missing feature meaning or metric; outcome-dependent parameter search;
label leakage or mixed train/test fitting; absent sensitivity for a cluster or
group claim; unavailable package or incompatible environment; a request to
install, download, or overwrite; or a request to treat visible clusters as
confirmed groups.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- McInnes, L., Healy, J., & Melville, J. (2018). *UMAP: Uniform manifold approximation and projection for dimension reduction*. arXiv. https://arxiv.org/abs/1802.03426
- UMAP developers. (n.d.). *UMAP-learn documentation and API reference*. https://umap-learn.readthedocs.io/en/latest/
