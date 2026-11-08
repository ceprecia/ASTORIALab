---
name: hcpd-skill
description: >-
  Evaluates whether one exact Human Connectome Project in Development release,
  participant subset, modality, task, behavioral measure, or processing tier can
  support a user-supplied research design and produces a selection-bound Dataset
  Suitability and Access Specification. Use when the request, or a part coordinator,
  hands over an explicitly matching HCP-D question. It verifies the current
  release and NDA access state; distinguishes the released cross-sectional visit
  from the broader developmental and longitudinal study aim; maps age, site,
  modality, task, completeness, processing, known-issue, and governance
  boundaries; and records only user-selected scope after two approval gates.
  Triggers: can HCP-D support my study, HCP Development data selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: developmental
  dependencies: ""
  requires: NDA access for HCP-D
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# HCP Development Dataset Suitability

Evaluate one exact HCP-D evidence state without importing HCP-Young Adult
assumptions or turning an external orchestration prompt into a data pipeline.

## Purpose

It does not create accounts, handle credentials, submit agreements, download data, choose participants, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`hcpd-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Human Connectome Project in
Development.

It owns:

- pinning the exact release, visit, participant subset, modality, task,
  behavioral or biomeasure package, processing tier, completeness state, and
  access route;
- distinguishing the released sample from the broader study enrollment target
  and intended longitudinal design;
- checking whether age, site, modality, task, measure, and completeness support
  the stated design;
- comparing only credible HCP-D release, modality, task, or processing routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, developmental model, age grouping,
participant selection, task contrast, QC rule, covariate choice, power target,
analysis, interpretation, or claim.

It never creates an account, handles credentials, submits a Data Use
Certification, accepts terms, downloads participant-level data, reorganizes
files, preprocesses imaging, excludes participants, fits a model, or uploads or
shares data.

Activate only when:

- The user invokes the exact trigger `hcpd-skill`; or
- a verified Active capability hands off one explicit HCP-D suitability or
  access-planning question.

Do not activate from `HCP`, `developmental connectome`, `pediatric MRI`,
`lifespan imaging`, `download HCP-D`, or `analyze HCP-D`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, age relation, contrast, outcome, unit, and timing |
| Population boundary | Age range, developmental window, exclusions, and generalization target |
| Data requirements | Structural, resting, task, diffusion, ASL, behavioral, biomeasure, or QC needs |
| Task requirements | Neural estimand, contrast, behavioral output, and task family if applicable |
| Release boundary | Candidate release or need to identify the current state |
| Access boundary | Approved public-document inspection and institutional or security constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the HCP-D Fit Brief

Return:

- exact scientific target and intended estimand;
- age, visit, modality, task, measure, and processing-tier requirements;
- candidate release, participant subset, package, completeness, and
  known-issue states;
- site, protocol, missingness, access, security, and storage constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection,
preprocessing, task modeling, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release, protocol, access, completeness, known-issue, or
  supplied local sources to inspect;
- whether any account, agreement, participant-level record, restricted lane,
  or protected path would be encountered;
- release, task, modality, processing, and access facts to verify;
- stop point before credentials, agreements, downloads, writes, or handoffs.

Ask:

> Approve this exact HCP-D source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, agreement submission, restricted-data
access, download, search expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- release, date, DOI, documentation version, and current-release check;
- visit, participant, age, site, modality, task, package, and processing tier;
- counts at the correct grain: participants, visits, runs, packages, or files;
- official completeness and known-issue record versions;
- current repository, access, agreement, renewal, group-sharing, and security
  conditions;
- conflicts, unknowns, and facts requiring account-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, date, and DOI | | | | |
| Participants, ages, and visit | | | | |
| Sites, scanners, and protocols | | | | |
| T1w and T2w structural MRI | | | | |
| Resting-state fMRI | | | | |
| CARIT, EMOTION, or GUESSING task fMRI | | | | |
| Diffusion MRI | | | | |
| ASL | | | | |
| Behavioral and biomeasures | | | | |
| Raw and processed packages | | | | |
| Completeness and known issues | | | | |
| Access and governance | | | | |

Do not infer participant-level completeness from a release-level package list.

### 5. Build the Visit, Task, and Package Map

| Requirement | Exact visit or package | Participant-level evidence | Processing provenance | Missingness or issue |
|---|---|---|---|---|
| Structural | | | | |
| Resting-state | | | | |
| CARIT | | | | |
| EMOTION | | | | |
| GUESSING | | | | |
| Diffusion | | | | |
| ASL | | | | |
| Behavioral or biomeasure | | | | |

Keep unprocessed and processed packages distinct. Never substitute an HCP-YA
task or contrast.

### 6. Build the Applicability Matrix

| Requirement | Exact HCP-D route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target age and population | | | | | |
| Cross-sectional or longitudinal design | | | | | |
| Modality | | | | | |
| Task and contrast | | | | | |
| Behavioral or biomeasure | | | | | |
| Site and protocol structure | | | | | |
| Processing tier | | | | | |
| Completeness tolerance | | | | | |
| Access and sharing | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- release sample versus broader study enrollment target;
- cross-sectional Release 2.0 versus requested longitudinal inference;
- age coverage, age distribution, developmental nonlinearity, and site
  confounding;
- participant-level modality, task, behavioral, and QC completeness;
- exact task family, conditions, contrasts, timing, and behavioral outputs;
- unprocessed versus processed package provenance;
- processing-version and template applicability across ages;
- site, scanner, protocol, burden, and motion differences;
- missing or incorrect variables and files in known issues;
- relatedness or unrelated-status requirements;
- NDA access, institutional approval, agreement, renewal, group sharing,
  storage, and dissemination duties;
- whether intended claims exceed a healthy, cross-sectional observational
  release.

Do not invent pediatric thresholds, templates, task durations, run counts, or
completeness rules.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact unprocessed modality package;
2. one exact processed package with pinned provenance;
3. one exact HCP-D task family and participant subset;
4. one behavioral or biomeasure package linked at the selected grain;
5. one completeness-filtered release subset whose scientific rule remains for
   the user to choose;
6. defer HCP-D because age, visit, longitudinal structure, modality, task,
   completeness, access, or processing requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- developmental, site, completeness, and processing assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Visit, Task, and Package Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which HCP-D release, visit, modalities, tasks, packages, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, agreement, credential, download, participant selection, BIDS action,
preprocessing, QC exclusion, task modeling, power calculation, analysis, save,
or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, date, DOI, visit, participant, age, site, and package state;
3. required modalities, HCP-D tasks, behavioral measures, and biomeasures;
4. unprocessed or processed tier and exact provenance;
5. completeness and known-issue requirements;
6. cross-sectional or longitudinal boundary;
7. site, scanner, protocol, motion, age, and missingness threats;
8. access, agreement, renewal, group-sharing, security, storage, and
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

The status is local to the selected design. It is not a developmental,
clinical, or scientific conclusion.

### 11. Verify and stop

Verify:

- current release and access claims are dated;
- release count and broader study aim are not conflated;
- Release 2.0 is not called longitudinal;
- HCP-D tasks are not replaced by HCP-YA tasks;
- participant-level completeness is verified;
- raw and processed packages remain distinct;
- repository and agreement routes are current;
- known issues remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, agreement, download, selection, write, preprocessing, or
  analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether HCP-D is considered;
- the scientific question, age target, estimand, contrast, outcome,
  developmental interpretation, and confirmatory status;
- release, participant, visit, modality, task, measure, and processing-tier
  candidates;
- treatment of site, age, acquisition, completeness, missingness, and known
  issues;
- every access, security, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and design consequences. It does not select an age
bin, task, modality, or released participant set for the user.

Use this order:

1. current official HCP Development release and study pages;
2. exact official access guide, release manifest, completeness file, protocol,
   processing, and known-issue documentation;
3. current NIMH Data Archive access and agreement documentation;
4. primary cohort and methods papers for historical design context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-package fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never substitute HCP-Young Adult protocols, tasks, counts, or access routes for
HCP-D evidence.

Edge cases:

- **Only “HCP-D” is supplied**: Ask for the scientific requirement. Do not
  choose a release, visit, modality, task, or processing tier.
- **A count near 600 is supplied**: distinguish the exact release count from a
  vague approximation and the broader study target.
- **Longitudinal data are assumed**: verify the exact released visits. Do not
  infer them from the study design.
- **MOTOR, GAMBLING, LANGUAGE, RELATIONAL, SOCIAL, or WM are listed**: flag the
  HCP-YA task substitution and return to the official HCP-D task protocol.
- **ConnectomeDB is proposed**: verify and correct the current HCP-D repository
  and access route.
- **Every participant is assumed complete**: inspect the official completeness
  record at the selected participant and package grain.
- **A processed package is proposed**: pin processing version, source data,
  space, outputs, and known issues.
- **A pediatric threshold or template is proposed as default**: return the
  scientific choice to the user and require evidence.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, longitudinal change,
developmental mechanism, task validity, causal identification, power, analysis
validity, generalizability, or fitness for clinical use. It cannot guarantee
that a release, repository, package, agreement, known issue, or endpoint
remains current after it was last checked.

## HCP-D facts that control the review

Use these as dated orientation and recheck them at invocation:

- HCP-D is a healthy developmental cohort spanning ages 5 to 21.
- The current official listed release is HCP-Development Lifespan 2.0,
  released 2021-02-26 with DOI `10.15154/1520708`.
- Release 2.0 contains 652 participants and cross-sectional Visit 1 only.
  The broader study aimed for more than 1,300 participants and included a
  planned three-wave longitudinal subset around puberty. Those aims do not
  establish longitudinal observations in Release 2.0.
- Acquisition occurred at four United States sites using 3T Siemens Prisma
  systems. Site and acquisition metadata still require exact verification.
- Unprocessed packages include T1-weighted and T2-weighted structural MRI,
  resting-state fMRI, task fMRI, diffusion MRI, and arterial spin labeling.
- Processed packages include structural, resting-state, and task-fMRI outputs,
  with separate behavioral and biomeasure data.
- Official HCP-D task families are `CARIT`, `EMOTION`, and `GUESSING`. The
  HCP-Young Adult seven-task family is not the HCP-D task set.
- Participant-level modality, behavioral, QC, and unrelated-status
  completeness must be checked in the exact official completeness record.
- Current distribution uses the NIMH Data Archive, not ConnectomeDB.
- Current controlled access requires an eligible institutional context, an
  active Federalwide Assurance, institutional approval, a signed Data Use
  Certification, and renewal. Exact requirements and sharing limits must be
  rechecked.
- The official known-issues record contains missing or incorrect variables and
  files. A release label is not proof of complete or error-free data.
- HCP-D protocols were harmonized with other HCP programs where feasible, not
  made identical. Developmental burden, hardware, and protocol constraints
  required differences.

Do not describe Release 2.0 as longitudinal because the broader study planned
longitudinal data.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about HCP-D
  developmental validity, task measurement, processing, motion, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when cross-sectional, age, task, or site
  structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  estimand, subset, design, analysis, inference family, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route access administration, download, storage, preprocessing, QC,
  participant selection, task modeling, and analysis to separately approved
  owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Human Connectome Project. (n.d.). *HCP Development study*. https://www.humanconnectome.org/study/hcp-lifespan-development
- Human Connectome Project. (n.d.). *HCP-D project protocols*. https://www.humanconnectome.org/study/hcp-lifespan-development/project-protocols
- Human Connectome Project. (n.d.). *Lifespan HCP data release updates: Known issues and planned fixes*. https://wiki.humanconnectome.org/docs/Lifespan%20HCP%20Data%20Release%20Updates%20Known%20Issues%20and%20Planned%20fixes.html
- Human Connectome Project. (2021). *HCP Development Lifespan 2.0 release* [Data set]. https://doi.org/10.15154/1520708
- Human Connectome Project. (2022, June). *Lifespan 2.0 release access instructions*. https://www.humanconnectome.org/storage/app/media/documentation/LS2.0/LS_Release_2.0_Access_Instructions_June2022.pdf
