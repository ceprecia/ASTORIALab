---
name: nsd-skill
description: >-
  Evaluates from public metadata whether one exact Natural Scenes Dataset core,
  synthetic, or imagery source state, participant, session, image set,
  repetition, shared-image subset, fMRI product, auxiliary modality, prepared
  derivative, access state, or proposed subset can support one user-supplied
  design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching NSD question. It preserves the eight-participant
  dense-sampling, 7 T, 70,566-observed-image, participant-specific,
  repeated-image, shared-image, source-versus-prepared, addition, rights, and
  data-agreement boundaries after two approval gates. Triggers: can NSD support
  my study, Natural Scenes Dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: general
  dependencies: ""
  requires: NSD data-use terms; large download space
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Natural Scenes Dataset Suitability

Evaluate one exact NSD source and inference fit without turning a dense
individual-brain resource into an automatic visual-decoding pipeline.

## Purpose

It does not receive NSD data or stimuli, submit the agreement, download, inspect, redistribute, select images or participants, preprocess, encode, decode, train, analyze, search broadly, make scientific claims, or save without separate approval.

`nsd-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access-planning question about the Natural Scenes Dataset.

It pins the NSD core, NSD synthetic, or NSD imagery source state; participant,
session, image, trial, repetition, shared-image subset, modality, raw or
prepared product, access, and rights grain; compares only credible
metadata-level routes; and produces one user-selected Dataset Suitability and
Access Specification.

It does not own visual theory, method selection, image semantics, encoding,
decoding, alignment, reconstruction, preprocessing, or analysis. It never
submits the agreement, downloads data, receives participant-level files or
stimuli, opens images, selects observations, fits models, or redistributes.

Activate only when:

- The user invokes the exact trigger `nsd-skill`; or
- a verified Active capability hands off one explicit Natural Scenes Dataset
  suitability or access-planning question.

Do not activate from `NSD`, `natural scenes`, `visual neuroscience`, `7T
fMRI`, `COCO images`, `brain decoding`, `download NSD`, or `analyze NSD`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the image, participant, repetition,
generalization, comparison, or evaluation structure must be designed. Offer
[paper-search](../../skills/paper-search/SKILL.md) only for a separately approved bounded search about a visual
construct, NSD product, measurement, or prior result.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, estimand, and intended inference |
| NSD source | Core, synthetic, imagery, or an explicit unresolved comparison |
| Observation grain | Participant, session, image, trial, repetition, voxel, ROI, or prepared response |
| Generalization target | Within participant, held-out image, shared image, across participant, out-of-distribution, or another explicit target |
| Product need | Raw BIDS, prepared fMRI, structural, diffusion, localizer, rest, physiology, eye tracking, behavior, or metadata only |
| Image boundary | Exact image pool, shared subset, repeat rule, annotation need, and rights status |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should the Natural Scenes Dataset be evaluated against?

Then stop.

## Steps

### 1. Build the NSD Fit Brief

Restate the user-supplied target, source addition, observation grain, required
products, image set, generalization target, access boundary, and unresolved
terms. Separate facts from interpretation.

### 2. Gate 1: approve the public inspection boundary

Present:

1. exact question and intended inference;
2. exact public sources and dates;
3. metadata fields to inspect;
4. selected source, product, and generalization route, or evidence-supported
   alternatives for any material choice that remains open;
5. agreement, image-rights, and private-manual boundaries;
6. facts that cannot be verified without data access.

Gate 1 authorizes only the displayed public-source inspection. It does not
authorize form submission, term acceptance, downloads, data or stimulus
transfer, saving, preprocessing, modeling, or analysis.

Reopen Gate 1 if the source addition or inference target changes.

### 3. Pin exact source and access states

Record the official-page date, agreement and terms state, primary paper DOI,
core or addition identity, raw or prepared product state, repository or manual
version when authorized, image-rights state, and unresolved conflicts.

### 4. Build the Source and Access Card

| Field | Verified value | Source state | Status | Consequence |
|---|---|---|---|---|
| Core or addition | | | | |
| Participant and session inventory | | | | |
| Images, repeats, and shared subset | | | | |
| fMRI acquisition | | | | |
| Auxiliary modality | | | | |
| Raw or prepared product | | | | |
| Agreement and image rights | | | | |

### 5. Build the Grain and Product Map

Map every requested element to participant, session, run, image, trial,
repetition, voxel, ROI, or derivative grain; intended versus collected
inventory; raw versus prepared state; participant-specific versus shared-image
status; availability; and inherited preprocessing.

Never use image or trial count as participant count.

### 6. Build the Applicability Matrix

Use the matrix for the exact selected route. If a material choice remains
open, include only credible candidates needed to resolve it. The rows below
are examples.

| Route | Supports | Does not support | Assumptions | Leakage controls | Access state |
|---|---|---|---|---|---|
| Public metadata only | | | | | |
| Core within-participant | | | | | |
| Core shared-image | | | | | |
| Core across-participant | | | | | |
| Synthetic or imagery addition | | | | | |

Omit unused rows. If the selected route is inapplicable, report the blocker
without substituting another route.

### 7. Build the Threat and Governance Register

At minimum assess:

- eight-person population inference versus dense trial precision;
- participant, image, repeat, session, and temporal leakage;
- `shared1000` versus `shared515` and incomplete sessions;
- participant-specific image pools and cross-participant alignment;
- continuous-recognition memory effects contaminating pure-vision claims;
- raw, prepared, denoised, and third-party product conflation;
- partial and variable eye-tracking or physiological coverage;
- 7 T acquisition and target-population generalization;
- addition-versus-core conflation;
- COCO annotation and image-rights separation;
- access-agreement, nonredistribution, PHI, and institutional duties.

For each threat, show evidence, consequence, possible control, residual risk,
and the user's retained decision.

### 8. Assess the selected or eligible routes

Assess the exact selected NSD route for scientific fit, supported inference,
data grain, generalization, dependence, preprocessing provenance, completeness,
access, rights, and unknowns. Compare eligible alternatives on the same criteria
only if a material choice remains open and more than one route is credible.
Report any blocker on the selected route without substituting another. Do not
rank routes or select a model.

If no route fits, identify the unmet condition and stop.

### 9. Gate 2: select the specification

Present the complete cards, maps, matrix, and register, with a comparison
only when a material choice required one. The user confirms the recorded
choices and decides any open items for the source addition, product,
participant and image grain, shared or participant-specific subset,
generalization and holdout rule, inherited processing, rights limits,
unresolved caveats, and next stop or handoff.

Gate 2 authorizes only the selected Dataset Suitability and Access
Specification. It does not authorize access, downloads, data or image
transfer, participant or stimulus selection, preprocessing, encoding,
decoding, reconstruction, training, analysis, claims, saving, or a pipeline.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. question and intended inference;
2. pinned source, addition, agreement, and product states;
3. participant, session, image, trial, repeat, and response grains;
4. shared and participant-specific image boundary;
5. modality and completeness requirements;
6. generalization, holdout, and leakage controls;
7. raw or prepared provenance;
8. image-rights and access duties;
9. assumptions, conflicts, exclusions, and residual risks;
10. user-selected choices and any rejected alternatives that were evaluated;
11. separately approved handoff or explicit stop.

### 11. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- core, synthetic, and imagery remain separate;
- intended 73,000 and observed 70,566 images remain distinct;
- `shared1000` and `shared515` remain distinct;
- participants, sessions, images, trials, and repetitions are not conflated;
- prepared products are not called raw;
- eight participants are not treated as a large population sample;
- no NSD data, image, credential, or private manual entered the workflow;
- both gates bound their authorization;
- no scientific or downstream choice was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The current NSD Data Sharing and Usage Agreement permits research and
educational use, prohibits redistribution and monetization, requires team
members to comply, prohibits attempts to retrieve protected health
information, and requires citation and institutional compliance.

For this workflow:

- accept only public documentation, papers, aggregate inventory, schemas, and
  user-authored requirement summaries;
- do not ask the user to paste, attach, upload, or expose NSD participant files,
  prepared responses, eye-tracking records, physiological data, credentials,
  private manual links, or stimulus images;
- do not submit the access form or accept terms for the user;
- do not treat access approval as permission to send data to a public AI
  service;
- treat COCO image copyright and redistribution rights as distinct from NSD
  data access;
- stop if the answer requires licensed data or image inspection.

The agreement contains no explicit AI clause. The metadata-only rule is this
ASTORIA adaptation's conservative enforcement of nonredistribution,
human-subject, and institutional duties.

The user owns the scientific question, hypothesis, estimand, target population,
participant versus population inference, image and trial unit, source
addition, modality, response product, generalization target, split structure,
confirmatory status, access decision, final suitability judgment, and every
downstream action.

This skill exposes evidence and threats. It does not choose an encoding or
decoding model, interpret a representation, infer mental content, rank methods,
or treat many trials from eight people as a large population sample.

Use this order:

1. current official NSD page, access agreement, terms, and data manual when
   the user lawfully supplies the exact authorized version;
2. the primary paper for NSD core;
3. the primary paper and official page for each addition;
4. exact public repository or manifest documentation for a pinned product;
5. secondary papers for paper-specific subsets and methods only;
6. repository candidates as design evidence, never as dataset authority.

For every fact, record the source, date or version, URL or exact local state,
access status, observation grain, and whether it describes intended design,
collected data, current release, or one paper-specific subset.

Preserve conflicts between:

- intended 73,000 images and 70,566 observed distinct images;
- prescribed 40 sessions and collected 30 to 40 sessions;
- `shared1000` and the fully repeated `shared515`;
- raw BIDS, prepared responses, derivatives, and paper-specific products;
- NSD core, NSD synthetic, and NSD imagery;
- image, trial, repetition, session, participant, and voxel sample sizes.

Label missing fields `unknown` or `unverified`. Never fill a gap from the
candidate's scripts.

Edge cases:

- **NSD without source state:** distinguish core, synthetic, and imagery.
- **Data, betas, or images pasted into chat:** do not inspect them; return to
  public metadata.
- **73,000 called collected responses:** restore 73,000 intended images versus
  70,566 observed distinct images.
- **All shared images called fully repeated:** restore `shared1000` versus
  `shared515`.
- **A random trial split is proposed:** expose image, repetition, participant,
  and temporal leakage against the stated target.
- **Prepared betas called raw BIDS:** restore product and processing
  provenance.
- **Eye tracking assumed complete:** preserve its partial, variable-quality
  coverage.
- **COCO source called redistribution permission:** verify each image's rights.
- **Many trials called population power:** separate within-person precision
  from between-person generalization.
- **No suitable route:** return a blocked specification.

This skill cannot verify private data-manual content, current download state,
file completeness, image rights, participant or stimulus alignment, prepared
product quality, preprocessing validity, or model suitability. It cannot infer
mental content, establish population generalizability, or grant data access.
- Data access runs through the NSD Data Access Agreement (https://forms.gle/eT4jHxaWwYUDEf2i9); this skill never submits it.

## NSD facts that control the review

Use these facts only with their pinned source state.

### Core design and collected inventory

- NSD core measured eight healthy adult participants with whole-brain 7 T
  fMRI at 1.8 mm isotropic resolution and 1.6 second sampling.
- Participants completed 30 to 40 core sessions over about one year and viewed
  9,000 to 10,000 distinct color natural scenes in 22,000 to 30,000 trials.
- The intended design prepared 73,000 distinct COCO images, with 1,000 shared
  across participants and 9,000 participant-specific images per person, each
  intended for three presentations.
- The collected core contains responses to 70,566 distinct images. Because
  some participants completed 30 or 32 rather than 40 sessions, only 515 of
  the shared 1,000 images were viewed three times by all eight participants.
- The task was continuous recognition, not passive fixation. Participants
  reported whether they had previously seen each image during the experiment.
- One session contained 750 stimulus trials across 12 runs in the prescribed
  design. Do not assume every collected session or shared product is complete
  without a manifest.

### Modalities and products

- The current access form distinguishes task fMRI, resting-state fMRI,
  retinotopic and category localizers, T1, T2, venogram, angiogram, diffusion,
  physiological, eye-tracking, and behavioral data.
- It also distinguishes raw BIDS from extensively prepared data.
- The primary paper reports 30 to 40 core hours of fMRI per participant,
  substantial resting-state and diffusion data, functional localizers, and
  partial-session physiological and eye-tracking acquisition.
- Eye tracking was collected in only two to four sessions per participant and
  varied in quality. Do not describe it as complete for every NSD trial.
- Raw data, prepared responses, denoised estimates, surface or ROI products,
  stimulus metadata, and third-party derivatives are different products with
  different processing histories.
- COCO annotations do not make every image freely redistributable. Verify the
  underlying image rights for any proposed output.

### Addition and inference boundaries

- NSD core, NSD synthetic, and NSD imagery are separate acquisitions and
  source states. The official project page reports the synthetic addition
  released in March 2025 and the imagery addition released in September 2025.
- Dense repeated measurements support strong within-participant estimation but
  do not erase the eight-person population limit.
- Image repetitions, shared images, sessions, and nearby trials create
  dependence and leakage routes. A split must match the intended
  generalization target.
- Shared images enable cross-participant comparison, but participant identity,
  anatomy, response scale, preprocessing, and alignment remain substantive
  design choices.

## Design choices and verification

Check which NSD source, products, and images the current agreement permits for
the question. When a choice remains, compare only eligible source, product,
image, and generalization routes, including whether a route uses shared or participant-specific
images. Use the Source and Access Card to record provenance and rights, the
Grain Map and Applicability Matrix to check the proposed units and inference,
and the Threat Register to retain assumptions and conflicts. If only one
defensible route remains, identify it and explain what rules out the others.

After Gate 2, prepare and verify only the selected Dataset Suitability and
Access Specification. Stop before access, data inspection, preprocessing,
modeling, analysis or saving.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) for an approved repeated-image, shared-image,
  participant, addition, or evaluation-design comparison.
- Offer [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded evidence search.
- Route BIDS, preprocessing, encoding, decoding, or analysis only after the user
  selects the design and an appropriate owner exists.

Never chain a handoff automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Allen et al. (2021). A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence. *Nature Neuroscience, 25*, 116–126. https://doi.org/10.1038/s41593-021-00962-x
- *Data sharing and usage agreement*. (n.d.). https://cvnlab.slite.page/p/IB6BSeW_7o/Terms-and-Conditions
- *Natural Scenes Dataset* [Data set]. (n.d.). https://www.naturalscenesdataset.org/
