---
name: seed-vig-skill
description: >-
  Evaluates from public metadata whether one exact SEED-VIG participant, driving
  experiment, EEG or forehead-EOG feature product, temporal window, PERCLOS
  label, access state, or proposed subset can support one user-supplied design
  and produces a selection-bound Dataset Suitability and Access Specification.
  Use when the request, or a part coordinator, hands over an explicitly matching
  SEED-VIG question. It preserves the 23-participant, approximately two-hour
  driving, acquisition-versus-shared-channel, 885-window, continuous-PERCLOS,
  dependence, product-provenance, and academic-license boundaries after two
  approval gates. It does not receive licensed participant data or features,
  request access, sign or upload terms, download, inspect, redistribute, select
  windows, preprocess, classify vigilance, analyze, search broadly, make
  scientific or clinical claims, or save without separate approval. Triggers:
  can SEED-VIG support my study, SEED-VIG vigilance EEG selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: eeg
  population: general
  dependencies: ""
  requires: SEED license application
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# SEED-VIG Dataset Suitability

Evaluate one exact SEED-VIG design fit without turning a licensed vigilance-estimation resource into an automatic modeling pipeline.

## Purpose

`seed-vig-skill` is the conditional Part 3 owner for one bounded prospective suitability and access-planning question about the SJTU SEED-VIG dataset.

It pins the participant, driving experiment, feature window, EEG, forehead-EOG, PERCLOS, acquisition, derived-product, access, and license grain; compares only applicable metadata-level routes; and produces one user-selected Dataset Suitability and Access Specification.

It does not own vigilance theory, scientific interpretation, study-design selection, signal processing, feature engineering, regression, classification, or analysis. It never receives licensed participant data, authenticates, applies, downloads, opens matrices, selects windows, preprocesses, trains, evaluates, or redistributes.

Activate only when:

- The user invokes the exact trigger `seed-vig-skill`; or
- a verified Active capability hands off one explicit SEED-VIG suitability or access-planning question.

Do not activate from `SEED`, `vigilance`, `fatigue`, `drowsy driving`, `EEG classification`, `PERCLOS`, `download SEED`, or `analyze driving`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the temporal, participant, evaluation, generalization, comparison, or proxy-validation structure must be designed. Offer [paper-search](../../skills/paper-search/SKILL.md) only for a separately approved bounded search about vigilance, fatigue, PERCLOS, EEG, EOG, or prior SEED-VIG evidence.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, construct, estimand, and intended inference |
| Observation grain | Participant, experiment, feature window, aggregate trajectory, or unresolved choice |
| Generalization target | Within participant, across time, across participants, or another explicit target |
| Product need | EEG features, forehead-EEG features, EOG features, PERCLOS, or public metadata only |
| Proxy boundary | Continuous PERCLOS use and the inference it is intended to support |
| Access boundary | Public metadata only or independently verified academic authorization |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should SEED-VIG be evaluated against?

Then stop.

## Steps

### 1. Build the SEED-VIG Fit Brief

Restate:

- The user-supplied question and intended inference;
- the observation and generalization grain;
- required feature product and PERCLOS use;
- access and stopping boundary;
- unresolved terms that could change suitability.

Separate supplied facts from interpretation. Do not formulate a hypothesis for
The user.

### 2. Gate 1: approve the public inspection boundary

Present:

1. exact question and intended inference;
2. proposed public sources;
3. planned metadata fields;
4. selected product, proxy, and generalization route, or evidence-supported
   alternatives for any material choice that remains open;
5. facts that cannot be inspected under the metadata-only boundary;
6. conflicts or missing definitions that must remain visible.

Gate 1 authorizes only the displayed public-source and metadata inspection. It
does not authorize access requests, terms acceptance, downloads, participant
data, feature inspection, simulator retrieval, saving, or analysis.

If the source or target changes materially, reopen Gate 1.

### 3. Pin exact source and governance states

Record:

- official-page access date;
- license document state and SHA-256 when locally verified;
- paper DOI and publication state;
- selected product description and its source;
- access status and unresolved rights;
- any documentation conflict.

Do not call an undated page a release.

### 4. Build the Evidence and Governance Card

Show:

| Field | Verified value | Source and date | Status | Consequence |
|---|---|---|---|---|
| Participant and experiment inventory | | | | |
| Driving context and timing | | | | |
| PERCLOS definition and proxy role | | | | |
| Acquisition channels and rate | | | | |
| Shared feature products | | | | |
| Windowing, smoothing, and sample grain | | | | |
| License and redistribution | | | | |

Keep acquisition, paper-processing, and shared-product facts in separate rows.

