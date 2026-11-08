---
name: self-paced-reading-designer
description: >-
  Compares and specifies one already-selected visual self-paced-reading
  administration for one user-approved construct, manipulation, contrast,
  population, and item set, then produces a selection-bound SPR Design
  Specification after two approval gates. Use when the request, or a stage
  coordinator, hands over an explicitly matching design question. It makes reveal
  mode, segmentation, geometry, rereading, critical and downstream regions,
  response mapping, probe and filler logic, platform constraints, event fields,
  pilot checks, and reliability threats visible without choosing self-paced
  reading over another method, writing or norming stimuli, choosing factors or
  allocation, calculating power, programming the task, cleaning reading times,
  modeling, interpreting, or saving without separate approval. Triggers: design
  a self paced reading study, self paced reading administration.
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

# Self-Paced Reading Designer

Specify one visual self-paced-reading administration without treating
segmentation, spillover, comprehension probes, or online timing as fixed
recipes.

## Purpose

`self-paced-reading-designer` is the conditional Part 3 owner for translating
one already-approved visual self-paced-reading task, construct, manipulation,
contrast, population, and item set into a reveal, region, response, probe,
filler, event, platform, and pilot specification.

It owns cumulative versus noncumulative presentation, spatially preserved
versus fixed-position reveal, word or phrase units, rereading policy, display
geometry, item-region mapping, theory-justified downstream regions, neutral
continuation, comprehension-probe and filler behavior, response and event
fields, target-platform constraints, and administration validation.

It does not choose self-paced reading over eye tracking, maze, RSVP,
acceptability, or another task; generate the hypothesis; write or norm
sentences; choose general factors, allocation, or lists; calculate power;
program the task; trim or transform reading times; fit a model; or interpret
results.

Activate only when:

- The user invokes the exact trigger `self-paced-reading-designer`; or
- a verified Active capability hands off one already-selected visual
  self-paced-reading administration with an explicit construct, manipulation,
  contrast, population, and item state.

Do not activate from `reading task`, `sentence processing`, `reading time`,
`eye tracking`, `maze`, `self-paced listening`, `analyze reading times`, or
`make language stimuli`.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the construct-to-task mapping or SPR
versus another paradigm remains undecided. Use [experimental-design](../../skills/experimental-design/SKILL.md) for
factors, units, allocation, and general counterbalancing. Use
[sentence-stimulus-norming](../sentence-stimulus-norming/SKILL.md) for sentence construction, lexical or syntactic
matching, plausibility, cloze, acceptability, familiarity, and norming.

This skill supports one already-selected visual moving-window or cumulative
self-paced-reading administration.

It excludes:

- self-paced listening and audiovisual presentation;
- eye tracking, maze, RSVP, lexical decision, acceptability, and recall as the
  primary task;
- stimulus writing, translation, norming, corpus selection, and lexical
  database operations;
- participant, item, list, or trial-count calculation;
- task code, server deployment, data collection, preprocessing, and analysis.

For an EEG plus SPR design, SPR owns reveal, segmentation, reading response,
and probe structure. [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) owns markers, physical onset
validation, and EEG-specific motor and ocular timing. Require a joint
checkpoint.

## Inputs

Handle one administration at a time.

| Field | Required content |
|---|---|
| Approved design | user-approved construct, manipulation, factors, contrast, and visual SPR choice |
| Item state | Exact source, language, script, versions, critical material, and norming state |
| Population | Language background, age, literacy, clinical, accessibility, and device-relevant constraints |
| Regions | Theory, source, or pilot basis for critical and candidate downstream regions |
| Response need | Advance action, rereading rule, comprehension purpose, and any secondary response |
| Platform | Lab or online context, target browser, OS, device, screen, and input constraints |
| Evidence | Exact methods, task source, local specification, and rights state |
| Stop point | Chat-only specification or separately approved handoff |

