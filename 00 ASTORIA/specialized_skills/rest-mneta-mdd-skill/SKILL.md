---
name: rest-mneta-mdd-skill
description: >-
  Evaluates from public metadata whether one exact REST-meta-MDD Phase I
  derivative product, cohort, hospital, diagnostic, episode, medication,
  phenotype, acquisition, preprocessing, access, or participant-subset
  requirement can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching REST-meta-MDD
  question. It preserves 2,428 total, 1,300 MDD, 1,128 control, 25-cohort,
  17-hospital, locally processed final-index, missing-clinical-state, multisite,
  DUA, annual-report, nonleakage, and Phase II separation boundaries through two
  approval gates. It is public-metadata-only and must not receive controlled
  REST-meta-MDD data or phenotypes in chat. Triggers: can REST-meta-MDD support
  my study, REST meta MDD derivative selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: clinical
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized controlled-data action requires the verified Data Use Agreement and applicable access and nonleakage controls
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# REST-meta-MDD Dataset Suitability

Evaluate one exact Phase I REST-meta-MDD evidence state without turning
locally processed consortium indices into a raw, harmonized, clinically
uniform, or analysis-ready fMRI cohort.

The file and trigger retain the approved catalog identifier
`rest-mneta-mdd-skill`. The dataset's proper name is REST-meta-MDD.

## Purpose

It does not obtain credentials, download or unlock data, treat derivatives as raw fMRI or BIDS, choose participants, harmonize, preprocess, set QC exclusions, analyze data, make diagnostic or clinical claims, search broadly, or save without separate approval.

`rest-mneta-mdd-skill` is a conditional Part 3 owner for one bounded
prospective suitability and access question about Phase I of the
REST-meta-MDD project within the DIRECT consortium.

It owns:

- pinning the exact public project page, derivative deposit, Data Use
  Agreement, cohort, hospital, participant or dataset grain, diagnostic,
  episode, medication, phenotype, acquisition, local preprocessing, final
  index, or access state under review;
- checking whether population, clinical, acquisition, processing,
  completeness, multisite, governance, and provenance constraints support
  the stated design;
- keeping the 25 contributed cohorts, 17 hospitals, source acquisitions,
  locally processed indices, shared derivatives, controlled phenotypes,
  paper-specific subsets, and DIRECT Phase II separate;
- comparing only public-metadata-supported routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the scientific question, MDD definition, episode or
medication rule, site model, harmonization method, participant selection, QC
threshold, imaging metric, preprocessing route, covariates, analysis,
interpretation, diagnosis, or claim.

It never signs the agreement, emails the consortium, obtains credentials,
downloads or unlocks data, reads controlled phenotypes, selects participants,
transforms derivatives, preprocesses images, harmonizes, fits a model, or
shares data.

Activate only when:

- The user invokes the exact trigger `rest-mneta-mdd-skill`; or
- a verified Active capability hands off one explicit REST-meta-MDD Phase I
  suitability or access-planning question.

Do not activate from `MDD`, `depression`, `resting-state fMRI`,
`REST-meta-MDD`, `DIRECT`, `download depression data`, or `harmonize sites`
alone.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or construct evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Population | MDD or control definition, episode or medication state, age range, exclusions, and generalization target |
| Unit and structure | Participant, contributed dataset, cohort, hospital, derivative index, phenotype, or public aggregate |
| Product boundary | Exact Phase I derivative or phenotype requirement; raw imaging requests are out of scope |
| Site boundary | One cohort, multiple cohorts, hospital grouping, or cross-cohort target |
| Access boundary | Public metadata only and any institutional containment constraints |
| Intended handoff | Design, power, bounded literature search, or later contained-environment work |

If the question, population, unit, derivative requirement, or cohort boundary
is missing, ask only for the missing item. Do not infer it from `depression`.

## Steps

### 1. Build the REST-meta-MDD Fit Brief

Show:

1. The user's exact question and intended decision;
2. population, unit, cohort, hospital, episode, medication, phenotype,
   derivative, metric, and site requirements;
