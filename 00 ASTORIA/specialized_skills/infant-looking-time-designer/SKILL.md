---
name: infant-looking-time-designer
description: >-
  Compares and specifies one already-selected infant looking-time administration
  for one user-approved construct, paradigm family, estimand, contrast, age
  range, population, and setting, then produces a selection-bound Infant
  Looking-Time Paradigm Specification after two approval gates. Use when the
  request, or a part coordinator, hands over an explicitly matching design question.
  Triggers: design an infant looking time study, looking time paradigm
  administration.
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

# Infant Looking-Time Designer

Specify one infant looking-time administration without treating longer looking,
novelty, familiarity, surprise, or habituation as a one-to-one measure of
infant knowledge.

## Purpose

It makes familiarization or habituation logic, trial and event structure, stopping behavior, stimulus position and order, attention recentering, caregiver and coder blinding, looking definition, recording mode, inclusion and exclusion, data loss, attrition, online-versus-lab context, reliability, infant welfare, privacy, and pilot validation visible without choosing the hypothesis or paradigm family, fixing universal timing or habituation thresholds, calculating power, implementing or running the study, analyzing looking data, inferring infant knowledge from longer looking, or saving without separate approval.

`infant-looking-time-designer` is the conditional Part 3 owner for translating
one already-approved infant looking-time paradigm family, construct, estimand,
contrast, age range, population, and setting into an administration and
validation specification.

It owns familiarization or habituation flow; session, phase, trial, event, and
look ontology; infant-controlled or fixed exposure routes; stopping behavior;
stimulus position and order; attention recentering; caregiver and coder
blinding; looking definition; live, offline-video, eye-tracker, or webcam
recording routes; prespecified inclusion and exclusion; data-loss and attrition
records; welfare stops; and pilot validation.

It does not choose habituation, preferential looking, violation of expectation,
or another paradigm; generate a hypothesis; choose the estimand or outcome;
calculate power; select an analysis; implement, recruit, collect, code, or
interpret data.

Activate only when:

- The user invokes the exact trigger `infant-looking-time-designer`; or
- a verified Active capability hands off one already-selected infant
  looking-time paradigm with an explicit construct, estimand, contrast, age
  range, population, and setting.

Do not activate from `infant study`, `baby looking`, `habituation`,
`preferential looking`, `surprise`, `eye tracking`, `online infants`, or
`analyze looking time`.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the paradigm family or construct-to-
method mapping remains undecided. Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors,
units, allocation, and general counterbalancing. Route participant, item,
trial, attrition, and operating-characteristic planning to
[cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) and [statistical-power](../../skills/statistical-power/SKILL.md).

This skill supports one visual or audiovisual infant looking-time
administration in a laboratory or explicitly selected remote setting.

It excludes:

- general eye-movement, saccade, fixation-dynamics, pupillometry, or
  gaze-contingent method design;
- clinical screening, developmental diagnosis, or individual assessment;
- stimulus creation, animation, recording, or licensing;
- eye-tracker acquisition, calibration execution, preprocessing, and analysis;
- recruitment, consent, compensation, video collection, coding, or deployment.

If the requested outcome requires spatial gaze coordinates rather than
condition-level looking, preserve the infant administration boundary and
route eye-tracking measurement and analysis separately.

## Inputs

Handle one administration at a time.

| Field | Required content |
|---|---|
| Approved paradigm | Habituation, familiarization-test, preferential looking, VoE, or another precisely defined family selected by the user |
| Construct and estimand | user-supplied construct, looking measure, contrast, and intended inference |
| Population | Age range, developmental context, sensory and motor access, language exposure, clinical exclusions, and generalization target |
| Stimuli and events | Exact source, modality, physical properties, event sequence, versions, and rights state |
| Setting | Laboratory, moderated remote, unmoderated remote, or another approved context |
| Recording route | Live observer, offline video, eye tracker, webcam, or unresolved comparison |
| Evidence | Exact prior paradigm, methods, hardware, platform, or local design source |
| Stop point | Chat-only specification or separately approved handoff |

If the paradigm family, estimand, contrast, age range, or setting is absent,
identify the missing owner-level decision and stop.

