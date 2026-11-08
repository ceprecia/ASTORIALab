---
name: scvi-tools
description: >-
  Implements one approved scvi-tools single-cell probabilistic-model operation
  through an already available verified environment while preserving assay,
  model, batch, training, diagnostics, split, checkpoint, output, and claim
  boundaries. Triggers: scvi-tools model on my single cell data.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, scvi-tools
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# scvi-tools

Implement one approved single-cell probabilistic-model checkpoint without
silently choosing a model, batch variable, training regime, or interpretation.

## Purpose

This is a conditional Part 4 probabilistic single-cell adapter. It audits
AnnData setup, assay and count semantics, model namespace, batch and covariate
fields, likelihood, latent representation, training settings, seeds,
diagnostics, checkpoints, held-out boundaries, and output provenance. It does
not choose the model, covariates, priors, target, or biological claim.

The user owns the estimand, model, assay, batch variables, training, comparison,
and claim. [scanpy](../scanpy/SKILL.md) owns standard single-cell checkpoints; [pymc](../pymc/SKILL.md) owns
general Bayesian model implementation.

Activate only for exact `scvi-tools` or an approved handoff naming one model
checkpoint. Do not trigger from generic batch correction, latent space,
single-cell, or differential-expression requests. In scope: one selected scVI,
scANVI, totalVI, MultiVI, or explicitly named model setup, training, inference,
or export. Out of scope: automatic model selection, full pipelines, downloads,
installs, and biological interpretation.

## Inputs

Obtain or mark missing: assay and count meaning, AnnData identity, model and
namespace, observed covariates, batch and label fields, likelihood, train and
held-out scope, seed, training settings, diagnostics, checkpoint, output, and
claim. If model, assay, covariates, or held-out boundary is missing, return
**scvi-tools intake incomplete**.

## Steps

### Gate 1: approve the probabilistic-model checkpoint

Show assay and counts, AnnData state, model and namespace, covariates, batch and
labels, likelihood, split, training settings, diagnostics, checkpoint, output,
and claim. Gate 1 authorizes a method plan only.

### Gate 2: approve one bounded action

Ask the user to select the exact model, environment, training or inference action,
checkpoint, output, and verification. Gate 2 authorizes one action only. It
does not authorize installation, downloading, unbounded tuning, or biological
interpretation.

Return:

```text
scvi-tools Implementation Record
Assay, counts, AnnData, and covariates:
Model namespace, likelihood, and batch fields:
Split, seed, training settings, and environment:
Diagnostics, checkpoint, output, and verification:
Sensitivity and biological-interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Verify the exact model namespace and version. Similar model names can refer
  to different likelihoods and data contracts.
- Keep raw counts and model inputs distinct; do not use normalized values when
  the selected model expects counts without an explicit approved reason.
- Record batch, donor, condition, and label fields. Batch correction is not
  automatically desirable, complete, or evidence of biological validity.
- Preserve held-out or validation boundaries and record seed, training epochs,
  learning settings, hardware, and checkpoint identity.
- Require convergence or training diagnostics, reconstruction or predictive
  checks, sensitivity to batch and covariate choices, and neutral reporting.
  Latent dimensions, differential-expression outputs, and transfers are not
  automatically biological discoveries.

Stop for unknown count semantics; model or namespace ambiguity; batch or donor
confounding; held-out leakage; failed diagnostics; unavailable environment; a
request to install, download, run a full pipeline, or choose a model; or a
request to interpret latent space, corrected expression, or transferred labels
as biological truth.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- scvi-tools developers. (n.d.). *scvi-tools documentation*. https://docs.scvi-tools.org/en/stable/