If the construct, manipulation, contrast, visual SPR choice, or item state is
absent, identify the missing owner and stop. Do not create it for the user.

## Steps

### 1. Establish the design boundary

Restate the approved construct, manipulation, contrast, visual SPR choice,
population, item state, language and script, candidate regions, platform,
rights, evidence, exclusions, and unresolved choices. Separate evidence from
interpretation.

### 2. Gate 1: approve the evidence and comparison boundary

Present:

1. approved design and item state;
2. exact sources and rights;
3. reveal, segmentation, geometry, region, response, probe, filler, platform,
   and validation fields to inspect;
4. credible administration routes;
5. fixed owner-level decisions and unresolved choices;
6. exclusions and later handoffs.

Gate 1 authorizes only the displayed design review. It does not authorize
task-family choice, stimulus writing or norming, power, programming, asset use,
data collection, preprocessing, analysis, deployment, or saving.

Reopen Gate 1 after a material construct, manipulation, item, language, script,
population, platform, or source change.

### 3. Build the Display Card

Record:

- cumulative or noncumulative mode;
- spatially preserved or fixed-position reveal;
- approved reveal unit and segmentation method;
- rereading, advance, omission, repeat, and timeout behavior;
- font, directionality, line breaking, wrapping, spacing, and screen geometry;
- input device, response mapping, and accessibility behavior;
- target platform and unresolved physical-timing limits.

### 4. Build the Region and Item Map

| Item and condition | Precritical | Critical | Downstream | Wrap-up | Material differences | Evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

Mark clause boundaries, punctuation, line breaks, ambiguous segmentation,
clitics, compounds, multiword units, and script-specific issues. Do not use
whitespace splitting for non-space scripts, right-to-left or bidirectional
text, clitics, or approved multiword regions.

### 5. Build the Probe and Filler Matrix

| Element | Purpose | Target relation | Condition coverage | Response balance | Strategy threat | Rights |
|---|---|---|---|---|---|---|
| | | | | | | |

Fail validation if probes or fillers reveal the manipulation unintentionally
or if participants see multiple versions of the same item without an approved
reason.

### 6. Build the Platform and Event Card

Specify target task version, browser or runtime, OS, device, display geometry,
input method, event fields, clocks, physical-timing uncertainty, data-loss
states, pause and restart behavior, and configuration-specific validation.

Do not turn this card into implementation instructions.

### 7. Build the Threat Register and Pilot Plan

At minimum assess:

- reveal-mode and spatial-layout effects;
- segmentation, wrapping, clause-boundary, and wrap-up confounds;
- critical and downstream material differences;
- ambiguity, disambiguation, plausibility, and norming gaps;
- probe and filler strategy changes;
- repeated item-version exposure;
- response-device and accessibility effects;
- browser, OS, screen, and device heterogeneity;
- practice, fatigue, learning, and list order;
- missing events, skips, repeats, timeouts, pauses, and restarts;
- individual-difference reliability;
- language, script, morphology, literacy, L2, child, older, and clinical
  population applicability.

Pilot readability, segmentation, item balance, comprehension, event logging,
and the exact platform. Retain failures and unresolved threats.

### 8. Gate 2: select the administration

Present the display card, region map, probe and filler matrix, platform card,
threat register, pilot plan, evidence labels, limitations, and handoffs.

The user selects the reveal and geometry route, segmentation, regions, response
behavior, probes, fillers, platform boundary, validation scope, unresolved
items, and next stop.

Gate 2 authorizes only the selected SPR Design Specification. It does not
authorize stimulus creation, norming, task code, sample size, data collection,
RT cleaning, statistical analysis, interpretation, deployment, or saving.

### 9. Produce the SPR Design Specification

Return:

1. approved construct, manipulation, contrast, population, and visual SPR
   choice;
