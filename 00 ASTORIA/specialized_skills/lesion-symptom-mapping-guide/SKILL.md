---
name: lesion-symptom-mapping-guide
description: >-
  Specifies one approved research-only lesion-symptom mapping estimand and
  comparison plan while preserving lesion masks, behavior, lesion volume,
  spatial dependence, disconnection, exchangeability, multiplicity, provenance,
  and clinical-boundary controls without analyzing data or making diagnoses.
  Triggers: plan a lesion symptom mapping analysis, VLSM estimand and
  comparison.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: smri
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Lesion-Symptom Mapping Guide

Specify one research-only lesion-symptom mapping route without converting an
association map into a clinical localization or causal claim.

## Purpose

This conditional Part 4 method guide compares voxel-based, multivariate,
disconnection, and network lesion mappings for one approved behavioral
estimand. It owns lesion-mask and behavior contracts, lesion-volume and
covariate control, spatial dependence, exchangeability, permutation and
multiplicity planning, and claim limits. It does not choose a clinical action,
analyze data, or interpret a lesion map diagnostically.

The user owns the question, behavior, lesion definition, method, covariates,
permutation, and claim. [smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI routing;
[cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential details.

Activate only for exact `lesion-symptom-mapping-guide` or an approved
research-only handoff. Do not trigger from patient diagnosis, prognosis,
surgery, treatment, or generic lesion requests. Out of scope: clinical
decision-making, individual prediction, administration, data execution, and
automatic localization.

## Inputs

Obtain or mark missing: research question, lesion mask and space, behavior and
measurement, sample and lesion distribution, lesion volume, covariates,
method, disconnection or network data, exchangeability, permutation, multiple
testing, validation, provenance, and permitted claim. If lesion space,
behavior, or research-only boundary is missing, return **lesion-mapping intake
incomplete**.

## Steps

### Gate 1: approve the research method boundary

Show lesion and behavior contracts, space, lesion distribution, volume,
covariates, candidate method, exchangeability, permutation, multiplicity,
validation, and claim. Gate 1 authorizes method comparison only.

### Gate 2: approve one complete specification

Ask the user to select, revise, or reject the method, covariates, null, permutation,
validation, reporting fields, and claim. Gate 2 authorizes a specification only;
it does not authorize data access, execution, or clinical interpretation.

Return:

```text
Lesion-Symptom Mapping Method Specification
Research question, behavioral estimand, and status:
Lesion masks, space, coverage, volume, and covariates:
Candidate VLSM, multivariate, disconnection, or network route:
Exchangeability, permutation, multiplicity, and validation:
Outcome contact, limitations, and permitted research claim:
Clinical-use stop point:
```

## Boundaries

Method rules:

- Lesions are nonrandom and spatially dependent. Preserve lesion prevalence,
  coverage, volume, and collinearity before interpreting any map.
- Control lesion volume and prespecified covariates; do not use post hoc
  nuisance selection to improve localization.
- Compare VLSM, multivariate, disconnection, and network routes against the
  estimand and data support. Permutation and FWE choices must be explicit.
- A map is an association under the selected design, not proof of a causal
  region, prognosis, diagnosis, or treatment target.

Stop for patient-specific diagnosis, prognosis, surgery, treatment, or
individual prediction; missing lesion or behavior contract; severe coverage or
volume confounding; unselected exchangeability; post hoc localization;
unavailable method owner; or a request to run analysis or call a lesion a
clinical target.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
