---
name: cognitive-paradigm-design
description: >-
  Compares prospective cognitive or behavioral paradigm architectures for one
  user-supplied construct, question, hypothesis, or prediction and approved
  constraints. Use when the request, or a part coordinator, hands over an explicitly
  matching task. It maps construct and measurement demands, generates two to
  four evidence-labeled paradigm options when credible, exposes task impurity,
  parameter evidence, threats, and feasibility, and records only user-selected
  elements after two approval gates. It does not choose the paradigm, inherit
  catalog defaults, implement tasks or stimuli, calculate power, select an
  analysis, search, save, or analyze outcomes without separate approval.
  Triggers: design a cognitive paradigm for this construct, which behavioral
  paradigm fits.
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

# Cognitive Paradigm Design

Compare cognitive and behavioral task architectures without treating a familiar paradigm as the scientific answer.

## Purpose

`cognitive-paradigm-design` is the Part 3 canonical owner for prospective comparison and specification of general cognitive or behavioral paradigm architectures for one user-supplied scientific target.

It owns:

- mapping an intended construct to observable task demands, manipulations, comparators, and outcome candidates;
- comparing two to four credible paradigm families or variants when evidence supports alternatives;
- specifying candidate trial-event, stimulus-category, response-mode, practice, catch or comprehension, timing, order, and nuisance-control structures;
- exposing task impurity, alternative processes, construct limits, evidence gaps, feasibility, accessibility, fatigue, learning, demand, and measurement threats;
- producing a selection-bound Cognitive Paradigm Specification and selected task-specific handoff packets.

The user owns the construct, question, hypothesis, prediction, paradigm selection, operationalization, manipulation, comparator, primary outcome, estimand, task parameters, controls, exclusions, confirmatory status, interpretation, and scientific claims.

[experimental-design](../../skills/experimental-design/SKILL.md) owns the general design family, units, conditions, allocation, assignment, clustering, and broad timing structure. [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) owns cognitive and behavioral power-input specification. [statistical-power](../../skills/statistical-power/SKILL.md) owns numerical power and sample-size calculations.

Active task-specific designers own their selected task after this workflow. For example, [alternative-uses-task-designer](../alternative-uses-task-designer/SKILL.md) owns AUT-specific administration once AUT and the general design are approved, while [visual-search-array-generator](../visual-search-array-generator/SKILL.md) owns array-manifest generation after controlled-array visual search and its scientific parameters are approved.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `design my study`;
- `build this task`;
- `generate visual-search arrays`;
- `power this cognitive study`;
- `analyze my reaction times`;
- `critique this existing paradigm`;
- broad phrases such as `cognition`, `memory`, `attention`, `task`, `paradigm`, or `experiment`.

One run covers one primary construct and one bounded scientific target under one approved general design and population context.

Up to three tightly linked constructs may remain in one run only when the user identifies an inseparable measurement question and Gate 1 displays their distinct roles. Otherwise split them.

A named paradigm is not automatically an appropriate measure of the intended construct. A robust group-level effect does not establish reliable individual differences, construct purity, clinical validity, ecological validity, or transportability to a new population, modality, or setting.

## Inputs

Gather:

- The user's exact construct, question, hypothesis, or prediction;
- intended use, decision, and inquiry part;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) Design Specification or equivalent supplied constraints;
- population, age, language, culture, clinical or developmental context, and accessibility needs;
- setting, modality, device, equipment, supervision, duration, burden, and resource limits;
- candidate observable behavior, manipulation, comparator, outcome, contrast, estimand, and generalization target;
- whether the goal is a group effect, within-person change, individual differences, classification, threshold, latent process, or another use;
- supplied paradigm candidates, existing tasks, source evidence, norms, consensus guides, or implementation constraints;
- participant, item, trial, session, and site structure when known;
- outcome visibility, confirmatory status, protocol, preregistration, and deviations;
- approved evidence boundary, desired output, and stop point.
- requested visual form and detail, if relevant to the task.

Mark essential missing items `unknown`. Do not fill them from the external candidate's catalog or parameter tables.

## Candidate-family map

Use this compact map only to generate candidates for the approved construct. It is not a decision tree and contains no preferred route:

