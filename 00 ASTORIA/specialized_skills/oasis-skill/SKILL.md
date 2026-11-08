---
name: oasis-skill
description: >-
  Evaluates whether one exact OASIS-1, OASIS-2, OASIS-3, OASIS-3 AV1451, or
  OASIS-4 release, cohort, participant grain, visit, modality, clinical field,
  imaging product, access state, or subset can support a user-supplied research
  design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching OASIS question. It preserves release separation,
  cross-release participant overlap, current-versus-paper inventory,
  retrospective multimodal and longitudinal structure, visit matching, tracer,
  diagnostic, scanner, derivative, and data-use boundaries through two approval
  gates. Triggers: can OASIS support my study, OASIS release and visit
  selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: aging
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized data access requires its verified repository route, applicable Data Use Agreement and PET review when required
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# OASIS Dataset Suitability

Evaluate one exact Open Access Series of Imaging Studies source state without turning several distinct releases into one interchangeable Alzheimer disease cohort.

## Purpose

It does not request or download data, combine releases, match identities or visits, choose participants, diagnose disease, create BIDS metadata, preprocess, set QC exclusions, analyze data, make scientific or clinical claims, search broadly, or save without separate approval.

`oasis-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about OASIS-1, OASIS-2, OASIS-3, the separate
OASIS-3 AV1451 project, or OASIS-4.

It owns:

- identifying the exact OASIS release, data dictionary, repository state,
  participant, visit, session, modality, clinical table, processed product,
  tracer, and access grain under review;
- checking whether population, temporal, imaging, phenotype, diagnostic,
  scanner, completeness, governance, and provenance constraints support the
  stated design;
- keeping OASIS releases, current inventories, original papers, processed
  products, and paper-specific subsets separate;
- comparing only credible release, modality, visit-matching, and subset
  routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the research question, disease definition, cognitive-status
rule, visit window, imaging-clinical linkage rule, participant selection,
tracer threshold, QC rule, preprocessing route, covariates, analysis,
interpretation, or claim.

It never requests access, downloads data, links cross-release identities,
matches visits, creates metadata, converts formats, preprocesses images,
computes PET measures, excludes participants, fits a model, or shares data.

Activate only when:

- The user invokes the exact trigger `oasis-skill`; or
- a verified Active capability hands off one explicit OASIS suitability or
  access-planning question.

Do not activate from `Alzheimer`, `dementia MRI`, `aging`, `OASIS`,
`download OASIS`, `process OASIS`, or `analyze OASIS` alone.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Population | Age, cognitive or clinical state, recruitment context, exclusions, and generalization target |
| Unit and structure | Participant, visit, imaging session, scan, clinical assessment, tracer, or processed product |
| Release candidates | Exact OASIS-1, OASIS-2, OASIS-3, OASIS-3 AV1451, or OASIS-4 candidate |
| Time rule | Cross-sectional, longitudinal, conversion, follow-up, or imaging-clinical matching requirement |
| Data requirements | Exact MR, PET, clinical, cognitive, biomarker, demographic, or derivative fields |
| Access boundary | Approved public-document inspection and institutional or storage constraints |
| Intended handoff | Design, power, BIDS planning, bounded literature search, or later analysis |

If the question, population, unit, release, temporal rule, or required fields
are missing, ask only for the missing item. Do not infer it from the word
`OASIS`.

## Steps

### 1. Build the OASIS Fit Brief

Show:

1. The user's exact question and intended decision;
2. population, unit, release, visit, modality, clinical, biomarker, tracer,
   and product requirements;
3. current source states and documents proposed for inspection;
4. known release, overlap, temporal, scanner, completeness, diagnostic,
   derivative, and governance threats;
5. inspection limit and unresolved facts;
6. the exact Gate 1 decision.

Do not search broadly, request data, or inspect participant-level material.

### 2. Gate 1: approve the inspection boundary

Ask the user to approve or revise:

- exact release or release comparison;
- exact public source documents, versions, and retrieval dates;
- population, unit, visit, modality, field, tracer, and product requirements;
- current-versus-paper inventory treatment;
- cross-release overlap and visit-matching questions;
- access, data-use, PET review, and storage questions;
- inspection stop condition.

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize a data request, download, identity linkage, visit matching,
selection, transformation, analysis, save, or handoff.

### 3. Pin exact source and access states

Record:

- release name and project identifier;
- current source page, data dictionary, repository, version, and retrieval
  date;
- release-paper identity and count separately;
- participant, visit, session, scan, tracer, and processed-product grains;
- access request, Data Use Agreement, acknowledgement, citation, PET review,
  storage, sharing, and reidentification conditions;
- local manifest state only if the user supplies and authorizes it;
- unresolved conflicts.

Never write `OASIS dataset` without the release and source state.

### 4. Build the Release and Evidence Card

| Dimension | Source fact | Source and state | Design consequence | Unknown |
|---|---|---|---|---|
| Release identity | | | | |
| Participant and visit inventory | | | | |
| Population and recruitment | | | | |
| Cognitive or clinical definitions | | | | |
| Imaging and biomarker modalities | | | | |
| Scanner and acquisition | | | | |
| Clinical-imaging timing | | | | |
| Processed products | | | | |
| Cross-release overlap | | | | |
| Access and data-use terms | | | | |

Counts must state whether they describe people, visits, sessions, scans,
assessments, tracer sessions, files, or retained observations.

### 5. Build the Release and Temporal Map

| Requirement | OASIS-1 | OASIS-2 | OASIS-3 or AV1451 | OASIS-4 | Mismatch |
|---|---|---|---|---|---|
| Population and recruitment | | | | | |
| Cross-sectional or longitudinal structure | | | | | |
| Visit and date representation | | | | | |
| Required modality or field | | | | | |
| Diagnostic or cognitive construct | | | | | |
| Scanner and protocol | | | | | |
| Processed-product state | | | | | |
| Access and publication duties | | | | | |

Do not recommend combining releases merely to increase sample size.

### 6. Build the Applicability Matrix

| Design requirement | Directly supported | Supported with approved rule | Not supported | Evidence |
|---|---:|---:|---:|---|
| Target population | | | | |
| Required unit and repeat structure | | | | |
| Clinical or cognitive construct | | | | |
| Imaging or biomarker modality | | | | |
| Temporal alignment | | | | |
| Cross-release identity handling | | | | |
| Complete-case or missingness needs | | | | |
| Access and reporting conditions | | | | |

`Supported with approved rule` must name the rule, assumption, sensitivity
check, and decision owner.

### 7. Build the Threat and Governance Register

At minimum assess:

- release conflation and participant overlap;
- original-paper versus current-source inventory drift;
- the unresolved 1,378 summary, 1,379 counter, and 755 plus 622 equals 1,377
  group-count conflict;
- retrospective project, scanner, sequence, and visit heterogeneity;
- nonuniform modality and product availability;
- clinical-imaging timing and arbitrary matching windows;
- repeated observations and participant dependence;
- changing cognition or diagnosis across visits;
- CDR, diagnosis, biomarker, and disease-mechanism conflation;
- selection, survivorship, attrition, missingness, and complete-case bias;
- tracer, reference-region, processing, and PET product differences;
- processed-versus-raw product confusion;
- age, recruitment, memory-clinic, and generalization boundaries;
- reidentification, facial rendering, acknowledgement, citation, PET review,
  storage, sharing, and current Data Use Agreement duties.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact OASIS-1 cross-sectional or reliability route;
2. one exact OASIS-2 longitudinal route;
3. one exact OASIS-3 multimodal or single-modality route;
4. one exact OASIS-3 AV1451 route;
5. one exact OASIS-4 clinical-cohort route;
6. one exact within-release subset with a prespecified visit-matching rule;
7. defer because release, population, timing, modality, field, access, or
   inference requirements are not met.

For each route show evidence, assumptions, tradeoffs, unknowns, access
conditions, and what would falsify suitability. Do not assign numeric
confidence or select a winner.

### 9. Gate 2: select the specification

Carry forward confirmed eligible choices. Ask the user to resolve only the
items below that remain open or have materially changed with new evidence.
Show a comparison only when it was needed to resolve a material choice.
Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10. Address these items in that specification.

- exact release, source state, unit, visits, modalities, fields, tracer, and
  product;
- cognitive, diagnostic, temporal-alignment, overlap, missingness, and
  heterogeneity rules;
- assumptions and sensitivity checks;
- access, acknowledgement, citation, PET review, storage, and sharing duties;
- unresolved limitations;
- next handoff, if any.

Gate 2 authorizes only the selected specification. It does not authorize a
data request, download, identity or visit matching, participant selection,
BIDS action, preprocessing, PET computation, QC exclusion, power calculation,
analysis, saving, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. user-supplied target and estimand;
2. exact OASIS release and source state;
3. population and generalization boundary;
4. participant, visit, session, scan, assessment, tracer, and product grains;
5. required modalities, fields, diagnoses, cognition measures, and timing;
6. release, overlap, visit-matching, scanner, completeness, diagnostic,
   derivative, and missingness threats;
7. selected assumptions and sensitivity checks;
8. access, reidentification, acknowledgement, citation, PET review, storage,
   sharing, and version duties;
9. unresolved unknowns and stop conditions;
10. The user's selections and rejected alternatives;
11. approved next handoff or `none`.

The output is a specification, not an analysis plan or permission to use data.

### 11. Verify and stop

Confirm:

- every count has a source state and grain;
- OASIS releases and AV1451 remain distinct;
- current and paper inventories remain distinct;
- cross-release overlap and visit matching remain explicit;
- clinical fields are not silently converted into diagnoses;
- raw and processed products remain distinct;
- current data-use and PET review duties are visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no access request, download, linkage, write, preprocessing, PET computation,
  exclusion, model, or analysis occurred.

Stop after the verified specification.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and
  confirmatory status;
- the release, cohort, visit, modality, clinical, imaging, tracer, and product
  candidates;
- definitions of cognition, impairment, dementia, Alzheimer disease,
  conversion, baseline, follow-up, temporal alignment, and missingness;
- every access, sampling, preprocessing, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes source facts and design threats. It does not diagnose
participants, infer a clinical endpoint from one field, or select a convenient
release for the user.

Use this order:

1. current OASIS and repository documentation, data dictionaries, request
   forms, and data-use terms;
2. exact release papers and official release notes;
3. user-supplied approved local manifests and documentation;
4. papers for paper-specific methods, subsets, and historical context;
5. external candidate material for prompts and negative evidence only.

Label every statement as one of:

- **Current source fact**
- **Release-paper fact**
- **Paper-specific subset**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never let an original publication count, downloaded local snapshot, processed
product, or paper-specific retained sample redefine a current release.

> [!info] References
> Read `./references/oasis_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only `OASIS` is supplied**: ask which release and scientific requirement
  are intended.
