---
name: ppmi-skill
description: >-
  Evaluates from public metadata whether one exact Parkinson's Precision
  Medicine Initiative source date, protocol era, enrollment cohort, current
  subgroup, visit, modality, measure, data cut, sequestered product, or
  governed-use boundary can support a user-supplied research design and produces
  a selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching PPMI question.
  It preserves rolling daily updates, enrollment-cohort versus
  biomarker-subgroup identity, protocol and visit changes, product completeness,
  current DUA 5.0 AI containment, publication, return-of-results, and sharing
  duties through two approval gates. It is public-metadata-only: it must not
  receive or inspect participant-level PPMI data in chat. Triggers: can PPMI
  support my study, PPMI cohort and visit selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: clinical
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized controlled-data action requires the verified access route and applicable data-use and containment controls
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# PPMI Dataset Suitability

Evaluate one exact Parkinson's Precision Medicine Initiative evidence state
without treating a continuously changing governed study as a fixed,
analysis-ready Parkinson disease dataset.

## Purpose

It does not apply for access, accept terms, request specimens or restricted products, download data, choose participants, create BIDS metadata, preprocess, set QC exclusions, analyze data, train models, make scientific or clinical claims, search broadly, or save without separate approval.

`ppmi-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about PPMI.

It owns:

- pinning the exact public dashboard date, protocol era, enrollment cohort,
  current subgroup, visit, modality, measure, public guidance document,
  curated data cut, standard, sequestered, genetic, sensor, imaging, or
  biospecimen product under review;
- checking whether population, temporal, phenotype, imaging, biomarker,
  protocol, completeness, governance, and provenance constraints support the
  stated design;
- keeping current enrolled counts, enrollment cohorts, biomarker-defined
  subgroups, legacy cohorts, rolling database states, curated cuts, and
  paper-specific subsets separate;
- comparing only public-metadata-supported routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the scientific question, Parkinson or prodromal definition,
biomarker threshold, subgroup rule, visit alignment, participant selection,
medication treatment, imaging or assay processing, missingness rule,
covariates, analysis, interpretation, or claim.

It never accesses the PPMI database, accepts the Data Use Agreement, applies
for data or specimens, authenticates, downloads, reads participant-level
records, selects participants, transforms files, preprocesses data, trains a
model, or uploads or shares results.

Activate only when:

- The user invokes the exact trigger `ppmi-skill`; or
- a verified Active capability hands off one explicit PPMI suitability or
  access-planning question.

Do not activate from `Parkinson`, `prodromal`, `DaTscan`, `PPMI`,
`download PPMI`, `process PPMI`, or `analyze PPMI` alone.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Population | Enrollment cohort or subgroup candidates, recruitment era, exclusions, and generalization target |
| Unit and structure | Participant, visit, assessment, scan, sample, device interval, assay, or public aggregate |
| Time rule | Baseline, follow-up, conversion, progression, remote or clinic visit, or matching requirement |
| Data requirements | Exact clinical, imaging, genetic, omics, sensor, biomarker, or specimen-derived variables |
| Source state | Public dashboard date, protocol, guidance document, or exact future data cut to request |
| Access boundary | Public metadata only and any institutional containment constraints |
| Intended handoff | Design, power, bounded literature search, or later contained-environment work |

If the question, population, unit, source state, temporal rule, or required
variables are missing, ask only for the missing item. Do not infer it from the
PPMI name.

## Steps

### 1. Build the PPMI Fit Brief

Show:

1. The user's exact question and intended decision;
2. population, unit, protocol era, cohort, subgroup, visit, modality, measure,
   product, and time requirements;
3. exact public sources and dates proposed for inspection;
4. known protocol, cohort, subgroup, rolling-update, completeness, temporal,
   assay, imaging, containment, and governance threats;
5. the public-metadata-only stop point;
6. the exact Gate 1 decision.

Do not access PPMI, inspect participant-level material, or search broadly.

### 2. Gate 1: approve the public inspection boundary

Ask the user to approve or revise:

- exact public dashboard, protocol, guidance, DUA, policy, or paper sources;
- exact retrieval date and historical or current source state;
- population, unit, cohort, subgroup, visit, modality, measure, product, and
  timing requirements;
- rolling-update and future data-cut treatment;
- containment, access, publication, return, model-sharing, and storage
  questions;
- inspection stop condition.

Gate 1 authorizes only the displayed public read-only inspection. It does not
authorize database access, an application, terms acceptance, authentication,
participant-level input, download, request, selection, transformation,
analysis, save, or handoff.

### 3. Pin exact public source and governance states

Record:

- current program name, protocol era, public document or dashboard URL,
  version, date, and retrieval time;
- aggregate counts with cohort and enrollment grain;
- current DUA version, Publication Policy, Data User Guide, and request route;
- standard, curated-cut, genetic, sequestered, sensor, imaging, omics,
  biomarker, biospecimen, or cell-line product identity;
- daily-update, uncurated, correction, and versioning conditions;
- AI containment, disclosure, team registration, annual update, publication,
  IP, acknowledgement, return-of-data, and model-sharing duties;
- unresolved conflicts.

Never write `current PPMI sample` without a dated source and grain.

### 4. Build the Public Evidence and Governance Card

| Dimension | Public source fact | Source and state | Design consequence | Unknown |
|---|---|---|---|---|
| Program and protocol era | | | | |
| Enrollment cohort and subgroup | | | | |
| Aggregate participant inventory | | | | |
| Visit and temporal structure | | | | |
| Clinical and cognitive measures | | | | |
| Imaging and sensor products | | | | |
| Biomarker, omics, and genetic products | | | | |
| Data cut and update state | | | | |
| Access and sequestered products | | | | |
| DUA, AI, publication, and sharing duties | | | | |

Counts must state whether they describe enrolled people, current cohort
assignments, visits, assessments, scans, files, specimens, or retained
observations.

### 5. Build the Cohort, Product, and Time Map

| Requirement | Enrollment cohort | Current subgroup | Exact product or visit | Fit or mismatch |
|---|---|---|---|---|
| Population and recruitment era | | | | |
| Parkinson, prodromal, or control definition | | | | |
| Conversion or progression target | | | | |
| Required clinical or cognitive measure | | | | |
| Required imaging or sensor product | | | | |
| Required biomarker, omics, or genetics | | | | |
| Data-cut and completeness rule | | | | |
| Access and containment state | | | | |

Do not use an enrollment label as a time-varying diagnosis or biomarker
subgroup.

### 6. Build the Applicability Matrix

| Design requirement | Publicly supported | Conditional on contained inspection | Not supported | Evidence |
|---|---:|---:|---:|---|
| Target population | | | | |
| Required unit and repeat structure | | | | |
| Cohort or subgroup construct | | | | |
| Required modality or measure | | | | |
| Temporal alignment | | | | |
| Product and data-cut completeness | | | | |
| Governance and containment | | | | |

`Conditional on contained inspection` is a future requirement, not permission
for this skill to inspect controlled data.

### 7. Build the Threat and Governance Register

At minimum assess:

- historical Progression Markers versus current Precision Medicine identity;
- protocol, eligibility, schedule, and assessment changes;
- enrollment cohort, current diagnosis, biomarker subgroup, and legacy SWEDD
  conflation;
- rolling daily updates, preliminary data, corrections, and unlocked values;
- aggregate dashboard count drift;
- participant, visit, scan, measure, assay, file, sample, and observation
  grains;
- repeated observations, within-person dependence, conversion, and treatment
  changes;
- modality, visit, assay, site, scanner, device, and product completeness;
- current subgroup and curated-data-cut definitions;
- standard versus genetic, sequestered, sensor, biospecimen, and cell-line
  access routes;
- diagnosis, symptom, DaTscan, assay, genetic risk, and disease-mechanism
  conflation;
- selection, attrition, missingness, remote-versus-clinic, and complete-case
  bias;
- DUA, AI containment, team registration, disclosure, safeguards, annual
  updates, publication review, IP, acknowledgement, return-of-data, and
  model-sharing duties.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact dated enrollment-cohort route;
2. one exact current subgroup or curated-data-cut route;
3. one exact clinical, imaging, sensor, biomarker, omics, or genetic product
   route;
4. one exact longitudinal or conversion route with future contained
   participant-level verification;
5. one exact sequestered or separately requested product route as an access
   contingency only;
6. defer because protocol, cohort, subgroup, visit, product, completeness,
   containment, or governance requirements are not met.

For each show public evidence, assumptions, tradeoffs, future contained checks,
unknowns, access conditions, and what would falsify suitability. Do not assign
numeric confidence or select a winner.

### 9. Gate 2: select the specification

Carry forward confirmed eligible choices. Ask the user to resolve only the
items below that remain open or have materially changed with new evidence.
Show a comparison only when it was needed to resolve a material choice.
Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10. Address these items in that specification.

- exact public source date, protocol era, cohort, subgroup, unit, visit,
  modality, measure, product, and future data cut;
- diagnostic, biomarker, progression, temporal, missingness, and completeness
  rules;
- assumptions, sensitivity checks, and future contained verification;
- DUA, AI, team, access, publication, IP, return, model-sharing, storage, and
  version duties;
- unresolved limitations;
- next handoff, if any.

Gate 2 authorizes only the selected public-metadata specification. It does not
authorize an application, terms acceptance, database access, participant-level
input, download, request, selection, BIDS action, preprocessing, model
training, analysis, saving, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. user-supplied target and estimand;
2. exact public source states and retrieval dates;
3. protocol, recruitment, cohort, subgroup, and generalization boundary;
4. participant, visit, measure, scan, assay, specimen, file, and product
   grains;
5. required modalities, measures, biomarkers, products, and timing;
6. protocol, label, rolling-update, temporal, completeness, selection,
   missingness, and generalization threats;
7. selected assumptions, sensitivities, and future contained checks;
8. access, DUA, AI containment, team, publication, IP, return, model-sharing,
   storage, and version duties;
9. unresolved unknowns and stop conditions;
10. The user's selections and rejected alternatives;
11. approved next handoff or `none`.

The output is a public-metadata specification, not an analysis plan or
permission to access or use PPMI data.

### 11. Verify and stop

Confirm:

- no participant-level PPMI material entered chat;
- every count has a date, source, and grain;
- enrollment cohort, current subgroup, and diagnosis remain distinct;
- protocols, visits, data cuts, and product routes remain explicit;
- rolling and preliminary data are not treated as frozen;
- standard, genetic, sequestered, biospecimen, and cell-line access remain
  distinct;
- current DUA 5.0 AI containment and sharing duties remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no application, access, terms acceptance, download, request, selection,
  write, model training, or analysis occurred.

Stop after the verified specification.

## Boundaries

PPMI Data Use Agreement version 5.0, April 2026, prohibits use of AI tools
that do not guarantee containment of PPMI data. It specifically treats
participant-specific input to a public-facing or third-party AI service as
unauthorized disclosure when the service can retain, share, train on,
regenerate, or otherwise expose that input.

Therefore this ASTORIA skill operates only on public PPMI documentation,
aggregate public dashboards, primary papers, and nonparticipant-specific
design requirements.

Never accept or inspect in chat:

- participant-level PPMI rows, images, files, identifiers, dates, measures,
  free text, or derived values;
- screenshots or pasted output from the controlled PPMI database;
- model inputs, outputs, weights, embeddings, summaries, or error logs that
  may encode participant-level PPMI information;
- access credentials, application details, or controlled manifests.

If the user supplies or offers such material, do not quote or transform it. State
the boundary, ask the user to keep the material in a DUA-compliant contained
environment, and continue only with public metadata or a fully abstract
design question.

This skill does not decide whether any other computational environment meets
the DUA. An opt-out setting alone is not sufficient under the current
agreement.

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and
  confirmatory status;
- the protocol era, cohort, subgroup, visit, modality, measure, biomarker,
  product, and data-cut candidates;
- definitions of Parkinson disease, prodromal state, control, conversion,
  progression, treatment state, assay positivity, and temporal alignment;
- every access, containment, sampling, preprocessing, analytic, publication,
  and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes public source facts and governance constraints. It does not
classify a participant, choose a biomarker subgroup, or infer disease stage.

Use this order:

1. current PPMI Data Use Agreement, Publication Policy, access guidance,
   public dashboard, current protocols, clarification letters, and data-user
   guidance;
2. exact curated-data-cut and group or subgroup documentation when publicly
   available;
3. primary PPMI design and cohort papers for dated historical context;
4. user-supplied abstract design constraints that contain no PPMI data;
5. external candidate material for prompts and negative evidence only.

Label every statement as one of:

- **Current public source fact**
- **Dated protocol or data-cut fact**
- **Historical-paper context**
- **Paper-specific subset**
- **User-supplied abstract constraint**
- **Inference**
- **Unknown**

Never let a paper-specific retained sample, an old Progression Markers
protocol, or a local download redefine the current Precision Medicine study.

> [!info] References
> Read `./references/ppmi_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only `PPMI` is supplied**: ask for the one scientific requirement and
  protocol or cohort candidate.
