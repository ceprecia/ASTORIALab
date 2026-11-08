---
name: signal-detection-analysis
description: >-
  Compares and specifies one approved nonclinical signal-detection-theory
  analysis for a defined behavioral or cognitive binary, forced-choice, rating,
  or same-different estimand. It separates sensitivity, criterion, paradigm,
  correction, model, aggregation, and inference decisions without choosing
  the user's question, computing results, fitting a model, interpreting a person, or
  silently treating accuracy as sensitivity. Triggers: signal detection analysis
  of my task, compute d prime and criterion.
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
  updated: "2026-10-29"
---

# Signal Detection Analysis

Specify one signal-detection analysis without converting a familiar formula,
benchmark, or correction rule into an unapproved scientific decision.

## Purpose

This is the conditional Part 4 method owner for one approved cognitive or
behavioral signal-detection estimand. It owns the 2x2 or rating-data audit,
paradigm and estimand comparison, sensitivity and criterion definitions,
extreme-rate handling, aggregation and reporting plan, and bounded statistical
handoff. It does not compute the data, fit a model, choose the hypothesis,
design the task, or interpret a person.

The user owns the question, target, task, stimulus classes, response mapping,
confirmatory status, population, base rates, payoffs, measure, correction,
model, aggregation, inference, and claim. [experimental-design](../../skills/experimental-design/SKILL.md) owns task
design and [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential methods, dependence,
multiplicity, and statistical interpretation.

Activate only for exact `signal-detection-analysis` or an approved handoff
with the task, response structure, stimulus classes, and estimand stated. Do
not trigger from `accuracy`, `hit rate`, `false alarm`, `d-prime`, `d'`,
`ROC`, `bias`, or a generic statistics request.

In scope: yes/no signal-present versus signal-absent, true 2AFC or 2IFC,
confidence-rating ROC, same-different, ABX, and related nonclinical SDT
estimands when the paradigm and model are explicitly defined. Out of scope:
multi-class responses without a selected extension, continuous outcomes,
missing or unknown noise classes, diagnostic accuracy, clinical classification,
person-level assessment, and automatic conversion of any task into SDT.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Scientific contract | Question, prediction, estimand, status, population, and permitted claim |
| Paradigm | Yes/no, true 2AFC/2IFC, rating, same-different, ABX, or selected extension |
| Trial structure | Signal and noise classes, response labels, counts, base rates, payoffs, blocks, conditions, and dependence |
| Data state | Trial-level contingency cells or rating distribution, missingness, exclusions, and provenance |
| Model boundary | Equal or unequal variance, nonparametric or parametric ROC, observer assumptions, and alternatives |
| Measure boundary | Sensitivity, criterion or likelihood ratio, metacognitive measure, and units |
| Extreme cells | Zero or one rates, correction candidate, reason, and sensitivity plan |
| Aggregation and inference | Participant and condition grain, hierarchical or summary route, multiplicity, and statistical owner |
| Outcome contact | Whether paradigm, correction, or measure was chosen after seeing outcomes |

If the paradigm, response mapping, class structure, counts, estimand, model,
or outcome-contact state is missing, return **SDT analysis intake incomplete**.
Do not infer a 2AFC design from two response labels or infer a signal/noise
class from a file column.

## Steps

### Gate 1: approve the SDT estimand boundary

Show the scientific contract, paradigm, response mapping, cell structure,
denominators, model assumptions, candidate sensitivity and criterion measures,
extreme-rate state, aggregation grain, statistical handoff, alternatives,
limitations, and outcome-contact state. Gate 1 authorizes method comparison
only, not data calculation or model fitting.

### Build the SDT decision ledger

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Paradigm and response mapping | | | | |
| Sensitivity estimand | | | | |
| Criterion estimand | | | | |
| Extreme-cell handling | | | | |
| Equal or unequal variance | | | | |
| ROC or rating model | | | | |
| Aggregation grain | | | | |
| Statistical and multiplicity handoff | | | | |

Do not fill a row from a package default, benchmark, or source recipe.

### Gate 2: approve one complete SDT specification

Ask the user to select, revise, or reject the paradigm, measure pair, correction
and sensitivity route, variance or ROC model, aggregation, reporting fields,
statistical handoff, and permitted claim. Gate 2 authorizes a chat-based
specification only. It does not authorize data access, calculations, model
fitting, interpretation, or file writes.

Return:

```text
SDT Analysis Method Specification
Question, prediction, estimand, and status:
Paradigm and response mapping:
Signal and noise classes with denominators:
Trial, participant, condition, and dependence grain:
Sensitivity measure and assumptions:
Criterion or bias measure and assumptions:
Extreme-cell correction and sensitivity route:
Equal or unequal variance and ROC model:
Aggregation and statistical handoff:
Outcome-contact and deviation state:
Reporting fields and permitted claim:
Known limitations and stop point:
```

Stop after the specification and hand off implementation to a separately
approved statistical or software capability.

## Boundaries

### Separate the four cells

For a binary yes/no design, preserve hits, misses, false alarms, and correct
rejections separately. Report denominators by condition and participant.
Accuracy alone cannot distinguish sensitivity from criterion placement.

### Match the measure to the paradigm

- For yes/no data, compare an approved sensitivity measure such as d' with an
  approved criterion measure such as c, c-prime, or a likelihood-ratio form.
  State equal-variance assumptions and the permitted claim.
- For true 2AFC or 2IFC, proportion correct has a different sampling and bias
  structure. Do not manufacture an independent false-alarm rate or criterion
  measure. Any conversion to a d-prime scale must be selected and justified.
- For confidence ratings, preserve the complete rating-by-class table and
  compare ROC, zROC, parametric, and nonparametric routes as applicable.
- Same-different and ABX require a selected observer model. Do not borrow a
  yes/no or 2AFC formula by analogy.

The task's response labels do not establish the paradigm. A single stimulus
with left/right labels is not automatically 2AFC.

### Extreme rates and corrections

When a rate is zero or one, the ordinary z transform is infinite. Compare
prospective correction or model routes, record their assumptions, and require
a sensitivity analysis when the correction could change the estimand. Do not
make a universal log-linear, half-trial, or other correction rule. Preserve
the original cell counts and corrected values separately.

### Equal and unequal variance

Standard d-prime is tied to an equal-variance Gaussian observer model. A rating
ROC or zROC can motivate an unequal-variance route, but a slope, visual shape,
or literature average does not prove the model for the user's data. Expose model
fit, identifiability, sampling uncertainty, and alternative interpretations.

### Criterion and bias language

Criterion location is descriptive relative to the specified model. Do not call
it irrational bias, diagnostic bias, strategy failure, or a stable trait
without a separately supported interpretation and design. Base rates, payoffs,
instructions, and condition changes can shift criterion rationally.

### Aggregation and inference

Preserve the trial and participant grain. Do not compute a pooled grand d-prime
or average participant d-primes by default. Route dependence, hierarchical
models, uncertainty, multiplicity, missingness, and evidence for absence to
[cogsci-statistics](../cogsci-statistics/SKILL.md). SDT measures are not automatically normally distributed,
independent, or comparable across paradigms.

Stop for clinical or diagnostic interpretation; missing class or response
mapping; a false 2AFC label; multi-class or continuous outcomes without a
selected extension; no noise distribution; outcome-selected measure or
correction without an exploratory label; pooled data that destroys dependence;
unsupported variance or ROC assumptions; a request to compute or fit results;
or a request to interpret criterion as a person-level trait.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Green, D. M., & Swets, J. A. (1966). *Signal detection theory and psychophysics*. Wiley.
- Hautus, M. J. (1995). Corrections for extreme proportions and their biasing effects on estimated values of d′. *Behavior Research Methods, Instruments, & Computers, 27*, 46–51. https://doi.org/10.3758/BF03203619
- Macmillan, N. A., & Creelman, C. D. (2005). *Detection theory: A user’s guide* (2nd ed.). Lawrence Erlbaum Associates. https://doi.org/10.4324/9781410611147
- Macmillan, N. A., & Kaplan, H. L. (1985). Detection theory analysis of group data: Estimating sensitivity from average hit and false-alarm rates. *Psychological Bulletin, 98*(1), 185–199. https://pubmed.ncbi.nlm.nih.gov/4034817/
- Maniscalco, B., & Lau, H. (2012). A signal detection theoretic approach for estimating metacognitive sensitivity from confidence ratings. *Consciousness and Cognition, 21*(1), 422–430. https://doi.org/10.1016/j.concog.2011.09.021
- Stanislaw, H., & Todorov, N. (1999). Calculation of signal detection theory measures. *Behavior Research Methods, Instruments, & Computers, 31*, 137–149. https://doi.org/10.3758/BF03207704
