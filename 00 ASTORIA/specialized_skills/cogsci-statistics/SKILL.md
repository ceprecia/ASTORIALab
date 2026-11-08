---
name: cogsci-statistics
description: >-
  Compares statistical method families for one bounded cognitive-science or
  neuroscience estimand and produces a user-selected Analysis Method
  Specification. Use when the request, or a part coordinator, hands over an exact
  method-guidance handoff. It exposes observation units, dependency structure,
  outcome distribution, missingness, multiplicity, estimand alignment,
  confirmatory status, assumptions, diagnostics, uncertainty, and absence-claim
  requirements without fitting a model, choosing software, changing thresholds
  after outcomes are seen, or interpreting results. Triggers: which statistical
  method fits my estimand, compare statistical approaches for this analysis.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: behavior
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Cognitive Science Statistics

Compare defensible statistical method families for one approved cognitive or
neuroscience estimand. Preserve the distinction between method reasoning,
software implementation, and scientific interpretation.

## Purpose

`cogsci-statistics` owns:

- mapping one approved estimand to plausible statistical method families;
- checking participant, item, trial, site, session, region, channel, and time
  dependencies;
- comparing outcome distributions, link functions, aggregation choices,
  repeated-measures structures, multilevel structures, resampling approaches,
  Bayesian approaches, and prespecified absence tests when applicable;
- exposing multiplicity, circularity, missingness, exclusion, convergence,
  sensitivity, and reporting implications;
- producing one selection-bound Analysis Method Specification.

The user owns the question, hypothesis, prediction, estimand, confirmatory status,
outcome role, exclusions, thresholds, multiplicity family, model choice,
priors, smallest effect size of interest, interpretation, and claims.

[research-literacy](../../skills/research-literacy/SKILL.md) owns evidence audits for explicit claims.
[statistical-power](../../skills/statistical-power/SKILL.md) owns prospective operating-characteristic calculations.
`statistical-analysis` or a selected software adapter owns implementation after
the method specification is approved.

Use only for the exact trigger:

- `cogsci-statistics`

Do not trigger from `statistics`, `analyze`, `run a model`, `significant`,
`mixed model`, `ANOVA`, `Bayesian`, `fMRI`, `EEG`, or another broad method or
modality word.

Do not use this skill to:

- invent a hypothesis or outcome;
- choose a method from package availability;
- inspect outcomes to optimize a confirmatory model;
- fit, tune, compare, or repair models;
- select thresholds or priors;
- interpret coefficients, p-values, intervals, Bayes factors, maps, or
  scientific meaning;
- treat nonsignificance as evidence of absence.

One review covers one estimand and one coherent dependency structure. Obtain or
mark missing:

- the approved question, prediction, and estimand;
- confirmatory, preregistered, registered-report, or exploratory status;
- outcome role, scale, support, censoring, and measurement reliability;
- participant, item, trial, session, site, family, region, channel, time, and
  other sampling or clustering units;
- fixed and varying predictors, interactions, contrasts, and nuisance terms;
- repeated measures, crossing, nesting, imbalance, missingness, and planned
  exclusions;
- sampling design, allocation, stopping rule, and data already inspected;
- multiplicity family and intended error criterion;
- effect-evidence basis, uncertainty target, and any absence claim;
- candidate implementation environment only as a later feasibility constraint.

If the estimand, outcome role, dependency structure, or confirmatory status is
missing, stop with **Method intake incomplete**.

## Steps

### 1. Build the Method Intake Record

Separate:

| Field | Record |
|---|---|
| user-owned scientific decision | Question, hypothesis, prediction, estimand, outcome role |
| Design grain | Participants, items, trials, sessions, sites, regions, channels, time |
| Outcome behavior | Scale, support, skew, bounds, censoring, zero inflation, reliability |
| Dependence | Crossing, nesting, repeated measures, autocorrelation, spatial structure |
| Analysis status | Confirmatory, preregistered, deviated, or exploratory |
| Data contact | What outcomes or diagnostics have already been viewed |
| Multiplicity | Tests, contrasts, search space, family, and criterion |
| Missingness and exclusions | Rules, timing, causes, and sensitivity needs |
| Absence claim | Prespecified smallest effect or Bayesian target, or not justified |
| Stop point | Method specification only |

Do not convert a vague research aim into a statistical estimand.

### 2. Gate 1: approve the bounded method review

Show the intake record, missing fields, exact sources to inspect, and proposed
comparison boundary. Ask the user to approve:

- the fixed scientific inputs;
- the confirmatory or exploratory label;
- the candidate method families to compare;
- any bounded literature or documentation lookup;
- the fact that no model will be fitted.

Gate 1 authorizes only the displayed method review. It does not authorize data
access, software execution, package installation, model selection, or saving.

### 3. Method fit for the estimand

Compare supported routes only when the task leaves a material method choice
open. When one method is selected or eligible, document its fit without adding
alternatives. Possible families include:

- aggregate repeated-measures models;
- trial-level generalized or multilevel models;
- distributional or survival-style models for bounded, censored, or timed
  outcomes;
- permutation or randomization procedures compatible with the exchangeability
  structure;
- Bayesian generative or hierarchical models with explicit prior checks;
- equivalence or interval-null procedures for a prespecified absence claim.

For each route state:

- the estimand it answers and does not answer;
- observation and dependency grain;
- assumptions and identification requirements;
- missingness and exclusion behavior;
- multiplicity implications;
- diagnostics and sensitivity checks;
- interpretability and reporting consequences;
- implementation burden and unresolved evidence.

Do not rank routes by convenience or available software.

### 4. Document dependence and assumptions in the decision record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present a Method Comparison Matrix:

| Route | Estimand fit | Dependence fit | Distribution fit | Assumptions | Diagnostics | Multiplicity | Sensitivity | Main limitation |
|---|---|---|---|---|---|---|---|---|

Always inspect these threats:

- averaging over a sampled participant, item, trial, or site source;
- random-effects structure unsupported by the design or data information;
- outcome transformations that change the estimand;
- binary or bounded outcomes analyzed through an incompatible Gaussian model;
- nonindependent selection and testing;
- outcome-dependent exclusions, contrasts, regions, windows, or thresholds;
- exchangeability violations in resampling;
- unreported convergence, singularity, prior, or predictive-check failures;
- multiplicity families defined after viewing results;
- nonsignificance presented as absence.

Conflicting defensible approaches remain visible. Do not manufacture consensus.

### 5. Gate 2: The user selects the method route

Ask the user to select, revise, or reject a route and approve:

- the estimand and analysis status;
- model family and dependency structure;
- predictor, contrast, nuisance, and multiplicity specification;
- diagnostic, sensitivity, and failure criteria;
- absence-testing method when relevant;
- implementation owner and stop point.

Do not infer selection from silence. If observed outcomes caused a
confirmatory choice to change, record the deviation and relabel the affected
work exploratory.

### 6. Return the selected method specification

Return:

```text
Cognitive-Neuroscience Analysis Method Specification
Scope:
Scientific decisions supplied by the user:
Confirmatory or exploratory status:
Estimand and outcome role:
Observation and dependency structure:
Selected method family:
Model terms and contrasts:
Missingness and exclusion rules:
Multiplicity family and criterion:
Diagnostics and sensitivity checks:
Absence-claim method, if any:
Known limitations:
Implementation owner:
Verification requirements:
Stop conditions:
```

The specification is the only integrated output. Hand it to
`statistical-analysis` or the selected implementation adapter only after that
capability is verified Active and separately invoked.

## Boundaries

- `p > alpha` is not significant. Do not call it marginal, approaching
  significance, a trend, or nearly supported.
- Exact p-values do not replace effect estimates, uncertainty, diagnostics,
  or design-based reasoning.
- Nonsignificance does not establish the null.
- Evidence for absence requires a justified prespecified interval-null,
  equivalence, or Bayesian method.
- Post hoc work remains exploratory and cannot become confirmatory
  retroactively.
- Record preregistration deviations and outcome-dependent choices.
- No random-effects structure, transformation, distribution, correction,
  prior, cutoff, or diagnostic threshold is a universal default.
- Successful computation does not establish model validity or a scientific
  conclusion.

## Cognitive-neuroscience method decisions

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **Evidence, assumption, diagnostic, sensitivity, and limitation fields.** Build the Method Comparison Matrix and threat audit. This makes the selection inspectable. This leaves genuine conflicts unresolved. This does not independently reproduce every cited study.
- **Labeled route cards.** Compare only method families applicable to the fixed estimand. This preserves real alternatives without method sprawl. This requires a complete intake first. This does not simulate operating behavior.
- **Verified Analysis Method Specification.** Integrate only the user's selected fields into the specification. This keeps scientific and implementation choices user-owned. This defers fitting to another capability. This cannot establish model adequacy from a specification.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Executed model and diagnostic record.** Fit and diagnose the selected model. This tests the specification against data. This introduces data access, software, and outcome-contact risks. This belongs to a separately invoked implementation owner.
- **Independent reproduction appendix.** Reproduce selected literature simulations and diagnostics. This tests portability of source claims. This requires code, environments, and a separate execution review. Reproduction cannot prove fit to the user's design.
- **Route cards plus simulation record.** Add design-based simulation for each plausible family. This reveals finite-sample behavior. This adds implementation, compute, and validation burden. This still depends on supplied data-generating assumptions.

## Checks

- **Positive:** a trial-level accuracy estimand with participants and sampled
  items yields applicable model-family options and no fit.
- **Negative:** `analyze these data` does not trigger this skill.
- **Edge:** outcome-dependent trimming or an already viewed contrast is
  recorded as a deviation and the affected work remains exploratory.
- **Absence:** a requested null claim without a smallest effect or justified
  Bayesian target stops as unsupported.
- **Overlap:** prospective power returns to [statistical-power](../../skills/statistical-power/SKILL.md); claim audit
  returns to [research-literacy](../../skills/research-literacy/SKILL.md); software execution waits for a verified
  implementation owner.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Barr et al. (2013). https://doi.org/10.1016/j.jml.2012.11.001
- Jaeger (2008). https://doi.org/10.1016/j.jml.2007.11.007
- Kriegeskorte et al. (2009). https://doi.org/10.1038/nn.2303
- Lakens (2017). https://doi.org/10.1177/1948550617697177
- Lo & Andrews (2015). https://doi.org/10.3389/fpsyg.2015.01171
- Maris & Oostenveld (2007). https://doi.org/10.1016/j.jneumeth.2007.03.024
- Matuschek et al. (2017). https://doi.org/10.1016/j.jml.2017.01.001