- **A paper reports 1,098 OASIS-3 participants**: preserve it as an original
  release-paper grain, not any one of the conflicting current 1,377, 1,378,
  or 1,379 person counts.
- **OASIS-1, OASIS-2, and OASIS-3 are proposed as one cohort**: stop and expose
  the source warning, possible participant overlap, different identifiers,
  releases, recruitment, protocols, and measures.
- **A nearby clinical and imaging day is called the same visit**: require
  the user's temporal rule and sensitivity analysis.
- **CDR is used as a diagnosis or biomarker**: separate rating, diagnostic,
  cognitive, and biological constructs.
- **Every OASIS-3 participant is assumed to have every modality**: inspect the
  exact participant-by-visit product manifest.
- **All releases are described as 1.5 T T1w data**: restrict that description
  to the verified earlier release and expose OASIS-3 heterogeneity.
- **OASIS-4 is called an OASIS-3 update**: reject the identity and restore the
  distinct clinical-cohort boundary.
- **AV1451 is assumed to share the ordinary OASIS-3 access route**: verify its
  separate request and publication-review duties.
- **A processed FreeSurfer or PUP product is called raw imaging**: preserve
  product provenance and version.
- **An upload, shared-account, facial rendering, reidentification, or
  collaborator access step is proposed**: stop unless the July 2025 agreement
  and separately verified written authorization permit the exact action.

