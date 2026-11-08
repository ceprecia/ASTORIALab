---
name: hbn-skill
description: >-
  Evaluates whether one exact Healthy Brain Network release, modality, phenotype
  tier, site, or participant subset can support a user-supplied research design
  and produces a selection-bound Dataset Suitability and Access Specification.
  Use when the request, or a part coordinator, hands over an explicitly matching HBN
  question. It verifies current release and access state; distinguishes
  community-referred recruitment from a healthy-control cohort; maps MRI, EEG,
  eye-tracking, phenotype, diagnostic, licensing, site, missingness, and
  cross-modality linkage limits; and records only user-selected scope after two
  approval gates. It does not create accounts, handle credentials, submit
  agreements, download data, define diagnoses, choose participants, organize
  files, preprocess, set QC exclusions, analyze data, make scientific claims,
  search broadly, or save without separate approval. Triggers: can HBN support
  my study, Healthy Brain Network data selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: developmental
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized controlled-data action requires the applicable verified access authorization and data-use agreement
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Healthy Brain Network Dataset Suitability

Evaluate one exact HBN evidence state without turning the word “healthy,” an
open-imaging route, or an external orchestration prompt into a scientific or
technical pipeline.

## Purpose

`hbn-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Child Mind Institute Healthy Brain
Network Biobank.

It owns:

- pinning the exact release, modality, phenotype tier, site, participant
  subset, access route, license, and dictionary;
- checking whether the proposed population, measures, modalities, diagnostic
  evidence, and linkage exist at the intended grain;
- exposing recruitment, site, scanner, protocol, missingness, diagnostic,
  licensing, and cross-modality threats;
- comparing only credible HBN release, modality, phenotype, or subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnosis, phenotype construction,
participant selection, QC rule, covariate choice, power target, analysis,
interpretation, or scientific claim.

It never creates an account, handles credentials, submits a Data Use Agreement,
accepts terms, downloads participant-level data, reorganizes files,
preprocesses imaging or EEG, merges phenotypes, excludes participants, fits a
model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `hbn-skill`; or
- a verified Active capability hands off one explicit HBN suitability or
  access-planning question.

Do not activate from `HBN`, `healthy brain`, `autism dataset`,
`developmental psychopathology`, `multimodal pediatric data`, `download HBN`,
or `analyze HBN`.

For broad dataset discovery or comparison, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measure evidence, offer a bounded
[paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast or dimension, outcome, unit, and timing |
| Population boundary | Age, recruitment, diagnostic, comparison, and exclusion needs |
| Data requirements | MRI, EEG, eye-tracking, phenotype, quality, and linkage needs |
| Release boundary | Candidate release or need to identify the current state |
| Evidence needs | Instruments, diagnostic process, modality completeness, and provenance |
| Access boundary | Approved public-document inspection and institutional, commercial-use, or security constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the HBN Fit Brief

Return:

- exact scientific target and intended estimand;
- population, recruitment, age, diagnosis, and comparison requirements;
- modality, phenotype, instrument, quality, and linkage requirements;
- candidate release, distribution, site, participant, and license states;
- access, commercial-use, security, and storage constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, phenotype construction,
participant selection, preprocessing, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release, FAQ, modality, phenotype, agreement, license, or
  supplied local sources to inspect;
- whether any account, agreement, participant-level record, restricted lane,
  or protected path would be encountered;
- release, linkage, instrument, and access facts to verify;
- stop point before credentials, agreements, downloads, writes, or handoffs.

Ask:

> Approve this exact HBN source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, agreement submission, restricted-data
access, download, search expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- release, cutoff, note date, distribution, and metadata snapshot;
- record counts at the correct grain: people, datasets, files, sessions, or
  modality releases;
- MRI, EEG, eye-tracking, minimal-demographic, and full-phenotype routes;
- selected site, phase, instrument, diagnostic, and modality state;
- current agreement, registration, license, `Commercial_Use`, and access
  conditions;
- dictionary, release-manifest, and known-issue versions;
- conflicts, unknowns, and facts requiring account-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Dataset Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Recruitment and population | | | | |
| Age and demographic coverage | | | | |
| Diagnostic process and certainty | | | | |
| Sites, phases, scanners, and protocols | | | | |
| MRI | | | | |
| EEG | | | | |
| Eye-tracking | | | | |
| Minimal demographics | | | | |
| Full phenotype and instruments | | | | |
| Other biological or digital modalities | | | | |
| Cross-modality linkage | | | | |
| Missingness and quality | | | | |
| Access, agreement, and license | | | | |

Do not mark a modality, diagnosis, instrument, or license as available for the
proposed sample merely because it exists somewhere in HBN.

### 5. Build the Cross-Modality Linkage Map

| Required component | Exact release or route | Participant-level linkage evidence | Timing relation | Missingness or mismatch |
|---|---|---|---|---|
| MRI | | | | |
| EEG | | | | |
| Eye-tracking | | | | |
| Minimal demographics | | | | |
| Full phenotype | | | | |
| Diagnostic evidence | | | | |
| Quality record | | | | |

Preserve differing release groups, timing, site, and identifier systems.

### 6. Build the Applicability Matrix

| Requirement | Exact HBN route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Recruitment or ascertainment | | | | | |
| Diagnostic or dimensional construct | | | | | |
| Modality | | | | | |
| Instrument or outcome | | | | | |
| Cross-modality linkage | | | | | |
| Site and scanner structure | | | | | |
| Missingness tolerance | | | | | |
| License and intended use | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only with the exact unresolved condition visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- community-referred enrichment and target-population mismatch;
- cross-sectional versus requested longitudinal inference;
- age, demographic, site, scanner, phase, protocol, and recruitment
  heterogeneity;
- diagnostic instrument, algorithm, certainty, and missingness;
- incomplete or nonconcurrent modality and phenotype linkage;
- modality-release rows counted as people;
- imaging or EEG available before full phenotype release;
- quality levels and nonrandom quality missingness;
- participant-level commercial-use restrictions;
- open-imaging versus DUA-controlled phenotype boundaries;
- unreleased or partially released digital, voice, video, actigraphy,
  biological, or genetic resources;
- whether a nominal diagnosis is being treated as a definitive clinical label;
- whether intended claims exceed a cross-sectional observational resource.

Do not call the released sample healthy, population-representative,
longitudinal, completely multimodal, or uniformly licensed.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one pinned MRI route plus minimal demographics;
2. one pinned EEG or eye-tracking route plus minimal demographics;
3. one DUA-controlled phenotype route;
4. one explicitly verified linked multimodal subset;
5. one license-compatible participant subset;
6. defer HBN because population, diagnosis, modality, linkage, access,
   commercial-use, or timing requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- recruitment, linkage, missingness, and diagnostic assumptions;
- access and license burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Dataset Evidence Card;
- Cross-Modality Linkage Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which HBN release, modality, phenotype, linkage, license, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, agreement, credential, download, participant or variable selection,
BIDS action, preprocessing, QC exclusion, power calculation, analysis, save,
or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, cutoff, distribution, site, modality, phenotype, and license
   state;
3. recruitment, population, age, diagnostic, and comparison boundary;
4. required instruments and diagnostic evidence;
5. participant-level cross-modality linkage requirement;
6. site, scanner, protocol, phase, quality, and missingness threats;
7. access, agreement, registration, commercial-use, security, storage, and
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

The status is local to the selected design. It is not a clinical or scientific
conclusion.

### 11. Verify and stop

Verify:

- release and access claims are dated;
- program, release, modality, and unique-person counts are not conflated;
- HBN is not labeled a healthy-control or epidemiologic cohort;
- cross-sectional and repeated-variable claims remain distinct;
- open modalities and controlled phenotypes remain distinct;
- participant-level license limits remain visible;
- site, instrument, diagnosis, modality, and linkage claims are verified at the
  selected grain;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, agreement, download, selection, write, preprocessing, or
  analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether HBN is considered;
- the scientific question, target population, estimand, group or dimensional
  contrast, outcome, and confirmatory status;
- release, modality, phenotype, diagnostic, site, participant, and license
  candidates;
- acceptable recruitment, site, scanner, protocol, missingness, and linkage
  limits;
- every access, agreement, security, storage, sampling, analytic, and reporting
  decision;
- the final suitability judgment and downstream action.

This skill exposes what is available and what it cannot support. It does not
turn a variable or diagnosis field into a scientific construct for the user.

Use this order:

1. current official Child Mind Institute HBN and INDI HBN pages;
2. exact official release notes, modality manifests, phenotype dictionaries,
   FAQ, agreements, and participant-level license fields;
3. exact selected BIDS or non-BIDS distribution metadata;
4. primary cohort and methods papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-distribution fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Do not infer a participant count by adding modality-release rows.

> [!info] References
> Read `./references/hbn_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “HBN” is supplied**: Ask for the scientific requirement. Do not choose
  a release, modality, phenotype, or participant subset.
