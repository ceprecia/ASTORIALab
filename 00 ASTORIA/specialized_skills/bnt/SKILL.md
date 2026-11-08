---
name: bnt
description: >-
  Implements one already selected Brain Network Transformer
  binary-classification checkpoint on fixed, ordered, dense ROI
  functional-connectivity matrices through either an explicitly labeled
  source-reproduction route or a separately approved evaluation-safe adaptation
  of one exact official source state. Use when the request names this skill or
  run-models hands off the selected BNT card after the prediction specification
  is fixed. Triggers: run Brain Network Transformer, BNT classification on
  connectivity matrices.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: Python, PyTorch, the BNT repository, ROI connectivity matrices
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Brain Network Transformer Adapter

Implement one approved Brain Network Transformer checkpoint without confusing
source reproduction, evaluation-safe adaptation, model behavior, and
scientific evidence.

## Purpose

It preserves target, observation, atlas, node order, matrix semantics, split, leakage, validation, source-drift, architecture, CUDA, logging, write, sealed-test, verification, and interpretation boundaries without choosing BNT or a target; inheriting NeuroClaw packages or orchestration; installing software; downloading data or weights; silently changing the official architecture; treating the public training code as evaluation-safe; diagnosing a person; interpreting attention or cluster assignments as mechanism; overwriting; or chaining downstream analysis.

`bnt` owns:

- the bounded ASTORIA implementation card for the official Brain Network
  Transformer source at one exact reviewed commit;
- verification of one fixed dense ROI-by-ROI functional-connectivity input
  contract;
- explicit separation of source-faithful reproduction from an
  evaluation-safe adapted training and evaluation route;
- a reviewed patch or command plan for one approved BNT action;
- structural, partition, execution, artifact, and failure verification;
- a BNT Implementation Record and bounded handoff.

The user owns the question, hypothesis, prediction, confirmatory status, target,
observation unit, population, generalization target, data rights, atlas,
connectivity definition, diagonal convention, split, metric, baseline,
model selection, route, source modification, compute budget, outcome contact,
sealed-test release, interpretation, and claims.

