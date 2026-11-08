---
name: tom-task-selector
description: >-
  Compares candidate Theory of Mind and social-cognition task families for one
  user-supplied construct, intended inference, population, setting, and outcome
  role, then produces a selection-bound ToM Task Specification after two
  approval gates. Use when the request, or a part coordinator, hands over an
  explicitly matching selection question. It deconstructs the Theory of Mind
  umbrella, distinguishes task demands and score meanings, exposes psychometric,
  language, culture, developmental, accessibility, neurodiversity, replication,
  and rights boundaries, and never treats performance as proof that a person or
  group has or lacks a mind, empathy, social understanding, or a clinical
  condition. It does not administer or reproduce task content, choose a
  hypothesis, fix a battery, calculate power, score participants, diagnose,
  analyze data, or save without separate approval. Triggers: choose a theory of
  mind task, social cognition task selection.
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
  updated: "2026-11-02"
---

# Theory of Mind Task Selector

Compare candidate Theory of Mind and social-cognition task families without treating Theory of Mind as one unitary ability or a task score as a property of a person.

## Purpose

`tom-task-selector` is the conditional Part 3 owner for comparing candidate Theory of Mind and adjacent social-cognition task families after the user supplies one bounded construct, intended inference, population, setting, and outcome role. It retains this component-selection ownership when the selected measure will later sit inside a larger neuropsychological battery; [neuropsych-battery-selector](../neuropsych-battery-selector/SKILL.md) may integrate only the already selected component.

It owns:

- deconstructing the broad Theory of Mind label into the component process actually under study;
- comparing candidate task families and versions at the level supported by available evidence;
- separating target-process demands from language, memory, executive, attention, perceptual, motor, cultural, and social-context demands;
- reviewing score meaning, psychometric fit, accessibility, transportability, replication, licensing, and administration constraints;
- producing a selection-bound ToM Task Specification for only the route the user approves.

The user owns the construct, question, hypothesis, prediction, confirmatory status, population, task selection, outcome, estimand, interpretation, claim language, clinical relevance, control measures, power inputs, and final decisions.

Activate only when:

- The user invokes the exact trigger `tom-task-selector`; or
- a verified Active capability hands off an explicitly bounded Theory of Mind or social-cognition task-selection question.

Do not activate from `theory of mind`, `social cognition`, `empathy`, `autism`, `false belief`, `perspective taking`, `mentalizing`, or `select a cognitive task`.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the target process or broad paradigm family remains undecided. Use [infant-looking-time-designer](../infant-looking-time-designer/SKILL.md) only after an infant looking-time family, contrast, and estimand are selected.

One run compares task families or versions for one primary component process, population, setting, and intended use.

This skill does not:

- formulate a hypothesis or infer a person's inner state;
- administer a task, write stimuli, reproduce stories, images, films, answer keys, scoring rubrics, translations, or proprietary manuals;
- prescribe a universal developmental sequence, passing age, normative cutoff, control battery, or number of tasks;
- select a diagnosis, treatment, intervention, accommodation, or eligibility decision;
- score, classify, clean, model, or interpret participant data;
- calculate power, choose sample size, implement software, search beyond the approved evidence boundary, or save without separate approval.

If the user requests individual clinical interpretation, stop and identify the qualified human clinical professional and exact assessment boundary outside ASTORIA.

## Inputs

| Field | Required content |
|---|---|
| Scientific target | user-supplied construct, question, hypothesis, or prediction |
| Component process | Belief reasoning, perspective, mental-state vocabulary, pragmatic inference, real-time use, reflective judgment, implicit response, or another precise target |
| Intended use | Group contrast, within-person change, individual differences, developmental description, intervention outcome, mechanistic test, or another use |
| Outcome role | Primary, secondary, manipulation check, descriptive, screening, or unresolved |
| Population | Age, language, culture, communication, sensory, motor, developmental, clinical, educational, and accessibility context |
| Setting | Lab, school, clinic, home, remote, neuroimaging, EEG, or another context |
| Response demands | Verbal, reading, pointing, button press, eye movement, looking, open response, informant report, or unresolved |
| Candidate boundary | Supplied task families, exact versions, translations, or sources allowed for comparison |
| Evidence boundary | Exact sources that may be inspected and whether bounded search is approved |
| Score and estimand | Proposed score grain, contrast, parameter, and generalization target |
| Constraints | Time, burden, equipment, staffing, training, rights, and qualification limits |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Stop point | Chat-only comparison or separately approved handoff |

