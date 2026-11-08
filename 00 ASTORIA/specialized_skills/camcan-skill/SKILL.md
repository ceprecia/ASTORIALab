---
name: camcan-skill
description: >-
  Evaluates whether one exact Cambridge Centre for Ageing and Neuroscience
  phase, arm, modality repository, task, measure, visit, or participant subset
  can support a user-supplied research design and produces a selection-bound
  Dataset Suitability and Access Specification. Use when the request, or a stage
  coordinator, hands over an explicitly matching CamCAN question. It verifies the
  current CBU portal and managed-access state; keeps phases, arms, modality
  repositories, people, and visits distinct; maps age sampling, MRI, MEG, task,
  coil-change, protocol, longitudinal, missingness, storage, and governance
  boundaries; and records only user-selected scope after two approval gates.
  Triggers: can Cam-CAN support my study, Cam-CAN phase and measure selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: aging
  dependencies: ""
  requires: Cam-CAN data access request
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# CamCAN Dataset Suitability

Evaluate one exact CamCAN state without accepting a false OpenNeuro accession,
license, MEG system, resting protocol, or automatic multimodal join.

## Purpose

It does not create accounts, submit proposals, accept terms, handle credentials, download data, choose participants, join repositories, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`camcan-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access question about the Cambridge Centre for Ageing and
Neuroscience.

It owns:

- pinning the exact phase, arm, modality repository, participant subset, visit,
  task, measure, acquisition state, access proposal, and data-use terms;
- separating people, visits, phases, arms, and modality-specific repositories;
- checking whether age sampling, modality, task, measure, visit, scanner, MEG
  system, coil state, and completeness support the stated design;
- comparing only credible CamCAN phase, arm, modality, or visit routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, aging model, cognitive-status
definition, participant selection, task contrast, QC rule, covariate choice,
power target, analysis, interpretation, or claim.

It never creates an account, submits an access proposal, accepts terms, handles
credentials, downloads data, joins repositories, preprocesses MRI or MEG,
excludes participants, fits a model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `camcan-skill`; or
- a verified Active capability hands off one explicit CamCAN suitability or
  access-planning question.

Do not activate from `CamCAN`, `Cam-CAN`, `ageing dataset`, `lifespan MRI`,
`MEG aging`, `download CamCAN`, or `analyze CamCAN`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, age or change relation, contrast, outcome, unit, and timing |
| Population boundary | Age range, screening, arm, health, and generalization target |
| Data requirements | T1, T2, DWI, MTI, rest, movie, sensorimotor fMRI, MEG, behavior, or QC |
| Longitudinal needs | Phase, visit, interval, repeated subset, and attrition |
| Repository boundary | Exact phase, arm, modality repository, or need to identify it |
| Access boundary | Approved public-document inspection and institutional storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the CamCAN Fit Brief

Return:

- exact scientific target and intended estimand;
- phase, arm, age, visit, modality, task, measure, and repository
  requirements;
- candidate participant, repeated, coil, protocol, and linkage states;
- access-proposal, supervisor, institutional storage, and transfer constraints;
- known unknowns;
- requested output and stop point.

If the request is really proposal submission, download, repository joining,
participant selection, preprocessing, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact current portal, phase, arm, modality, request, terms, protocol, news,
  correction, or supplied local sources to inspect;
- whether any account, proposal, participant-level record, SFTP state,
  restricted lane, or protected path would be encountered;
- phase, count, task, modality, coil, repository, and access facts to verify;
- stop point before credentials, proposals, term acceptance, downloads, writes,
  or handoffs.

Ask:

> Approve this exact CamCAN source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, proposal submission, term acceptance,
participant-level access, SFTP, download, search expansion, saving, or another
capability.

### 3. Pin the exact portal and repository state

Record:

- portal state, phase, arm, modality repository, version, manifest, and
  correction status;
- participants, visits, runs, files, tasks, and measures at the correct grain;
- MRI scanner, gradient coil, protocol, echo, shimming, and sequence state;
- MEG system, channel, task, and acquisition state;
- participant overlap across required repositories;
- current account, proposal, reviewer, terms, SFTP, storage, sharing, and
  dissemination conditions;
- conflicts, unknowns, and facts requiring approved-access verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Repository and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Portal, phase, arm, and repository | | | | |
| Population and age sampling | | | | |
| Participants and visits | | | | |
| T1, T2, DWI, and MTI | | | | |
| Resting fMRI | | | | |
| Movie fMRI | | | | |
| Sensorimotor fMRI | | | | |
| Resting, sensorimotor, and passive MEG | | | | |
| Behavioral, cognitive, and sensory measures | | | | |
| Scanner, gradient coil, and protocol | | | | |
| Cross-repository linkage | | | | |
| Missingness and quality | | | | |
| Access, SFTP, and storage terms | | | | |

Do not infer participant-level overlap from separate repository counts.

### 5. Build the Phase, Arm, and Modality Map

| Requirement | Phase 1 | Phase 2 Arm 1 | Phase 2 Arm 2 | Phase 3 | Exact evidence or mismatch |
|---|---|---|---|---|---|
| Recruitment and age | | | | | |
| Cross-sectional visit | | | | | |
| Repeated visit | | | | | |
| MRI modality | | | | | |
| fMRI task or rest | | | | | |
| MEG task or rest | | | | | |
| Cognitive or sensory measure | | | | | |
| Repository and overlap | | | | | |

Keep planned but unreleased phases separate.

### 6. Build the Applicability Matrix

| Requirement | Exact CamCAN route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target age and population | | | | | |
| Cross-sectional or change estimand | | | | | |
| Required phase and arm | | | | | |
| MRI, fMRI, or MEG modality | | | | | |
| Task, echo, and resting condition | | | | | |
| Cross-modality overlap | | | | | |
| Coil and protocol structure | | | | | |
| Missingness tolerance | | | | | |
| Access and storage terms | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- phase, arm, modality, repository, participant, and visit identity;
- CC700 target label versus per-modality counts and overlap;
- Phase 2 Arm 2 enrichment for low screening scores;
- Phase 3 repeated subset and one-to-three-year interval;
- age sampling, survivor selection, cohort effects, and attrition;
- separate MRI, fMRI, MEG, and behavioral repositories;
- single-echo rest and sensorimotor fMRI versus multi-echo movie fMRI;
- eyes-closed resting condition;
- Siemens MRI and Elekta 306-channel MEG systems;
- gradient-coil change after participant 97, B0, shimming, and covariate use;
- portal corrections, fiducials, known issues, and current manifests;
- proposal scope, supervisor, reviewer, SFTP, institutional-server, external
  drive, consumer-cloud, sharing, and dissemination duties;
- whether intended claims exceed an observational aging sample.

Do not describe the current data as CC0, one complete repository, or exactly
700 fully multimodal participants.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact Phase 2 Arm 1 modality repository;
2. one explicit Phase 2 Arm 2 design;
3. one verified Phase 3 repeated subset;
4. one exact MRI, fMRI, or MEG task route;
5. one verified cross-repository linked subset;
6. defer because age, arm, visit, modality, task, coil, linkage, access,
   storage, or completeness requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- aging, sampling, phase, coil, protocol, linkage, and missingness assumptions;
- access and storage burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Repository and Evidence Card;
- Phase, Arm, and Modality Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which CamCAN phase, arm, repositories, visits, modalities, tasks, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, proposal, term acceptance, credential, SFTP, download, participant
selection, repository join, BIDS action, preprocessing, QC exclusion, power
calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact portal, phase, arm, repository, version, participant, visit, and task
   state;
3. age, screening, health, and population boundary;
4. required MRI, fMRI, MEG, behavioral, cognitive, and sensory products;
5. participant overlap and longitudinal requirements;
6. scanner, gradient coil, echo, shimming, protocol, and known-issue evidence;
7. missingness, completeness, and quality limits;
8. account, proposal, supervisor, reviewer, terms, SFTP, institutional storage,
   sharing, and dissemination duties;
9. selected assumptions and explicit non-assumptions;
10. unresolved gaps and disqualifying conditions;
11. downstream handoff packets;
12. verification record;
13. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not an aging, cognitive,
clinical, or scientific conclusion.

### 11. Verify and stop

Verify:

- current portal, phase, repository, and terms claims are dated;
- OpenNeuro `ds003097` is not used for CamCAN;
- phase, arm, participant, visit, and per-modality counts remain distinct;
- CamCAN is not called wholly cross-sectional;
- MRI, MEG, echo, and resting-condition claims match official protocols;
- gradient-coil change remains visible;
- separate repositories are not silently joined;
- institutional storage and sharing limits remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, proposal, term acceptance, SFTP, download, join, selection,
  write, preprocessing, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether CamCAN is considered;
- the scientific question, target population, estimand, age relation,
  cognitive or sensory construct, contrast, outcome, and confirmatory status;
- phase, arm, modality, visit, task, measure, participant, and repository
  candidates;
- treatment of age sampling, low cognitive-screening scores, visit timing,
  coil change, site, missingness, and cross-modality linkage;
- every access, proposal, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and design limits. It does not choose an age model,
label cognitive impairment, or construct a multimodal cohort for the user.

Use this order:

1. current University of Cambridge CBU CamCAN Data Portal;
2. exact official phase, arm, repository, request, terms, news, correction,
   protocol, and modality documentation;
3. exact approved proposal scope and delivered manifest when legitimately
   available;
4. primary CamCAN cohort and repository papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated portal fact**
- **Selected-repository fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Do not treat the old CamCAN site, an external OpenNeuro accession, or the label
CC700 as a current exact data state.

Edge cases:

- **Only “CamCAN” is supplied**: Ask for the scientific requirement. Do not
  choose a phase, arm, modality, or repository.
- **CC700 is treated as 700 complete people**: inspect exact per-modality
  counts and participant overlap.
- **OpenNeuro `ds003097` is proposed**: identify it as AOMIC ID1000, not
  CamCAN.
- **CC0 is asserted**: correct it to the current managed proposal and terms.
- **A 275-channel CTF system is assumed**: return to the official
  306-channel Elekta Neuromag protocol.
- **Resting fMRI is called multi-echo or eyes open**: correct the protocol;
  movie fMRI is multi-echo and rest used eyes closed.
- **CamCAN is called wholly cross-sectional**: inspect the Phase 3 repeat
  subset.
- **Arm 2 is merged with CC700**: keep the low-screening enrichment visible.
- **Data are proposed for an external drive or consumer cloud**: stop under the
  current terms.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish normative aging, cognitive impairment,
longitudinal change, aging mechanism, causal identification, power, analysis
validity, generalizability, or fitness for clinical use. It cannot guarantee
that a portal, phase, repository, term, count, correction, or endpoint remains
current after it was last checked.

## CamCAN facts that control the review

Use these as dated orientation and recheck them at invocation:

- The current University of Cambridge CBU Data Portal replaced the old CamCAN
  site on 2025-08-21.
- Phases 1 through 3 are currently available. Phases 4 and 5 were planned for
  release in 2027 and must not be treated as available until verified.
- Phase 1 includes approximately 2,700 Cambridge-area adults recruited through
  general practices.
- Phase 2 Arm 1, commonly called CC700, aimed for 100 people per decade from
  ages 18 to 88. It is not 700 completely multimodal participants.
- Current official raw counts vary by modality: T1 653, T2 653, DWI 642,
  MTI 623, resting fMRI 652, movie fMRI 649, sensorimotor fMRI 651,
  resting MEG 647, sensorimotor MEG 647, and passive-sensory MEG 639.
- Phase 2 Arm 2 added approximately 80 participants, about half selected for
  low MMSE or ACE-R scores. It must not be silently merged with Arm 1.
- Phase 3 repeats more complex MRI and MEG tasks in a subset one to three years
  after Phase 2. CamCAN is therefore not wholly cross-sectional.
- Data are distributed as separate BIDS repositories by phase, arm, and
  modality, not one complete repository.
- MRI used a Siemens 3T MAGNETOM TrioTim. MEG used a 306-channel Elekta
  Neuromag Vectorview, not a 275-channel CTF system.
- Resting and sensorimotor fMRI are single-echo. Movie fMRI is multi-echo.
  Resting fMRI used eyes closed.
- After the first 97 participants, an MRI gradient-coil failure changed B0
  frequency and passive shimming. Coil type is provided as a covariate.
- Access is managed, not CC0. It requires an account, focused proposal,
  selected data types, reviewer approval, and acceptance of CamCAN terms.
- Students require a supervisor to apply. Approved data are delivered by SFTP,
  must remain on the institution’s server, and cannot be placed on external
  drives or consumer cloud storage under the current terms.
- OpenNeuro `ds003097` is AOMIC ID1000, not CamCAN.

Do not use a per-modality raw count as a linked multimodal sample count.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about CamCAN
  sampling, aging, task validity, coil effects, longitudinal follow-up, or
  prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when phase, arm, visit, task, or modality
  structure changes the design.
- Route power planning only after the user approves exact participant and visit
  units, overlap, estimand, design, analysis, inference family, and loss
  assumptions.
- Route BIDS curation only after an exact approved repository and separate
  specification are available.
- Route proposal administration, SFTP, download, storage, repository joining,
  preprocessing, QC, participant selection, modeling, and interpretation to
  separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *CamCAN* [Data set]. (n.d.). https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/
- [CamCAN CC700 MRI protocol parameters]. (n.d.). https://opendata.mrc-cbu.cam.ac.uk/wp-content/uploads/opendata/sites/10/2025/08/CAMCAN700_MR_params.pdf
- [CamCAN data access process]. (n.d.). https://opendata.mrc-cbu.cam.ac.uk/access/
- [CamCAN data request process]. (n.d.). https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/request/
