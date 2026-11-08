---
name: bayesian-cognitive-model-builder
description: >-
  Reviews and specifies one approved hierarchical Bayesian cognitive model,
  including estimand, constraints, priors, pooling, computation, diagnostics,
  predictive checks, and implementation handoff without choosing the model,
  fitting data, or silently selecting software. Triggers: specify a hierarchical
  Bayesian cognitive model, priors and pooling for my cognitive model.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: behavior
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Bayesian Cognitive Model Builder

Review and specify one cognitive model before any probabilistic-programming
implementation begins.

## Purpose

This is the Part 4 method and implementation-handoff owner for one approved
nonclinical Bayesian cognitive model. It owns model-review questions, parameter
constraints, prior and pooling comparison, identifiability, computational
diagnostics, predictive checks, and a bounded implementation brief. It does not
choose the user's theory, fit data, select a package, or interpret posterior
parameters as established cognitive processes.

The user owns the question, construct, predictions, model, priors, pooling,
likelihood, software, sampler, thresholds, and claim. [cogsci-statistics](../cogsci-statistics/SKILL.md)
owns general inferential interpretation. [drift-diffusion-model](../drift-diffusion-model/SKILL.md) owns DDM
method comparison when the approved model is a DDM.

Activate only for exact `bayesian-cognitive-model-builder` or an approved
handoff with a named cognitive model and estimand. Do not trigger from a broad
Bayesian statistics, regression, or coding request.

In scope: hierarchical cognitive models, constrained parameters, prior and
prior-predictive review, partial pooling, identifiability, sampler diagnostics,
posterior predictive checks, model comparison planning, and implementation
handoff. Out of scope: clinical claims, automatic model invention, data access,
fitting, package installation, or unreviewed code execution.

## Inputs

Obtain or mark missing: question and construct, prediction, confirmatory status,
observational unit, likelihood, parameters and constraints, grouping and
pooling, prior candidates and rationale, prior-predictive plan, identifiability
threats, computational route, diagnostic plan, posterior-predictive checks,
model-comparison rule, data provenance, and outcome contact. If the estimand,
likelihood, parameter constraints, or claim is missing, return **Bayesian model
intake incomplete**.

## Steps

### Gate 1: approve the model-review boundary

Show the construct and estimand, likelihood, parameters and constraints,
pooling candidates, prior candidates and observable implications,
identifiability threats, computational alternatives, diagnostics, predictive
checks, comparison rule, outcome-contact state, and limitations. Gate 1
authorizes review and comparison planning only.

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Cognitive construct and estimand | | | | |
| Likelihood and observation model | | | | |
| Parameter constraints | | | | |
| Priors and prior predictive checks | | | | |
| Pooling and grouping | | | | |
| Identifiability and recovery | | | | |
| Computation and diagnostics | | | | |
| Comparison and permitted claim | | | | |

### Gate 2: approve the implementation brief

Ask the user to select, revise, or reject the model, priors, pooling, computation,
diagnostics, predictive checks, comparison rule, reporting fields, and claim.
Gate 2 authorizes an implementation brief only. It does not authorize data
access, fitting, package installation, external writes, or interpretation.

Return:

```text
Bayesian Cognitive Model Implementation Brief
Question, construct, prediction, and status:
Estimand, likelihood, and observation model:
Parameters, constraints, and transformations:
Prior candidates and prior-predictive plan:
Pooling and grouping structure:
Identifiability and recovery plan:
Software and sampler route, if selected:
Diagnostics and posterior-predictive checks:
Comparison rule and permitted claim:
Outcome-contact, limitations, and stop point:
```

## Boundaries

Review rules:

- Separate the scientific model from the software implementation. A Stan or
  PyMC feature does not justify a modeling choice.
- Encode known parameter support explicitly, but do not label a prior
  "noninformative" without showing its implications on the observable scale.
  Compare prior-predictive simulations and retain the rationale for the chosen
  alternative.
- Compare complete, partial, and no pooling against the grouping and data
  structure. Partial pooling is a candidate, not an automatic default.
- Check parameter recovery and practical identifiability under the proposed
  design. A converged sampler does not establish that the parameters are
  identified or that the theory is supported.
- Require rank-normalized convergence diagnostics, effective sample checks,
  divergent-transition review, and posterior-predictive checks when fitting is
  later authorized. Do not turn numerical thresholds into universal validity
  claims.
- Separate model comparison from hypothesis confirmation. LOO, WAIC, Bayes
  factors, or another criterion must be selected and justified before use.

Stop for a missing estimand or likelihood; unconstrained parameters with no
observable-scale prior rationale; unidentified parameters; post hoc prior,
pooling, or model selection without an exploratory label; failed diagnostics or
predictive checks; a request to fit, install, execute, or write; or a request
to treat a posterior parameter as a person-level cognitive truth.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Betancourt & Girolami (2015).
- Gelman et al. (2013).
- Kruschke (2015).
- Lee & Wagenmakers (2014).
- Schad et al. (2021).
- Vehtari et al. (2021).
