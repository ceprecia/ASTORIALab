---
name: tcp-skill
description: >-
  Evaluates from public metadata whether one exact Transdiagnostic Connectome
  Project release, repository snapshot, participant grain, diagnostic or
  dimensional field, site, MRI run, behavioral measure, raw product, processed
  derivative, access state, or proposed subset can support one user-supplied
  design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching TCP question. It preserves the 241-directory,
  148-versus-93 paper, 149-versus-92 manifest, 245-row table, two-site, T1w,
  T2w, rest, Stroop, Emotional Faces, missingness, source-versus-derivative,
  open-release, and consent boundaries after two approval gates. Triggers: can
  TCP support my study, TCP dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: clinical
  dependencies: ""
  requires: OpenNeuro access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Transdiagnostic Connectome Project Dataset Suitability

Evaluate one exact TCP source and inference fit without converting an open
psychiatric-neuroimaging release into an automatic connectivity pipeline.

## Purpose

It does not receive participant data, download, inspect, relabel diagnosis, select participants, preprocess, harmonize, connect, predict, analyze, search broadly, make scientific or clinical claims, or save without separate approval.

`tcp-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access-planning question about the Transdiagnostic Connectome
Project.

It pins the repository snapshot, participant table, subject-directory,
clinical or dimensional field, site, anatomical or functional run, behavioral
measure, raw or processed product, access, and consent grain; compares only
credible metadata-level routes; and produces one user-selected Dataset
Suitability and Access Specification.

It does not own diagnosis, phenotype construction, method selection,
connectivity estimation, preprocessing, prediction, harmonization, or
analysis. It never downloads participant data, opens phenotypes or images,
selects people, relabels groups, fits models, or generates clinical claims.

Activate only when:

- The user invokes the exact trigger `tcp-skill`; or
- a verified Active capability hands off one explicit Transdiagnostic
  Connectome Project suitability or access-planning question.

Do not activate from `TCP`, `transdiagnostic`, `connectome`, `psychiatric
fMRI`, `Stroop`, `emotional faces`, `download TCP`, or `analyze TCP`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the site, group, dimension, task, run,
missingness, comparison, or evaluation structure must be designed. Offer
[paper-search](../../skills/paper-search/SKILL.md) only for a separately approved bounded search about a
construct, measure, task, or prior TCP result.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, estimand, and intended inference |
| Population and construct | Diagnostic, dimensional, general-population, or explicit comparison rule |
| Unit | Participant, site, run, task condition, scale, item, raw image, timeseries, or derivative |
| Product need | T1w, T2w, rest, Stroop, Emotional Faces, field map, behavioral measure, raw BIDS, or processed derivative |
| Generalization target | Within release, across site, across diagnosis, new population, or another explicit target |
| Source state | OpenNeuro snapshot, NDA Study, paper state, or unresolved comparison |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should the Transdiagnostic Connectome Project be evaluated against?

Then stop.

## Steps

### 1. Build the TCP Fit Brief

Restate the question, construct, participant and site grain, required run or
measure, source and product state, generalization target, access boundary, and
unresolved definitions. Separate evidence from interpretation.

### 2. Gate 1: approve the public inspection boundary

Present:

1. exact question and inference;
2. versioned public sources;
3. cohort, field, run, product, and consent metadata to inspect;
4. the selected route or credible alternatives for a material choice that
   remains open;
5. known count, run, and product conflicts;
6. participant-level facts that remain out of scope.

Gate 1 authorizes only the displayed public metadata inspection. It does not
authorize downloads, participant records, NDA access, selection, relabeling,
preprocessing, harmonization, analysis, or saving.

Reopen Gate 1 after a material source or construct change.

### 3. Pin exact source and access states

Record the OpenNeuro version, DOI, commit, license, tree and participant-table
grains; NDA Study ID and DOI; peer-reviewed paper DOI; raw or derivative
product; access state; and unresolved conflict.

### 4. Build the Source and Consent Card

| Field | Verified value | Source state | Status | Consequence |
|---|---|---|---|---|
| Cohort and group inventory | | | | |
| Site and scanner | | | | |
| Functional-run inventory | | | | |
| Behavioral and clinical measures | | | | |
| Raw and processed products | | | | |
| Consent and access state | | | | |

### 5. Build the Grain and Completeness Map

Map each requested element to participant, site, run, condition, scale, item,
raw file, timeseries, or derivative grain; manifest count; missingness; group
label source; raw or processed state; and access route.

Never infer complete cases from the maximum participant count.

### 6. Build the Applicability Matrix

Assess the exact selected route in this matrix. Include alternatives only
when needed to resolve a material open choice. The table shows example rows.

| Route | Supports | Does not support | Assumptions | Missingness controls | Access state |
|---|---|---|---|---|---|
| Public metadata only | | | | | |
| Raw OpenNeuro route | | | | | |
| OpenNeuro parcellated route | | | | | |
| NDA derivative route | | | | | |
| Site or task subset | | | | | |

Omit unused rows. If the selected route cannot answer the approved question,
report the blocker. Keep ranking and selection with the user.

### 7. Build the Threat and Governance Register

At minimum assess:

- paper, participant-table, and subject-directory count conflicts;
- 148-versus-93 and 149-versus-92 group-label conflict;
- four-versus-six rest-run documentation conflict;
- site, scanner, motion, and completion differences;
- diagnosis, group label, dimension, and measure conflation;
- measure-specific missingness and complete-case selection;
- run and task availability;
- raw, parcellated, and HCP-derivative conflation;
- unsupported diffusion claims;
- open-hosting consent and nonparticipating records;
- psychiatric-population stigma, reidentification, and clinical overreach;
- leakage across participant, run, condition, site, and preprocessing state.

For each threat, show evidence, consequence, possible control, residual risk,
and the user's retained decision.

### 8. Assess the selected or eligible routes

Assess the selected route for scientific fit, construct support, cohort grain,
site and run coverage, missingness, raw-versus-processed provenance, access,
consent, generalization, and unresolved evidence. Compare eligible alternatives on these criteria only
if a material choice remains open and more than one route is credible. Report a blocker
on the selected route without substituting another. Do not recommend or
select a route.

### 9. Gate 2: select the specification

Present all cards, maps, matrices, and threats. Include a comparison only
when a material choice required one. The user confirms the recorded choices
and decides any open items for the source snapshot, population and construct, site handling,
participant and run grain, raw or processed product, missingness rule, generalization boundary,
consent caveats, and next stop or handoff.

Gate 2 authorizes only the selected Dataset Suitability and Access
Specification. It does not authorize data access, download, participant
selection, diagnosis relabeling, preprocessing, harmonization, connectivity,
prediction, analysis, claims, saving, or a pipeline.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. question, estimand, and intended inference;
2. pinned OpenNeuro, NDA, and paper states;
3. cohort, group, site, participant, run, measure, and product grains;
4. exact count conflicts and selected handling;
5. construct and label interpretation;
6. missingness, site, run, leakage, and generalization controls;
7. raw or processed provenance;
8. access, consent, privacy, and citation duties;
9. assumptions, unknowns, exclusions, and residual risks;
10. user-selected choices and any rejected alternatives that were evaluated;
11. separately approved handoff or explicit stop.

### 11. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- 241 paper participants, 241 directories, and 245 table rows remain distinct;
- 148-versus-93 and 149-versus-92 remain visible;
- four-versus-six resting-run statements remain unresolved by manifest;
- no unsupported diffusion product is introduced;
- raw and processed products remain distinct;
- group labels are not treated as clinical truth;
- no participant data entered the workflow;
- both gates bound their authorization;
- no scientific or downstream choice was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The peer-reviewed release reports raw BIDS data on OpenNeuro under CC0 and
processed derivatives on the NIMH Data Archive. It also states that five
participants did not permit sharing through openly hosted repositories.
Current access states, repository terms, consent constraints, and
institutional duties still control each action.

This Part 3 skill:

- accepts only public documentation, aggregate inventory, schemas, and
  user-authored requirement summaries;
- does not ask the user to paste, attach, or upload participant-level phenotype,
  imaging, event, quality, or identifier records;
- does not download public files or treat CC0 as a waiver of ethical,
  reidentification, consent, or institutional duties;
- does not submit an NDA request, authenticate, or accept terms;
- stops if the answer requires participant-level inspection.

The user owns the research question, hypothesis, estimand, diagnostic or
dimensional construct, group or continuous comparison, site treatment, run
selection, phenotype definition, participant exclusions, missingness rule,
generalization target, confirmatory status, access decision, final suitability
judgment, and every downstream action.

This skill exposes evidence and threats. It does not decide that a dimensional
model is scientifically preferable, collapse heterogeneous diagnoses, treat a
repository group label as a clinical truth, or select a convenient processed
product.

Use this order:

1. exact versioned OpenNeuro snapshot and its manifests;
2. immutable NDA Study release and current NDA access terms;
3. peer-reviewed TCP Data Descriptor and supplements;
4. exact user-supplied, authorized local manifest;
5. secondary papers for paper-specific subsets and analysis only;
6. repository candidate material as design evidence, never data authority.

For each fact, record source, version or date, URL or commit, grain, access
state, and whether it is a paper count, metadata-table row, subject directory,
run, or complete-case subset.

Preserve conflicts between:

- the paper's 148 diagnosis and 93 comparison participants;
- OpenNeuro `participants.tsv` and subject-directory inventory;
- four versus six resting-state-run statements;
- consented study participants and openly hosted participants;
- raw BIDS, parcellated timeseries, and HCP derivatives;
- intended acquisition and per-run completion.

Never infer a clinical status from `Patient` or `GenPop` alone.

Edge cases:

- **TCP is ambiguous:** confirm Transdiagnostic Connectome Project.
- **Six rest runs are assumed:** preserve the README conflict and inspect the
  exact snapshot tree.
- **dMRI is requested:** mark it unsupported by the current authoritative
  product state.
- **245 rows are called 245 released subjects:** separate participant-table
  rows from 241 subject directories.
- **`Patient` is called a diagnosis:** require the exact clinical field and
  construct rule.
- **Every measure is assumed complete:** build a field-specific missingness
  map.
- **NDA and OpenNeuro products are merged:** restore access and processing
  provenance.
- **Open data is called unrestricted clinical evidence:** restore consent,
  ethics, and inference boundaries.
- **No suitable route:** return a blocked specification.

This skill cannot verify participant-level phenotypes, diagnosis validity,
measure scoring, missingness mechanisms, image quality, site harmonization,
processed-product validity, access eligibility, or clinical utility. It
cannot grant permission or establish population generalizability.

## TCP facts that control the review

Use these only with their pinned source states.

### Cohort and repository grain

- The peer-reviewed Data Descriptor and NDA Study describe 241 people aged 18
  to 70, comprising 148 participants meeting criteria for a broad range of
  psychiatric illnesses and 93 healthy comparison participants.
- Data were collected at Yale University and McLean Hospital between November
  2019 and March 2023.
- OpenNeuro snapshot `1.1.3`, DOI
  `10.18112/openneuro.ds005237.v1.1.3`, is pinned to repository commit
  `2e273d8466162208bbccd8591337e55b7a8b5721`.
- That snapshot contains 241 subject directories, but its
  `participants.tsv` has 245 rows. At the directory grain, current labels sum
  to 149 `Patient` and 92 `GenPop`, not the paper's 148 and 93.
- Four `GenPop` rows lack subject directories. The paper separately states
  that five people did not permit openly hosted sharing. Do not silently
  equate those facts or repair the mismatch.

The exact versioned manifest, not a headline count, controls a proposed
subset.

### Imaging, task, and product grain

- Both sites used a harmonized protocol on Siemens Magnetom 3 T Prisma
  scanners with 64-channel head coils.
- The paper documents T1w and T2w anatomy, four resting-state runs, two Stroop
  runs with opposite phase encoding, one Emotional Faces run, and field maps.
- The current dataset description also says four resting-state and three
  task-fMRI runs. The README headline says six resting-state runs, while its
  acquisition section says four. Preserve the conflict and inspect the
  versioned run manifest.
- The released task paradigms are Stroop and Emotional Faces. A README measure
  label such as `Hammer Task` does not establish a third fMRI task.
- Completion varies by run. Paper counts include 241 for each first rest run,
  237 and 235 for the second pair, 226 and 224 for Stroop, and 226 for
  Emotional Faces.
- The candidate's diffusion-MRI claim is not supported by the peer-reviewed
  acquisition or the current OpenNeuro product description. Mark dMRI absent
  unless an exact later product proves otherwise.
- OpenNeuro supplies raw, anonymized BIDS and selected parcellated products.
  NDA supplies HCP-pipeline derivatives. These are different processing and
  access states.

### Construct and consent boundaries

- Participants completed a structured DSM-5 interview and more than 50
  psychological and cognitive assessments, but availability and missingness
  are measure-specific.
- Diagnosis, broad `Patient` versus `GenPop`, symptom dimensions, task
  behavior, and functional connectivity are different constructs.
- A transdiagnostic sampling frame does not itself justify a dimensional
  estimand, pooled diagnosis group, or clinical prediction claim.
- Site, diagnosis, medication, motion, measure completion, and open-sharing
  consent can jointly affect an eligible subset.

## Design choices and verification

Pin the source snapshot and consent boundary before comparing TCP cohorts,
phenotypes, runs or products. Show the Source and Consent Card with the
Grain Map so discrepancies in people, directories and rows stay visible.
Use the Applicability Matrix and Threat Register to show which routes answer
the question and what conflicts or unknowns remain. Compare only compatible routes when the requested decision remains open. Present one route on its own when it is the only defensible choice.

After Gate 2, prepare and verify only the selected Dataset Suitability and
Access Specification. Stop before data access, selection, preprocessing or
analysis.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) for an approved site, construct, run,
  missingness, comparison, or evaluation-design question.
- Offer [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded evidence search.
- Route BIDS, preprocessing, harmonization, connectivity, or analysis only
  after the user selects the design and an appropriate owner exists.

Never chain automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Chopra et al. (2025). The Transdiagnostic Connectome Project dataset. *Scientific Data*. https://doi.org/10.1038/s41597-025-04895-z
- *ds005237* (Version 1.1.3) [Data set]. (n.d.). OpenNeuro. https://doi.org/10.18112/openneuro.ds005237.v1.1.3
- *NDA Study 2932* [Data set]. (n.d.). NDA. https://doi.org/10.15154/dtpj-vv60
