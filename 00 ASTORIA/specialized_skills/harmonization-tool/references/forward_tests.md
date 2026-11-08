# Forward tests (harmonization-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive fit:** one approved known-site training partition, fixed
  covariates, method, version, schema, and model destination produces one
  estimator record without held-out contact.
- **Positive apply:** one approved known-site partition uses the fixed model
  and schema without refitting.
- **Negative:** `which harmonization method should I use?` routes to
  [statistical-analysis](../../../skills/statistical-analysis/SKILL.md).
- **Broad phrase:** `remove site effects` does not trigger this adapter.
- **Environment:** absent packages stop without installation.
- **Leakage:** a diagnosis target requested as a validation or test
  preservation covariate stops.
- **Confounding:** perfect site-target confounding or a demonstrated design-rank/overlap
  failure is exposed as nonidentifiable rather than solved by listing the
  target as protected; one single-class site alone does not establish failure.
- **Fallback:** candidate `NotImplementedError` to full-cohort `fit_transform`
  is rejected.
- **Unseen site:** leave-one-site-out application through standard
  neuroHarmonize stops because the held-out site is not represented in fit.
- **Category:** unseen sex, scanner, or other encoded level stops instead of
  becoming the reference level.
- **Covariate:** a requested missing covariate stops instead of being skipped.
- **Connectome:** diagonal and edge order are not silently destroyed by upper
  triangle reconstruction.
- **Diagnostic:** lower site R-squared alone does not produce a pass.
- **Transductive:** full-cohort fitting cannot support an external
  generalization claim.
- **Failure:** estimator and partial output evidence remain without method
  switching, bound changes, imputation, refitting, retry, or overwrite.
