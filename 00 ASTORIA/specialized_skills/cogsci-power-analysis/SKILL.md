---
name: cogsci-power-analysis
description: >-
  Builds a cognitive or behavioral Power Inputs Specification for one approved
  design without calculating or selecting sample size. Use when the request, or
  a part coordinator, hands over an explicitly matching task. It maps participants,
  items, trials, sessions, reliability, variance, data loss, effect-evidence
  applicability, and resource tradeoffs, then records only user-selected
  assumptions and scenarios after two approval gates for handoff to
  statistical-power. It does not supply fixed modality priors, choose scientific
  inputs, calculate power or N, install tools, search, analyze observed data,
  save, or start another capability without separate approval. Triggers: power
  inputs for my behavioral study, cognitive experiment power specification.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: power
  modality: behavior
  dependencies: ""
  requires: ""
  gates: choosing the sample size
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Cognitive Science Power Analysis

Specify cognitive and behavioral power inputs without turning inherited rules of thumb into scientific decisions.

## Purpose

`cogsci-power-analysis` is the Part 3 canonical owner for cognitive and behavioral power-input specification for one approved design.

It owns:

- mapping participants, items or stimuli, trials, blocks, sessions, lists, sites, and other sampling levels;
- distinguishing independent units, repeated observations, crossed factors, nested factors, and intended generalization targets;
- assessing whether candidate effect evidence matches the construct, population, task, outcome, contrast, metric, design, estimand, and planned analysis;
- specifying candidate variance, correlation, reliability, exclusion, attrition, and unusable-data assumptions;
- comparing participant-by-item-by-trial-by-session input scenarios within supplied resource bounds;
- producing a selection-bound Power Inputs Specification and [statistical-power](../../skills/statistical-power/SKILL.md) handoff packet.

The user owns the question, hypothesis, prediction, outcome, estimand, design, generalization target, analysis model, effect basis, parameter values, error rules, target power, resource allocation, final sample size, interpretation, and scientific claims.

[experimental-design](../../skills/experimental-design/SKILL.md) owns the design. [statistical-power](../../skills/statistical-power/SKILL.md) owns the quantitative calculation. This skill does not calculate sample size, power, MDE, or operating characteristics.

EEG, MEG, fMRI, and other neuroimaging power assumptions belong to their modality-specific power owners. This skill may specify a behavioral outcome collected alongside those modalities only when that outcome is a separable approved target.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `calculate my sample size`;
- `how many participants do I need`;
- `power my fMRI study`;
- `power my EEG study`;
- `design this cognitive task`;
- `analyze my pilot data`;
- broad phrases such as `power`, `cognitive study`, `trials`, or `participants`.

One run covers one primary cognitive or behavioral estimand and one approved design-analysis structure.

Several related parameter scenarios may vary participants, items, trials, sessions, reliability, data loss, or effect assumptions while preserving that structure. Separate materially different outcomes, estimands, tasks, models, or generalization targets.

No source table, field median, or rule of thumb may become an input merely because it appears in the external candidate.

## Inputs

Gather:

- exact cognitive or behavioral research question, hypothesis, or prediction supplied by the user;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) Design Specification or equivalent supplied design;
- primary outcome, contrast, estimand, and intended generalization target;
- planned analysis model, tested parameter, and decision rule when selected;
- participant population, grouping, sampling, and repeated structure;
- item or stimulus population, sampling, assignment, counterbalancing, list, and generalization scope;
- trial, block, session, visit, site, cohort, rater, or other repeated and clustered levels;
- expected response distribution, floor or ceiling risk, speed-accuracy relationship, and scoring rules;
- candidate effect evidence or effect-basis options and their sources;
- candidate variance components, correlations, reliability, and measurement-error information;
- participant, item, trial, session, and site exclusions or data-loss mechanisms;
- recruitment, task-duration, fatigue, learning, burden, calendar, staffing, equipment, and cost constraints;
- outcome visibility, confirmatory status, protocol, preregistration, and deviations;
- supplied evidence, approved evidence boundary, desired output, and stop point.

