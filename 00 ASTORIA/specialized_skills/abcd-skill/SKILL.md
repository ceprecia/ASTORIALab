---
name: abcd-skill
description: >-
  Evaluates whether one exact Adolescent Brain Cognitive Development Study
  release, event, substudy, modality, variable family, or participant subset can
  support a user-supplied research design and produces a selection-bound Dataset
  Suitability and Access Specification. Use when the request, or a part coordinator,
  hands over an explicitly matching ABCD question. It verifies the current
  release and NBDC access state; maps longitudinal events, families, sites,
  scanners, modalities, measures, missingness, withdrawals, derivatives, and
  governance; exposes dependency and inference threats; and records only
  user-selected scope after two approval gates. It does not create accounts,
  handle credentials, submit agreements, download data, choose participants or
  variables, organize files, preprocess, set QC exclusions, analyze data, make
  scientific claims, search broadly, or save without separate approval.
  Triggers: can ABCD support my study, ABCD release and event selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: developmental
  dependencies: ""
  requires: approval of the applicable public-source inspection boundary for public-metadata review. Any separately authorized protected-data action requires verified authorization through the applicable NBDC route or documented eligible legacy route
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-10-29"
---

# ABCD Study Dataset Suitability

Evaluate one exact ABCD Study state without turning a large longitudinal
resource, a stale access route, or an external orchestration prompt into an
automatic pipeline.

## Purpose

`abcd-skill` is the Part 3 canonical owner for one bounded prospective
suitability and access question about the Adolescent Brain Cognitive
Development Study.

It owns:

- pinning the exact current release, patch, freeze, event, substudy, modality,
  file, table, variable family, and access state;
- mapping participant, family, birth-group, event, site, scanner, and substudy
  dependencies;
- checking whether the proposed population, observations, modalities, measures,
  timing, and governance support the stated design;
- comparing only credible release, event, modality, substudy, or derivative
  routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the scientific question, estimand, hypotheses, sampling rule,
variable choice, QC rule, covariate choice, weighting, causal assumptions,
power target, analysis, interpretation, or scientific claim.

It never creates an account, handles credentials, submits a Data Use
Certification, accepts terms, downloads participant-level data, reorganizes
files, preprocesses imaging, selects a cohort, fits a model, or uploads or
shares data.

Activate only when:

- The user invokes the exact trigger `abcd-skill`; or
- a verified Active capability hands off one explicit ABCD suitability or
  access-planning question.

Do not activate from `ABCD`, `developmental cohort`, `adolescent imaging`,
`large longitudinal dataset`, `download ABCD`, or `analyze ABCD`.

If the request is broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). If it asks what prior studies have done, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, exposure or contrast, outcome, unit, and time relation |
| Observation structure | Participant, family, visit, event, site, scanner, and substudy needs |
| Data requirements | Modalities, measures, files, tables, derived variables, and timing |
| Release boundary | Candidate release or need to identify the current release |
| Missingness boundary | Required waves and acceptable incomplete or irregular observations |
| Access boundary | Approved public-document inspection and institutional or security constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the user has not supplied the scientific target, ask for it and stop.

## Steps

### 1. Build the ABCD Fit Brief

Return:

- exact scientific target and intended estimand;
- fixed population, timing, observation, modality, and measure requirements;
- candidate release, event, substudy, file, table, or derivative states;
- family, site, scanner, and repeated-observation needs;
- access, security, and storage constraints;
- known unknowns;
- requested output and stop point.

If the request is actually access administration, cohort extraction,
preprocessing, variable selection, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact official release, access, dictionary, known-issue, imaging, or supplied
  local sources to inspect;
- whether any controlled portal, agreement, participant-level record, or
  protected path would be encountered;
- release and design facts to verify;
- stop point before credentials, agreements, downloads, writes, or handoffs.

Ask:

> Approve this exact ABCD source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, access applications, agreement
submission, protected-data access, download, search expansion, saving, or
another capability.

### 3. Pin the exact release and access state

Record:

- release number, patch, posting date, freeze date, and documentation version;
- participants, events, and completion status at their correct grain;
- withdrawal and correction state;
- selected core event, substudy event, file, table, variable family, or
  derivative version;
- current access route, agreement type, renewal state, and security conditions;
- data dictionary, known-issue, imaging, and curation documentation versions;
- conflicts, unknowns, and facts that require account-level verification.

If the state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, patch, and freeze | | | | |
| Participant and withdrawal state | | | | |
| Core and substudy events | | | | |
| Population and recruitment | | | | |
| Family and birth-group structure | | | | |
| Site, scanner, and software | | | | |
| Structural MRI | | | | |
| Diffusion MRI | | | | |
| Resting and task fMRI | | | | |
| Behavioral and cognitive measures | | | | |
| Biospecimen, genetic, wearable, or linked data | | | | |
| Missingness and completion | | | | |
| Raw and derivative provenance | | | | |
| Access and governance | | | | |

Do not infer participant-level availability from a release-level domain list.

### 5. Build the Longitudinal Dependency Map

| Level | Identifier or evidence | Repetition or clustering | Planned role | Unresolved issue |
|---|---|---|---|---|
| Participant | | | | |
| Family or birth group | | | | |
| Core event | | | | |
| Substudy event | | | | |
| Site | | | | |
| Scanner and software | | | | |
| File, table, or variable | | | | |

Preserve irregular visit timing, skipped events, changing assent or consent,
scanner changes, and substudy-specific event semantics.

### 6. Build the Applicability Matrix

| Requirement | Exact ABCD route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Exposure or contrast | | | | | |
| Outcome and measure | | | | | |
| Temporal ordering | | | | | |
| Required events | | | | | |
| Modality and file type | | | | | |
| Family dependence | | | | | |
| Site and scanner dependence | | | | | |
| Missingness tolerance | | | | | |
| Target inference | | | | | |

### 7. Build the Threat and Governance Register

Check at minimum:

- recruitment, sampling, weighting, and target-population limits;
- family, twin, sibling, site, scanner, software, and repeated-event
  dependencies;
- event completeness, irregular timing, attrition, withdrawal, and
  informative missingness;
- changing instruments, derived variables, curation, and release definitions;
- modality and measure availability at the selected participant-event grain;
- temporal-order and developmental-change assumptions;
- exposure, outcome, and covariate timing;
- substudy and core-event misalignment;
- site or scanner confounding with age, event, group, or outcome;
- use of a derivative as if it were raw data;
- access, training, agreement, security, storage, dissemination, and renewal
  duties;
- whether planned claims exceed an observational cohort.

Do not call ABCD nationally representative without the exact sampling,
weighting, target-population, and inferential qualifications.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one pinned release and one core event;
2. one pinned release and a defined repeated-event window;
3. one substudy with its own event and access structure;
4. one exact modality or variable-family route;
5. one version-pinned derivative with explicit provenance;
6. defer ABCD because timing, measure, completeness, access, dependency, or
   inference requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- dependency and missingness assumptions;
- access burden;
- unresolved evidence;
- downstream handoffs.

Do not rank routes unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show:

- Release and Evidence Card;
- Longitudinal Dependency Map;
- Applicability Matrix;
- Threat and Governance Register;
- assessed route and disqualifying conditions, plus any comparison needed
  to resolve a material choice;
- unresolved conflicts and unknowns.

Carry forward confirmed eligible choices. If a material decision is open or
new evidence changes it, ask only about the affected fields in this prompt.

> Which ABCD release, events, modalities, measures, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, agreement, credential, download, cohort or variable selection, BIDS
action, preprocessing, QC exclusion, power calculation, analysis, save, or
handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, patch, freeze, event, substudy, modality, file, table, and
   derivative state;
3. population and observation units;
4. family, event, site, scanner, software, and substudy dependencies;
5. required measures and their timing;
6. completion, withdrawal, missingness, and attrition limits;
7. raw and derivative provenance;
8. access, agreement, security, storage, renewal, and dissemination duties;
9. selected assumptions and explicit non-assumptions;
10. unresolved gaps and disqualifying conditions;
11. downstream handoff packets;
12. verification record;
13. suitability status:
    - **Suitable within the selected boundary**
    - **Conditionally suitable**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the specified design and is not a causal, clinical, or
