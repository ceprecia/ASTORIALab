---
name: dmt-har-med-skill
description: >-
  Evaluates whether the exact DMT-HAR-MED OpenNeuro release, participant groups,
  pre-retreat and post-retreat sessions, resting-state fMRI, post-only T1w,
  physiology, derivatives, or participant subset can support one user-supplied
  research design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching DMT-HAR-MED question. It verifies the current ds006644
  release and license state; preserves the 40-released-versus-39-paper-analyzed
  distinction and the CC0-versus-CC-BY-4.0 conflict; separates subacute
  retreat-plus-drug effects from acute drug effects; maps group, timing,
  modality, completeness, processing, blinding, generalizability, and access
  boundaries; and records only user-selected scope after two approval gates.
  Triggers: can DMT-HAR-MED support my study, DMT HAR MED dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: fmri
  population: clinical
  dependencies: ""
  requires: OpenNeuro access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# DMT-HAR-MED Dataset Suitability

Evaluate one exact DMT-HAR-MED evidence state without converting a specialized
subacute retreat study into a generic psychedelic fMRI pipeline.

## Purpose

It does not download data, resolve the license conflict, choose participants or contrasts, organize files, preprocess, set QC exclusions, analyze data, infer psychometric associations, make scientific or clinical claims, search broadly, or save without separate approval.

`dmt-har-med-skill` is the conditional Part 3 owner for one bounded
prospective suitability and access question about OpenNeuro dataset
`ds006644`, DMT-HAR-MED.

It pins the release, participant grain, group, session, modality, physiology,
derivative, completeness, and access state; separates released from
paper-analyzed participants and subacute from acute imaging; compares only
credible routes; and produces one user-selected Dataset Suitability and Access
Specification.

It does not own scientific or analytic decisions. It never downloads data,
changes BIDS files, reruns derivatives, excludes participants, reconstructs
unreleased measures, fits models, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `dmt-har-med-skill`; or
- a verified Active capability hands off one explicit DMT-HAR-MED suitability
  or access-planning question.

Do not activate from `DMT`, `psychedelic fMRI`, `ayahuasca`, `meditation`,
`OpenNeuro`, `download ds006644`, or `analyze DMT data`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the intervention, control, timing, or
measurement structure must be designed. Offer [paper-search](../../skills/paper-search/SKILL.md) only for a
separately approved bounded search about measurement validity, prior evidence,
or an unresolved study-design question.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target and estimand | user-supplied question or design; population, contrast, outcome, unit, and timing |
| Population and intervention | Intended population; DMT plus harmine, placebo, retreat, and required causal distinction |
| Data and session | Required modality or product; pre-retreat, post-retreat, change, or another exact timing |
| Release and access | Snapshot 1.0.1 or newer-state check; intended use and approved inspection boundary |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should DMT-HAR-MED be evaluated against?

Then stop.

## Steps

### 1. Build the DMT-HAR-MED Fit Brief

Return the exact target and estimand; population, intervention, control,
session, timing, modality, product, and completeness requirements; candidate
participant grains; required causal distinctions; design, access, and license
constraints; known conflicts and unknowns; and the requested stop point.

If the request is really a download, participant selection, BIDS action,
preprocessing, QC exclusion, psychometric reconstruction, or analysis, stop
and route it outside this skill.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact sources to inspect;
- any account, credential, participant-level, protected-path, or
  license-sensitive boundary;
- release, participant, design, product, processing, and license facts to
  verify;
- the stop point before downloads, writes, search expansion, or handoffs.

Ask:

> Approve this exact DMT-HAR-MED source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize account creation, credentials, downloads, license resolution,
search expansion, saving, preprocessing, analysis, or another capability.

### 3. Pin the exact release and access state

Record exact identity and changes; released and paper-analyzed participant
grains; group and exclusion context; sessions and drug-to-scan interval;
product availability and absence; acquisition and derivative provenance;
access and both license statements; missingness, unknowns, and rechecks.

If the exact release cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Conflict or recheck |
|---|---|---|---|---|
| Accession, snapshot, DOI, and date | | | | |
| Released versus paper-analyzed participants | | | | |
| Groups, retreat, intervention, and blinding | | | | |
| Sessions and subacute timing | | | | |
| Resting-state fMRI and post-only T1w | | | | |
| Raw physiology and included derivatives | | | | |
| Unreleased psychometrics and absent task, events, and diffusion | | | | |
| Site, scanner, and coil | | | | |
| Access and license conflict | | | | |

