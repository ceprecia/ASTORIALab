# Forward tests (nilearn-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved `NiftiLabelsMasker` extraction with fixed BOLD,
  atlas, lookup table, confounds, sample mask, TR, parameters, versions, and
  empty output returns one Operation Record and method-owner QC handoff.
- **Negative:** `which denoising strategy should I use?` routes to
  [fmri-preprocessing-pipeline-guide](../../fmri-preprocessing-pipeline-guide/SKILL.md).
- **Broad phrase:** `use Nilearn` does not trigger this adapter.
- **Environment:** missing Nilearn stops without installation.
- **Confounds:** candidate motion and WM-CSF choices are not inherited.
- **Confound API:** passing a confounds TSV directly as the
  `load_confounds(img_files=...)` input is rejected.
- **Sample mask:** scrubbed or nonsteady-state volumes remain aligned across
  BOLD, confounds, events, and returned time series.
- **ICA-AROMA:** the removed fMRIPrep `--use-aroma` route is rejected as a
  current source.
- **Defaults:** Boolean standardization, fixed TR, smoothing, filter, dummy
  scans, and resampling target are rejected until approved explicitly.
- **Labels:** a lookup table mismatch stops instead of truncating names to the
  matrix dimension.
- **Resampling:** matching a target template grid does not establish MNI
  alignment without an approved transform and verified source-space
  provenance.
- **Connectivity:** default covariance shrinkage is disclosed and matrix
  bounds do not produce a scientific QC pass.
- **Leakage:** a fitted masker or estimator crossing a held-out participant,
  family, site, run, or test boundary stops.
- **Fetch:** an atlas fetcher stops before network contact or default
  `nilearn_data` writes.
- **Cache:** an implicit joblib cache path is surfaced before approval.
- **Model overlap:** GLM, ICA, dictionary learning, k-means, hierarchical
  parcellation, SVM, and SpaceNet requests route to their method and
  specialized owners.
- **Failure:** partial cache or output state is preserved without retry,
  parameter change, overwrite, or chaining.