## Steps

### 1. Establish the infant-design boundary

Restate the approved paradigm, construct, estimand, contrast, age and
population, stimuli, setting, recording route, intended interpretation, rights,
welfare and privacy boundary, exclusions, and unresolved choices.

### 2. Gate 1: approve the evidence and comparison boundary

Present:

1. approved paradigm, estimand, contrast, and inference boundary;
2. exact sources, stimuli, systems, and rights;
3. exposure, event, looking, stopping, recording, exclusion, reliability, and
   setting fields to inspect;
4. credible administration routes;
5. fixed owner-level decisions and unresolved choices;
6. power, recruitment, collection, analysis, and privacy exclusions.

Gate 1 authorizes only the displayed design review. It does not authorize a
new hypothesis, paradigm choice, stimulus use, sample size, recruitment,
consent, video collection, task implementation, coding, analysis, external
upload, deployment, or saving.

Reopen Gate 1 after a material paradigm, estimand, population, stimulus,
setting, recording, source, welfare, or privacy change.

### 3. Build the Interpretation Boundary Card

Record the observable looking measure, comparison, what it can show, what it
cannot show, perceptual and conceptual alternatives, novelty and familiarity
alternatives, owner-approved directional prediction, and conditions that would
block interpretation.

### 4. Build the Event and Look Ontology

For each session, phase, trial, event, and look state, record:

- identifier, condition, role, preceding exposure, and order;
- stimulus position and physical properties;
- trial start, attention recentering, look start and end, away state, response,
  stopping event, and timeout behavior;
- live versus final measurement source;
- missing, invalid, pause, caregiver-interference, technical-failure, abort,
  and restart states;
- later analysis requirement without choosing it.

### 5. Build the Administration Route Matrix

| Route | Exposure logic | Looking measure | Blinding | Setting and device | Strength | Threats and unknowns |
|---|---|---|---|---|---|---|
| Route A | | | | | | |
| Route B | | | | | | |
| Fixed route | | | | | | |

Compare only routes compatible with the approved paradigm. Do not rank them.

### 6. Build the Exclusion, Attrition, and Reliability Plan

Specify prospective trial and participant criteria, reason codes, counts at
each stage, condition balance, stopping-before-exclusion distinction,
caregiver and technical events, coder training, blinding, independent
double-coding selection, outcome-aligned reliability, adjudication, and
retention of disagreements.

### 7. Build the Threat and Pilot Register

At minimum assess:

- perceptual versus conceptual differences;
- novelty, familiarity, exposure, fatigue, state, and order;
- side or position, stimulus assignment, caregiver cues, and observer cues;
- unequal exposure under infant-controlled rules;
- outcome-linked stopping or exclusion;
- selective attrition and small effective cells;
- live, video, eye-tracker, and webcam measurement disagreement;
- calibration, geometry, lighting, distance, latency, data loss, and privacy;
- age, sensory or motor access, language, culture, clinical, and developmental
  generalization;
- repeated testing, sibling or household exposure, and platform differences;
- welfare stops and distress.

Pilot stimulus salience, event flow, duration routes, caregiver instructions,
measurement agreement, data loss, stopping behavior, infant tolerance, and the
exact target configuration. Retain failures.

### 8. Gate 2: select the administration

Present the interpretation card, ontology, route matrix, exclusion and
attrition plan, reliability plan, threat register, pilot plan, evidence labels,
limitations, and handoffs.

The user selects exposure and stopping logic, event flow, position and order,
looking definitions, caregiver and coder blinding, recording route, exclusions,
reliability evidence, setting, pilot scope, unresolved items, and next stop.

Gate 2 authorizes only the Infant Looking-Time Paradigm Specification. It does
not authorize sample size, recruitment, consent, asset use, task code, video or
gaze collection, coding, preprocessing, analysis, interpretation, deployment,
or saving.

### 9. Produce the Infant Looking-Time Paradigm Specification

Return:

1. approved paradigm, construct, estimand, contrast, age, and population;
2. inference and longer-looking interpretation boundary;
3. stimuli, source, modality, physical-property, and rights states;
4. session, phase, trial, event, and look ontology;
5. selected exposure, stopping, position, order, and recentering behavior;
6. caregiver, observer, coder, and recording plan;
7. prospective exclusions, attrition accounting, data-loss states, and
   reliability plan;
8. setting, device, geometry, privacy, welfare, and validation requirements;
9. assumptions, unknowns, exclusions, and residual risks;
10. user-selected choices and rejected routes;
11. separately approved handoff or explicit stop.

### 10. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- paradigm, estimand, contrast, age, and setting came from the user or an approved
  handoff;
- exposure, looking, preference, and interpretation remain distinct;
- no universal timing, habituation, exclusion, attrition, coder, or platform
  default was inherited;
- perceptual novelty and conceptual interpretation remain distinct;
- trial stopping and participant exclusion remain distinct;
- recruited, completed, valid, excluded, and analyzed counts remain distinct;
- caregiver and coder blinding, welfare, and video privacy are explicit;
- exact-setting validation is required;
- both gates bound their authorization;
- no power, implementation, collection, analysis, or conclusion occurred.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The user owns the question, hypothesis, prediction, confirmatory status, paradigm
family, construct, estimand, contrast, preference interpretation, age range,
population, setting, factors, stopping and exclusion rules, power inputs,
analysis, and final selections.

This skill:

- never equates longer looking with surprise, novelty, preference, knowledge,
  violation detection, or a specific representation;
- never chooses an expected direction from infant age alone;
- never assigns universal timing, habituation, exclusion, attrition, or coder
  thresholds;
- gives infant comfort and a caregiver- or experimenter-initiated stop priority
  over completion;
- treats face video, voice, gaze, caregiver speech, and home-background
  recordings as sensitive human data;
- never uploads recordings or unpublished stimuli to an external service;
- records stimulus, sound, animation, software, and platform rights;
- stops when welfare, consent, privacy, safety, or asset rights are unresolved.

For every proposed choice:

1. label it `direct evidence`, `bounded adaptation`, `design-derived`,
   `candidate for pilot`, or `unknown`;
2. record source, version, age, population, stimulus, paradigm, setting,
   recording route, and applicability;
3. distinguish exposure, looking, preference score, and scientific inference;
4. distinguish live stopping from final offline or device-derived outcomes;
5. preserve conflicting practices and known replication limits;
6. give no fixed parameter priority because it is conventional;
7. require a target-setting pilot.

Do not inherit universal familiarization trials, habituation baselines or
decrements, sliding windows, maximum or minimum trials, trial durations,
look-away rules, attention-getter timing, intertrial intervals, preference
cutoffs, effect sizes, exclusions, attrition rates, over-recruitment multipliers,
double-coding proportions, reliability cutoffs, screen distance, or platform.

Edge cases:

- **Only `infant looking` is supplied:** do not activate or choose a paradigm.
- **Longer looking is called knowledge or surprise:** restore the observable
  and alternative interpretations.
- **A universal 50-percent habituation rule is requested:** compare only
  applicable evidence-backed routes.
- **Failure to habituate is an automatic exclusion:** expose the induced
  population and selection consequence.
- **Fixed age timing is requested:** require task-, stimulus-, population-, and
  setting-specific evidence.
- **A 55-percent preference is called meaningful:** route the estimand and
  operating characteristics to the analysis and power owners.
- **Live coding is treated as ground truth:** distinguish trial control from
  final outcome measurement.
- **Online is assumed equivalent to laboratory testing:** require exact-setting
  validation and preserve environmental and privacy differences.
- **Caregiver blinding conflicts with infant safety:** safety prevails and the
  design is revised or blocked.
- **Video is proposed for external AI coding:** stop for explicit privacy,
  consent, governance, validation, and vendor authority.
- **No defensible administration:** return a blocked specification.

This skill cannot prove that looking indexes a particular representation,
predict infant tolerance or attrition, calculate power, validate a camera or
eye tracker, establish coder accuracy, authorize child research, or guarantee
that a later implementation preserves the specification.

## Design facts that control the review

### Paradigm, exposure, and interpretation

- Habituation, familiarization-test, preferential-looking, and VoE designs
  create different exposure histories and support different contrasts.