Do not infer participant-level quality from release-level availability.

### 5. Build the Design and Product Map

| Requirement | Exact released route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Population and generalization | | | | | |
| DMT plus harmine, placebo, and retreat | | | | | |
| Drug-specific, retreat, or synergy claim | | | | | |
| Acute versus subacute pre-post state | | | | | |
| Resting-state fMRI and structural MRI | | | | | |
| Physiology and psychometric association | | | | | |
| Task fMRI, events, or diffusion | | | | | |
| Raw or included derivative product | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 6. Build the Applicability Matrix

| Requirement | Selected release, group, session, or product | Supported evidence | Limitation | Unknown or recheck |
|---|---|---|---|---|
| Target population and estimand | | | | |
| Intervention, control, and temporal interpretation | | | | |
| Required modality and measure | | | | |
| Participant and product completeness | | | | |
| Processing provenance | | | | |
| Access and intended use | | | | |

Do not convert an unsupported psychometric, task, acute, or synergy
requirement into a conditional fit.

### 7. Build the Threat and Governance Register

Check at minimum:

- 40 released participants versus 39 analyzed in the imaging paper;
- DMT plus harmine rather than DMT alone;
- retreat exposure in both treatment groups;
- absence of intervention-free and meditation-free drug groups;
- pre-retreat versus post-retreat session identity;
- approximately two-day subacute timing rather than acute drug imaging;
- post-only T1w and its implications for longitudinal structural claims;
- participant-level resting-state, physiology, T1w, and derivative
  completeness;
- absence of released questionnaires, psychometrics, task fMRI, event files,
  and diffusion MRI;
- site, scanner, coil, acquisition, and processing state;
- one motion-related paper exclusion and the absence of a dataset-owned QC
  threshold;
- fMRIPrep 23.0.2 and physIO derivative provenance;
- blinding failure and expectancy risk;
- experienced-meditator and demographic generalizability;
- CC0 versus CC-BY-4.0 source conflict;
- whether intended claims exceed this randomized retreat-plus-drug design.

Do not invent event timing, phenotype fields, a 0.3 mm motion rule, or a
license resolution.

### 8. Assess the selected or eligible routes

Assess the selected DMT-HAR-MED release, session, or product route against
the approved question.
If it cannot meet the requirements, report the blocker. Compare eligible
routes only if a material choice remains open and the evidence supports
more than one. These are examples of routes and possible dispositions.

1. one exact snapshot 1.0.1 participant-metadata route;
2. one exact pre-retreat or post-retreat resting-state route;
3. one exact pre-post subacute resting-state route;
4. one exact post-session T1w route;
5. one exact physiology-informed route;
6. one exact included fMRIPrep or physIO derivative route with provenance;
7. defer because population, intervention, control, timing, modality,
   measurement, completeness, license, or design requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- population, retreat, treatment, timing, completeness, processing, and
  license assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Design and Product Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward the user's confirmed choices.

Ask about the DMT-HAR-MED release, participant grain, groups, sessions,
products, assumptions, and handoffs only when a decision remains open or
new evidence materially changes it.

Ask for explicit approval of the assembled Dataset Suitability and Access
Specification and its scope, including the stopping point.

Gate 2 authorizes only the selected specification. It does not authorize an
account, credential, download, license interpretation, participant selection,
BIDS action, preprocessing, QC exclusion, psychometric construction, power
calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact accession, snapshot, DOI, release date, commit, and access state;
3. released and paper-analyzed participant grains;
4. population, DMT-plus-harmine, placebo, retreat, and control boundary;
5. pre-retreat, post-retreat, and subacute timing boundary;
6. required resting-state, post-only T1w, physiology, and derivative products;
7. explicitly unavailable psychometric, behavioral, task, event, and
   diffusion products;
8. site, scanner, coil, completeness, motion, blinding, and generalizability
   threats;
9. raw or included derivative provenance;
10. both license statements and the unresolved conflict;
11. selected assumptions and explicit non-assumptions;
12. unresolved gaps and disqualifying conditions;
13. downstream handoff packets;
14. verification record;
15. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not a scientific, clinical,
legal, or licensing conclusion and is not a recommendation to use the
dataset.

### 11. Verify and stop

Verify:

- release, access, and license claims are dated;
- 40 released and 39 paper-analyzed participants remain distinct;
- DMT plus harmine is not shortened to DMT alone;
- post-retreat imaging is not called acute;
- retreat and drug effects are not separated beyond the design;
- T1w remains post-only;
- task fMRI, events, diffusion, questionnaires, and psychometrics are not
  invented;
- raw physiology and included derivatives remain distinct;
- fMRIPrep and physIO provenance remains visible;
- no fixed QC threshold or participant exclusion was selected;
- the license conflict remains explicit;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no download, write, preprocessing, QC exclusion, analysis, or claim
  occurred.

Then stop.

## Boundaries

The user owns the scientific question, hypothesis, prediction, estimand, contrast,
outcome, unit, timing, confirmatory status, candidate groups and products,
treatment of design threats, every access or analytic decision, the final
suitability judgment, and downstream action.

This skill exposes evidence, source conflicts, and design constraints. It does
not infer a DMT effect, a harmine effect, a meditation effect, or synergy for
The user.

Use this order:

1. current official OpenNeuro snapshot and machine-readable metadata;
2. exact snapshot README, CHANGES, participants table, file tree, and sidecars;
3. current OpenNeuro access and publication terms;
4. the primary imaging paper and trial record for design context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement as **Verified current source fact**, **Dated
release fact**, **Selected-product fact**, **Official-source conflict**,
**Primary-paper context**, **User-supplied constraint**, **Inference**, or
**Unknown**.

Never silently resolve the license conflict or treat a study measure as
released data.

Edge cases:

- **Only “DMT-HAR-MED” is supplied**: ask for the one scientific requirement.
  Do not choose a contrast, session, product, or participant subset.
- **The dataset is called acute DMT imaging**: correct it to post-retreat,
  approximately two-day subacute imaging.
- **The intervention is called DMT alone**: preserve DMT plus harmine.
- **Forty participants are called the paper sample**: distinguish 40 released
  from 39 analyzed.
- **The release is called rs-fMRI only**: record post-session T1w.
- **T1w is treated as longitudinal**: record that it is available only post.
- **Psychometric association is requested**: record that the study collected
  measures but snapshot 1.0.1 does not release the questionnaire data.
- **Event timing or task fMRI is requested**: record that the release has
  resting-state data and no event files or task fMRI.
- **Diffusion is requested**: return a mismatch.
- **FD 0.3 is proposed as a dataset rule**: return the QC decision to the user and
  require separate method evidence.
- **CC0 or CC-BY-4.0 is asserted as settled**: preserve the source conflict and
  require current clarification for any license-sensitive action.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish acute drug effects, a DMT-specific effect,
harmine-specific effect, meditation effect, drug-meditation synergy,
psychometric association, causal mechanism, power, analysis validity,
clinical utility, generalizability, or legal license interpretation. It cannot
guarantee that a snapshot, file inventory, term, correction, or endpoint
remains current after it was last checked.

## Design choices and verification

These design references describe the workflow, not a prior decision for this user. Apply the current request's scope and required approvals; these notes authorize no additional action.

Keep source labels, the 40-versus-39 grains, design limitations, missing products, derivative provenance, and the license conflict visible in the Release and Evidence Card, Design and Product Map, Applicability Matrix, and Threat and Governance Register. Use the Applicable Route Comparison for an unresolved choice among evidence-supported release, group, session, modality, physiology, derivative, or defer routes.

After Gate 2, record only the elements the user selected in the Dataset Suitability and Access Specification and retain the verification record. This is a specification-only handoff with no data action.

The stronger behaviors of downloading data, constructing a cohort, choosing a
motion rule, rerunning a pipeline, or testing an analysis are outside this
skill.

> [!info] References
> Read `./references/dmt_har_med_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about
  psychedelic-retreat design, measure validity, blinding, generalizability,
  or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when control groups, timing, intervention
  decomposition, or measurement requirements change the design.
- Route download, storage, BIDS work, preprocessing, QC, participant
  selection, modeling, interpretation, and license resolution to separately
  approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- ClinicalTrials.gov. (n.d.). *NCT05780216*. https://clinicaltrials.gov/study/NCT05780216
- *DMT-HAR-MED* (Version 1.0.1) [Data set]. (n.d.). OpenNeuro. https://doi.org/10.18112/openneuro.ds006644.v1.0.1
- Egger et al. (2025). *Imaging Neuroscience*. https://doi.org/10.1162/IMAG.a.907
- OpenNeuro. (n.d.). *User guide*. https://docs.openneuro.org/user_guide.html
