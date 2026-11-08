---
name: harmonization-tool
description: >-
  Implements one already approved multisite feature-harmonization fit,
  application, or diagnostic operation through an available, exact-version
  library and returns an exact partition, batch, covariate, estimator,
  transformation, output, validation, and provenance record. Use when the
  request names this skill or a verified Active method or analysis skill routes
  one exact harmonization handoff. It makes the estimand, feature grain,
  partitions, site levels, confounding, covariates, target access, method,
  version, model state, unseen-site behavior, memory, writes, diagnostics, and
  claim limits visible before execution. Triggers: harmonize multisite features,
  ComBat harmonization.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: multimodal
  dependencies: ""
  requires: Python, neuroHarmonize or neuroCombat
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Harmonization Tool

Implement one approved harmonization operation on already derived research
features while preserving partition and covariate provenance.

## Purpose

It does not choose ComBat, ComBat-GAM, CovBat, a split, protected covariates, or a pass threshold; install packages; use held-out outcomes; refit on all data after a split failure; silently handle unknown sites or categories; overwrite; or claim that lower site signal proves biological preservation or better generalization.

`harmonization-tool` owns:

- exact harmonization-library, API, version, and environment preflight;
- translation of one approved harmonization specification into inspectable
  fit, apply, or diagnostic code;
- feature, participant, partition, batch, covariate, encoder, estimator,
  model-state, memory, output, and side-effect control;
- one approved estimator fit, one approved application to one partition, or
  one approved diagnostic operation at a time;
- preservation of model, schema, warnings, failures, transformed outputs, and
  validation evidence;
- a Harmonization Operation Record.

The user owns the scientific question, need for harmonization, feature
construction, batch definition, target and covariates, causal assumptions,
split and evaluation design, method, reference site, empirical Bayes,
parametric form, nonlinear terms and bounds, treatment of missing data and
outliers, diagnostics, acceptance criteria, downstream model, interpretation,
and claims.

