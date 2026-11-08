---
name: torch-geometric
description: >-
  Implements one approved graph-learning operation through an already available,
  version-verified PyTorch Geometric environment while preserving node and edge
  meaning, graph construction, partitions, leakage, seeds, resources, writes,
  and claim boundaries. Triggers: graph learning with PyTorch Geometric, GNN on
  my graph data.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, PyTorch Geometric
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# PyTorch Geometric

Implement one approved graph-learning operation without silently changing the
graph, downloading datasets, or treating model output as causal structure.

## Purpose

This is a conditional Part 4 graph-learning adapter. It audits graph type,
node and edge semantics, ordering, features, labels, batching, masks, model
operation, split, sampling, seed, device, extension versions, checkpoints,
and neutral verification. It does not choose the graph representation, model,
target, split, or scientific interpretation.

The user owns graph construction, estimand, architecture, target, partitions,
metrics, tuning, and claim. [networkx](../networkx/SKILL.md) owns a selected descriptive graph
operation. [pytorch-lightning](../pytorch-lightning/SKILL.md) owns a selected training orchestration action.

Activate only for exact `torch-geometric` or an approved handoff naming one
graph-learning operation. Do not trigger from generic graph analysis, PyTorch,
or network requests.

In scope: one node, edge, graph, heterogeneous-graph, message-passing, or
sampling operation when explicitly selected. Out of scope: automatic dataset
downloads, graph construction from ambiguous tables, unbounded architecture or
hyperparameter search, test leakage, package installation, and causal claims.

## Inputs

Obtain or mark missing: graph population and unit, node and edge meaning,
direction, weights and signedness, ordering, features, labels, masks, missing
nodes or edges, operation, architecture, train/validation/test split, sampler,
seed, PyTorch/PyG/CUDA versions, extensions, checkpoint, output, and claim. If
node or edge semantics, split, or environment is missing, return **PyG intake
incomplete**.

## Steps

### Gate 1: approve the graph operation

Show graph semantics, target unit, features, operation, architecture, masks,
partitions, sampling, seed, environment, resources, checkpoint, output,
verification, and claim. Gate 1 authorizes an implementation plan only.

### Gate 2: approve one execution or structure check

Ask the user to select the exact operation, environment, compute, output, and
verification. Gate 2 authorizes one bounded action only. It does not authorize
downloads, installs, unbounded tuning, sealed-test access, overwrites, or
interpretation.

Return:

```text
PyG Implementation Record
Graph and target unit:
Node, edge, feature, label, and ordering audit:
Operation, architecture, and masks:
Partitions, sampler, seed, and environment:
Checkpoint, output, and verification:
Leakage and interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Validate `edge_index` orientation, node ordering, graph IDs, self-loops,
  duplicate edges, isolated nodes, and heterogeneous type keys before execution.
- Preserve graph-level, node-level, and edge-level target units. Do not infer
  subject or ROI meaning from tensor shape.
- Keep learned preprocessing, normalization, neighbor sampling, and masks
  inside the approved training scope. Validation metrics may guide bounded
  tuning under the approved design; they do not authorize changing graph
  construction. Keep sealed-test labels and metrics out of graph construction
  and tuning. Any permitted use of unlabeled held-out graph structure must be
  explicit in the approved inductive or transductive design.
- Record PyTorch, PyG, CUDA, and optional extension versions. Do not install
  or fetch wheels to repair incompatibility.
- A learned edge weight, attention coefficient, or embedding is not a causal
  edge, biomarker, or explanation without a separate validation design.

Stop for ambiguous graph semantics or ordering; target or partition leakage;
missing environment or incompatible extension; unapproved dataset fetch or
installation; graph construction inferred from ambiguous tables; unbounded
tuning; or a request to interpret learned graph weights as causal structure.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- PyG developers. (n.d.). *PyTorch Geometric documentation*. https://pytorch-geometric.readthedocs.io/en/latest/