- **An old paper count is called current PPMI**: pin the paper-specific sample
  and current public dashboard separately.
- **The 7,755 dashboard count is reused later**: recheck the live dashboard
  and retain the 2026-07-23 value only as a dated snapshot.
- **Enrollment cohort is treated as current diagnosis**: separate enrollment,
  time-varying clinical status, and analytic subgroup.
- **All prodromal participants are assumed not to have PD at baseline**:
  preserve the public warning that some had a diagnosis at baseline.
- **Every participant is assumed to have MRI, DaTscan, DTI, sensors, omics,
  and CSF**: require future contained participant-by-visit completeness.
- **A standard account is assumed to expose SAA, BAM, or FASTQ**: restore the
  sequestered or separate-request route.
- **A local CSV or screenshot is offered for chat review**: refuse the
  participant-level input and keep the work public-metadata-only.
- **An AI service has an opt-out setting**: do not treat it as sufficient
  containment under DUA 5.0.
- **De-identified or derived rows are proposed for sharing**: preserve the
  disclosure, registration, repository, and model-sharing restrictions.
- **Current public metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish DUA compliance for an external environment,
diagnosis validity, biomarker validity, subgroup correctness, visit
equivalence, causal identification, missing-at-random assumptions,
preprocessing quality, power, analytic validity, clinical utility, or
generalizability. It cannot guarantee that a dashboard, protocol, data
element, access route, sequestered state, agreement, or policy remains current
after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about a PPMI
  construct, measure, assay, imaging product, subgroup, visit rule,
  generalization claim, or prior analysis.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when protocol era, cohort, repeat visits,
  conversion, missingness, or product structure changes the design.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the unit, dependence
  structure, estimand, analysis family, and loss assumptions.
- Route data applications, contained-environment inspection, downloads,
  requests, participant selection, preprocessing, modeling, analysis,
  publication review, and result return to separately approved owners.

Every handoff requires separate approval. This skill never chains
automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Marek et al. (2011). [Original PPMI design]. *Lancet Neurology, 10*(12), 1060–1067. https://doi.org/10.1016/S1474-4422(11)70280-9
- PPMI. (n.d.-a). [Data access page]. https://www.ppmi-info.org/access-data-specimens/download-data
- PPMI. (n.d.-b). [Guidance resources]. https://www.ppmi-info.org/access-data-specimens/guidance-resources
- PPMI. (n.d.-c). *PPMI data user guide*. https://www.ppmi-info.org/sites/default/files/docs/PPMI%20Data%20User%20Guide.pdf
- PPMI. (n.d.-d). [Public data dashboard]. https://www.ppmi-info.org/access-data-specimens/data
- PPMI. (n.d.-e). [Study cohorts]. https://www.ppmi-info.org/study-design/study-cohorts
- PPMI. (2026, April). *PPMI data use agreement* (Version 5.0). https://www.ppmi-info.org/sites/default/files/docs/ppmi-data-use-agreement.pdf
