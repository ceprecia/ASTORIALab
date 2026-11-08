---
name: seed-iv-skill
description: >-
  Evaluates from public metadata whether one exact SEED-IV participant, session,
  film-trial, emotion condition, EEG product, eye-movement product, feature
  state, label state, access state, or proposed subset can support one
  user-supplied design and produces a selection-bound Dataset Suitability and
  Access Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching SEED-IV question. It preserves the 15-participant,
  three-session, 24-trial-per-session, four-emotion, multimodal,
  repeated-measures, film-rights, product-provenance, and academic-license
  boundaries after two approval gates. It does not receive licensed participant
  data or features, request access, sign or upload terms, download, inspect,
  redistribute, select trials, preprocess, classify emotion, analyze, search
  broadly, make scientific or clinical claims, or save without separate
  approval. Triggers: can SEED-IV support my study, SEED-IV emotion EEG
  selection.
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

# SEED-IV Dataset Suitability

Evaluate one exact SEED-IV design fit without converting a licensed
emotion-elicitation resource into an automatic classification pipeline.

## Purpose

`seed-iv-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access-planning question about the SJTU Emotion EEG Dataset IV
or SEED-IV.

It pins the participant, session, trial, film, emotion, EEG, eye-movement,
feature, label, timing, access, and license grain; compares only applicable
metadata-level routes; and produces one user-selected Dataset Suitability and
Access Specification.

It does not own emotion theory, scientific interpretation, experimental-design
selection, feature engineering, classification, or analysis. It never receives
licensed participant data, authenticates, applies, downloads, opens feature
files, selects observations, preprocesses, trains, evaluates, or redistributes.

Activate only when:

- The user invokes the exact trigger `seed-iv-skill`; or
- a verified Active capability hands off one explicit SEED-IV suitability or
  access-planning question.

Do not activate from `SEED`, `emotion EEG`, `affective computing`, `EEG
classification`, `eye tracking`, `download SEED`, or `analyze emotion`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the repeated-measures, elicitation,
generalization, comparison, or evaluation structure must be designed. Offer
[paper-search](../../skills/paper-search/SKILL.md) only for a separately approved bounded search about emotion
elicitation, EEG features, eye-movement measures, or prior SEED-IV evidence.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, construct, estimand, and intended inference |
| Observation grain | Participant, session, trial, time window, feature matrix, or unresolved choice |
| Generalization target | Within participant, across sessions, across participants, across films, or another explicit target |
| Product need | Raw EEG, EEG features, raw eye movements, eye features, labels, or public metadata only |
| Emotion boundary | Happy, sad, fear, neutral, contrast, dimensional interpretation, or unresolved |
| Access boundary | Public metadata only or independently verified academic authorization |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should SEED-IV be evaluated against?

Then stop.

## Steps

### 1. Build the SEED-IV Fit Brief

Restate:

- The user-supplied question and intended inference;
- the observation and generalization grain;
- required product, modality, label, and emotion boundary;
- access and stopping boundary;
- unresolved terms that could change suitability.

Separate supplied facts from interpretation. Do not formulate a hypothesis for
The user.

### 2. Gate 1: approve the public inspection boundary

Present:

1. exact question and intended inference;
2. proposed public sources;
3. planned metadata fields;
4. selected product and generalization route, or evidence-supported
   alternatives for any material choice that remains open;
5. facts that cannot be inspected under the metadata-only boundary;
6. conflicts or missing definitions that must remain visible.

Gate 1 authorizes only the displayed public-source and metadata inspection. It
does not authorize access requests, terms acceptance, downloads, participant
data, feature inspection, stimulus retrieval, saving, or analysis.

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
| Participant and session inventory | | | | |
| Trial and film inventory | | | | |
| Emotion and label meaning | | | | |
| EEG acquisition | | | | |
| Eye-movement acquisition | | | | |
| Shared products and processing | | | | |
| License and film rights | | | | |

Mark arithmetic, paper-specific values, and current page statements separately.

### 5. Build the Grain and Product Map

Map each requested variable or product to:

- participant, session, trial, film, or temporal-window grain;
- acquisition or derived-product status;
- known shape or inventory;
- label source;
- repeat and nesting structure;
- public, licensed, supplied, absent, or unverified availability;
- conversion or preprocessing already embedded in the shared product.

Never infer one-to-one alignment from matching row counts alone.

### 6. Build the Applicability Matrix

Assess the exact selected route in this matrix. Include alternatives only
when needed to resolve a material open choice. The table shows example rows.

| Route | Supports | Does not support | Required assumptions | Leakage controls | Access state |
|---|---|---|---|---|---|
| Public metadata only | | | | | |
| Raw EEG route | | | | | |
| EEG feature route | | | | | |
| Eye-movement route | | | | | |
| Multimodal route | | | | | |

Omit unused rows. If the selected route cannot answer the approved question,
report the blocker. Keep ranking and selection with the user.

### 7. Build the Threat and Governance Register

At minimum test:

- participant, session, film, and temporal-window leakage;
- session-day and film-set confounding;
- intended-condition versus self-assessed-label mismatch;
- missing observations or product-specific exclusions;
- preprocessing and smoothing inherited by feature products;
- modality-alignment and clock assumptions;
- trial, participant, and film nonindependence;
- small participant count and target-population limits;
- license, private-link, film-rights, and redistribution limits;
- historical evaluation choices being mistaken for current evidence.

For each threat, state evidence, consequence, possible control, residual risk,
and the decision the user retains.

### 8. Assess the selected or eligible routes

Apply the criteria below to the selected route. Compare eligible alternatives
on the same criteria only if a material choice remains open and more than
one route is credible. Report a blocker on the selected route without
substituting another, and leave any ranking to the user.

- exact scientific fit;
- supported generalization level;
- product and preprocessing provenance;
- label validity and construct gap;
- dependence and leakage control;
- access and rights burden;
- unresolved evidence.

If no route is suitable, say so and show the missing condition that would
change the result.

### 9. Gate 2: select the specification

Present the complete Evidence and Governance Card, Grain and Product Map,
Applicability Matrix, and Threat Register. Include the comparison only when a material choice required one. The user confirms
recorded selections and resolves the remaining items below.

- product and product state;
- participant, session, trial, and window grain;
- emotion and label interpretation;
- generalization and holdout structure;
- inclusion and exclusion logic;
- unresolved limitations to carry forward;
- metadata-only stopping or a separate handoff.

Gate 2 authorizes only the selected Dataset Suitability and Access
Specification. It does not authorize access, downloads, data transfer,
preprocessing, modeling, analysis, claims, saving, or a pipeline.

### 10. Produce the Dataset Suitability and Access Specification

Write only the selected route:

1. question and intended inference;
2. pinned source and license states;
3. product and observation grain;
4. cohort, session, trial, film, and emotion boundaries;
5. label and construct interpretation;
6. generalization and leakage controls;
7. access and rights limits;
8. known preprocessing and provenance;
9. assumptions, conflicts, unknowns, and exclusions;
10. threats and residual risks;
11. separately approved next handoff or explicit stop.

Label every design choice as user-selected.

### 11. Verify and stop

Verify:

- one exact trigger and one canonical owner;
- public-metadata-only operation;
- 15 participants, three sessions, 24 trials per session, four emotions, and
  1,080 maximum observations are not conflated;
- raw acquisition is separated from official feature processing;
- participant, session, film, trial, and window dependence are visible;
- elicitation conditions are not treated as clinical or infallible truth;
- no licensed data, feature content, film, or private link entered the
  workflow;
- both gates bound their authorization;
- no scientific choice or downstream action was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop.

Saving or handing off requires separate explicit approval.

## Boundaries

The current SEED family license explicitly covers SEED-IV. It permits academic
research use after a signed application is reviewed and prohibits commercial
use and redistribution, apart from small portions used solely to clarify an
academic publication or presentation. It also prohibits sharing an issued
download link.

For this workflow:

- accept only public documentation, papers, aggregate counts, schemas, and
  user-authored requirement summaries;
- do not ask the user to attach, paste, quote, or expose licensed participant-level
  signals, features, labels, file contents, credentials, signed forms, or
  private download links;
- do not treat public page visibility, a local copy, or academic affiliation as
  proof that the proposed use is authorized;
- do not redistribute film clips, frames, stimuli, data, features, or download
  links;
- stop if answering requires inspecting licensed content.

This is a conservative handling rule for the ASTORIA adaptation. It does
not claim that the license contains an AI-specific prohibition.

The user owns the research question, hypothesis, estimand, emotion construct,
label interpretation, participant and session grain, generalization target,
product choice, split logic, confirmatory status, access decision, final
suitability judgment, and every downstream action.

This skill exposes evidence, assumptions, dependencies, and threats. It does
not choose a model, infer a participant's emotional state, treat an elicited
label as ground truth, rank scientific approaches, or convert observed
classification performance into a psychological claim.

Use this order:

1. current official SEED-IV page and current official SEED family license;
2. primary SEED-IV methods paper;
3. exact public README, channel-order, or package documentation when
   independently supplied and lawful to inspect;
4. secondary papers for dated analytical precedent only;
5. repository candidates as design evidence, never as data authority.

For every source, record the title, responsible organization or authors,
version or date, URL or exact local source state, access date, license status,
and which field it supports.

Preserve conflicts. Do not silently reconcile:

- official page, paper, README, and package inventories;
- intended emotion, self-assessment, and inferred emotion;
- acquisition data, official shared products, and third-party derivatives;
- participant, session, trial, and time-window counts;
- historical evaluation choices and defensible generalization claims.

Label a missing field `unknown`, `unverified`, `not documented`, or `not
applicable`. Never fill it from a repository script or memory.

Edge cases:

- **SEED without version.** Stop and distinguish SEED, SEED-IV, SEED-VIG,
  SEED-V, SEED-GER, and SEED-FRA.
- **Data or features pasted into chat.** Do not inspect them. Ask the user to
  remove the content from scope and continue with public metadata only.
- **Public download link.** Treat visibility as neither permission nor
  redistribution authority.
- **Film stimuli requested.** Stop. Film rights are separate and unverified.
- **Only feature matrices are available.** Preserve their documented
  preprocessing and do not describe them as raw EEG.
- **Random window split proposed.** Expose the leakage target and require the user
  to choose the actual generalization level.
- **Missing label workbook.** Mark channel order, label order, or trial mapping
  unverified. Do not reconstruct it.
- **Different counts across sources.** Preserve source, date, and grain for
  each count.
- **Clinical emotion inference.** Refuse the clinical interpretation and
  return to the bounded elicitation construct.
- **No suitable route.** Produce a blocked specification rather than relaxing
  requirements.

This skill cannot verify licensed file contents, current applicant eligibility,
private link state, product completeness, missingness, channel order, trial
alignment, synchronization, or analysis readiness. It cannot determine that an
elicited label measures a naturalistic or clinical emotional state. It cannot
grant film rights or data permission.
- The SEED administrators may change the license terms; reverify them before any access action.

## Design choices and verification

Use public evidence and the current license to determine which SEED-IV products
can answer the question. When a choice remains, compare eligible product and generalization choices at
the participant, session, trial, and window grains they actually support.
Carry emotion-label assumptions, source provenance, conflicts and unknowns
into the Evidence and Governance Card, Applicability Matrix and Threat Register.
If the constraints leave one defensible route, identify it and explain the
limitation without offering artificial alternatives.

Gate 2 permits preparing and verifying the selected Dataset Suitability and
Access Specification only. Stop before access, data inspection, preprocessing,
analysis or saving.

> [!info] References
> Read `./references/seed_iv_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) for an approved design comparison involving
  repeated measures, film generalization, multimodal structure, or evaluation.
- Offer [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded evidence search.
- Route preprocessing or analysis only after the user has selected the design and
  an appropriate Part 4 owner exists.
- Return any claim or manuscript wording to its canonical analysis or writing
  owner.

Never chain a handoff automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- BCMI Laboratory, Shanghai Jiao Tong University. (n.d.). *License agreement for SEED datasets*.
- BCMI Laboratory, Shanghai Jiao Tong University. (n.d.). *SEED-IV* [Data set]. https://bcmi.sjtu.edu.cn/home/seed/seed-iv.html
- Zheng et al. (n.d.). EmotionMeter: A multimodal framework for recognizing human emotions. *IEEE Transactions on Cybernetics*. https://doi.org/10.1109/TCYB.2018.2797176