Mark an essential missing item `unknown`. Do not fill it from a modality table or convention.

## Cognitive and behavioral input lanes

Offer only applicable lanes at Gate 1:

1. **Participants and populations**
   - Sampling unit, grouping, repeated structure, heterogeneity, attrition, and intended population inference.

2. **Items, stimuli, and lists**
   - Item population, fixed versus sampled items, crossing or nesting with participants and conditions, counterbalancing, list construction, and intended item generalization.

3. **Trials, blocks, and sessions**
   - Repetitions per condition, usable-trial yield, learning, fatigue, order, practice, session variation, and diminishing returns.

4. **Effect-evidence applicability**
   - Construct, task, contrast, metric, design, estimand, analysis, population, and uncertainty match.

5. **Variance, correlation, and reliability**
   - Participant, item, residual, slope, session, and site variance; within-unit correlations; measurement reliability; and attenuation risks.

6. **Data loss and resource tradeoffs**
   - Recruitment versus retention, item and trial loss, exclusions, burden, duration, cost, and feasible scenario bounds.

More trials may improve within-participant precision, but they do not create more independent participants or guarantee greater overall power. More participants cannot compensate indefinitely for too few sampled items when the intended inference generalizes across items. The balance depends on variance components, the planned model, and resource costs.

## Steps

### 1. Build the Cognitive Power Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and inquiry part |
| Intended decision | What the input specification should help the user evaluate |
| Scientific target | The user's question, hypothesis, or prediction |
| Outcome and estimand | Exact approved target |
| Generalization target | Participants, items, settings, sessions, or other populations |
| Design | Conditions, factors, allocation, timing, and approved unit structure |
| Planned analysis | Model, tested parameter, contrast, and decision rule, or `unknown` |
| Sampling levels | Participants, items, trials, blocks, sessions, sites, cohorts, and raters |
| Effect evidence | Supplied sources or candidate effect-basis routes |
| Measurement inputs | Variance, correlation, reliability, distribution, scoring, floor, and ceiling information |
| Data loss | Attrition, exclusions, invalid trials, unusable items, missingness, and adherence |
| Resources | Recruitment, duration, fatigue, burden, cost, equipment, staffing, and calendar |
| Selected lanes | Exact input lanes requested |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied material that may be inspected |
| Excluded work | Design selection, numeric input selection, calculation, search, installation, observed-data analysis, saving, and unapproved handoffs |
| Stop point | Exact output or decision that ends the run |

### 2. Gate 1: approve the domain-input boundary

Ask the user to approve or correct the Cognitive Power Brief and selected lanes.

Gate 1 authorizes only:

- inspection of the displayed design and supplied evidence;
- mapping the displayed sampling levels;
- assessment of candidate evidence and parameter applicability;
- generation of bounded input scenarios from supplied values and resource bounds.

It does not authorize:

- selecting an effect, variance, reliability, exclusion rate, error rule, target power, design, analysis, or final sample size;
- calculating power, N, MDE, or an operating characteristic;
- searching, installing software, analyzing observed data, saving, or starting another capability.

If the outcome, estimand, generalization target, design, analysis, selected lane, outcome visibility, or evidence boundary changes materially, rebuild the brief and repeat Gate 1.

### 3. Build the Unit and Replication Map

| Level | Required content |
|---|---|
| Participants | Population, sampling, groups, repeated structure, and independent count |
| Items or stimuli | Population, selection, condition assignment, crossing or nesting, and inference scope |
| Trials | Trials per condition, repeated observations, expected usable yield, and aggregation or trial-level use |
| Blocks and lists | Blocking, list assignment, counterbalancing, order, and dependency |
| Sessions or visits | Timing, repeated sessions, learning, fatigue, attrition, and within-person dependence |
| Sites, cohorts, or raters | Sampling, clustering, calibration, and generalization |
| Analysis unit | Unit and hierarchy the planned analysis represents |
| Intended inference | Exact participant, item, condition, setting, or time population |
| Replication risk | Pseudoreplication, sparse levels, confounding, or unmodeled dependence |

