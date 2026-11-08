# Forward tests (svm)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive evaluation:** one approved group-aware outer evaluation keeps
  scaling and tuning inside folds and returns fold-keyed predictions.
- **Positive refit:** one separately approved final refit returns a frozen
  pipeline without claiming new performance.
- **Trigger:** Load for the explicit `svm` skill name, a bounded request such as `train an SVM on my features`, or an exact SVM handoff from Neural Decoding Analysis, the fMRI or sMRI Coordinator, or Scikit-learn.
- **Method selection:** `try every classifier` routes to
  [neural-decoding-analysis](../../neural-decoding-analysis/SKILL.md) and does not select SVM.
- **Identity:** duplicate or unmatched participant identifiers stop.
- **Join:** an inner join that drops participants or multiplies duplicates
  stops.
- **Leakage:** globally scaled or outcome-selected features without train-only
  provenance stop.
- **Dependence:** repeated participants split by ordinary stratified K-fold
  stop.
- **Class support:** a training, calibration, or test fold missing a required
  class stops.
- **Calibration:** a probability request without an approved calibration
  design stops; `probability=True` is not enabled automatically.
- **Metric:** pooled `cross_val_predict` AUC is rejected as the default.
- **Version:** a synthetic older installed release is recorded rather than silently using `1.9.0`
  syntax or defaults.
- **Weights:** nonlinear SVC exposes no linear coefficient map; linear weights
  remain conditional decoder parameters.
- **Checkpoint:** outer evaluation does not authorize final refit.
- **Clinical boundary:** predictive discrimination is not called diagnosis or
  clinical utility.
- **Output:** collision, early holdout access, retry, or parameter change
  reopens Gate 2.
