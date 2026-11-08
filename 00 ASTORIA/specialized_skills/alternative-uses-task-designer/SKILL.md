---
name: alternative-uses-task-designer
description: >-
  Designs one prospective Alternative Uses Task administration specification
  after the user has selected the task and approved the broader experimental design.
  Use when the request, or a part coordinator, hands over an explicitly matching
  task. It compares AUT-specific instruction emphasis, objects, timing, response
  capture, order, quality-control, and optional tool-access parameters, exposes
  their evidence and construct consequences, and records only user-selected
  choices after two approval gates. It does not decide whether AUT is the right
  paradigm, choose conditions or sample size, score responses, deploy a survey,
  recruit participants, operate external tools, search, save, or analyze
  outcomes without separate approval. Triggers: set up an alternative uses task,
  AUT administration spec.
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
  updated: "2026-10-29"
---

# Alternative Uses Task Designer

Design an Alternative Uses Task administration without converting inherited defaults into research decisions.

## Purpose

`alternative-uses-task-designer` is the Part 3 canonical owner for prospective AUT-specific administration design after the task and general experimental structure are approved.

It owns:

- comparing instruction-emphasis options for one specified divergent-thinking target;
- comparing candidate objects or object-selection strategies within the approved population and language;
- specifying timing, item count, response capture, practice, order, breaks, and participant-facing task flow;
- specifying AUT-specific condition access, tool-use records, manipulation checks, and privacy constraints when the user has approved an assistance condition;
- specifying prospective task-quality indicators, review flags, and a pilot and verification plan;
- producing a selection-bound AUT Task Design Specification.

The user owns the construct, hypothesis, prediction, decision to use AUT, conditions, experimental unit, allocation, assignment, primary outcome, scoring target, task parameters, exclusions, confirmatory status, interpretation, and scientific claims.

[experimental-design](../../skills/experimental-design/SKILL.md) owns the general condition and allocation structure. [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) owns participant, item, trial, session, reliability, data-loss, and effect-evidence inputs. [statistical-power](../../skills/statistical-power/SKILL.md) owns quantitative power and sample-size calculations.

[cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) compares AUT with other cognitive or behavioral paradigms. The `divergent-thinking-scoring` capability owns response validation, fluency, flexibility, originality, elaboration, semantic or human scoring, raters, reliability, aggregation, and observed-response analysis.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `measure creativity`;
- `choose a divergent-thinking task`;
- `score these alternative uses`;
- `calculate my sample size`;
- `build this Qualtrics survey`;
- `run an AUT`;
- broad phrases such as `creativity`, `alternative uses`, `divergent thinking`, or `task design`.

One run covers one prospective AUT administration for one approved construct, population, language, setting, and general experimental structure.

Related conditions may be compared within that administration only when [experimental-design](../../skills/experimental-design/SKILL.md) has already specified their role. Separate materially different constructs, populations, languages, modalities, settings, or experimental structures.

AUT performance is evidence about performance on the specified divergent-thinking task. Do not silently relabel it as creativity in general, creative achievement, or a pure measure of one cognitive process.

## Inputs

Gather:

- The user's exact construct, question, hypothesis, or prediction;
- explicit confirmation that AUT is selected, or an approved specialist handoff that establishes it;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) Design Specification or equivalent condition and allocation structure;
- population, age, language, culture, clinical or developmental context, and accessibility needs;
- setting, device, modality, response interface, and supervision level;
- primary outcome and planned downstream scoring target, without selecting the scoring method here;
- intended objects or object-selection requirements;
- candidate instruction emphasis and whether quantity, quality, flexibility, or another aspect is intended;
- proposed timing, item count, order, practice, breaks, and session constraints;
- condition-specific assistance, information access, or tool use already approved by the user;
- proposed task records, manipulation checks, privacy boundary, consent and ethics constraints, and retention rules;
- prospective quality indicators, exclusion-policy inputs, and outcome visibility;
- confirmatory status, protocol, preregistration, and deviations;
- supplied evidence, approved evidence boundary, desired output, and stop point.

Mark an essential missing item `unknown`. Do not fill it from the external candidate's tables or templates.

## AUT design lanes

