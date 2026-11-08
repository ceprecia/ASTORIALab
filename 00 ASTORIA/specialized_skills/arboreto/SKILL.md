---
name: arboreto
description: >-
  Implements one approved exploratory gene-regulatory-network inference
  operation through an already available verified environment while preserving
  expression unit, transcription-factor list, observation dependence, null or
  validation plan, compute, outputs, and noncausal-claim boundaries. Triggers:
  infer a gene regulatory network with Arboreto.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, Arboreto
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Arboreto

Perform one approved exploratory GRN inference without treating tree-based
importance scores as regulatory edges or causal mechanisms.

## Purpose

This conditional Part 4 genomics adapter audits expression matrix orientation,
observation and gene units, preprocessing, candidate transcription factors,
algorithm, seeds, parallelism, validation, null, output, and provenance. It
does not choose the regulatory question, TF list, model, threshold, or claim.

The user owns the expression contract, TF set, algorithm, validation, and claim.
[scanpy](../scanpy/SKILL.md) owns single-cell preprocessing; [pydeseq2](../pydeseq2/SKILL.md) owns selected bulk
expression analysis.

Activate only for exact `arboreto` or an approved handoff naming one GRN
operation. Do not trigger from generic gene regulation, network, expression, or
transcriptomics requests. Out of scope: causal claims, automatic TF selection,
cluster deployment, installs, downloads, and interpretation.

## Inputs

Obtain or mark missing: expression scale and orientation, sample/cell unit,
batch and donor structure, TF list, algorithm, preprocessing, seed, compute,
validation or null, output, and claim. If expression semantics, TF list, or
validation is missing, return **Arboreto intake incomplete**.

## Steps

### Gate 1: approve the GRN specification

Show expression unit, TF list, algorithm, preprocessing, grouping, seed,
compute, validation, null, output, and claim. Gate 1 authorizes method review.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, compute, output, and
verification. Gate 2 authorizes one action only; it does not authorize installs,
downloads, cluster submission, automatic TF choice, or interpretation.

Return:

```text
Arboreto GRN Operation Record
Expression unit, orientation, preprocessing, and TF list:
Algorithm, seed, grouping, parallelism, and resources:
Validation, null, stability, output, and provenance:
Exploratory and noncausal interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve raw and transformed expression semantics; do not infer counts or
  normalization from column names.
- Group or split by biological unit to avoid donor, batch, or repeated-cell
  leakage. Candidate TFs and targets are scientific decisions.
- Record algorithm, seed, parallel workers, missingness, importance scale,
  thresholding, null or permutation, and stability across resamples.
- GRN edges are exploratory associations under the selected model, not evidence
  of regulation, direction, causality, or mechanism.

Stop for unknown expression scale; missing TF list or biological grouping;
batch/donor leakage; unvalidated importance thresholds; unavailable
environment; a request to install, download, deploy, infer causality, or call
edges regulatory facts.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Arboreto developers. (n.d.). *Arboreto documentation*. https://arboreto.readthedocs.io/en/latest/
- Moerman, T., Aibar Santos, S., Bravo González-Blas, C., Simm, J., Moreau, Y., Aerts, J., & Aerts, S. (2019). GRNBoost2 and Arboreto: Efficient and scalable inference of gene regulatory networks. *Bioinformatics, 35*(12), 2159–2161. https://doi.org/10.1093/bioinformatics/bty916
