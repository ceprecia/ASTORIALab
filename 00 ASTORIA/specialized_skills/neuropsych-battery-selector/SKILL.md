---
name: neuropsych-battery-selector
description: >-
  Compares exact neuropsychological research measures and battery configurations
  for one user-approved construct map, outcome role, population, language and
  cultural context, design, timepoint, setting, and burden boundary, then
  produces a version-locked Neuropsych Research Battery Specification after two
  approval gates. Use when the request, or a part coordinator, hands over an
  explicitly matching prospective group-research question. Triggers: choose a
  neuropsychological battery, which cognitive measures for this construct.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: behavior
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Neuropsychological Battery Selector

Compare prospective neuropsychological research measures without turning a research protocol into an individual clinical evaluation.

## Purpose

It exposes construct coverage, task impurity, score-specific psychometrics, repeated-measure effects, fairness, accessibility, burden, redundancy, rights, qualifications, test security, and data-export limits without generating a deficit profile, choosing the question or outcome, administering or reproducing tests, calculating or interpreting scores or norms, selecting cutoffs, diagnosing, acquiring instruments, analyzing data, or saving without separate approval.

`neuropsych-battery-selector` is the conditional Part 3 owner for comparing exact neuropsychological research measures and battery configurations after the user approves what constructs and scores the study needs. It may integrate an already selected Theory of Mind or social-cognition component into a larger battery, but [tom-task-selector](../tom-task-selector/SKILL.md) owns that component's task-family and version comparison.

It owns:

- translating one approved Construct and Outcome Map into measure requirements;
- comparing two to four exact measure or battery configurations when credible;
- exposing construct coverage, task impurity, score-specific psychometrics, fairness, accessibility, repeated-measure effects, burden, redundancy, rights, qualifications, security, and export constraints;
- producing a version-locked Neuropsych Research Battery Specification from only user-selected elements.

The user owns the question, hypothesis, prediction, constructs, outcome roles, scores, estimands, timepoints, population, interpretation, confirmatory status, clinical relevance, primary outcome, battery selection, and final decisions.

Activate only when:

- The user invokes the exact trigger `neuropsych-battery-selector`; or
- a verified Active capability hands off a bounded prospective group-research measure-selection question with approved constructs and outcome roles.

Do not activate from `neuropsych`, `cognitive testing`, `test battery`, `memory test`, `clinical assessment`, a condition name, a score, or a suspected deficit.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the battery-versus-custom-task question, construct, or broad measurement architecture remains undecided. Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, schedule, order, and counterbalancing.

One run covers one prospective research protocol, population, language and cultural context, setting, timepoint structure, and approved construct map.

In scope:

- group-level observational, experimental, longitudinal, or intervention research;
- clinical cohorts only when the purpose is group research, authorized human administration is independently secured, and no individual decision is made;
- audit of a proposed battery using public or lawfully authorized metadata, manuals, technical reports, and measurement evidence.

Stop and route to qualified licensed, institutional, or legal expertise for:

- a named individual, patient, or participant's score or profile;
- diagnosis, differential diagnosis, treatment, rehabilitation, clinical feedback, capacity, disability, fitness, return-to-work, forensic, legal, or presurgical decisions;
- test administration, scoring, norm calculation, cutoff selection, performance-validity, effort, response-bias, or malingering judgments;
- acquisition, credentialing, protected-content access, or interpretation of incidental clinical findings.

This skill never generates an expected deficit profile or selects measures because they are said to match a diagnosis.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied question, hypothesis, prediction, or protocol objective |
| Construct map | Each approved construct and what is outside its boundary |
| Outcome roles | Primary, secondary, covariate, exploratory, descriptive, manipulation check, or another role |
| Scores and estimands | Exact planned score variable, contrast, parameter, and generalization target |
| Design and timepoints | Cross-sectional or repeated structure, interval, prior exposure, and approved schedule |
| Population | Age, clinical or developmental context, language, dialect, culture, education quality, literacy, and sampling |
| Accessibility | Communication, vision, hearing, motor, fatigue, distress, device, and accommodation needs |
| Setting and mode | In person, remote, paper, digital, site, device, staff, and supervision |
| Candidate boundary | Exact measures, editions, forms, languages, platforms, or configurations allowed for comparison |
| Evidence boundary | Public or lawfully authorized sources and approved search scope |
| Constraints | Time, burden, cost, equipment, training, qualification, security, export, and site limits |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Stop point | Chat-only comparison or separately approved handoff |

