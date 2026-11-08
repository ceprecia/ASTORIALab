---
name: statistical-power
description: >-
  Quantifies prospective sample-size, power, minimum-detectable-effect, and
  operating-characteristic scenarios for one approved design and analysis
  specification. Use when the request, or a part coordinator, hands over a complete
  matching packet. It exposes effect-basis provenance, assumptions, units,
  sensitivity, numerical method, and uncertainty, then calculates only
  user-selected scenarios after two approval gates. It does not choose the
  design, estimand, effect basis, error rates, target power, final sample size,
  analysis, or scientific conclusion, and it does not install packages, analyze
  observed outcomes, search, save, or start another capability without separate
  approval. Triggers: power analysis for this design, how many participants do I
  need.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: power
  modality: any
  dependencies: ""
  requires: ""
  gates: choosing the sample size
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Statistical Power

Quantify prospective operating characteristics without turning a calculation into a scientific decision.

## Purpose

`statistical-power` is the Part 3 canonical owner for general quantitative sample-size, power, minimum-detectable-effect, and operating-characteristic calculations for one already-approved design and analysis specification.

It owns:

- translating approved scientific and design inputs into explicit calculation scenarios;
- distinguishing required analyzed units, required enrolled units, achieved design power under prospective assumptions, and minimum detectable effects;
- comparing justified analytic, numerical, or simulation-based calculation routes;
- calculating only user-selected scenarios through a validated implementation;
- exposing effect-basis provenance, sensitivity, numerical uncertainty, assumptions, unit definitions, and limitations;
- producing a reproducible Power Planning Record.

The user owns the question, hypothesis, prediction, primary outcome, estimand, design, planned analysis, effect basis, alpha or other error rule, multiplicity strategy, target power or operating characteristic, sidedness, allocation, attrition assumption, feasible resource bound, final sample size, interpretation, and scientific claims.

[experimental-design](../experimental-design/SKILL.md) owns the design structure. [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) owns cognitive and behavioral power-input specification. Neuroimaging power capabilities own modality-specific spatial, correction, first-level, second-level, reliability, and pipeline assumptions. Part 4 owns analysis of observed data.

Use this skill when the user names it or the bounded request matches its
frontmatter description and trigger meaning. A verified coordinator or
capability handoff may invoke the same matching task.

[research-coordinator](../research-coordinator/SKILL.md) or another verified Active capability may route a complete, explicitly matching packet from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `design my experiment`;
- `what effect size should I use`;
- `pick alpha and power`;
- `analyze these data`;
- `why was my result nonsignificant`;
- broad phrases such as `sample size`, `power`, `statistics`, or `how many participants`.

One run covers one primary estimand, one decision criterion, and one approved design-analysis specification.

Several related scenarios may vary effect assumptions, sample size, allocation, attrition, or another approved input while preserving that core specification. Separate materially different estimands, tests, models, designs, or confirmatory families into separate runs.

Power is conditional on a complete set of assumptions. It is not a property of sample size alone and does not measure whether a hypothesis is true.

## Calculation modes

Offer only applicable modes:

1. **Prospective required sample size**
   - Solve for the required number of analyzed units under approved inputs.
   - Separately derive enrolled or recruited units when the user approves a data-loss model.

2. **Prospective power or operating-characteristic curve**
   - Evaluate approved candidate sample sizes or resource bounds.
   - Show sensitivity rather than one authoritative point.

3. **Minimum detectable effect or design sensitivity**
   - Solve for the effect detectable under a fixed prospective sample-size and design specification.
   - Label this a property of the assumed design, not evidence about an observed effect.

4. **Simulation-based operating characteristics**
   - Use when an approved data-generating and analysis specification requires simulation or when a validated analytic route is unavailable.
   - Include both alternative and null scenarios, numerical uncertainty, and model-failure behavior.

Do not compute retrospective observed power from the effect estimated in the same completed study.

## Inputs