### 5. Build the Grain, Channel, and Product Map

Map each requested variable or product to:

- participant, experiment, temporal-window, or aggregate grain;
- acquisition or derived-product status;
- documented shape and channel count;
- proxy or signal source;
- temporal dependence and nesting;
- public, licensed, supplied, absent, or unverified availability;
- filtering, downsampling, windowing, smoothing, or decomposition already
  embedded in the product.

Never infer channel identity, alignment, or independence from array shape.

### 6. Build the Applicability Matrix

Assess the exact selected route in this matrix. Include alternatives only
when needed to resolve a material open choice. The table shows example rows.

| Route | Supports | Does not support | Required assumptions | Leakage controls | Access state |
|---|---|---|---|---|---|
| Public metadata only | | | | | |
| 17-channel EEG features | | | | | |
| Forehead EEG features | | | | | |
| EOG features | | | | | |
| Multimodal feature route | | | | | |

Omit unused rows. If the selected route cannot answer the approved question,
report the blocker. Keep ranking and selection with the user.

### 7. Build the Threat and Governance Register

At minimum test:

- participant and temporal-window leakage;
- adjacent-window dependence and smoothing;
- within-experiment versus cross-participant generalization;
- PERCLOS proxy validity and circularity when eye-derived features are used;
- driving duration, time-of-day, post-lunch, and unmeasured-state confounding;
- acquisition-versus-shared-channel mismatch;
- unexplained channel index 6 in the public product note;
- feature-product processing and loss of raw-signal flexibility;
- missingness and alignment across EEG, EOG, and PERCLOS;
- small participant count and population limits;
- license, private-link, and redistribution limits;
- historical five-part evaluation being mistaken for current validation.

For each threat, state evidence, consequence, possible control, residual risk,
and the decision the user retains.

### 8. Assess the selected or eligible routes

Apply the criteria below to the selected route. Compare eligible alternatives
on the same criteria only if a material choice remains open and more than
one route is credible. Report a blocker on the selected route without
substituting another, and leave any ranking to the user.

- exact scientific fit;
- supported generalization level;
- product and processing provenance;
- PERCLOS proxy validity and construct gap;
- temporal dependence and leakage control;
- access and rights burden;
- unresolved evidence.

If no route is suitable, say so and show the missing condition that would
change the result.

### 9. Gate 2: select the specification

Present the complete Evidence and Governance Card, Grain, Channel, and Product
Map, Applicability Matrix, and Threat Register. Include the comparison only when a material choice required one. The user confirms
recorded selections and resolves the remaining items below.

- feature product and product state;
- participant, experiment, and temporal-window grain;
- PERCLOS interpretation and permissible claim;
- generalization and holdout structure;
- inclusion and exclusion logic;
- unresolved limitations to carry forward;
- metadata-only stopping or a separate handoff.

Gate 2 authorizes only the selected Dataset Suitability and Access
Specification. It does not authorize access, downloads, data transfer,
preprocessing, modeling, analysis, safety or clinical claims, saving, or a
pipeline.

### 10. Produce the Dataset Suitability and Access Specification

Write only the selected route:

1. question and intended inference;
2. pinned source and license states;
3. product and observation grain;
4. participant, experiment, channel, feature, and temporal boundaries;
5. PERCLOS proxy interpretation;
6. generalization and leakage controls;
7. access and rights limits;
8. inherited processing and provenance;
9. assumptions, conflicts, unknowns, and exclusions;
10. threats and residual risks;
11. separately approved next handoff or explicit stop.

Label every design choice as user-selected.

### 11. Verify and stop

Verify:

- one exact trigger and one canonical owner;
- public-metadata-only operation;
- 23 participants, approximately two hours, and 885 feature windows are not
  conflated as the same grain;
- the 18-channel acquisition description is separated from the 17-channel
  shared EEG tensor;
- PERCLOS remains a continuous eye-closure proxy, not direct ground truth;
- no unsupported KSS or binary label was introduced;
- within-experiment precedent is not called cross-participant evidence;
- no licensed data, feature content, simulator material, or private link
  entered the workflow;
- both gates bound their authorization;
- no scientific choice or downstream action was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop.

Saving or handing off requires separate explicit approval.

## Boundaries

The current SEED family license explicitly covers SEED-VIG. It permits academic research use after a signed application is reviewed and prohibits commercial use and redistribution, apart from small portions used solely to clarify an academic publication or presentation. It also prohibits sharing an issued download link.

For this workflow:

- accept only public documentation, papers, aggregate counts, schemas, and user-authored requirement summaries;
- do not ask the user to attach, paste, quote, or expose licensed participant-level signals, features, labels, file contents, credentials, signed forms, or private download links;
- do not treat public page visibility, a local copy, or academic affiliation as
  proof that the proposed use is authorized;