Mark essential unknowns `unknown`. Do not fill them from the external candidate's age table, decision tree, task database, norms, or recommendations.

## Component-process map

Use this map to separate targets before comparing tasks. It is not a developmental hierarchy and does not make the families interchangeable.

| Component process | Examples of observable demand |
|---|---|
| Belief reasoning | Predict or explain action from a stated or inferred belief |
| Visual perspective | Represent what another person can see or how a scene appears |
| Mental-state vocabulary | Map words or labels to facial, vocal, or contextual cues |
| Emotion attribution | Infer affect from perceptual or situational information |
| Pragmatic or social inference | Explain irony, indirectness, misunderstanding, or social context |
| Online use | Use another person's information during time-sensitive action or comprehension |
| Reflective judgment | Deliberately explain motives, beliefs, intentions, or knowledge |
| Implicit or spontaneous response | Anticipatory looking, response interference, or another indirect index |
| Naturalistic integration | Interpret temporally extended film, narrative, or interaction |

A task may combine several rows. Describe the combination rather than calling the task a pure measure of Theory of Mind.

## Steps

### 1. Establish the selection boundary

Restate the scientific target, component process, intended use, outcome role,
population, setting, response demands, score and estimand, candidate sources,
constraints, outcome visibility, and stop point.

Explicitly list excluded adjacent processes and claims. If `Theory of Mind` is
the only construct description, return the unresolved component-process
decision before task comparison.

### 2. Gate 1: approve evidence and comparison scope

Show the ToM Selection Brief, candidate families, exact source boundary,
comparison criteria, rights questions, and missing specialist evidence.

Gate 1 authorizes only bounded source inspection, task-family comparison, and
the records below. It does not authorize selection, search outside the shown
boundary, task reproduction, implementation, power, scoring, analysis, saving,
or interpretation.

Repeat Gate 1 after a material change in construct, intended use, population,
setting, candidate family, evidence scope, score, or outcome visibility.

### 3. Build the Construct Boundary Card

| Field | Required content |
|---|---|
| Included process | Exact component under study |
| Excluded processes | Adjacent processes the score must not be said to measure |
| Observable demand | What the participant sees, hears, reads, infers, or does |
| Intended score meaning | Bounded meaning proposed for the exact score |
| Alternative demands | Language, memory, executive, attention, perceptual, motor, and social-context demands |
| Intended inference | Claim the design could test if other requirements hold |
| Forbidden inference | Claims the task cannot establish |
| Population boundary | People, language, culture, setting, and access context |

### 4. Build candidate Task Evidence Cards

Create two to four cards when credible alternatives exist.

| Field | Required content |
|---|---|
| Candidate ID | Stable label |
| Task family and version | Exact task family, version, language, and response mode |
| Component link | Why it could operationalize the approved process |
| Observable and score | Participant demand, score grain, direction, and estimand |
| Non-target demands | Language, memory, executive, perceptual, motor, and cultural demands |
| Evidence | Exact direct, adaptation, conflicting, candidate, or missing source |
| Psychometrics | Reliability and validity evidence matched to intended use |
| Population fit | Direct support, bounded translation, unsupported, or unknown |
| Floor and ceiling | Applicable evidence and uncertainty |
| Replication | Relevant success, failure, dispute, or missing evidence |
| Feasibility | Duration, burden, equipment, training, scoring, and setting |
| Accessibility | Communication, sensory, motor, cognitive, and platform access |
| Rights | Exact license, qualification, modification, and redistribution state |
| Claim limit | What the score cannot establish |