Gather:

- approved [experimental-design](../experimental-design/SKILL.md) Design Specification or equivalent supplied design;
- exact primary estimand and outcome;
- allocation, experimental, observation, and intended analysis units;
- planned test, model, estimator, contrast, decision rule, and relevant degrees of freedom;
- effect metric, candidate value or range, provenance, and applicability;
- alpha or other Type I error rule, sidedness, multiplicity strategy, and target power or operating characteristic;
- allocation ratio, blocking, clustering, repeated measures, nesting, strata, periods, or sequential features;
- variance, baseline risk, correlation, intracluster dependence, cluster-size distribution, event rate, censoring, or other parameters required by the method;
- anticipated exclusions, attrition, unusable observations, adherence, missingness, or other data loss;
- feasible participant, item, cluster, trial, session, site, time, cost, or resource bounds;
- intended confirmatory, exploratory, mixed, or unclear status;
- outcome visibility and any deviations from a protocol or preregistration;
- supplied evidence and approved evidence boundary;
- desired calculation mode, output, and stop point.

Mark an essential missing input `unknown`. Do not substitute a conventional default or package default.

## Effect-basis options

When the user has not selected an effect basis, present applicable options without imposing a universal hierarchy:

- a smallest effect or target difference that the user considers substantively important, with its rationale;
- directly applicable prior evidence, with construct, population, outcome, metric, design, and analysis match;
- pilot information used primarily for variance, reliability, feasibility, or other design parameters, with instability disclosed;
- a theoretically specified model parameter or data-generating scenario;
- a resource-constrained sensitivity range;
- a conventional standardized effect only as an explicitly weak, field-insensitive assumption.

For every candidate basis, show provenance, translation steps, transportability limits, uncertainty, and consequences across a plausible range.

Do not automatically shrink, take a confidence-bound value, or select the smallest effect. Do not copy a published or pilot estimate without inspecting its applicability and uncertainty.

## Steps

### 1. Build the Power Analysis Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and inquiry part |
| Intended decision | What the calculation should help the user decide |
| Calculation mode | Required sample size, curve, MDE, or simulation |
| Design specification | Approved design, allocation, units, and dependence |
| Estimand and outcome | The user's exact selected target |
| Planned analysis | Test, model, contrast, estimator, and decision rule |
| Effect basis | Metric, values or range, provenance, and applicability |
| Error rules | Alpha or equivalent, sidedness, multiplicity, and target operating characteristic |
| Additional parameters | Variance, rates, correlations, ICC, cluster sizes, events, censoring, or other inputs |
| Data loss | Attrition, exclusions, unusable observations, missingness, and enrollment implications |
| Resource bounds | Feasible limits and their units |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied material that may be inspected |
| Missing inputs | User-owned or technical inputs not yet available |
| Excluded work | Design choice, scientific input choice, search, installation, observed-data analysis, saving, and unapproved handoffs |
| Stop point | Exact output or decision that ends the run |

### 2. Build the Scenario and Method Preview

Generate two or more `AI-generated calculation scenario` entries only when multiple scientifically plausible input combinations fit the approved boundary. If only one scenario is specified, show one. Do not create artificial effect sizes or error rates.

| Field | Required content |
|---|---|
| Scenario ID | Stable label |
| Target | Quantity to solve or evaluate |
| Unit | Per arm, total participants, pairs, clusters, events, items, trials, sessions, or another exact unit |
| Effect input | Metric, value or range, provenance, and translation |
| Error and decision inputs | Alpha or equivalent, sidedness, multiplicity, target power, and criterion |
| Design inputs | Allocation, dependence, repeated structure, cluster sizes, or other design features |
| Data-loss inputs | Analyzed-to-enrolled relationship and assumptions |
| Candidate method | Analytic, numerical inversion, simulation, or specialist route |
| Method basis | Why the route matches the approved design and analysis |
| Assumptions | Distributional, design, measurement, missingness, and implementation assumptions |
| Verification plan | Independent benchmark, second implementation, limiting case, or simulation calibration |
| Scenario status | One status below with a reason |

