---
name: abide-skill
description: >-
  Evaluates whether one exact ABIDE release, site, modality, phenotype, or
  participant subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching ABIDE question.
  It distinguishes ABIDE I, ABIDE II, raw distributions, and separately derived
  preprocessed resources; verifies current official identity, access, license,
  and metadata; exposes site, protocol, diagnostic, modality, missingness,
  repeat-observation, and governance threats; and records only user-selected
  scope after two approval gates. It does not create accounts, handle
  credentials, download data, choose participants, define diagnoses, organize
  BIDS files, preprocess, set QC exclusions, analyze data, make clinical or
  scientific claims, search broadly, or save without separate approval.
  Triggers: can ABIDE support my study, ABIDE site and phenotype selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: autism
  dependencies: ""
  requires: ABIDE access (NITRC or download), phenotype files
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-11-02"
---

# ABIDE Dataset Suitability

Evaluate ABIDE as a prospective evidence source without turning a public
dataset, old mirror, or external orchestration prompt into an automatic
pipeline.

## Purpose

`abide-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Autism Brain Imaging Data Exchange.

It owns:

- distinguishing ABIDE I, ABIDE II, exact contributing sites, and selected
  distributions;
- checking whether the intended population, modalities, sessions, measures,
  and site structure exist in the exact proposed subset;
- identifying repeated observations, cross-site heterogeneity, missingness,
  access, license, and governance constraints;
- comparing only scientifically credible ABIDE release, site, modality,
  phenotype, or derivative routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own:

- the research question, hypothesis, estimand, diagnostic definition, sample
  inclusion rule, covariate choice, power target, analysis, interpretation, or
  scientific claim;
- account creation, credentials, data-use acceptance, download, transfer, or
  storage;
- BIDS mapping, file organization, preprocessing, harmonization, QC exclusion,
  model fitting, or visualization;
- broad paper discovery or a cross-dataset recommendation.

Activate only when:

- The user invokes the exact trigger `abide-skill`; or
- a verified Active capability hands off one explicit ABIDE suitability or
  access-planning question.

Do not activate from broad phrases such as `autism`, `autism imaging`,
`developmental dataset`, `public fMRI`, `dataset search`, `download ABIDE`, or
`analyze ABIDE`.

For a broad dataset comparison, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For literature coverage, use [paper-search](../../skills/paper-search/SKILL.md) after
separate approval.

## Inputs

Ask for or recover only the minimum needed:

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, exposure or contrast, outcome, and unit |
| Population boundary | Age, diagnostic grouping, comparison group, and exclusions under consideration |
| Data requirements | Structural MRI, resting-state fMRI, other modality, phenotype, QC, and session needs |
| Design structure | Cross-sectional or repeated-observation needs; site and scanner handling |
| Evidence needs | Measures, acquisition details, sample counts, missingness, and provenance needed before judgment |
| Access boundary | Approved network inspection, institutional constraints, license needs, and storage constraints |
| Intended handoff | Design revision, bounded search, power planning, BIDS planning, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the research target is absent, return that gap. Do not formulate it.

## Steps

### 1. Build the ABIDE Fit Brief

Return:

- the exact ABIDE question;
- fixed scientific requirements;
- release, site, modality, phenotype, and session candidates;
- evidence and access boundaries;
- known unknowns;
- requested output and stop point.

If the request is really broad dataset discovery, participant selection,
preprocessing, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official pages, selected distribution, dictionary, or supplied files
  to inspect;
- whether any login, account, usage agreement, protected location, or
  participant-level record would be encountered;
- facts to verify;
- privacy and access limits;
- stop point before any account, download, write, or handoff.

Ask:

> Approve this exact ABIDE source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, acceptance of terms, participant-level
download, search expansion, saving, or another capability.

### 3. Pin the exact ABIDE state

Record:

- ABIDE I, ABIDE II, or both;
- exact site, collection, release, snapshot, derivative, or mirror;
- source URL, access date, release date, and version where available;
- current access route and license or data-use terms;
- data dictionary and site-protocol version;
- counts at the correct grain: datasets, unique people, sessions, or files;
- evidence gaps and conflicting source states.

If the selected state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Dataset Evidence Card

| Dimension | Verified state | Grain and provenance | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Population and recruitment | | | | |
| Diagnostic and comparison definitions | | | | |
| Age and demographic coverage | | | | |
| Sites, scanners, and protocols | | | | |
| Structural MRI | | | | |
| Resting-state fMRI | | | | |
| Additional modalities | | | | |
| Phenotype and assessments | | | | |
| Sessions and repeat observations | | | | |
| Missingness and quality metadata | | | | |
| Raw or derivative provenance | | | | |
| Access, license, and use limits | | | | |

Do not mark a modality or measure available for the proposed sample merely
because it exists somewhere in ABIDE.

### 5. Build the Applicability Matrix

| Requirement | Exact ABIDE route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Population | | | | | |
| Diagnostic definition | | | | | |
| Comparator | | | | | |
| Imaging modality | | | | | |
| Phenotype or outcome | | | | | |
| Cross-sectional or repeated design | | | | | |
| Site and scanner structure | | | | | |
| Sample independence | | | | | |
| Missingness tolerance | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 6. Build the Heterogeneity and Threat Register

Check at minimum:

- site, scanner, field strength, sequence, and instruction differences;
- recruitment and ascertainment differences;
- diagnostic instrument, algorithm, and certainty differences;
- age, sex, IQ, medication, motion, and quality coverage;
- participant, session, and collection overlap;
- structural and resting-state availability at the selected grain;
- task, diffusion, field-map, or extended phenotype availability by site;
- nonrandom missingness and site-confounded missingness;
- raw-versus-derivative pipeline and censoring provenance;
- whether planned group labels flatten meaningful uncertainty;
- whether the selected aggregate supports the claimed target population;
- whether the intended model can represent site and repeated observations.

Never describe ABIDE as clinically or demographically representative without a
specific justified target and evidence.

### 7. Build the Governance and Access Matrix

| Route | Registration or agreement | License or use limit | Participant-level sensitivity | Current-state confidence | Action owner |
|---|---|---|---|---|---|
| Raw ABIDE I | | | | | |
| Raw ABIDE II | | | | | |
| Selected official mirror | | | | | |
| ABIDE Preprocessed derivative | | | | | |

Do not request, receive, display, or store credentials. Do not accept terms for
The user. An accessible URL is not authorization to use, redistribute, or share
the data.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one pinned ABIDE I site or subset;
2. one pinned ABIDE II site or subset;
3. a justified cross-site raw subset with explicit heterogeneity controls;
4. a version-pinned preprocessed derivative with its pipeline provenance;
5. defer ABIDE because a required modality, measure, longitudinal structure,
   access condition, or target population is not supported.

For each route show:

- exact scope;
- what it enables;
- what it cannot establish;
- assumptions;
- access burden;
- missing evidence;
- threats and downstream handoffs.

Do not rank routes unless the user supplies a decision rule and asks for a
comparison under that rule.

### 9. Gate 2: select the specification

Show:

- complete Dataset Evidence Card;
- Applicability Matrix;
- Heterogeneity and Threat Register;
- Governance and Access Matrix;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and stop conditions.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which ABIDE route, subset, assumptions, and downstream handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, agreement, credential, download, participant selection, BIDS action,
preprocessing, QC exclusion, power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact ABIDE release, site, subset, session, and distribution state;
3. required modalities and phenotype fields;
4. unit of observation and repeat-observation handling requirement;
5. site, scanner, protocol, diagnostic, and missingness threats;
6. raw or derivative provenance;
7. access route, license, governance, and storage requirements;
8. selected assumptions and explicit non-assumptions;
9. unresolved evidence gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status applies only to the stated boundary. It is not a scientific
conclusion or a claim that the eventual analysis will be valid.

### 11. Verify and stop

Verify:

- every release, count, field, access, and license claim has a dated source;
- dataset counts are not mislabeled as unique people;
- ABIDE I and II are not silently merged;
- cross-sectional and repeated observations are correctly separated;
- raw and preprocessed resources remain distinct;
- site-specific modalities and phenotypes are not treated as universal;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, account, download, write, preprocessing, selection, or
  analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question and intended estimand;
- whether ABIDE is considered at all;
- which release, site, participant, modality, phenotype, and session options
  remain candidates;
- acceptable heterogeneity, missingness, overlap, and access burden;
- inclusion, exclusion, diagnostic, QC, covariate, and analysis decisions;
- the final suitability judgment and every downstream action.

This skill may expose evidence, compare applicable routes, and test design fit.
It must not select a dataset or scientific rule for the user.

Use this order:

1. the exact current official ABIDE, ABIDE I, ABIDE II, and access pages;
2. the exact selected distribution, release metadata, data dictionary, site
   protocol, license, and usage agreement;
3. versioned derivative documentation when a preprocessed resource is being
   considered;
4. primary dataset papers for historical design and collection context;
5. user-supplied local records;
6. external candidate material only as provenance and negative evidence.

Label every material statement as one of:

- **Verified current source fact**
- **Dated official release fact**
- **Selected-distribution fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never turn a dated cohort count, mirror, endpoint, license, phenotype field, or
preprocessed derivative into a timeless fact.

Edge cases:

- **Only “ABIDE” is supplied**: Ask for the scientific requirement. Do not
  choose I, II, a site, or a derivative.
- **ABIDE I and II are requested together**: Preserve separate release,
  participant, session, site, phenotype, and provenance records before
  considering aggregation.
- **A unique-person total is requested**: Do not add published dataset counts.
  Verify identifiers, repeat observations, and overlap in the selected state.
- **Longitudinal inference is requested**: Identify the exact ABIDE II repeat
  subset and determine whether its structure supports the intended estimand.
- **A site-specific modality is requested**: Verify it at the selected
  participant and session grain.
- **A preprocessed download is proposed**: Record exact pipeline, strategy,
  censoring, release, coverage, and provenance. Do not call it raw ABIDE.
- **An old mirror is named**: Verify that it still operates and that its terms
  and snapshot match the proposed use.
- **Commercial or redistribution use is proposed**: Recheck the exact
  distribution license and institutional obligations.
- **The request asks for a research classifier**: record the approved
  scientific target and route research design and analysis separately.
  Prediction of dataset labels does not establish diagnostic validity.
- **The request asks for individual clinical inference**: stop. This is outside
  ASTORIA research scope and requires qualified human clinical expertise.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, diagnostic validity,
harmonization, causal identification, generalizability, power, analysis
validity, or fitness for clinical use. It cannot guarantee that an endpoint,
mirror, participant set, field, or license remains current after it was
last checked.
- ABIDE I's distribution page reports CC BY-NC-SA terms and a login requirement; recheck the exact use terms before any access action.

## ABIDE facts that control the review

Use these as dated orientation, then recheck the exact current sources at
invocation:

- ABIDE is a retrospective aggregation of independently collected datasets,
  not one prospectively harmonized cohort.
- The official ABIDE I page reports 1,112 datasets from 17 sites, including 539
  autism spectrum disorder and 573 control datasets, ages 7 to 64, released in
  2012.
- The official ABIDE II page reports 1,114 datasets from 19 sites, including
  521 autism spectrum disorder and 593 control datasets, ages 5 to 64,
  released in 2016.
- ABIDE II reports two collections containing 38 individuals assessed twice.
  Its dataset count is therefore not automatically a unique-person count.
- Structural MRI and resting-state fMRI define the common ABIDE I imaging
  identity. Additional imaging or phenotype fields in ABIDE II are
  site-specific unless the selected records prove otherwise.
- ABIDE I is cross-sectional. ABIDE II is predominantly cross-sectional with a
  small explicitly identified repeated-observation subset.
- Acquisition, scanner, instructions, diagnostic procedures, assessments,
  medication reporting, quality, and missingness vary by site.
- Raw and derivative distributions are different evidence objects. The ABIDE
  Preprocessed resource is not raw ABIDE, a consensus pipeline, or proof of
  equal ABIDE I and II coverage.
- Raw access has historically required NITRC registration or distribution-
  specific membership and terms. Old LORIS, LONI, COINS, NITRC, or other
  mirrors must be checked before recommendation.

Do not sum ABIDE I and II and call the result a unique-person count without
checking identifiers, sessions, and overlap.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about ABIDE
  validity, measure coverage, preprocessing comparisons, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when the dataset review exposes a design choice.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the exact analytic subset,
  unit structure, effect basis, and loss assumptions.
- Use [bids](../bids/SKILL.md) to design a curation specification for an already acquired and
  governed source.
- Route download, storage, preprocessing, harmonization, QC, participant
  selection, and analysis to the appropriate later capability only after
  separate approval.

Handoffs carry the selected specification and unresolved gaps. They do not
activate the destination.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- [ABIDE access page]. (n.d.). https://fcon_1000.projects.nitrc.org/indi/abide/databases.html
- *ABIDE I* [Data set]. (n.d.). https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html
- *ABIDE II* [Data set]. (n.d.). https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html
- *ABIDE Preprocessed* [Data set]. (n.d.). http://preprocessed-connectomes-project.org/abide/
