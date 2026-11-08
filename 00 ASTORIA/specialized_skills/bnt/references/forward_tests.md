# Forward tests (bnt)

Read these forward tests when the skill or the user requests them.

## Forward tests

- **Positive:** an approved binary target, fixed dense ROI matrices, exact
  atlas order, grouped partitions, selected BNT card, compatible CUDA
  environment, and evaluation-safe diff produce one gated action and BNT
  Implementation Record.
- **Trigger:** only `bnt` loads this card.
- **Broad request:** `run a transformer on my fMRI` routes to
  [neural-decoding-analysis](../../neural-decoding-analysis/SKILL.md) and does not load this card.
- **Selection:** a BNT-like input or installed package does not select BNT;
  comparison returns to [run-models](../../run-models/SKILL.md).
- **Lane:** BNT is not loaded alongside the overlapping NeuroSTORM platform
  lane.
- **Source state:** a branch name, uncommitted code, or changed official
  commit stops until the exact state is reviewed.
- **Candidate completeness:** the absent NeuroClaw training entry point
  prevents execution.
- **Paper-code conflict:** epochwise source test access is disclosed and
  cannot support a final evaluation claim.
- **Route A test boundary:** a request to connect the user's sealed test to the
  source-faithful route is rejected and must move to a reviewed Route B
  harness.
- **Regression:** a continuous target stops because the pinned official model
  card is binary classification only.
- **Multiclass:** three classes stop rather than silently resizing the head.
- **Atlas:** CC200 matrices and HCP 360 matrices are never pooled in one
  model.
- **Node order:** equal matrix shapes with different ROI order stop.
- **Diagonal:** paper, source data, and supplied matrix conventions are
  reconciled rather than automatically zeroed.
- **Fisher transform:** a Fisher-z matrix is not passed through `tanh` unless
  that transform is explicitly approved and verified upstream.
- **Head divisibility:** an ROI count not divisible by four stops the pinned
  architecture route.
- **T1 fusion:** optional T1 values from the candidate are excluded as an
  unsupported source modification.
- **Fallback label:** a missing label never becomes an identifier-derived
  class.
- **Split:** family, site, participant, session, or longitudinal dependence
  cannot cross the approved boundary.
- **Leakage:** learned preprocessing before the outer split invalidates the
  affected evaluation.
- **Test set:** training code cannot construct, iterate, log, or tune against
  the sealed test.
- **Checkpoint:** last-epoch weights are not substituted for the approved
  validation-selected checkpoint.
- **Metric:** published ABIDE or ABCD performance is not treated as an
  expected result on another dataset.
- **Baseline:** BNT is evaluated against the upstream-approved baseline under
  identical outer partitions and data access.
- **W&B:** automatic external logging stops without separate service,
  credential, privacy, and network approval.
- **Runtime:** a synthetic host lacking the pinned source's NVIDIA CUDA or required packages stops the selected route; another host is verified separately.
- **Dependencies:** a missing package produces a blocker, not an install.
- **Failure:** OOM, NaN, CUDA mismatch, nonzero exit, missing artifact, or
  unexpected network access is preserved and not silently retried.
- **Interpretability:** attention and OCREAD assignments remain model
  behavior, not neural explanations.
- **Artifact exposure:** OCREAD assignments or centers are not claimed to be
  available from the pinned public route; extraction stops without an
  approved Route B diff and verification.
- **Clinical:** individual diagnosis, prognosis, screening, monitoring, or
  treatment use stops.
- **Single action:** a successful source patch does not automatically train;
  a successful training run does not automatically release the test set.
- **Reporting and saving:** return records in the current task's requested form or under the recipient's existing reporting policy. Save only to an exact target that was separately requested and approved.
- **Handoff:** verified keyed outputs may return to
  [neural-decoding-analysis](../../neural-decoding-analysis/SKILL.md) for bounded evaluation reasoning; raw fMRI or
  connectivity changes return to [fmri-coordinator](../../fmri-coordinator/SKILL.md).