2. source, language, script, item, and rights state;
3. reveal mode, geometry, rereading, advance, and response behavior;
4. region and item map with critical, downstream, and wrap-up labels;
5. probe and filler plan;
6. platform, device, event, and physical-timing boundary;
7. strategy, segmentation, lexical, structural, population, and reliability
   threats;
8. pilot and exact-configuration validation plan;
9. evidence labels, assumptions, unknowns, and residual risks;
10. user-selected choices and rejected routes;
11. separately approved handoff or explicit stop.

### 10. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- construct, manipulation, contrast, SPR choice, and item state came from the user
  or an approved handoff;
- reveal mode, segmentation, geometry, and rereading are explicit;
- critical, downstream, and wrap-up regions remain distinct;
- no fixed spillover, timing, matching, probe, item, filler, trimming, model,
  or effect-size default was inherited;
- no whitespace auto-splitting is used;
- no participant sees multiple item versions unless approved;
- probes and fillers do not reveal the target unintentionally;
- exact-platform validation is required;
- stimulus norming and analysis remain with later owners;
- both gates bound their authorization.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The user owns the research question, hypothesis, prediction, confirmatory status,
construct, manipulation, contrast, task choice, population, item content,
stimulus versions, power inputs, analysis plan, interpretation, and all final
selections.

This skill:

- never chooses a region because an effect appeared there;
- never assigns a universal spillover length or reading-time threshold;
- never treats overall reading speed as a reliable individual-difference
  contrast;
- never auto-splits text on whitespace;
- never copies sentences, corpora, norms, code, fonts, or copyrighted task
  materials;
- records language, script, population, source, license, and modification
  state for every item set;
- stops when stimulus or platform rights are unresolved.

For every proposed choice:

1. label it `direct evidence`, `bounded adaptation`, `design-derived`,
   `candidate for pilot`, or `unknown`;
2. record source, version, language, script, population, platform, display
   mode, item grain, and applicability;
3. separate reveal design from stimulus validity and later analysis;
4. preserve conflicting methods;
5. make line wrapping and segmentation explicit;
6. use no fixed parameter as a default without direct applicable evidence;
7. validate the exact target configuration.

Do not inherit universal fixation, timeout, postdelay, practice, spillover,
matching tolerance, probe frequency, accuracy cutoff, item count, filler ratio,
adaptation, trimming, transformation, random-effect, region-test, or effect-size
rules.

Edge cases:

- **Only `reading task` is supplied:** do not activate or choose SPR.
- **SPR versus eye tracking or maze is unresolved:** route to the paradigm
  owner.
- **Self-paced listening is requested:** mark it outside this visual scope.
- **A fixed spillover, item, timing, or probe rule is supplied:** treat it as a
  source claim requiring applicability review.
- **The target ends a sentence or clause:** separate wrap-up and compare a
  neutral continuation route.
- **Conditions differ in line break or geometry:** surface the display
  confound.
- **CJK, Thai, right-to-left, bidirectional, clitic, or multiword text:** use
  language-appropriate explicit segmentation, never whitespace auto-split.
- **Online mobile or touch administration:** require population and
  configuration-specific evidence and validation.
- **Individual differences are claimed from one session:** require a
  reliability plan or block the inference.
- **Sample or item counts are requested:** hand off to power planning.
- **RT trimming, transformation, or model choice is requested:** route to the
  later analysis owner.
- **Copyrighted sentences, corpora, or norms are proposed:** verify rights
  separately.
- **No defensible administration:** return a blocked specification.

This skill cannot establish stimulus validity, physical display timing,
population generalizability, person-specific reliability, sample adequacy, or
the causal interpretation of a reading-time contrast. It cannot guarantee
that an implementation matches the specification.

## Design facts that control the review

### Reveal and display mode

- Cumulative and noncumulative moving-window formats are not interchangeable.
  Neither are spatially preserved and fixed-position reveal.
- Select and report word, phrase, clitic, morpheme, or approved multiword reveal
  units. Do not infer units from spaces.
