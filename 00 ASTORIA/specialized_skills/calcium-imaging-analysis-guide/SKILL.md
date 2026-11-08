---
name: calcium-imaging-analysis-guide
description: >-
  Specifies one approved nonclinical calcium-imaging measurement and QC route
  while preserving modality, indicator kinetics, motion, ROI, neuropil,
  fluorescence, deconvolution, sampling, provenance, and claim boundaries
  without choosing parameters or executing software. Triggers: plan my calcium
  imaging analysis, ROI and deconvolution route.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: calcium
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Calcium Imaging Analysis Guide

Specify one calcium-imaging analysis route without treating fluorescence or
deconvolved events as direct neural spikes or silently selecting corrections.

## Purpose

This conditional Part 4 method guide compares two-photon, miniscope, one-
photon, and fiber-photometry measurement issues, motion correction, ROI
extraction, neuropil, bleaching, indicator kinetics, deconvolution, QC, and
downstream aggregation. It does not choose the indicator, ROI method, model,
parameters, or biological claim.

The user owns modality, indicator, question, ROI, correction, deconvolution,
aggregation, and claim. Other software adapters own implementation only after
selection.

Activate only for exact `calcium-imaging-analysis-guide` or an approved handoff
naming one nonclinical calcium-imaging estimand. Do not trigger from generic
imaging, fluorescence, spike, or cell requests. Out of scope: clinical use,
automatic ROI or event inference, full-pipeline execution, and interpretation.

## Inputs

Obtain or mark missing: modality, indicator and kinetics, acquisition rate,
motion, field of view, ROI or cell unit, neuropil and bleaching state,
fluorescence measure, deconvolution candidate, behavior alignment, sampling,
QC, provenance, outcome contact, and claim. If modality, indicator, unit, or
estimand is missing, return **calcium-imaging intake incomplete**.

## Steps

### Gate 1: approve the calcium-imaging estimand

Show modality, indicator, acquisition, ROI unit, corrections, measure,
deconvolution, behavior alignment, QC, alternatives, and claim. Gate 1
authorizes method comparison only.

### Gate 2: approve one complete specification or handoff

Ask the user to select, revise, or reject the route, parameters, implementation
owner, output, and verification. Gate 2 authorizes a specification or bounded
handoff only; it does not authorize execution or interpretation.

Return:

```text
Calcium-Imaging Method Specification
Modality, indicator, acquisition, and sampling:
ROI/cell unit, motion, neuropil, bleaching, and fluorescence measure:
Deconvolution or event route and behavior alignment:
Animal, session, cell, QC, and sensitivity structure:
Implementation handoff, provenance, and verification:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve raw movies and metadata; distinguish fluorescence, dF/F, inferred
  events, and spikes.
- Match correction and deconvolution to indicator kinetics, sampling, motion,
  and noise. Do not import thresholds or event rates as universal defaults.
- Separate ROI detection, neuropil correction, bleaching, motion, and event
  inference. Report exclusions, missingness, and sensitivity.
- Preserve cell, field, animal, and session dependence. A fluorescent event or
  population pattern is not proof of a spike, cell type, or mechanism.

Stop for clinical use; missing indicator, sampling, modality, or ROI unit;
outcome-dependent ROI or event selection; treating dF/F or inferred events as
spikes; unavailable owner; or a request to execute, install, overwrite, or
interpret calcium signals biologically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Chen et al. (2013).
- Friedrich et al. (2017).
- Giovannucci et al. (2019).
- Pachitariu et al. (2017).
- Zhang et al. (2023).