Repeated trials are observations within higher-level units unless the approved design establishes otherwise. A fixed stimulus set may support inference to those stimuli, but not automatically to a broader item population.

### 4. Build the Effect Evidence Applicability Matrix

Create one row per candidate source or user-defined basis:

| Field | Required content |
|---|---|
| Evidence ID | Stable identifier |
| Source and exact result | Citation or supplied source, estimate, uncertainty, and sample |
| Effect metric | Raw or standardized metric and exact denominator |
| Construct and task | Match to the planned construct, manipulation, and paradigm |
| Population and setting | Match to participants, language, culture, age, clinical status, and context |
| Outcome and contrast | Match to measure, scoring, timing, and tested comparison |
| Design and estimand | Match to within, between, crossed, longitudinal, interaction, or other structure |
| Analysis | Match to aggregation, trial-level model, covariates, random effects, correction, and decision rule |
| Reliability and data quality | Relevant reliability, exclusions, trial count, and missingness |
| Selective-evidence risk | Publication, selection, small-study, follow-up, or other inflation risk |
| Translation | Every conversion or adjustment needed |
| Applicability status | One status below with a reason |

Use only:

- **Compatible as supplied**
- **Compatible with explicit translation**
- **Incompatible with the target calculation**
- **Not assessable from supplied evidence**

Do not convert a review, benchmark, or field median into a prior without checking the underlying estimate and exact target match.

### 5. Build the Variance, Reliability, and Data-Loss Register

| Field | Required content |
|---|---|
| Parameter ID | Stable identifier |
| Parameter | Effect, variance component, correlation, reliability, rate, or yield |
| Level | Participant, item, trial, session, site, or other level |
| Candidate value or range | Supplied values with units, or `unknown` |
| Basis | User supplied, source supported, pilot summary, methodological inference, or unverified |
| Applicability | Exact match and translation limits |
| Consequence | How the parameter affects information or scenario interpretation |
| Failure mode | Ceiling, floor, attenuation, nonconvergence, bias, sparse levels, or invalid loss model |
| Resolution | The user selection, evidence audit, search, specialist input, or defer |

Use pilot work cautiously. It may inform variance, reliability, timing, exclusions, and usable-trial yield, but a small pilot effect estimate must not be silently treated as the population effect.

Reliability is specific to the score, population, design, and use. Do not apply a generic correction or assume more trials solve construct validity.

### 6. Build the Participant-by-Item-by-Trial Scenario Grid

Generate two to four `AI-generated input scenario` entries only from supplied feasible bounds and compatible evidence. If one complete scenario is supplied, preserve one. If no defensible values are available, show unresolved fields rather than inventing them.

| Field | Required content |
|---|---|
| Scenario ID | Stable label |
| Participants | Analyzed and recruited candidate values or ranges |
| Items or stimuli | Sampled or fixed count, per condition, and generalization scope |
| Trials | Presented and expected usable trials per condition |
| Blocks and sessions | Counts, timing, and dependency |
| Effect basis | Selected candidate evidence ID or user-defined SESOI route |
| Variance and reliability | Candidate ranges and levels |
| Data loss | Participant, item, trial, and session loss assumptions |
| Planned analysis match | How the model represents participants, items, trials, and repeated structure |
| Resource implications | Duration, fatigue, burden, recruitment, staffing, equipment, and cost |
| Tradeoff | What information may improve or degrade relative to another scenario |
| Calculation inputs still needed | Error rules, target power, parameters, method, or specialist inputs |
| Scenario status | Compatible, compatible with translation, incompatible, or not assessable |

Do not rank a scenario by counting participants alone. Do not use arbitrary claims such as interactions always being half the main effect or requiring four times the sample.

### 7. Present response options

For each consequential input, offer only applicable options:

