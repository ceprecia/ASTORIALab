---
name: anndata
description: >-
  Performs one approved annotated-matrix structure, I/O, subset, or metadata
  operation through an already available verified AnnData environment while
  preserving observation and variable identity, layers, provenance, memory,
  writes, and claim boundaries. Triggers: AnnData structure or subset operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, AnnData
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# AnnData

Operate on one approved annotated matrix without silently changing axes,
layers, metadata, sparse semantics, or analysis meaning.

## Purpose

This is a conditional Part 4 data-structure adapter. It audits `X`, `obs`,
`var`, `layers`, `obsm`, `varm`, `obsp`, `varp`, `uns`, indices, backed mode,
format, versions, and round-trip behavior. It does not choose QC, normalization,
clustering, modeling, biological annotation, or biological interpretation.

The user owns the object contract, axis identity, operation, memory mode, output,
and claim. [scanpy](../scanpy/SKILL.md) owns selected single-cell analysis; [zarr-python](../zarr-python/SKILL.md) owns
selected store operations.

Activate only for exact `anndata` or an approved handoff naming one object or
I/O operation. Do not trigger from generic single-cell, h5ad, or genomics
analysis requests. In scope: read, inspect, subset, concatenate, attach or edit
explicitly supplied metadata, convert, or write one selected object. Out of
scope: automatic filtering, normalization, integration, clustering, downloads,
installs, and interpretation.

## Inputs

Obtain or mark missing: source and format, observation and variable units,
indices and ordering, `X` type and shape, layers, annotations, sparse/backed
mode, operation, memory limit, version, output path, overwrite policy, and
claim. If axis identity, source, or write boundary is missing, return
**AnnData intake incomplete**.

## Steps

### Gate 1: approve the object operation

Show source, format, axes, layers, annotations, operation, memory mode,
versions, output, collision policy, round-trip checks, and claim. Gate 1
authorizes a structure plan only.

### Gate 2: approve one bounded action

Ask the user to select the exact object, operation, environment, output, and
verification. Gate 2 authorizes one action only. It does not authorize analysis,
installation, downloads, or overwrites.

Return:

```text
AnnData Operation Record
Source, format, version, and object shape:
Observation and variable identity:
X, layers, annotations, and sparse/backed state:
Operation and collision policy:
Output, round-trip verification, and warnings:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Verify that `obs` and `var` indices are unique, stable, and aligned with
  every layer and matrix annotation before subsetting or concatenating.
- Preserve raw counts, normalized data, and derived layers as distinct. Never
  overwrite `X` or infer that a layer is counts from its name.
- Record sparse versus dense and backed versus in-memory behavior; do not
  materialize a large object silently.
- Make join, batch, category, missing-value, and duplicate-index policies
  explicit. A successful write does not prove semantic preservation.
- Attach or edit only the approved supplied metadata fields with verified axis
  keys and alignment. Do not infer cell types, gene function, or other
  biological annotations.
- Validate a bounded round trip and report unsupported or lossy fields before
  writing. Do not install optional I/O dependencies.

Stop for duplicate or ambiguous axes; unknown layer meaning; hidden
materialization; lossy or unverified conversion; unavailable environment; a
request to filter, normalize, cluster, infer biological annotations, install,
download, or overwrite; or a request to interpret object contents scientifically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- scverse. (n.d.). *AnnData documentation*. https://anndata.readthedocs.io/en/stable/
