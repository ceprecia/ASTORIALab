---
name: hcpep-skill
description: >-
  Evaluates whether one exact Human Connectome Project for Early Psychosis
  release, NDA collection, diagnostic group, modality, assessment, site,
  processing tier, or participant subset can support a user-supplied research
  design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching HCP-EP question. It verifies current release and NDA
  state; preserves the official 251-versus-252 count conflict; separates
  behavioral, imaging, processed structural, baseline, and longitudinal
  collections; maps diagnosis, assessment timing, site, scanner, coil, modality,
  completeness, medication, and governance; and records only user-selected scope
  after two approval gates. Triggers: can HCP Early Psychosis support my study,
  HCP-EP collection selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: clinical
  dependencies: ""
  requires: NDA access for HCP-EP
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# HCP Early Psychosis Dataset Suitability

Evaluate one exact HCP-EP evidence state without suppressing official source
conflicts or importing HCP-Young Adult tasks and pipeline assumptions.

## Purpose

It does not create accounts, handle credentials, submit agreements, download data, define diagnoses, choose participants, organize files, preprocess, set QC exclusions, analyze data, make clinical or scientific claims, search broadly, or save without separate approval.

`hcpep-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access question about the Human Connectome Project for Early
Psychosis.

It owns:

- pinning the exact release, NDA collection, diagnostic group, participant
  subset, modality, assessment, site, scanner, coil, processing tier,
  completeness, and access state;
- separating clinical and behavioral participants, imaging participants,
  minimally preprocessed structural participants, baseline data, and separate
  longitudinal collections;
- preserving official count and documentation conflicts;
- checking whether diagnostic, temporal, modality, assessment, acquisition,
  and governance evidence support the stated design;
- comparing only credible HCP-EP release, collection, modality, or subset
  routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnostic definition, group
construction, participant selection, medication treatment, QC rule, covariate
choice, power target, analysis, interpretation, or claim.

It never creates an account, handles credentials, submits a Data Use
Certification, accepts terms, downloads controlled data, reorganizes files,
preprocesses imaging, labels patients, excludes participants, fits a model, or
uploads or shares data.

Activate only when:

- The user invokes the exact trigger `hcpep-skill`; or
- a verified Active capability hands off one explicit HCP-EP suitability or
  access-planning question.

Do not activate from `early psychosis`, `psychosis imaging`, `HCP clinical`,
`schizophrenia dataset`, `download HCP-EP`, or `analyze HCP-EP`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For diagnostic, measurement, medication, or
prior-study evidence, offer a bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate
approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, diagnostic or dimensional contrast, outcome, unit, and timing |
| Population boundary | Clinical groups, illness stage, medication, age, control, and exclusions under consideration |
| Data requirements | Structural, resting-state, diffusion, field map, clinical, cognitive, assessment-date, or QC needs |
| Longitudinal needs | Baseline only or exact follow-up collection and interval |
| Release boundary | Candidate release and NDA collection or need to identify current state |
| Access boundary | Approved public-document inspection and institutional or security constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the HCP-EP Fit Brief

Return:

- exact scientific target and intended estimand;
- release, NDA collection, clinical group, modality, assessment, site,
  processing, and longitudinal requirements;
- candidate participant, imaging, processed, baseline, and follow-up states;
- medication, chronicity, timing, acquisition, missingness, access, security,
  and storage constraints;
- known official-source conflicts and unknowns;
- requested output and stop point.

If the request is really access administration, diagnosis construction,
participant selection, preprocessing, clinical classification, or analysis,
stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release, manual, change log, NDA collection, access,
  dictionary, or supplied local sources to inspect;
- whether any account, controlled-access record, agreement, restricted lane,
  or protected path would be encountered;
- count, diagnosis, modality, timing, acquisition, and access facts to verify;
- stop point before credentials, applications, downloads, writes, or handoffs.

Ask:

> Approve this exact HCP-EP source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, data-use application, agreement
submission, controlled-data access, download, search expansion, saving, or
another capability.

### 3. Pin the exact release and collection state

Record:

- release, date, NDA collection, manual, appendix, change-log, manifest, and
  dictionary versions;
- clinical and behavioral, imaging, processed structural, baseline, and
  follow-up counts at the correct grain;
- selected diagnostic, medication, clinical, cognitive, modality, site,
  scanner, coil, and assessment-date records;
- current data-use, institutional, security, storage, sharing, renewal, and
  dissemination conditions;
- official-source conflicts, corrections, unknowns, and account-level rechecks.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Conflict or recheck |
|---|---|---|---|---|
| Release and NDA collection | | | | |
| Clinical and behavioral participants | | | | |
| Imaging participants | | | | |
| Processed structural participants | | | | |
| Diagnostic groups and criteria | | | | |
| Medication and illness stage | | | | |
| Assessment timing and age | | | | |
| Recruitment sites | | | | |
| Scanner and coil | | | | |
| T1w and T2w structural MRI | | | | |
| Resting-state fMRI | | | | |
| Diffusion MRI and field maps | | | | |
| Baseline and longitudinal collections | | | | |
| Missingness and completeness | | | | |
| Access and governance | | | | |

Do not infer imaging completeness from a clinical release count.

### 5. Build the Count and Collection Reconciliation

| Source or collection | Total | Affective | Non-affective | Control | Imaging or behavior | Status |
|---|---:|---:|---:|---:|---|---|
| Release page and main manual | 251 | 57 | 126 | 68 | Clinical and behavioral | Working summary |
| Release-detail page | 252 | | | | Clinical and behavioral | Official conflict |
| Appendix 3 group counts | 252 | 57 | 127 | 68 | Clinical and behavioral | Official conflict |
| Appendix 3 site table | 251 | | | | Clinical and behavioral | Official conflict |
| Imaging cohort | 183 | 34 | 91 | 58 | Imaging | Separate grain |
| Processed structural cohort | 169 | | | | Structural derivative | Separate grain |
| Longitudinal Collection 3179 | | | | | Follow-up | Separate collection |

Inventory the current NDA Collection 2914 before defining a cohort.

### 6. Build the Applicability Matrix

| Requirement | Exact HCP-EP route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target clinical population | | | | | |
| Diagnostic or dimensional construct | | | | | |
| Medication and illness stage | | | | | |
| Structural, rest, diffusion, or field maps | | | | | |
| Clinical or cognitive assessment | | | | | |
| Assessment timing | | | | | |
| Baseline or longitudinal design | | | | | |
| Site, scanner, and coil structure | | | | | |
| Completeness tolerance | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- unresolved 251-versus-252 official count conflict;
- clinical and behavioral versus imaging versus processed-structural samples;
- exact affective and non-affective diagnostic composition;
- medication, illness duration, chronicity, recruitment, and treatment
  heterogeneity;
- imaging, demographic, and assessment dates and age differences;
- baseline Release 1.1 versus separate longitudinal Collection 3179;
- participant-level modality, assessment, and QC completeness;
- four recruitment sites versus three imaging scanners;
- scanner, coil, protocol, and site differences;
- absence of task fMRI in the released modality list;
- raw and processed package provenance;
- NDA application, institutional, agreement, security, storage, renewal,
  sharing, and dissemination duties;
- whether intended claims exceed an observational clinical cohort.

Do not invent early-psychosis motion thresholds, diagnostic labels, or
matching guarantees.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact Release 1.1 clinical and behavioral subset;
2. one exact structural, resting-state, diffusion, or field-map imaging subset;
3. one exact minimally preprocessed structural subset with provenance;
4. one baseline design under Collection 2914;
5. one separately verified longitudinal design under Collection 3179;
6. defer because diagnostic, medication, timing, modality, completeness,
   source-conflict, acquisition, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- diagnosis, medication, timing, site, completeness, and processing
  assumptions;
- access burden;
- unresolved conflicts and evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Count and Collection Reconciliation;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which HCP-EP release, collection, groups, modalities, assessments, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, application, agreement, credential, download, diagnosis or participant
selection, BIDS action, preprocessing, QC exclusion, power calculation,
analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, date, NDA collection, manifest, participant, and package
   state;
3. diagnostic, medication, illness-stage, control, and population boundary;
4. required modalities, clinical or cognitive assessments, and timing;
5. baseline or longitudinal collection boundary;
6. site, scanner, coil, protocol, completeness, and missingness threats;
7. official count conflicts and required inventory checks;
8. raw or processed provenance;
9. access, application, agreement, security, storage, sharing, renewal, and
   dissemination duties;
10. selected assumptions and explicit non-assumptions;
11. unresolved gaps and disqualifying conditions;
12. downstream handoff packets;
13. verification record;
14. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnostic, clinical,
or scientific conclusion.

### 11. Verify and stop

Verify:

- current release, collection, and access claims are dated;
- the 251-versus-252 contradiction remains explicit;
- clinical, imaging, and processed-structural counts remain distinct;
- diagnostic groups are not reduced to schizophrenia versus bipolar disorder;
- task fMRI is not invented;
- baseline and separate longitudinal collections remain distinct;
- assessment timing, site, scanner, and coil differences remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, application, agreement, download, diagnosis or participant
  selection, write, preprocessing, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether HCP-EP is considered;
- the scientific question, target population, estimand, diagnostic grouping,
  contrast, outcome, temporal interpretation, and confirmatory status;
- release, collection, participant, modality, assessment, clinical variable,
  and processing-tier candidates;
- treatment of diagnosis, medication, chronicity, site, scanner, coil,
  assessment timing, missingness, and completeness;
- every access, security, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and contradictions. It does not label a diagnosis,
collapse clinical heterogeneity, or choose a cohort for the user.

Use this order:

1. current official HCP-EP data-release page;
2. exact official release manual, change log, appendices, NDA collection,
   access documentation, manifests, and dictionaries;
3. current NDA agreement and institutional-access requirements;
4. primary cohort and methods papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-collection fact**
- **Official-source conflict**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never silently average, resolve, or omit conflicting official counts.

> [!info] References
> Read `./references/hcp_ep_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “HCP-EP” is supplied**: Ask for the scientific requirement. Do not
  choose a release, group, modality, or collection.
