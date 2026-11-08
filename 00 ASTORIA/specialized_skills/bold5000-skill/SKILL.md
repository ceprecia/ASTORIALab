---
name: bold5000-skill
description: >-
  Evaluates whether one exact BOLD5000 release, participant, session, stimulus
  set, behavioral or physiological record, raw product, processed product, or
  subset can support a user-supplied visual-neuroscience design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching BOLD5000
  question. It keeps KiltHub Release 2.0 separate from OpenNeuro Release 1 and
  other products; distinguishes four-person, complete-participant, session,
  trial, and unique-stimulus grains; preserves incomplete CSI4 coverage,
  stimulus-rights, product-provenance, and generalization boundaries; and
  records only user-selected scope after two approval gates. Triggers: can
  BOLD5000 support my study, BOLD5000 session and stimulus selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: general
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized download or stimulus use requires verification of the selected repository's access terms and applicable image rights
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# BOLD5000 Dataset Suitability

Evaluate one exact BOLD5000 evidence state without conflating participants,
sessions, trials, unique images, raw products, or Release 2 response estimates.

## Purpose

It does not download stimuli or imaging, choose participants or stimuli, infer labels, organize files, preprocess, estimate responses, set QC exclusions, train or evaluate models, analyze data, make scientific claims, search broadly, or save without separate approval.

