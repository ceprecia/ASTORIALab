---
name: aibl-skill
description: >-
  Evaluates whether one exact full Australian Imaging, Biomarker and Lifestyle
  Integrated Data Set product or separate LONI and ADNI collaboration subset,
  cohort state, collection cycle, site, diagnostic group, modality, measure
  stream, acquisition product, or participant subset can support one
  user-supplied research design and produces a selection-bound Dataset
  Suitability and Access Specification. Use when the request, or a part coordinator,
  hands over an explicitly matching AIBL question. It keeps the controlled full
  IDS separate from the incomplete and separately authorized LONI and ADNI
  subset, dates participant counts, preserves ongoing replenishment and 18-month
  collection cycles, and maps multimodal, acquisition, completeness,
  heterogeneity, and governance limits after two approval gates. Triggers: can
  AIBL support my study, AIBL cohort selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: aging
  dependencies: ""
  requires: approved access for the selected AIBL product and release
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-10-29"
---

# AIBL Dataset Suitability

Evaluate one exact AIBL evidence state without treating an ongoing,
replenished multimodal cohort or its collaboration subset as one fixed,
uniformly complete dataset.

## Purpose

It does not submit an expression of interest, authenticate, accept terms, inspect controlled participant data, download data, invent identifiers or mappings, select participants or diagnoses, organize files, preprocess, set cutoffs or QC exclusions, harmonize with ADNI, analyze data, make scientific or clinical claims, search broadly, or save without separate approval.

`aibl-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access question about the full AIBL Integrated Data Set or the
separate LONI and ADNI collaboration subset.

It pins the product, dated cohort state, participant grain, collection cycle,
site, diagnostic group, modality, measure, acquisition state, completeness,
and access route; compares only credible routes; and produces one user-selected
Dataset Suitability and Access Specification.

It does not own scientific or analytic decisions. It never submits access
materials, handles credentials, accepts terms, inspects controlled participant
records, downloads data, invents identifiers or mappings, selects a cohort,
converts DICOM, preprocesses, harmonizes, fits models, or shares data.

Activate only when:

- The user invokes the exact trigger `aibl-skill`; or
- a verified Active capability hands off one explicit AIBL suitability or
  access-planning question.

Do not activate from `Alzheimer's`, `dementia`, `aging MRI`, `AIBL`,
`download AIBL`, `process AIBL`, or `analyze AIBL`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the cohort, diagnostic, temporal, control, or
measurement structure must be designed. Offer [paper-search](../../skills/paper-search/SKILL.md) only for a
separately approved bounded search about measurement validity, cohort
comparability, or prior evidence.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target and estimand | user-supplied question or design; population, contrast, outcome, unit, and timing |
| Product boundary | Full AIBL IDS, AIBL and ADNI subset, or an unresolved product choice |
| Population and cycle | Age, diagnosis, site, inception or replenishment state, and required 18-month contacts |
| Data requirements | MRI, PET, biofluid, genetics, cognition, lifestyle, or exact linked stream |
| Acquisition boundary | Raw or derived state, field strength, protocol, tracer, and required comparability |
| Access boundary | Public documentation only or a separately verified approved environment |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should AIBL be evaluated against?

Then stop.

## Steps

### 1. Build the AIBL Fit Brief

Return the exact target and estimand; intended product, population, diagnosis,
cycle, site, modality, stream, and acquisition requirements; participant and
observation grains; comparability, completeness, access, and governance
constraints; known conflicts and unknowns; and the requested stop point.

If the request is really an expression of interest, login, participant
inspection, download, DICOM conversion, diagnosis mapping, harmonization,
participant selection, preprocessing, cutoff choice, or analysis, stop and
route it outside this skill.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact public pages, dated notices, paper sections, or supplied metadata to
  inspect;
- any account, credential, controlled-record, protected-path, or terms
  boundary;
- product, cohort, cycle, site, stream, acquisition, completeness, and access
  facts to verify;
- the stop point before credentials, applications, downloads, writes, search
  expansion, or handoffs.

Ask:

> Approve this exact AIBL public-source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize an expression of interest, account use, terms acceptance,
controlled-data access, participant-level inspection, download, search
expansion, saving, or another capability.

### 3. Pin the exact product and access state