This skill cannot establish diagnosis validity, construct validity, visit
equivalence, causal identification, measurement invariance, missing-at-random
assumptions, preprocessing quality, tracer comparability, power, analytic
validity, clinical utility, or generalizability. It cannot guarantee that a
release, inventory, request process, product, or data-use term remains current
after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about an
  OASIS measure, diagnostic rule, imaging product, tracer, visit window,
  generalization claim, or prior analysis.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when repeated visits, release choice, temporal
  alignment, missingness, or cohort structure changes the design.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the unit, dependence
  structure, estimand, analysis family, and loss assumptions.
- Use [bids](../bids/SKILL.md) only after the user legitimately obtains one exact source product
  and separately approves curation planning.
- Route access requests, downloads, visit matching, preprocessing, PET
  quantification, QC, analysis, interpretation, and reporting to separately
  approved owners.

Every handoff requires separate approval. This skill never chains
automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Koenig et al. (2020). *NeuroImage: Clinical, 26*, Article 102248. https://doi.org/10.1016/j.nicl.2020.102248
- LaMontagne et al. (n.d.). https://doi.org/10.1101/2019.12.13.19014902
- Marcus et al. (2007). *Journal of Cognitive Neuroscience, 19*(9), 1498–1507. https://doi.org/10.1162/jocn.2007.19.9.1498
- Marcus et al. (2010). *Journal of Cognitive Neuroscience, 22*(12), 2677–2684. https://doi.org/10.1162/jocn.2009.21407
- OASIS. (n.d.). *OASIS project*. https://sites.wustl.edu/oasisbrains/
- OASIS. (n.d.). *OASIS-3 imaging methods and data dictionary* (Version 2.3). https://sites.wustl.edu/oasisbrains/files/2024/04/OASIS-3_Imaging_Data_Dictionary_v2.3-a93c947a586e7367.pdf
- OASIS. (2024). *OASIS-4* [Data set]. NITRC. https://www.nitrc.org/projects/oasis4/
- OASIS. (2025, July). *OASIS data use agreement terms*. https://sites.wustl.edu/oasisbrains/files/2025/07/Data-Use-Agreement_July2025.pdf
