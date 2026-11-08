---
name: mnd-skill
description: >-
  Evaluates whether one exact MND appetite-fMRI OpenNeuro release, case or
  control group, fasted or postprandial session, resting-state or food-cue task
  product, structural or diffusion product, phenotype field, derivative, or
  participant subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching ds005874
  question. It verifies the current release; distinguishes one-visit prandial
  sessions from longitudinal follow-up; preserves heterogeneous MND diagnoses,
  convenience controls, DWI additions and exceptions, motion, coil, processing,
  and completeness boundaries; and records only user-selected scope after two
  approval gates. Triggers: can the MND dataset support my study, MND OpenNeuro
  dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: clinical
  dependencies: ""
  requires: OpenNeuro access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# MND Appetite fMRI Dataset Suitability

Evaluate one exact `ds005874` evidence state without turning its fasted and
postprandial appetite design into a motor paradigm or longitudinal disease
study.

## Purpose

It does not download data, choose participants or diagnoses, organize files, preprocess, set QC exclusions, infer motor-task data, analyze data, make scientific or clinical claims, search broadly, or save without separate approval.

`mnd-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about the OpenNeuro Motor Neuron Disease
appetite-fMRI dataset.

It owns:

- pinning the exact release, participant, diagnostic group, session, prandial
  state, modality, task, phenotype field, derivative, exception, and access
  state;
- keeping release 1.1.0 distinct from the paper-era 1.0.0 state;
- checking whether population, control recruitment, diagnosis, prandial
  contrast, task, structural, diffusion, physiology, phenotype, motion,
  processing, and completeness support the stated design;
- comparing only credible group, session, modality, product, and subset
  routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnosis definition, participant
selection, task contrast, appetite endpoint, QC rule, preprocessing route,
covariate choice, power target, analysis, interpretation, or claim.

It never downloads data, reorganizes BIDS files, preprocesses imaging,
excludes participants, codes diagnoses, fits a model, or uploads or shares
data.

Activate only when:

- The user invokes the exact trigger `mnd-skill`; or
- a verified Active capability hands off one explicit `ds005874` suitability
  or access-planning question.

Do not activate from `MND`, `ALS`, `motor task`, `food fMRI`, `download
OpenNeuro`, or `analyze MND data`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, group or prandial contrast, outcome, unit, and timing |
| Population boundary | MND definition, control definition, age, and generalization target |
| Data requirements | Rest, food-cue task, T1w, T2w FLAIR, DWI, physiology, appetite, clinical, or QC needs |
| Session requirements | Fasted, postprandial, within-visit change, or another exact state |
| Release boundary | Snapshot 1.1.0 or exact later-state check |
| Access boundary | Approved public-document inspection and storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the MND Dataset Fit Brief

Return:

- exact scientific target and intended estimand;
- case, control, diagnosis, fasted, postprandial, modality, task, phenotype,
  derivative, and completeness requirements;
- candidate release, participant grain, exception, and access state;
- convenience-control, prandial, appetite, site, coil, protocol, DWI,
  motion, processing, missingness, and generalization constraints;
- known unknowns;
- requested output and stop point.

If the request is really download, participant selection, diagnosis coding,
BIDS action, preprocessing, QC exclusion, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact snapshot, README, CHANGES, participant table, phenotype dictionary,
  sidecar, derivative record, or supplied local metadata to inspect;
- whether participant-level records, credentials, restricted lanes, or
  protected paths would be encountered;
- release, participant, diagnosis, session, task, modality, exception,
  processing, completeness, and access facts to verify;
- stop point before downloads, writes, search expansion, or handoffs.

Ask:

> Approve this exact MND dataset source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize download, participant selection, search expansion, saving,
preprocessing, analysis, or another capability.

### 3. Pin the exact release and access state

Record:

- accession, snapshot, DOI, date, commit, BIDS version, and license;
- participants, diagnoses, sessions, runs, scans, phenotype rows, and
  derivative outputs at the correct grain;
- fasted, meal, postprandial, and scan-interval state;
- task conditions, rest instructions, structural, diffusion, physiology,
  appetite, clinical, and QC availability;
- `sub-17` DWI and `sub-43` coil and protocol exceptions;
- site, scanner, coil, acquisition, processing, and derivative provenance;
- conflicts, unknowns, and facts requiring file-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Accession, snapshot, DOI, and license | | | | |
| Participants and diagnostic groups | | | | |
| Control recruitment | | | | |
| Fasted and postprandial sessions | | | | |
| Resting-state fMRI | | | | |
| Food-cue task and conditions | | | | |
| T1w and T2w FLAIR | | | | |
| DWI and participant exceptions | | | | |
| Appetite, anthropometric, and clinical phenotype | | | | |
| Physiology | | | | |
| Site, scanner, coil, and protocol | | | | |
| fMRIPrep and PhysIO derivatives | | | | |
| Motion, completeness, and missingness | | | | |

Do not infer participant-level paired completeness from a release-level
modality list.

### 5. Build the Session and Product Map

| Requirement | Fasted session | Postprandial session | Exact evidence or mismatch |
|---|---|---|---|
| Resting-state fMRI | | | |
| Food-cue task fMRI | | | |
| T1w and T2w FLAIR | | | |
| DWI | | | |
| Physiology | | | |
| Appetite and clinical measures | | | |
| Raw product | | | |
| fMRIPrep or PhysIO derivative | | | |
| Participant exceptions | | | |

Keep sessions, modalities, raw products, and derivatives separate.

### 6. Build the Applicability Matrix

| Requirement | Exact dataset route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target MND population | | | | | |
| Control comparison | | | | | |
| Fasted or postprandial estimand | | | | | |
| Required rest or task run | | | | | |
| Structural or diffusion need | | | | | |
| Appetite or clinical phenotype | | | | | |
| Motion and completeness tolerance | | | | | |
| Raw or derivative product | | | | | |
| Access and storage | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- 36 heterogeneous MND cases and 23 convenience controls;
- ALS, PLS, undefined MND, and ALS-bvFTD labels;
- no prospective age matching;
- participants versus sessions, runs, scans, and phenotype rows;
- same-visit fasted and postprandial dependence;
- liquid meal, interval, task conditions, appetite timing, and carryover;
- rest instructions and any unresolved protocol fields;
- session-1 structural and session-2 diffusion structure;
- `sub-17` missing DWI;
- `sub-43` coil, TE, and TR differences;
- single-site scanner and acquisition;
- participant-level rest, task, physiology, phenotype, and derivative
  completeness;
- four high-motion MND participants and absence of a dataset-owned QC rule;
- raw, fMRIPrep, PhysIO, and MRtrix provenance;
- whether intended claims exceed a small convenience-control appetite study.

Do not inherit a fixed FD cutoff or translate food-cue viewing into motor
function.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact fasted resting-state or food-cue route;
2. one exact postprandial resting-state or food-cue route;
3. one exact within-visit prandial-change route;
4. one exact session-1 structural route;
5. one exact release-1.1.0 diffusion route with participant exceptions;
6. one exact physiology or phenotype-informed route;
7. one exact derivative route with pinned provenance;
8. defer because population, control, session, modality, task, phenotype,
   completeness, motion, or inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- diagnosis, control, prandial, coil, missingness, motion, and processing
  assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Session and Product Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which MND release, groups, sessions, modalities, food-cue conditions, phenotype fields, products, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize
download, participant or diagnosis selection, BIDS action, preprocessing, QC
exclusion, power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact accession, snapshot, DOI, commit, BIDS version, participant, session,
   and access state;
3. MND diagnosis, control-recruitment, population, and generalization boundary;
4. fasted, meal, postprandial, interval, rest, task, and condition boundary;
5. required structural, diffusion, physiology, appetite, clinical, QC, and
   derivative products;
6. `sub-17`, `sub-43`, site, scanner, coil, protocol, completeness, missingness,
   motion, and processing threats;
7. license, citation, storage, sharing, and redistribution duties;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnostic, appetite,
motor, causal, or scientific conclusion.

### 11. Verify and stop

Verify:

- release and access claims are dated;
- snapshot 1.1.0 and 1.0.0-era facts remain distinct;
- participants, sessions, runs, scans, and phenotype rows are not conflated;
- heterogeneous MND labels and convenience controls remain visible;
- fasted and postprandial sessions are not called longitudinal;
- the food-cue task is not called motor;
- session and modality availability is exact;
- `sub-17` and `sub-43` exceptions remain visible;
- raw, fMRIPrep, PhysIO, and MRtrix products remain distinct;
- motion evidence does not become an automatic exclusion;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no download, selection, write, preprocessing, QC exclusion, or analysis
  occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- diagnostic group, participant, session, prandial state, modality, task,
  phenotype, derivative, and subset candidates;
- treatment of heterogeneous MND diagnoses, convenience controls, appetite,
  coil, protocol, DWI missingness, motion, QC, and generalization;
- every access, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and design constraints. It does not collapse MND
subtypes, call controls age-matched, select a motion threshold, or choose a
prandial contrast for the user.

Use this order:

1. current official OpenNeuro snapshot and machine-readable metadata;
2. exact README, CHANGES, participant and phenotype tables, sidecars, and file
   tree;
3. current OpenNeuro access and publication terms;
4. primary Scientific Data paper and supplement;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-product fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never let a paper-specific analytic sample or diagnostic summary replace the
current released participant table.

> [!info] References
> Read `./references/mnd_dataset_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “MND” is supplied**: ask whether `ds005874` is intended and what one
  scientific requirement is in scope.