[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general statistical design and can hold the
method-selection handoff. [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns connectome
feature and edge meaning. Modality and preprocessing owners retain image,
pipeline, space, and QC decisions. This adapter does not create features,
choose a model, split data, train a downstream predictor, or make a
cross-site-generalization claim.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `harmonize`, `ComBat`, `ComBat-GAM`, `CovBat`, `site
effect`, `scanner effect`, `batch effect`, `multisite`, `mega-analysis`,
`leave-site-out`, or another broad method, problem, or evaluation term.

Do not use this skill to:

- decide whether site adjustment is scientifically justified;
- choose among harmonization methods or set covariates from age range,
  feature type, or package availability;
- create train, validation, or test partitions;
- download cohort data or extract imaging features;
- install, update, or clone neuroHarmonize, neuroCombat, CovBat, or another
  implementation;
- treat diagnosis, outcome, or test labels as ordinary preservation
  covariates;
- interpret harmonized features, train models, or write claims.

## Inputs

Obtain or mark missing:

- an approved Harmonization Specification and operation type: fit, apply, or
  diagnostic;
- scientific estimand and reason the adjustment is needed;
- feature matrix, hashes, feature names, grain, shape, dtype, units,
  preprocessing, space, atlas, and extraction provenance;
- participant identifiers and one-to-one metadata alignment;
- immutable train, validation, test, fold, family, site, and cohort
  partitions, or an explicit nonpredictive full-cohort design;
- batch column, site or scanner levels, sample counts, reference level, and
  acquisition meaning;
- approved target-free preservation covariates and whether each would be
  available at deployment or inference time;
- target and outcome access policy;
- missingness, outlier, duplicate, repeated-measures, longitudinal, and
  related-participant policy;
- selected method, public API, parameters, model form, empirical Bayes,
  parametric, mean-only, reference-batch, nonlinear-term, and bound choices;
- exact Python and package versions plus source and license state;
- categorical encoding schema fitted only on the authorized training data;
- known-site and unseen-site behavior;
- estimator serialization, model and schema destination, collision, memory,
  precision, random, thread, and rollback policy;
- diagnostic and biological-preservation checks plus their limitations;
- compute and destination authority.

If the estimand, split, batch, confounding, target access, covariates, method,
API, unseen-site behavior, estimator persistence, or validation plan is
unresolved, stop with **harmonization operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one operation

Choose exactly one already approved transition:

1. fit one harmonization estimator on one fixed training partition and save
   its exact state and encoding schema;
2. apply one approved fitted estimator to one fixed partition without
   refitting;
3. compute one approved outcome-blind diagnostic on fixed raw or transformed
   features.

Do not combine split creation, estimator fitting, application to several
partitions, downstream model training, and claim generation. Do not use
`fit_transform` as a shortcut across an evaluation cohort.

For an approved nonpredictive full-cohort analysis, label the operation
transductive and restrict claims to that cohort. Never reuse it as evidence of
held-out or unseen-site generalization.

### 2. Audit identifiability and leakage before data contact

Show:

- participant, family, site, cohort, repeated-measures, and fold separation;
- batch levels and sample counts by partition;
- target and each covariate by site;
- perfect or near confounding between site and target or preservation
  covariates;
- covariates unavailable at deployment;
- outcome, diagnosis, treatment, or future information that would enter fit
  or transform;
- unseen site or categorical levels in the application partition;
- duplicate participants or sessions across partitions;
- feature extraction or normalization fitted before the split.

Placing a target such as diagnosis in a preservation design does not solve
site-target confounding. Using held-out target values during transformation is
label leakage. Stop and return the nonidentifiability or leakage problem for
The user to resolve.

### 3. Preflight the exact implementation

Record:

- Python, harmonization package, NumPy, pandas, statsmodels, and transitive
  versions;
- public API signatures, source identity, license, and documented fit and
  apply behavior;
- training feature and covariate orientation, order, dtype, finite state, and
  memory;
- explicit site, categorical, continuous, nonlinear, reference, and
  empirical-Bayes arguments;
- categorical levels and column order learned on training data;
- estimator contents, serialization API, compatibility, and security limits;
- output shape, feature order, units, precision, diagonal and symmetry
  handling where applicable;
- destination, collision, temporary, atomic-write, and rollback state.

Current official review found neuroHarmonize `2.4.5` and neuroCombat `0.2.12`
as their current PyPI releases on 2026-07-23. The official CovBat repository
had no release. Its R package DESCRIPTION declared Artistic License 2.0, but
the repository root and Python implementation had no verified license; no
canonical `covbat` PyPI package was verified. Verify these packages in the user-selected participant environment. An unavailable package, unpinned source, or
unverified implementation license is a stop, not authorization to install or
substitute an implementation.

### 4. Gate 1: approve inspection and the operation contract

Show a **Harmonization Operation Contract**:

| Element | Approved meaning | Observed state | Leakage or side effect | Verification |
|---|---|---|---|---|
| Estimand and operation | | | | |
| Features and extraction provenance | | | | |
| Participants and partitions | | | | |
| Batch levels and confounding | | | | |
| Covariates and target access | | | | |
| Method, API, and versions | | | | |
| Encoding, model state, and unseen levels | | | | |
| Memory, outputs, and writes | | | | |
| Diagnostics and claim limits | | | | |

Gate 1 authorizes only displayed metadata, schema, partition, version, API,
confounding, memory, and destination inspection plus code construction. It
does not authorize feature loading beyond the approved bounded checks,
estimator fitting, transformation, package installation, imputation,
partition changes, output creation, or downstream modeling.

### 5. Eligible implementations of the approved harmonization

Keep the selected implementation of the approved harmonization method.
Compare forms only if a material implementation choice remains open under
the user's approval and more than one already available form implements the
same method and operation. The following forms may qualify.

1. the selected version-pinned library public API;
2. an existing reviewed project function using that same API;
3. a synthetic-fixture route using the same method and parameters.

For each show source state, supported fit and apply semantics, site-level
handling, encoding, model persistence, memory, output, reproducibility,
visible result, benefit, tradeoff, and limitation. These are implementation
forms, not alternative harmonization methods, covariates, or splits. Do not
propose installation.

### 6. Construct and audit exact code

For estimator fitting, display:

- training indices and hashes only;
- feature and metadata row reconciliation;
- batch, categorical, continuous, nonlinear, reference, and model arguments;
- training-only category schema and nonlinear bounds;
- complete-case or missing-data behavior;
- exact estimator serialization and model hash;
- no contact with held-out outcomes or features beyond approved schema checks.

For application, display:

- fitted estimator and schema hashes;
- partition indices and input hashes;
- permitted covariates available without outcome access;
- site and category compatibility;
- exact transform call with no fit, update, tuning, or fallback;
- output path, feature order, and round-trip invariants.

For diagnostics, display:

- partition and outcome-blinding boundary;
- prespecified site-removal, distribution, feature-preservation, reliability,
  negative-control, or downstream-stability check;
- uncertainty, multiplicity, and no-universal-threshold limit.

Never fall back from unsupported `transform` to full-cohort `fit_transform`.
Never encode an unknown application-site or covariate level as the training
reference. neuroHarmonize documents an error when holdout data contain a
different number of sites; standard train-site fitting therefore does not
support a leave-one-site-out application without a separately approved method
that handles unseen sites.

For connectomes, do not flatten and reconstruct while silently discarding the
diagonal, asymmetry, edge order, or missing-edge state. Preserve the approved
representation and exact feature index.

### 7. Review site assumptions and validation limits

Show:

- site-target and site-covariate confounding;
- Gaussian, location-scale, empirical-Bayes, independence, feature-similarity,
  nonlinear, reference-site, and covariance assumptions relevant to the
  method;
- small or singleton sites, imbalance, outliers, missingness, and
  extrapolation;
- transductive versus inductive design and known-site versus unseen-site
  scope;
- label or target access and deployment availability;
- category coding, rank deficiency, nonlinear-bound, precision, feature-order,
  and model-serialization risks;
- distributional and biological signals that the transformation may remove,
  distort, or preserve;
- what lower site predictability or site R-squared can and cannot establish;
- why improved accuracy, unchanged accuracy, or reduced batch association
  alone does not prove valid harmonization.

Do not call ComBat a de facto correct default, select ComBat-GAM from age
range, select CovBat from connectome shape, or describe a before-after site
metric as an honest proof of biological preservation.

### 8. Gate 2: approve one exact operation

Ask the user to approve:

- operation type, fixed partition, features, and hashes;
- batch, covariates, target-access boundary, and confounding disclosure;
- method, version, public API, exact code, and parameters;
- category schema, nonlinear bounds, reference level, model state, and
  unseen-site policy;
- memory, precision, random, thread, estimator, output, and collision state;
- diagnostics, verification, stop point, and claim limits;
- no-install, no-imputation, no-split-change, no-held-out-outcome,
  no-refit-on-apply, no-full-cohort-fallback, no-overwrite, no-retry,
  no-model-training, and no-chaining boundary.

Gate 2 authorizes only the displayed fit, apply, or diagnostic operation and
verification. Another fold, partition, method, covariate, reference site,
estimator update, diagnostic, retry, or downstream model requires new
approval.

### 9. Run the approved fit, apply, or diagnostic

Run only the approved code. Capture:

- environment, package versions, source identity, and public APIs;
- exact code, parameters, feature schema, and category encoding;
- participant and partition indices and hashes;
- batch levels, covariates, target-access audit, and confounding record;
- estimator contents, serialization path, model hash, and training-only
  provenance;
- application compatibility and absence of refitting;
- memory, precision, thread, random, runtime, warnings, exceptions, and
  deviations;
- created outputs, feature order, metadata, and hashes;
- prespecified structural and diagnostic results.

On an unknown site, category, out-of-bound smooth term, rank failure, missing
value, shape mismatch, warning escalation, exception, or unexpected output,
stop and preserve evidence. Do not remove a covariate, widen a bound, change a
site reference, impute, refit, relax the split, switch methods, retry, or
continue.

Return:

```text
Harmonization Operation Record
Approved estimand and operation:
Feature schema, provenance, and hashes:
Participants, partitions, and hashes:
Batch levels, sample counts, and confounding:
Covariates, target access, and deployment availability:
Method, environment, version, API, code, and parameters:
Encoding schema, reference, nonlinear, and unseen-site policy:
Estimator state, path, and hash:
Outputs, order, precision, and hashes:
Structural and prespecified diagnostic results:
Warnings, failures, deviations, and limitations:
Transductive or inductive claim boundary:
user-owned acceptance, downstream model, interpretation, and claim decision:
```

## Boundaries

- Stop if the method is selected from a candidate default or package
  availability.
- Stop on site-target nonidentifiability that the approved design does not
  address.
- Stop before any held-out outcome, diagnosis, treatment, or future
  information enters fit or transform.
- Stop on an unknown site or categorical level unless the selected method has
  an approved, documented behavior for it.
- Stop when a fit or transform API, estimator state, category schema, feature
  order, reference, or nonlinear bound cannot be reproduced exactly.
- Stop before any CovBat operation unless the exact selected implementation,
  source state, and applicable license have been independently verified. The
  R package's Artistic-2.0 declaration does not license an unverified Python
  implementation.
- Stop before any full-cohort fallback after a split-scoped transform failure.
- Stop before package installation, source cloning, data download,
  unapproved full-array contact, output overwrite, or downstream training.
- Never silently skip a missing preservation covariate.
- Never treat a lower site R-squared, lower site-classifier accuracy, or
  unchanged target accuracy as proof that biology was preserved.
- Never convert a transductive cohort adjustment into an external
  generalization claim.

## Harmonization partitions and validation

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Harmonization Operation Contract.** Audit partitions, confounding, covariates, target access, method assumptions, versions, estimator state, unseen levels, writes, diagnostics, and claim limits. This prevents silent target leakage and full-cohort fallback. This requires detailed design and metadata provenance. Nonidentifiability and out-of-distribution sites may remain unresolved.
- **Harmonization Operation Record.** Execute one approved fit, apply, or diagnostic once and preserve estimator, partition, and output evidence. This preserves exact authorization and fold provenance. Every partition transition needs a new approval. Structural checks cannot establish scientific validity.
- **Labeled public-API, reviewed-function, or fixture forms.** Compare only already available implementation forms for the same approved harmonization method and operation. This makes fit, apply, site-level, model-state, and write behavior visible without reopening method choice. This adds an implementation review. This cannot resolve an unidentified batch effect, split, or method.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and readiness comparison.** Run a synthetic fixture or one prespecified fold before a separately approved full evaluation. This can expose leakage, unknown-level, and persistence defects early. This adds a consequential checkpoint and compute. A passing fold does not guarantee cohort-wide validity.
- **Fixture design and expected invariants.** Add a synthetic multisite fixture with known biological and batch signals. This can reveal leakage, overcorrection, unknown-site, and encoding defects before observed-data contact. This adds simulation and validation work. Fixture performance does not establish study validity.
- **Independent leakage and preservation audit.** Add independent code review plus simulation and negative-control diagnostics. This improves detection of signal destruction and batch-removal artifacts. This adds review, compute, and multiplicity. Diagnostics cannot prove all relevant biology was preserved.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Chen et al. (2022). https://doi.org/10.1002/hbm.25688
- *CovBat_Harmonization* [Computer software]. (n.d.). GitHub. https://github.com/andy1764/CovBat_Harmonization
- Fortin et al. (2018). https://doi.org/10.1016/j.neuroimage.2017.11.024
- Johnson, Li, & Rabinovic (2007). https://doi.org/10.1093/biostatistics/kxj037
- *neuroCombat* (Version 0.2.12) [Computer software]. (2021). PyPI. https://pypi.org/project/neuroCombat/
- *neuroHarmonize* (Version 2.4.5) [Computer software]. (2024). PyPI. https://pypi.org/project/neuroHarmonize/
- Pomponio et al. (2020). https://doi.org/10.1016/j.neuroimage.2019.116450