Use only:

- **Ready for analytic or numerical calculation**
- **Ready for simulation after approval**
- **Blocked by a user-owned input**
- **Blocked by a method or implementation gap**
- **Power is not the appropriate justification as framed**

An analytical formula may be exact under a model, a numerical inversion of a model-based expression, or an approximation. Label it accurately.

### 3. Gate 1: approve the calculation boundary

Ask the user to approve or correct the Power Analysis Brief and Scenario and Method Preview.

Gate 1 authorizes only:

- inspection of the displayed inputs and evidence;
- assessment of scenario readiness and method fit;
- construction of the Assumption and Sensitivity Register.

It does not authorize:

- selecting an estimand, effect basis, error rule, target power, sidedness, design, analysis, sample size, or scientific conclusion;
- network search, package installation, code execution, saving, or another capability.

If any scientific target, design, analysis, effect basis, error rule, data-loss model, or evidence boundary changes materially, rebuild the brief and repeat Gate 1.

### 4. Build the Assumption and Sensitivity Register

Create one row per consequential assumption:

| Field | Required content |
|---|---|
| Assumption ID | Stable identifier |
| Scenario | Affected scenario ID |
| Quantity or rule | Exact parameter, model feature, or decision rule |
| Value or range | Approved candidate values and units |
| Basis | User supplied, source supported, methodological inference, or unverified |
| Applicability | Match to construct, population, design, analysis, and setting |
| Sensitivity consequence | Direction and nature of its effect on the output |
| Failure mode | How violation changes interpretation or validity |
| Resolution options | User decision, bounded evidence, specialist input, or defer |

Handle these explicitly when relevant:

- effect-size uncertainty and translation;
- alpha, sidedness, multiplicity, and target operating characteristics;
- independent units versus observations;
- unequal allocation, variance, cost, or event rates;
- clustering, cluster-size variation, nesting, and repeated measures;
- variance, baseline risk, reliability, correlation, events, and censoring;
- exclusions, attrition, missingness, adherence, and unusable measurements;
- analysis-model and data-generating-model mismatch;
- nonconvergence, separation, singular fits, or numerical failures;
- prospective versus outcome-informed inputs.

Simple inflation factors and cluster design effects are valid only under their assumptions. Do not apply them universally.

### 5. Present response options

For each blocked or consequential item, offer only applicable options:

- retain the supplied value or range;
- return the input to the user for selection;
- widen or revise a sensitivity range;
- prepare a bounded evidence or specialist handoff;
- remove the scenario;
- defer the calculation.

Do not recommend a sample size before computation and validation.

### 6. Gate 2: The user selects scenarios and inputs

Ask the user to:

- select the scenarios to calculate;
- confirm every scientific and decision input;
- select the calculation route when more than one valid route remains;
- approve the sensitivity grid and numerical precision;
- select any handoff packet.

Gate 2 authorizes calculation only for the selected scenarios through the displayed execution and verification route.

It does not authorize a package installation, design change, actual-data analysis, search, save, final sample-size decision, or another capability.

Do not infer selection from silence.

### 7. Preflight the numerical implementation

Before calculation:

1. identify the exact formula, calculator, package, version, or simulation implementation;
2. verify the method and parameterization against current authoritative documentation or a primary methodological source;
3. confirm the meaning of every sample-size output and round only in the conservative direction appropriate to the approved design;
4. define an independent verification route;
5. stop if implementation behavior, units, parameterization, or version is not verifiable.

No numerical engine is a standing dependency. Use a project-owned or already available implementation only after Gate 2. Do not install or activate software without separate approval.

The K-Dense source scripts are provenance-only and must not be executed or copied.

### 8. Calculate and verify selected scenarios

For analytic or numerical routes:

- calculate only approved scenarios;
- retain full precision internally and show justified rounding;
- report per-group, total, cluster, event, pair, item, trial, or session units explicitly;
- verify with an independent formula, implementation, published benchmark, or limiting case where feasible;
- label limited verification rather than overstating certainty.

For simulations:

- encode the approved data-generating and analysis models;
- use a reproducible random-number strategy;
- choose repetitions from the approved Monte Carlo precision target rather than a universal count;
- evaluate the selected alternative scenarios and corresponding null rejection behavior;
- report Monte Carlo intervals;
- report convergence, separation, singular-fit, and other failure rates and how failures were handled;
- verify that sample-size search did not rely on noisy monotonicity without rechecking candidate boundaries.

Do not call every failed fit nonsignificant or automatically describe that handling as conservative.

### 9. Produce the Power Planning Record

Return:

| Field | Required content |
|---|---|
| Approved scope | Study, estimand, design, analysis, mode, and evidence boundary |
| Selected scenarios | Only Gate 2 selections |
| Inputs | Every value, range, unit, source, translation, and decision owner |
| Method | Formula, inversion, simulation, or specialist route and why it fits |
| Results | Required analyzed and enrolled units, power, MDE, or curve as applicable |
| Sensitivity | Results across the approved uncertainty grid |
| Numerical uncertainty | Monte Carlo interval, rounding, or approximation limits |
| Verification | Independent check and outcome |
| Software state | Tool, version, source, and execution environment, or `not applicable` |
| Failure behavior | Fit or numerical failures and their treatment |
| Limitations | Model, evidence, transportability, implementation, and feasibility limits |
| The user's remaining decision | Final sample size or other scientific choice not made by this skill |
| Handoff packets | Only packets selected for preparation |
| Provenance | User inputs, source evidence, AI-generated scenarios, calculations, and decisions kept separate |

Use these result labels:

- **Computed and independently verified**
- **Computed with limited verification**
- **Calculation blocked by unresolved input**
- **Calculation blocked by implementation gap**
- **Calculation not appropriate under the approved framing**

Verify that no scientific input or final decision was silently selected and no result is reported beyond its assumptions.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the applicable verified reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **Power Analysis Brief**
- **Scenario and Method Preview**
- **Assumption and Sensitivity Register**, after Gate 1
- **Response Options**
- **Selected Scenario Results**, only after Gate 2 and preflight
- **Power Planning Record**
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return power-analysis results in the current task's requested form or under the recipient's existing reporting policy.

Gate 1 and Gate 2 do not authorize network search, package installation, source modification, saving, or starting another capability. Numerical execution after Gate 2 is limited to the approved preflighted route.

Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized saved output, use the destination the user names. Otherwise follow the recipient's configured placement policy, including an established operational project destination when that policy selects it. Apply the configured Area-folder boundary and keep skill and system implementation files in `00 ASTORIA/`. Verify current paths from `me.md` and the layout reference. Link from the existing owning MOC when the selected workflow calls for it and the link edit is authorized. Ask only when required ownership or destination remains unresolved.

## Boundaries