- **“Healthy controls” are requested**: Require the exact comparison
  definition and evidence. Do not infer it from the dataset name.
- **An autism cohort is requested**: Verify the exact assessment and certainty
  fields. HBN is not a comprehensive autism cohort.
- **An 8,000 or 10,000 participant claim appears**: distinguish program impact
  or recruitment target from released analytic records.
- **Release-table counts are summed**: stop and identify unique people,
  modalities, sessions, and release groups.
- **Longitudinal inference is requested**: record the cross-sectional design
  mismatch unless an exact repeated structure supports the specific estimand.
- **Open imaging is linked to full phenotypes**: verify identifiers, timing,
  agreement, and participant-level coverage.
- **Commercial use is proposed**: inspect `Commercial_Use` for the selected
  participants and the exact distribution terms.
- **Actigraphy, voice, video, or genetics are assumed released**: verify the
  current official modality state and separate repository or agreement.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, diagnostic validity,
longitudinal change, multimodal completeness, causal identification, power,
analysis validity, generalizability, or fitness for clinical use. It cannot
guarantee that a release, route, instrument, count, agreement, license, or
endpoint remains current after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about HBN
  recruitment, diagnostic measures, modality validity, missingness, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when ascertainment, linkage, or cross-sectional
  structure changes the design.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the exact analytic subset,
  units, dependency structure, effect basis, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route access administration, download, storage, preprocessing, EEG or
  imaging QC, phenotype construction, participant selection, modeling, and
  interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Child Mind Institute. (n.d.). *HBN about*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/About.html
- Child Mind Institute. (n.d.). *HBN FAQ*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/FAQ.html
- Child Mind Institute. (n.d.). *HBN MRI and EEG*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/MRI_EEG.html
- Child Mind Institute. (n.d.). *HBN phenotypic data*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/Phenotypic.html
- Child Mind Institute. (n.d.). *HBN project*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/Project.html
- Child Mind Institute. (n.d.). *HBN Release 11 notes*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/release/release_notes11_0.html
- Child Mind Institute. (n.d.). *HBN releases*. https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/Releases.html
- Child Mind Institute. (n.d.). *Healthy Brain Network*. https://childmind.org/science/global-open-science/healthy-brain-network/
