---
name: mne-python-guide
description: >-
  Compares and specifies one approved nonclinical MNE-Python neurophysiology
  analysis route while separating data type, representation, preprocessing,
  measurement, source, decoding, inference, software, and claim boundaries
  without choosing a method or executing code. Triggers: which MNE route for my
  data, MNE analysis route.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: eeg
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# MNE-Python Analysis Guide

Specify one MNE-compatible analysis route without turning a software API or
example pipeline into the user's scientific design.

## Purpose

This is a conditional Part 4 method guide for nonclinical EEG, MEG, sEEG,
ECoG, NIRS, or related MNE-readable data. It compares I/O, preprocessing,
epochs and evoked responses, time-frequency, source, decoding, connectivity,
and visualization routes, with data contracts and downstream handoffs. It does
not choose the estimand, parameters, software execution, or interpretation.

The user owns data type, question, method, parameters, source assumptions, and
claim. [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) owns scalp-EEG measurement; [mne-eeg-tool](../mne-eeg-tool/SKILL.md) owns
one selected implementation operation.

Activate only for exact `mne-python-guide` or an approved handoff naming one
MNE method route. Do not trigger from generic MNE, EEG, MEG, epochs, or Python
requests. Out of scope: clinical use, automatic modality detection, full
pipelines, package installation, and code execution.

## Inputs

Obtain or mark missing: modality, file and metadata state, montage or sensor
geometry, sampling, events, reference, downstream estimand, candidate route,
preprocessing, source or decoding assumptions, inference, environment,
provenance, and claim. If modality, metadata, or estimand is missing, return
**MNE method intake incomplete**.

## Steps

### Gate 1: approve the MNE method boundary

Show modality, data and metadata, estimand, candidate route, preprocessing,
source or decoding assumptions, inference, provenance, alternatives, and claim.
Gate 1 authorizes comparison only.

### Gate 2: approve one method specification and handoff

Ask the user to select, revise, or reject the route, parameters, implementation
owner, output, and verification. Gate 2 authorizes a specification and bounded
handoff only; it does not authorize code, data access, installation, or writes.

Return:

```text
MNE-Python Method Specification
Modality, acquisition, and metadata:
Question, estimand, and data representation:
Preprocessing and measurement route:
Source, decoding, connectivity, or visualization assumptions:
Inference, leakage, multiplicity, and sensitivity:
Implementation handoff and verification:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Match the MNE object and method to the modality and acquisition. Do not infer
  sensor geometry, source space, or reference from a filename.
- Keep I/O, preprocessing, measurement, source, decoding, and inference as
  separate checkpoints. API convenience does not select a method.
- Record filters, reference, epoching, baseline, covariance, inverse or
  forward model, splits, leakage, permutation, and multiplicity assumptions.
- Route implementation to a separately approved adapter and return a neutral
  method specification. MNE plots or decoded scores do not establish a
  mechanism or clinical result.

Stop for clinical use; missing modality, metadata, or estimand; automatic
modality or method selection; source or decoding claims without required
geometry or split; unavailable owner; a request to install, execute, or
interpret an MNE output scientifically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Dale, A. M., Liu, A. K., Fischl, B. R., Buckner, R. L., Belliveau, J. W., Lewine, J. D., & Halgren, E. (2000). Dynamic statistical parametric mapping: Combining fMRI and MEG for high-resolution imaging of cortical activity. *Neuron, 26*(1), 55–67. https://doi.org/10.1016/S0896-6273(00)81138-1
- Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Goj, R., Jas, M., Brooks, T., Parkkonen, L., & Hämäläinen, M. S. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience, 7*, Article 267. https://doi.org/10.3389/fnins.2013.00267
- Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Parkkonen, L., & Hämäläinen, M. S. (2014). MNE software for processing MEG and EEG data. *NeuroImage, 86*, 446–460. https://doi.org/10.1016/j.neuroimage.2013.10.027
- Jas, M., Larson, E., Engemann, D. A., Leppäkangas, J., Taulu, S., Hämäläinen, M., & Gramfort, A. (2018). A reproducible MEG/EEG group study with the MNE software: Recommendations, quality assessments, and good practices. *Frontiers in Neuroscience, 12*, Article 530. https://doi.org/10.3389/fnins.2018.00530
- Maris, E., & Oostenveld, R. (2007). Nonparametric statistical testing of EEG- and MEG-data. *Journal of Neuroscience Methods, 164*(1), 177–190. https://doi.org/10.1016/j.jneumeth.2007.03.024
- MNE-Python. (n.d.). *MNE-Python* [Computer software]. https://mne.tools/stable/
