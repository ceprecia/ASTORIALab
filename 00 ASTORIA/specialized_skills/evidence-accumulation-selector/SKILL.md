---
name: evidence-accumulation-selector
description: >-
  Compares DDM, LBA, race, and related evidence-accumulation model families for
  one approved choice-RT estimand without automatically selecting a model,
  fitting data, or interpreting latent parameters. Triggers: which evidence
  accumulation model fits, DDM versus LBA choice.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: behavior
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Evidence Accumulation Model Comparison

Compare candidate evidence-accumulation families without turning a decision
tree, trial-count rule, or package default into the user's model choice.

## Purpose

This is the Part 4 method-comparison owner for one approved nonclinical
choice-RT estimand. It compares DDM, LBA, race, and explicitly named variants
against task structure, response alternatives, timing, dependency, and
identifiability. It does not select a model, fit data, choose software, or
interpret latent parameters.

The user owns the question, task, response alternatives, predictions, model,
scaling, priors, fitting method, and claim. [drift-diffusion-model](../drift-diffusion-model/SKILL.md) owns a
selected DDM specification. [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential comparison
and uncertainty.

Activate only for exact `evidence-accumulation-selector` or an approved handoff
with full choice-RT data or a clearly bounded summary estimand. Do not trigger
from generic reaction-time, accuracy, or machine-learning requests.

In scope: model-family comparison for two or more discrete choices, speed-
accuracy tradeoffs, full RT distributions, race and ballistic alternatives,
and model-comparison planning. Out of scope: automatic selection, fitting,
clinical interpretation, continuous tracking, untimed accuracy-only tasks, and
go/no-go extensions without a separately selected model.

## Inputs

Obtain or mark missing: question, prediction, task, response alternatives,
timing and speed-accuracy instructions, trial-level or summary data, correct
and error RTs, participant and item grain, candidate families, assumptions,
parameter scaling, trial sufficiency, recovery, validation, comparison rule,
and outcome contact. If response alternatives, RT definition, data grain, or
candidate comparison boundary is missing, return **evidence-accumulation intake
incomplete**.

## Steps

### Gate 1: approve the comparison boundary

Show the task and response structure, estimand, data state, candidate families,
assumptions, parameterization, identifiability threats, recovery and
validation plan, comparison criterion, alternatives, outcome contact, and
limitations. Gate 1 authorizes comparison planning only.

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Response architecture | | | | |
| DDM, LBA, race, or named variant | | | | |
| Data and trial sufficiency | | | | |
| Parameters and scaling | | | | |
| Recovery and predictive checks | | | | |
| Comparison criterion | | | | |
| Permitted claim | | | | |

### Gate 2: approve one comparison specification

Ask the user to select, revise, or reject the candidate set, assumptions,
parameterization, recovery, validation, comparison criterion, reporting fields,
and permitted claim. Gate 2 authorizes a method specification only; it does not
authorize fitting, model selection by software, interpretation, or file writes.

Return:

```text
Evidence-Accumulation Model Comparison Specification
Question, prediction, estimand, and status:
Task, response alternatives, and timing:
Data grain and correct/error RT structure:
Candidate families and architecture assumptions:
Parameters, scaling, and identifiability:
Recovery and predictive checks:
Comparison criterion and exploratory state:
Reporting fields and permitted claim:
Known limitations and stop point:
```

## Boundaries

Comparison rules:

- Compare architecture, observation model, response alternatives, within- and
  across-trial variability, parameter constraints, and estimand before
  discussing software.
- DDM is a candidate for a specified two-boundary process; LBA or race models
  are candidates when the multi-accumulator architecture is theoretically
  defensible. Neither task format nor number of buttons proves a model.
- Treat trial counts and timing ranges as design evidence and identifiability
  questions, not universal pass/fail thresholds.
- Preserve correct and error RT distributions, missingness, exclusions,
  participant and condition dependence, and outcome-contact state.
- Require simulation-based recovery, predictive checks, and a prespecified
  comparison criterion. A lower information criterion is not by itself a
  confirmed cognitive explanation.

Stop for accuracy-only or untimed data; missing response alternatives or RT
definition; unbounded model-family requests; outcome-selected model choice
without an exploratory label; failed recovery or predictive checks; clinical or
person-level interpretation; or a request to fit, install, execute, or write.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