Do not rank candidates by familiarity, popularity, citation count, convenience,
or availability of a published protocol.

### 5. Build the Applicability Matrix

For each candidate show:

- component-process match;
- intended-use and outcome-role match;
- version, language, culture, age, population, and setting match;
- score-grain and estimand match;
- psychometric support at the required level;
- task-demand and accessibility burden;
- replication and interpretation uncertainty;
- rights and qualification feasibility;
- status: `eligible`, `eligible with bounded validation`,
  `specialist-required`, `unresolved`, or `reject`.

Do not collapse the dimensions into a numeric composite or automatic winner.

### 6. Build the threat registers

Create one row per material issue across:

- construct underrepresentation and task impurity;
- language, reading, vocabulary, pragmatic, memory, executive, attention,
  perceptual, emotion-label, face, voice, timing, and motor demands;
- floor, ceiling, restricted range, low trial count, rater dependence,
  practice, carryover, and retest;
- group comparability, measurement invariance, translation, culture,
  communication access, and sampling;
- implicit-task replication, alternative explanations, and estimand ambiguity;
- stigmatizing or deficit-framed inference;
- copyright, licensing, qualification, and redistribution;
- administration fidelity, version drift, and missing validation.

For each show candidate, evidence, affected inference, severity, detectable
indicator, mitigation options, residual risk, owner, and unresolved decision.

### 7. Present response options

Offer only defensible actions:

- retain a candidate for bounded specification;
- retain it only with an exact pilot, validation, translation, rights, or
  specialist condition;
- narrow the component process or intended claim;
- compare an additional approved candidate;
- return the task choice to the user;
- reject an unsupported route;
- stop for missing evidence, rights, clinical qualification, or accessibility
  expertise.

Never present diagnosis, treatment, participant classification, or a fixed
battery as an option.

### 8. Gate 2: approve selection

Show the cards, matrices, registers, unresolved conflicts, response options, and
exact proposed selection.

The user chooses the task family and version, component wording, score role,
controls, validation, rights route, and residual risks. Approval applies only
to the displayed selection.

Repeat Gate 2 after any material change. One approval does not authorize
administration, acquisition, implementation, power, scoring, analysis,
interpretation, search, or saving.

### 9. Produce the ToM Task Specification

Record:

- source Selection Brief and Gate 1 scope;
- approved component process and forbidden inferences;
- selected task family, exact version, language, population, setting, and
  response mode;
- intended score, role, estimand, generalization target, and claim boundary;
- selected controls and what each does and does not control;
- psychometric, floor, ceiling, accessibility, replication, and validation
  requirements;
- rights, qualification, modification, storage, and reporting conditions;
- excluded candidates and reasons;
- unresolved conflicts, residual risks, owners, and stop conditions;
- Gate 2 decision and separate handoff or save state.

Label it `design specification, not administration authorization`.

### 10. Verify and stop

Verify:

- the selected task matches the approved component and intended use;
- task-family evidence was not treated as exact-version evidence;
- no universal age, cutoff, norm, battery, or developmental hierarchy entered;
- no deficit, diagnostic, empathy, or person-level conclusion was encoded;
- confounds, accessibility, psychometrics, replication, and rights are visible;
- only Gate 2 selections were integrated;
- the output stops before task content, implementation, scoring, analysis, or
  interpretation.

Return `blocked` when a consequential requirement remains unresolved. Saving or
handoff requires separate explicit approval.

## Boundaries

Treat `Theory of Mind` as a contested umbrella over partially separable processes and measurement traditions. Never use one score to claim that a person or group:

- lacks a mind, Theory of Mind, empathy, social understanding, morality, or self-awareness;
- is mind-blind, deficient in humanity, or incapable of relationships;
- has or does not have autism, another diagnosis, or a clinical impairment;
- failed to develop along a universal hierarchy.

For autistic participants:

- use identity language and construct framing supplied or approved by the user and the relevant community or study protocol;
- preserve heterogeneity and communication, sensory, language, motor, and context differences;
- include bidirectional interaction and double-empathy explanations when applicable;
- never treat nonautistic behavior as the unexamined gold standard;
- distinguish performance on a specific task version from everyday social communication or mutual understanding.

Participant-informed and neurodiversity-respecting design is an evidence and ethics requirement, not a cosmetic wording step.

For every task family, version, translation, and score:

1. identify the exact source, version, language, population, setting, and use;
2. label evidence `direct`, `bounded adaptation`, `task-family only`, `unverified candidate`, `conflicting`, or `unknown`;
3. distinguish construct evidence from administration familiarity;
4. distinguish group-level sensitivity from individual-difference reliability;
5. distinguish score reliability from construct validity and clinical utility;
6. record floor, ceiling, range, missingness, rater, practice, and retest issues;
7. inspect measurement invariance or transport evidence when group comparisons depend on score comparability;
8. preserve disagreements and failed replications;
9. verify exact copyright, license, qualification, translation, and redistribution terms before selection or implementation.

Do not inherit fixed ages, item counts, passing rates, normative means, reliability thresholds, scoring rules, cutoffs, control tasks, or batteries. Evidence for another version, language, population, response mode, or outcome does not transfer automatically.

Edge cases:

- **Only a broad ToM label:** return the component-process decision.
- **One familiar task named:** compare exact-version fit and at least the
  credible alternative of not using it; do not assume selection.
- **Autistic sample:** enforce the construct-respect boundary and show
  communication, sensory, context, heterogeneity, and double-empathy issues.
- **Infant implicit task:** surface replication and estimand disputes, then
  hand selected administration design to [infant-looking-time-designer](../infant-looking-time-designer/SKILL.md).
- **Adult child-version substitution:** treat as a new validation question.
- **Translated task:** require exact translation, adaptation, equivalence,
  rights, and target-population evidence.
- **Clinical screening request:** stop; research-task selection cannot provide
  diagnosis or individual clinical interpretation.
- **Proprietary material supplied:** inspect only metadata and permitted
  excerpts; do not reproduce content.
- **Outcome already seen:** label post hoc selection risk and do not present it
  as prospective or confirmatory.
- **No credible task:** return a gap and specialist route without inventing a
  battery.

Limits:

- This is a comparator and specification skill, not a clinical assessment,
  developmental norm, task manual, implementation, scoring, or analysis skill.
- Exact task versions, translations, permissions, psychometrics, and
  replication evidence can change and require current verification.
- It cannot establish that a task isolates a mental process or that a person
  has or lacks an internal capacity.
- It does not resolve theoretical disputes about Theory of Mind, implicit
  mentalizing, autism, empathy, or social cognition.

## Design facts that control the review

### Construct and task impurity

- Different Theory of Mind measures can show weak convergence even when each is widely used. Do not assume they measure one latent ability.
- False-belief reasoning, emotion recognition, visual perspective, pragmatic inference, and naturalistic social understanding are not substitutes.
- Task performance may depend on receptive and expressive language, reading, vocabulary, memory, executive control, attention, processing speed, face or voice perception, motor response, test familiarity, and motivation.
- A verbal explanation score and an online response can support different claims. Explicit and implicit measures are not difficulty-matched versions of the same construct.
- A physical-control story, vocabulary measure, or executive task can describe an alternative demand but does not automatically purify the target score.

### Development, language, culture, and population

- Do not treat reported age sequences as universal biological stages. Order and performance can vary with task form, language, culture, sampling, teaching, response demands, and scoring.
- A child, adult, translated, shortened, remote, or clinical version is a distinct measurement object until equivalence is supported.
- Avoid age-based routing that assumes what participants can understand or communicate. Record actual access needs and pilot the exact procedure.
- Group differences do not establish a deficit in one group or a universal property of its members.
- Clinical sensitivity is not diagnostic specificity, and research scores are not individual clinical conclusions.

### Psychometrics and interpretation

