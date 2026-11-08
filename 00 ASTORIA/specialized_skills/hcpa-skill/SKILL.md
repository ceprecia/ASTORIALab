---
name: hcpa-skill
description: >-
  Evaluates whether one exact Aging Adult Brain Connectome or legacy HCP-Aging
  release, visit, modality, task, measure, processing tier, or participant
  subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching HCP-A question.
  It verifies the current release and access route; keeps AABC Release 2
  separate from legacy HCP-Aging Lifespan 2.0; maps age, visit, site, modality,
  task, completeness, processing, longitudinal, and governance boundaries; and
  records only user-selected scope after two approval gates. Triggers: can
  HCP-Aging support my study, HCP Aging release selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: aging
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized restricted-data action requires verified access and terms for that release through the applicable BALSA or NDA route
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# HCP Aging and AABC Dataset Suitability

Evaluate one exact aging-connectome evidence state without mixing the current
AABC release with a legacy HCP-Aging release or importing HCP-Young Adult
assumptions.

## Purpose

It does not create accounts, handle credentials, accept terms, download data, choose participants, define cognitive status, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`hcpa-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access question about:

- the current combined Human Connectome Project in Aging and Aging Adult Brain
  Connectome release; or
- the separate legacy HCP-Aging Lifespan release.

It owns:

- pinning the exact release, visit, participant subset, modality, task,
  behavioral measure, processing tier, completeness state, and access route;
- distinguishing current AABC identifiers, terms, variables, packages, and
  repeated visits from legacy HCP-Aging Lifespan 2.0;
- checking whether age, visit, site, modality, task, measure, completeness, and
  longitudinal structure support the stated design;
- comparing only credible release, visit, modality, task, and product routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, aging model, cognitive-status
definition, participant selection, task contrast, QC rule, covariate choice,
power target, analysis, interpretation, or claim.

It never creates an account, handles credentials, accepts data-use terms,
downloads participant-level data, reorganizes files, preprocesses imaging,
excludes participants, fits a model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `hcpa-skill`; or
- a verified Active capability hands off one explicit HCP-A or AABC
  suitability or access-planning question.

Do not activate from `HCP`, `aging connectome`, `older adults`,
`cognitive aging`, `download HCP-A`, or `analyze HCP-A`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, age or change relation, contrast, outcome, unit, and timing |
| Population boundary | Age range, health or cognitive-state criteria, and generalization target |
| Data requirements | Structural, rest, task, diffusion, ASL, hippocampal T2, MRS, behavior, or QC needs |
| Longitudinal needs | Visits, intervals, within-person change, attrition, and completeness |
| Release boundary | Current AABC or legacy HCP-Aging candidate |
| Access boundary | Approved public-document inspection and institutional or storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the Aging Connectome Fit Brief

Return:

- exact scientific target and intended estimand;
- current AABC or legacy HCP-Aging scope;
- age, visit, modality, task, measure, processing, and longitudinal
  requirements;
- candidate release, participant subset, package, completeness, and access
  states;
- health, cognitive-state, site, protocol, attrition, storage, and governance
  constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection,
preprocessing, cognitive classification, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact current or legacy release, protocol, terms, completeness, package, or
  supplied local sources to inspect;
- whether any account, agreement, participant-level record, restricted lane,
  or protected path would be encountered;
- release, visit, task, modality, processing, and access facts to verify;
- stop point before credentials, term acceptance, downloads, writes, or
  handoffs.

Ask:

> Approve this exact HCP-A or AABC source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, term acceptance, restricted-data
access, download, search expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- AABC Release 2 or exact later state, or legacy HCP-Aging Lifespan 2.0;
- release date, documentation version, repository, and terms;
- participant, visit, session, imaging, modality, task, measure, and package
  counts at the correct grain;
- site, scanner, protocol, acquisition, and processing state;
- completeness, attrition, missingness, health, and cognitive-status evidence;
- access eligibility, agreement, storage, sharing, and dissemination duties;
- conflicts, unknowns, and facts requiring account-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, date, and repository | | | | |
| Participants, ages, and visits | | | | |
| Health and cognitive-state evidence | | | | |
| Sites, scanners, and protocols | | | | |
| Structural MRI | | | | |
| Resting-state fMRI | | | | |
| VISMOTOR, CARIT, or FACENAME task fMRI | | | | |
| Diffusion MRI and ASL | | | | |
| Hippocampal T2 and MRS | | | | |
| Behavioral and health measures | | | | |
| Raw and processed packages | | | | |
| Completeness, attrition, and known issues | | | | |
| Access and governance | | | | |

Do not infer visit-level completeness from a release-level modality list.

### 5. Build the Release and Visit Map

| Requirement | Current AABC Release 2 | Legacy HCP-Aging 2.0 | Exact evidence or mismatch |
|---|---|---|---|
| Population and age | | | |
| Visit 1 | | | |
| Repeated visits | | | |
| Structural and resting MRI | | | |
| VISMOTOR, CARIT, FACENAME | | | |
| Diffusion and ASL | | | |
| Hippocampal T2 | | | |
| 7T MRS | | | |
| Behavioral or health measures | | | |
| Repository and terms | | | |

Keep identifiers, variables, packages, and terms separate.

### 6. Build the Applicability Matrix

| Requirement | Exact release route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target age and population | | | | | |
| Cross-sectional or change estimand | | | | | |
| Required visits and intervals | | | | | |
| Modality or task | | | | | |
| Health or cognitive measure | | | | | |
| Site and protocol structure | | | | | |
| Processing tier | | | | | |
| Attrition and missingness tolerance | | | | | |
| Access and storage | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- current AABC versus legacy HCP-Aging identity;
- participant versus session count;
- enrollment health criteria versus later cognitive or health state;
- age range, survivor selection, cohort effects, interval, and attrition;
- visit-level modality, task, behavior, and QC completeness;
- site, scanner, protocol, acquisition, and processing changes;
- unprocessed-only hippocampal T2 and limited MRS visits;
- exact task family, conditions, contrasts, and behavioral outputs;
- raw and processed package provenance;
- BALSA or NDA account, eligibility, terms, transfer, storage, sharing, and
  dissemination duties;
- whether intended claims exceed an observational typically aging cohort.

Do not treat observed longitudinal decline as evidence that the release was
designed as a clinical impairment cohort.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact AABC Visit 1 modality or task;
2. one exact AABC repeated-visit subset;
3. one exact AABC high-resolution hippocampal T2 or MRS subset;
4. one version-pinned processed package;
5. one legacy HCP-Aging Lifespan 2.0 Visit 1 route;
6. defer because age, health, cognitive state, visit, task, modality,
   completeness, attrition, processing, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- aging, visit, site, attrition, completeness, and processing assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Release and Visit Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which HCP-A or AABC release, visits, modalities, tasks, packages, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, term acceptance, credential, download, participant selection, BIDS
action, preprocessing, cognitive classification, QC exclusion, power
calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact current or legacy release, date, repository, participant, visit, and
   session state;
3. age, health, cognitive-status, and population boundary;
4. required modalities, aging tasks, behavior, health measures, hippocampal T2,
   and MRS;
5. raw or processed package provenance;
6. site, scanner, protocol, visit, attrition, completeness, and missingness
   threats;
7. access, eligibility, terms, transfer, security, storage, sharing, and
   dissemination duties;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not an aging, clinical, or
scientific conclusion.

### 11. Verify and stop

Verify:

- current release and access claims are dated;
- AABC and legacy HCP-Aging remain distinct;
- participants, sessions, and imaging sessions are not conflated;
- Visit 1 and repeated-visit evidence remain distinct;
- aging tasks are not replaced by HCP-YA tasks;
- typically aging enrollment is not relabeled clinical impairment;
- participant-visit completeness is verified;
- raw and processed packages remain distinct;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, term acceptance, download, selection, write, preprocessing,
  classification, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether current AABC or legacy HCP-Aging is considered;
- the scientific question, age target, estimand, contrast, outcome, change
  model, and confirmatory status;
- release, participant, visit, modality, task, measure, and processing-tier
  candidates;
- treatment of aging, cognitive status, attrition, site, scanner, protocol,
  missingness, and completeness;
- every access, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and longitudinal constraints. It does not label a
participant cognitively impaired or select an aging trajectory for the user.

Use this order:

1. current official HCP Lifespan Aging release and AABC pages;
2. exact official release notes, completeness records, task protocols,
   packages, terms, and processing documentation;
3. current BALSA or NDA access documentation for the selected release;
4. primary cohort and methods papers for historical context;
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

Never combine current AABC and legacy HCP-Aging participants, visits,
identifiers, variables, terms, or packages without an explicit evidence-backed
design.

Edge cases:

- **Only “HCP-A” is supplied**: Ask whether current AABC or legacy HCP-Aging is
  intended and what scientific requirement is in scope.
- **Approximately 700 participants are assumed current**: distinguish legacy
  HCP-Aging Lifespan 2.0 from current AABC Release 2.
- **The obsolete ConnectomeDB URL is proposed**: verify and use the current
  BALSA route for AABC.
- **MOTOR, EMOTION, GAMBLING, LANGUAGE, RELATIONAL, SOCIAL, or WM are listed**:
  flag the HCP-YA substitution and return to `VISMOTOR`, `CARIT`, and
  `FACENAME`.
- **All participants are called cognitively normal**: inspect enrollment,
  visit, instrument, and selected definition. Do not assume a stable label.
- **All 1,396 participants are treated as longitudinal**: inspect the exact
  visit counts and participant-level completeness.
- **Hippocampal T2 is treated as processed**: preserve its unprocessed-only
  status unless a later release proves otherwise.
- **MRS is treated as universal**: verify the selected participant-visit set.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish normative aging, cognitive impairment,
longitudinal change, aging mechanism, causal identification, power, analysis
validity, generalizability, or fitness for clinical use. It cannot guarantee
that a release, repository, package, agreement, task, or endpoint remains
current after it was last checked.

## HCP-A and AABC facts that control the review

Use these as dated orientation and recheck them at invocation:

- The current release is Aging Adult Brain Connectome Release 2, released
  2026-01-28.
- AABC Release 2 reports 1,396 typically aging adults ages 36 to 90 or older
  and 2,878 sessions: 1,396 at Visit 1, 915 at Visit 2, 471 at Visit 3, and 96
  at Visit 4.
- Imaging exists for 1,390 participants across 2,789 sessions. Participant and
  session counts must remain distinct.
- Current modalities include structural MRI, resting-state fMRI, task fMRI,
  diffusion MRI, ASL, and high-resolution hippocampal T2. The hippocampal T2
  is unprocessed only in the current release.
- Seven-tesla magnetic resonance spectroscopy is available for 282 participant
  visits, not every participant or visit.
- Current AABC access is through the BALSA ConnectomeDB tab under AABC terms,
  not the obsolete `db.humanconnectome.org` route. Eligibility and terms must
  be rechecked.
- The separate legacy HCP-Aging Lifespan 2.0 release contains 725 healthy
  participants ages 36 to 100 or older, Visit 1 only, and was released through
  NDA in 2021.
- Official aging-task families are `VISMOTOR`, `CARIT`, and `FACENAME`. The
  HCP-Young Adult seven-task family is not the HCP-A or AABC task set.
- The cohort is described as typically aging and cognitively and physically
  healthy at enrollment. It is not a clinical cognitive-impairment cohort,
  although longitudinal decline can occur.
- AABC is multisite and longitudinal. Imaging and non-imaging events have
  different completeness, and site, protocol, visit, attrition, and processing
  metadata remain material.

Do not call every AABC participant cognitively normal at every later visit
without current participant-level evidence and an approved definition.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about aging,
  cognition, task validity, attrition, processing, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when visit, cohort, or longitudinal structure
  changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant and visit units, estimand, analysis, inference family, and loss
  assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route account administration, download, transfer, storage, preprocessing,
  QC, cognitive-status construction, participant selection, modeling, and
  interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- AABC. (n.d.). *AABC research design*. https://agingadultbrainconnectome.wustl.edu/research/
- HCP. (n.d.). *AABC data-use terms*. https://www.humanconnectome.org/study/hcp-lifespan-aging/data-use-terms
- HCP. (n.d.). *HCP Lifespan Aging data releases*. https://www.humanconnectome.org/study/hcp-lifespan-aging/data-releases
- HCP. (n.d.). *HCP Lifespan Aging overview*. https://www.humanconnectome.org/study/hcp-lifespan-aging/overview
- HCP. (n.d.). *HCP Lifespan Aging project protocols*. https://www.humanconnectome.org/study/hcp-lifespan-aging/project-protocols
- HCP. (2026, January 28). *AABC Release 2*. https://www.humanconnectome.org/study/hcp-lifespan-aging/document/aging-adult-brain-connectome-release-2