Offer only applicable lanes at Gate 1:

1. **Construct and instruction alignment**
   - Intended divergent-thinking aspect, participant instruction emphasis, response goal, and downstream scoring compatibility.

2. **Objects and item sampling**
   - Familiarity, affordances, conventional-use baseline, language, culture, accessibility, object comparability, fixed versus sampled items, and inference scope.

3. **Timing and task flow**
   - Item count, time or self-pacing, practice, response entry, prompts, breaks, order, counterbalancing requirements, and burden.

4. **Condition access and assistance**
   - user-approved AI, search, reference, collaboration, or unaided conditions; access parity; versioning; contamination; manipulation checks; and privacy.

5. **Quality control and review**
   - Prospective validity rules, duplicate or empty responses, technical failures, attention or seriousness checks, review flags, exclusion ownership, and bias risk.

6. **Pilot and reporting**
   - Comprehension, timing, usability, accessibility, object comparability, data-capture integrity, protocol fidelity, version preservation, and reporting fields.

No object, time limit, item count, platform, condition, attention check, cutoff, exclusion, or instruction wording is a default.

## Steps

### 1. Build the AUT Design Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and Part 3 task |
| Scientific target | The user's exact construct, question, hypothesis, or prediction |
| AUT status | Selected by the user, established by an approved handoff, or unresolved |
| General design | Conditions, units, assignment, timing structure, and approved constraints |
| Population | Age, language, culture, clinical or developmental context, and accessibility |
| Setting | Lab, remote, supervised, device, modality, and interface constraints |
| Outcome intent | Primary outcome and downstream scoring target, or `unknown` |
| Object scope | Supplied objects or selection requirements |
| Instruction scope | Candidate emphasis without copied wording |
| Task flow | Candidate timing, item count, order, practice, breaks, and response capture |
| Assistance conditions | Approved access, comparison role, and contamination controls |
| Privacy and ethics | Records, consent, deception, vulnerable groups, tool logs, and retention limits |
| Quality policy | Prospective indicators, review flags, and exclusion authority |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied material that may be inspected |
| Selected lanes | Exact AUT design lanes requested |
| Excluded work | Paradigm selection, general design changes, scoring, power, implementation, recruitment, search, saving, and observed-data analysis |
| Stop point | Exact output or decision that ends the run |

If AUT is not already selected, stop and prepare a bounded [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) handoff rather than assuming it is appropriate.

### 2. Gate 1: approve the AUT comparison boundary

Ask the user to approve or correct the AUT Design Brief, selected lanes, evidence boundary, and option-comparison plan.

Gate 1 authorizes only:

- inspection of the approved supplied material;
- comparison of AUT-specific administration options;
- construction of evidence, parameter, threat, and feasibility records;
- preparation of response options.

It does not authorize:

- selecting an instruction, object, time limit, item count, condition, platform, task record, check, cutoff, or exclusion;
- changing the general experimental design;
- drafting copied instructions or instrument items;
- calculating power, implementing or deploying a task, recruiting, logging tool use, searching, saving, scoring, or analyzing outcomes.

If the construct, AUT status, population, language, design, outcome intent, assistance condition, privacy boundary, or evidence scope changes materially, rebuild the brief and repeat Gate 1.

### 3. Build the Construct and Administration Map

| Field | Required content |
|---|---|
| Intended construct | Exact bounded divergent-thinking target |
| Task demand | What participants must generate, select, enter, or revise |
| Instruction emphasis | Quantity, uncommonness, appropriateness, flexibility, or another supplied target |
| Outcome alignment | How the planned scoring target corresponds to the instruction |
| Alternative processes | Verbal fluency, memory search, executive control, strategy, motivation, typing, language, prior object experience, and tool skill |
| Object role | Fixed prompts, sampled item population, comparability, and inference boundary |
| Condition role | Exact approved manipulation and comparator |
| Measurement limit | What AUT performance cannot establish by itself |

Expose instruction and scoring mismatch. Instructions that emphasize one aspect can change the number and nature of responses, so the task cannot be specified independently of the intended outcome.

### 4. Build the AUT Design Option Matrix