- retain a compatible value or range;
- return the value to the user for selection;
- translate it with displayed assumptions;
- investigate through a bounded evidence or specialist handoff;
- remove an incompatible input or scenario;
- defer the specification.

Do not recommend a final sample size or target power.

### 8. Gate 2: The user selects assumptions and scenarios

Ask the user to:

- select the effect-evidence basis or user-defined route;
- select participant, item, trial, session, variance, reliability, and data-loss scenarios;
- confirm the intended generalization and planned-analysis match;
- preserve unresolved parameters that must remain open;
- select any handoff packet.

Gate 2 authorizes only the selected inputs for the Power Inputs Specification and selected handoff packets.

It does not authorize calculation, design or analysis changes, search, software installation, observed-data analysis, saving, or another capability.

Do not infer selection from silence.

### 9. Produce and verify the Power Inputs Specification

Return:

| Field | Required content |
|---|---|
| Approved scope | Study, outcome, estimand, design, analysis, and evidence boundary |
| Generalization target | Exact participant, item, setting, session, or other populations |
| Unit structure | Participants, items, trials, blocks, sessions, sites, and dependencies |
| Selected effect basis | Value or range, metric, provenance, applicability, and translation |
| Selected parameter scenarios | Variance, correlation, reliability, data loss, and resource ranges |
| Selected scenario grid | Only Gate 2 selections |
| Error and power inputs | user-supplied rules, or explicit unresolved decisions |
| Calculation requirements | Exact analytic, simulation, or specialist features the later calculation must honor |
| Open items | Missing evidence, user choices, or specialist inputs |
| Statistical Power packet | Complete selected inputs for [statistical-power](../../skills/statistical-power/SKILL.md) |
| Provenance | User statements, source evidence, AI-generated scenarios, translations, and decisions kept separate |

Verify that:

- the specification matches both gates;
- participant, item, trial, session, site, and analysis units are not conflated;
- repeated observations are not counted as independent participants;
- the item-generalization claim matches item sampling and analysis;
- effect evidence matches the construct, task, population, outcome, metric, design, estimand, and analysis, or its mismatch is explicit;
- every conversion and reliability or data-loss assumption is visible;
- no fixed source table or generic modality range was adopted;
- no effect, error rule, target power, scenario, calculation, final sample size, design change, or analysis model was silently selected;
- no search, installation, observed-data analysis, save, or unapproved handoff occurred.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the recipient's applicable reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **Cognitive Power Brief**
- **Unit and Replication Map**, after Gate 1
- **Effect Evidence Applicability Matrix**
- **Variance, Reliability, and Data-Loss Register**
- **Participant-by-Item-by-Trial Scenario Grid**
- **Response Options**
- **Power Inputs Specification**, only after Gate 2
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return power-analysis results in the current task's requested form or under the recipient's existing reporting policy. Neither gate authorizes searching, installing software, modifying a source, saving, or starting another capability.

Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized save, use the destination selected for the task. Otherwise use the established project or area destination when the recipient's placement policy calls for it. Keep skill and system work in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved.

## Boundaries

- **No approved design**: Route to [experimental-design](../../skills/experimental-design/SKILL.md) and stop.
- **No planned analysis structure**: Mark analysis compatibility unresolved and prepare the appropriate method handoff.
- **Participant count supplied without item or trial structure**: Do not calculate or imply adequacy.
- **Fixed stimulus set**: Preserve the restricted item-inference scope unless the user changes the design.
- **Few sampled items**: Do not imply that more participants guarantee generalization across items.
- **Many repeated trials**: Do not count them as independent participants or promise an automatic power gain.
- **Small pilot effect supplied**: Use it only after applicability and instability review; preserve variance, reliability, and data-quality uses separately.
- **Meta-analytic estimate supplied**: Inspect the included studies, effect metric, target match, heterogeneity, selection risk, and uncertainty.
- **Generic modality median or lookup table supplied**: Reject it as a direct input unless independently verified and specifically applicable.
- **Interaction target**: Require the exact interaction parameter and model. Do not apply a universal fraction or sample multiplier.
- **Speed and accuracy both matter**: Require the user to define the primary estimand or an approved joint model.
- **Ceiling or floor risk**: Include the response distribution and measurement implications in the scenario.
- **High attrition or invalid-trial rate**: Separate participant, item, trial, and session loss and preserve the assumed mechanism.
- **EEG, MEG, or fMRI signal is primary**: Route to the modality-specific power owner and stop.
- **Observed nonsignificant result**: Route interpretation to Part 4. Do not produce observed post hoc power.
- **Statistical Power begins**: Require separate approval and that skill's own Gate 1.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