- do not redistribute data, features, labels, simulator materials, or download links;
- stop if answering requires inspecting licensed content.

This is a conservative handling rule for the ASTORIA adaptation. It does not claim that the license contains an AI-specific prohibition.

The user owns the research question, hypothesis, estimand, vigilance construct,
PERCLOS interpretation, participant and temporal grain, generalization target,
product choice, split logic, confirmatory status, access decision, final
suitability judgment, and every downstream action.

This skill exposes evidence, assumptions, dependencies, proxy limitations, and
threats. It does not choose a model, diagnose fatigue or impairment, treat
PERCLOS as direct ground truth, rank scientific approaches, or convert
prediction performance into a psychological, safety, or clinical claim.

Use this order:

1. current official SEED-VIG page and current official SEED family license;
2. primary SEED-VIG methods paper;
3. exact public README or package documentation when independently supplied
   and lawful to inspect;
4. secondary papers for dated analytical precedent only;
5. repository candidates as design evidence, never as data authority.

For every source, record the title, responsible organization or authors,
version or date, URL or exact local source state, access date, license status,
and which field it supports.

Preserve conflicts. Do not silently reconcile:

- acquisition channels and official shared-product channels;
- paper methods, official page descriptions, README, and package inventory;
- PERCLOS as a measured eye-closure proxy and vigilance as a latent construct;
- experiment, window, fold, and participant grain;
- historical within-experiment evaluation and cross-participant evidence;
- acquisition data, official feature products, and third-party derivatives.

Label a missing field `unknown`, `unverified`, `not documented`, or `not
applicable`. Never fill it from a repository script or memory.

Edge cases:

- **SEED without version.** Stop and distinguish SEED, SEED-IV, SEED-VIG,
  SEED-V, SEED-GER, and SEED-FRA.
- **Data or features pasted into chat.** Do not inspect them. Ask the user to
  remove the content from scope and continue with public metadata only.
- **Public download link.** Treat visibility as neither permission nor
  redistribution authority.
- **Raw EEG requested.** Mark raw EEG availability unverified. The current
  official page documents feature products.
- **18 versus 17 EEG channels.** Preserve acquisition and shared-product
  statements separately. Do not infer the missing or excluded channel.
- **Channel index 6.** Mark it undocumented in the official ordering note.
- **KSS or binary label requested.** Mark it unsupported by the official page
  unless a separately verified source is approved.
- **Random window split proposed.** Expose the leakage target and require the user
  to choose the actual generalization level.
- **Eye-derived predictor with PERCLOS outcome.** Flag potential measurement
  circularity and require an explicit construct decision.
- **Clinical or driving-safety inference.** Refuse the interpretation and
  return to the bounded proxy-estimation construct.
- **No suitable route.** Produce a blocked specification rather than relaxing
  requirements.

This skill cannot verify licensed file contents, current applicant eligibility,
private link state, product completeness, missingness, channel identity,
feature alignment, synchronization, or analysis readiness. It cannot determine
that PERCLOS is a sufficient measure of vigilance, fatigue, impairment, or
driving safety. It cannot grant data permission.
- The SEED administrators may change the license terms; reverify them before any access action.

## Design choices and verification

Make the PERCLOS proxy interpretation explicit when deciding whether a
SEED-VIG feature product fits the question. If a choice remains, compare defensible product, proxy, and generalization
routes within the public evidence and license. Record provenance, assumptions, conflicts and unknowns in the
Evidence and Governance Card, Applicability Matrix and Threat Register.
If a single defensible route survives, present it as fixed and explain why.

Prepare and verify only the Dataset Suitability and Access Specification
selected at Gate 2. The checkpoint ends before access, data inspection,
preprocessing, analysis or saving.

> [!info] References
> Read `./references/seed_vig_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) for an approved temporal, participant,
  proxy-validation, multimodal, or evaluation-design comparison.
- Offer [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded evidence search.
- Route preprocessing or analysis only after the user has selected the design and
  an appropriate Part 4 owner exists.
- Return any claim or manuscript wording to its canonical analysis or writing
  owner.

Never chain a handoff automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- BCMI Laboratory, Shanghai Jiao Tong University. (n.d.). *SEED-VIG* [Data set]. https://bcmi.sjtu.edu.cn/home/seed/seed-vig.html
- Zheng & Lu. (n.d.). A multimodal approach to estimating vigilance using EEG and forehead EOG. *Journal of Neural Engineering*. https://doi.org/10.1088/1741-2552/aa5a98