- Match reliability evidence to the exact score and intended use. Internal consistency may be inappropriate for heterogeneous tasks and does not establish temporal stability or validity.
- For open responses, define coder training, blinding, independent coding, adjudication, and score-level agreement without importing a universal coefficient cutoff.
- Inspect whether the score has enough range for the intended population and whether ceiling, floor, or sparse trials limit inference.
- Norms are dated, sampled, version-specific descriptions. They are not universal cutoffs and do not prove impairment.
- One significant group contrast does not establish construct validity. Nonsignificance does not establish equivalence or absence.

### Implicit measures and replication

- Implicit false-belief and anticipatory-looking findings have substantial replication and interpretation disputes.
- Do not select an implicit task to bypass an explicit-task result or to claim an earlier, automatic, innate, or preserved capacity.
- Looking, response-time, or interference effects require a prespecified estimand and plausible nonmental-state alternatives.
- Route infant exposure, stopping, observation, attrition, and welfare design to [infant-looking-time-designer](../infant-looking-time-designer/SKILL.md) after task-family selection.

### Rights and protected materials

- Treat task photographs, films, stories, drawings, manuals, answer keys, scoring rubrics, norms, and translations as protected unless exact terms say otherwise.
- A citation, online copy, supplement, or published example does not establish permission to reproduce, translate, modify, redistribute, or deploy.
- Record owner, source, version, license, qualification, permitted use, modification, storage, and reporting limits.
- Stop before displaying or reconstructing protected task content.

## Task applicability and claim limits

Use the Construct Boundary Card, Task Evidence Cards, and Applicability
Matrix to judge whether a task family or exact version suits the approved
component process, intended use, population, and setting. Compare only
evidence-compatible candidates when a choice remains. Explain why a sole
defensible candidate fits. If none is defensible, identify the evidence or
applicability gap.

Use the Confound and Accessibility Register, Psychometric Register,
Replication Register, and Rights Register to expose the limits of the
candidate and its use. After Gate 2, record only the user's selections in
the ToM Task Specification. Stop before administration, stimulus
reproduction, power, implementation, scoring, analysis, or interpretation.

## Handoffs

- broader construct-to-paradigm comparison: [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md)
- infant looking-time administration: [infant-looking-time-designer](../infant-looking-time-designer/SKILL.md)
- integration of an already selected ToM component into a larger research battery: [neuropsych-battery-selector](../neuropsych-battery-selector/SKILL.md)
- general design, factors, units, and allocation: `experimental-design`
- cognitive and behavioral power inputs: `cogsci-power-analysis`
- quantitative power calculation: `statistical-power`
- sentence creation and norming: `sentence-stimulus-norming`
- EEG schedule compatibility: `eeg-paradigm-designer`
- fMRI timing compatibility: `fmri-task-design-guide`
- detailed claim audit: `research-literacy`
- bounded source discovery: `paper-search`

Verify each destination in the live [Skill Map](../../Skill%20Map.md) before handoff.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Gernsbacher & Yergeau (2019). Empirical failures of the claim that autistic people lack a theory of mind. *Archives of Scientific Psychology*. https://doi.org/10.1037/arc0000067
- Kulke, von Duhn, Schneider, & Rakoczy (2018). Is implicit theory of mind a real and robust phenomenon? Results from a systematic replication study. *Psychological Science*. https://doi.org/10.1177/0956797617747090
- Olderbak et al. (2015). A psychometric analysis of the Reading the Mind in the Eyes Test. *Frontiers in Psychology*. https://doi.org/10.3389/fpsyg.2015.01503
- Schaafsma, Pfaff, Spunt, & Adolphs (2015). Deconstructing and reconstructing theory of mind. *Trends in Cognitive Sciences*. https://doi.org/10.1016/j.tics.2014.11.007
- Warnell & Redcay (2019). Minimal coherence among varied theory of mind measures in childhood and adulthood. *Cognition*. https://doi.org/10.1016/j.cognition.2019.06.009
