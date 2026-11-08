---
name: neurostorm
description: >-
  Implements one already selected NeuroSTORM platform checkpoint for the
  official NeuroSTORM four-dimensional fMRI backbone through either an
  explicitly labeled source-reproduction route or a separately approved
  evaluation-safe adaptation of one exact official source state. Use when the
  request names this skill or run-models hands off the selected NeuroSTORM
  platform lane after the prediction specification is fixed. Triggers: use the
  NeuroSTORM checkpoint, 4D fmri foundation model checkpoint.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: Python, PyTorch, the NeuroSTORM repository
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# NeuroSTORM Platform Adapter

Implement one approved NeuroSTORM platform checkpoint without confusing an
integrated software platform, the NeuroSTORM backbone, an embedded alternative
model, source reproduction, evaluation-safe adaptation, and scientific
evidence.

## Purpose

It preserves platform-lane exclusivity, source, model, checkpoint, input, preprocessing, split, leakage, validation, license, environment, CUDA, network, logging, write, sealed-test, verification, and claim boundaries without choosing NeuroSTORM or a task; loading standalone model cards; treating embedded alternative models as eligible; inheriting NeuroClaw dependencies; installing software; downloading data or weights; trusting unreviewed checkpoints; using the public evaluation harness as sealed-test safe; diagnosing a person; overwriting; or chaining downstream analysis.

`neurostorm` owns:

- the bounded ASTORIA implementation card for the official NeuroSTORM
  platform at one exact reviewed commit;
- the platform lane after the user selects it through [run-models](../run-models/SKILL.md);
- the official platform's own `model=neurostorm` four-dimensional volume
  backbone, including one approved source audit, synthetic check, conversion,
  pretraining, fine-tuning, validation, sealed-test, or research-inference
  checkpoint;
- explicit separation of exact-source reproduction from an evaluation-safe
  adapted harness;
- verification of source, checkpoint, environment, input, partition, action,
  artifact, failure, and claim boundaries;
- a NeuroSTORM Platform Readiness Record or one bounded Platform Action
  Record.

The user owns the question, hypothesis, prediction, confirmatory status, target,
observation unit, population, generalization target, data rights, upstream
preprocessing, representation, split, metric, baseline, model and lane
selection, source modification, pretrained-weight use, compute budget,
outcome contact, sealed-test release, interpretation, and claims.