3. exact public sources and dates proposed for inspection;
4. known derivative-only, multisite, acquisition, local-processing, clinical
   missingness, diagnostic, access, and generalization threats;
5. the public-metadata-only stop point;
6. the exact Gate 1 decision.

Do not access the deposit, request credentials, inspect controlled data, or
search broadly.

### 2. Gate 1: approve the public inspection boundary

Ask the user to approve or revise:

- exact project page, public cohort table, DUA, deposit metadata, code, or
  paper sources;
- exact retrieval date and Phase I product identity;
- population, unit, cohort, hospital, episode, medication, phenotype,
  derivative, and metric requirements;
- controlled-data and missingness questions reserved for future contained
  inspection;
- access, nonleakage, annual-report, citation, acknowledgement, storage, and
  sharing questions;
- inspection stop condition.

Gate 1 authorizes only the displayed public read-only inspection. It does not
authorize email, agreement signature, credential receipt, data access,
download, unlock, participant-level input, selection, transformation,
harmonization, analysis, save, or handoff.

### 3. Pin exact public source and access states

Record:

- Phase I project and deposit identities, DOI, public page date, and retrieval
  date;
- 2,428, 1,300, 1,128, 25-cohort, and 17-hospital grains;
- cohort-specific acquisition and local-processing evidence;
- exact shared-derivative and phenotype description without opening the
  controlled package;
- episode and medication counts and missingness;
- DUA signature, credentials, annual report, nonleakage, citation, and
  acknowledgement duties;
- Phase II separation;
- unresolved conflicts.

Never write `raw REST-meta-MDD fMRI` unless an exact authorized product proves
that claim.

### 4. Build the Public Evidence and Product Card

| Dimension | Public source fact | Source and state | Design consequence | Unknown |
|---|---|---|---|---|
| Phase and deposit identity | | | | |
| Participant or dataset inventory | | | | |
| Cohorts and hospitals | | | | |
| Diagnosis and recruitment | | | | |
| Episode and medication state | | | | |
| Acquisition heterogeneity | | | | |
| Local preprocessing | | | | |
| Shared derivative indices | | | | |
| Phenotype availability | | | | |
| DUA and sharing terms | | | | |

Counts must state whether they describe people, contributed datasets, cohorts,
hospitals, derivative maps, phenotypic rows, or paper-specific observations.

### 5. Build the Cohort and Derivative Map

| Requirement | Exact cohort or product grain | Direct fit | Conditional fit | Mismatch |
|---|---|---|---|---|
| MDD or control population | | | | |
| First episode or recurrent state | | | | |
| Medication state | | | | |
| Cohort or hospital structure | | | | |
| Acquisition requirement | | | | |
| Shared derivative requirement | | | | |
| Phenotype completeness | | | | |
| Access and nonleakage state | | | | |

Do not infer a uniform diagnostic interview, medication history, or raw image
product.

### 6. Build the Applicability Matrix

| Design requirement | Publicly supported | Conditional on contained inspection | Not supported | Evidence |
|---|---:|---:|---:|---|
| Target population | | | | |
| Required unit and cohort structure | | | | |
| Episode or treatment construct | | | | |
| Required derivative metric | | | | |
| Acquisition or site requirement | | | | |
| Phenotype and missingness requirement | | | | |
| Access and governance | | | | |

`Conditional on contained inspection` is a future requirement, not permission
for this skill to open the data.

### 7. Build the Threat and Governance Register

At minimum assess:

- Phase I versus Phase II identity;
- 25 cohorts versus 17 hospitals and use of `site` for cohort;
- participant, contributed-dataset, cohort, hospital, derivative, phenotype,
  and retained-observation grains;
- locally processed final indices versus raw imaging;
- scanner, coil, TR, TE, flip angle, slice, time-point, voxel, and field-of-
  view heterogeneity;
- preprocessing standardization versus local implementation and QC;
- cohort-specific recruitment, diagnosis, instruments, severity, age, sex,
  education, illness duration, and treatment;
- episode status missing for 456 MDD cases;
- medication status missing for 84 first-episode and 85 recurrent cases;
- cross-sectional group differences versus treatment, progression, or causal
  claims;