- **A total of 251 or 252 is asserted as settled**: show the official-source
  conflict and inventory current NDA Collection 2914.
- **Approximately 250 people are treated as imaging complete**: distinguish
  clinical, imaging, and processed-structural records.
- **Task fMRI is requested**: record that Release 1.1 lists structural,
  resting-state, diffusion, and field-map imaging, not task fMRI.
- **HCP-YA tasks are listed**: flag the source substitution.
- **ConnectomeDB is proposed**: verify and correct the current NDA route.
- **Early psychosis is treated as one diagnosis**: inspect exact diagnostic
  codes, criteria, certainty, medication, and chronicity.
- **Release 1.1 is called longitudinal**: preserve baseline-only status and
  inspect separate Collection 3179.
- **Age matching is assumed**: inspect actual assessment dates and variables.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnostic validity, treatment effects,
longitudinal change, psychosis mechanism, causal identification, power,
analysis validity, generalizability, or fitness for clinical use. It cannot
guarantee that a release, collection, agreement, count, diagnostic field,
package, or endpoint remains current after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about HCP-EP
  diagnosis, medication, task-free imaging, clinical measures, longitudinal
  design, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when clinical groups, assessment timing,
  baseline, or follow-up structure changes the design.
- Route power planning only after the user approves the exact participant units,
  groups, estimand, design, analysis, inference family, and loss assumptions.
- Route BIDS curation only after an exact governed source and separate
  specification are available.
- Route NDA administration, download, storage, preprocessing, QC, diagnosis
  construction, participant selection, modeling, and interpretation to
  separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Human Connectome Project. (n.d.-a). *Appendix 3: HCP-EP Release 1.1 change log*. https://www.humanconnectome.org/storage/app/media/documentation/HCP-EP1.1/Appendix_3_HCP-EP_Release_1.1_Change_Log.pdf
- Human Connectome Project. (n.d.-b). *HCP-EP data releases*. https://www.humanconnectome.org/study/human-connectome-project-for-early-psychosis/data-releases
- Human Connectome Project. (n.d.-c). *HCP-EP Release 1.1 manual*. https://www.humanconnectome.org/storage/app/media/documentation/HCP-EP1.1/HCP-EP_Release_1.1_Manual.pdf
- Human Connectome Project. (n.d.-d). [HCP-EP release detail]. https://www.humanconnectome.org/study/human-connectome-project-for-early-psychosis/document/hcp-ep
- NDA. (n.d.-a). *Collection 2914*. https://nda.nih.gov/edit_collection.html?id=2914
- NDA. (n.d.-b). [Data access information]. https://nda.nih.gov/nda/access-data-info
