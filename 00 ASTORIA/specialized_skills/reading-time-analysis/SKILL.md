---
name: reading-time-analysis
description: >-
  Specifies one approved nonclinical reading-time analysis by separating the
  reading measure, event and region definitions, preprocessing, exclusions,
  baseline, aggregation, model, and claim boundaries without choosing the
  linguistic construct, analyzing data, or interpreting a reader. Triggers:
  analyze my reading times, reading time preprocessing and regions.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: analysis
  modality: behavior
  dependencies: ""
  requires: ""
  gates: running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Reading Time Analysis

Specify one reading-time analysis without turning a familiar eye-tracking or
self-paced-reading workflow into an unapproved theory test.

## Purpose

This is the conditional Part 4 method owner for one approved nonclinical
reading-time estimand. It owns event and region definitions, measure selection,
preprocessing and exclusion comparisons, baseline specification, aggregation,
model comparison, and claim boundaries. It does not choose the user's linguistic
construct, design the task, access or analyze data, select a statistical model
silently, or interpret a reader.

The user owns the question, prediction, construct, population, task, materials,
confirmatory status, measure, exclusion, baseline, aggregation, model, and
claim. [experimental-design](../../skills/experimental-design/SKILL.md) owns task and stimulus design. [cogsci-statistics](../cogsci-statistics/SKILL.md)
owns inferential dependence, multiplicity, uncertainty, and statistical
interpretation.

Activate only for exact `reading-time-analysis` or an approved handoff with a
named reading measure and event structure. Do not trigger from generic
"reading," "reaction time," "language analysis," or a broad statistics request.

In scope: self-paced reading, eye-tracking first-pass and later-pass measures,
word or region reading times, regressions, skipping, fixation counts, and
related nonclinical reading-time estimands. Out of scope: clinical or
diagnostic interpretation, comprehension scoring without a selected reading
estimand, speech or motor reaction time, neural signal analysis, and automatic
conversion between measures.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Scientific contract | Question, prediction, construct, status, population, and permitted claim |
| Task and modality | Self-paced reading, eye tracking, or selected modality; apparatus and sampling |
| Event structure | Word or region boundaries, interest areas, trial timing, displays, and rereading rules |
| Measure | First fixation, gaze duration, go-past, regression path, total time, skipping, fixation count, or selected measure |
| Data state | Trial and participant grain, missingness, blinks, track loss, exclusions, and provenance |
| Preprocessing | Unit conversion, invalid-trial rules, latency cutoffs, transformations, and outlier policy |
| Baseline | Control condition, pre-target baseline, covariate, or no baseline with justification |
| Aggregation and inference | Item and participant structure, random effects or summary route, multiplicity, and statistical owner |
| Outcome contact | Whether event, measure, exclusion, baseline, or model was chosen after seeing outcomes |

If the event boundaries, measure, units, participant or item grain, or outcome-
contact state is missing, return **reading-time analysis intake incomplete**.
Do not infer a region, baseline, or psychological process from column names.

## Steps

### Gate 1: approve the reading estimand boundary

Show the scientific contract, modality, event and region definitions, measure,
units, preprocessing and exclusions, baseline, confounds, aggregation grain,
candidate model routes, alternatives, limitations, and outcome-contact state.
Gate 1 authorizes method comparison only, not data access or computation.

### Build the reading-time decision ledger

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Event and region boundaries | | | | |
| Reading-time measure | | | | |
| Unit and preprocessing | | | | |
| Exclusions and sensitivity | | | | |
| Baseline and confounds | | | | |
| Participant and item grain | | | | |
| Model and statistical handoff | | | | |
| Permitted claim | | | | |

Do not fill a row from a package default, benchmark, or post hoc pattern.

### Gate 2: approve one complete specification

Ask the user to select, revise, or reject the event definitions, measure,
preprocessing, exclusions, baseline, aggregation, model route, reporting
fields, and permitted claim. Gate 2 authorizes a chat-based specification only;
it does not authorize data access, computation, model fitting, interpretation,
or file writes.

Return:

```text
Reading-Time Analysis Method Specification
Question, prediction, construct, and status:
Task, modality, event and region definitions:
Measure, units, and estimand:
Preprocessing, exclusions, and sensitivity route:
Baseline and named confounds:
Participant, item, and trial dependence:
Model and statistical handoff:
Outcome-contact and deviation state:
Reporting fields and permitted claim:
Known limitations and stop point:
```

Stop after the specification and hand off implementation to a separately
approved statistical or software capability.

## Boundaries

### Preserve event and region identity

Keep the mapping from display event to word or region, item, condition,
participant, and trial. Distinguish a word-level measure from a region-level
sum or mean. Do not merge regions because they appear adjacent or because a
software export has already aggregated them.

### Match the measure to the question

- First fixation and first-pass measures describe early processing under the
  selected event definition; they do not establish a discrete early process.
- Go-past or regression-path measures include movement beyond the target and
  require an explicit treatment of rereading and display boundaries.
- Total time and later-pass measures include rereading and should not be
  described as purely early or lexical without a separate argument.
- Skipping and fixation counts are event or count outcomes with different
  missingness and exposure structures. Do not force them into a continuous
  latency analysis.

### Preprocessing and exclusions

Preserve raw timing, units, missingness, blinks or track loss, and exclusion
reasons. Compare prospective rules and sensitivity routes for implausible
latencies, short or long trials, and participant or item exclusions. A
transformation, trimming rule, or software default is not a scientific
justification.

### Baselines and confounds

State whether a baseline is a control condition, pre-target measure, covariate,
or none. Surface word length, frequency, predictability, position, display
duration, sentence difficulty, skipping opportunity, and trial order when they
could alter the estimand. A baseline adjustment does not automatically remove
construct confounding.

### Aggregation and inference

Preserve participant and item dependence. Compare trial-level hierarchical,
mixed-effects, or justified summary routes without silently selecting one.
Route distribution, missingness, multiplicity, and uncertainty to
[cogsci-statistics](../cogsci-statistics/SKILL.md). Do not call a longer latency evidence of a specific
mental process without a supported construct-to-measure bridge.

Stop for clinical or diagnostic interpretation; missing event boundaries or
units; a request to infer a mental process from latency alone; unapproved
outcome-selected trimming or baseline adjustment; pooled data that destroys
participant or item dependence; incompatible count or latency outcomes; a
request to compute or fit results; or a request to interpret reading time as a
person-level trait.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
