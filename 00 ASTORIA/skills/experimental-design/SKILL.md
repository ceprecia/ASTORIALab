---
name: experimental-design
description: >-
  Compares prospective experimental-design structures for one bounded
  user-supplied research question, hypothesis, or prediction and constraint set.
  Use when the request, or a part coordinator, hands over explicitly prospective
  design construction. It maps experimental and observation units, generates
  labeled design options, exposes assumptions and feasibility threats, and
  produces only the user's selected Design Specification after two approval gates.
  It does not generate hypotheses, choose the design, calculate power or sample
  size, create an allocation schedule, execute an analysis, search, save, or
  start another capability without separate approval. Triggers: compare
  experimental designs for this question, which design fits my hypothesis.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: any
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-11-02"
---

# Experimental Design

Compare prospective study structures without taking ownership of the scientific decision.

## Purpose

`experimental-design` is the Part 3 canonical owner for prospective, general experimental-design construction and comparison for one bounded user-supplied research question, hypothesis, or prediction and constraint set.

It owns:

- identifying experimental, intervention, observation, and intended analysis units;
- mapping independent replication, nesting, clustering, repeated measurement, and nuisance structure;
- comparing applicable design families and control structures;
- exposing confounding, pseudoreplication, contamination, carryover, period, order, batch, and feasibility threats;
- specifying randomization, restriction, counterbalancing, allocation concealment, and role-specific masking requirements at the design level;
- showing analysis and power implications that a later capability must honor;
- producing a selection-bound Design Specification.

The user owns the research question, hypothesis, prediction, primary outcome, estimand, confirmatory status, design selection, factors, levels, controls, thresholds, power target, analysis model, interpretation, and scientific claims.

This skill constructs prospective design options. [research-critique](../research-critique/SKILL.md) audits the coherence and threats of an already supplied whole research object or design. [prediction-stress-test](../prediction-stress-test/SKILL.md) challenges prediction-centered testability, falsifiability, counterexamples, contrary-result implications, and bounded novelty.

Use this skill when the user names it or the bounded request matches its
frontmatter description and trigger meaning. A verified coordinator or
capability handoff may invoke the same matching task.

