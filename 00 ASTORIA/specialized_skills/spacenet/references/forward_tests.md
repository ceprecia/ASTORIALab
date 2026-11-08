# Forward tests (spacenet)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive evaluation:** one approved group-aware outer evaluation keeps
  the outer test sealed and returns sample-and-fold-keyed predictions.
- **Positive refit:** one separately approved final refit returns a frozen
  fitted state and class-mapped coefficients without claiming new
  performance.
- **Trigger:** Load for the explicit `spacenet` skill name, a bounded request such as `SpaceNet classifier on my volumes`, or an exact SpaceNet handoff from Neural Decoding Analysis, the fMRI or sMRI Coordinator, or Nilearn Tool.
- **Method selection:** `find the best disease classifier` routes to
  [neural-decoding-analysis](../../neural-decoding-analysis/SKILL.md) and does not select SpaceNet.
- **In-sample defect:** fitting and predicting the same images is rejected as
  validation.
- **Identity:** label rows and image paths aligned only by position stop.
- **Dependence:** repeated participants split across ordinary stratified folds
  stop.
- **Geometry:** mask or image affine mismatch stops.
- **Screening:** default 20 percent is exposed as target-aware; strict inner
  control considers disabling it with the compute tradeoff.
- **Groups:** group-aware inner splits are materialized explicitly because
  `fit(X, y)` does not accept a groups argument.
- **Multiclass:** decision-score columns and coefficient volumes preserve
  class identity.
- **Compatibility:** Nilearn `0.14.0` with scikit-learn `1.9.0` stops.
- **Availability:** missing Nilearn stops without installation.
- **Checkpoint:** outer evaluation does not authorize final refit.
- **Output:** existing destination, retry, changed fold, or changed parameter
  reopens Gate 2.
- **Interpretation:** sparse weights are not called neural effects or
  diagnostic regions.