Generate two to four `AI-generated AUT design option` entries only when scientifically credible. If one route is credible, explain why and do not invent alternatives. If required evidence is missing, show unresolved fields.

| Field | Required content |
|---|---|
| Option ID | Stable label |
| Instruction strategy | Emphasis and participant task, without copied wording |
| Object strategy | Objects or selection criteria, sampling status, and population fit |
| Timing and item count | Candidate values or ranges and their evidence status |
| Response capture | Entry format, editing, order preservation, timestamps, and accessibility |
| Task flow | Practice, prompts, breaks, order, and return behavior |
| Assistance access | Approved tool or information access, version, parity, and contamination controls |
| Task records | Minimum necessary protocol and condition records |
| Quality approach | Prospective validity checks, review flags, and exclusion decision point |
| Construct consequence | What the option emphasizes or may alter |
| Feasibility | Burden, device, staffing, privacy, platform, and pilot needs |
| Evidence status | Verified exact-match evidence, verified translated evidence, user supplied, unverified candidate, or unresolved |
| Residual gap | Remaining evidence, rights, ethics, specialist, or implementation need |

Do not rank options automatically. Do not present a source's object tier, five-minute limit, one-to-three item count, fixed condition set, or platform choice as established practice.

### 5. Build the Parameter and Evidence Register

Create one row per consequential parameter:

| Field | Required content |
|---|---|
| Parameter ID | Stable identifier |
| Parameter | Instruction, object, timing, item count, response rule, condition access, record, check, or exclusion input |
| Candidate value | Exact value, range, wording purpose, or `unknown` |
| Provenance | The user supplied, verified source, translated source, external candidate, or AI-generated option |
| Exact match | Construct, population, language, setting, condition, outcome, and scoring match |
| Rights status | Original wording, faithful paraphrase, licensed item, permission required, or unresolved |
| Assumption | What must hold |
| Consequence | Construct, measurement, burden, bias, privacy, or feasibility effect |
| Status | Eligible, eligible with translation, unresolved, or reject |

Repository licensing does not license paper language, task instructions, scales, or copyrighted instruments reproduced in the candidate. Do not copy its templates or quoted scale items.

### 6. Build the Construct and Administration Threat Register

Assess:

- instruction and scoring mismatch;
- fluency, time-on-task, and originality dependence;
- task impurity and strategy differences;
- object familiarity, affordance, language, culture, and item effects;
- fixed-item inference and weak item sampling;
- practice, learning, fatigue, order, and carryover;
- demand characteristics, participant expectancy, and deception;
- typing speed, device, interface, accessibility, and technical failure;
- AI or search access, model drift, prompt exposure, copying, contamination, and collective-response homogeneity;
- collection of sensitive prompts, queries, responses, identifiers, or external-service logs;
- post-outcome checks, arbitrary time cutoffs, language exclusions, and differential exclusion bias;
- scorer needs and raw-data sufficiency without designing the scoring method;
- ceiling, floor, low response yield, and unusable item behavior.

For each threat show severity, evidence, affected option, detectable indicator, mitigation candidates, residual risk, owner, and unresolved decision.

### 7. Present response options

For every consequential decision, offer only applicable choices:

- retain an eligible parameter;
- return a parameter to the user for selection;
- translate a source-supported parameter with displayed assumptions;
- pilot two or more parameters prospectively;
- request a bounded [research-literacy](../../skills/research-literacy/SKILL.md) audit or [paper-search](../../skills/paper-search/SKILL.md);
- prepare an [experimental-design](../../skills/experimental-design/SKILL.md), [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md), [statistical-power](../../skills/statistical-power/SKILL.md), ethics, privacy, rights, implementation, or future scoring handoff;
- defer the AUT specification.

Do not recommend one option merely because it appears in the source candidate.

### 8. Gate 2: The user selects the AUT parameters

Ask the user to select:

- the instruction strategy and outcome alignment;
- objects or object-selection strategy;
- timing, item count, response capture, practice, order, and breaks;
- assistance access and minimum necessary records;
- prospective quality checks, review flags, and exclusion decision ownership;
- pilot and verification requirements;
- unresolved parameters that must remain open;
- requested handoff packets.

Gate 2 authorizes only the selected elements for the AUT Task Design Specification and selected handoff packets.