When the user selects the handoff, include:

- approved Power Inputs Specification;
- exact primary estimand, outcome, generalization target, and planned analysis;
- participant, item, trial, session, site, and dependency structure;
- selected effect metric, value or range, provenance, applicability, and translations;
- selected variance, correlation, reliability, and data-loss assumptions;
- selected resource scenarios and exact units;
- user-supplied alpha, sidedness, multiplicity, target power, or explicit unknowns;
- required sensitivity grid, simulation features, limitations, and stop point.

Show the packet and ask for separate approval before [statistical-power](../../skills/statistical-power/SKILL.md) begins its own Gate 1.

Boundaries and handoffs:

- Use [experimental-design](../../skills/experimental-design/SKILL.md) when the design, units, conditions, allocation, counterbalancing, or timing is not approved.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) for quantitative sample-size, power, MDE, or operating-characteristic calculation after inputs are approved.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for a bounded audit of one effect-evidence claim.
- Use [paper-search](../../skills/paper-search/SKILL.md) only after separate approval for a bounded effect, variance, reliability, data-loss, or paradigm evidence need.
- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the construct, paradigm architecture, manipulation, comparator, trial event, outcome, or task-specific validity remains unresolved.
- Use [alternative-uses-task-designer](../alternative-uses-task-designer/SKILL.md) when the approved task is AUT and its instruction, object, timing, response-capture, quality-control, or assistance-access specification is unresolved.
- Use [visual-search-array-generator](../visual-search-array-generator/SKILL.md) when an approved controlled-array visual-search design needs deterministic layout-manifest generation or constraint validation.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) when an approved behavioral task needs model-aware task-fMRI timing and schedule validation.
- Use future task-specific design skills for other unresolved stimulus or task construction.
- Use [neuroimaging-power-guide](../neuroimaging-power-guide/SKILL.md) for MRI-specific signal, correction, spatial, run, ROI, pipeline, reliability, or quality-control assumptions.
- Use a future EEG or MEG power owner for modality-specific sensor and signal assumptions.
- Route observed-data fitting, diagnostics, and inference to an approved Part 4 capability.

Each destination begins its own workflow and gates. Cognitive Science Power Analysis approval does not authorize another capability.

This skill does not design the study, supply fixed priors, calculate sample size or power, choose scientific or statistical inputs, install software, search, analyze observed data, or make a scientific conclusion for the user. Save a verified result only within the separately authorized content and destination. The scientific gates grant no write authority.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Albers, C., & Lakens, D. (2018). When power analyses based on pilot data are biased. *Journal of Experimental Social Psychology, 74*. https://doi.org/10.1016/j.jesp.2017.09.004
- Baker, D. H., Vilidaite, G., Lygo, F. A., et al. (2021). Power contours: Optimising sample size and precision in experimental psychology and human neuroscience. *Psychological Methods, 26*(3). https://doi.org/10.1037/met0000337
- Lakens, D. (2022). Sample size justification. *Collabra: Psychology, 8*(1). https://doi.org/10.1525/collabra.33267
- Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11). https://doi.org/10.1002/sim.8086
- Westfall, J., Kenny, D. A., & Judd, C. M. (2014). Statistical power and optimal design in experiments in which samples of participants respond to samples of stimuli. *Journal of Experimental Psychology: General, 143*(5). https://doi.org/10.1037/xge0000014