- **No approved design or analysis**: Route to [experimental-design](../experimental-design/SKILL.md) or the appropriate method owner and stop.
- **Missing effect basis or error rule**: Present options and consequences, then return the decision to the user.
- **Only a resource ceiling is known**: Offer prospective power or MDE sensitivity across approved scenarios.
- **Observed nonsignificant result**: Refuse observed post hoc power. Offer confidence-interval interpretation through Part 4 or prospective design sensitivity at the achieved design.
- **Pilot effect supplied**: Expose instability, outcome visibility, and applicability. Do not plug it in automatically.
- **Published effect supplied**: Verify construct, population, outcome, metric, design, analysis, and uncertainty before use.
- **Conventional effect requested**: Label it field-insensitive and weakly grounded.
- **Several primary tests**: Require the confirmatory family and multiplicity rule, or split the runs.
- **One-sided test**: Require the user's scientific and decision rationale before calculation.
- **Unequal allocation**: Preserve variance, event-rate, cost, feasibility, and ethical implications rather than assuming equal allocation is optimal.
- **Clustered or repeated observations**: Preserve the independent unit and full dependence structure. Do not count observations as independent participants.
- **Attrition or unusable data**: Separate required analyzed units from enrolled or collected units and state the data-loss model.
- **Noninferiority, equivalence, sequential, adaptive, survival, rare-event, or Bayesian design**: Require the exact specialist specification and a validated method. Do not force a generic formula.
- **Simulation failures**: Report rate, reason, handling, and sensitivity. Do not hide failures inside the power estimate.
- **No independent numerical check**: Label limited verification or stop when the risk is material.
- **Implementation unavailable**: Return a complete blocked record. Do not install a package or substitute an unverified calculator.
- **Cognitive or behavioral paradigm**: Prepare a handoff to [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) for domain-specific inputs.
- **MRI neuroimaging design**: Route modality-specific assumptions to [neuroimaging-power-guide](../../specialized_skills/neuroimaging-power-guide/SKILL.md).
- **EEG or MEG design**: Route to the appropriate future modality owner and disclose the current gap.
- **Outcome-informed change**: Do not present it as a prospective confirmatory calculation for already inspected outcomes.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [experimental-design](../experimental-design/SKILL.md) when the design, units, allocation, factors, repeated structure, clustering, or sequential rules are not approved.
- Use [cognitive-paradigm-design](../../specialized_skills/cognitive-paradigm-design/SKILL.md) when a cognitive or behavioral construct still lacks an approved paradigm architecture, manipulation, comparator, outcome, or estimand.
- Use [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) for participants-by-items-by-trials structure, reliability, data loss, and cognitive or behavioral effect-evidence applicability.
- Use [neuroimaging-power-guide](../../specialized_skills/neuroimaging-power-guide/SKILL.md) for MRI-specific spatial inference, correction, ROI or search-space definition, effect maps, model levels, reliability, pipeline, and detection-event inputs.
- Use [neuroimaging-sample-size-calculator](../../specialized_skills/neuroimaging-sample-size-calculator/SKILL.md) when an approved calculation needs an MRI-specific spatial or pipeline implementation.
- Use [prediction-stress-test](../prediction-stress-test/SKILL.md) for prediction-centered testability and contrary-result implications.
- Use [research-literacy](../research-literacy/SKILL.md) when one proposed effect basis requires a bounded evidence audit.
- Use [paper-search](../paper-search/SKILL.md) only after separate approval for a bounded effect, variance, reliability, ICC, attrition, or other parameter search.
- Route analysis of observed data, model fitting, diagnostics, and inference to a separately approved Part 4 capability.

Each destination begins its own workflow and gates. Statistical Power approval does not authorize another capability.

This skill does not design the study, specify cognitive or neuroimaging inputs, choose scientific assumptions, calculate observed post hoc power, analyze observed outcomes, install software, search, alter a protocol, or make a scientific conclusion for the user. Save a verified result only within the separately authorized content and destination. The scientific gates grant no write authority.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Arnold, B. F., Hogan, D. R., Colford, J. M., Jr., & Hubbard, A. E. (2011). Simulation methods to estimate design power: An overview for applied research. *BMC Medical Research Methodology, 11*, Article 94. https://doi.org/10.1186/1471-2288-11-94
- CONSORT 2025 explanation and elaboration. (2025). *BMJ, 389*, Article e081124. https://www.bmj.com/content/389/bmj-2024-081124
- Hoenig, J. M., & Heisey, D. M. (2001). The abuse of power. *The American Statistician, 55*(1). https://doi.org/10.1198/000313001300339897
- Lakens, D. (2022). Sample size justification. *Collabra: Psychology, 8*(1). https://doi.org/10.1525/collabra.33267