It does not authorize final copyrighted wording, general design changes, sample-size calculation, survey construction, deployment, recruitment, tool operation, data logging, search, saving, scoring, or outcome analysis.

Do not infer selection from silence.

### 9. Produce and verify the AUT Task Design Specification

Return:

| Field | Required content |
|---|---|
| Approved scope | Construct, population, language, setting, design, evidence boundary, and intended use |
| Task objective | Participant action and intended divergent-thinking target |
| Instructions specification | Selected emphasis and required concepts, not copied paper language |
| Objects | Selected prompts or criteria, familiarity and accessibility checks, order, and inference scope |
| Timing and flow | Selected timing, item count, practice, prompts, breaks, navigation, and completion behavior |
| Response capture | Format, editing, timestamps, metadata, accessibility, and missing-response behavior |
| Conditions | user-approved access and comparator rules without altering the general design |
| Records and privacy | Minimum necessary fields, consent, de-identification, retention, access, and prohibited records |
| Quality plan | Prospective indicators, review flags, blinded decision process when applicable, and who owns exclusions |
| Scoring requirements | Raw-data fields and selected target for future scoring, without a scoring protocol |
| Pilot plan | Comprehension, timing, usability, accessibility, item comparability, and data-integrity checks |
| Version record | Task, instructions, objects, platform specification, assistance tool and version, and approved changes |
| Open items | Unresolved evidence, rights, ethics, privacy, power, implementation, or scoring decisions |
| Handoffs | Only Gate 2 selected packets |
| Provenance | User decisions, source evidence, translations, and AI-generated options kept separate |

Verify that:

- AUT was explicitly selected;
- the specification matches both gates and the approved general design;
- instruction emphasis and downstream scoring target are compatible or the mismatch is explicit;
- objects and inference scope are not overgeneralized;
- no fixed source parameter became a default;
- task records are necessary, consent-compatible, and privacy bounded;
- no post-outcome exclusion was made prospective by relabeling;
- no copied paper instructions, scale items, or source template language was inserted;
- no scoring, power calculation, survey implementation, recruitment, external action, search, save, or outcome analysis occurred;
- all unresolved scientific and operational decisions remain visible.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the recipient's applicable reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **AUT Design Brief**
- **Construct and Administration Map**, after Gate 1
- **AUT Design Option Matrix**
- **Parameter and Evidence Register**
- **Construct and Administration Threat Register**
- **Response Options**
- **AUT Task Design Specification**, only after Gate 2
- **Pilot and Verification Plan**
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return the design results in the current task's requested form or under the recipient's existing reporting policy. Neither gate authorizes searching, survey construction, deployment, recruitment, external-tool use, collection of participant or tool logs, software installation, source modification, saving, or starting another capability.

Identify relevant privacy, ethics, rights, account, credential and retention implications before acting. Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized save, use the verified destination selected for the task. If none is selected, use the workflow's established project-owned scientific destination where it applies. For other supporting content, use a destination established by the recipient's placement policy, including Resources when that policy selects it. Skill and system work stays in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved. Add a verified link at the selected location only when the authorized scope includes that edit.

## Boundaries