| Scientific demand | Example candidate families |
|---|---|
| Interference or conflict | Stroop, flanker, Simon, or task-specific alternatives |
| Spatial or temporal attention | Cueing, visual search, attentional-blink, or detection variants |
| Recognition, recall, false memory, or working memory | Recognition, recall, associative-list, change-detection, span, or updating variants |
| Perceptual sensitivity or threshold | Yes/no detection, forced choice, constant stimuli, staircase, or adaptive variants |
| Response withholding or cancellation | Go/no-go, stop-signal, or task-specific inhibition variants |
| Cognitive flexibility or updating | Task switching, rule shifting, n-back, or complex-span variants |
| Lexical or sentence processing | Lexical decision, priming, self-paced reading, eye tracking, or modality-specific variants |
| Risk, reward, or intertemporal choice | Learning, gambling, discounting, or model-based choice variants |
| Divergent-thinking performance | Alternative Uses Task or another construct-matched ideation task |

The examples are source candidates, not defaults. A paradigm absent from the map may be preferable. Load and verify only the selected candidate material.

## Steps

### 1. Build the Cognitive Paradigm Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and Part 3 task |
| Scientific target | The user's exact construct, question, hypothesis, or prediction |
| Intended use | Group effect, individual differences, change, classification, threshold, latent process, or another use |
| Approved design | Conditions, units, assignment, timing structure, and fixed constraints |
| Population | Age, language, culture, clinical or developmental context, and accessibility |
| Setting and modality | Lab, remote, behavioral, EEG, MEG, fMRI, device, and equipment constraints |
| Observable target | Candidate behavior, manipulation, comparator, outcome, contrast, and estimand |
| Generalization | Participants, items, settings, sessions, or other target populations |
| Candidate scope | Supplied paradigms and candidate families allowed for comparison |
| Measurement need | Sensitivity, reliability, validity, temporal precision, ecological relevance, or another criterion |
| Resources | Duration, burden, staffing, equipment, recruitment, and implementation limits |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied evidence that may be inspected |
| Excluded work | General design change, task implementation, stimulus generation, power, analysis selection, search, saving, and observed-data analysis |
| Stop point | Exact output or decision that ends the run |

If the general design, primary construct, intended use, or observable target is too unclear to compare paradigms, return the missing decisions to the user or prepare an [experimental-design](../../skills/experimental-design/SKILL.md) handoff.

### 2. Gate 1: approve the construct-to-paradigm boundary

Ask the user to approve or correct the Cognitive Paradigm Brief, candidate-family boundary, evidence plan, and comparison criteria.

Gate 1 authorizes only:

- inspection of the displayed supplied evidence;
- construct and measurement mapping;
- comparison of the approved paradigm families or variants;
- creation of evidence, threat, and feasibility records;
- preparation of response options.

It does not authorize:

- choosing a paradigm, manipulation, comparator, outcome, parameter, control, exclusion, or analysis;
- applying a catalog value as a default;
- implementing a task or generating stimuli;
- calculating power, searching, installing software, saving, or analyzing observed data.

If the construct, intended use, general design, population, modality, candidate boundary, outcome visibility, or evidence scope changes materially, rebuild the brief and repeat Gate 1.

### 3. Build the Construct and Measurement Map

| Field | Required content |
|---|---|
| Intended construct | The user's exact theoretical target |
| Observable behavior | What a participant does and what is recorded |
| Manipulation | Candidate change intended to vary the target process |
| Comparator | Candidate baseline or contrast and what it controls |
| Primary outcome | Candidate measure, scoring level, direction, and time scale |
| Estimand | Exact contrast or parameter the study would estimate |
| Task demands | Perception, memory, language, motor, strategy, motivation, and device demands |
| Alternative processes | Plausible processes producing the same observable pattern |
| Generalization | Participant, item, context, session, and construct claims supported |
| Measurement limit | What the candidate task cannot establish by itself |

No task is process-pure. Make mono-operation risk explicit when one task stands in for a broad construct.

Show a construct-to-task-to-recorded-measure schematic when it clarifies this map, preserving alternative processes and the inference limit. Add trial and comparison views beside the option matrix under the figures rules in Outputs; several views may explain different parts of the same candidate.

### 4. Build the Paradigm Option Matrix

Generate two to four `AI-generated paradigm option` entries only when scientifically credible. If one route is credible, explain why and do not invent alternatives. If none can be supported within the evidence boundary, stop with the exact evidence or specialist gap.

| Field | Required content |
|---|---|
| Option ID | Stable label |
| Paradigm or variant | Exact candidate family and configuration concept |
| Construct link | Why it could operationalize the target |
| Trial event | High-level cue, stimulus, delay, response, feedback, and interval structure |
| Manipulation and comparator | Candidate contrast and nuisance controls |
| Outcome candidates | Observable measures and intended estimand |
| Task impurity | Alternative processes and task-specific variance |
| Evidence basis | Exact verified source, user source, unverified catalog candidate, or unresolved |
| Population and modality fit | Match, translation, or specialist gap |
| Reliability and validity | Applicable evidence, intended-use match, and uncertainty |
| Feasibility | Burden, duration, fatigue, accessibility, equipment, and implementation |
| Tradeoff | What the option gains and sacrifices relative to another |
| Specialist handoff | Narrow owner needed after selection |