- site, diagnosis, medication, episode, and demographic confounding;
- later-paper exclusion rules and leakage from site-random splitting;
- DUA signature, password, annual report, third-party nonleakage, citation,
  acknowledgement, storage, and sharing duties.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact full Phase I derivative-index route;
2. one exact MDD-versus-control public design route;
3. one exact first-episode, recurrent, medication, or drug-naive route
   conditional on future contained completeness checks;
4. one exact cohort or hospital subset route;
5. one exact derivative metric route after future manifest verification;
6. defer because product, population, clinical state, acquisition,
   missingness, access, or inference requirements are not met.

For each show public evidence, assumptions, tradeoffs, future contained checks,
unknowns, and what would falsify suitability. Do not assign numeric confidence
or select a winner.

### 9. Gate 2: select the specification

Carry forward confirmed eligible choices. Ask the user to resolve only the
items below that remain open or have materially changed with new evidence.
Show a comparison only when it was needed to resolve a material choice.
Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10. Address these items in that specification.

- exact Phase I source, unit, cohort, hospital, episode, medication,
  phenotype, derivative, and metric;
- diagnostic, clinical, site, missingness, and generalization rules;
- assumptions, sensitivity checks, and future contained verification;
- DUA, credential, annual-report, nonleakage, citation, acknowledgement,
  storage, and sharing duties;
- unresolved limitations;
- next handoff, if any.

Gate 2 authorizes only the selected public-metadata specification. It does not
authorize email, agreement signature, credentials, access, download, unlock,
participant-level input, selection, BIDS action, harmonization, preprocessing,
model training, analysis, saving, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. user-supplied target and estimand;
2. exact Phase I public source states and retrieval dates;
3. population, recruitment, cohort, hospital, and generalization boundary;
4. participant, contributed-dataset, derivative, phenotype, and site grains;
5. required episode, medication, acquisition, metric, and clinical fields;
6. derivative-only, acquisition, processing, missingness, site, selection,
   diagnostic, and generalization threats;
7. selected assumptions, sensitivities, and future contained checks;
8. DUA, credential, annual-report, nonleakage, citation, acknowledgement,
   storage, sharing, and version duties;
9. unresolved unknowns and stop conditions;
10. The user's selections and rejected alternatives;
11. approved next handoff or `none`.

The output is a public-metadata specification, not an analysis plan or
permission to obtain or use the controlled product.

### 11. Verify and stop

Confirm:

- no controlled REST-meta-MDD material entered chat;
- 2,428 equals 1,300 plus 1,128;
- 1,300 equals 562 plus 282 plus 456 episode states;
- first-episode and recurrent medication counts retain their missing values;
- 25 cohorts and 17 hospitals remain distinct;
- source acquisitions, local processing, and shared final indices remain
  distinct;
- Phase I and Phase II remain distinct;
- unrestricted-phase language did not erase DUA duties;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no email, signature, credential, access, download, unlock, write,
  harmonization, model, or analysis occurred.

Stop after the verified specification.

## Boundaries

The REST-meta-MDD Data Use Agreement says users must not leak the data or
phenotypic information to third parties. The controlled package and phenotype
tables therefore must not be pasted, attached, summarized, or inspected in
this chat.

This skill may use only:

- public project and repository metadata;
- the public Data Use Agreement;
- public acquisition and cohort summaries;
- primary papers and public supplementary descriptions;
- The user's abstract design requirements that contain no controlled data.

Never accept:

- participant-level REST-meta-MDD images, derivative maps, indices, rows,
  identifiers, phenotypes, or clinical values;
- unlocked archives, credentials, passwords, FTP listings, or screenshots;
- excerpts or derived values whose sharing would violate the agreement;
- model artifacts or logs that may encode participant-level information.

If such material is offered, do not quote or transform it. State the boundary
and continue only with public metadata or an abstract design question.

`Unrestricted sharing phase` describes removal of proposal-coordination after
2020. It does not remove the signed agreement, credential, annual-report,
nonleakage, citation, or acknowledgement requirements.

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and
  confirmatory status;
- the cohort, hospital, diagnostic, episode, medication, phenotype,
  derivative, metric, and subset candidates;