- **AUT not selected**: Prepare a [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) handoff and stop.
- **Existing AUT submitted for review**: Route to [research-critique](../../skills/research-critique/SKILL.md).
- **No approved general design**: Route to [experimental-design](../../skills/experimental-design/SKILL.md).
- **One credible task option**: Explain the constraint and do not invent alternatives.
- **No verified object evidence**: Preserve object selection as unresolved or propose a pilot; do not use source tiers.
- **New language, culture, age, clinical group, or disability context**: Require population-specific evidence and accessibility review.
- **Several objects**: Distinguish fixed prompts from an item sample and preserve item, order, and generalization limits.
- **Instruction emphasizes quality but scoring target is fluency, or vice versa**: Expose the mismatch and return the decision to the user.
- **AI-assisted condition**: Require the approved scientific role, exact access rules, tool and model version, prompt or output handling, contamination control, privacy, consent, and data-retention decisions. Do not assume a no-assistance or web-search comparator.
- **Interaction logs proposed**: Minimize records, assess consent and external-service exposure, and require separate approval before collection.
- **Deception or cover story proposed**: Route to ethics review and require a debriefing decision. Do not adopt the source's cover story.
- **Copyrighted instructions or scale items requested**: Verify rights or create original construct-matched wording after separate selection.
- **Fixed cutoff or automated exclusion proposed**: Require prospective justification, error and bias review, and the user's ownership. Never exclude automatically.
- **Outcomes already inspected**: Label resulting changes and exclusions post hoc or exploratory as appropriate.
- **Sample size requested**: Route first to [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) when domain inputs are unresolved, then [statistical-power](../../skills/statistical-power/SKILL.md).
- **Scoring requested**: Preserve raw-data requirements and route to the verified `divergent-thinking-scoring` owner. Do not analyze responses here.
- **Platform unavailable**: Keep the platform-neutral specification and prepare a separate implementation handoff.
- **Implementation requested**: Require a separate platform-specific workflow, exact environment, privacy review, and approval.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when AUT has not been selected or must be compared with another paradigm.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when conditions, units, allocation, assignment, general counterbalancing, or broader timing structure are unresolved.
- Use [prediction-stress-test](../../skills/prediction-stress-test/SKILL.md) for falsifiability, counterexamples, boundary conditions, result implications, or bounded novelty questions.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) for participant, item, trial, session, reliability, data-loss, and effect-evidence input specification.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) for quantitative sample-size, power, MDE, or operating-characteristic calculation after inputs are approved.
- Use the verified `divergent-thinking-scoring` capability for validation and scoring of AUT responses.
- Use [research-critique](../../skills/research-critique/SKILL.md) to critique an existing AUT design rather than prospectively construct it.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for one bounded methodological claim and [paper-search](../../skills/paper-search/SKILL.md) for a separately approved evidence search.
- Route ethics, deception, vulnerable-population, privacy, information-security, rights, platform implementation, recruitment, and observed-data analysis to their approved owners.

Each destination begins its own workflow and gates. AUT Task Designer approval does not authorize another capability.

This skill does not choose AUT, alter the general design, calculate power, write copied instrument text, score responses, select exclusions after outcomes are visible, build or deploy a platform, recruit, compensate, operate AI or search tools, collect logs, search, or make a scientific conclusion for the user. Save a verified result only within the separately authorized content and destination. The scientific gates grant no write authority.

## Checks

The plan may specify:

- participant comprehension and interpretation of instructions;
- object familiarity, conventional-use understanding, cultural and language fit;
- response-entry usability, accessibility, device behavior, and data capture;
- timing distribution, fatigue, learning, and completion behavior;
- expected raw fields and protocol-version preservation;
- condition-access fidelity and contamination detection;
- whether planned checks behave as intended without inspecting the primary outcome;
- decision rules for prospective revision and when a change requires confirmatory-status review.

A pilot can test administration feasibility. It does not automatically validate the construct, supply a stable effect size, justify the final sample size, or authorize outcome-informed protocol changes.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Forthmann, B., Bürkner, P. C., Szardenings, C., Benedek, M., & Holling, H. (2019). A new perspective on the multidimensionality of divergent thinking tasks. *Frontiers in Psychology, 10*. https://doi.org/10.3389/fpsyg.2019.00985
- Lee, B. C., & Chung, J. (2024). An empirical investigation of the impact of ChatGPT on creativity. *Nature Human Behaviour, 8*. https://doi.org/10.1038/s41562-024-01953-1
- Meincke, L., Nave, G., & Terwiesch, C. (2025). ChatGPT decreases idea diversity in brainstorming. *Nature Human Behaviour, 9*. https://doi.org/10.1038/s41562-025-02173-x
- Nusbaum, E. C., Silvia, P. J., & Beaty, R. E. (2014). Ready, set, create: What instructing people to be creative reveals about the meaning and mechanisms of divergent thinking. *Psychology of Aesthetics, Creativity, and the Arts, 8*(4). https://doi.org/10.1037/a0036549
- Reiter-Palmon, R., Forthmann, B., & Barbot, B. (2019). Scoring divergent thinking tests: A review and systematic framework. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2). https://doi.org/10.1037/aca0000227
