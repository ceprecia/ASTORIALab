# Model Card Comparator Summary (bnt)

Read this reference when the skill or the user asks for it.

## Model Card Comparator Summary

Read only this section and frontmatter when [run-models](../../run-models/SKILL.md) compares cards.

- **Canonical owner and exact trigger:** `bnt`; trigger `bnt`.
- **Lane:** Individual card.
- **Model, paper, code, release or commit, license, and verification date:**
  Brain Network Transformer by Kan et al., NeurIPS 2022; official repository
  `Wayfear/BrainNetworkTransformer`; commit
  `8a588aadad0166209269fa114e5df4e42209e207`; no release or tag found;
  MIT License, Copyright (c) 2022 Xuan Kan; verified 2026-07-24.
- **Intended research task and prohibited uses:** Research-only binary
  graph-level classification from one fixed-order dense ROI connectivity
  matrix per observation. No clinical use, automatic model selection,
  regression, multiclass prediction, unsupported modality transfer, or
  mechanistic interpretation.
- **Target type, prediction unit, and output semantics:** The pinned official
  model has a fixed two-logit head and supervised cross-entropy training.
  One matrix produces two class logits. Class order, probability conversion,
  thresholding, and calibration must be specified outside the model.
- **Required modalities, input representation, shape, atlas, and
  preprocessing:** Dense square Pearson-correlation connection profiles with
  identical ROI count, atlas, node order, matrix convention, and acquisition
  meaning across observations. The paper used Craddock 200 for ABIDE and HCP
  360 for ABCD. The pinned code consumes the supplied matrix as is. It does
  not establish Fisher-z inversion, zero diagonal, T1 fusion, ROI masking, or
  another transform as a universal BNT requirement.
- **Training, fine-tuning, inference, and pretrained-weight state:** The
  official repository provides training code but no reviewed pretrained
  weights or inference release. Its public code is not evaluation-safe
  without an approved harness adaptation because it evaluates and logs its
  internal test loader every epoch and saves the final model.
- **Population, acquisition, site, and domain evidence:** Published evidence
  is tied to ABIDE, 1009 observations from 17 sites using Craddock 200, and a
  restricted ABCD sample of 7901 observations using HCP 360. Transfer to
  another population, acquisition, atlas, site structure, or target is
  unresolved.
- **Partition, tuning, evaluation, calibration, and uncertainty evidence:**
  The paper reports 70/10/20 train, validation, and test partitions, five
  random runs, validation-AUROC checkpoint selection, and test reporting.
  The pinned public code does not implement that boundary faithfully: it
  reads test metrics each epoch, has no validation-selected checkpoint
  restoration, and saves the last model. Calibration and formal uncertainty
  are not established by the card.
- **Leakage controls and unresolved leakage risks:** Split before any
  outcome-informed or cross-observation transform; keep related
  observations, families, sites, and longitudinal units in the approved
  groups; fit all learned transforms inside training partitions; never use
  the sealed test during development. The official source's epochwise test
  access, mutable random splitting, and source-data conventions are
  unresolved for confirmatory use.
- **Baselines, ablations, and comparison fairness:** The paper compares
  several graph transformers, fixed-network models, learned-network models,
  and readout ablations in its own datasets. Those results are not
  commensurable with a new target, split, population, preprocessing route, or
  compute budget. Use only upstream-approved baselines evaluated under the
  same outer partitions and data access.
- **Performance evidence with exact dataset and evaluation context:**
  Published metrics are descriptive for the paper's ABIDE and ABCD tasks and
  five-run evaluation. The repository README adds an out-of-paper regression
  figure, but the pinned public model and training code remain fixed to
  binary classification. No reported value predicts performance on the user's
  data.
- **Interpretability artifact and permitted claim:** The pinned layers retain
  last-pass self-attention weights in memory, but the official BNT forward
  route does not return its locally accumulated OCREAD assignments and its
  cluster-center helper is not valid at model level. Assignment or center
  extraction therefore requires a separately approved reviewed diff. Any
  resulting artifact describes fitted model behavior under one source, data,
  and checkpoint state, not a causal, mechanistic, anatomical, diagnostic,
  or biomarker result.
- **Runtime, package, hardware, memory, storage, and time requirements:** The
  README lists Python 3.9, CUDA toolkit 11.3, PyTorch 1.12.1, torchvision
  0.13.1, torchaudio 0.12.1, Weights and Biases 0.13.1, scikit-learn 1.1.1,
  pandas 1.4.3, and hydra-core 1.2.0. The code calls CUDA directly and
  initializes Weights and Biases. It has no reviewed environment lock or
  CPU-safe route. The paper reports an NVIDIA Quadro RTX 8000. Actual memory,
  storage, time, and compatibility remain environment-specific.
- **Determinism, provenance, failure, and verification behavior:** The pinned
  source does not establish complete random seeds, immutable environment
  resolution, one-shot test isolation, or validation-best checkpoint
  restoration. A valid run must record source and diff hashes, environment,
  hardware, seeds, subject and partition hashes, exact config, exit state,
  artifact hashes, and failures.
- **Known limitations, missing evidence, and implementation blockers:** The
  official paper and code diverge on evaluation behavior. The NeuroClaw
  reimplementation changes defaults and inputs and lacks the advertised
  training entry point. Verify the participant's selected runtime against the source requirements. This documentation review does not establish that a participant run has been executed or validated.
