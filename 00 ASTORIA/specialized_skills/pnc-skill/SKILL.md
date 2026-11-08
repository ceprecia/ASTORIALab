---
name: pnc-skill
description: >-
  Evaluates whether one exact Philadelphia Neurodevelopmental Cohort dbGaP
  release, imaging subset, modality, task, phenotype, genetic resource, or
  participant subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching PNC question. It
  verifies the current accession and controlled-access state; separates
  consented participants, imaging participants, scans, and files; maps
  population sampling, age, imaging tasks, modalities, clinical and cognitive
  measures, genetics, repeat observations, acquisition conflicts, missingness,
  and governance; and records only user-selected scope after two approval gates.
  Triggers: can PNC support my study, Philadelphia Neurodevelopmental Cohort
  selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: developmental
  dependencies: ""
  requires: dbGaP authorized access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Philadelphia Neurodevelopmental Cohort Dataset Suitability

Evaluate one exact PNC evidence state without accepting a false repository,
dataset accession, task list, or external orchestration pipeline.

## Purpose

It does not create accounts, handle credentials, submit data-access requests, download data, define diagnoses, choose participants, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`pnc-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Philadelphia Neurodevelopmental
Cohort, formally registered in dbGaP as Neurodevelopmental Genomics:
Trajectories of Complex Phenotypes.

It owns:

- pinning the exact dbGaP accession, version, consent group, imaging subset,
  modality, task, phenotype, genetics, release manifest, and access state;
- separating participants, imaging participants, visits, scans, images, and
  files;
- checking whether population, age, sampling, modalities, tasks, measures,
  repeat observations, acquisition, and governance support the stated design;
- preserving conflicts between official sources for later resolution;
- comparing only credible PNC release, modality, task, or subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, developmental model, diagnostic
definition, participant selection, task contrast, QC rule, covariate choice,
power target, analysis, interpretation, or claim.

It never creates an account, handles credentials, submits a dbGaP application,
accepts terms, downloads controlled data, reorganizes files, preprocesses
imaging, merges phenotypes, excludes participants, fits a model, or uploads or
shares data.

Activate only when:

- The user invokes the exact trigger `pnc-skill`; or
- a verified Active capability hands off one explicit PNC suitability or
  access-planning question.

Do not activate from `PNC`, `Philadelphia cohort`, `developmental genomics`,
`pediatric imaging`, `download PNC`, or `analyze PNC`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measure evidence, offer a bounded
[paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, age relation, exposure or contrast, outcome, unit, and timing |
| Population boundary | Age, recruitment frame, consent group, diagnosis, and exclusions under consideration |
| Data requirements | Structural, diffusion, ASL, resting, task, phenotype, cognitive, clinical, genetic, and QC needs |
| Task requirements | Fractal N-back, face-emotion identification, rest, or another exact verified protocol |
| Release boundary | Candidate accession/version or need to identify the current state |
| Access boundary | Approved public-document inspection and institutional or security constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the PNC Fit Brief

Return:

- exact scientific target and intended estimand;
- age, recruitment, consent, modality, task, phenotype, cognitive, clinical,
  genetic, and repeat-observation requirements;
- candidate accession, participant subset, release manifest, acquisition, and
  access states;
- known official-source conflicts;
- security, storage, and data-use constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection,
preprocessing, phenotype construction, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official accession, data-use, Penn, manifest, dictionary, acquisition,
  or supplied local sources to inspect;
- whether any account, controlled-access record, agreement, restricted lane,
  or protected path would be encountered;
- release, count, task, modality, acquisition, and access facts to verify;
- stop point before credentials, applications, downloads, writes, or handoffs.

Ask:

> Approve this exact PNC source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, data-access application, agreement
submission, controlled-data access, download, search expansion, saving, or
another capability.

### 3. Pin the exact release and access state

Record:

- accession, version, study-subject table, release manifest, and access date;
- consent group, participant, visit, imaging, scan, image, and file counts at
  the correct grain;
- selected modality, task, phenotype, cognitive, clinical, genetic, and QC
  records;
- scanner, coil, sequence, and acquisition metadata;
- repeat-visit evidence;
- current data-use limitations, access process, institutional approval,
  security, storage, and dissemination conditions;
- conflicts, unknowns, and facts requiring authorized-access verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Accession, version, and consent | | | | |
| Population and recruitment | | | | |
| Participants versus imaging records | | | | |
| Age and demographic coverage | | | | |
| Clinical and diagnostic evidence | | | | |
| Cognitive battery | | | | |
| Genetics | | | | |
| T1w structural MRI | | | | |
| Diffusion and ASL | | | | |
| Resting-state fMRI | | | | |
| Fractal N-back fMRI | | | | |
| Face-emotion-identification fMRI | | | | |
| Visits and repeat observations | | | | |
| Acquisition and quality | | | | |
| Access and governance | | | | |

Do not infer participant-level completeness from a study-level modality list.

### 5. Build the Task and Acquisition Map

| Requirement | Exact record or protocol | Imaging or behavioral | Participant-level availability | Conflict or gap |
|---|---|---|---|---|
| Resting-state | | | | |
| Fractal N-back | | | | |
| Face-emotion identification | | | | |
| Penn CNB measure | | | | |
| Scanner and coil | | | | |
| Sequence and run | | | | |
| Repeat visit | | | | |

Keep behavioral tasks, imaging tasks, and acquisition metadata distinct.

### 6. Build the Applicability Matrix

| Requirement | Exact PNC route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Recruitment frame | | | | | |
| Diagnostic construct | | | | | |
| Cognitive or clinical measure | | | | | |
| Imaging modality | | | | | |
| Imaging task | | | | | |
| Cross-sectional or repeated design | | | | | |
| Acquisition consistency | | | | | |
| Consent and data use | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- health-network recruitment and target-population limits;
- imaging-subsample selection from the broader consented cohort;
- participant, visit, scan, image, and file count confusion;
- age, sex, ethnicity, socioeconomic, and health-network structure;
- historical screening and diagnostic construct limits;
- cognitive test versus fMRI task confusion;
- modality and phenotype missingness at participant grain;
- cross-sectional versus actual repeat-visit availability;
- scanner, coil, sequence, and acquisition conflicts;
- genotype, phenotype, and imaging consent-group compatibility;
- raw, converted, and derivative provenance;
- dbGaP application, institutional approval, data-use limitation, security,
  storage, renewal, sharing, and dissemination duties;
- whether intended claims exceed an observational cohort.

Do not resolve the 12-channel versus 32-channel conflict without exact
participant-level acquisition metadata.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact structural, diffusion, ASL, or resting-state subset;
2. one exact fractal N-back or face-emotion-identification subset;
3. one exact cognitive, clinical, or genetic subset under compatible consent;
4. one verified linked imaging and phenotype subset;
5. one release-manifest-defined repeated-observation subset;
6. defer PNC because population, consent, modality, task, measure, acquisition,
   repeat-visit, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- sampling, diagnosis, acquisition, missingness, and linkage assumptions;
- access burden;
- unresolved evidence and official-source conflicts;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Task and Acquisition Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which PNC accession, consent group, participant subset, modalities, tasks, measures, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, application, agreement, credential, download, participant or variable
selection, BIDS action, preprocessing, QC exclusion, power calculation,
analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact accession, version, consent group, manifest, participant, visit, and
   modality state;
3. population, recruitment, age, clinical, cognitive, and genetic boundary;
4. exact imaging tasks and behavioral measures;
5. scanner, coil, sequence, and acquisition evidence or conflict;
6. repeat-observation and missingness requirements;
7. raw, converted, or derivative provenance;
8. access, application, agreement, security, storage, sharing, and
   dissemination duties;
9. selected assumptions and explicit non-assumptions;
10. unresolved gaps, conflicts, and disqualifying conditions;
11. downstream handoff packets;
12. verification record;
13. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a developmental,
diagnostic, clinical, or scientific conclusion.

### 11. Verify and stop

Verify:

- current accession and access claims are dated;
- consented participants, imaging participants, scans, images, and files are
  not conflated;
- PNC is not routed to NDA or OpenNeuro `ds000030`;
- behavioral and imaging tasks remain distinct;
- repeat imaging is not assumed from a longitudinal study label;
- official acquisition conflicts remain unresolved until exact metadata
  adjudicate them;
- diagnosis fields are not treated as definitive current clinical labels;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, application, agreement, download, selection, write,
  preprocessing, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether PNC is considered;
- the scientific question, target population, estimand, age relation, contrast,
  outcome, temporal interpretation, and confirmatory status;
- accession, consent group, participant, imaging, task, phenotype, genetic, and
  modality candidates;
- treatment of sampling, diagnosis, site, scanner, coil, missingness, related
  observations, and access limits;
- every access, security, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and conflicts. It does not choose a diagnostic
label, task, modality, or analytic cohort for the user.

Use this order:

1. current official dbGaP study page, accession history, data-use limitations,
   consent groups, and access documentation;
2. current official University of Pennsylvania PNC and Brain Behavior
   Laboratory pages;
3. exact release manifests, study-subject tables, data dictionaries,
   acquisition metadata, and phenotype documentation;
4. primary cohort and imaging methods papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-manifest fact**
- **Primary-paper context**
- **Official-source conflict**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never resolve an official-source conflict by choosing whichever value is more
convenient.

> [!info] References
> Read `./references/pnc_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “PNC” is supplied**: Ask for the scientific requirement. Do not choose
  an accession, consent group, modality, task, or participant subset.
