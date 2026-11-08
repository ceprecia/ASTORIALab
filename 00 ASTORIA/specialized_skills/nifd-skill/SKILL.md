---
name: nifd-skill
description: >-
  Evaluates whether one exact NIFD or FTLDNI archive state, clinical group,
  visit, modality, processed product, control subset, or governed use can
  support a user-supplied research design and produces a selection-bound Dataset
  Suitability and Access Specification. Use when the request, or a part coordinator,
  hands over an explicitly matching NIFD question. It treats LONI IDA as the
  current controlled-access authority; keeps NIFD distinct from 4RTNI, ALLFTD,
  the deleted OpenNeuro duplicate, and paper-specific combined cohorts;
  preserves shared-control, multisite, preliminary-product, update, and DUA
  boundaries; and records only user-selected scope after two approval gates.
  Triggers: can NIFD support my study, FTLDNI dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: clinical
  dependencies: ""
  requires: LONI access for NIFD
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# NIFD and FTLDNI Dataset Suitability

Evaluate one exact NIFD or FTLDNI evidence state without treating a controlled,
rolling archive as a public OpenNeuro release or importing counts from a
combined paper cohort.

## Purpose

It does not apply for access, handle credentials, accept terms, inspect controlled participant-level data, download data, choose participants or diagnoses, organize files, preprocess, set QC exclusions, analyze data, make scientific or clinical claims, search broadly, or save without separate approval.

