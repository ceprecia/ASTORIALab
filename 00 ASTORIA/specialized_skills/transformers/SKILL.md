---
name: transformers
description: >-
  Implements one approved local or cached Hugging Face Transformers model
  operation while preserving model identity, tokenizer, data, splits, license,
  network, credentials, resources, writes, and claim boundaries. Triggers: run a
  Hugging Face model locally, transformers model operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, transformers, a cached model
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Transformers

Implement one approved model operation without silently fetching a checkpoint,
trusting remote code, or treating output as validated scientific evidence.

## Purpose

This conditional Part 4 adapter audits model and tokenizer identity, immutable
revision, task, inputs, preprocessing, labels, partitions, checkpoint
provenance, license, remote-code state, credentials, device, seed, resources,
outputs, and verification. It does not choose a model, task, prompt, training
design, or scientific claim.

The user owns the task, target, model, revision, tokenizer, split, metrics,
evaluation, and claim. [pytorch-lightning](../pytorch-lightning/SKILL.md) owns separately selected
Lightning training orchestration; this adapter owns the selected Transformers
model and tokenizer operation.

Activate only for exact `transformers` or an approved handoff naming one local
or cached model operation. Do not trigger from generic language-model,
embedding, AI, or NLP requests. In scope: one load, tokenization, inference,
or fine-tuning operation when explicitly selected. Out of scope: model
selection, unbounded Hub search, gated access without approval, remote-code
execution, package installation, and claims about validity from output alone.

## Inputs

Obtain or mark missing: model ID and immutable revision, tokenizer or processor,
task and target, input schema, preprocessing, labels, split, checkpoint
provenance, license, network and credential state, `trust_remote_code`, device,
seed, resources, output, and claim. If model identity, revision, license, task,
or data boundary is missing, return **Transformers intake incomplete**. For
fine-tuning, also require the approved objective, optimizer, learning schedule,
bounded training steps or epochs, validation and stopping rule, sealed-test
boundary, and checkpoint destinations.

## Steps

### Gate 1: approve the model operation

Show model and revision, task, tokenizer, inputs, labels, license, network,
credentials, remote-code state, split, device, parameters, output,
verification, and claim. Gate 1 authorizes review only.

### Gate 2: approve one bounded action

Ask the user to select the exact snapshot, operation, environment, network state,
resources, output files and destinations, and verification. Gate 2 authorizes
only that selected action. When fine-tuning is selected, it includes only the
displayed bounded training specification and checkpoint writes. It does not
authorize downloads, login, remote code, unbounded search, additional training
runs or epochs beyond that specification, or overwrites.

Return:

```text
Transformers Implementation Record
Model, revision, tokenizer, and license:
Task, inputs, labels, and preprocessing:
Network, credentials, and remote-code state:
Split, device, seed, and resource state:
Approved training and checkpoint state, when applicable:
Output and verification:
Limitations and permitted claim:
```

## Boundaries

Method rules:

- Verify the exact model snapshot, tokenizer, configuration, weights, and
  license. A model name is not an immutable identity.
- Keep Hub access off unless the user separately approves bounded network access;
  never expose or print tokens.
- Treat `trust_remote_code=True` as a high-risk review requiring source
  inspection; default to false.
- Preserve train, validation, and sealed-test separation. Record truncation,
  padding, label mapping, sampling, and preprocessing exactly.
- Record seed, device, dtype, batch size, decoding settings, and resource use.
  Output is an execution artifact, not a scientific conclusion.

Stop for mutable or unknown model identity; missing license; gated access or
credentials; unreviewed remote code; train/test leakage; unavailable snapshot
or environment; a request to install, download, login, or search unboundedly;
or a request to interpret model output as validated evidence.
- Check the installed Transformers version and the model card before each approved operation.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Hugging Face. (n.d.-a). *Hugging Face Hub documentation*. https://huggingface.co/docs/hub/index
- Hugging Face. (n.d.-b). *Transformers documentation*. https://huggingface.co/docs/transformers/index