- Rereading availability, advance response, skipped or repeated advance,
  timeout behavior, display persistence, and response-device mapping must be
  explicit.
- Line breaks, wrapping, cursor movement, font, spacing, and region position
  can change processing and comprehension. Stabilize geometry on the exact
  target configuration.

### Regions and continuations

- Predefine the critical region and downstream regions from theory, source, or
  independent pilot evidence. Do not move them after observing the target
  contrast.
- Effects may appear downstream, but no fixed number of spillover words is
  universal.
- Separate spillover from clause or sentence wrap-up. When a target would end
  a clause or sentence, consider a neutral, condition-matched continuation and
  label the later boundary separately.
- Prefer identical critical and downstream material across conditions when
  scientifically possible. Otherwise expose lexical, morphological,
  structural, semantic, plausibility, and norming differences.
- Route creation and validation of those materials to
  [sentence-stimulus-norming](../sentence-stimulus-norming/SKILL.md). Matching tolerances never prove equivalence.

### Probes, fillers, platform, and reliability

- Comprehension probes and fillers can alter participant strategy. Specify
  their purpose, content, condition coverage, response balance, frequency, and
  relation to the manipulation.
- A probe or filler that transparently reveals the target can invalidate the
  administration. Participants must not see multiple versions of the same
  experimental item unless that exposure is explicitly part of the approved
  design.
- Browser, operating system, device, screen geometry, input method, and task
  version are measurement context. Validate the exact target setup.
- Heterogeneous devices weaken unqualified absolute reading-time comparisons.
  A platform log does not prove physical display timing.
- Stable overall speed or a population-level condition effect does not prove a
  reliable person-specific contrast. Individual-difference use needs an
  explicit repeated-occasion or parallel-form reliability plan with
  uncertainty.

## Display and response validation

Use the Display Card and Region and Item Map to identify what readers see
and where responses are recorded. Capture probes and fillers in the Probe
and Filler Matrix, record platform constraints in the Platform Card, and use
the Threat Register and Pilot Plan to define what must be checked. Compare
evidence-compatible reveal, segmentation, geometry, region, probe, filler,
platform, and validation choices where the design remains open. Explain why
a sole defensible route fits.

After Gate 2, record only the user's selections in the SPR Design
Specification. Stop before stimulus creation, programming, data collection,
cleaning, modeling, or interpretation.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) for SPR-versus-alternative selection.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, and list
  architecture.
- Use [sentence-stimulus-norming](../sentence-stimulus-norming/SKILL.md) for sentence creation, lexical and
  syntactic controls, plausibility, cloze, acceptability, and norms.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) and [statistical-power](../../skills/statistical-power/SKILL.md) for participant, item,
  trial, reliability, attrition, and operating-characteristic planning.
- Use [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) at a joint checkpoint for EEG plus SPR.
- Route RT cleaning, transformations, mixed models, regionwise inference,
  programming, and packaging only after the relevant designs are selected.

Never chain automatically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Anwyl-Irvine et al. (2021). https://doi.org/10.3758/s13428-020-01501-5
- Aurnhammer et al. (2021). https://doi.org/10.1371/journal.pone.0257430
- Bridges et al. (2020). https://doi.org/10.7717/peerj.9414
- Chromý & Tomaschek. (2024). https://doi.org/10.1162/opmi_a_00173
- Frinsel & Christiansen. (2024). https://doi.org/10.3758/s13428-024-02355-x
- James et al. (2018). https://doi.org/10.1016/j.jml.2018.05.006
- Just, Carpenter, & Woolley. (1982). https://doi.org/10.1037/0096-3445.111.2.228
- Keating & Jegerski. (2015). https://doi.org/10.1017/S0272263114000187
- Marsden, Thompson, & Plonsky. (2018). https://doi.org/10.1017/S0142716418000036
- Tsoukala, Vogelzang, & Tsimpli. (2025). https://doi.org/10.1017/langcog.2025.10009
