---
name: ixi-skill
description: >-
  Evaluates whether one exact IXI source archive, hospital site, T1, T2, PD,
  MRA, diffusion product, demographic field, license state, or participant
  subset can support a user-supplied research design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching IXI question. It
  pins exact archive files and hashes because the official page has no semantic
  release; preserves nearly-600 versus verified-manifest counts, site and
  scanner heterogeneity, modality-specific completeness, source-health-label,
  demographic, format, and CC BY-SA 3.0 boundaries; and records only
  user-selected scope after two approval gates. Triggers: can IXI support my
  study, IXI site and sequence selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: smri
  population: general
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized download or use follows the selected archive's verified CC BY-SA terms
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# IXI Dataset Suitability

Evaluate one exact IXI source state without turning a legacy multimodal archive
into a versioned, complete, harmonized, or BIDS-ready cohort.

## Purpose

It does not download data, choose participants, infer health or site labels, organize files, create metadata, convert formats, preprocess, perform vessel or diffusion analysis, set QC exclusions, analyze data, make scientific or clinical claims, search broadly, or save without separate approval.

`ixi-skill` is a conditional Part 3 owner for one bounded prospective
suitability and access question about the IXI Dataset.

It owns:

- pinning the exact official archive URL, retrieval date, local hash, hospital
  site, participant grain, modality, demographic file, format, and license;
- checking whether source health labeling, site, scanner, field strength,
  modality, acquisition, completeness, demographic, and provenance support
  the stated design;
- keeping original IXI products separate from IXI Tiny and other third-party
  preprocessed mirrors;
- comparing only credible site, modality, archive, and subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, health definition, participant
selection, site model, modality pairing, QC rule, preprocessing route,
covariate choice, power target, analysis, interpretation, or claim.

It never downloads data, infers site from an unchecked filename, reorganizes
files, fabricates sidecars, converts formats, preprocesses imaging, performs
vessel or diffusion analysis, excludes participants, fits a model, or uploads
or shares data.

Activate only when:

- The user invokes the exact trigger `ixi-skill`; or
- a verified Active capability hands off one explicit IXI suitability or
  access-planning question.

Do not activate from `healthy MRI`, `brain age`, `MRA`, `download IXI`,
`process IXI`, or `analyze IXI`.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast or relation, outcome, unit, and timing |
| Population boundary | Intended health, age, demographic, and generalization target |
| Data requirements | T1, T2, PD, MRA, DTI, demographics, or QC needs |
| Site requirements | Hammersmith, Guy's, Institute of Psychiatry, multisite, or unresolved |
| Archive boundary | Exact official archive or local source candidate and retrieval date |
| License boundary | Intended use, adaptation, redistribution, and share-alike needs |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the IXI Fit Brief

Return:

- exact scientific target and intended estimand;
- health, age, demographic, site, scanner, field-strength, modality, product,
  pairing, format, and completeness requirements;
- candidate archive URL, retrieval state, manifest, and license;
- screening, site, protocol, missingness, derivative, storage, and
  share-alike constraints;
- known unknowns;
- requested output and stop point.

If the request is really download, participant selection, site inference,
BIDS organization, metadata creation, conversion, preprocessing, vessel or
diffusion analysis, or modeling, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official page, archive headers, parameter page, demographic schema,
  license, or supplied local source to inspect;
- whether participant-level records, protected paths, unverified mirrors, or
  large archives would be encountered;
- archive, participant, site, modality, format, completeness, demographic, and
  license facts to verify;
- stop point before downloads, archive extraction, writes, search expansion,
  or handoffs.

Ask:

> Approve this exact IXI source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize download, archive extraction, participant selection, search
expansion, saving, or another capability.

### 3. Pin the exact archive and access state

Record:

- official page state and access date;
- archive URL, filename, size, retrieval timestamp, and hash;
- participants, site labels, scans, modalities, demographic rows, and files
  at the correct grain;
- scanner, field strength, acquisition, protocol, orientation, format, and
  metadata state;
