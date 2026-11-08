---
name: pymc
description: >-
  Implements one already approved Bayesian generative model through an
  available, version-verified PyMC API. Use when the request names this skill or
  a verified Active method or execution skill routes an exact Bayesian Model
  Specification. It records the model graph, dimensions, likelihood, priors and
  provenance, prior predictive implications, sampler or inference settings,
  compute budget, diagnostics, posterior predictive checks, prespecified
  comparisons, and neutral summaries. It does not choose the scientific model or
  priors, install packages, tune automatically, rank models as truth, hide
  diagnostic failures, or interpret scientific meaning. Triggers: build this
  Bayesian model in PyMC, PyMC sampling.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, PyMC
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# PyMC

Implement and verify one approved Bayesian generative model with the exact PyMC
version available in the selected environment.

## Purpose

`pymc` owns:

- PyMC version and API preflight;
- translation of one approved Bayesian Model Specification into a named model
  graph;
- dimensions, likelihood, links, priors, transforms, deterministic quantities,
  and parameterization implementation;
- approved prior predictive checks before observed-data fitting;
- one approved sampling or inference operation;
- convergence, geometry, effective-sample, posterior predictive, and
  prespecified comparison diagnostics;
- a PyMC Implementation Record.

The user owns the estimand, generative assumptions, likelihood, priors, prior
provenance, hierarchy, parameterization, inference method, compute budget,
diagnostic criteria, comparison set, summaries, interpretation, and claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns method-family comparison.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software execution control.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `Bayesian`, `posterior`, `MCMC`, `hierarchical model`,
`Bayes factor`, `sample`, or another broad term.

Do not use this skill to invent priors from observed outcomes, choose a
likelihood, select a sampler for convenience, install optional backends, or
automatically reparameterize, retune, add draws, compare, average, save, or
interpret models.

## Inputs

Obtain or mark missing:

- approved Bayesian Model Specification;
- likelihood, link, hierarchy, parameterization, and identification boundary;
- parameter names, dimensions, coordinates, units, and transformations;
- priors with scientific or calibration provenance;
- observed-data schema, missingness, censoring, and access boundary;
- prior predictive questions and acceptance criteria;
- inference method, sampler, chains or replicates, warmup, draws, seeds,
  initialization, and compute limits;
- diagnostic and posterior predictive criteria;
- requested posterior summaries and interval definition;
- prespecified comparison models, scoring rule, or averaging policy, if any;
- installed PyMC, PyTensor, ArviZ, backend, and hardware state;
- output destination and retention policy.

If the likelihood, prior, data-generating structure, diagnostic criteria, or
compute boundary is unresolved, stop with **Bayesian specification
incomplete**.

## Steps

### 1. Preflight the exact PyMC state

Record:

- Python, PyMC, PyTensor, ArviZ, sampler backend, and accelerator versions;
- public APIs and signatures needed by the approved specification;
- deprecations, default changes, optional extras, and output data structures;
- installed versus documented version mismatch;
- network, compilation, cache, temporary-file, and telemetry behavior.

PyMC `6.2.0` was current in official sources on 2026-07-23. Live use always
pins the installed state and matching documentation.

### 2. Gate 1: approve model implementation and prior checks

Show:

- model graph and dimension table;
- likelihood, priors, transforms, and parameterization;
- prior provenance and scaling;
- exact prior predictive plan;
- sampler or inference candidates allowed by the specification;
- compute and artifact plan;
- exact data fields that remain unread until Gate 2.

Gate 1 authorizes model construction with synthetic or prior-predictive draws
only. It does not authorize observed-data fitting, package changes, model
comparison, export, or saving.

### 3. Implementation forms for the approved model

Use the selected implementation of the approved model. Compare exact forms
only when a material implementation choice remains open under the user's
approval and the approved model permits more than one already available
form. The following forms may qualify.

- centered versus noncentered parameterization;
- a verified existing script versus a minimal named-dimension model;
- approved MCMC versus an explicitly accepted approximate inference route.

For each show model equivalence assumptions, geometry implications, compute
cost, diagnostic coverage, visible output, benefit, tradeoff, and limitation.
Do not reopen the scientific model.

### 4. Build and check the prior model

Produce:

| Component | Approved meaning | PyMC object | Shape and dimensions | Prior provenance | Verification |
|---|---|---|---|---|---|

Verify:

- dimensions, coordinates, broadcasting, observed and latent shapes;
- link and support compatibility;
- units, scaling, transformations, Jacobians, and deterministic quantities;
- prior predictive ranges, dependencies, impossible values, and tail behavior;
- reproducible seeds and exact code state.

An implausible prior predictive result returns to the user. Do not change a prior
silently.

### 5. Review inference and diagnostic choices

Show:

- exact inference or sampler API and arguments;
- initialization, warmup, draws, chains, seeds, parallelism, and compute budget;
- approved convergence, geometry, and effective-sample criteria;
- posterior predictive statistics and visual checks;
- requested summaries, interval definition, transformations, and units;
- prespecified model-comparison method and reliability diagnostics;
- failure and inconclusive conditions.

No chain count, draw count, target acceptance, prior family,
parameterization, diagnostic cutoff, or comparison label is universal.

### 6. Gate 2: approve observed-data execution

After reviewing the prior predictive record, ask the user to approve:

- exact model code and data;
- selected implementation form and inference operation;
- compute resources, seeds, and stop conditions;
- diagnostics, posterior predictive checks, summaries, and output destination;
- no-automatic-remediation boundary.

Gate 2 authorizes one displayed observed-data operation. Any prior,
parameterization, sampler, tuning, draw-count, comparison, or compute change
requires reopening Gate 2.

### 7. Run and verify the approved inference

Capture:

- code, model graph, data, environment, and version hashes;
- prior predictive record;
- exact sampling or inference call;
- runtime, warnings, errors, divergences, tree behavior, convergence,
  effective-sample, and termination evidence;
- posterior predictive checks;
- requested neutral summaries with scale and interval definition;
- comparison diagnostics only when prespecified;
- deviations, artifacts, and hashes.

Return:

```text
PyMC Implementation Record
Approved Bayesian Model Specification:
Versions and backend:
Model graph, dimensions, and code:
Likelihood and priors with provenance:
Prior predictive record:
Inference operation and compute:
Diagnostics and failures:
Posterior predictive checks:
Neutral posterior summaries:
Prespecified comparison evidence:
Specification-conformance check:
Unresolved limitations:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Stop when prior predictive implications violate approved criteria.
- Preserve divergences, poor mixing, low effective information, high
  convergence statistics, multimodality, unreliable importance sampling, or
  posterior predictive mismatch according to the approved criteria.
- Do not increase target acceptance, draws, warmup, chains, or compute
  automatically.
- Do not switch centeredness, priors, likelihood, sampler, or inference method
  automatically.
- Variational inference is an approximation and cannot silently replace the
  approved posterior computation.
- Information criteria and weights are uncertain predictive comparisons, not
  automatic model selectors or scientific truth.
- Posterior probability, credible intervals, or Bayes factors do not remove
  dependence on the specified model and priors.
- Successful sampling does not establish identification, calibration,
  robustness, causality, or a scientific conclusion.

## Bayesian inference and diagnostic records

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled parameterization or inference forms.** Compare only implementation forms allowed by the approved generative model. This exposes computational choices without choosing the science. This requires a complete model specification. This cannot resolve a scientifically ambiguous model.
- **Model and Inference Decision Record.** Expose priors, prior predictions, API choices, compute, diagnostics, and failure criteria. This makes Bayesian assumptions visible before outcomes. This extends the prefit review. This cannot guarantee posterior geometry.
- **PyMC Implementation Record.** Run one approved inference operation and preserve every diagnostic. This prevents silent tuning and model selection. Remediation requires new approval. One fit does not establish robustness.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Bayesian verification bundle.** Execute approved calibration, sensitivity, and predictive comparison sets. This tests selected computational and modeling sensitivities. This adds compute, multiplicity, and data contact. This requires separate explicit authorization.
- **Calibration design and result bundle.** Add simulation-based calibration for each form. This tests computational behavior under known generation. This adds major compute and implementation work. This depends on the supplied generative assumptions.
- **Prior robustness matrix.** Add independent prior elicitation and sensitivity families. This reveals prior dependence. This requires more scientific decisions and runs. Sensitivity sets can still omit plausible priors.

## Checks

- **Positive:** an approved hierarchical model yields a dimension audit, prior
  predictive record, exact sampling plan, diagnostics, and neutral summaries.
- **Negative:** `choose priors for me` stops and returns the decision to the user.
- **Edge:** unavailable PyMC or optional sampler produces an availability
  record and no install.
- **Failure:** divergences or predictive mismatch are preserved without
  automatic retuning or reparameterization.
- **Comparison:** unapproved LOO or model averaging does not run.
- **Handoff:** method ambiguity returns to [cogsci-statistics](../cogsci-statistics/SKILL.md); general
  execution control may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- PyMC. (n.d.). *Predictive-check workflow*. https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/posterior_predictive.html
- PyMC. (n.d.). *PyMC* (Version 6.2.0) [Computer software]. GitHub. https://github.com/pymc-devs/pymc/releases/tag/v6.2.0
- PyMC. (n.d.). *PyMC documentation* (Version 6.2.0). https://www.pymc.io/projects/docs/en/stable/
- PyMC. (n.d.). *pymc.sample*. https://www.pymc.io/projects/docs/en/stable/api/generated/pymc.sample.html