- Fixed and infant-controlled exposure are not interchangeable. A criterion can
  make exposure amount and trial count depend on the infant's prior looks.
- A decrement rule is an operational stopping rule, not proof that a stimulus
  was fully encoded or that a cognitive representation exists.
- Novelty and familiarity preferences can vary with exposure, stimulus
  complexity, task, age, state, and population. Direction must be justified
  prospectively and interpreted cautiously.
- Expected and unexpected events can differ in perceptual novelty as well as
  conceptual structure. Recent meta-analytic evidence shows these contributions
  can be partly independent.
- A null preference does not establish absence, and a directional preference
  does not uniquely identify its mechanism.

### Observation and recording

- Define looking, away, center, left, right, valid trial, missing sample,
  fussiness or disengagement, caregiver interference, and technical failure at
  the measurement grain used by the selected recording route.
- Live observation can control trial flow but need not be the final outcome.
  Offline coding, eye tracking, and webcam coding have different uncertainty,
  data-loss, and blinding profiles.
- Prespecify caregiver instructions, what the caregiver can see or hear, and
  how caregiver behavior is prevented, recorded, or adjudicated. Never
  compromise infant safety or caregiver access.
- If an eye tracker is selected, record device and software version, signal,
  sampling behavior, geometry, calibration and validation plan, measurement
  uncertainty, data loss, and synchronization. This skill does not choose or
  execute preprocessing.

### Exclusion, reliability, and setting

- Trial and participant exclusions must be prospective, reason-coded, and
  reported by condition and stage. Excluding failure to meet an outcome-linked
  habituation rule can change the inferential population.
- Keep recruited, started, completed, technically valid, behaviorally valid,
  excluded, and analyzed counts distinct. Attrition may be selective.
- Specify coder blinding, training evidence, independent double-coding sample,
  disagreement adjudication, and a reliability measure aligned to the final
  outcome. No universal percentage or coefficient proves validity.
- Laboratory, moderated remote, and unmoderated remote procedures differ in
  screen, distance, lighting, distraction, caregiver behavior, latency, video,
  and privacy. Validate the exact task and configuration.

## Looking behavior and interpretation limits

Use the Interpretation Boundary Card to say what the observed looks can
support and the Event and Look Ontology to define how those looks are
identified. In the Route Matrix, compare evidence-compatible exposure,
trial-control, position, order, observation, blinding, exclusion, and
setting choices only where they remain open. Explain why a sole defensible
route fits. Use the Exclusion and Attrition Plan, Reliability Plan, and
Threat Register to document how those choices affect the evidence.

After Gate 2, record only the user's selections in the Infant Looking-Time
Paradigm Specification. Stop before recruitment, collection, coding,
preprocessing, analysis, or interpretation.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) for paradigm-family selection.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, and general
  counterbalancing.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) and [statistical-power](../../skills/statistical-power/SKILL.md) for participants,
  items, trials, attrition, reliability, and operating characteristics.
- Route stimulus production, eye-tracker acquisition, implementation,
  recruitment, consent, coding, preprocessing, analysis, and reporting only
  after the relevant design is selected.

Never chain automatically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Bacon, Weaver, & Saffran (2021). https://doi.org/10.3389/fpsyg.2021.703839
- Dunn et al. (2024). [Eye-tracking reporting guidelines, 2023 edition]. https://doi.org/10.3758/s13428-023-02187-1
- Frank et al. (2017). https://doi.org/10.1111/infa.12182
- Kucharský et al. (2024). Habituation, part II. https://doi.org/10.1002/icd.2383
- Kunin et al. (2024). Perceptual and conceptual novelty independently guide infant looking behaviour. https://doi.org/10.1038/s41562-024-01965-x
- Oakes (2010). Using habituation of looking time to assess mental processes in infancy. https://doi.org/10.1080/15248371003699977
- Oakes (2017). https://doi.org/10.1111/infa.12186
- Scott & Schulz (2017). [Lookit, Part 1]. https://doi.org/10.1162/opmi_a_00002
- Zettersten, Pomper, & Saffran (2022). https://doi.org/10.1002/icd.2326