scientific conclusion.

### 11. Verify and stop

Verify:

- current release and access claims are dated;
- recruitment and release counts are not conflated;
- event labels are not treated as complete data;
- participant, family, event, site, scanner, and substudy dependencies remain
  explicit;
- raw ABCD and derivative collections remain distinct;
- new users are not routed to the stale NDA path;
- incomplete events remain labeled incomplete;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, agreement, download, cohort selection, write, preprocessing,
  or analysis occurred.

Then stop.

## Boundaries

The user owns:

- whether ABCD is a candidate at all;
- the question, target population, estimand, exposure, contrast, outcome,
  temporal ordering, and confirmatory status;
- release, event, substudy, modality, measure, participant, and derivative
  candidates;
- treatment of family, site, scanner, repeated observations, missingness,
  withdrawals, sampling, and weights;
- every access, security, storage, data-use, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and implications. It does not turn database
availability into a scientific decision.

Use this order:

1. current official ABCD documentation and release notes;
2. current NIH Brain Development Cohorts Data Hub documentation and agreements;
3. exact official data dictionaries, known-issue records, imaging
   documentation, and release manifests;
4. primary cohort and methods papers for historical design context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-table or file fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Release, count, event, access, patch, variable, table, and known-issue claims
must carry a source and access date.

> [!info] References
> Read `./references/abcd_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “ABCD” is supplied**: Ask for the scientific requirement. Do not
  choose a release, event, measure, or cohort.
- **A candidate says Release 5.1 is current**: Mark it stale and verify the
  current official release.
- **A new user is routed to NDA**: Correct the route to the current NBDC Data
  Hub process and preserve the limited legacy NDA exception.
- **A participant count is requested**: State whether it is recruitment,
  release inclusion, event availability, or analytic completeness.
- **A wave is called complete**: Check the exact release note, freeze, event,
  and domain.
- **A row is treated as independent**: Check participant, family, birth-group,
  event, site, scanner, and substudy identifiers.
- **A substudy visit is aligned by label alone**: require its exact event
  mapping and timing.
- **A modality is assumed annual**: verify its collection schedule and
  participant-event availability.
- **ABCC is proposed**: record its exact derivative version and provenance; do
  not call it raw ABCD.
- **American Indian or Alaska Native analysis is proposed**: recheck the
  current separate agreement and dissemination rules.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish representativeness, causal identification,
diagnostic or clinical validity, developmental mechanism, power, analysis
validity, or generalizability. It cannot guarantee that a release, table,
variable, known issue, access rule, agreement, or endpoint remains current
after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about measure
  validity, cohort methods, missingness, weighting, scanner effects, or prior
  analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when release or event structure changes the
  scientific design.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) only after the user approves the exact analytic units,
  dependencies, event window, effect basis, and loss assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route access administration, cohort extraction, preprocessing, QC, variable
  selection, weighting, modeling, and interpretation to separately approved
  owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- ABCD Study. (n.d.). *ABCD documentation*. https://docs.abcdstudy.org/latest/
- ABCD Study. (n.d.). *ABCD study overview*. https://docs.abcdstudy.org/latest/study/
- ABCD Study. (n.d.). *Access guide*. https://docs.abcdstudy.org/latest/usage/access.html
- ABCD Study. (n.d.). *Data sharing*. https://abcdstudy.org/scientists/data-sharing/
- ABCD Study. (n.d.). *Data structure*. https://docs.abcdstudy.org/latest/documentation/curation/structure.html
- ABCD Study. (n.d.). *Imaging documentation*. https://docs.abcdstudy.org/latest/documentation/imaging/index.html
- ABCD Study. (2026, May 13). *Release 7.0 notes*. https://docs.abcdstudy.org/latest/documentation/release_notes/7_0.html
- NBDC Data Hub. (n.d.). *Data access process*. https://www.nbdc-datahub.org/data-access-process
