# Model Card Comparator Summary (neurostorm)

Read this reference when the skill or the user asks for it.

## Model Card Comparator Summary

Read only this section and frontmatter when [run-models](../../run-models/SKILL.md) compares cards.

- **Canonical owner and exact trigger:** `neurostorm`; trigger `neurostorm`.
- **Lane:** NeuroSTORM platform. Do not load standalone model cards in the
  same comparison or implementation context.
- **Initially eligible component:** only the official platform's own
  `model=neurostorm` four-dimensional volume backbone. Every embedded
  alternative model remains ineligible until its exact platform
  implementation, original source, license, fidelity, task surface, and
  evaluation behavior pass a separate review.
- **Paper, code, commit, and verification date:** Wang et al., "Towards a
  general-purpose foundation model for functional MRI analysis," Nature
  Biomedical Engineering, published 2026-04-23, DOI
  `10.1038/s41551-026-01666-y`; official repository
  `CUHK-AIM-Group/NeuroSTORM`, commit
  `4971d5d1343e99137460f265270e92c3159e5106`, verified 2026-07-24.
- **License state:** the pinned root `LICENSE` is Apache License 2.0. The
  README badge and directory description call it MIT, while the official
  Hugging Face model card also declares MIT. Preserve this mismatch in every
  readiness record and verify the exact code or weight license before
  modification, redistribution, or release.
- **Intended research task and prohibited uses:** research-only representation
  learning and downstream prediction from already approved fMRI inputs. No
  clinical use, automatic model or target selection, person-specific verdict,
  or mechanistic or biomarker claim.
- **Input representation and conversion:** the reviewed platform volume route
  expects preprocessed MNI-space four-dimensional fMRI. Its converter
  resamples to 2 mm spatial resolution and 0.8 s temporal resolution,
  center-crops each spatial axis to at most 96 voxels, removes negative
  values, applies subject-level foreground scaling, and stores symmetric
  int8-quantized tensors. These are source behaviors, not universal fMRI
  requirements, and each must match the approved scientific specification.
- **Training and adaptation surface:** the source supports masked-autoencoder
  pretraining for NeuroSTORM, full fine-tuning, and task-specific
  parameter-efficient tuning. Availability does not establish validity for a
  new task or population.
- **Published evidence boundary:** the paper reports pretraining on 28.65
  million frames from more than 50,000 participants across multiple centers
  and ages 5 to 100, with five downstream task families. Those reported
  results do not predict performance under a new cohort, preprocessing
  route, target, partition, or checkpoint.
- **Partition and sealed-test state:** the public data module can create
  subject-level random splits and write them when a split file is absent. It
  does not establish family, site, scanner, acquisition, or longitudinal
  grouping. Its split routine hard-codes NumPy seed 0 but uses Python random
  before the main route seeds it. When train and validation consume the full
  sample, it aliases test to validation.
- **Evaluation blocker:** the public validation loader returns both validation
  and test loaders every validation epoch, and the training model computes
  and logs both sets of metrics before a final test call. Evaluation loaders
  use `drop_last=True`. The bundled atlas sweep records `test_acc` while
  varying model, atlas, and learning rate. Distributed metrics are calculated
  locally and then synchronized rather than gathered from keyed predictions.
  The public route is not sealed-test safe and cannot support a confirmatory
  or final generalization claim without an approved harness adaptation.
- **Checkpoint and network state:** `main.py` attempts a Hugging Face download
  when a requested local checkpoint is missing. The reviewed official model
  repository is public and declares MIT, but its checkpoint content and
  compatibility were not downloaded or executed. Disable automatic network
  fallback and verify exact revision, filename, content hash, license,
  architecture, target, preprocessing, class or scale semantics, and trust
  before loading. A failed download can fall through to training from scratch
  rather than failing closed.
- **Runtime and compute state:** the official instructions center on Python
  3.11, CUDA 12.8, PyTorch 2.7.1, PyTorch Lightning 1.9.4, MONAI, Mamba-SSM,
  and an NVIDIA GPU. Several imported packages are absent from the pinned
  requirements file, and some components require source builds. Verify the participant's selected runtime against those source requirements. This card does not establish that a participant run has been executed or validated.
- **Logging and writes:** TensorBoard is the default logger; Neptune can
  contact an external service. Source routes may write split manifests,
  quantized data, logs, checkpoints, and prediction files. Every read, write,
  network, credential, and collision boundary requires an exact action
  approval.
- **Test evidence:** the repository has source-level tests and CI, but the
  reviewed tests do not validate the complete preprocessing, split,
  fine-tuning, sealed-test, checkpoint-download, or real Mamba execution
  route. Graph dependency and import failures are allowed in CI. Test presence
  is not scientific validation.
- **Known blockers:** lane and component identity, upstream preprocessing,
  immutable dependence-aware partitions, source-versus-weight license
  mismatch, unverified checkpoint trust and compatibility, incomplete
  dependency specification, test exposure during validation, environment
  availability, external logging, and output paths.