Mark essential missing facts `unknown`. Do not fill them with the external candidate's deficit profiles, test catalog, universal battery, timings, norms, cutoffs, condition recommendations, or availability claims.

## Steps

### 1. Build the Construct and Outcome Map

For every approved construct show:

| Field | Required content |
|---|---|
| Construct | Exact theoretical target |
| Included process | What the proposed score may represent |
| Excluded process | What it must not be said to represent |
| Outcome role | Primary, secondary, covariate, exploratory, or another approved role |
| Score and estimand | Exact planned variable, contrast, parameter, and level |
| Timepoint | Baseline, repeated visit, endpoint, or another role |
| Generalization | People, languages, sites, occasions, or settings |
| Prohibited inference | Diagnostic, clinical, localization, deficit, or other unsupported claim |

If the user has not chosen the construct or outcome role, stop or return the
architecture question to [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md).

### 2. Gate 1: approve comparison and evidence scope

Show the Construct and Outcome Map, population and setting boundary, candidate
measures, exact evidence sources, comparison criteria, protected-content rule,
and specialist gaps.

Gate 1 authorizes only bounded metadata and evidence review plus option
comparison. It does not authorize selection, acquisition, credentialing,
administration, scoring, interpretation, norm use, search outside the displayed
boundary, power, analysis, saving, or participant contact.

Repeat Gate 1 after any material change in construct, score, role, population,
language, setting, timepoint, mode, candidate, evidence, or outcome visibility.

### 3. Build Measure Evidence Records

| Field | Required content |
|---|---|
| Candidate ID | Stable label |
| Measure identity | Exact owner, edition, form, language, platform, mode, and version |
| Construct and demands | Intended process plus task impurity and access demands |
| Score | Exact variable, scale, direction, role, and estimand fit |
| Evidence applicability | Score, use, population, language, form, mode, timepoint, and setting |
| Psychometrics | Reliability, precision, error, validity, floor, ceiling, and range |
| Repeated use | Exposure, retest, practice, responsiveness, alternate-form, and interval evidence |
| Fairness and access | Culture, education, literacy, language, sensory, motor, communication, and accommodation |
| Feasibility | Time, burden, cost, equipment, staff, training, scoring, and export |
| Rights and security | License, qualification, use, reproduction, remote, recording, translation, storage, and supply |
| Conflicts and gaps | Vendor interest, disagreement, indirect evidence, or missing fact |
| Status | Eligible, eligible with validation, specialist-required, unresolved, or reject |

Use public or lawfully authorized documentation only. Never copy protected
content into the record.

### 4. Build the Battery Evidence Matrix

Create two to four labeled configurations only when credible. Compare:

- construct and score coverage;
- task impurity, shared-method variance, and incremental information;
- score-specific psychometrics and intended-use fit;
- population, language, culture, fairness, and accessibility;
- repeated-measure and longitudinal suitability;
- mode, site, device, software, and version stability;
- floor, ceiling, range, missingness, and data export;
- burden, fatigue, distress, staffing, cost, and training;
- rights, qualifications, security, supply, and feasibility;
- residual gaps and forbidden inferences.

Do not calculate a composite rank or name a universal best battery.

### 5. Build the risk and requirements registers

Create one row per material issue with candidate, evidence, affected score or
inference, severity, detectable indicator, mitigation options, residual risk,
owner, and unresolved decision.

At minimum review construct undercoverage, task impurity, reliability mismatch,
floor or ceiling, population transport, language and cultural equivalence,
education and literacy, sensory and motor access, repeated exposure, mode or
version drift, burden, redundancy, missingness, multiplicity, qualification,
security, rights, and data export.

### 6. Present response options

Offer only defensible actions:

- retain an eligible measure or configuration;
- retain it with an exact validation, pilot, access, rights, qualification,
  accommodation, or specialist condition;
