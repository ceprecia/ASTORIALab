---
name: pytorch-lightning
description: >-
  Implements one approved PyTorch Lightning training or evaluation operation
  through an already available verified environment while preserving data
  splits, seeds, devices, checkpoints, logging, resource, write, and claim
  boundaries. Triggers: train this model with PyTorch Lightning, Lightning
  training loop.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, PyTorch Lightning
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# PyTorch Lightning

Implement one approved Lightning operation without importing a training stack,
downloading data, or silently changing the scientific pipeline.

## Purpose

This is a conditional Part 4 software adapter for one approved Lightning
operation. It audits the selected module or data module, train/validation/test
partitions, callbacks, strategy, precision, device, seed, checkpoint,
reproducibility, resource, logging, and output state. It does not choose the
network, loss, split, optimizer, stopping rule, or interpretation.

The user owns the task, target, architecture, loss, split, metrics, tuning, compute,
and claim. [scikit-learn](../scikit-learn/SKILL.md) owns a selected classical ML adapter;
[torch-geometric](../torch-geometric/SKILL.md) owns a selected graph-learning operation.

Activate only for exact `pytorch-lightning` or an approved handoff naming one
Lightning operation. Do not trigger from generic deep learning, PyTorch, GPU,
or model-training requests.

In scope: one existing LightningModule or LightningDataModule operation,
checkpoint evaluation, structure-only validation, or one approved training run
when separately authorized. Out of scope: package installation, data download,
unbounded tuning, automatic architecture selection, remote logging, and
clinical or scientific interpretation.

## Inputs

Obtain or mark missing: source and target, module and data-module identity,
partitions, preprocessing, loss and metrics, seed, device and precision,
strategy, callbacks, checkpoint, logger and network state, resource limit,
output path, test-set seal, and permitted claim. If partitions, module,
environment, or write boundary is missing, return **Lightning intake
incomplete**.

## Steps

### Gate 1: approve the Lightning operation

Show module, data, partitions, target, loss, metrics, seed, device, precision,
strategy, callbacks, checkpoint, resource, logger, output, verification, and
claim. Gate 1 authorizes an implementation plan only.

### Gate 2: approve one execution or structure check

Ask the user to select the exact environment, operation, compute, output, and
verification. Gate 2 authorizes one bounded action only. It does not authorize
installation, downloading, remote logging, unsealed test access, overwrites,
or later training steps.

Return:

```text
PyTorch Lightning Implementation Record
Module and data-module:
Target, loss, metrics, and partitions:
Seed, device, precision, and strategy:
Callbacks, checkpoint, and logger:
Environment and resource state:
Output, verification, and failure state:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Verify Python, PyTorch, Lightning, CUDA or accelerator, and callback versions
  without installing or upgrading them.
- Preserve train, validation, and sealed-test separation. Validation metrics
  may guide epoch, hyperparameter, or checkpoint selection only under the
  approved selection and stopping rules. Sealed-test metrics must not guide
  those choices.
- Record every seed and deterministic setting; report when hardware or kernels
  prevent deterministic reproduction.
- Treat automatic checkpointing, early stopping, gradient accumulation,
  mixed precision, distributed strategies, and loggers as explicit choices,
  not harmless defaults.
- Do not send data or credentials to W&B, MLflow, Comet, or a remote service
  without a separately approved external-write action.

Stop for missing partitions or target; unavailable or version-incompatible
environment; test leakage; unapproved checkpoint or early-stopping choice;
remote logging or credentials; a request to install, download, tune, or
overwrite; or a request to interpret model output.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Lightning AI. (n.d.-a). *Early stopping*. PyTorch Lightning documentation. https://lightning.ai/docs/pytorch/stable/common/early_stopping.html
- Lightning AI. (n.d.-b). *PyTorch Lightning documentation*. https://lightning.ai/docs/pytorch/stable/
