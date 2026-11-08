---
name: adni-skill
description: >-
  Evaluates whether one exact Alzheimer's Disease Neuroimaging Initiative phase,
  visit, cohort, modality, measure, file family, processing state, advisory
  state, or participant subset can support a user-supplied research design and
  produces a selection-bound Dataset Suitability and Access Specification. Use
  when the request, or a part coordinator, hands over an explicitly matching ADNI
  question. It pins a dated LONI IDA inventory; keeps ADNI1, GO, 2, 3, and 4
  protocols and participant pools distinct; maps longitudinal, diagnostic,
  imaging, biomarker, missingness, update, and Data Use Agreement boundaries;
  and records only user-selected scope after two approval gates. Triggers: can
  ADNI support my study, ADNI phase and cohort selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: aging
  dependencies: ""
  requires: ADNI data-use application (LONI)
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# ADNI Dataset Suitability

Evaluate one exact ADNI evidence state without treating a continuously updated,
multiphase archive as one fixed release or complete longitudinal cohort.

## Purpose

It does not apply for access, handle credentials, accept terms, inspect controlled participant-level data in an unapproved AI environment, download data, choose participants or diagnoses, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`adni-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about the Alzheimer's Disease Neuroimaging
Initiative.

It owns:

- pinning the exact ADNI phase, cohort, visit, participant grain, modality,
  measure, file family, processing state, advisory state, and access route;
- keeping ADNI1, ADNI-GO, ADNI2, ADNI3, and ADNI4 protocol and participant
  states distinct;
- checking whether population, diagnosis, visit, modality, biomarker,
  acquisition, processing, completeness, update, and governance support the
  stated design;
- comparing only credible phase, visit, modality, file, and subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnostic definition, disease-stage
model, participant selection, visit alignment, biomarker cutoff, QC rule,
covariate choice, power target, analysis, interpretation, or claim.

It never applies for access, handles credentials, accepts the Data Use
Agreement, exposes participant-level ADNI data to an unapproved third-party AI
tool, downloads data, reorganizes files, preprocesses imaging, excludes
participants, fits a model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `adni-skill`; or
- a verified Active capability hands off one explicit ADNI suitability or
  access-planning question.

Do not activate from `Alzheimer's`, `dementia`, `aging MRI`, `download ADNI`,
`process ADNI`, or `analyze ADNI`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast or relation, outcome, unit, and timing |
| Population boundary | Phase, age, diagnosis or biomarker state, and generalization target |
| Longitudinal needs | Visits, interval, change, conversion, attrition, and completeness |
| Data requirements | MRI, PET, biofluid, genetics, cognition, digital, clinical, or QC needs |
| Archive boundary | Exact phase, file family, query date, and advisory state |
| Access boundary | Public documentation only or separately verified approved environment |
| Intended handoff | Design, power, bounded literature search, secure curation, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the ADNI Fit Brief

Return:

- exact scientific target and intended estimand;
- phase, cohort, diagnosis, biomarker, visit, modality, measure, file, and
  query-date scope;
- candidate archive inventory, advisory state, and access route;
- longitudinal, diagnostic, scanner, protocol, processing, missingness,
  secure-compute, storage, publication, and governance constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection, secure
data handling, BIDS organization, preprocessing, diagnosis construction, or
analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact public ADNI page, policy, protocol, data dictionary, advisory, or
  user-supplied approved metadata source to inspect;
- whether any account, agreement, participant-level record, restricted lane,
  third-party service, or protected path would be encountered;
- phase, cohort, visit, modality, file, processing, advisory, and governance
  facts to verify;
- stop point before credentials, agreement acceptance, participant-level
  access, downloads, writes, or handoffs.

Ask:

> Approve this exact ADNI public-source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, an application, agreement acceptance, controlled-data
access, participant-level data exposure, download, search expansion, saving,
or another capability.

### 3. Pin the exact archive and access state

Record:

- ADNI phase, cohort, exact file family, archive query date, and data-dictionary
  state;
- participants, visits, assessments, images, biosamples, and files at the
  correct grain;
- diagnosis and biomarker fields with their visit and derivation;
- site, scanner, acquisition, protocol, processing, and QC state;
- completeness, attrition, missingness, corrections, withdrawals, removals,
  and current advisories;
- DUA version, approved user, declared team, purpose, environment, storage,
  sharing, AI containment, publication, and annual-update duties;
- conflicts, unknowns, and facts requiring approved IDA inspection.

