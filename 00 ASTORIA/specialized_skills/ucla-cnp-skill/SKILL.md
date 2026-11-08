---
name: ucla-cnp-skill
description: >-
  Evaluates from public metadata whether one exact UCLA Consortium for
  Neuropsychiatric Phenomics LA5c release, participant or diagnosis grain, MRI
  modality, task, phenotype field, source-versus-derivative state, access state,
  or proposed subset can support one user-supplied design and produces a
  selection-bound Dataset Suitability and Access Specification. Use when the
  request, or a part coordinator, hands over an explicitly matching UCLA CNP
  question. It preserves the 290-person parent-description versus 272-person
  distributed-snapshot distinction, 130 CONTROL, 50 SCHZ, 49 BIPOLAR, 43 ADHD
  inventory, modality-specific missingness, T1 aliasing, event-timing
  correction, PAM design-change, historical diagnostic, population,
  public-release, and raw-versus-derivative boundaries after two approval gates.
  Triggers: can UCLA CNP support my study, LA5c dataset selection.
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

# UCLA CNP Dataset Suitability

Evaluate one exact UCLA CNP source and inference fit without turning a public
multimodal psychiatric-neuroimaging release into an automatic processing
pipeline.

## Purpose

It does not receive participant data, download, select, relabel, preprocess, validate BIDS, harmonize, model, analyze, make scientific or clinical claims, or save without separate approval.

`ucla-cnp-skill` is the conditional Part 3 owner for one bounded prospective
suitability and access-planning question about the UCLA Consortium for
Neuropsychiatric Phenomics LA5c dataset.

It pins the release, participant table, diagnosis label, modality, task,
phenotype field, source-versus-derivative state, missingness, access, and
intended inference; compares only credible metadata-level routes; and produces
one user-selected Dataset Suitability and Access Specification.

It does not own diagnosis, phenotype construction, experimental design,
preprocessing, BIDS validation, harmonization, quality exclusion, modeling, or
analysis. It never downloads data, opens participant records, selects people,
relabels groups, processes images, or generates clinical claims.

Activate only when:

- The user invokes the exact trigger `ucla-cnp-skill`; or
- a verified Active capability hands off one explicit UCLA CNP suitability or
  access-planning question.

Do not activate from `UCLA`, `CNP`, `psychiatric MRI`, `OpenNeuro`,
`schizophrenia`, `ADHD`, `bipolar`, `download ds000030`, or `analyze CNP`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the group, dimensional construct, modality,
task, field, missingness, comparison, or evaluation structure must be
designed. Offer [paper-search](../../skills/paper-search/SKILL.md) only for a separately approved bounded search
about a construct, task, measure, or prior UCLA CNP result.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, estimand, and intended inference |
| Population and construct | Exact group, dimension, phenotype, or comparison rule |
| Unit | Participant, session, modality, run, task condition, scale, item, raw image, event row, or derivative |
| Product need | T1w, DWI, rest, breath hold, BART, stop signal, task switching, SCAP, PAM, physiology, phenotype, or derivative |
| Generalization target | Within release, across diagnosis, new population, or another explicit target |
| Source state | OpenNeuro snapshot, paper state, historical derivative, or unresolved comparison |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should UCLA CNP be evaluated against?

Then stop.

## Steps

### 1. Build the UCLA CNP Fit Brief

Restate the question, construct, participant and modality grain, required task
or phenotype, source and product state, generalization target, access boundary,
and unresolved definitions. Separate evidence from interpretation.

### 2. Gate 1: approve the public inspection boundary

Present:

1. exact question and inference;
2. versioned public sources;
3. cohort, diagnosis, field, modality, task, product, and timing metadata to
   inspect;
4. the selected route or credible alternatives for a material choice that
   remains open;
5. known count, completion, quality, and timing conflicts;
6. participant-level facts that remain out of scope.

Gate 1 authorizes only the displayed public metadata inspection. It does not
authorize downloads, participant records, subset construction, diagnosis
relabeling, BIDS validation, preprocessing, quality exclusion, modeling,
analysis, or saving.

