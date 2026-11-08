---
name: hcpya-skill
description: >-
  Evaluates whether one exact HCP Young Adult release, package, modality, task,
  measure, family structure, retest state, or participant subset can support a
  user-supplied research design and produces a selection-bound Dataset
  Suitability and Access Specification. Use when the request, or a part coordinator,
  hands over an explicitly matching HCP-YA question. It verifies the current
  release and access route; keeps the 2025 release separate from S1200 and
  earlier processing; distinguishes participant, imaging, processed, retest, 7T,
  and MEG grains; maps modality, task, relatedness, completeness, processing,
  and governance boundaries; and records only user-selected scope after two
  approval gates. Triggers: can HCP Young Adult support my study, HCP-YA release
  and package selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: multimodal
  population: general
  dependencies: ""
  requires: ConnectomeDB data-use terms
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# HCP Young Adult Dataset Suitability

Evaluate one exact HCP Young Adult evidence state without mixing the current
2025 release with S1200 or importing the assumptions of another HCP cohort.

## Purpose

It does not create accounts, handle credentials, accept terms, download data, choose participants, define unrelated samples, organize files, preprocess, set QC exclusions, analyze data, make scientific claims, search broadly, or save without separate approval.

`hcpya-skill` is the Part 3 owner for one bounded prospective suitability and
access question about the Human Connectome Project Young Adult dataset.

It owns:

- pinning the exact release, participant grain, package, modality, task,
  measure, processing tier, family structure, retest state, and access route;
- keeping the current 2025 release separate from S1200 and earlier releases;
- checking whether population, age, relatedness, modality, task, completeness,
  acquisition, processing, and governance support the stated design;
- comparing only credible release, package, modality, task, and subset routes;
- producing one user-selected Dataset Suitability and Access Specification.

It does not own the question, estimand, family model, unrelated-sample rule,
participant selection, task contrast, QC rule, covariate choice, power target,
analysis, interpretation, or claim.

It never creates an account, handles credentials, accepts data-use terms,
downloads participant-level data, reorganizes files, preprocesses imaging,
excludes participants, fits a model, or uploads or shares data.

Activate only when:

- The user invokes the exact trigger `hcpya-skill`; or
- a verified Active capability hands off one explicit HCP-YA suitability or
  access-planning question.

Do not activate from `HCP`, `young adults`, `connectome`, `download HCP`,
`analyze HCP`, or a task name alone.

For broad dataset discovery, return to [research-companion](../../skills/research-companion/SKILL.md) or
[experimental-design](../../skills/experimental-design/SKILL.md). For prior-study or measurement evidence, offer a
bounded [paper-search](../../skills/paper-search/SKILL.md) handoff after separate approval.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or design |
| Intended estimand | Population, contrast or relation, outcome, unit, and timing |
| Population boundary | Young-adult target, family or unrelated requirements, and generalization target |
| Data requirements | Structural, rest, task, diffusion, 7T, MEG, behavior, genetics, or QC needs |
| Task requirements | Exact task, condition, contrast, behavioral output, and run needs |
| Release boundary | Current 2025, S1200, or another exact historical candidate |
| Product boundary | Unprocessed, minimally processed, MSMAll, task output, or other exact package |
| Access boundary | Open or restricted fields, approved public-document inspection, and storage constraints |
| Intended handoff | Design, power, BIDS, bounded literature search, or later analysis |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask for it and stop.

## Steps

### 1. Build the HCP-YA Fit Brief

Return:

- exact scientific target and intended estimand;
- current 2025, S1200, or other exact historical release scope;
- participant, family, unrelated, retest, modality, task, measure, processing,
  and completeness requirements;
- candidate package, open or restricted field, and access state;
- acquisition, site, relatedness, missingness, processing, storage, and
  governance constraints;
- known unknowns;
- requested output and stop point.

If the request is really access administration, participant selection,
preprocessing, unrelated-sample construction, or analysis, stop and route it.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact release, package inventory, task protocol, known-issue record, terms,
  or supplied local source to inspect;
- whether an account, agreement, participant-level record, restricted lane, or
  protected path would be encountered;
- release, grain, modality, task, processing, completeness, family, and access
  facts to verify;
- stop point before credentials, term acceptance, downloads, writes, or
  handoffs.

Ask:

> Approve this exact HCP-YA source and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize credentials, account creation, term acceptance, restricted-data
access, download, search expansion, saving, or another capability.

### 3. Pin the exact release and access state

Record:

- current 2025 release, S1200, or exact other release;
- release date, documentation version, repository, and terms;
- participant, observation, family, retest, imaging, non-imaging, modality,
  task, run, package, and processing counts at the correct grain;