Record the full IDS or collaboration-subset identity; source and query date;
dated cohort, participant, visit, image, assay, and observation grains;
diagnostic and age definitions; inception and replenishment state; collection
cycles and sites; available streams; raw or derived state; scanner, field
strength, protocol, and tracer; completeness and missingness; access
authorization; corrections, conflicts, unknowns, and rechecks.

If the exact product cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Product and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Product, source, and query date | | | | |
| Dated cohort and participant counts | | | | |
| Inception, replenishment, and attrition | | | | |
| Age and diagnostic groups | | | | |
| Cycles, contacts, and sites | | | | |
| MRI and PET products | | | | |
| Biofluid, genetics, cognition, and lifestyle | | | | |
| Raw, derived, protocol, and tracer state | | | | |
| Completeness and linkage | | | | |
| Authorization and governance | | | | |

Do not infer participant-level completeness from a cohort-level stream list.

### 5. Build the Cycle and Stream Map

| Requirement | Exact product and cycle | Exact stream or acquisition | Evidence or mismatch |
|---|---|---|---|
| Population and diagnosis | | | |
| Cross-sectional or longitudinal timing | | | |
| MRI modality and field strength | | | |
| PET tracer and acquisition | | | |
| Biofluid or genetic measure | | | |
| Cognitive or lifestyle measure | | | |
| Raw or derived product | | | |
| Linkage and completeness | | | |
| Access route | | | |

Keep IDS and collaboration products, study contacts and imaging timepoints,
diagnostic labels, sites, protocols, tracers, and processing states separate.

### 6. Build the Applicability Matrix

| Requirement | Selected product, cycle, or stream | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population and estimand | | | | | |
| Diagnosis and age boundary | | | | | |
| Required cycles and timing | | | | | |
| Required modality and measure | | | | | |
| Acquisition comparability | | | | | |
| Participant and stream completeness | | | | | |
| Authorization and intended use | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- full IDS versus LONI and ADNI collaboration subset;
- February 2023 counts versus current ongoing replenished inventory;
- original 1,112-person cohort versus later enriched cohorts;
- participant, contact, visit, image, assay, file, and observation grains;
- 18-month schedule versus actual stream-specific timing;
- AD, MCI, healthy, and cognitively normal label definitions;
- Perth and Melbourne site identity;
- participant-level MRI, PET, biofluid, genetics, cognition, and lifestyle
  availability;
- raw DICOM, derived products, 1.5 T and 3 T, scanner, protocol, and tracer
  heterogeneity;
- attrition, replenishment, selection, missingness, and generalizability;
- EOI, management review, authorization, terms, storage, sharing, and
  publication duties;
- partial ADNI table mapping and incomplete subset coverage;
- whether the intended claim exceeds an observational cohort.

Do not invent identifiers, diagnosis or visit mappings, cutoffs, reference
regions, or harmonization.

### 8. Assess the selected or eligible routes

Assess the selected AIBL product or cohort route against the approved question.
If it cannot meet the requirements, report the blocker. Compare eligible
routes only if a material choice remains open and the evidence supports
more than one. These are examples of routes and possible dispositions.

1. full IDS metadata-level planning followed by a separately approved EOI;
2. one exact authorized LONI and ADNI collaboration-subset route;
3. one exact 18-month longitudinal route with verified stream completeness;
4. one exact MRI, PET, biofluid, genetics, cognition, or lifestyle route;
5. one exact cross-stream route with verified linkage and timing;
6. defer because population, product, cycle, modality, acquisition,
   completeness, comparability, or access requirements are not met.

For each show exact scope, support, non-support, cohort and acquisition
assumptions, access burden, unresolved evidence, and downstream handoffs. Do
not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show the Product and Evidence Card, Cycle and Stream Map, Applicability Matrix,
Threat and Governance Register, assessed route, disqualifying conditions,
and unresolved conflicts. Include the comparison if a material choice required
one. Carry forward the user's confirmed choices.

Ask about the AIBL product, cohort state, cycles, sites, groups, streams,
acquisition states, assumptions, and handoffs only when a decision remains
open or new evidence materially changes it.

Ask for explicit approval of the assembled Dataset Suitability and Access
Specification and its scope, including the stopping point.