- definitions of MDD, control, first episode, recurrence, treatment exposure,
  illness duration, severity, site, and generalization;
- every access, containment, sampling, harmonization, analytic, and reporting
  decision;
- the final suitability judgment and downstream action.

This skill exposes public evidence and threats. It does not diagnose a
participant, recommend a convenient subgroup, or turn one shared index into a
clinical biomarker.

Use this order:

1. current REST-meta-MDD project page, data deposit, Data Use Agreement, and
   official cohort or acquisition table;
2. original PNAS paper and DIRECT consortium methods paper;
3. exact public analysis code for historical processing context;
4. later papers only for paper-specific subsets and methods;
5. user-supplied abstract constraints that contain no controlled data;
6. external candidate material for prompts and negative evidence only.

Label every statement as one of:

- **Current public source fact**
- **Original-project fact**
- **Cohort-specific fact**
- **Paper-specific subset**
- **User-supplied abstract constraint**
- **Inference**
- **Unknown**

Never let a later retained sample, a raw-data claim, or DIRECT Phase II
redefine the Phase I shared product.

> [!info] References
> Read `./references/rest_meta_mdd_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only `REST-meta-MDD` is supplied**: ask for the one scientific requirement.
- **The candidate's 3,600-person count is repeated**: replace it with the
  source-pinned Phase I count of 2,428.
- **A site count of 17 or 25 is asserted without grain**: state whether it
  means hospitals or contributed cohorts.
- **The shared product is called raw rs-fMRI or BIDS**: restore the final
  locally processed R-fMRI index boundary.
- **Every case is called first episode, drug-naive, or recurrent**: expose the
  exact categories and missing clinical state.
- **A later paper's retained sample is treated as the release inventory**:
  label it paper-specific and restore 2,428.
- **Unrestricted sharing is treated as no-terms access**: restore signature,
  credential, annual-report, nonleakage, citation, and acknowledgement duties.
- **DIRECT Phase II is proposed as more Phase I participants**: stop and
  separate the resource, deposit, terms, cohorts, and source state.
- **Controlled phenotypes or maps are offered for chat review**: refuse the
  input and keep the work public-metadata-only.
- **A diagnostic classifier is proposed as a clinical tool**: reject the
  clinical claim and preserve site and subset generalization boundaries.

This skill cannot establish diagnosis validity, treatment status, episode
classification, metric reliability, acquisition comparability,
harmonization validity, causal identification, missing-at-random assumptions,
preprocessing quality, power, diagnostic utility, clinical validity, or
generalizability. It cannot guarantee that a deposit, password route, DUA, or
sharing policy remains current after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about an MDD
  construct, clinical measure, acquisition, derivative index, site effect,
  generalization claim, or prior REST-meta-MDD analysis.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when cohort, site, episode, medication,
  missingness, or derivative structure changes the design.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the unit, site and
  participant dependence, estimand, analysis family, and loss assumptions.
- Route data access, contained-environment inspection, selection,
  harmonization, preprocessing, modeling, analysis, and reporting to
  separately approved owners.

Every handoff requires separate approval. This skill never chains
automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Chen et al. (2022). [DIRECT methods paper]. *Psychoradiology, 2*(1), 32–42. https://doi.org/10.1093/psyrad/kkac005
- DIRECT. (2025, June 11). *DIRECT Phase II* [Project page]. https://rfmri.org/DIRECTPhase2
- REST-meta-MDD. (n.d.-a). [Phase I derivative deposit] [Data set]. Psychological Science Data Bank. https://doi.org/10.57760/sciencedb.o00115.00013
- REST-meta-MDD. (n.d.-b). *REST-meta-MDD data use agreement*. https://rfmri.org/sites/default/files/REST-meta-MDD_Data_Use_Agreement.pdf
- REST-meta-MDD. (2022, June 15). *REST-meta-MDD* [Project page]. https://rfmri.org/REST-meta-MDD
- Yan et al. (2019). [Original REST-meta-MDD analysis]. *PNAS, 116*(18), 9078–9083. https://doi.org/10.1073/pnas.1900390116