[run-models](../run-models/SKILL.md) owns comparison and selection among eligible deep-model cards.
[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns the predictive estimand, split,
generalization, validation, leakage, metric, baseline, null, and claim
specification. [fmri-coordinator](../fmri-coordinator/SKILL.md) owns modality routing and an approved upstream
functional-connectivity preparation handoff. `bnt` does not select itself,
preprocess raw fMRI, or replace those owners.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `Brain Network Transformer`, `transformer`, `brain
network`, `deep learning`, `functional connectivity`, `phenotype
prediction`, `best model`, `run_models`, `fMRI`, or another broad model,
method, task, or modality phrase.

Do not use this skill to:

- decide whether a deep model or BNT is scientifically appropriate;
- formulate a target, label, split, metric, baseline, or neural claim;
- adapt BNT for regression, multiclass prediction, dynamic connectivity,
  voxelwise data, structural connectivity, multimodal fusion, or a different
  observation grain without a separate method and code review;
- accept a candidate's undocumented or incomplete reimplementation as an
  executable source;
- download ABIDE, request ABCD, access restricted data, clone a repository,
  install packages, create an environment, authenticate to Weights and
  Biases, allocate a remote GPU, or change software without separate
  authority;
- use participant labels inferred from filenames, identifiers, row order, or
  any fallback rule;
- inspect or reuse a sealed test set during preprocessing, fitting, tuning,
  checkpoint selection, threshold selection, or debugging;
- diagnose, prognose, screen, monitor, or recommend treatment for a person;
- call attention weights, soft cluster assignments, or learned embeddings
  neural mechanisms, causes, biomarkers, functional modules, or validated
  explanations.

## Exact reviewed source state

### Official source

The implementation authority is the official repository at commit
`8a588aadad0166209269fa114e5df4e42209e207`. It has no reviewed release or
tag. Preserve that state or identify and re-review a new exact state.

At the pinned commit:

- `source/models/BNT/bnt.py` consumes a dense square node-feature matrix,
  fixes four attention heads, uses a two-logit output head, and ignores the
  supplied time-series tensor inside the BNT forward method;
- the default BNT configuration uses two attention layers, no added
  positional encoding, pooling flags `[false, true]`, orthonormal cluster
  initialization, frozen cluster centers, projection assignments, and a
  final pool target of 100;
- four attention heads require the feature dimension, normally the ROI
  count, to be divisible by four;
- the official source does not implement the candidate's automatic head
  adjustment, default identity embedding, adaptive pool sizes, regression
  head, T1 fusion, or BrainGNN input layout;
- `source/__main__.py` initializes Weights and Biases and repeats the full
  training route;
- `source/training/training.py` computes test metrics in every epoch, logs
  them, and saves the final model rather than restoring the
  validation-selected checkpoint described in the paper;
- the BNT forward method accumulates pooling assignments locally but returns
  only logits; its model-level `get_cluster_centers` helper references a
  nonexistent `self.dec`; and the optional training artifact routine expects
  three model outputs that the BNT forward method does not provide;
- the repository declares version suggestions in its README but provides no
  reviewed environment lock, release artifact, pretrained weights, or
  complete portability contract.

Do not silently repair or reinterpret these facts. A change to model code,
data handling, logging, partitioning, checkpoint selection, assignment or
center exposure, or outputs is an adaptation and must be recorded as such.

### NeuroClaw candidate state

The candidate card and two bounded code files are design evidence only:

- the advertised `models/bnt/scripts/train.py` is absent from the reviewed
  NeuroClaw archive;
- its model file changes official defaults and adds adaptive heads,
  regression, identity embeddings, and different pooling behavior;
- its data adapter adds Fisher-z inversion, diagonal zeroing, optional T1
  fusion, ROI masks, edge boosts, silent sample skips, and an identifier-based
  fallback label;
- those changes are not inherited, installed, or treated as verified BNT
  behavior.

Do not use the incomplete candidate route for execution.

## Route boundary

Carry forward the user's approved BNT route if it fits the fixed
scientific and evaluation specification. Resolve any open material route choice
with the user before building the implementation contract.

### Route A: source-reproduction checkpoint

Use the exact official source to inspect or reproduce its behavior. Preserve
the code and label every deviation from the paper. Because the public
training code reads its internal test loader every epoch, that loader is a
development set, not the user's sealed test. Outputs are source-reproduction
evidence only and cannot support a confirmatory or final generalization
claim.

Visible output:

- Source Reproduction Contract
- exact commit and clean-tree record
- paper-to-code discrepancy table
- descriptive run and artifact record

Benefit: preserves what the public source actually does.

Tradeoff: preserves known evaluation, logging, randomization, portability,
and checkpoint-selection limitations.

Limitation: cannot establish evaluation-safe performance on the user's target or
sealed test.

### Route B: evaluation-safe adapted checkpoint

Preserve the selected BNT architecture while replacing the unsafe training
and evaluation harness under an explicit reviewed diff. Partition by the
approved dependence and generalization units before fitting any learned
transform; tune and select checkpoints using training and validation only;
freeze code, weights, threshold, and metric logic; then release the sealed
test once in a separately approved action.

Visible output:

- BNT Adaptation Contract
- source-to-adaptation diff and rationale
- partition and outcome-contact ledger
- one approved action record

Benefit: can implement the upstream prediction specification without
epochwise test exposure.

Tradeoff: it is an adaptation, not an exact reproduction of the public
training pipeline, and needs code review plus environment verification.

Limitation: model validity, transportability, and scientific interpretation
still depend on the data and evaluation design.

An open route permits bounded assessment in Step 2 only. Stop before
implementation until the user has selected an eligible route. Availability,
reported performance and compute access are feasibility evidence.

## Inputs

Obtain or mark missing:

- a selected-card handoff from [run-models](../run-models/SKILL.md);
- an approved Neural Decoding Method Specification or equivalent fixed
  prediction and evaluation specification;
- the user's approved source-reproduction or evaluation-safe adaptation route,
  or the open route decision to resolve before implementation;
- binary target, class ontology and order, observation key, population,
  inclusion and exclusion rules, and prohibited use;
- intended generalization target and dependence groups, including
  participant, family, site, session, acquisition, and longitudinal structure
  where applicable;
- exact dense functional-connectivity matrix provenance, estimator,
  time-series window, nuisance and denoising state, atlas, ROI count, node
  order, missing-ROI policy, symmetry rule, diagonal convention, numerical
  range, and storage layout;
- train, tuning, validation, calibration if applicable, and sealed-test
  manifests fixed by identifiers before outcome contact;
- primary metric, uncertainty unit, threshold and calibration policy,
  baseline, null when applicable, subgroup plan, negative controls,
  multiplicity, and acceptance criteria;
- exact official source commit, local repository path if already present,
  working-tree state, approved adaptation diff if any, and license record;
- exact runtime, interpreter, package, CUDA, driver, GPU, memory, storage,
  scheduler, network, credential, and logging boundaries;
- seed and determinism policy;
- one exact action, command or patch scope, input paths, output paths,
  collision policy, retention policy, and failure policy;
- handoff and no-save boundary.

If BNT was not explicitly selected, the target is not binary, the matrix
contract is not fixed, the atlas or node order is unresolved, the split or
sealed-test boundary is missing, or the source state is not exact, stop with
**BNT implementation contract incomplete**.

> [!info] References
> The model card comparator summary is in `./references/model_card_comparator.md`; read it when comparing cards.
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm the selected handoff

Verify:

- `bnt` is the exact selected card;
- the individual-card lane, prediction target, generalization target, input
  representation, split, metric, baseline, compute budget, and claim boundary
  are already fixed;
- the current card and Comparator Summary match the state reviewed by
  [run-models](../run-models/SKILL.md);
- no later information has changed the scientific design.

An available connectivity matrix or CUDA environment does not select BNT.

### 2. Verify the selected route or resolve an open choice

Assess the approved route against the fixed task and evidence fields below.
Carry it forward if compatible. If it conflicts with the specification,
report the blocker and stop without substituting the other route.

Compare Route A and Route B only when a material decision remains open and
both are eligible. If only one is eligible, show its limitation and seek the
user's decision. Verify the selected route before the implementation contract.

| Field | Route A: source reproduction | Route B: evaluation-safe adaptation |
|---|---|---|
| Code state | Exact official commit | Exact official base plus approved diff |
| Internal test | Development-exposed by source | Sealed until frozen release |
| Checkpoint | Public source behavior | Validation-selected under approved rule |
| Logging | Source W&B behavior requires separate approval | Approved local or separately authorized logging |
| Scientific use | Descriptive reproduction only | Bounded evaluation under upstream specification |
| Claim | Source behavior | No broader than actual external validity |

Record why the chosen route fits. If neither route fits, return to
[run-models](../run-models/SKILL.md) rather than inventing a third route.

### 3. Build the BNT Implementation Contract

Create:

| Element | Approved state | Evidence | Conflict or missing state | Stop rule |
|---|---|---|---|---|
| Route and exact source | | | | |
| Binary target and class order | | | | |
| Observation and dependence unit | | | | |
| Population and generalization | | | | |
| Atlas, ROI count, and node order | | | | |
| Matrix estimator and diagonal | | | | |
| Split, tuning, validation, and sealed test | | | | |
| Metric, baseline, uncertainty, and threshold | | | | |
| Architecture and approved diff | | | | |
| Runtime, CUDA, W&B, and network | | | | |
| Exact action and writes | | | | |
| Verification and handoff | | | | |

### 4. Gate 1: approve route and read-only preflight

Show:

- selected route and why it fits;
- exact source, license, clean-tree expectation, and source hashes;
- paper, official-code, and NeuroClaw-candidate conflicts;
- target, observation, atlas, node order, matrix, and partition contract;
- proposed architecture and every proposed code or configuration change;
- runtime, CUDA, package, W&B, network, credential, compute, and privacy
  requirements;
- exact read-only paths and metadata to inspect;
- missing evidence, blockers, and no-go conditions;
- proposed single later action and stop point.

Gate 1 authorizes read-only inspection of only the named source, environment,
manifests, matrix metadata, and existing matrix attestations within the
approved scope. Matrix arrays and label values are outside this gate. It does
not authorize cloning, network access, credentials, package installation,
environment creation, data download, outcome inspection, source changes,
training, validation, sealed-test access, inference, output writes, or saving.

If the route, source, target, atlas, node order, matrix convention, split,
metric, architecture, or action changes, rebuild the contract.

### 5. Verify source and environment read-only

Check:

- repository path resolves to the approved commit;
- working tree is clean or every difference is listed and classified;
- official license and source-file hashes match the reviewed state;
- no mutable branch name or unpinned remote replaces the commit;
- interpreter, package, CUDA, driver, GPU, memory, storage, and scheduler
  states are recorded without installing or changing anything;
- W&B or another external logger is disabled by a reviewed local route or has
  separate explicit service and credential approval;
- input and output paths are explicit, minimally scoped, and collision-free.

Verify the selected participant host against the pinned source's Python, package and NVIDIA CUDA requirements. Missing or incompatible requirements stop this route. This check does not authorize creating an environment, installing packages, emulation or moving a run to another machine.

### 6. Audit matrices and partitions without outcome leakage

Verify from the approved manifests and metadata:

- one unique observation key maps to one matrix and one permitted label-row
  identifier;
- matrix shape is exactly `[V, V]` and common across observations;
- atlas identity, ROI count, atlas label list, and node order match exactly;
- no participant, family, site, session, or longitudinal relation crosses a
  prohibited partition boundary;
- all target-informed or learned preprocessing is absent before the split;
- the sealed-test manifest is hashed and unavailable to development code;
- no identifier-derived or fallback label exists.

Use existing attestations tied to the exact matrix identities or immutable
input manifest to verify finiteness, symmetry, diagonal, sign, scale, Fisher
transform, and missing-value rules against the approved contract. If an
attestation is missing, inspect values only in a separately authorized check
of the named nonsealed matrices, with exact read scope and no outcome contact.
Record missing evidence as unresolved and stop before any action that depends
on it. Sealed-test access remains limited to the single separately approved
Route B release after the required freeze.

Do not automatically apply `tanh`, zero the diagonal, append T1 values, mask
ROIs, boost edges, impute, harmonize, standardize, or reorder nodes. Route
upstream preparation changes to [fmri-coordinator](../fmri-coordinator/SKILL.md) and scientific split changes to
[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md).

### 7. Audit architecture and evaluation behavior

For the exact planned route, record:

- ROI count and four-head divisibility;
- attention layers, pooling flags, final cluster count, positional encoding,
  cluster initialization, center freezing, projection assignment, dropout,
  classifier head, and parameter count;
- loss, optimizer, learning-rate schedule, epoch cap, batch size, stopping
  rule, checkpoint-selection rule, and seed policy;
- whether mixup or another augmentation is used and whether it is confined
  to training;
- exact output class order and probability, calibration, and threshold
  semantics;
- where train, validation, and test metrics are computed and logged;
- whether attention or cluster artifacts are generated and under which
  partition.

For Route A, preserve discrepancies and downgrade the claim.

For Route B, the approved diff must at minimum:

- take immutable partition manifests rather than create a new random split;
- prevent sealed-test construction or iteration during training and tuning;
- select and restore a checkpoint using only the approved validation rule;
- release the sealed test only after code, config, threshold, and checkpoint
  are frozen;
- write keyed predictions and one final test record without feeding results
  back into model choice;
- remove or separately gate external logging;
- record every architecture-preserving and harness-changing line.

Do not claim the adapted harness reproduces published metrics.

### 8. Prepare one exact action

Choose one action permitted by the selected route.

Route A permits only:

1. verify source fidelity;
2. perform one synthetic shape and forward-pass check in the exact source;
3. run one exact-source descriptive reproduction in which every source
   `test` input is explicitly designated development data rather than the user's
   sealed test;
4. extract one already approved model-behavior artifact from that descriptive
   reproduction.

Route B permits only:

1. create one reviewed evaluation-harness adaptation that preserves the
   pinned BNT architecture;
2. perform one synthetic shape and forward-pass check in the adapted harness;
3. run one training checkpoint without sealed-test access;
4. run one validation-only evaluation;
5. freeze one checkpoint and evaluation manifest;
6. release one sealed test once;
7. extract one already approved model-behavior artifact.

Route A never permits source adaptation, validation-selected checkpoint
claims, or contact with the user's sealed test. Those actions require Route B.

State exact command or patch, working directory, environment, inputs, outputs,
resource request, network state, expected files, hashes, collision behavior,
failure behavior, and verification. Do not bundle several actions into one
approval.

### 9. Gate 2: approve one exact adaptation or execution action

Show:

- the completed preflight record;
- selected route and exact source or source-plus-diff hashes;
- source-code and paper conflicts that remain;
- fixed target, matrix, partitions, architecture, metric, baseline, and
  claim boundary;
- exact action, command or patch, environment, hardware, resource, network,
  credential, read, and write scope;
- sealed-test state before and after the action;
- expected outputs, verification, stop conditions, and rollback or retention
  behavior;
- all unresolved limitations.

Gate 2 authorizes only that exact route-qualified action. It does not
authorize a missing package installation, repository clone, data or weights
download, W&B login, remote execution, another fold or seed, hyperparameter
search, interpretation, saving elsewhere, or downstream chaining. Sealed-test
release is available only when Route B is selected and that release is the
single named action.

### 10. Execute only the approved action

Before execution:

- recheck source, diff, environment, manifest, and output hashes or metadata;
- verify no output target exists unless the collision plan explicitly allows
  it;
- verify external network and logging state;
- record the start state.

During execution:

- preserve stdout, stderr, exit status, resource state, and warnings;
- stop on nonzero exit, unexpected network access, manifest drift, NaN or
  infinite values, shape mismatch, class-order conflict, output collision,
  device mismatch, or sealed-test contact outside the approved action;
- do not repair by installing, changing parameters, retrying with new seeds,
  or inspecting outcomes.

After execution:

- stop before another action;
- preserve failure artifacts according to the approved retention plan;
- do not select a new model or checkpoint from unexpected results.

### 11. Verify and return the implementation record

Verify:

- exact source and diff;
- environment and hardware;
- input keys, matrix and partition contracts;
- no unauthorized data, network, credential, or sealed-test contact;
- exit state and expected artifacts;
- keyed prediction shape and class order when predictions were approved;
- checkpoint source and selection rule;
- artifact hashes and collision state;
- metric calculation only on the approved partition;
- attention and cluster outputs labeled as model behavior;
- claim no broader than the route and evidence.

Return:

```text
BNT Implementation Record
Selected route and approved action:
Official source, license, and source hash:
Adaptation diff and rationale:
Target, observation, population, and permitted claim:
Atlas, ROI order, matrix semantics, and input manifest:
Partition, outcome-contact, and sealed-test ledger:
Architecture, training, checkpoint, metric, and baseline:
Environment, CUDA, hardware, network, and logging state:
Command or patch and write scope:
Exit state, warnings, failures, and retries:
Artifacts, keys, shapes, and hashes:
Attention or cluster artifact claim boundary:
Verification passed, failed, or unresolved:
Required next approval or bounded handoff:
```

## Boundaries

- Stop if BNT was not explicitly selected through the individual-card lane.
- Stop if the target is not an approved binary classification target.
- Stop if observation keys, class order, atlas, ROI count, node order, matrix
  convention, split, metric, baseline, or sealed-test boundary is unresolved.
- Stop if the ROI feature dimension is incompatible with the pinned
  four-head architecture. Return the model or method choice to
  [run-models](../run-models/SKILL.md) and [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) for a newly reviewed
  architecture or separate card rather than changing BNT inside this adapter.
- Stop if source commit, license, working-tree state, or proposed diff is
  unclear.
- Stop if the NeuroClaw route is offered as executable without its missing
  training entry point and independent verification.
- Stop before using the public source's epochwise test metrics as final
  evidence.
- Stop before installing packages, creating an environment, cloning,
  downloading data or weights, authenticating, enabling external logging,
  using a remote GPU, or writing outside the exact approved scope.
- Stop before a sealed-test release unless it is the single approved action
  and all code, config, checkpoint, threshold, and metric logic are frozen.
- Stop after one action. A successful adaptation does not authorize training;
  successful training does not authorize test release.
- Never infer labels, silently skip observations, reorder ROIs, alter the
  diagonal, change transforms, or fuse modalities by convenience.
- Never promote attention, OCREAD assignment, or model weights to anatomy,
  mechanism, causation, diagnosis, or treatment relevance.
- Never overwrite source, data, checkpoints, predictions, logs, or records
  without an exact approved collision plan.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Kan, X. (n.d.). *BrainNetworkTransformer* [Computer software]. GitHub. https://github.com/Wayfear/BrainNetworkTransformer
- Kan, Dai, Cui, Zhang, Guo, & Yang. (2022). Brain network transformer. *NeurIPS 2022*. https://papers.nips.cc/paper_files/paper/2022/hash/a408234a9b80604a9cf6ca518e474550-Abstract-Conference.html
- Kapoor & Narayanan. (2023). Leakage and the reproducibility crisis in machine-learning-based science. https://doi.org/10.1016/j.patter.2023.100804