- participant-level modality pairing, missingness, and known issues;
- CC BY-SA 3.0 attribution, adaptation, redistribution, and share-alike duties;
- conflicts, unknowns, and facts requiring file-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Archive and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Official source, retrieval date, and hash | | | | |
| Participants and source health label | | | | |
| Demographic fields | | | | |
| Hammersmith site and scanner | | | | |
| Guy's site and scanner | | | | |
| Institute of Psychiatry site and scanner | | | | |
| T1 and T2 | | | | |
| PD and MRA | | | | |
| DTI and gradient metadata | | | | |
| Format and metadata | | | | |
| Participant-level modality completeness | | | | |
| License, attribution, and share-alike | | | | |

Do not infer complete pairing from the existence of separate modality
archives.

### 5. Build the Site and Modality Map

| Requirement | Hammersmith | Guy's | Institute of Psychiatry | Exact evidence or mismatch |
|---|---|---|---|---|
| Scanner and field strength | | | | |
| T1 | | | | |
| T2 | | | | |
| PD | | | | |
| MRA | | | | |
| DTI and gradients | | | | |
| Demographic linkage | | | | |
| Acquisition metadata | | | | |
| Participant-level completeness | | | | |

Keep site, scanner, modality, protocol, and participant grains separate.

### 6. Build the Applicability Matrix

| Requirement | Exact archive route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population and health definition | | | | | |
| Age or demographic requirement | | | | | |
| Required site or multisite design | | | | | |
| Required modality pair | | | | | |
| Acquisition compatibility | | | | | |
| Format and metadata sufficiency | | | | | |
| Completeness and QC tolerance | | | | | |
| License and redistribution | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and License Register

Check at minimum:

- approximate headline count versus exact manifest;
- participant, scan, modality-file, and demographic-row grains;
- source health label versus documented screening and incidental findings;
- Hammersmith, Guy's, and Institute of Psychiatry identity;
- Philips versus GE and 3 T versus 1.5 T;
- site and modality acquisition parameters;
- participant-level T1, T2, PD, MRA, DTI, demographics, and gradient
  completeness;
- cross-sectional versus unsupported longitudinal assumptions;
- original source versus IXI Tiny and third-party derivatives;
- NIfTI, orientation, sidecar, gradient, and BIDS metadata state;
- CC BY-SA 3.0 attribution, adaptation, redistribution, and share-alike
  implications;
- whether intended claims exceed a historical convenience sample labeled
  normal or healthy.

Do not manufacture JSON sidecars or interpret filename codes without an exact
source map.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact site and structural modality;
2. one exact multisite T1 or T2 route;
3. one exact participant-level multimodal paired route;
4. one exact MRA route;
5. one exact DTI route with verified gradients;
6. one exact original-versus-derivative comparison;
7. defer because health, population, site, modality, metadata, completeness,
   format, license, or inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- source-health, site, scanner, protocol, missingness, format, and license
  assumptions;
- storage burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Archive and Evidence Card;
- Site and Modality Map;
- Applicability Matrix;
- Threat and License Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which IXI archives, sites, modalities, demographic fields, format and license states, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize
download, archive extraction, participant or site selection, BIDS action,
metadata fabrication, conversion, preprocessing, QC exclusion, vessel or
diffusion analysis, power calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact official source, access date, archive URL, filename, size, and hash;
3. participant, source-health, demographic, site, scan, modality, and file
   grains;
4. required T1, T2, PD, MRA, DTI, gradients, and metadata;
5. scanner, field strength, acquisition, protocol, format, completeness,
   missingness, and QC threats;
6. original-versus-derivative provenance;
7. CC BY-SA 3.0 attribution, adaptation, redistribution, and share-alike
   duties;
8. selected assumptions and explicit non-assumptions;
9. unresolved gaps and disqualifying conditions;
10. downstream handoff packets;
11. verification record;
12. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a health, vascular,
diffusion, causal, or scientific conclusion.

### 11. Verify and stop

Verify:

- source access date, archive identity, and hash are recorded;
- approximate and exact manifest counts remain distinct;
- participants, scans, modality files, and demographic rows are not
  conflated;
- source health labels are not expanded into clinical claims;
- sites, vendors, field strengths, and protocols remain distinct;
- participant-level modality and metadata completeness is verified;
- original IXI and third-party derivatives remain distinct;
- no BIDS or sidecar state is invented;
- CC BY-SA 3.0 duties remain visible;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no download, extraction, selection, write, conversion, preprocessing, or
  analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- archive, site, modality, demographic, participant, and product candidates;