- **More than 9,700 MRI images are called participants**: identify the record
  grain and find the exact imaging-subject count.
- **The 1,445 imaging subsample is treated as complete current data**: inspect
  the selected release manifest and modality completeness.
- **NDA is proposed**: correct the route to dbGaP Authorized Access.
- **OpenNeuro `ds000030` is proposed**: identify it as UCLA CNP, not PNC.
- **A CNB test is called an imaging task**: inspect the exact protocol and
  separate behavioral from fMRI measures.
- **Longitudinal MRI is assumed**: require release-level repeat-visit evidence.
- **A coil count is hardcoded**: preserve the official 12-versus-32-channel
  conflict until exact acquisition metadata resolve it.
- **A diagnosis is treated as definitive**: inspect instrument, algorithm,
  historical criteria, and certainty.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, diagnostic validity,
longitudinal change, developmental mechanism, genetic inference, causal
identification, power, analysis validity, generalizability, or fitness for
clinical use. It cannot guarantee that an accession, manifest, consent group,
agreement, acquisition description, or endpoint remains current after it
was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about PNC
  sampling, measure validity, task interpretation, acquisition, missingness, or
  prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when sampling, task, repeat-visit, or
  consent-group structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant units, design, analysis, inference family, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route dbGaP administration, download, storage, conversion, preprocessing, QC,
  phenotype construction, participant selection, modeling, and interpretation
  to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- dbGaP. (n.d.-a). *dbGaP access overview*. https://www.ncbi.nlm.nih.gov/books/NBK570242/
- dbGaP. (n.d.-b). *PNC data use certification*. https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?stacc=phs000607.v3.p2&view_pdf=
- *Philadelphia Neurodevelopmental Cohort* (phs000607.v3.p2) [Data set]. (n.d.). dbGaP. https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000607.v3.p2
- Penn. (n.d.). *Philadelphia Neurodevelopmental Cohort*. https://www.med.upenn.edu/bbl/philadelphianeurodevelopmentalcohort.html