If the exact state cannot be pinned without controlled-data access, mark it
**Unknown** and stop before a suitability conclusion.

### 4. Build the Archive and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Phase, cohort, query date, and file | | | | |
| Participants, visits, and observations | | | | |
| Diagnosis and transition state | | | | |
| Cognitive and clinical measures | | | | |
| Structural and functional MRI | | | | |
| Diffusion, ASL, and other MRI | | | | |
| PET tracers and processing | | | | |
| CSF, blood, and other biomarkers | | | | |
| Genetics, omics, and repository | | | | |
| Digital and remote measures | | | | |
| Scanner, protocol, and processing | | | | |
| Completeness, attrition, and advisories | | | | |
| DUA, AI containment, and governance | | | | |

Do not infer visit-level multimodal completeness from a phase-level modality
list.

### 5. Build the Phase and File Map

| Requirement | Exact ADNI phase and cohort | Exact file or image family | Exact evidence or mismatch |
|---|---|---|---|
| Population and diagnosis | | | |
| Baseline or longitudinal visits | | | |
| Cognitive or clinical endpoint | | | |
| MRI modality | | | |
| PET tracer | | | |
| Biofluid biomarker | | | |
| Genetics or omics | | | |
| Processing and QC | | | |
| Advisory state | | | |
| Repository and terms | | | |

Keep phases, visit codes, file updates, modalities, repositories, and
processing generations separate.

### 6. Build the Applicability Matrix

| Requirement | Exact archive route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Diagnosis or biomarker state | | | | | |
| Cross-sectional or change estimand | | | | | |
| Required visits and dates | | | | | |
| Modality or measure | | | | | |
| Phase and protocol compatibility | | | | | |
| Processing and advisory state | | | | | |
| Completeness and attrition tolerance | | | | | |
| DUA, containment, and storage | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- ADNI1, GO, 2, 3, and 4 phase and cohort identity;
- participant, visit, image, file, assay, and observation grains;
- diagnosis, conversion, reversion, biomarker, and visit timing;
- rolling daily and laboratory-specific updates;
- participant overlap and continuation across phases;
- site, scanner, field strength, vendor, protocol, acquisition, and processing
  changes;
- modality, tracer, biosample, cognitive, clinical, and QC completeness;
- attrition, informative missingness, withdrawals, removals, and advisories;
- March 2026 `381_S_` removal and any later updates;
- exact DUA, declared users, purpose, secure environment, AI containment,
  annual update, redistribution, derived-data, publication, acknowledgement,
  and manuscript-submission duties;
- whether the intended claim exceeds an observational convenience cohort.

Do not upload ADNI participant-level data to this chat or any unapproved
public-facing AI service.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact phase, cohort, visit, modality, and file family;
2. one exact phase-spanning longitudinal route with verified compatibility;
3. one exact diagnosis or biomarker-defined route with dated derivation;
4. one exact imaging-plus-biomarker complete-case or missing-data route;
5. one exact approved external genomics or omics repository route;
6. defer because population, phase, visit, modality, file, advisory,
   completeness, DUA, containment, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- diagnosis, visit, phase, scanner, processing, missingness, and advisory
  assumptions;
- access and governance burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Archive and Evidence Card;
- Phase and File Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which ADNI phase, cohort, visits, diagnoses or biomarkers, modalities, file states, advisories, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
application, agreement acceptance, credential, controlled-data inspection,
participant-level AI exposure, download, diagnosis or participant selection,
BIDS action, preprocessing, QC exclusion, power calculation, analysis, save,
or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact phase, cohort, query date, file, participant, visit, and access state;
3. diagnosis, transition, biomarker, population, and generalization boundary;
4. required modalities, measures, visits, dates, and processing state;
5. site, scanner, protocol, phase, visit, attrition, completeness, missingness,
   update, and advisory threats;
6. exact DUA, approved-user, declared-team, purpose, AI-containment, security,
   storage, sharing, publication, and annual-update duties;
7. selected assumptions and explicit non-assumptions;
8. unresolved gaps and disqualifying conditions;
9. downstream handoff packets;
10. verification and recheck schedule;
11. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnosis, disease,
biomarker, causal, or scientific conclusion.

### 11. Verify and stop

Verify:

- the archive query date and every material update are recorded;
- ADNI phases, cohorts, protocols, and participant pools remain distinct;
- participants, visits, images, files, assays, and observations are not
  conflated;