- **A motor task is requested**: correct the task to high-calorie,
  low-calorie, and non-food image viewing.
- **The two sessions are called longitudinal**: preserve the same-visit fasted
  and postprandial design.
- **Controls are called age-matched**: record convenience recruitment and
  distinguish a nonsignificant age difference from prospective matching.
- **All cases are called ALS**: preserve PLS, undefined MND, and ALS-bvFTD.
- **DWI is called absent**: distinguish 1.0.0 from 1.1.0 and inspect the
  participant exceptions.
- **DWI is called complete**: preserve missing `sub-17` and changed `sub-43`.
- **FD 0.5 is proposed as automatic exclusion**: treat the paper observation
  as evidence and return the QC rule to the user.
- **Eyes-open or eyes-closed is asserted**: require exact sidecar or protocol
  evidence.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnosis, disease mechanism, appetite mechanism,
motor function, longitudinal progression, population representativeness,
causal identification, QC validity, processing superiority, power, analysis
validity, generalizability, or fitness for clinical use. It cannot guarantee
that a release, file, participant exception, license, or endpoint remains
current after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about MND
  diagnosis, appetite measurement, food-cue validity, prandial effects,
  controls, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when case, control, meal, session, task, or
  repeated-observation structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact unit,
  diagnosis and control structure, estimand, analysis, inference family,
  motion, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact source is legitimately
  available.
- Route download, curation, preprocessing, QC, diagnosis coding, participant
  selection, modeling, and interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Chang et al. (2025, March 20). *Scientific Data, 12*, Article 466. https://www.nature.com/articles/s41597-025-04828-w
- *ds005874: MND* (Version 1.1.0) [Data set]. (n.d.). OpenNeuro. https://doi.org/10.18112/openneuro.ds005874.v1.1.0