- site, scanner, acquisition, processing, and QC state;
- completeness, missingness, known issues, and excluded processing states;
- open or restricted status for each selected field;
- access eligibility, agreement, storage, sharing, and dissemination duties;
- conflicts, unknowns, and facts requiring account-level verification.

If the exact state cannot be pinned, mark it **Unknown** and stop before a
suitability conclusion.

### 4. Build the Release and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| Release, date, and repository | | | | |
| Participants, families, and retest observations | | | | |
| Unprocessed, processed, and non-imaging counts | | | | |
| Structural MRI | | | | |
| Resting-state fMRI | | | | |
| MOTOR, EMOTION, and GAMBLING | | | | |
| LANGUAGE, RELATIONAL, SOCIAL, and WORKING MEMORY | | | | |
| Diffusion MRI | | | | |
| Seven-tesla imaging | | | | |
| MEG | | | | |
| Behavioral and restricted measures | | | | |
| Processing tier and provenance | | | | |
| Completeness, QC, and known issues | | | | |
| Access and governance | | | | |

Do not infer participant-level completeness from release-level availability.

### 5. Build the Release and Product Map

| Requirement | 2025 release | S1200 or exact historical release | Exact evidence or mismatch |
|---|---|---|---|
| Population and participant grain | | | |
| Family and retest structure | | | |
| Structural and resting MRI | | | |
| Selected task and runs | | | |
| Diffusion MRI | | | |
| Seven-tesla or MEG subset | | | |
| Behavioral or restricted measure | | | |
| Unprocessed product | | | |
| Minimally processed or MSMAll product | | | |
| Repository and terms | | | |

Keep processing generations, participant grains, variables, and terms
separate.

### 6. Build the Applicability Matrix

| Requirement | Exact release route | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Target population | | | | | |
| Family or unrelated design | | | | | |
| Independent or retest unit | | | | | |
| Required modality | | | | | |
| Exact task and contrast | | | | | |
| Behavioral or restricted measure | | | | | |
| Processing tier | | | | | |
| Completeness and QC tolerance | | | | | |
| Access and storage | | | | | |
| Planned inference | | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- current 2025 versus S1200 release identity;
- processed, unprocessed, non-imaging, and participant grains;
- family, twin, sibling, unrelated, and retest structure;
- participant-level modality, task, run, measure, and QC completeness;
- selected task conditions, contrasts, timing, run count, and behavioral
  outputs;
- 3T, 7T, and MEG acquisition and subset boundaries;
- site, scanner, protocol, acquisition, and processing state;
- exact package and derivative provenance;
- release-specific known issues and processing-error eligibility;
- open versus restricted fields;
- current account, eligibility, terms, transfer, storage, sharing, and
  dissemination duties;
- whether intended claims exceed a young-adult observational cohort.

Do not construct a complete unrelated sample or declare a processing route
superior.

### 8. Assess the selected or eligible routes

Carry forward a route the user already selected if it meets the approved
requirements. Apply the evidence and eligibility checks to that route. If
a check rules it out, report the blocker and leave any replacement choice
to the user. Compare evidence-supported alternatives only when a material
choice remains open and more than one eligible route is credible. Use the
relevant examples below to assess routes or explain why to defer.

1. one exact 2025-release unprocessed modality or task package;
2. one exact 2025-release minimally processed or MSMAll product;
3. one exact family-aware or retest-aware participant design;
4. one exact 7T or MEG subset;
5. one exact S1200 or historical-release route kept fully separate;
6. defer because population, family, task, modality, completeness, processing,
   restricted-field, or access requirements are not met.

For each show:

- exact scope;
- what it supports;
- what it cannot establish;
- family, retest, acquisition, completeness, QC, and processing assumptions;
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

> Which HCP-YA release, participant grain, family or retest structure, modalities, tasks, packages, assumptions, and handoffs should the Dataset Suitability and Access Specification record?

Ask for explicit approval of the assembled specification and stopping point
before proceeding to Step 10.

Gate 2 authorizes only the selected specification. It does not authorize an
account, term acceptance, credential, download, participant selection,
unrelated-sample construction, BIDS action, preprocessing, QC exclusion, power
calculation, analysis, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied scientific target and estimand;
2. exact release, date, repository, participant, observation, family, retest,
   and access state;
3. population and generalization boundary;
4. required modalities, tasks, measures, runs, 7T, and MEG subset;
5. unprocessed or processed package provenance;
6. family, retest, site, scanner, acquisition, processing, completeness,
   missingness, QC, and known-issue threats;
7. open or restricted status and access, security, storage, sharing, and
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