Reopen Gate 1 after a material source or construct change.

### 3. Pin exact source and product states

Record the OpenNeuro version, DOI, commit, license, participant-table and
modality grains; paper DOI; any derivative version; raw or processed state;
access state; and unresolved conflict.

### 4. Build the Source and Population Card

| Field | Verified value | Source state | Status | Consequence |
|---|---|---|---|---|
| Parent and distributed cohort | | | | |
| Diagnostic and demographic fields | | | | |
| Imaging and task inventory | | | | |
| Phenotype inventory | | | | |
| Raw and processed products | | | | |
| Access, consent, and ethics state | | | | |

### 5. Build the Grain and Completeness Map

Map each requested element to participant, session, modality, run, condition,
scale, item, raw file, event row, or derivative grain; manifest count;
missingness; label source; timing state; raw or processed state; and access
route.

Do not derive a complete-case count from the separate availability totals.

### 6. Build the Applicability Matrix

Assess the exact selected route in this matrix. Include alternatives only
when needed to resolve a material open choice. The table shows example rows.

| Route | Supports | Does not support | Assumptions | Missingness controls | Product state |
|---|---|---|---|---|---|
| Public metadata only | | | | | |
| Raw OpenNeuro modality | | | | | |
| Task-event route | | | | | |
| Phenotype-linked route | | | | | |
| Historical derivative route | | | | | |

Omit unused rows. If the selected route cannot answer the approved question,
report the blocker. Keep ranking and selection with the user.

### 7. Build the Threat and Governance Register

At minimum assess:

- parent-description versus distributed-snapshot counts;
- diagnostic label, symptom dimension, and clinical-truth conflation;
- historical race, ethnicity, education, language, and handedness restrictions;
- modality and task-specific missingness;
- PAM task-version exclusion;
- T1 aliasing and analysis-specific QC;
- corrected, uncompensated, and estimated event timing;
- raw, summary, and processed-product conflation;
- participant, session, run, item, and derivative leakage;
- medication, substance-screen, diagnosis, and recruitment-era boundaries;
- psychiatric-population stigma, reidentification, and clinical overreach;
- small or unbalanced complete-case subsets and generalization.

For each threat, show evidence, consequence, possible control, residual risk,
and the user's retained decision.

### 8. Assess the selected or eligible routes

Assess the selected route for scientific fit, construct support, population
grain, modality and task coverage, missingness, timing state, quality threats,
raw-versus-processed provenance, access, ethics, generalization, and unresolved
evidence. Compare eligible alternatives on these criteria only
if a material choice remains open and more than one route is credible. Report a blocker
on the selected route without substituting another. Do not recommend or
select a route.

### 9. Gate 2: select the specification

Present all cards, maps, matrices, and threats. Include a comparison only
when a material choice required one. The user confirms the recorded choices
and decides any open items for the source snapshot, population and construct, modality and task,
phenotype fields, participant and run grain, raw or processed product, missingness and
quality rule, timing handling, generalization boundary, ethics caveats, and
next stop or handoff.

Gate 2 authorizes only the selected Dataset Suitability and Access
Specification. It does not authorize data access, download, participant
selection, diagnosis relabeling, BIDS validation, preprocessing, QC exclusion,
harmonization, modeling, analysis, claims, saving, or a pipeline.

### 10. Produce the Dataset Suitability and Access Specification

Return:

1. question, estimand, and intended inference;
2. pinned OpenNeuro, paper, and derivative states;
3. parent and distributed population grains;
4. diagnosis, phenotype, modality, task, session, run, and product grains;
5. exact availability and unresolved intersection;
6. quality, timing, missingness, leakage, and generalization controls;
7. raw or processed provenance;
8. access, consent, privacy, ethics, and citation duties;
9. assumptions, unknowns, exclusions, and residual risks;
10. user-selected choices and any rejected alternatives that were evaluated;
11. separately approved handoff or explicit stop.