- diagnosis and biomarker states remain tied to visits and derivations;
- planned enrollment is not reported as released inventory;
- current advisories and withdrawals are checked;
- the March 2026 removal is respected unless superseded by official evidence;
- DUA, declared-user, AI-containment, redistribution, and publication duties
  remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, agreement acceptance, controlled-data access, participant
  exposure, download, selection, write, preprocessing, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- phase, cohort, diagnosis, visit, modality, biomarker, file, and participant
  candidates;
- treatment of diagnostic transitions, biomarker positivity, attrition,
  scanner, protocol, processing, missingness, advisories, and phase changes;
- every access, secure-compute, storage, sampling, analytic, and reporting
  decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and governance constraints. It does not define an
ADNI diagnostic group, harmonize phases, or construct a longitudinal sample
for the user.

Use public ADNI documentation and user-approved nonparticipant metadata only.
Do not inspect, quote, transmit, summarize, or upload participant-level raw or
derived ADNI data unless:

1. The user has valid current access;
2. the exact intended use is covered by the current Data Use Agreement;
3. the environment provides the required containment guarantees;
4. the data never enter a public-facing or otherwise unapproved AI service;
5. The user separately approves that bounded access.

If any condition is unverified, stop at public metadata-level guidance.

Use this order:

1. current official ADNI data, documentation, FAQ, advisory, DUA, and policy
   pages;
2. exact LONI IDA inventory and data dictionary viewed only in an approved
   environment;
3. phase-specific protocols, schedules of events, manuals, and processing
   documentation;
4. primary ADNI cohort and methods papers for historical context;
5. user-supplied local documentation that satisfies the DUA;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated inventory fact**
- **Selected-file fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never use a planned enrollment target, paper-specific analytic cohort, or
historical phase total as the current archive count.

> [!info] References
> Read `./references/adni_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “ADNI” is supplied**: ask for the exact phase, scientific requirement,
  and intended grain.
- **A single total sample size is requested**: explain that the rolling archive
  needs a dated query and exact phase, cohort, visit, modality, and file
  inventory.
- **ADNI4 target enrollment is treated as released data**: label it a planned
  target and inspect the current archive.
- **Baseline diagnosis is carried across visits**: require visit-specific
  diagnosis and conversion evidence.
- **All phases are pooled because names match**: expose protocol, scanner,
  measure, processing, and participant-continuation differences.
- **Participant-level rows are pasted into chat**: stop, do not process or
  repeat them, and return to the DUA and containment boundary.
- **A public AI or external notebook is proposed**: stop unless its containment
  guarantees and DUA compatibility are documented and approved.
- **A `381_S_` participant is present**: stop and follow the current data
  advisory and deletion instructions.
- **A fixed BIDS or fMRIPrep route is assumed**: return to exact phase, source,
  metadata, DUA, and approved curation planning.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnosis, disease progression, conversion,
biomarker positivity, population representativeness, causal identification,
phase harmonization, processing superiority, power, analysis validity,
generalizability, or fitness for clinical use. It cannot guarantee that a
rolling archive, advisory, file, agreement, protocol, or endpoint remains
current after the recorded query date.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about disease
  stage, biomarker validity, phase compatibility, processing, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when phase, visit, diagnosis, biomarker, or
  missingness structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant and visit units, estimand, analysis, inference family, attrition,
  and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available in an approved environment.
- Route access applications, credentials, agreements, secure transfer,
  storage, preprocessing, QC, diagnosis construction, participant selection,
  modeling, and interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- ADNI. (n.d.). *ADNI data*. https://adni.loni.usc.edu/data-samples/adni-data/
- ADNI. (n.d.). *ADNI data advisory*. https://adni.loni.usc.edu/news-publications/adni-data-advisory/
- ADNI. (n.d.). *ADNI data use agreement* [PDF]. https://adni.loni.usc.edu/wp-content/themes/adni_2023/documents/ADNI_Data_Use_Agreement.pdf
- ADNI. (n.d.). *ADNI documentation*. https://adni.loni.usc.edu/help-faqs/adni-documentation/
- ADNI. (n.d.). *FAQs*. https://adni.loni.usc.edu/help-faqs/faqs/
- ADNI. (2025, December 11). *TEAM-ADNI protocol* (Version 1.1) [PDF]. https://adni.loni.usc.edu/wp-content/uploads/2026/03/TEAM-ADNI_Protocol_v1.1_11Dec2025.pdf