The status is local to the selected design. It is not a scientific conclusion
or a recommendation to use the dataset.

### 11. Verify and stop

Verify:

- release and access claims are dated;
- the 2025 release and S1200 remain distinct;
- participant, observation, imaging, processed, non-imaging, retest, 7T, and
  MEG grains are not conflated;
- family structure and dependence remain visible;
- selected tasks, conditions, contrasts, runs, and outputs are exact;
- open and restricted variables remain distinct;
- participant-level completeness and QC are verified;
- unprocessed and processed products remain distinct;
- unknowns remain unknown;
- only user-selected elements entered the specification;
- no credential, term acceptance, download, selection, write, preprocessing,
  QC exclusion, or analysis occurred.

Then stop.

## Boundaries

The user owns:

- the scientific question, estimand, contrast, outcome, unit, and confirmatory
  status;
- whether the current 2025 release, S1200, or another exact historical release
  is considered;
- participant, family, unrelated, retest, modality, task, measure, and
  processing candidates;
- treatment of relatedness, site, scanner, acquisition, missingness, quality,
  processing version, and restricted variables;
- every access, storage, sampling, analytic, and reporting decision;
- the final suitability judgment and downstream action.

This skill exposes evidence and design constraints. It does not construct an
unrelated sample, choose a family model, or select a processing generation for
The user.

Use this order:

1. current official HCP Young Adult release and data-use pages;
2. exact official release notes, package inventories, known issues, task
   protocols, processing documentation, and open-versus-restricted guide;
3. current BALSA ConnectomeDB access documentation;
4. primary HCP cohort and methods papers for historical context;
5. user-supplied local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement:

- **Verified current source fact**
- **Dated release fact**
- **Selected-package fact**
- **Primary-paper context**
- **User-supplied constraint**
- **Inference**
- **Unknown**

Never combine participants, packages, processing outputs, variables, or QC
states across the 2025 release and S1200 merely because identifiers resemble
one another.

> [!info] References
> Read `./references/hcp_ya_facts.md` before the workflow; it holds the facts that control the review.

Edge cases:

- **Only “HCP” is supplied**: Ask which cohort and exact scientific
  requirement are intended.
- **S1200 and 2025 files are proposed in one analysis**: stop and require an
  explicit, evidence-backed harmonization decision outside this skill. Cite
  the official no-mixing warning.
- **The 1,071 processed count is treated as the total cohort**: distinguish
  processed-release eligibility from unprocessed imaging and non-imaging
  grains.
- **The 46-person retest cohort and 45-person processed-retest count are
  conflated**: preserve the separate project, eligibility, and
  repeated-observation grains. Verify retained IDs and avoid overwriting a
  first-visit file with a retest file.
- **A simple random sample is assumed**: expose twin, sibling, and family
  dependence.
- **Every participant is assumed to have every task and modality**: inspect
  participant-level and run-level completeness.
- **A 7T or MEG requirement is universalized**: verify the exact subset.
- **A restricted variable is requested as open access**: stop and show the
  current restricted-data route and duties.
- **An HCP-A task or age range is imported**: return to the HCP-YA protocol and
  population.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish population representativeness, causal
identification, task validity, family-model validity, processing superiority,
power, analysis validity, generalizability, or fitness for clinical use. It
cannot guarantee that a release, repository, package, agreement, task, or
endpoint remains current after it was last checked.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about cohort
  sampling, task validity, processing, relatedness, or prior analyses.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when family, retest, task, or observation
  structure changes the design.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) only after the user approves the exact unit,
  family or retest handling, estimand, analysis, inference family, and loss
  assumptions.
- Use [bids](../bids/SKILL.md) for curation planning only after an exact governed source is
  legitimately available.
- Route account administration, download, transfer, storage, preprocessing,
  QC, unrelated-sample construction, participant selection, modeling, and
  interpretation to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- [HCP-YA data-use terms]. (n.d.). https://www.humanconnectome.org/study/hcp-young-adult/data-use-terms
- [HCP-YA open-access versus restricted data quick reference]. (n.d.). https://www.humanconnectome.org/study/hcp-young-adult/document/quick-reference-open-access-vs-restricted-data
- [HCP-YA project protocols]. (n.d.). https://www.humanconnectome.org/study/hcp-young-adult/project-protocols
- *HCP-YA 2025 release* [Data set]. (2025, August 11). https://www.humanconnectome.org/study/hcp-young-adult/document/hcp-young-adult-2025-release
- *HCP Retest* [Data set]. (n.d.). BALSA. https://balsa.wustl.edu/project?project=HCP_Retest
