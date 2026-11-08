---
name: drift-diffusion-model
description: >-
  Specifies one approved nonclinical two-choice evidence-accumulation model
  comparison with explicit estimand, parameterization, identifiability,
  recovery, fit checks, and claim boundaries without choosing a model, fitting
  data, or interpreting latent parameters as processes. Triggers: fit a drift
  diffusion model, DDM parameterization and recovery.
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

# Drift Diffusion Model

Specify one DDM route without turning familiar parameter labels or trial-count
rules into automatic scientific decisions.

## Purpose

This is the Part 4 method owner for one approved nonclinical two-choice
evidence-accumulation model comparison. It owns the DDM estimand and
parameterization ledger, data sufficiency and identifiability checks,
candidate-variant comparison, recovery and posterior-predictive requirements,
and claim boundaries. It does not choose the user's question, fit data, select a
software package, or interpret a latent parameter as a cognitive process.

The user owns the task, prediction, confirmatory status, response mapping, model,
constraints, priors, fitting method, and claim. [experimental-design](../../skills/experimental-design/SKILL.md) owns
task design. [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inference, dependence, multiplicity,
and uncertainty.

Activate only for exact `drift-diffusion-model` or an approved handoff with a
two-choice response structure and response-time estimand. Do not trigger from
generic reaction-time, accuracy, decision, or Bayesian-model requests.

In scope: classic or expanded DDM comparisons for two-choice RT and accuracy,
hierarchical structure, parameter constraints, simulation-based recovery,
posterior-predictive checks, and model-comparison planning. Out of scope:
multi-choice race models without an explicit extension, go/no-go without a
selected single-boundary model, clinical claims, and automatic fitting.

## Inputs

Obtain or mark missing: question, prediction, estimand, status, task and
response coding, trial counts by participant and condition, correct and error
RTs, missingness, candidate models and alternatives, free and fixed parameters,
noise scaling, constraints, hierarchy, identifiability, recovery, validation,
and outcome contact. If response mapping, RT definition, candidate model,
scaling convention, or outcome-contact state is missing, return **DDM intake
incomplete**. Do not infer a DDM from two response labels alone.

## Steps

### Gate 1: approve the model-comparison boundary

Show the scientific contract, task and response mapping, RT and accuracy
estimands, data grain, candidate variants and alternatives, parameters and
constraints, scaling convention, identifiability threats, recovery plan,
validation checks, outcome-contact state, and limitations. Gate 1 authorizes
comparison planning only.

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Task and response mapping | | | | |
| DDM variant and alternatives | | | | |
| Free and fixed parameters | | | | |
| Scaling and constraints | | | | |
| Hierarchical structure | | | | |
| Recovery and predictive checks | | | | |
| Statistical handoff and claim | | | | |

### Gate 2: approve one complete specification

Ask the user to select, revise, or reject the task mapping, candidate model,
parameters, constraints, hierarchy, recovery, validation, reporting fields,
and permitted claim. Gate 2 authorizes a specification only; it does not
authorize data access, fitting, model selection, interpretation, or file writes.

Return:

```text
DDM Method Specification
Question, prediction, estimand, and status:
Task, response mapping, and RT definition:
Candidate model and rejected alternatives:
Parameters, constraints, and scaling convention:
Participant and condition structure:
Identifiability, recovery, and predictive checks:
Outcome-contact and deviation state:
Reporting fields and permitted claim:
Known limitations and stop point:
```

## Boundaries

Method rules:

- Drift, boundary separation, starting point, and nondecision time are model
  parameters, not direct measurements of evidence quality, caution, bias, or
  encoding. Interpretations require a construct-to-parameter argument.
- Record response boundaries, within-trial noise scaling, stationarity,
  distributional assumptions, parameter constraints, condition variation, and
  hierarchical structure. Do not import typical ranges or trial-count cutoffs
  as universal validity rules.
- Retain correct and error RT distributions, participant and condition grain,
  missingness, exclusions, and response coding. Mean RT and accuracy summaries
  are not substitutes for distributional information.
- Plan simulation-based parameter recovery under the proposed design and
  parameterization. Require posterior-predictive or equivalent checks,
  convergence diagnostics when Bayesian, and sensitivity to plausible
  preprocessing and model constraints.

Stop for missing two-choice response mapping; multi-choice or go/no-go data
without a selected extension; insufficient information to assess
identifiability; post hoc model selection without an exploratory label; a
request to fit or execute software; or a request to interpret a latent
parameter as a person-level cognitive trait.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Ratcliff (1978).
- Ratcliff & McKoon (2008).
- Voss, Nagler, & Lerche (2013).
- Wagenmakers, van der Maas, & Grasman (2007).
- Wiecki, Sofer, & Frank (2013).