Do not rank options by familiarity, citation count, apparent standardness, or available software.

### 5. Build the Parameter and Evidence Register

Create one row per consequential parameter:

| Field | Required content |
|---|---|
| Parameter ID | Stable identifier |
| Parameter | Manipulation, stimulus, response, timing, proportion, practice, catch trial, order, feedback, or control |
| Candidate value or structure | Supplied value, evidence-supported range, or `unknown` |
| Provenance | The user supplied, verified exact source, verified translated source, external candidate, or AI-generated option |
| Applicability | Construct, paradigm, variant, population, modality, outcome, analysis, and setting match |
| Consequence | Construct, measurement, strategy, burden, or feasibility effect |
| Conflict | Source disagreement or competing rationale |
| Status | Eligible, eligible with translation, specialist-required, unresolved, or reject |

Every numerical value from the external source is `unverified candidate` until checked against the exact selected paradigm, variant, primary or consensus source, population, modality, outcome, and analysis.

Reject universal claims about timing, proportions, trials, practice, catch trials, counterbalancing, response deadlines, exclusion, or analysis. A parameter that is valid for one stop-signal, masking, cueing, staircase, or language task does not become a general cognitive-task rule.

### 6. Build the Threat and Feasibility Register

Assess:

- construct underrepresentation and construct-irrelevant variance;
- task impurity, strategy variation, and mono-operation bias;
- weak convergent, discriminant, criterion, ecological, or transport validity;
- group-effect versus individual-difference reliability mismatch;
- participant and stimulus sampling, fixed-item inference, pseudoreplication, and item effects;
- carryover, learning, fatigue, order, sequence, practice, and demand;
- stimulus matching, response mapping, base-rate, prevalence, expectancy, and contingency confounds;
- speed-accuracy tradeoffs, ceiling, floor, lapse, response bias, and missingness;
- population, language, culture, disability, device, remote-setting, clinical, and developmental mismatch;
- modality timing, movement, trial count, and artifact constraints;
- implementation fidelity, version drift, calibration, and data-capture requirements;
- evidence disagreement, missing current consensus, and unverified source parameters.

For each threat show affected option, evidence, severity, detectable indicator, mitigation candidates, residual risk, owner, and unresolved decision.

### 7. Present response options

For each consequential choice, offer only applicable options:

- retain an eligible paradigm or parameter;
- return the choice to the user;
- translate a source-supported element with displayed assumptions;
- compare or pilot selected candidates prospectively;
- request a bounded [research-literacy](../../skills/research-literacy/SKILL.md) audit or [paper-search](../../skills/paper-search/SKILL.md);
- prepare an [experimental-design](../../skills/experimental-design/SKILL.md), task-specific, [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md), [statistical-power](../../skills/statistical-power/SKILL.md), modality, implementation, ethics, or accessibility handoff;
- defer the specification.

Do not recommend one paradigm merely because it has a familiar name or complete catalog entry.

### 8. Gate 2: The user selects the paradigm route

Ask the user to select:

- paradigm or variant;
- construct operationalization, manipulation, comparator, outcome, and estimand;
- eligible parameter structures and control candidates;
- evidence translations and unresolved items;
- pilot, reliability, validity, and feasibility checks;
- selected specialist handoff packets.

Gate 2 authorizes only the selected elements for the Cognitive Paradigm Specification and selected handoff packets.

It does not authorize task or stimulus implementation, general design changes, numerical power, analysis selection, search, installation, saving, preregistration, data collection, or observed-data analysis.

Do not infer selection from silence.

### 9. Produce and verify the Cognitive Paradigm Specification

Return:

| Field | Required content |
|---|---|
| Approved scope | Construct, scientific target, intended use, population, setting, modality, design, and evidence boundary |
| Selected paradigm | Exact family, variant, and why the user selected it |
| Construct map | Operationalization, task demands, alternative processes, and inference limit |
| Trial architecture | High-level phase and event sequence |
| Manipulation and comparator | Selected contrast and nuisance controls |
| Stimulus and response | Categories, sampling, matching, response mode, mapping, and accessibility |
| Parameter register | Only Gate 2 selected parameters with evidence status |
| Outcomes and estimand | Selected measure and target without choosing the statistical model |
| Unit structure | Participants, items, trials, blocks, sessions, sites, and dependencies |
| Threats and residual risks | Selected mitigations and remaining limitations |
| Pilot and verification | Comprehension, difficulty, timing, reliability, validity, accessibility, and fidelity needs |
| Specialist implementation packet | Exact task-specific or modality-specific unresolved work |
| Open items | Evidence, user, specialist, ethics, implementation, power, or analysis gaps |
| Provenance | User statements, verified evidence, translations, catalog material, and AI-generated options kept separate |