Gate 2 authorizes only the selected specification. It does not authorize an
EOI, account, credential, terms acceptance, controlled-data inspection,
download, identifier or diagnosis mapping, participant selection, DICOM
conversion, harmonization, preprocessing, cutoff choice, analysis, save, or
handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied target and estimand;
2. exact full IDS or collaboration-subset state and query date;
3. dated cohort, participant, contact, cycle, site, and diagnostic grains;
4. required MRI, PET, biofluid, genetics, cognition, and lifestyle streams;
5. raw or derived state, scanner, field strength, protocol, tracer, linkage,
   completeness, attrition, replenishment, and missingness threats;
6. exact access route, authorization, terms, and governance boundary;
7. selected assumptions and explicit non-assumptions;
8. unresolved gaps and disqualifying conditions;
9. downstream handoff packets and verification record;
10. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a diagnosis, biomarker,
causal, clinical, licensing, or scientific conclusion.

### 11. Verify and stop

Verify:

- full IDS and collaboration subset remain distinct;
- all counts are dated and the original 1,112 is historical;
- ongoing replenishment, attrition, and 18-month cycles remain visible;
- participant, contact, visit, image, assay, and file grains are not conflated;
- site, field strength, protocol, tracer, and processing differences remain
  visible;
- multimodal availability is not treated as participant-level completeness;
- partial ADNI mapping is not called full harmonization;
- no identifier, diagnosis mapping, SUVR cutoff, reference region, or QC rule
  was invented;
- only user-selected elements entered the specification;
- no access, credential, controlled inspection, download, selection,
  conversion, preprocessing, harmonization, analysis, or claim occurred.

Then stop.

## Boundaries

The user owns the scientific question, hypothesis, estimand, contrast, outcome,
unit, timing, confirmatory status, product and participant candidates,
treatment of diagnosis, attrition, replenishment, missingness, scanner,
protocol, tracer, and site effects, every access or analytic decision, the
final suitability judgment, and downstream action.

This skill exposes evidence and constraints. It does not define a diagnostic
group, choose a biomarker threshold, harmonize AIBL with ADNI, or construct a
longitudinal sample for the user.

Use public documentation and user-approved nonparticipant metadata only. Do
not enter an AIBL, CSIRO, ADNI, or LONI account; inspect controlled
participant-level data; submit an expression of interest; accept terms; or
transmit protected material.

If suitability cannot be established without controlled inspection, mark the
needed evidence **Unknown** and stop at a metadata-level specification.

Use this order:

1. current official AIBL homepage, collaboration, data-system, and access
   documentation;
2. current full IDS inventory and dictionary only in a separately approved
   environment;
3. official AIBL and ADNI subset documentation and dated LONI release notices;
4. primary AIBL cohort and methods papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement as **Verified current source fact**, **Dated
cohort fact**, **Selected-product fact**, **Historical-paper context**,
**User-supplied constraint**, **Inference**, or **Unknown**.

Never use a historical cohort total, dated homepage count, paper-specific
sample, or collaboration subset as the current full IDS denominator.

Edge cases:

- **Only AIBL is supplied**: ask for the one scientific requirement.
- **3,045 is called the current sample**: date it to February 2023 and recheck.
- **1,112 is called the full cohort**: label it the historical Inception
  cohort.
- **The LONI product is called full AIBL**: correct it to the separately
  authorized, incomplete LONI and ADNI subset.
- **Every stream is assumed at every visit**: require participant, cycle, and
  stream-specific completeness.
- **An 18-month contact is treated as an imaging visit**: verify the exact
  modality timing.
- **MRI is treated as uniform**: expose DICOM state, 1.5 T and 3 T,
  scanner, series, and protocol differences.
- **PET is treated as one tracer**: pin tracer and acquisition period.
- **ADNI-style fields are called harmonized**: preserve incomplete mapping and
  semantic differences.
- **A participant ID, diagnosis mapping, SUVR cutoff, or QC rule is proposed**:
  return the decision to the user and require exact source evidence.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish diagnosis, disease progression, biomarker
positivity, causal identification, multimodal completeness, cohort
representativeness, scanner or tracer comparability, ADNI harmonization,
power, analysis validity, clinical utility, generalizability, or legal access
interpretation. It cannot guarantee that an ongoing cohort, IDS inventory,
subset, access term, protocol, or endpoint remains current after the recorded
query date.

## AIBL facts that control the review

Use these as dated orientation and recheck them at invocation:

- AIBL is an ongoing observational longitudinal cohort launched in 2006. It
  uses replenishment recruitment, so cohort membership and counts change.
- The official homepage reports 3,045 participants and 10,494 person-contact
  years specifically **at February 2023**. These are dated facts, not a
  current inventory.
- The original Inception cohort of 1,112 participants is a historical cohort,
  not the current AIBL total. The 2021 review reported 768 cognitively normal,
  133 MCI, and 211 AD participants in that cohort.
- Current official summaries describe a minimum participant age of 50 and
  Alzheimer disease, mild cognitive impairment, and healthy participant
  groups. Exact release-specific diagnostic definitions must still be pinned.
- Study information is collected on an approximately 18-month cycle.
  Schedule labels do not establish that every stream exists at every contact.
- Collection occurs at Perth and Melbourne centers. Site proportions and
  available streams must be verified for the selected product and cycle.
- AIBL spans MRI, PET, biofluid, genetics, cognition, health, and lifestyle
  information. A study-level stream list does not establish participant-level
  multimodal completeness.
- The full Integrated Data Set is nonpublic and governed through a rigorous
  expression-of-interest process reviewed by AIBL management.
- AIBL supplies ADNI researchers a separately authorized collaboration subset
  through LONI. It is not the full IDS and must not be treated as one.
- The LONI/ADNI collaboration subset is limited to participants with PET and
  MR imaging. Its non-imaging tables and elements are incomplete, and access
  uses a distinct AIBL authorization through LONI.
- Official collaboration documentation says the subset's MR images are raw DICOM
  only, include both 1.5 T and 3 T acquisitions, and provide only selected
  ADNI-compliant series. Some older noncompliant baseline imaging is absent.
- MRI scanners, field strengths, and protocols vary. PET acquisition also
  varies across amyloid and tau tracers and collection periods. Pin the exact
  product, scanner, protocol, tracer, and cycle before comparison.
- Mapping some collaboration-subset tables to ADNI structures does not prove
  complete harmonization, shared semantics, or full table coverage.

Do not invent participant identifiers, diagnosis mappings, visit mappings,
SUVR cutoffs, reference regions, QC thresholds, or ADNI harmonization.

## Design choices and verification

These design references describe the workflow, not a prior decision for this user. Apply the current request's scope and required approvals; these notes authorize no additional action.

Use the Applicable Route Comparison only when an unresolved choice warrants comparing evidence-supported full IDS, collaboration-subset, cycle, stream, acquisition, or defer routes. Keep product identity, dated counts, replenishment, completeness, heterogeneity, and governance reviewable in the Product and Evidence Card, Cycle and Stream Map, Applicability Matrix, and Threat and Governance Register.

After Gate 2, record only the elements the user selected in the Dataset Suitability and Access Specification and retain the verification record. This is a specification-only handoff with no data action.

The stronger behaviors of applying for access, authenticating, inspecting
controlled records, downloading data, constructing a cohort, harmonizing
tables, setting thresholds, or testing an analysis are outside this skill.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about disease
  stage, measure validity, cohort comparability, acquisition, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when diagnosis, cycle, site, stream, control, or
  missingness structure changes the design.
- Route access applications, credentials, agreements, secure transfer,
  storage, participant selection, DICOM conversion, curation, preprocessing,
  harmonization, modeling, and interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- ADNI. (n.d.). *AIBL study data*. https://adni.loni.usc.edu/category/aibl-study-data/
- AIBL. (n.d.-a). *AIBL and ADNI imaging*. https://data.aibl.org.au/adni/imaging.html
- AIBL. (n.d.-b). *AIBL and ADNI non-imaging data*. https://data.aibl.org.au/adni/nonimaging.php
- AIBL. (n.d.-c). *AIBL and ADNI subset overview*. https://data.aibl.org.au/adni/index.html
- AIBL. (n.d.-d). *Collaboration*. https://aibl.org.au/collaboration/
- AIBL. (n.d.-e). *The Australian Imaging Biomarkers and Lifestyle (AIBL) study* [Homepage]. https://aibl.org.au/
- Florey. (n.d.). *The Australian Imaging Biomarkers and Lifestyle (AIBL) study*. https://florey.edu.au/research-project/the-australian-imaging-biomarkers-and-lifestyle-aibl-study/
- Fowler et al. (2021). https://doi.org/10.3233/ADR-210005
