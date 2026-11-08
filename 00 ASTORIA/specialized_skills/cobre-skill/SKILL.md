---
name: cobre-skill
description: >-
  Evaluates whether one exact Center for Biomedical Research Excellence
  schizophrenia dataset state, modality, phenotype field, diagnostic group, or
  participant subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching COBRE question.
  It verifies the current NITRC file, account, request, and
  noncommercial-license state; maps participants, diagnostic evidence,
  structural MRI, resting-state fMRI, phenotype schema, acquisition,
  completeness, missingness, and governance; and records only user-selected
  scope after two approval gates. Triggers: can COBRE support my study, COBRE
  schizophrenia dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: clinical
  dependencies: ""
  requires: verified access through the current approved COBRE/INDI route
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-10-29"
---

# COBRE Dataset Suitability

Evaluate one exact COBRE evidence state without turning a diagnostic label,
fixed motion threshold, or external orchestration prompt into a classification
pipeline.

## Purpose

It does not create accounts, handle credentials, submit requests, download data, hardcode diagnosis labels, choose participants, organize files, preprocess, set QC exclusions, classify, analyze data, make clinical or scientific claims, search broadly, or save without separate approval.

`cobre-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access question about the Center for Biomedical Research
Excellence schizophrenia dataset distributed through INDI and NITRC.

It owns:

- pinning the exact current file list, manifest, participant state, modality,
  phenotype schema, diagnostic coding evidence, acquisition state, license,
  and access route;
- separating released participants from complete or analysis-ready
  participants;
- checking whether diagnostic, population, structural, resting-state,
  phenotype, acquisition, and governance evidence support the stated design;
- comparing only credible COBRE modality, phenotype, or subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnostic definition, group coding,
participant selection, QC rule, motion threshold, covariate choice, power
target, classification, analysis, interpretation, or claim.

It never creates an account, handles credentials, submits a NITRC request,
accepts terms, downloads data, reorganizes files, preprocesses imaging, labels
groups, excludes participants, fits a classifier, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `cobre-skill`; or
- a verified Active capability hands off one explicit COBRE suitability or
  access-planning question.

Do not activate from `COBRE`, `schizophrenia imaging`, `brain disorder
classification`, `resting-state benchmark`, `download COBRE`, or
`analyze COBRE`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For diagnosis, measurement, or prior-study evidence,
offer a bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, diagnostic or dimensional contrast, outcome, and unit |
| Population boundary | Age, diagnosis, control definition, medication, and exclusions under consideration |
| Data requirements | Multi-echo MPRAGE, resting-state fMRI, phenotype, acquisition, or QC needs |
| Release boundary | Candidate local or current NITRC state |
| Phenotype boundary | Required fields, coding evidence, and protected-data limits |
| Access boundary | Approved public-document inspection and noncommercial, institutional, or storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the COBRE Fit Brief

Return:

- exact scientific target and intended estimand;
- population, diagnostic, modality, phenotype, acquisition, and quality
  requirements;
- candidate local or NITRC file, manifest, participant, and access states;
- medication, illness, motion, completeness, license, and storage constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, download, group coding,
participant selection, preprocessing, classification, or analysis, stop and
route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release, NITRC request, terms, file list, manifest,
  acquisition, protected-schema, or supplied local sources to inspect;
- whether any account, request, participant-level record, phenotype file,
  restricted lane, or protected path would be encountered;
- file, count, diagnosis, modality, acquisition, license, and access facts to
  verify;
- stop point before credentials, requests, downloads, writes, or handoffs.

Ask:

> Approve this exact COBRE source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, access request, term acceptance,
participant-level access, protected phenotype display, download, search
expansion, saving, or another capability.

### 3. Pin the exact dataset and access state

Record:

- current official page, NITRC project, request, file list, manifest, hash, and
  access date;
- participant, group, modality, file, and phenotype counts at the correct
  grain;
- exact diagnosis field, codes, dictionary, missingness, and protection state;
- MPRAGE, resting-state, scanner, sequence, and acquisition metadata;
- current account, request, license, noncommercial, storage, sharing, and
  dissemination conditions;
- repository review warning, conflicts, unknowns, and required rechecks.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Dataset and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| File state and manifest | | | | |
| Population and recruitment | | | | |
| Schizophrenia and control records | | | | |
| Diagnostic instrument and coding | | | | |
| Age and demographic coverage | | | | |
| Medication and clinical variables | | | | |
| Multi-echo MPRAGE | | | | |
| Resting-state fMRI | | | | |
| Scanner, sequence, and acquisition | | | | |
| Phenotype fields | | | | |
| Missingness and quality | | | | |
| License and access | | | | |

Do not infer analysis readiness from release membership.

### 5. Build the Phenotype and Completeness Map

| Requirement | Exact field or file | Code or definition evidence | Participant-level completeness | Protected-data limit |
|---|---|---|---|---|
| Diagnosis | | | | |
| Age | | | | |
| Gender or sex field | | | | |
| Handedness | | | | |
| Medication or clinical measure | | | | |
| Structural MRI | | | | |
| Resting-state fMRI | | | | |
| Acquisition metadata | | | | |
| QC evidence | | | | |

Never hardcode schizophrenia as `1` or control as `2` without current schema
evidence.

### 6. Build the Applicability Matrix

| Requirement | Exact COBRE route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Diagnostic or dimensional construct | | | | | |
| Control definition | | | | | |
| Structural or resting modality | | | | | |
| Phenotype or clinical variable | | | | | |
| Acquisition structure | | | | | |
| Missingness and QC tolerance | | | | | |
| Noncommercial use | | | | | |
| Analysis-ready subset | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- released participant count versus future usable sample;
- diagnostic criteria, field, code, certainty, medication, and clinical
  heterogeneity;
- participant-level structural, resting, phenotype, and acquisition
  completeness;
- age, gender or sex, handedness, motion, and demographic structure;
- scanner, sequence, acquisition, temporal, recruitment, and batch effects;
- raw versus converted or derivative provenance;
- QC evidence versus user-owned exclusion rule;
- small-sample, imbalance, overfitting, leakage, and classification claims;
- repository-under-review warning and file integrity;
- NITRC account, request, license, attribution, noncommercial, storage,
  sharing, and dissemination duties;
- whether intended claims exceed a retrospective observational dataset.

Do not select a fixed framewise-displacement threshold or a machine-learning
model.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact structural MRI subset;
2. one exact resting-state fMRI subset;
3. one exact linked structural, resting, and phenotype subset;
4. one phenotype-defined design after the user separately approves the definition;
5. one local pinned copy with verified manifest and provenance;
6. defer because diagnosis, modality, phenotype, completeness, access,
   license, quality, or inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- diagnosis, acquisition, missingness, quality, and sample assumptions;
- access and license burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Dataset and Evidence Card;
- Phenotype and Completeness Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which COBRE file state, participant boundary, modalities, phenotype fields, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, request, term acceptance, credential, download, diagnosis or
participant selection, BIDS action, preprocessing, QC exclusion,
classification, power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact official or local file, manifest, hash, participant, modality, and
   phenotype state;
3. population, diagnostic, control, medication, and demographic boundary;
4. required structural, resting-state, phenotype, and acquisition evidence;
5. participant-level completeness, missingness, and quality requirements;
6. raw, converted, or derivative provenance;
7. repository warning and required integrity rechecks;
8. access, request, license, attribution, noncommercial, storage, sharing, and
   dissemination duties;
9. selected assumptions and explicit non-assumptions;
10. unresolved gaps and disqualifying conditions;
11. downstream handoff packets;
12. verification record;
13. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnostic, clinical,
classification, or scientific conclusion.

### 11. Verify and stop

Verify:

- current file, request, license, and repository claims are dated;
- participants, modality records, and files are not conflated;
- diagnosis codes are not guessed;
- released participants are not called analysis ready;
- one acquisition protocol is not called absence of site or batch effects;
- no fixed QC threshold or classification route is selected;
- protected phenotype fields remain protected;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, request, term acceptance, download, diagnosis or participant
  selection, write, preprocessing, classification, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether COBRE is considered;
- the scientific question, target population, estimand, diagnostic or
  dimensional contrast, outcome, and confirmatory status;
- participant, modality, phenotype, diagnosis, and file candidates;
- treatment of diagnostic criteria, medication, illness, motion, acquisition,
  missingness, QC, and exclusions;
- every access, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and limitations. It does not convert a protected
phenotype code into a group definition for the user.

Use this order:

1. current official COBRE and INDI pages;
2. exact current NITRC request, license, file list, manifest, hashes, phenotype
   dictionary, and acquisition metadata;
3. primary dataset and methods papers for historical context;
4. user-supplied local documentation;
5. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release-page fact**
- **Selected-file fact**
- **Protected-schema fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never infer protected phenotype coding from a source candidate or example.

Edge cases:

- **Only “COBRE” is supplied**: Ask for the scientific requirement. Do not
  choose a modality, phenotype, group, or participant subset.
- **All 147 participants are called analysis ready**: inspect modality,
  phenotype, quality, and missingness at participant grain.
- **Diagnosis is coded as 1 and 2**: inspect the current protected dictionary.
- **FD 0.3 is proposed as a COBRE rule**: return the QC decision to the user and
  require method evidence.
- **No site effects are claimed**: preserve acquisition, temporal, recruitment,
  and batch threats.
- **Brain-disorder classification is assumed**: route method design separately
  after the user supplies the estimand and evaluation boundary.
- **Commercial use is proposed**: stop under the current noncommercial license
  unless a different current license state is verified.
- **The NITRC repository changes during review**: repin the file list and
  hashes.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnostic validity, representativeness,
classification performance, clinical utility, causal identification, power,
analysis validity, or generalizability. It cannot guarantee that a NITRC file,
manifest, phenotype schema, request, license, or endpoint remains current after
it was last checked.

## COBRE facts that control the review

Use these as dated orientation and recheck them at invocation:

- The official release page reports 147 participants: 72 people with
  schizophrenia and 75 healthy controls, ages 18 to 65 in each group.
- The official page reports raw multi-echo MPRAGE anatomical MRI,
  resting-state fMRI, and phenotype fields for age, gender, handedness, and
  diagnosis for each released participant.
- Diagnostic information was collected with the Structured Clinical Interview
  for DSM Disorders. Exact field names, codes, criteria, and completeness must
  be verified in the current protected phenotype state.
- The official page lists one acquisition protocol and credits the Mind
  Research Network and University of New Mexico. That does not establish that
  temporal, scanner, protocol, recruitment, or hidden batch effects can be
  ignored.
- The release page provides no semantic release version or release date.
  Current file list and hashes therefore control the exact state.
- Access requires a NITRC account and a request for the 1000 Functional
  Connectomes Project. Current availability and terms must be rechecked.
- The official license is Creative Commons Attribution-NonCommercial.
- NITRC currently warns that its repository is under review for potential
  modification. File availability and integrity must be rechecked before use.
- A released count does not establish that all 147 records pass a future
  user-approved QC or completeness rule.

COBRE is not inherently a classification benchmark, and one-site release
language does not eliminate site-like or acquisition effects.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about COBRE
  diagnosis, acquisition, QC, representativeness, classification limitations,
  or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when diagnostic, comparison, or modality
  structure changes the design.
- Route power planning only after the user approves the exact participant units,
  groups, estimand, design, analysis, inference family, and loss assumptions.
- Route BIDS curation only after an exact governed source and separate
  specification are available.
- Route NITRC administration, download, storage, preprocessing, QC, phenotype
  construction, participant selection, classification, modeling, and
  interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *COBRE* [Data set]. (n.d.). https://fcon_1000.projects.nitrc.org/indi/retro/cobre.html
- [INDI access page]. (n.d.). https://fcon_1000.projects.nitrc.org/
- [NITRC access request page]. (n.d.). https://www.nitrc.org/project/request.php?group_id=296