Verify that:

- The user supplied or approved the scientific target and selected the paradigm;
- the selected paradigm is not described as process-pure;
- intended-use, population, modality, and setting match are explicit;
- instruction, scoring, outcome, and estimand are coherent or the mismatch remains visible;
- participant and item generalization claims match sampling and unit structure;
- every numerical parameter has exact applicable evidence or remains unresolved;
- no source conflict was hidden;
- no task or stimulus implementation, power calculation, analysis selection, search, save, or outcome analysis occurred;
- every handoff begins separately.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the recipient's applicable reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **Cognitive Paradigm Brief**
- **Construct and Measurement Map**, after Gate 1
- **Paradigm Option Matrix**
- **Parameter and Evidence Register**
- **Threat and Feasibility Register**
- **Response Options**
- **Cognitive Paradigm Specification**, only after Gate 2
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return the design results in the current task's requested form or under the recipient's existing reporting policy. Neither gate authorizes searching, installing software, task construction, stimulus generation, platform use, source modification, saving, data collection, or starting another capability.

Identify relevant privacy, ethics, rights, account, credential and implementation implications before acting. Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized save, use the destination selected for the task. Otherwise use the established project or area destination when the recipient's placement policy calls for it. Keep skill and system work in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved.

## Figures and examples

- Use the task's selected visual form and detail, then the recipient's applicable reporting policy. When neither specifies visuals, add only a view that clarifies the decision. Construct-to-measure schematics, trial-event sequences, condition-by-measure tables, and stimulus or response-category sketches can clarify different demands.
- Before Gate 1, illustrate only the supplied brief. After Gate 1, show candidate architecture and comparisons. After Gate 2, retain only selected elements in the specification. Present explanatory diagrams in the current task's requested form or under the recipient's existing reporting policy. Implemented tasks, generated stimulus sets and executable schedules are outside this capability. Saving requires separate approval.
- Carry the same candidate ID, construct, events, conditions, and notation through the views. Explain what to notice and whether arrows show event order, task demands, an assumed process, or measurement. Distinguish proposed mechanisms from recorded behavior and preserve competing processes; a neat diagram does not make a task process-pure.
- Begin with event order, then add a comparison or measurement view rather than crowding one diagram. Unknown timings remain `unknown`, and an order-only sequence states that spacing does not represent duration. Use a duration-scaled timeline only with supplied or approved timing values.
- Use schematic trial or stimulus-category examples to explain the candidate, labeling them illustrative. Do not turn the sketch into a stimulus manifest, select a response mapping, invent parameters, inherit catalog defaults, or depict unreported findings. A concrete object count in a sketch is not a chosen number of items or trials.
- Choose supported representations within the selected format. Tables, diagrams, and formulas are options. For a rendered formula, define quantities, units, and assumptions, and keep display math outside table cells. Use only supplied or specified measurement relationships. Visuals stay within the approved construct, evidence, and action scope.
- Check every view against the Construct and Measurement Map, option matrix, and Parameter and Evidence Register. Preserve parameter provenance, modality limits, task impurity, candidate status, and unresolved choices. Inspect labels, arrow meanings, spacing, and rendering where possible; give a useful text/table alternative if rendering cannot be checked.

## Boundaries

- **No user-supplied construct or scientific target**: Stop.
- **General design unresolved**: Route to [experimental-design](../../skills/experimental-design/SKILL.md).
- **One credible paradigm**: Explain the constraint and do not invent alternatives.
- **No credible paradigm within supplied evidence**: Preserve the gap and propose a bounded evidence or specialist handoff.
- **Paradigm absent from the source catalog**: Evaluate it on the approved criteria; do not force a listed task.
- **Task already selected**: Confirm selection and route task-specific parameterization to its Active owner.
- **Whole existing task submitted for critique**: Route to [research-critique](../../skills/research-critique/SKILL.md).
- **Broad construct represented by one task**: Disclose mono-operation and task-impurity limits.
- **Individual-differences use**: Require reliability and between-person variance evidence for the exact score, population, setting, and use. A robust group effect is insufficient.
- **Fixed stimuli**: Restrict inference to those stimuli unless sampling and analysis justify a broader item population.
- **New language, culture, age, clinical group, or disability context**: Require population-specific validity, accessibility, and parameter evidence.
- **Source supplies a fixed number or standard**: Mark it unverified until exact-match verification.
- **Sources disagree**: Preserve the conflict for the user; do not average or choose silently.
- **Outcome already inspected**: Do not relabel task or parameter changes confirmatory.
- **EEG, MEG, or fMRI context**: Require the modality-specific timing, artifact, event, run, and power owner.
- **Power requested**: Route to [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md), then [statistical-power](../../skills/statistical-power/SKILL.md).
- **Task or stimulus implementation requested**: Use the selected Active task-specific owner or disclose the gap.
- **Analysis requested**: Route to Part 4 after the design and analysis plan are approved.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