`nifd-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about the Frontotemporal Lobar Degeneration
Neuroimaging Initiative, also called NIFD or FTLDNI.

It owns:

- pinning the exact archive query, clinical group, visit, modality, processed
  product, control subset, update state, and governed use;
- keeping NIFD distinct from 4RTNI, later ALLFTD, external UCSF cohorts, and
  deleted or stale OpenNeuro records;
- checking whether population, syndrome, visit, modality, multisite
  acquisition, control overlap, completeness, processing, and governance
  support the stated design;
- comparing only credible archive, modality, visit, product, and subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnosis definition, participant or
control selection, visit alignment, biomarker choice, QC rule, covariate
choice, power target, analysis, interpretation, or claim.

It never applies for access, handles credentials, accepts the Data Use
Agreement, inspects participant-level controlled data, downloads data,
reorganizes files, preprocesses imaging, excludes participants, fits a model,
or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `nifd-skill`; or
- a verified Active capability hands off one explicit NIFD or FTLDNI
  suitability or access-planning question.

Do not activate from `frontotemporal dementia`, `FTD imaging`, `NIFD download`,
`OpenNeuro ds004403`, `ALLFTD`, or `analyze NIFD`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, syndrome, contrast or change, outcome, unit, and timing |
| Population boundary | Clinical group, control source, and generalization target |
| Longitudinal needs | Visits, intervals, attrition, and completeness |
| Data requirements | Structural MRI, DTI, ASL, clinical, neuropsychological, or other exact need |
| Archive boundary | Exact NIFD query date, release or file state, and processed-product state |
| Access boundary | Public metadata only or separately verified approved environment |
| Intended handoff | Design, power, bounded literature search, secure curation, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the NIFD Fit Brief

Return:

- exact scientific target and intended estimand;
- syndrome, diagnosis, control, visit, modality, measure, processed-product,
  and completeness requirements;
- candidate archive query, version, update, and access state;
- shared-control, multisite, scanner, protocol, attrition, missingness,
  preliminary-processing, storage, and governance constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, controlled-data inspection,
participant or control selection, file organization, preprocessing, diagnosis
coding, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact public DUA, protocol, paper, archive metadata, update record, or
  user-supplied approved source to inspect;
- whether any account, agreement, participant-level record, restricted lane,
  external compute, or protected path would be encountered;
- archive, group, visit, modality, control-overlap, processing, update, and
  governance facts to verify;
- stop point before credentials, agreement acceptance, participant-level
  access, downloads, writes, or handoffs.

Ask:

> Approve this exact NIFD public-source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize an application, credentials, agreement acceptance, participant-level
access, download, search expansion, saving, or another capability.

### 3. Pin the exact archive and access state

Record:

- NIFD or FTLDNI identity, archive query date, release or file version, and
  processed-product state;
- participants, diagnoses, controls, visits, modalities, measures, files, and
  observations at the correct grain;
- NIFD-only versus shared 4RTNI controls;
- site, scanner, acquisition, protocol, processing, and QC state;
- completeness, attrition, missingness, preliminary status, corrections, and
  updates;
- approved user, team, purpose, environment, storage, sharing, publication,
  acknowledgement, and breach duties;
- conflicts, unknowns, and facts requiring approved IDA inspection.

If the exact state cannot be pinned without controlled-data access, mark it
**Unknown** and stop before a suitability conclusion.

### 4. Build the Archive and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| NIFD identity, query date, and version | | | | |
| Participants, diagnoses, and controls | | | | |
| NIFD and 4RTNI overlap | | | | |
| Visits and longitudinal intervals | | | | |
| Clinical and neuropsychological measures | | | | |
| Structural MRI | | | | |
| Diffusion imaging | | | | |
| ASL perfusion | | | | |
| Any other asserted modality | | | | |
| Sites, scanners, and protocols | | | | |
| Processed products and methods | | | | |
| Completeness, attrition, and updates | | | | |
| DUA, storage, and governance | | | | |

Do not infer current archive coverage from a paper's modality list.

### 5. Build the Identity and Product Map

| Requirement | Exact NIFD archive route | Neighboring or historical source | Exact evidence or mismatch |
|---|---|---|---|
| Population and diagnosis | | | |
| NIFD-only controls | | | |
| Shared 4RTNI controls | | | |
| Visits and change | | | |
| Structural MRI | | | |
| DTI or ASL | | | |
| Clinical or neuropsychological measures | | | |
| Processed product and version | | | |
| LONI DUA and access | | | |

Keep NIFD, 4RTNI, ALLFTD, `AG019724`, and deleted `ds004403` identities
separate.

### 6. Build the Applicability Matrix

| Requirement | Exact archive route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target syndrome and population | | | | | |
| Control source and independence | | | | | |
| Cross-sectional or change estimand | | | | | |
| Required visits and intervals | | | | | |
| Required modality or measure | | | | | |
| Site and protocol compatibility | | | | | |
| Processing and version state | | | | | |
| Completeness and attrition tolerance | | | | | |
| DUA, storage, and sharing | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- NIFD, FTLDNI, 4RTNI, ALLFTD, `AG019724`, and deleted OpenNeuro identity;
- participant, control, visit, scan, measure, file, and processed-output
  grains;
- shared controls and duplicate counting;
- clinical syndrome, diagnosis, pathology, and biomarker heterogeneity;
- visit intervals, attrition, and informative missingness;
- site, scanner, vendor, acquisition, protocol, and modality differences;
- structural, DTI, ASL, clinical, and neuropsychological completeness;
- whether a result is archive evidence or paper-specific analysis context;
- preliminary processed products, method changes, versions, and updates;
- exact DUA, declared users, purpose, safeguards, storage, redistribution,
  breach reporting, acknowledgements, and publication recheck duties;
- whether intended claims exceed an observational clinical cohort.

Do not upload controlled NIFD data to chat or unauthorized external compute.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact NIFD syndrome and visit state;
2. one exact NIFD longitudinal subset;
3. one exact NIFD structural, DTI, ASL, clinical, or neuropsychological route;
4. one exact processed product with pinned version and method;
5. one explicit NIFD-plus-4RTNI route with shared controls accounted for;
6. defer because identity, population, control, visit, modality, completeness,
   processing, DUA, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- syndrome, shared-control, visit, site, modality, missingness, and processing
  assumptions;
- access and governance burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Archive and Evidence Card;
- Identity and Product Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which NIFD archive state, syndromes, controls, visits, modalities, products, governance assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
application, agreement acceptance, credential, controlled-data inspection,
download, diagnosis, control or participant selection, BIDS action,
preprocessing, QC exclusion, power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact NIFD or FTLDNI archive, query date, version, participant, control,
   visit, and access state;
3. syndrome, diagnosis, pathology, biomarker, population, and generalization
   boundary;
4. required modalities, measures, visits, intervals, and processing state;
5. NIFD-only and shared-4RTNI control boundary;
6. site, scanner, protocol, visit, attrition, completeness, missingness,
   preliminary-product, version, and update threats;
7. DUA, approved-user, declared-team, purpose, safeguards, storage, sharing,
   breach, acknowledgement, and publication duties;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification and recheck schedule;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnosis, biomarker,
causal, clinical, or scientific conclusion.

### 11. Verify and stop

Verify:

- archive query date and version are recorded;
- NIFD, 4RTNI, ALLFTD, `AG019724`, and `ds004403` remain distinct;
- participants, controls, visits, scans, measures, and files are not
  conflated;
- shared controls are not counted twice;
- paper-specific counts are not called current archive counts;
- current modality and completeness claims come from the selected archive;
- preliminary processed products retain method and version;
- DUA, storage, redistribution, acknowledgement, and update duties remain
  visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, agreement acceptance, participant-level access, download,
  selection, write, preprocessing, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- archive, syndrome, diagnosis, visit, modality, product, control, and
  participant candidates;
- treatment of shared controls, multisite acquisition, syndrome
  heterogeneity, attrition, missingness, preliminary processing, and updates;
- every access, secure-storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and governance constraints. It does not classify
an FTD syndrome, select a shared control, or construct a longitudinal cohort
for the user.

Use the public LONI DUA and public source documentation only. Do not inspect,
quote, transmit, summarize, or upload NIFD participant-level raw or derived
data unless the user separately establishes:

1. a valid current LONI IDA approval;
2. the declared user, team, and analysis purpose;
3. institutional and IRB compliance;
4. a DUA-compatible secure environment and storage plan;
5. separate approval for the exact bounded access.

If any condition is unverified, stop at public metadata-level guidance.

Use this order:

1. current official LONI NIFD application and DUA;
2. exact LONI IDA inventory viewed only in an approved environment;
3. current NIFD or FTLDNI protocol, processed-product, and update records;
4. primary cohort and methods papers for dated context;
5. current UCSF pages only when their study identity is verified;
6. user-supplied local documentation that satisfies the DUA;
7. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated archive fact**
- **Selected-product fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never use a paper-specific combined cohort as the current NIFD archive
inventory.

> [!info] References
> Read `./references/nifd_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “NIFD” is supplied**: ask for the exact scientific requirement,
  syndrome, visit, and modality.