### 11. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- 290 parent-description people and 272 distributed rows remain distinct;
- 130, 50, 49, and 43 distributed group counts remain visible;
- availability stays modality and task specific;
- no complete-case intersection is invented;
- T1 ghost, PAM design change, and event-timing states remain visible;
- historical labels are not treated as present clinical truth;
- raw and processed products remain distinct;
- no participant data entered the workflow;
- both gates bound their authorization;
- no scientific or downstream choice was made for the user.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

OpenNeuro snapshot `ds000030` version `1.0.0` is public under CC0. Public
availability does not remove ethical, reidentification, stigma, consent,
institutional, or scientific-inference duties. Historical derivative releases
are separate products with their own processing provenance.

This Part 3 skill:

- accepts only public documentation, aggregate inventories, schemas, and
  user-authored requirement summaries;
- does not ask the user to paste, attach, or upload participant-level phenotype,
  imaging, event, motion, quality, or identifier records;
- does not download public data or treat CC0 as permission to ignore human-data
  safeguards;
- does not authenticate, execute access commands, or accept terms;
- stops if the answer requires participant-level inspection.

The user owns the research question, hypothesis, estimand, diagnostic or
dimensional construct, comparison, modality and task choice, phenotype
definition, participant exclusions, missingness rule, generalization target,
confirmatory status, access decision, final suitability judgment, and every
downstream action.

This skill exposes evidence and threats. It does not decide that a categorical
or dimensional model is scientifically preferable, treat a historical
diagnosis code as current clinical truth, merge modalities for convenience, or
choose a processed product because it is easier to use.

Use this order:

1. exact versioned OpenNeuro snapshot and its manifests;
2. peer-reviewed UCLA CNP Data Descriptor and supplements;
3. exact versioned derivative description for a derivative-specific question;
4. exact user-supplied, authorized local manifest;
5. secondary papers for paper-specific subsets and analyses only;
6. repository candidate material as design evidence, never data authority.

For each fact, record source, version or date, URL or commit, grain, access
state, and whether it describes the parent recruitment pool, distributed
participant row, completed modality, run, or complete-case subset.

Preserve conflicts between:

- the 290-person parent-study description and 272-person distributed snapshot;
- intended acquisition and participant-table completion;
- diagnosis label, symptom dimension, and current clinical interpretation;
- raw BIDS, metadata summaries, and separately processed derivatives;
- task-program timing and scanner-trigger-adjusted event timing.

Never infer complete cases from a headline sample size.

Edge cases:

- **CNP is ambiguous:** confirm the UCLA Consortium for Neuropsychiatric
  Phenomics LA5c dataset.
- **290 is called the released sample:** restore the 290 parent-description
  versus 272 distributed-snapshot distinction.
- **All 272 are called multimodal complete cases:** show per-modality
  availability and leave the intersection unresolved.
- **A diagnosis code is treated as current clinical truth:** restore the
  historical instrument, label, and construct boundary.
- **Face memory or monetary incentive is assumed:** reject it unless an exact
  authoritative product proves otherwise.
- **T1w is treated as uniformly usable:** surface the aliasing flag and require
  analysis-specific QC later.
- **Event onsets are mixed:** separate adjusted, unadjusted, and estimated
  timing.
- **Raw and historical derivatives are merged:** restore version, processing,
  and exclusion provenance.
- **CC0 is called unrestricted clinical evidence:** restore ethics and
  inference boundaries.
- **No suitable route:** return a blocked specification.

This skill cannot verify participant-level diagnoses, symptom scoring,
medication state, missingness mechanisms, image quality, event accuracy,
complete-case counts, derivative validity, or clinical utility. It cannot
grant ethical permission or establish population generalizability.

## UCLA CNP facts that control the review

Use these only with their pinned source states.

### Cohort and repository grain

- The peer-reviewed Data Descriptor and OpenNeuro `participants.tsv` describe
  272 distributed participants: 130 `CONTROL`, 50 `SCHZ`, 49 `BIPOLAR`, and
  43 `ADHD`.
- The current `dataset_description.json` describes a larger parent-study
  recruitment state of 290 people: 138 community controls, 58 schizophrenia,
  49 bipolar disorder, and 45 ADHD. Do not call that the released BIDS count.
