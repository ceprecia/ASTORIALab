---
name: adhd200-skill
description: >-
  Evaluates whether one exact ADHD-200 source release, site, raw or preprocessed
  product, modality, phenotype field, correction state, or participant subset
  can support a user-supplied research design and produces a selection-bound
  Dataset Suitability and Access Specification. Use when the request, or a stage
  coordinator, hands over an explicitly matching ADHD-200 question. It distinguishes
  the original 776-person release from later training-plus-test and derivative
  inventories; preserves site, protocol, diagnosis, age, missingness,
  correction, product-provenance, and noncommercial-access boundaries; and
  records only user-selected scope after two approval gates. Triggers: can
  ADHD-200 support my study, ADHD-200 site and product selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: clinical
  dependencies: ""
  requires: NITRC access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# ADHD-200 Dataset Suitability

Evaluate one exact ADHD-200 evidence state without conflating the original
release, competition test data, raw products, or Preprocessed Connectomes
Project derivatives.

## Purpose

It does not register accounts, accept terms, download data, choose participants or diagnosis codes, organize files, preprocess, set QC exclusions, classify cases, analyze data, make scientific claims, search broadly, or save without separate approval.

`adhd200-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about ADHD-200.

It owns:

- pinning the exact release, site, participant grain, modality, phenotype
  schema, correction state, raw product, derivative, and access route;
- distinguishing the original release from later competition-label and
  preprocessed inventories;
- checking whether age, site, diagnostic definition, modality, phenotype,
  acquisition, correction, completeness, and product provenance support the
  stated design;
- comparing only credible site, raw-product, derivative, phenotype, and subset
  routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, diagnosis definition, participant
selection, site model, QC rule, preprocessing pipeline, covariate choice,
power target, classifier, analysis, interpretation, or claim.

It never registers an account, handles credentials, accepts terms, downloads
participant-level data, reorganizes files, preprocesses imaging, excludes
participants, fits a classifier, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `adhd200-skill`; or
- a verified Active capability hands off one explicit ADHD-200 suitability or
  access-planning question.

Do not activate from `ADHD`, `pediatric fMRI`, `resting state`, `download
ADHD data`, `classify ADHD`, or `analyze ADHD-200`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast or relation, outcome, unit, and timing |
| Population boundary | Age, diagnosis or control definition, sites, and generalization target |
| Data requirements | T1w, resting-state fMRI, phenotype, medication, IQ, or QC needs |
| Release boundary | Original release, labeled test set, or exact derivative candidate |
| Product boundary | Raw source or exact PCP pipeline, atlas, nuisance, filtering, and correction state |
| Access boundary | Approved public-document inspection and institutional or storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the ADHD-200 Fit Brief

Return:

- exact scientific target and intended estimand;
- original, competition-test, or exact derivative scope;
- site, age, diagnosis, modality, phenotype, product, correction,
  completeness, and QC requirements;
- candidate raw release, derivative pipeline, manifest, and access state;
- DSM-era, medication, IQ, class-balance, site, scanner, acquisition,
  missingness, correction, storage, and governance constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection, BIDS
organization, preprocessing, diagnosis coding, classification, or analysis,
stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release page, manifest, phenotype key, correction record,
  derivative documentation, terms, or supplied local source to inspect;
- whether an account, agreement, participant-level record, restricted lane, or
  protected path would be encountered;
- release, site, grain, modality, diagnosis, phenotype, correction, product,
  completeness, and access facts to verify;
- stop point before credentials, registration, term acceptance, downloads,
  writes, or handoffs.

Ask:

> Approve this exact ADHD-200 source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, registration, term acceptance, download, search
expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- original release, test-label state, or exact derivative and manifest;
- release or snapshot date, documentation version, repository, and terms;
- participants, imaging records, sites, diagnoses, modalities, phenotype
  rows, and derivative outputs at the correct grain;
- site, scanner, acquisition, rest instruction, diagnostic instrument, and
  phenotype state;
- correction, missingness, completeness, QC, pipeline, atlas, nuisance,
  filtering, and scrubbing state;
- access registration, noncommercial-use, storage, sharing, and citation
  duties;
- conflicts, unknowns, and facts requiring account-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, date, and repository | | | | |
| Participants and imaging records | | | | |
| Sites and age | | | | |
| Diagnosis, subtype, and instrument | | | | |
| T1-weighted MRI | | | | |
| Resting-state fMRI | | | | |
| Phenotype and medication fields | | | | |
| Scanner, acquisition, and rest instruction | | | | |
| Training and test identity | | | | |
| Structural and phenotype corrections | | | | |
| Raw product | | | | |
| PCP derivative pipeline and manifest | | | | |
| Completeness, QC, and missingness | | | | |
| Access, license, and governance | | | | |

Do not infer a complete paired T1w, resting-state, phenotype, and QC sample
from a headline release count.

### 5. Build the Release and Product Map

| Requirement | Original or labeled source route | Exact PCP derivative route | Exact evidence or mismatch |
|---|---|---|---|
| Participants and sites | | | |
| Diagnosis and phenotype | | | |
| T1-weighted MRI | | | |
| Resting-state fMRI | | | |
| Correction state | | | |
| Pipeline and atlas | | | |
| Nuisance, filtering, and scrubbing | | | |
| QC and missingness | | | |
| License and access | | | |

Keep raw data, corrected source packages, and every derivative pipeline
separate.

### 6. Build the Applicability Matrix

| Requirement | Exact dataset route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target age and population | | | | | |
| Diagnosis or symptom construct | | | | | |
| Site and class composition | | | | | |
| Required modality pair | | | | | |
| Phenotype or medication field | | | | | |
| Acquisition compatibility | | | | | |
| Correction and product state | | | | | |
| Missingness and QC tolerance | | | | | |
| Access and noncommercial use | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- original training, competition test, labeled, and derivative inventories;
- participant, scan, image, phenotype-row, and derivative-output grains;
- site, scanner, acquisition, rest instruction, recruitment, and protocol
  heterogeneity;
- site-specific diagnosis instruments, DSM era, subtype codes, medication,
  IQ, and phenotype missingness;
- control-only sites and site-by-diagnosis or site-by-test confounding;
- sex, age, diagnosis, and class imbalance;
- 73-participant structural correction and any later source corrections;
- raw versus PCP product, exact pipeline, atlas, nuisance, filter, scrub, and
  QC state;
- no task-fMRI;
- current NITRC registration, noncommercial-use, download, storage, sharing,
  and citation duties;
- whether intended claims imply current clinical diagnosis, causality, or
  clinical deployment.

Do not inherit a fixed FD threshold or treat preprocessing output as
scientific validation.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact corrected raw-source site or multisite subset;
2. one exact labeled training-plus-test source inventory;
3. one exact PCP pipeline, atlas, and nuisance variant;
4. one exact phenotype-defined subset with site-specific schema checks;
5. one structural-only or resting-state-only route when pairing is incomplete;
6. defer because age, diagnosis, site, modality, phenotype, correction,
   product, QC, license, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- site, diagnostic, acquisition, correction, missingness, and processing
  assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Release and Product Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which ADHD-200 release, sites, participant grain, modalities, phenotype fields, correction and product states, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, registration, term acceptance, credential, download, participant or
diagnosis selection, BIDS action, preprocessing, QC exclusion, classification,
power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, date, repository, participant, site, and access state;
3. age, diagnosis, subtype, instrument, medication, IQ, and population
   boundary;
4. required T1w, resting-state, phenotype, and QC evidence;
5. raw or exact derivative provenance, correction state, pipeline, atlas,
   nuisance, filtering, and scrubbing state;
6. site, scanner, protocol, class-balance, correction, completeness,
   missingness, QC, and product threats;
7. registration, noncommercial-use, security, storage, sharing, citation, and
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

The status is local to the selected design. It is not a diagnostic,
classification, or scientific conclusion.

### 11. Verify and stop

Verify:

- release and access claims are dated;
- original, competition-test, labeled, and derivative inventories remain
  distinct;
- participant, image, phenotype, and derivative grains are not conflated;
- site and diagnosis structure remain visible;
- DSM-era labels are not silently modernized;
- T1w and resting-state completeness are verified separately;
- raw, corrected, and preprocessed products remain distinct;
- pipeline, atlas, nuisance, filtering, scrubbing, and QC states are exact;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, registration, term acceptance, download, selection, write,
  preprocessing, classification, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- release, site, raw or derivative, modality, phenotype, diagnostic, and
  participant candidates;
- treatment of DSM-era labels, subtypes, medication, IQ, site, scanner,
  protocol, missingness, corrections, QC, and class imbalance;
- every access, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and historical-release constraints. It does not
translate diagnosis codes, define a current clinical phenotype, or select a
classification sample for the user.

Use this order:

1. current official FCP/INDI ADHD-200 pages and NITRC records;
2. exact official raw-release, test-label, correction, phenotype-key, and
   download documentation;
3. exact PCP or Neuro Bureau derivative documentation and manifests;
4. primary dataset and competition papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-product fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never let a paper-specific or derivative-specific retained sample become the
official raw-release inventory.

> [!info] References
> Read `./references/adhd_200_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “ADHD data” is supplied**: ask whether ADHD-200 is intended and what
  exact scientific requirement is in scope.