`bold5000-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about BOLD5000.

It owns:

- pinning the exact release, participant, session, run, stimulus, trial,
  behavioral or physiological record, raw product, processed product, and
  access state;
- keeping KiltHub Release 2.0, OpenNeuro Release 1, original Figshare products,
  and third-party derivatives distinct;
- checking whether participant coverage, visual stimulus design, repetition,
  session structure, acquisition, physiology, behavior, product provenance,
  and stimulus rights support the stated design;
- comparing only credible participant, stimulus, source-product, and
  processed-product routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, participant choice, stimulus taxonomy,
response estimator, ROI, QC rule, model, train-test split, power target,
analysis, interpretation, or claim.

It never downloads imaging or stimuli, reorganizes files, preprocesses data,
estimates responses, excludes runs, constructs labels, trains a model, or
uploads or shares data.

Activate only when:

- The user invokes the exact trigger `bold5000-skill`; or
- a verified Active capability hands off one explicit BOLD5000 suitability or
  access-planning question.

Do not activate from `visual fMRI`, `image dataset`, `brain encoding`,
`download BOLD5000`, `train on BOLD5000`, or `analyze BOLD5000`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or stimulus-evidence questions, offer
a bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Participant, stimulus, trial, session, or response unit and target relation |
| Population boundary | Individual or cross-participant inference and generalization target |
| Stimulus needs | SUN, COCO, ImageNet, repeated images, labels, or exact image identities |
| Data requirements | Raw BOLD, response estimates, anatomy, diffusion, behavior, physiology, ROI, or QC |
| Release boundary | KiltHub Release 2.0, OpenNeuro Release 1, or exact other product |
| Rights boundary | Imaging license and selected stimulus-source rights |
| Intended handoff | Design, power, bounded literature search, curation, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the BOLD5000 Fit Brief

Return:

- exact scientific target and intended estimand;
- participant, session, run, trial, unique-stimulus, repetition, label,
  behavior, physiology, and response requirements;
- candidate release, product, processing, and rights state;
- within-participant, CSI4, stimulus-source, acquisition, missingness, QC,
  storage, and license constraints;
- known unknowns;
- requested output and stop point.

If the request is really download, stimulus selection, response estimation,
preprocessing, label construction, model training, or analysis, stop and route
it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact release page, snapshot, file inventory, documentation, processing
  record, stimulus-rights source, or supplied local metadata to inspect;
- whether participant-level data, copyrighted stimuli, credentials, restricted
  lanes, or protected paths would be encountered;
- participant, session, trial, stimulus, behavior, physiology, product,
  processing, and rights facts to verify;
- stop point before downloads, stimulus access, writes, or handoffs.

Ask:

> Approve this exact BOLD5000 source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize download, copying stimuli, participant-data inspection, search
expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- release, snapshot, DOI, date, repository, file inventory, and license;
- participants, sessions, runs, trials, unique images, repetitions, localizers,
  response rows, and files at the correct grain;
- CSI1 to CSI4 completeness;
- stimulus source, identity, label, repetition, and rights state;
- scanner, acquisition, anatomy, diffusion, physiology, behavior, and QC
  availability;
- raw, BIDS, filtered, preprocessed, ROI, and Release 2 response-estimate
  provenance;
- conflicts, unknowns, and facts requiring file-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, version, DOI, and repository | | | | |
| Participants and demographics | | | | |
| Sessions, runs, and localizers | | | | |
| Trials, unique images, and repetitions | | | | |
| CSI4 completeness | | | | |
| SUN, COCO, and ImageNet identity | | | | |
| Stimulus labels and rights | | | | |
| Task and behavioral response | | | | |
| Functional MRI and anatomy | | | | |
| Diffusion, physiology, and daily intake | | | | |
| Raw, BIDS, and processed products | | | | |
| Release 2 response estimates | | | | |
| QC, missingness, and known issues | | | | |
| License and citation | | | | |

Do not infer file-level availability from the general project website.

### 5. Build the Release and Product Map

| Requirement | KiltHub Release 2.0 | OpenNeuro Release 1 or exact original product | Exact evidence or mismatch |
|---|---|---|---|
| Participant and session coverage | | | |
| Trial and stimulus mapping | | | |
| Raw functional time series | | | |
| Response estimates | | | |
| Anatomy and diffusion | | | |
| Behavior and physiology | | | |
| ROI and QC products | | | |
| Processing provenance | | | |
| Stimulus files and rights | | | |
| License and citation | | | |

Keep raw acquisitions, BIDS assets, preprocessing, ROI products, and Release 2
estimates separate.

### 6. Build the Applicability Matrix

| Requirement | Exact dataset route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Individual or population inference | | | | | |
| Participant completeness | | | | | |
| Required sessions or runs | | | | | |
| Stimulus source and repetitions | | | | | |
| Behavior or physiology | | | | | |
| Raw or response-estimate product | | | | | |
| ROI, QC, or spatial state | | | | | |
| Stimulus-use rights | | | | | |
| Storage and access | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Rights Register

Check at minimum:

- four-person cohort and narrow graduate-student sampling;
- participant versus session, run, trial, unique-image, and repetition grains;
- CSI4 partial coverage;
- within-participant dependence and cross-participant generalization;
- trial ordering, repeated images, session effects, slow event timing, and
  localizer availability;
- like, dislike, neutral behavior and missing responses;
- scanner, headcase, acquisition, physiology, and motion or QC state;
- raw, filtered, BIDS, preprocessed, ROI, GLM, and percent-signal-change
  product provenance;
- response-estimation version and possible leakage across train, validation,
  or test sets;
- SUN, COCO, ImageNet, image-level rights, labels, and redistribution;
- CC0 release metadata versus third-party stimulus rights;
- whether intended claims exceed an intensive single-site visual experiment.

Do not select a stimulus ontology or model split based on available filenames.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact complete participant with raw or BIDS time series;
2. one exact complete-participant cross-person route;
3. one exact CSI4 partial-data route;
4. one exact Release 2 response-estimate product;
5. one exact stimulus family, repetition, behavior, or physiology subset;
6. defer because participant, session, stimulus, response, provenance, rights,
   storage, or inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- participant, session, repetition, processing, and rights assumptions;
- access and storage burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Release and Product Map;
- Applicability Matrix;
- Threat and Rights Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which BOLD5000 release, participants, sessions, stimuli, repetitions, behavioral or physiological records, products, rights assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize
download, stimulus copying, participant or stimulus selection, BIDS action,
preprocessing, response estimation, ROI choice, QC exclusion, model training,
power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, version, DOI, repository, participant, session, run, trial,
   unique-stimulus, and access state;
3. population and generalization boundary;
4. required stimuli, repetitions, labels, behavior, physiology, modalities,
   ROI, QC, and response products;
5. raw or processed product provenance;
6. participant, CSI4, session, repetition, acquisition, missingness, QC,
   response-estimation, and leakage threats;
7. release license, stimulus rights, citation, storage, sharing, and
   redistribution duties;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a visual, neural, model,
or scientific conclusion.

### 11. Verify and stop

Verify:

- release and access claims are dated;
- KiltHub Release 2.0, OpenNeuro Release 1, and original products remain
  distinct;
- participants, sessions, runs, trials, unique images, and repetitions are not
  conflated;
- CSI4 remains partial;
- raw, BIDS, preprocessed, ROI, and response-estimate products remain distinct;
- stimulus-source and image-level rights are verified;
- within-participant dependence and generalization limits remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no download, stimulus copy, selection, write, preprocessing, response
  estimation, model training, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- participant, session, run, stimulus, repetition, ROI, response-product, and
  model candidates;
- treatment of CSI4 incompleteness, within-person dependence, stimulus source,
  repetition, session, acquisition, behavior, physiology, QC, and
  generalization;
- every access, sampling, analytic, model, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and product constraints. It does not choose a
participant, stimulus split, label ontology, response estimator, or encoding
model for the user.

Use this order:

1. current official BOLD5000 website and release pages;
2. exact KiltHub Release 2.0 record, file inventory, documentation, and
   processing repository;
3. exact OpenNeuro `ds001499` snapshot and original Figshare records;
4. primary Scientific Data paper and methods supplements;
5. source-dataset terms for SUN, COCO, ImageNet, and individual stimuli;
6. user-supplied local documentation;
7. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-product fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never let a processed response matrix, paper-specific subset, or third-party
derivative redefine the source acquisition.

> [!info] References
> Read `./references/bold5000_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “BOLD” is supplied**: ask whether BOLD5000 is intended and what exact
  scientific requirement is in scope.