- treatment of source health labels, site, scanner, field strength, protocol,
  modality missingness, demographics, and generalization;
- every access, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and archive constraints. It does not declare
participants disease-free, choose a matched subset, or harmonize scanner
effects for the user.

Use this order:

1. current official IXI Dataset page and its exact archive and parameter links;
2. exact official archive manifests, local hashes, and demographic spreadsheet;
3. institutional or primary IXI documentation for acquisition context;
4. user-supplied local source files;
5. third-party mirrors only for comparison, never as source authority;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated archive fact**
- **Selected-file fact**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never replace an exact source manifest with the headline phrase "nearly 600."

Edge cases:

- **Only “IXI” is supplied**: ask for the one scientific requirement.
- **Six hundred is treated as exact**: require a file-level manifest and
  participant deduplication.
- **All participants are called verified healthy controls**: inspect the source
  screening evidence and preserve its limitations.
- **Every participant is assumed to have all five modalities**: inspect exact
  participant-level pairing.
- **All scans are called 3 T Philips**: preserve the three site, vendor, and
  field-strength states.
- **IXI Tiny is proposed as original IXI**: separate the derivative's
  preprocessing, labels, participants, and license.
- **Task or resting fMRI is required**: return **Not suitable for the stated
  requirement** based on the verified modality list.
- **MRA is called a vessel ground truth**: distinguish angiographic images
  from validated segmentations or clinical labels.
- **BIDS sidecars are assumed**: inspect exact source metadata and route any
  curation separately.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish health status, absence of pathology, population
representativeness, scanner comparability, vessel ground truth, diffusion
validity, longitudinal change, causal identification, preprocessing
superiority, power, analysis validity, generalizability, or fitness for
clinical use. It cannot guarantee that an unversioned archive, link, file,
license, or endpoint remains current after the recorded retrieval date.

## IXI facts that control the review

Use these as dated orientation and recheck them at invocation:

- The official IXI page describes nearly 600 MR images from normal, healthy
  participants. "Nearly 600" is an approximate source description, not a
  participant-level complete-case count.
- Source language calling participants normal or healthy does not by itself
  establish the screening procedure, absence of incidental pathology, current
  diagnostic status, or population representativeness.
- Data came from three London hospitals with different scanners:
  Hammersmith Hospital used a Philips 3 T system, Guy's Hospital used a Philips
  1.5 T system, and the Institute of Psychiatry used a GE 1.5 T system.
- The official page distributes separate T1, T2, PD, MRA, and DTI archives
  plus a demographic spreadsheet. A modality-level archive does not establish
  that every participant has every modality.
- The official page does not assign a semantic release version. Pin exact
  URLs, retrieval time, archive filenames, byte sizes, hashes, and local
  manifest before design use.
- Original files are distributed as source imaging archives, commonly NIfTI
  products. They are not established as a complete modern BIDS dataset.
- Acquisition parameters differ by hospital, scanner, field strength, and
  modality. Verify the exact site-specific parameter page and selected file.
- The official page makes IXI available under Creative Commons Attribution
  ShareAlike 3.0 and requests acknowledgement of the IXI source.
- IXI Tiny, federated-learning versions, normalized brain maps, segmentations,
  and other mirrors are third-party derivatives with their own participant
  counts, processing, labels, and provenance. They are not the original IXI
  release.
- No task fMRI or resting-state fMRI is established by the official IXI
  modality list.
- Do not infer longitudinal follow-up from filenames or multiple modalities.

Do not assume complete multimodal pairing, a single scanner, uniform protocol,
verified clinical controls, or a ready-made segmentation ground truth.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about cohort
  screening, acquisition, modality validity, scanner effects, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when site, scanner, population, or modality
  structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact
  participant unit, site structure, estimand, analysis, inference family, and
  loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after exact source archives and
  metadata are legitimately available.
- Route download, archive extraction, curation, metadata authoring, conversion,
  preprocessing, QC, vessel or diffusion analysis, participant selection,
  modeling, and interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *IXI Dataset* [Data set]. (n.d.). https://brain-development.org/ixi-dataset/