- Participants were 21 to 50 years old. The description records Los Angeles
  community recruitment and historical inclusion rules that limited the
  racial and ethnic sampling frame.
- The description records at least eight years of education and English or
  Spanish testing, with language selected by verbal fluency for bilingual
  participants. These are design and generalization constraints, not
  background trivia.
- Historical diagnostic verification used the SCID-IV. A repository label does
  not establish present diagnosis, symptom state, medication state, or current
  DSM classification.
- A portion of the parent sample completed the imaging sessions. The exact
  participant-modality manifest controls every proposed subset.

### Imaging, task, and completion grain

- OpenNeuro snapshot `1.0.0`, DOI
  `10.18112/openneuro.ds000030.v1.0.0`, is pinned to repository commit
  `4070b6eea231517bfeff42527a46d9d166ac4e13`.
- The source metadata documents 3 T Siemens TrioTim acquisition, T1w MPRAGE,
  64-direction DWI, BOLD fMRI, rest with physiology, breath hold with
  physiology, BART, stop signal, task switching, spatial working memory
  capacity or SCAP, and paired-associate memory encoding and retrieval.
- In the 272-row participant table, availability is 265 T1w, 262 DWI, 268
  rest, 258 breath hold, 263 BART, 266 stop signal, 266 task switch, 268 SCAP,
  207 PAM encoding, and 208 PAM retrieval.
- These modality counts do not define one multimodal complete-case cohort.
  Intersections must be calculated only during an approved participant-level
  workflow.
- The repository records a non-MRI stop-signal training run separately from
  the in-scanner task. Preserve that run distinction.
- Candidate claims about face-memory or monetary-incentive fMRI tasks are not
  supported by the pinned source inventory and must not be introduced.

### Quality, timing, and product grain

- The README reports that around 20 percent of included T1w images show a
  headset-related aliasing ghost that may overlap one or both temporal lobes.
  A dataset flag is not a substitute for analysis-specific image QC.
- PAM missingness is elevated because data collected before an early task
  design change were excluded.
- When scanner trigger time was available, event onsets were corrected for
  trigger delay. The source retains uncompensated onset values and documents
  an eight-second, four-TR prescan discrepancy.
- When no trigger was available, the README describes only an estimated
  prescan time. Do not mix corrected, uncompensated, and estimated timing.
- T1w images were defaced. Defacing lowers one identification risk but does not
  make the multimodal record anonymous or ethically unconstrained.
- Raw snapshot data, repository summary derivatives, and the separately
  described historical preprocessing release are distinct products. Never
  merge their methods, versions, exclusions, or provenance.

## Design choices and verification

Separate the parent population from the distributed sample before comparing
UCLA CNP routes. Check the Source and Population Card, Grain Map and
Applicability Matrix against the question's source, cohort, diagnosis or
phenotype, modality, task, timing and product requirements. Show conflicts
and unknowns in the Threat Register, including unresolved intersections of
those requirements. For an unresolved choice, present only compatible routes. If a single route is
defensible, explain why it fits.

After Gate 2, prepare and verify only the selected Dataset Suitability and
Access Specification. Stop before data access, selection, validation,
processing or analysis.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) for an approved population, construct, task,
  missingness, comparison, or evaluation-design question.
- Offer [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded evidence search.
- Route BIDS, preprocessing, QC, harmonization, modeling, or analysis only
  after the user selects the design and an appropriate owner exists.

Never chain automatically.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *ds000030* (Version 1.0.0) [Data set]. (n.d.). OpenNeuro. https://doi.org/10.18112/openneuro.ds000030.v1.0.0
- Gorgolewski, Durnez, & Poldrack (n.d.). Preprocessed Consortium for Neuropsychiatric Phenomics dataset (Version 2). *F1000Research*. https://doi.org/10.12688/f1000research.11964.2
- Poldrack et al. (2016). A phenome-wide examination of neural and cognitive function. *Scientific Data*. https://doi.org/10.1038/sdata.2016.110