When the user selects a task-specific handoff, include:

- approved Cognitive Paradigm Specification;
- exact construct, question, hypothesis, or prediction;
- selected paradigm and variant;
- approved general design, manipulation, comparator, outcome, and estimand;
- population, language, culture, accessibility, setting, and modality;
- selected trial architecture, stimulus categories, response mode, and eligible parameters;
- evidence statuses, conflicts, assumptions, threats, and residual gaps;
- privacy, ethics, rights, platform, and equipment constraints;
- desired task-specific output and stop point.

Show the packet and ask for separate approval before the destination begins its own Gate 1.

Boundaries and handoffs:

- Use [experimental-design](../../skills/experimental-design/SKILL.md) when the general design family, units, conditions, allocation, assignment, clustering, or broad timing structure is unresolved.
- Use [prediction-stress-test](../../skills/prediction-stress-test/SKILL.md) for prediction falsifiability, counterexamples, boundary conditions, outcome implications, or bounded novelty work.
- Use [alternative-uses-task-designer](../alternative-uses-task-designer/SKILL.md) after AUT is selected for AUT-specific administration design.
- Use [visual-search-array-generator](../visual-search-array-generator/SKILL.md) after controlled-array visual search is selected and its scientific parameters are approved for deterministic layout-manifest generation and validation.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) after a behavioral or cognitive task and neural estimand are approved for model-aware task-fMRI timing design.
- Use the verified `self-paced-reading-designer` or `eeg-paradigm-designer` when the selected task fits. Verify current availability for other task-specific designers; report a capability gap only when no matching installed or catalog capability exists.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) for participant, item, trial, session, reliability, data-loss, and effect-evidence input specification.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) for numerical sample-size, power, MDE, or operating-characteristic calculation after inputs are approved.
- Use [bids](../bids/SKILL.md) after the task events and scientific labels are approved when
  the unresolved work is version-pinned BIDS event, metadata, provenance,
  privacy, or compliance specification.
- Use [research-critique](../../skills/research-critique/SKILL.md) to critique an existing task or paradigm rather than prospectively compare architectures.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for one bounded methodological claim and [paper-search](../../skills/paper-search/SKILL.md) for a separately approved evidence search.
- Route statistical-model selection, trimming, observed-data diagnostics, and inference to an approved Part 4 capability.

Each destination begins its own workflow and gates. Cognitive Paradigm Design approval does not authorize another capability.

This skill does not generate or revise the user's hypothesis, select the paradigm, alter the general design, apply unverified defaults, implement tasks or stimuli, calculate power, select the statistical analysis, search, install software, collect data, analyze outcomes, or make a scientific conclusion for the user. Save a verified result only within the separately authorized content and destination. The scientific gates grant no write authority.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Hedge, C., Powell, G., & Sumner, P. (2018). The reliability paradox: Why robust cognitive tasks do not produce reliable individual differences. *Behavior Research Methods, 50*. https://doi.org/10.3758/s13428-017-0935-1
- Schwaighofer, M., Fischer, F., & Bühner, M. (2014). A task is a task is a task: Putting complex span, n-back, and other working memory indicators in psychometric context. *Frontiers in Psychology, 5*. https://doi.org/10.3389/fpsyg.2014.01475
- Verbruggen, F., Aron, A. R., Band, G. P. H., et al. (2019). A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. *eLife, 8*. https://doi.org/10.7554/eLife.46323
- Westfall, J., Kenny, D. A., & Judd, C. M. (2014). Statistical power and optimal design in experiments in which samples of participants respond to samples of stimuli. *Journal of Experimental Psychology: General, 143*(5). https://doi.org/10.1037/xge0000014
- Zorowitz, S., & Niv, Y. (2023). Improving the reliability of cognitive task measures: A narrative review. *Biological Psychiatry: Cognitive Neuroscience and Neuroimaging, 8*(8). https://doi.org/10.1016/j.bpsc.2023.02.004