- narrow the construct, score, role, timepoint, or claim;
- compare another user-approved candidate;
- return a decision to the user;
- reject an unsupported configuration;
- select no current battery and preserve the gap.

Never offer a diagnosis, deficit profile, clinical cutoff, patient conclusion,
performance-validity judgment, or automatic battery.

### 7. Gate 2: approve the research battery

Show all records, matrices, risks, unresolved conflicts, response options, and
the exact proposed configuration.

The user selects the measures, versions, forms, languages, platforms, modes,
scores, roles, timepoints, form sequence, conditions, and accepted gaps.
Approval applies only to the displayed configuration.

Repeat Gate 2 after any material change. Approval does not authorize acquisition,
credentialing, administration, scoring, norm use, interpretation, power,
analysis, participant contact, saving, or external action.

### 8. Produce the Neuropsych Research Battery Specification

Record:

- source Construct and Outcome Map and Gate 1 boundary;
- every selected measure's exact owner, edition, form, language, platform,
  mode, version, source, and evidence date;
- exact score, role, estimand, timepoint, sequence, and claim boundary;
- construct coverage, task impurity, redundancy, and method-variance rationale;
- population, culture, language, literacy, education, accessibility, and
  setting boundary;
- score-specific psychometric, retest, practice, responsiveness, floor,
  ceiling, and validation requirements;
- burden, equipment, staff, cost, training, security, rights, qualification,
  storage, and export conditions;
- excluded candidates, unresolved gaps, residual risks, owners, deviations,
  stop conditions, and Gate 2 decision;
- separate Part 4 handoff and save state.

Label it `research protocol specification, not clinical or administration
authorization`.

### 9. Verify and stop

Verify:

- constructs and outcome roles preceded measure selection;
- every measure and score is version-locked and evidence-matched;
- no protected content, norm, cutoff, deficit profile, or diagnostic logic was
  reproduced or inferred;
- fairness, accessibility, repeated use, burden, rights, qualification,
  security, and export conditions are visible;
- only Gate 2 selections were integrated;
- the output stops before acquisition, administration, scoring, interpretation,
  analysis, participant contact, or saving.

Return `blocked` when a consequential evidence, access, rights, qualification,
security, or fairness requirement remains unresolved.

## Boundaries

Never request, quote, transcribe, store, transform, upload, generate, or reveal:

- test items, stimuli, instructions, administration scripts, forms, response options, answer keys, scoring algorithms, scoring or normative tables;
- restricted manual text, protected screenshots, platform credentials, or participant data;
- copyrighted translations, alternate forms, record forms, or embedded test content from an article or repository.

`Found online`, `academic use`, `free`, `open access`, or repository MIT licensing does not establish test permission. Open licensing for an article does not license embedded instruments, manuals, supplements, or vendor assets.

For every exact measure, form, score, and configuration:

1. identify owner, edition, form, language, platform, mode, source, date, and evidence version;
2. label evidence `direct`, `bounded adaptation`, `measure-family only`, `vendor claim`, `conflicting`, `unverified candidate`, or `unknown`;
3. match reliability, precision, error, and validity evidence to the exact score, intended use, population, language, mode, timepoint, and estimand;
4. separate task familiarity and domain labels from use-specific validity;
5. distinguish a robust within-person or group effect from reliable individual-difference measurement;
6. inspect floor, ceiling, range, missingness, prior exposure, retest, practice, responsiveness, alternate-form, and mode effects when applicable;
7. disclose vendor funding, conflicts of interest, marketing-only claims, and missing independent evidence;
8. verify current rights, qualifications, security, use, reproduction, adaptation, translation, remote, recording, export, and supply terms;
9. preserve disagreements and return `no current configuration meets the evidence, fit, and rights requirements` when appropriate.

Do not use a universal reliability threshold, validity label, test hierarchy, core battery, duration, break schedule, norm adjustment, cutoff, or number of measures.

Edge cases:

- **No approved construct:** stop before test comparison.
- **Condition or suspected deficit supplied:** use it only as population
  context; do not generate a deficit profile or condition battery.
- **Score supplied:** do not interpret it; prospective metadata review may
  continue only after the score is excluded from view.