- **Five thousand participants are assumed**: correct the name-based error and
  preserve the four-person cohort.
- **5,254 stimuli are called unique**: distinguish trials from 4,916 unique
  images and the repetition structure.
- **All four people are called complete**: preserve CSI4's nine functional
  sessions and 3,108 trials.
- **Release 2.0 is called raw BIDS**: identify it as an optimized
  response-estimation release and inspect exact products.
- **OpenNeuro `ds002785` is proposed**: reject it as AOMIC PIOP1, not
  BOLD5000. The BOLD5000 OpenNeuro accession is `ds001499`.
- **The KiltHub CC0 label is applied to every stimulus image**: verify source
  and image-level rights before copying or redistribution.
- **Trials are split randomly across training and testing**: expose repeated
  images, within-person dependence, and leakage risk.
- **Population claims are proposed**: expose the intensive four-person,
  single-site sampling boundary.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish visual-category validity, neural representation,
population representativeness, causal identification, response-estimator or
model superiority, leakage-free evaluation, power, analysis validity,
generalizability, or fitness for clinical use. It cannot guarantee that a
release, product, file, stimulus right, or endpoint remains current after it
was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about visual
  constructs, stimulus labels, response estimation, generalization, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when trial, repetition, session, participant, or
  stimulus structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact unit,
  participant structure, estimand, analysis, inference family, and loss
  assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact source and
  stimulus-rights boundary are legitimately available.
- Route download, stimulus transfer, curation, preprocessing, QC, response
  estimation, ROI construction, model training, evaluation, and interpretation
  to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- BOLD5000. (n.d.-a). *BOLD5000*. https://bold5000-dataset.github.io/website/
- BOLD5000. (n.d.-b). *BOLD5000* (ds001499, Version 1.3.1) [Data set]. OpenNeuro. https://openneuro.org/datasets/ds001499/versions/1.3.1
- BOLD5000. (n.d.-c). *Overview*. https://bold5000-dataset.github.io/website/overview.html
- BOLD5000. (2021). *BOLD5000 Release 2.0* (Version 2) [Data set]. KiltHub. https://doi.org/10.1184/R1/14456124
- Chang et al. (2019). [BOLD5000 dataset paper]. *Scientific Data, 6*, 49. https://www.nature.com/articles/s41597-019-0052-3