- **776, 947, and 973 are treated as interchangeable**: pin the exact source
  or derivative manifest, state whether the 26 unknown-diagnosis records are
  included, and record grain.
- **All sites use one protocol or diagnostic instrument**: expose the
  site-specific acquisition and phenotype documentation.
- **Every record has T1w, resting-state, phenotype, and QC**: inspect paired
  participant-level completeness.
- **A PCP pipeline is called the raw dataset**: separate source data,
  derivative pipeline, atlas, nuisance, filter, scrub, and output manifest.
- **An uncorrected structural archive is proposed**: verify the 73-participant
  correction state before use.
- **Diagnosis is treated as current or clinical ground truth**: preserve the
  DSM-era and site-specific instrument boundary.
- **Task fMRI is requested**: return **Not suitable for the stated
  requirement** unless a separate dataset is selected.
- **Commercial or clinical use is proposed**: stop and require current
  custodian authorization.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish a current diagnosis, clinical ground truth,
population representativeness, causal identification, classifier validity,
preprocessing superiority, power, analysis validity, generalizability, or
fitness for clinical use. It cannot guarantee that a source, correction,
derivative, agreement, or endpoint remains current after it was last
checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about
  diagnostic instruments, site effects, phenotype validity, preprocessing, or
  prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when site, diagnosis, class, or observation
  structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant unit, site structure, estimand, analysis, inference family, and
  loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route registration, download, transfer, BIDS staging, preprocessing, QC,
  diagnosis coding, participant selection, classification, modeling, and
  interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *ADHD-200 competition results*. (n.d.). NITRC. https://fcon_1000.projects.nitrc.org/indi/adhd200/results.html
- *ADHD-200 phenotypic key* [PDF]. (n.d.). NITRC. https://fcon_1000.projects.nitrc.org/indi/adhd200/general/ADHD-200_PhenotypicKey.pdf
- *ADHD-200 Preprocessed* [Data set]. (n.d.). Preprocessed Connectomes Project. https://github.com/preprocessed-connectomes-project/adhd200
- *ADHD-200 sample* [Data set]. (n.d.). NITRC. https://fcon_1000.projects.nitrc.org/indi/adhd200/index.html
- Bellec et al. (2017). *NeuroImage, 144*(Part 2), 275–286. https://doi.org/10.1016/j.neuroimage.2016.06.034
- FCP/INDI. (n.d.). *FCP/INDI Amazon documentation*. NITRC. https://fcon_1000.projects.nitrc.org/indi/s3/index.html
- NITRC. (2011, April 12). *ADHD-200 structural correction notice* [Forum post]. https://www.nitrc.org/forum/forum.php?forum_id=1735&thread_id=2250