- **Ambiguous edition, form, language, or platform:** return an identity gap.
- **Older evidence for a newer edition:** mark indirect; do not transfer it.
- **Open article with a reproduced form:** do not infer test permission.
- **Translation without adaptation evidence:** return equivalence and rights
  gaps.
- **Raw group score with no norms:** norms may be unnecessary, but score-level
  validity and reliability remain required.
- **Total-score evidence for a planned subscore or difference:** reject the
  evidence transfer.
- **Remote or device change:** require exact equivalence and version review.
- **Longitudinal protocol:** expose practice, prior exposure, alternate-form,
  responsiveness, interval, floor, ceiling, and mode stability.
- **No qualified user or lawful access:** stop; do not substitute another test.
- **Race-corrected norms:** stop automatic correction and return the fairness
  and norm decision to qualified owners.
- **Post-registration change:** preserve the deviation and exploratory status.
- **No suitable configuration:** return the gap without creating a battery.

Limits:

- This is a research measure comparator, not a clinical neuropsychology,
  administration, scoring, interpretation, norm, diagnosis, or acquisition
  skill.
- Public evidence cannot replace proprietary manuals, qualified judgment,
  institutional policy, IRB requirements, or exact current license terms.
- It cannot establish that a battery isolates a construct, is culturally fair,
  or supports an individual decision.
- Version, platform, vendor, qualification, and rights information can change
  and requires current verification for each use.

## Measure coverage and conditions of use

Trace each exact measure or battery configuration from the Construct and
Outcome Map through the Measure Evidence Records, Battery Evidence Matrix,
and Coverage and Impurity Map. Compare evidence-compatible configurations
when a selection remains open. Explain the evidence for a sole defensible
configuration and keep the option to select none.

Use the Psychometric Register, Repeated-Measure Register, Burden and
Accessibility Register, and Rights, Qualification, Security, and Export
Checklist to show the limits and conditions of each viable configuration.
After Gate 2, record only the user's selected measures, forms, scores,
roles, timepoints, conditions, and gaps in the Neuropsych Research Battery
Specification. Stop before acquisition or administration.

> [!info] References
> Read `./references/design_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- custom task or battery-versus-task architecture: [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md)
- Theory of Mind or social-cognition component selection before battery integration: [tom-task-selector](../tom-task-selector/SKILL.md)
- factors, units, allocation, schedule, order, and counterbalancing:
  [experimental-design](../../skills/experimental-design/SKILL.md)
- cognitive and behavioral power inputs: `cogsci-power-analysis`
- numerical power calculation: `statistical-power`
- bounded evidence discovery: `paper-search`
- one bounded measurement-claim audit: `research-literacy`
- scoring-derived data, composites, invariance, missingness, multiplicity,
  longitudinal modeling, and inference: the selected Part 4 method owner
- access, administration, clinical feedback, and incidental findings:
  qualified neuropsychology, publisher, institution, IRB, and clinical owners

Verify every Active destination in the live [Skill Map](../../Skill%20Map.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- American Academy of Clinical Neuropsychology. (2021). *Position statement on race norms*.
- American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*.
- Boone et al. (2022). Official position of the American Academy of Clinical Neuropsychology on test security. *The Clinical Neuropsychologist*. https://doi.org/10.1080/13854046.2021.2022214
- Calamia, Markon, & Tranel. (2012). Scoring higher the second time around. *The Clinical Neuropsychologist*. https://doi.org/10.1080/13854046.2012.680913
- Hedge, C., Powell, G., & Sumner, P. (2018). The reliability paradox: Why robust cognitive tasks do not produce reliable individual differences. *Behavior Research Methods, 50*. https://doi.org/10.3758/s13428-017-0935-1
- International Test Commission. (2014). *Statement on the use of tests and other assessment instruments for research purposes* (Version 1.2).
- International Test Commission. (2017). *Guidelines for translating and adapting tests* (2nd ed., Version 2.4).
- Nguyen et al. (2024). Neuropsychological application of the International Test Commission guidelines for translation and adapting of tests. *Journal of the International Neuropsychological Society, 30*, 621–634. https://doi.org/10.1017/S1355617724000286