[research-coordinator](../research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching prospective design task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `critique this research design`;
- `stress-test this prediction`;
- `calculate power`;
- `choose the best design`;
- `randomize these participants`;
- `analyze this study`;
- broad words such as `design`, `experiment`, `method`, or `research`.

One run covers one bounded study or one inseparable design family for a single stated scientific objective.

If the request contains independent studies, separate them and ask the user which one is in scope. A multistage or multi-experiment program may remain one run only when the user confirms that the components form one inseparable design decision.

Design work is prospective. If relevant outcomes were already inspected, record that visibility. A modified design may govern new data prospectively, but this skill must not retroactively call an outcome-informed change confirmatory.

## Inputs

Gather only what is needed to compare structures:

- exact user-supplied research question, hypothesis, or prediction;
- intended use, inquiry part, and decision in scope;
- primary outcome and estimand when the user has selected them, or `unknown`;
- candidate intervention, exposure, manipulation, comparison, factors, and levels as supplied;
- target population, sampling frame, setting, and recruitment constraints;
- intervention unit, experimental unit for each factor, observation unit, intended analysis unit, and inference level when known;
- timing, repeated observations, periods, washout, order, and follow-up;
- anticipated nesting, clustering, batch, site, family, classroom, scanner, run, stimulus, or other dependency;
- ethical, burden, cost, equipment, staffing, calendar, and access constraints;
- allocation, concealment, masking, contamination, and operational constraints;
- outcome visibility and intended confirmatory, exploratory, mixed, or unclear status;
- relevant protocol, preregistration, fixed decisions, supplied evidence, and permitted evidence boundary;
- desired stop point and excluded work.
- requested visual form and detail, if relevant to the task.

Mark an essential missing item `unknown`. Do not invent it or select it for the user.

## Candidate design families

Offer only families that fit the approved brief:

1. **Between-unit comparative designs**
   - Completely randomized or otherwise prospectively allocated comparisons.
   - Nonrandomized alternatives must be labeled with their stronger confounding limits.

2. **Blocked or stratified designs**
   - Use when a small, defensible set of prognostic or operational factors can improve comparability or precision.
   - Expose sparse-stratum, predictability, and implementation risks.

3. **Within-unit, repeated-measures, or crossover designs**
   - Consider correlation, period effects, carryover, learning, fatigue, reversibility, washout, missingness, and attrition.
   - Do not claim an automatic power advantage.

4. **Cluster-assigned designs**
   - Consider contamination, cluster-level delivery, unequal cluster sizes, intracluster dependence, number of independent clusters, and inference level.
   - Do not substitute the number of observations for the number of independently assigned units.

5. **Factorial, fractional-factorial, or split-plot designs**
   - Map factor-specific experimental units, hard-to-change factors, error strata, aliasing, interactions, replication, and estimability.
   - Do not assume higher-order interactions are absent without disclosure.

6. **Counterbalanced or Latin-square structures**
   - Consider order, period, carryover, balance conditions, missing cells, and whether the assumed structure is scientifically credible.

7. **Response-surface or space-filling designs**
   - Consider the intended functional approximation, region of interest, curvature, model dependence, and whether physical constraints make candidate points infeasible.

8. **Sequential or adaptive designs**
   - Treat as a specialist route when decisions depend on accumulating data.
   - Require prospective rules, operating-characteristic evaluation, estimation checks, information-access controls, and context-specific oversight.
   - Do not choose a stopping boundary or implement an adaptive trial here.

Do not propose a design merely because software can generate it.

## Steps

### 1. Build the Experimental Design Brief

Preserve the user's scientific statements and show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and inquiry part |
| Scientific objective | The user's question, hypothesis, or prediction |
| Intended decision | What the comparison should help the user decide |
| Primary outcome and estimand | The user's selections, or `unknown` |
| Candidate factors and comparisons | Supplied interventions, exposures, conditions, factors, and levels |
| Unit structure | Intervention, experimental, observation, analysis, and inference units as supplied |
| Dependency structure | Repeated measures, clusters, nesting, batches, sites, stimuli, or other dependence |
| Timing | Periods, order, washout, follow-up, and outcome timing |
| Constraints | Ethics, burden, recruitment, cost, access, equipment, staffing, and calendar |
| Bias controls | Allocation, restriction, concealment, masking, contamination, and implementation constraints |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied material that may be inspected |
| Fixed decisions | User-owned choices that must not be changed |
| Missing material | Essential unknowns and access limits |
| Excluded work | Hypothesis generation, design selection, power calculation, schedules, analysis, search, saving, and unapproved handoffs |
| Stop point | The output or decision that ends the run |

### 2. Gate 1: approve the design question and comparison boundary

Ask the user to approve or correct the Experimental Design Brief and the candidate design families to compare.

Gate 1 authorizes only:

- inspection of the displayed inputs and evidence boundary;
- comparison of the displayed design families;
- production of the Unit and Dependency Map, Design Option Matrix, and Threat and Feasibility Register.

It does not authorize:

- generating or rewriting a hypothesis or prediction;
- selecting the primary outcome, estimand, design, factor, control, measure, or threshold;
- calculating power, sensitivity, or sample size;
- generating or revealing an allocation sequence;
- selecting an analysis model;
- searching, saving, preregistering, collecting data, executing code, or starting another capability.

If the scientific objective, estimand, unit structure, candidate family, fixed constraint, outcome visibility, confirmatory status, or evidence boundary changes materially, rebuild the brief and repeat Gate 1.

### 3. Build the Unit and Dependency Map

Show, for each factor or intervention:

| Field | Required content |
|---|---|
| Assignment or exposure | What varies and how |
| Intervention unit | Unit that receives or experiences the intervention |
| Experimental unit | Smallest independently assigned or independently varying unit |
| Observation unit | Unit on which measurements are recorded |
| Intended analysis unit | The user's supplied unit, proposed candidate, or `unknown` |
| Inference level | Population or unit to which the intended conclusion refers |
| Replication | Independent replication available at each relevant level |
| Dependence | Nesting, clustering, repeated measures, shared environments, batches, stimuli, or sites |
| Nuisance structure | Prognostic or operational factors that may require control |
| Unresolved risk | Pseudoreplication, perfect confounding, contamination, imbalance, or unclear hierarchy |

Do not treat repeated observations on the same experimental unit as independent replication. Analysis can model an existing hierarchy, but it cannot manufacture absent independent replication or disentangle perfect confounding.

Draw the supplied or candidate hierarchy beside this map: show assignment for each factor, nesting or crossing, and repeated observations. Add a condition grid or sequence view when it explains another part of the same structure. Follow the figures rules under Outputs and keep unknown unit counts and timings unresolved.

### 4. Generate and compare design options

Generate two to four clearly labeled `AI-generated design option` entries when at least two scientifically credible structures fit the approved boundary.

If only one route is credible, state why and do not invent alternatives. If none can be assessed, stop with the exact missing inputs.

Use this matrix:

| Field | Required content |
|---|---|
| Option ID and family | Stable label and design family |
| Structure | Units, factors, conditions, periods, clusters, blocks, or sequences |
| Scientific fit | Which supplied objective and estimand it can address |
| Independent replication | Where replication occurs and where it does not |
| Allocation and control | Randomization or nonrandomized assignment, restrictions, counterbalancing, comparators, and concealment needs |
| Assumptions | Scientific, operational, measurement, and statistical assumptions |
| Bias and validity implications | Confounding, contamination, selection, carryover, period, order, batch, attrition, and missingness |
| Feasibility implications | Recruitment, burden, time, equipment, staffing, ethics, and logistics |
| Analysis implications | Design features a later analysis must represent |
| Power inputs | Quantities a later power capability would require, without calculating them |
| Failure modes | Conditions under which the design becomes uninformative or infeasible |
| Evidence basis | User supplied, source supported, methodological inference, or unverified |
| Option status | One status below with a reason |

Use only these statuses:

- **Viable within supplied constraints**
- **Viable with material unresolved assumptions**
- **Not viable within supplied constraints**
- **Not assessable from supplied material**

Do not average statuses, create a composite score, or rank a design as scientifically best. A status is a bounded assessment, not a decision.

Randomization balances measured and unmeasured covariates only in expectation. It can support causal inference when assignment, conduct, measurement, analysis, interference, adherence, missingness, and other design assumptions are handled appropriately. It does not turn every comparison into a causal claim.

Describe masking by role, such as participants, interventionists, outcome assessors, data processors, analysts, or adjudicators. Do not rely on ambiguous `single-blind` or `double-blind` labels.

### 5. Build the Threat and Feasibility Register

Create one row per consequential issue:

| Field | Required content |
|---|---|
| Threat ID | Stable identifier |
| Affected option | One or more option IDs |
| Threat | Exact inferential, ethical, or operational risk |
| Mechanism | How the threat could affect the study |
| Basis | User supplied, source supported, methodological inference, or unverified |
| Detectability | What could reveal the problem |
| Prevention or mitigation candidates | Clearly labeled options, not automatic requirements |
| Residual risk | What remains even if a mitigation is selected |
| Decision owner | The user, ethics or regulatory body, statistician, domain expert, or other named owner |
| Evidence or expertise needed | Exact unresolved question |

Pay particular attention to:

- absent independent replication and pseudoreplication;
- perfect confounding between condition and batch, site, period, order, or operator;
- contamination, spillover, or interference;
- unequal cluster sizes or too few independent clusters;
- carryover, irreversibility, inadequate washout, learning, and fatigue;
- attrition and missingness that differ by condition or period;
- hard-to-change factors and restricted randomization;
- allocation predictability or inadequate concealment;
- role-specific masking failures;
- unreplicated factorial structures, aliasing, and unestimable effects;
- outcome-informed changes presented as confirmatory;
- burdens or risks that require ethics, regulatory, clinical, or specialist review.

### 6. Present response options

For each consequential option or threat, offer only applicable responses:

- retain the option for Gate 2 consideration;
- remove it from consideration;
- return a missing scientific decision to the user;
- gather bounded evidence or specialist input;
- prepare a handoff packet;
- defer the design decision.

Preserve tradeoffs and residual risks. Do not transform a response option into an implied recommendation when the evidence does not support one.

### 7. Gate 2: The user selects the design route

Ask the user to:

- select one design option, combine explicitly compatible elements, or defer;
- confirm the primary outcome, estimand, factors, controls, and unit structure that the user owns;
- select any threat mitigations;
- identify unresolved items that must remain open;
- select any handoff packet to prepare.

Gate 2 authorizes only the selected elements for the Design Specification and the preparation of selected handoff packets.

It does not authorize code, a randomization schedule, power or sample-size calculation, analysis, preregistration, data collection, saving, search, or starting another capability.

Do not infer selection from silence. If the user combines options, verify that the combined structure remains internally coherent before documenting it.

### 8. Produce and verify the Design Specification

Produce:

| Field | Required content |
|---|---|
| Approved scope | Study, objective, decision, and evidence boundary |
| Selected design | The user's chosen family and structure |
| Scientific elements | user-selected outcome, estimand, factors, levels, conditions, controls, and timing |
| Unit and dependency structure | Intervention, experimental, observation, analysis, and inference units plus nesting or clustering |
| Replication | Independent replication at every relevant level |
| Allocation specification | Method class, restrictions, counterbalancing, concealment, and authorized roles, but no generated schedule |
| Masking specification | Exactly who should remain unaware of what, when, and how |
| Threat controls | user-selected prevention or mitigation elements and residual risks |
| Analysis requirements | Design features a later analysis must represent, without selecting the analysis |
| Power inputs | Required quantities and uncertainty ranges for a later power workflow |
| Confirmatory status | The user's stated status, outcome visibility, and any deviations |
| Open items | Unresolved scientific, feasibility, evidence, ethics, regulatory, or specialist questions |
| Handoff packets | Only packets the user selected for preparation |
| Provenance | User statements, AI-generated options, supplied evidence, inferences, and decisions kept separate |

Verify that:

- the specification matches Gate 1 and Gate 2;
- every AI-generated design option remains labeled;
- The user selected every consequential scientific element in the specification;
- experimental, observation, and analysis units are not silently conflated;
- repeated observations are not counted as independent replication;
- every factor has a defensible experimental unit and estimable comparison;
- no condition is perfectly confounded with a nuisance factor without explicit disclosure;
- randomization restrictions, concealment, and role-specific masking are distinguished;
- crossover, cluster, factorial, split-plot, sequential, and adaptive features carry their relevant assumptions;
- analysis and power implications match the selected structure;
- outcome-informed changes are not mislabeled as confirmatory;
- no schedule, code, power value, analysis, search, save, data collection, or unapproved handoff occurred.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the applicable verified reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **Experimental Design Brief**
- **Unit and Dependency Map**, after Gate 1
- **Design Option Matrix**
- **Threat and Feasibility Register**
- **Response Options**
- **Design Specification**, only after Gate 2
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return the design results in the current task's requested form or under the recipient's existing reporting policy.

Gate 1 and Gate 2 do not authorize saving, modifying a source, searching, installing packages, creating an allocation schedule, preregistering, collecting data, starting another capability, or initiating an external action.

Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized saved output, use the destination the user names. Otherwise follow the recipient's configured placement policy, including an established operational project destination when that policy selects it. Apply the configured Area-folder boundary and keep skill and system implementation files in `00 ASTORIA/`. Verify current paths from `me.md` and the layout reference. Link from the existing owning MOC when the selected workflow calls for it and the link edit is authorized. Ask only when required ownership or destination remains unresolved.

## Figures and examples

- Use the task's selected visual form and detail, then the applicable verified reporting policy. With neither specified, add only the views that clarify the current decision. Hierarchy diagrams, factor-by-condition grids, period or crossover sequences, and structural examples can clarify distinct design issues.
- Before Gate 1, show only the supplied brief. After Gate 1, illustrate the compared options. After Gate 2, show selected elements in the specification. Present explanatory diagrams in the current task's requested form or under the recipient's existing reporting policy. Apply the same decision boundaries as the tables. Allocation schedules and executable code are outside this capability. Save a figure only when its file output and destination are authorized.
- Use consistent option IDs, conditions, factors, and unit names. Explain arrows as assignment, nesting, crossing, or repeated measurement rather than leaving their meaning implicit. Distinguish independent units from observations within them; do not draw a crossed structure as nested.
- Start with the overall structure, then add the factor-specific assignment or repeated-measure detail. Reuse the same example across views. Label candidate structures and assumptions; illustrative objects do not set participant counts, factor levels, allocation ratios, washout, or other missing scientific parameters.
- Use a representation supported by the selected form. Markdown tables, Mermaid diagrams and LaTeX are available when supported and useful. Show formulas only for supplied or specified relationships, with symbols and assumptions defined. Keep display math outside table cells. For an order-only view, state that spacing does not indicate duration. Use only supplied or approved timings for a scaled timeline.
- Preserve the strongest supported inference and its local assumptions. Arrows showing assignment or exposure do not by themselves prove causation, independent replication, or identification of a mechanism.
- Check each figure against the Unit and Dependency Map, option matrix, and selected specification for unit levels, dependencies, conditions, order, provenance, and unknowns. Inspect readable rendering where possible; supply a useful text/table alternative when it cannot be checked. Do not create new alternatives, estimates, schedules, or scientific selections just to complete a picture.

## Boundaries

- **No user-owned scientific objective**: Stop and ask the user to supply the question, hypothesis, or prediction.
- **Primary outcome or estimand missing**: Compare only what can be compared, mark compatibility unresolved, and return the decision to the user.
- **Only one credible design family**: Explain the constraint and do not invent alternatives.
- **No assessable design family**: Return the exact missing inputs or specialist evidence needed.
- **Existing design submitted for critique**: Route to [research-critique](../research-critique/SKILL.md) and stop this workflow.
- **Prediction stress test requested**: Route to [prediction-stress-test](../prediction-stress-test/SKILL.md) and stop this workflow.
- **Power or sample size requested**: Prepare a bounded handoff to the appropriate Active power capability, or disclose the gap.
- **Allocation list requested**: This skill may specify the intended method but must not generate or reveal the schedule.
- **Outcomes partly or fully seen**: Preserve the visibility and do not retroactively label modifications confirmatory.
- **Nonrandomized design**: State the confounding and causal limits directly. Do not imply randomization occurred.
- **Very few independent units**: Do not use repeated observations to hide the limitation.
- **Perfect condition-by-batch or site confounding**: Mark the intended effect not separately estimable from that nuisance structure.
- **Crossover with irreversible or persistent intervention effects**: Mark the route not viable unless a defensible structure resolves the problem.
- **Cluster design**: Distinguish participant count from independent cluster count and preserve unequal-size and contamination risks.
- **Factorial design without replication**: Disclose the lack of pure-error information and any assumptions used to interpret interactions.
- **Adaptive or sequential request**: Limit work to comparison and a specialist handoff. Do not choose rules or operate the study.
- **Human, clinical, regulated, or animal study**: Flag applicable ethics, regulatory, clinical, and reporting expertise. This skill does not replace them.
- **Package appears convenient**: Ignore package availability when selecting candidate designs.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [prediction-stress-test](../prediction-stress-test/SKILL.md) for prospective prediction-centered pressure testing.
- Use [research-critique](../research-critique/SKILL.md) for whole-object or retrospective design critique, including the trigger `critique this research design`.
- Use [research-literacy](../research-literacy/SKILL.md) to audit evidence for one explicit claim.
- Use [paper-search](../paper-search/SKILL.md) only after separate approval for a bounded design-method evidence need.
- If an invoking companion routed this capability and the project, stage, or
  destination remains unclear, return that unresolved boundary to the invoking
  companion. If no companion invoked it, stop at this capability boundary and
  offer [research-companion](../research-companion/SKILL.md) only as an optional public routing entry.
- Use [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) for cognitive and behavioral participant, item, trial, session, reliability, data-loss, and effect-evidence input specification.
- Use [statistical-power](../statistical-power/SKILL.md) for general quantitative power, sample-size, MDE, or operating-characteristic calculations after the Design Specification is approved.
- Use [cognitive-paradigm-design](../../specialized_skills/cognitive-paradigm-design/SKILL.md) for construct-to-task operationalization and comparison of general cognitive or behavioral paradigm architectures.
- Use [bids](../../specialized_skills/bids/SKILL.md) for version-pinned BIDS curation and compliance specification
  after the relevant design and scientific labels are approved.
- Use [method-design](../method-design/SKILL.md) for prospective computational-method architecture
  comparison after the study and evaluation boundary are approved.
- Use [alternative-uses-task-designer](../../specialized_skills/alternative-uses-task-designer/SKILL.md) for prospective AUT-specific administration parameters after the task and general design are approved.
- Use [visual-search-array-generator](../../specialized_skills/visual-search-array-generator/SKILL.md) for approved controlled-array visual-search layout generation and validation.
- Use [fmri-task-design-guide](../../specialized_skills/fmri-task-design-guide/SKILL.md) for task-fMRI timing comparison and schedule validation after the neural estimand and model are approved.
- Use [neuroimaging-power-guide](../../specialized_skills/neuroimaging-power-guide/SKILL.md) for prospective MRI neuroimaging power-method and input specification after the design and analysis target are approved.
- Use [neuroimaging-sample-size-calculator](../../specialized_skills/neuroimaging-sample-size-calculator/SKILL.md) only after an approved MRI-specific Power Inputs Specification requires numerical execution.
- Route analysis selection and execution to a separately approved Part 4 method guide or adapter.

This skill does not generate or rewrite hypotheses or predictions, audit an existing whole research object, select the design, calculate power, create or reveal allocation schedules, select an analysis, search, preregister, collect data, execute code, provide ethics or regulatory approval, or make scientific conclusions for the user. Save a verified result only within the separately authorized content and destination. The scientific gates grant no write authority.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Hurlbert, S. H. (1984). Pseudoreplication and the design of ecological field experiments. *Ecological Monographs, 54*(2). https://doi.org/10.2307/1942661
- NIST/SEMATECH. (n.d.). *Choosing an experimental design*. https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm
- Percie du Sert, N., et al. (2020). The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biology, 18*(7). https://doi.org/10.1371/journal.pbio.3000410
- *SPIRIT 2025 and CONSORT 2025 statements*. (2025). https://www.consort-spirit.org/published-statements
- U.S. Food and Drug Administration. (2019). *Adaptive designs for clinical trials of drugs and biologics: Guidance for industry*. https://www.fda.gov/media/78495/download