- **`ds004403` is proposed as public NIFD**: record that the OpenNeuro dataset
  was deleted as a duplicate and return to LONI.
- **Approximately 120 participants are assumed**: require a dated approved
  archive inventory.
- **The paper's 161 patients and 137 controls are called NIFD counts**:
  preserve its combined FTLDNI-plus-`AG019724` analytic cohort.
- **NIFD and 4RTNI are pooled**: detect shared controls before any sample
  arithmetic.
- **The old UCSF NIFD page is treated as current inventory**: identify its
  redirect to ALLFTD and return to LONI.
- **Every participant is assumed to have T1w, DTI, ASL, and clinical data**:
  inspect exact archive-level completeness.
- **PET is asserted**: leave it unknown unless the current approved inventory
  proves availability.
- **Participant-level data are pasted into chat**: stop, do not process or
  repeat them, and return to the DUA and secure-environment boundary.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnosis, pathology, disease progression,
clinical-trial endpoint validity, population representativeness, causal
identification, multisite harmonization, processing superiority, power,
analysis validity, generalizability, or fitness for clinical use. It cannot
guarantee that a rolling archive, processed product, agreement, protocol, or
endpoint remains current after the recorded query date.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about syndrome,
  endpoint validity, imaging change, multisite methods, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when syndrome, control, visit, modality, or
  repeated-observation structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant and visit units, control overlap, estimand, analysis, inference
  family, attrition, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available in an approved environment.
- Route access applications, credentials, agreements, secure transfer,
  storage, preprocessing, QC, diagnosis construction, participant selection,
  modeling, and interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- LONI. (n.d.). *NIFD data use agreement*. https://ida.loni.usc.edu/collaboration/access/appApply.jsp?project=NIFD
- Staffaroni et al. (2019). *Brain, 142*, 443–459. https://pmc.ncbi.nlm.nih.gov/articles/PMC6351779/