[run-models](../run-models/SKILL.md) owns comparison and selection between the platform lane and
eligible standalone cards. [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns the predictive
estimand, dependence groups, outer and inner partitions, leakage controls,
metric, baseline, null, calibration, and claim specification. [fmri-coordinator](../fmri-coordinator/SKILL.md)
owns modality routing and the upstream preprocessing handoff. `neurostorm`
does not select itself, redesign preprocessing, or replace those owners.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `NeuroSTORM platform`, `foundation model`, `fMRI`,
`pretrain`, `fine-tune`, `phenotype prediction`, `disease diagnosis`,
`brain model`, `best model`, `run-models`, a dataset name, a file extension,
or another broad model, method, task, or modality phrase.

Do not use this skill to:

- decide whether a foundation model, deep model, or NeuroSTORM is appropriate;
- choose a target, label, model, split, metric, baseline, or scientific claim;
- load or compare standalone `bnt`, `brain_gnn`, `combraintf`, `fm_app`,
  `ibgnn`, or `lggnn` cards while the platform lane is active;
- treat the platform's embedded BrainGNN, BNT, LG-GNN, Com-BrainTF, IBGNN,
  BrainNetCNN, or SwiFT implementations as eligible merely because files
  exist in the repository;
- download HCP, ABCD, UK Biobank, ABIDE, clinical, or other data;
- clone a repository, download a checkpoint, create an environment, install
  packages, build a container, allocate a remote GPU, authenticate to
  Neptune or Hugging Face, or enable a service without separate authority;
- load an untrusted pickle-capable checkpoint;
- let the source create a new split when an approved immutable manifest is
  required;
- inspect a sealed test during training, tuning, checkpoint selection,
  threshold selection, debugging, or routine validation;
- perform person-specific clinical inference, diagnosis, prognosis,
  screening, monitoring, or treatment recommendation;
- call predictions, embeddings, attention, prompts, selected voxels, or
  transfer performance mechanisms, causes, biomarkers, or validated
  explanations.

## Exact reviewed source state

### Official platform

The implementation authority is the official repository at commit
`4971d5d1343e99137460f265270e92c3159e5106`, tree
`ea7df0e11db2bee26e9aa41cefe1fd262a842a89`. No tag or GitHub release was
found. Preserve this commit or identify and re-review a new exact state.

Relevant SHA-256 values:

| File | SHA-256 |
|---|---|
| `LICENSE` | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` |
| `README.md` | `23f10f756ec27fb903a31967a7ef848833b878e957ca283da8bc215d196b9c23` |
| `requirements.txt` | `25c391334de3aaa35e282b89e1db79ddaad725952bbfeb39a179b0708673af72` |
| `main.py` | `dcd9e5a7657aaae6ce7e65e9343f4a072e7fe5ef70c8b89d477845177b0c252f` |
| `datasets/data_module.py` | `f4e88cdb69c7e6e5ea81167fcdd420d5e1516e8bdec9b46a4c7cfd9247e9fcdf` |
| `datasets/preprocessing_volume.py` | `e6f60d319ff618ac74cce7f3595ed664592dc84d9f672648d9e695495c08d752` |
| `models/neurostorm.py` | `867bb1b8f9e016b3c3634afb382511538bc85526e5b7471b58382850d473ce55` |
| `models/peft.py` | `032dc2422d42b0c93536fe1c7fef00a9129ba430380d26cdd43fb89cc336fac5` |
| `models/load_model.py` | `9c8ccc737ca79b59c26175ab85e79bc4df8f625537db643a152c3e60bd93d7ff` |
| `models/lightning_model.py` | `0f2030e0cda60770a512831bdad34c5b786ed627ad233b4408ea55912948f75d` |
| `.github/workflows/ci.yml` | `a64a427b68bf014a4801cc75c826d73dbdc97bd30f2600af1d8ca211c674b364` |

At this state:

- `main.py` imports external logging and Hugging Face support at module load,
  uses TensorBoard by default, and can download a missing weight automatically;
- the data module creates and writes random subject splits when the named
  split file is absent;
- the validation loader returns validation and test together, so test metrics
  are computed every validation epoch;
- evaluation loaders use `drop_last=True`, which can omit observations from
  reported validation or test metrics;
- the default 0.9 train and 0.1 validation split aliases test to validation;
- the bundled sex and atlas sweep uses test accuracy while varying model,
  atlas, and learning rate;
- the final training route calls test again after fitting;
- target scaling is fit on the training dataset, but every partition,
  repeated-observation weight, label, and transform still requires audit;
- the volume converter performs scientifically material resampling, cropping,
  clipping, scaling, quantization, file creation, and optional source deletion;
- checkpoint inspection includes pickle-capable loading;
- the requirements file does not fully enumerate imports used by the
  repository;
- a missing checkpoint can trigger an automatic Hugging Face download, while
  failure can fall through to training from scratch;
- the single-subject age demo does not establish inverse scaling from the
  standardized model output to years and labels an uncalibrated softmax value
  as confidence;
- the CI and unit tests do not establish an end-to-end, sealed-test-safe
  research workflow.

Do not silently repair or reinterpret these facts. A change to preprocessing,
input layout, split construction, checkpoint loading, model architecture,
tuning, logging, validation, test access, prediction output, or supported
task is an adaptation and must be recorded as such.

### Official weight source

The official Hugging Face model repository
`zxcvb20001/NeuroSTORM` was reviewed at revision
`f3ad4a9e6692e208b87fc72149ecb8443334eeba`, modified
2026-07-23T07:30:18Z. Its model card declares MIT. The listed NeuroSTORM
pretraining checkpoint
`pretraining/pt_neurostorm_mae_5ds.ckpt` reports Xet content identifier
`de3cbda81064bd2f72641b393d0940a599e6d17307cbb4a8ae195a7ea5a568e2`
and size 93,061,240 bytes.

This review did not download or deserialize the checkpoint. A listing and
remote content identifier do not prove source compatibility, safety,
scientific fit, or license coverage. Automatic download remains prohibited.

### NeuroClaw candidate

The NeuroClaw card is design evidence only. It broadly wraps preprocessing,
pretraining, fine-tuning, inference, dataset download, environment creation,
and eight model implementations. Its copied dependencies, broad triggers,
commands, package graph, model claims, automatic lifecycle, and action
surfaces are not inherited.

The candidate also:

- labels the official platform MIT although its pinned root license is
  Apache-2.0;
- describes 2026-05-08 as a release although the official repository has no
  tag or GitHub release;
- claims PT and H5 dual-format flags that do not exist in the pinned source;
- references absent ROI, FC, training-script, pretrained-model, and test
  paths;
- documents a dataset argument that the pinned subject-name resolver does not
  support.

None of those claims or commands is retained.

## Route boundary

Carry forward the user's approved NeuroSTORM route if it fits the fixed
scientific and evaluation specification. Resolve any open material route choice
with the user before building the implementation contract.

### Route A: exact-source reproduction

Use the pinned source only to inspect or reproduce its behavior. Treat every
source `test` loader seen during validation as development-exposed data, not
The user's sealed test. No result from this route can support a confirmatory or
final generalization claim.

Visible outputs:

- Source Reproduction Contract
- exact source, checkpoint, and environment record
- source behavior and paper-to-code discrepancy table
- descriptive artifact or failure record

Benefit: preserves what the public source actually does.

Tradeoff: preserves its partition, test-contact, logging, dependency, and
portability limitations.

Limitation: cannot establish sealed-test performance.

### Route B: evaluation-safe adaptation

Preserve the selected NeuroSTORM backbone while replacing unsafe
orchestration under an explicit reviewed diff. Use immutable
dependence-aware manifests, fit transforms inside training partitions, tune
and select checkpoints using training and validation only, keep the sealed
test unavailable to development code, disable automatic downloads and
unapproved external logging, freeze code and evaluation logic, and release
the sealed test once in a separately approved action.

Visible outputs:

- NeuroSTORM Adaptation Contract
- exact source-to-adaptation diff and rationale
- partition and outcome-contact ledger
- one approved Platform Action Record

Benefit: can support bounded evaluation under the user's approved specification.

Tradeoff: it is an ASTORIA adaptation, not an exact reproduction of the
public training harness.

Limitation: model validity and transportability still depend on the approved
data, task, preprocessing, population, and external validation.

An open route permits bounded assessment in Step 2 only. Stop before
implementation until the user has selected an eligible route. Availability,
reported performance and compute access are feasibility evidence.

## Inputs

Obtain or mark missing:

- a selected-platform handoff from [run-models](../run-models/SKILL.md);
- an approved Neural Decoding Method Specification or equivalent fixed
  prediction and evaluation specification;
- the user's approved source-reproduction or evaluation-safe adaptation route,
  or the open route decision to resolve before implementation;
- exact target, target timing, observation key, participant or unit,
  population, inclusion and exclusion rules, and prohibited uses;
- intended generalization and dependence groups, including participant,
  family, site, scanner, session, acquisition, and longitudinal structure;
- approved upstream fMRI preprocessing provenance and QC state;
- exact MNI space, voxel size, temporal resolution, spatial shape, frame
  count, mask, sign, scaling, crop, quantization, and missing-data contract;
- immutable train, tuning, validation, calibration when applicable, and
  sealed-test manifests;
- primary metric, uncertainty unit, threshold, calibration, baseline, null
  when applicable, subgroup plan, negative controls, multiplicity, and
  acceptance criteria;
- exact official source commit and clean-tree state;
- exact checkpoint source, revision, filename, remote and local hash,
  license, target, architecture, preprocessing, trust, and compatibility, or
  an explicit train-from-scratch route;
- exact interpreter, package, Mamba, CUDA, driver, GPU, memory, storage,
  scheduler, container, network, credential, and logger boundaries;
- one exact action, command or patch, read paths, write paths, collision
  policy, retention policy, failure policy, and stop point;
- handoff and no-save boundary.

If the platform lane, official NeuroSTORM component, prediction
specification, source, checkpoint, input, partition, environment, or exact
action is unresolved, stop with **NeuroSTORM platform contract incomplete**.

> [!info] References
> The model card comparator summary is in `./references/model_card_comparator.md`; read it when comparing cards.

## Steps

### 1. Confirm platform-lane selection

Verify:

- The user selected the NeuroSTORM platform lane;
- no standalone deep-model card is loaded or being compared;
- the exact component is the official `model=neurostorm` backbone;
- target, generalization, input, partition, metric, baseline, compute, and
  claim boundaries are already fixed;
- the comparator summary still matches the reviewed source state.

An available checkpoint, GPU, dataset, or reported benchmark does not select
the platform.

### 2. Verify the selected route or resolve an open choice

Assess the approved route against the fixed task and evidence fields below.
Carry it forward if compatible. If it conflicts with the specification,
report the blocker and stop without substituting the other route.

Compare Route A and Route B only when a material decision remains open and
both are eligible. If only one is eligible, show its limitation and seek the
user's decision. Verify the selected route before the implementation contract.

| Field | Route A: source reproduction | Route B: evaluation-safe adaptation |
|---|---|---|
| Code | Exact pinned source | Pinned source plus approved diff |
| Test contact | Development-exposed by source | Sealed until frozen release |
| Split | Source behavior, fully labeled | Immutable approved manifests |
| Network | Source may download weights | Disabled unless separately approved |
| Logging | Source TensorBoard or Neptune behavior | Exact approved local route |
| Claim | Descriptive source behavior | Bounded evaluation only |

If neither route fits, return to [run-models](../run-models/SKILL.md).

### 3. Build the NeuroSTORM Platform Contract

Create:

| Element | Approved state | Evidence | Conflict or missing state | Stop rule |
|---|---|---|---|---|
| Lane, component, route, and source | | | | |
| Target, observation, and population | | | | |
| Generalization and dependence groups | | | | |
| Upstream preprocessing and QC | | | | |
| Platform conversion and input shape | | | | |
| Train, validation, calibration, and sealed test | | | | |
| Metric, uncertainty, baseline, and null | | | | |
| Checkpoint source, trust, and compatibility | | | | |
| Environment, CUDA, network, and logging | | | | |
| Exact action, reads, writes, and collision policy | | | | |
| Verification, claim, and handoff | | | | |

### 4. Gate 1: approve contract and read-only preflight

Show:

- selected lane, component, route, and exact source;
- source and weight license mismatch;
- target, observation, preprocessing, conversion, partition, metric,
  baseline, checkpoint, and claim contract;
- every proposed code, configuration, conversion, or harness change;
- runtime, CUDA, package, network, credential, logger, compute, privacy,
  read, write, and collision requirements;
- test-exposure and checkpoint-trust blockers;
- proposed single later action and stop point.

Gate 1 authorizes read-only inspection of only the named source, checkpoint
metadata, environment, manifests, and input metadata. It does not authorize
cloning, downloading, installing, environment creation, data access,
checkpoint deserialization, source changes, conversion, training,
validation, test access, inference, network contact, logging, or writes.

### 5. Verify source, checkpoint, and environment read-only

Check:

- repository path resolves to the approved commit;
- the working tree is clean or every change is classified;
- source hashes and root license match the reviewed state;
- the checkpoint is already local or remains metadata-only;
- remote revision, filename, size, content identifier, license, and expected
  architecture are exact;
- checkpoint loading would not deserialize an untrusted object;
- interpreter, packages, Mamba, CUDA, driver, GPU, memory, storage, and
  scheduler state are recorded without installing or changing anything;
- automatic Hugging Face download and Neptune contact are disabled;
- every output path is explicit, minimally scoped, and collision-free.

Verify the participant's selected runtime against the exact source's NVIDIA CUDA, Python and package requirements. Missing requirements stop execution; this does not authorize installation, emulation, containerization or moving the run elsewhere.

### 6. Audit inputs, conversion, and partitions

Verify:

- one unique observation key maps to the permitted image and label row;
- participant, family, site, scanner, session, acquisition, and longitudinal
  dependencies respect the approved manifests;
- upstream images passed human-approved QC and match the declared MNI space;
- voxel size, TR, spatial shape, frames, mask, crop, sign, scaling, and
  quantization match the approved contract;
- every learned or outcome-informed transform is fit inside training;
- no source-generated replacement split exists;
- the sealed-test manifest is hashed and unavailable to development code;
- no identifier-derived, filename-derived, row-order, or fallback label
  exists.

Do not silently resample, crop, clip, normalize, quantize, delete a NIfTI,
skip an image, rewrite a split, or change preprocessing. Route scientific
changes to [fmri-coordinator](../fmri-coordinator/SKILL.md) or [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md).

### 7. Audit model and evaluation behavior

Record:

- exact backbone, pretraining state, fine-tuning or tuning strategy, head,
  target scale or class order, parameter count, and checkpoint mapping;
- optimizer, loss, schedule, epoch cap, batch size, augmentation, stopping,
  checkpoint selection, and seed policy;
- where train, validation, test, and subgroup metrics are computed and
  logged;
- whether any test loader is constructed or iterated before frozen release;
- output probability, score, calibration, threshold, and aggregation
  semantics;
- exact external logger, network, and artifact behavior.

Route B must at minimum:

- consume immutable manifests rather than create random splits;
- keep all related units in approved groups;
- prevent sealed-test construction and iteration during development;
- select and restore a checkpoint using only the approved validation rule;
- remove automatic checkpoint downloads;
- use only trusted, hash-verified checkpoint loading;
- disable unapproved external logging;
- freeze source, diff, config, weight, threshold, and metric logic before one
  sealed-test release;
- write keyed predictions and one final test record without feeding results
  back into model choice.

Do not claim the adapted harness reproduces published metrics.

### 8. Prepare one exact action

Permitted action types, one at a time:

1. verify source, checkpoint metadata, or environment;
2. review one evaluation-harness patch;
3. convert one synthetic or approved nonsealed input after conversion
   semantics are fixed;
4. perform one synthetic shape and forward-pass check;
5. run one training checkpoint without sealed-test access;
6. run one validation-only evaluation;
7. freeze one checkpoint and evaluation manifest;
8. release one sealed test once;
9. run one bounded research-only inference on an approved nonclinical input;
10. verify one resulting artifact.

State the exact command or patch, working directory, environment, inputs,
outputs, resource request, network state, logger state, expected files,
hashes, collision behavior, failure behavior, and verification. Do not
bundle several actions into one approval.

### 9. Gate 2: approve one exact action

Show:

- completed preflight record;
- source, diff, checkpoint, environment, and manifest hashes;
- route and unresolved source or paper conflicts;
- exact action, command or patch, hardware, network, credential, read, and
  write scope;
- sealed-test state before and after;
- expected outputs, verification, stop conditions, and retention or rollback
  behavior;
- all remaining limitations.

Gate 2 authorizes only that exact action. It does not authorize an install,
clone, download, credential, external logger, another fold or seed,
hyperparameter search, interpretation, saving elsewhere, or downstream
chaining.

### 10. Execute only the approved action

Before execution:

- recheck source, diff, checkpoint, environment, manifest, and output state;
- verify that network and external logging are disabled unless explicitly
  authorized;
- verify no output collision.

During execution:

- preserve command, stdout, stderr, exit status, resource state, warnings,
  and unexpected file or network behavior;
- stop on nonzero exit, hash drift, dependency drift, untrusted load, shape
  mismatch, NaN or infinite values, label conflict, split conflict, output
  collision, unauthorized network or logging, or sealed-test contact;
- do not repair by installing packages, changing parameters, downloading a
  weight, retrying with a new seed, or inspecting outcomes.

After execution:

- verify only the expected artifacts;
- preserve failures according to the approved retention plan;
- stop before another action.

### 11. Return the readiness or action record

Return:

```text
NeuroSTORM Platform Record
Selected lane, component, route, and action:
Official source, tree, license, and hashes:
Checkpoint source, revision, license, trust, and hash:
Adaptation diff and rationale:
Target, observation, population, and permitted claim:
Upstream preprocessing and platform conversion:
Partition, dependence, outcome-contact, and sealed-test ledger:
Model, tuning, checkpoint selection, metric, and baseline:
Environment, CUDA, hardware, network, and logging:
Command or patch and exact read and write scope:
Exit state, warnings, failures, and retries:
Artifacts, keys, shapes, and hashes:
Verification passed, failed, or unresolved:
Required next approval or bounded handoff:
```

## Boundaries

- Stop if the NeuroSTORM platform lane was not explicitly selected.
- Stop if a standalone deep-model card is loaded in the same context.
- Stop if an embedded alternative model is requested without its own
  platform-component source, license, fidelity, and evaluation intake.
- Stop if target, observation, dependence, preprocessing, input, split,
  metric, baseline, checkpoint, or sealed-test boundary is unresolved.
- Stop if source, license, checkpoint trust, environment, or diff is unclear.
- Stop before the public test loader is used as a sealed final test.
- Stop before a source-created random split replaces an approved manifest.
- Stop before automatic Hugging Face download or Neptune contact.
- Stop before installing, cloning, building, containerizing, downloading,
  authenticating, using a remote GPU, or writing outside the exact scope.
- Stop after one action. Successful conversion does not authorize training;
  training does not authorize validation; validation does not authorize test
  release; test release does not authorize interpretation.
- Never delete an input, infer a label, silently skip an observation, alter a
  partition, or overwrite an artifact.
- Never promote prediction, embedding, prompt, attention, or transfer
  performance to anatomy, mechanism, causation, diagnosis, prognosis, or
  treatment relevance.
- Apply TRIPOD+AI only when the approved research task falls within its scope; it does not authorize clinical use.

## Handoffs

- Return model or lane comparison to [run-models](../run-models/SKILL.md).
- Return prediction, partition, metric, calibration, and generalization
  changes to [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md).
- Route upstream fMRI preprocessing and QC changes to [fmri-coordinator](../fmri-coordinator/SKILL.md).
- Route a selected software installation, environment build, container,
  credential, remote-compute, or data-access request through a separately
  authorized operational workflow.
- Hand a verified result to the approved interpretation or writing owner only
  after the user approves that transition.

No handoff sends, saves, installs, downloads, authenticates, executes, or
loads another skill automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Collins et al. (2024). TRIPOD+AI. https://doi.org/10.1136/bmj-2023-078378
- CUHK AIM Group. (n.d.). *NeuroSTORM* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroSTORM
- CUHK AIM Group. (2026). *NeuroSTORM* [Model weights]. Hugging Face. https://huggingface.co/zxcvb20001/NeuroSTORM
- Kapoor & Narayanan. (2023). Leakage and the reproducibility crisis in machine-learning-based science. https://doi.org/10.1016/j.patter.2023.100804
- Wang et al. (2026). Towards a general-purpose foundation model for functional MRI analysis. *Nature Biomedical Engineering*. https://doi.org/10.1038/s41551-026-01666-y
