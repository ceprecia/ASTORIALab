---
name: aomic-skill
description: >-
  Evaluates whether one exact Amsterdam Open MRI Collection subdataset,
  OpenNeuro snapshot, modality, task, phenotype, raw product, derivative, or
  participant subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching AOMIC question.
  It keeps ID1000, PIOP1, and PIOP2 distinct; verifies version, BIDS and license
  metadata; maps population, task, modality, scanner-upgrade, physiology,
  missingness, and derivative provenance; and records only user-selected scope
  after two approval gates. It does not download data, choose participants,
  reorganize an official BIDS snapshot, preprocess, set QC exclusions, merge
  cohorts, analyze data, make scientific claims, search broadly, upload, share,
  or save without separate approval. Triggers: can AOMIC support my study,
  Amsterdam Open MRI Collection selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: general
  dependencies: ""
  requires: OpenNeuro access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Amsterdam Open MRI Collection Dataset Suitability

Evaluate one exact AOMIC subdataset without merging three different samples or
turning an open BIDS snapshot into an automatic pipeline.

## Purpose

`aomic-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Amsterdam Open MRI Collection.

It owns:

- pinning ID1000, PIOP1, or PIOP2 and the exact OpenNeuro snapshot, DOI,
  license, declared BIDS version, raw or derivative state, modality, task,
  phenotype, physiology, and participant subset;
- checking whether the proposed population, task, modality, measure, scanner,
  and completeness support the stated design;
- preserving acquisition and protocol differences across the three
  subdatasets;
- comparing only credible AOMIC subdataset, task, modality, or product routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, population target, task contrast,
participant selection, QC rule, covariate choice, power target, analysis,
interpretation, or claim.

It never downloads files, chooses participants, rewrites an official BIDS
snapshot, preprocesses imaging, imputes phenotypes, excludes participants,
fits a model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `aomic-skill`; or
- a verified Active capability hands off one explicit AOMIC suitability or
  access-planning question.

Do not activate from `AOMIC`, `Amsterdam MRI`, `OpenNeuro dataset`,
`movie fMRI`, `student sample`, `download AOMIC`, or `analyze AOMIC`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measure evidence, offer a bounded
[paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast, outcome, unit, and timing |
| Population boundary | Age, recruitment, education, and generalization target |
| Data requirements | T1w, DWI, fMRI, task, rest, physiology, phenotype, or QC needs |
| Task requirements | Exact cognitive or movie-watching construct and contrast |
| Snapshot boundary | Candidate subdataset and version or need to identify current state |
| Access boundary | Approved public-document inspection and local storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the AOMIC Fit Brief

Return:

- exact scientific target and intended estimand;
- population, subdataset, modality, task, phenotype, physiology, and product
  requirements;
- candidate snapshot, raw, derivative, scanner, and participant states;
- sampling, task, protocol, missingness, license, and storage constraints;
- known unknowns;
- requested output and stop point.

If the request is really download, participant selection, BIDS rewriting,
preprocessing, phenotype imputation, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official OpenNeuro snapshot, AOMIC page, mirror commit, metadata, or
  supplied local sources to inspect;
- whether any participant-level files, large downloads, protected paths, or
  external stimulus assets would be encountered;
- version, task, modality, participant, license, and provenance facts to
  verify;
- stop point before download, write, search expansion, or handoff.

Ask:

> Approve this exact AOMIC source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only metadata inspection. It does not
authorize participant-level download, large-file access, file writes, search
expansion, saving, or another capability.

### 3. Pin the exact snapshot

Record:

- ID1000, PIOP1, or PIOP2;
- OpenNeuro accession, snapshot tag, snapshot date, DOI, and mirror commit;
- declared BIDS version and license;
- participant, session, modality, task, run, event, physiology, and phenotype
  state at the correct grain;
- raw and derivative products with software and processing provenance;
- scanner, coil, protocol, and display state;
- current validation, change history, conflicts, and unknowns.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Snapshot and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Subdataset and snapshot | | | | |
| Population and recruitment | | | | |
| Participants and session | | | | |
| Scanner, coil, and protocol | | | | |
| T1w structural MRI | | | | |
| Diffusion MRI | | | | |
| fMRI task or rest | | | | |
| Events and behavioral outputs | | | | |
| Physiology | | | | |
| Phenotype and psychometrics | | | | |
| Raw and derivative products | | | | |
| BIDS declaration and validation | | | | |
| License and stimulus rights | | | | |
| Missingness and quality | | | | |

Do not infer participant-level availability from a subdataset-level list.

### 5. Build the Subdataset and Task Map

| Requirement | ID1000 | PIOP1 | PIOP2 | Exact evidence or mismatch |
|---|---|---|---|---|
| Target population | | | | |
| Movie watching | | | | |
| Resting-state | | | | |
| Faces or emotion matching | | | | |
| Gender Stroop | | | | |
| Working memory | | | | |
| Anticipation | | | | |
| Stop signal | | | | |
| DWI | | | | |
| Phenotype or physiology | | | | |

An empty cell is not a no until the exact snapshot has been checked.

### 6. Build the Applicability Matrix

| Requirement | Exact AOMIC route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Task and contrast | | | | | |
| Modality | | | | | |
| Behavioral output | | | | | |
| Phenotype or physiology | | | | | |
| Scanner and protocol | | | | | |
| Raw or derivative product | | | | | |
| Missingness tolerance | | | | | |
| License and stimulus use | | | | | |
| Planned inference | | | | | |

### 7. Build the Threat and Provenance Register

Check at minimum:

- three-subdataset identity and prohibited silent pooling;
- narrow ID1000 age range and PIOP student sampling;
- single-session design and absence of longitudinal evidence;
- task availability and exact event or contrast definitions;
- behavioral, physiology, phenotype, and modality completeness;
- scanner model, upgrade, coil, display, angulation, multiband, and protocol
  differences;
- participant overlap or identifier assumptions across subdatasets;
- raw, derivative, and NeuroVault product separation;
- derivative software version, inputs, space, censoring, and QC provenance;
- declared historical BIDS version versus current validation;
- CC0 dataset state versus separate stimulus or external-asset rights;
- whether planned claims exceed these samples and tasks.

Do not call the same physical scanner a constant acquisition environment.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one pinned ID1000 movie-watching subset;
2. one pinned PIOP1 task or resting-state subset;
3. one pinned PIOP2 task or resting-state subset;
4. one exact T1w or DWI subset;
5. one version-pinned derivative with explicit processing provenance;
6. an explicitly justified cross-subdataset design that keeps population,
   task, scanner, and protocol differences visible;
7. defer AOMIC because population, task, modality, session, provenance, or
   inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- sampling, task, scanner, missingness, and derivative assumptions;
- storage or stimulus-rights burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Snapshot and Evidence Card;
- Subdataset and Task Map;
- Applicability Matrix;
- Threat and Provenance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which AOMIC subdataset, snapshot, modalities, tasks, products, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize a
download, participant selection, BIDS rewrite, preprocessing, QC exclusion,
phenotype merge, power calculation, analysis, upload, share, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact subdataset, accession, snapshot, date, DOI, commit, license, and BIDS
   declaration;
3. population, recruitment, participant, and session boundary;
4. required modalities, tasks, events, behavior, physiology, and phenotypes;
5. scanner, coil, display, protocol, and upgrade evidence;
6. raw or derivative provenance;
7. missingness, quality, validation, and stimulus-rights requirements;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a scientific conclusion.

### 11. Verify and stop

Verify:

- exact current snapshot, version, DOI, and license claims are dated;
- ID1000, PIOP1, and PIOP2 remain distinct;
- participant counts and task identities match the pinned snapshot;
- ID1000 is not mislabeled resting-state or assigned PIOP tasks;
- DWI is not omitted;
- single-session data are not called longitudinal;
- scanner upgrades and protocol differences remain visible;
- raw, derivative, and group-level products remain distinct;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no download, participant selection, BIDS rewrite, preprocessing, or analysis
  occurred.

Then stop.

## Boundaries

The user owns:

- whether AOMIC is considered;
- the scientific question, target population, estimand, contrast, outcome,
  task interpretation, and confirmatory status;
- subdataset, snapshot, participant, modality, task, phenotype, physiology,
  raw, and derivative candidates;
- treatment of narrow age range, student sampling, scanner upgrades, protocol
  differences, missingness, and quality;
- every download, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and tradeoffs. It does not select an AOMIC
subdataset or merge samples for the user.

Use this order:

1. exact official OpenNeuro snapshot and dataset-authored AOMIC page;
2. snapshot `dataset_description.json`, README, change history, participants,
   events, sidecars, derivative descriptions, license, and BIDS validation
   state;
3. official OpenNeuro mirror commit for an immutable source state;
4. primary AOMIC methods and data papers;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified snapshot fact**
- **Verified current source fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never call an unversioned AOMIC landing page an exact data state.

Edge cases:

- **Only “AOMIC” is supplied**: Ask for the scientific requirement. Do not
  choose ID1000, PIOP1, or PIOP2.
- **A merged AOMIC cohort is proposed**: preserve population, task, scanner,
  protocol, phenotype, and identifier differences before any design judgment.
- **ID1000 resting-state is requested**: flag the mismatch; its released fMRI
  identity is movie watching.
- **Raven matrices are assigned to ID1000**: verify the exact phenotype.
  Raven variables belong to PIOP states, while ID1000 uses other intelligence
  variables.
- **DWI is said to be absent**: correct the candidate after checking the exact
  snapshot.
- **An official snapshot is sent to BIDS organization**: stop unless the user has a
  separate curation reason and approved specification.
- **A derivative is treated as raw**: pin software, inputs, version, space,
  strategies, and QC provenance.
- **CC0 is treated as automatic stimulus permission**: inspect underlying
  stimulus and external-asset rights.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, task validity, longitudinal
change, causal identification, power, analysis validity, generalizability, or
fitness for clinical use. It cannot guarantee that a snapshot, DOI, license,
validation state, derivative, or endpoint remains current after it was
last checked.

## AOMIC facts that control the review

Use these as dated orientation and recheck them at invocation:

| Subdataset | Official snapshot | Participants | Sampling and fMRI identity |
|---|---|---:|---|
| ID1000 | OpenNeuro `ds003097` v1.2.1 | 928 | Adults ages 19 to 26; movie-watching fMRI |
| PIOP1 | OpenNeuro `ds002785` v2.0.0 | 216 | University students; faces, gender Stroop, emotion matching, working memory, anticipation, and rest |
| PIOP2 | OpenNeuro `ds002790` v2.0.0 | 226 | University students; working memory, rest, stop signal, and emotion matching |

Additional controlling facts:

- AOMIC is three distinct single-session datasets, not one cohort and not a
  longitudinal resource.
- All three include T1-weighted MRI, diffusion MRI, fMRI, demographics,
  psychometrics, and varying physiological recordings.
- ID1000 uses movie-watching fMRI. It is not a resting-state, emotion,
  gambling, motor, or language dataset.
- ID1000 recruitment sought educational-level approximation to the Dutch
  population within ages 19 to 26. That does not establish population
  representativeness across age or other demographic dimensions.
- PIOP1 and PIOP2 are student samples.
- The three datasets used the same physical Philips 3T scanner across
  Intera, Achieva, and Achieva dStream states. Head coil, display, slice
  angulation, multiband use, and scan parameters changed.
- The pinned snapshots declare CC0, but exact downstream files and external
  stimulus rights must still be checked.
- The pinned snapshots declare different historical BIDS versions. A declared
  version is not proof of compliance with the current BIDS specification.
- Raw and included derivatives are separate products. Included QC records do
  not choose an exclusion rule.

Do not treat task or phenotype coverage as uniform across ID1000, PIOP1, and
PIOP2.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about AOMIC
  task validity, population limits, scanner upgrades, derivatives, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when task, sample, or cross-subdataset structure
  changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact subset,
  estimand, design, analysis, inference family, and loss assumptions.
- Use [bids](../bids/SKILL.md) only for a separately approved curation or current-spec review.
  Do not reorganize the official snapshot merely because its declared BIDS
  version is historical.
- Route download, storage, preprocessing, QC, phenotype construction,
  participant selection, modeling, and interpretation to separately approved
  owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- AOMIC. (n.d.). [Dataset project page]. https://nilab-uva.github.io/AOMIC.github.io/
- *AOMIC ID1000* (Version 1.2.1) [Data set]. (2021). OpenNeuro. https://openneuro.org/datasets/ds003097/versions/1.2.1
- *AOMIC PIOP1* (Version 2.0.0) [Data set]. (2020). OpenNeuro. https://openneuro.org/datasets/ds002785/versions/2.0.0
- *AOMIC PIOP2* (Version 2.0.0) [Data set]. (2020). OpenNeuro. https://openneuro.org/datasets/ds002790/versions/2.0.0
- [AOMIC primary data article]. (n.d.). *Scientific Data*. https://www.nature.com/articles/s41597-021-00870-6
