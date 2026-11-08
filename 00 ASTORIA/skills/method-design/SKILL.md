---
name: method-design
description: >-
  Compares and specifies prospective computational method architectures for one
  user-supplied scientific objective and approved evaluation boundary. Use when
  the request, or a part coordinator, hands over an explicitly matching
  computational-method question. It maps inputs, outputs, representations,
  modules, objectives, constraints, assumptions, failure modes, validation,
  ablations, and reproducibility; generates only credible labeled options; and
  produces a user-selected Computational Method Specification after two approval
  gates. It does not generate the research objective, rank designs through an
  LLM tournament, choose a method, claim a proof, search, implement or train
  models, run observed-data experiments, install software, write publication
  text, or save without separate approval. Triggers: design a computational
  method for this objective, compare method architectures.
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
  updated: "2026-11-01"
---

# Method Design

Design a prospective computational method around the scientific objective and evaluation boundary, not around a fashionable architecture or installed package.

## Purpose

`method-design` is the Part 3 canonical owner for prospective comparison and specification of one computational model, algorithm, or processing-method architecture after the user supplies the scientific objective.

It owns:

- mapping approved scientific inputs, outputs, estimands, constraints, and
  evaluation criteria into computational requirements;
- comparing two to four credible architecture or algorithm families when the
  evidence supports alternatives;
- specifying representations, modules, information flow, objective terms,
  regularization, constraints, interfaces, failure handling, ablations, and
  reproducibility requirements;
- separating mathematical definitions, assumptions, derivations, empirical
  propositions, and unverified conjectures;
- producing only the user-selected Computational Method Specification and
  bounded implementation or evidence handoffs.

The user owns the research question, hypothesis, prediction, scientific objective, inputs and outcomes, permissible information, target population or domain, confirmatory status, evaluation estimand, comparison baseline, data-splitting unit, architecture selection, loss and constraint choices, acceptable tradeoffs, interpretation, and scientific claims.

[experimental-design](../experimental-design/SKILL.md) owns study-level units, conditions, assignment, sampling, and general design structure. [research-critique](../research-critique/SKILL.md) owns critique of an existing complete method or study. Part 4 method and software capabilities own implementation, training, tuning, analysis, and observed-data evaluation. [experiment-controller](../../specialized_skills/experiment-controller/SKILL.md) owns one checkpointed technical smoke test for an already approved computational method without selecting or implementing it.

This skill specifies a method. It does not build or run one.

Use this skill when the user names it or the bounded request matches its
frontmatter description and trigger meaning. A verified coordinator or
capability handoff may invoke the same matching task.

[research-coordinator](../research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching request from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `design my study`;
- `choose the best model`;
- `train this network`;
- `compare these results`;
- `derive a proof`;
- `write the Methods section`;
- broad phrases such as `architecture`, `algorithm`, `model`, `method`,
  `equations`, or `deep learning`.

One run covers:

- one user-supplied scientific objective;
- one approved input and output boundary;
- one evaluation estimand and leakage boundary;
- one bounded computational method family or comparison set;
- one selection-bound specification.

Several outputs may remain together only when they share the same scientific objective, permissible information, data-splitting unit, evaluation boundary, and architecture decision. Otherwise split them.

Do not absorb study design, acquisition, preprocessing selection, power, observed-data analysis, software implementation, training orchestration, or manuscript writing.

## Inputs

Obtain or mark missing:

- exact user-supplied scientific objective;
- approved hypothesis or prediction when relevant;
- intended use: prediction, estimation, classification, segmentation,
  generation, representation, simulation, control, or another exact purpose;
- input objects, units, modalities, dimensions, time or spatial structure, and
  permissible metadata;
- target, output, estimand, decision rule, or required artifact;
- study unit, grouping, repeated measures, sites, families, time points, and
  leakage boundary;
- prospective, preregistered, exploratory, benchmark, or post hoc status;
- candidate method family or open comparison boundary;
- required baselines and null or simpler comparators;
- evaluation metrics, uncertainty, calibration, robustness, subgroup, and
  external-validation requirements;
- constraints on interpretability, latency, memory, compute, energy, data,
  licensing, deployment, privacy, and reproducibility;
- supplied evidence and approved evidence boundary;
- fixed decisions and open decisions;
- intended downstream implementation owner;
- stop point.
- visual detail: full by default, with complementary architecture, information-flow, mathematical, and evaluation views where useful; honor fewer/no figures or a shorter explanation.

If the scientific objective, target, permitted information, evaluation unit, or leakage boundary is unresolved, return it to the user.

## Steps

### 1. Build the Computational Method Brief

Show:

| Field | Required content |
|---|---|
| Scientific objective | Verbatim user-supplied purpose |
| Input and unit | Objects, dimensions, groups, time, sites, and permissible information |
| Output and estimand | Exact prediction, estimate, representation, or artifact |
| Evaluation boundary | Split unit, held-out context, metrics, baselines, and uncertainty |
| Candidate scope | Families included and excluded |
| Constraints | Data, compute, latency, interpretability, privacy, licensing, and reproducibility |
| Evidence | Supplied sources, applicability, and gaps |
| Fixed decisions | user-owned selections already made |
| Open decisions | Architecture, objective, interfaces, and verification choices |
| Excluded work | Search, study redesign, implementation, training, tuning, analysis, writing, and saving |
| Stop point | Selection-bound Computational Method Specification |

Classify the request:

- **Ready for architecture comparison**
- **Ready for fixed-route specification**
- **Needs study-design clarification**
- **Needs evaluation-boundary clarification**
- **Needs bounded evidence**
- **Needs Part 4 owner**

### 2. Gate 1: approve the design boundary

Before drafting options, ask the user to approve:

- scientific objective and intended use;
- inputs, outputs, units, permissible information, and leakage boundary;
- evaluation estimand, metrics, baselines, and uncertainty;
- candidate families and exclusions;
- supplied evidence and any separately approved evidence handoff;
- constraints and fixed decisions;
- option-comparison and mathematical-verification plan;
- stop point.

Gate 1 authorizes only the displayed prospective comparison and specification.

It does not authorize:

- generating or revising the scientific objective;
- search;
- method selection;
- model implementation, training, tuning, or observed-data evaluation;
- installing software;
- saving files;
- another capability.

Do not infer approval from silence.

### 3. Build the Requirement and Information-Flow Map

Map:

| Element | Required content |
|---|---|
| Source object | Exact input, unit, shape, modality, and provenance |
| Permissible information | Features available at intended use time |
| Forbidden information | Outcome, future, site, subject, duplicate, or other leakage |
| Representation | Raw, engineered, learned, graph, sequence, image, tabular, or hybrid |
| Transformation | Proposed module and its scientific role |
| Output | Exact shape, scale, constraints, and interpretation |
| Target or supervision | Source, timing, uncertainty, and missingness |
| Evaluation unit | Participant, item, session, site, time, image, or other unit |
| Interface | Inputs and outputs between modules |
| Failure route | Missing, invalid, out-of-domain, or abstention behavior |

Trace every path from input to output. Flag shortcuts, outcome leakage, duplicate leakage, preprocessing leakage, site confounding, temporal leakage, and hidden use of unavailable information.

Show a readable input-to-output diagram, then separate module or split views when they expose different dependencies. Label each arrow's transferred object and each node's known shape or `unknown`; distinguish fitting a transformation on training data from applying it to validation or test data. Use the figures under Outputs throughout the comparison, not only in the final specification.

### 4. Generate credible method options

Generate two to four options only when each is:

- compatible with the approved objective and data structure;
- distinguishable in assumptions or tradeoffs;
- feasible enough to specify;
- testable against approved baselines;
- supported by supplied evidence or clearly labeled as AI-generated;
- not merely a package or brand variant.

Label each:

- **Source-backed candidate**
- **Project-constrained candidate**
- **AI-generated candidate**
- **Fixed user-selected route**
- **Blocked candidate**

Possible comparison dimensions include:

- explicit versus learned representation;
- linear, kernel, tree, probabilistic, neural, graph, sequence, spatial, or
  hybrid structure;
- shared versus hierarchical parameters;
- deterministic versus stochastic components;
- discriminative versus generative objective;
- single-task versus multi-task structure;
- constrained versus unconstrained output;
- interpretable versus flexible components.

Do not treat this list as mandatory. Do not invent options when only one route is defensible.

Never rank options with an LLM judge, Bradley-Terry tournament, aggregate score, popularity, novelty, or package availability.

### 5. Build the Method Option Matrix

For each candidate, show:

| Dimension | Required content |
|---|---|
| Scientific fit | Objective and estimand supported |
| Architecture | Modules, connections, information flow, and interfaces |
| Representation | Assumptions and invariances |
| Objective | Terms, constraints, regularization, and optimization target |
| Data demand | Samples, labels, items, sites, and effective observations |
| Leakage risk | Paths and prevention |
| Identifiability | Parameters or components that may not be recoverable |
| Baselines | Simpler and null comparators |
| Evaluation | Metrics, calibration, uncertainty, and split strategy |
| Robustness | Shift, missingness, noise, perturbation, and sensitivity |
| Interpretability | Valid questions and invalid overclaims |
| Compute | Training and inference resource envelope |
| Reproducibility | Seeds, versions, determinism, and artifact needs |
| Evidence | Source, applicability, conflict, and uncertainty |
| Failure modes | Detectable and silent failures |
| Status | Eligible, conditional, blocked, or rejected |

Use no composite score. Preserve incomparable tradeoffs.

### 6. Specify mathematical components

For each eligible candidate, distinguish:

- **Definition**: notation and quantities chosen by the specification;
- **Assumption**: condition required but not established;
- **Derivation**: steps that follow from displayed definitions and assumptions;
- **Empirical proposition**: behavior that requires data or simulation;
- **Conjecture**: plausible but unverified claim;
- **Known result**: source-backed statement with exact applicability.

Specify only what the decision requires:

- input, output, and parameter spaces;
- module functions and compositions;
- objective and regularization terms;
- constraints and invariances;
- probability model when applicable;
- optimization target and stopping concept;
- uncertainty or calibration output;
- dimensions, units, and boundary behavior.

Check algebra, dimensions, domains, limiting cases, sign conventions, and degenerate inputs. Use an already available symbolic or numerical checker only after the user approves the exact expression and check. Do not install one.

Write decision-relevant equations in LaTeX, one `$$ ... $$` display block per formula outside table cells, with symbols, domains, units, and the component's status defined nearby. Connect them to the same candidate's diagram and interface table. A worked substitution uses supplied or separately approved example inputs and checks; do not invent a functional form or execute an example through the visual-detail setting.

Do not claim convergence, identifiability, optimality, unbiasedness, consistency, invariance, or a proof unless the conditions and valid derivation are complete and independently reviewable.

### 7. Build the Evaluation and Ablation Plan

Specify:

- split and resampling unit;
- train, validation, test, external, temporal, or site-held-out roles;
- baseline and null models;
- primary and secondary metrics with denominators and direction;
- uncertainty and calibration checks;
- hyperparameter selection boundary;
- nested selection when required;
- negative controls and leakage probes;
- robustness and distribution-shift checks;
- module, objective-term, input-family, and complexity ablations;
- repeated-seed or initialization sensitivity;
- compute and failure logging;
- criteria for supported, unsupported, insensitive, or inconclusive
  comparisons.

An ablation tests a specified contribution under the selected evaluation design. It does not prove a module's scientific mechanism.

### 8. Build the Threat and Feasibility Register

Include:

- mismatch between computational target and scientific construct;
- shortcut learning and confounding;
- train-test dependence;
- participant, item, site, session, or temporal leakage;
- target leakage through preprocessing or metadata;
- insufficient data for complexity;
- class or outcome imbalance;
- missingness and informative exclusion;
- non-identifiability or equivalent parameterizations;
- unstable optimization and seed sensitivity;
- calibration and uncertainty failure;
- out-of-distribution use;
- subgroup performance and fairness boundaries;
- interpretability overreach;
- compute, storage, latency, and licensing limits;
- mismatch between paper architecture and available implementation;
- post hoc architecture or metric changes.

For each threat, record evidence, assumption, consequence, test, mitigation options, residual risk, owner, and status.

### 9. Present response options

Offer only applicable choices:

- select one candidate;
- combine explicitly compatible elements and rebuild the specification;
- request a named sensitivity or ablation addition;
- keep several candidates for a preregistered comparison;
- return an objective, target, split, or constraint decision to the user;
- prepare a bounded [paper-search](../paper-search/SKILL.md) or [research-literacy](../research-literacy/SKILL.md) handoff;
- prepare an [experiment-controller](../../specialized_skills/experiment-controller/SKILL.md) or Part 4 implementation handoff;
- defer because evidence, data, math, or feasibility is inadequate.

Do not recommend one candidate as the scientific answer.

### 10. Gate 2: The user selects the method

Ask the user to select:

- architecture or candidate set;
- representations, modules, connections, and interfaces;
- objective, constraints, and regularization;
- baselines, split, evaluation, uncertainty, and ablations;
- assumptions and unresolved claims to retain;
- resource and reproducibility requirements;
- selected handoff packets.

Gate 2 authorizes only the selected Computational Method Specification and displayed handoffs.

It does not authorize implementation, executable code generation, training, tuning, observed-data analysis, software installation, saving, manuscript drafting, or an unselected additional capability. A displayed handoff carries only its approved task and preserves the receiving capability's requirements and action gates.

Do not infer selection from silence.

### 11. Produce and verify the Computational Method Specification

Include:

1. scientific objective and intended use;
2. input, output, unit, and permissible-information boundary;
3. selected architecture and information-flow map;
4. module and interface definitions;
5. mathematical definitions, assumptions, derivations, empirical propositions,
   conjectures, and known results;
6. objective, constraints, regularization, and optimization target;
7. baselines and null comparators;
8. data split, evaluation, calibration, and uncertainty plan;
9. robustness, sensitivity, and ablation plan;
10. compute, latency, privacy, licensing, and reproducibility requirements;
11. Threat and Feasibility Register;
12. fixed decisions, open decisions, and post hoc boundaries;
13. selected implementation and evidence handoffs;
14. provenance separating source evidence, AI options, and the user's selections.

Verify:

- every component traces to the approved objective;
- no forbidden information reaches training, tuning, or evaluation;
- shapes, dimensions, units, and interfaces are coherent;
- mathematical claims have the displayed conditions and checks;
- baselines can test whether complexity adds value;
- evaluation does not reuse a selection set as an unbiased test set;
- ablations match their stated question;
- uncertainty and failure behavior are specified;
- no candidate was selected by the skill;
- no implementation, training, analysis, install, search, writing, or save
  occurred.

## Outputs

Return:

1. **Computational Method Brief**
2. **Requirement and Information-Flow Map**
3. **Method Option Matrix**
4. **Mathematical Component Record**
5. **Evaluation and Ablation Plan**
6. **Threat and Feasibility Register**
7. **Response Options**
8. **Gate Decisions**
9. **Computational Method Specification**
10. **Selected Handoff Packets**
11. **Limitations and Unresolved Items**

Return the method design results in the current task's requested form or under the recipient's existing reporting policy.

For a persistent file, implementation code, search, execution, or handoff outside existing authorization:

1. show the exact content or action;
2. show the destination, source, tools, versions, and overwrite behavior;
3. obtain only the outstanding approval;
4. perform only the approved action;
5. verify afterward.

Gate 2 carries authorization for its selected displayed handoffs; do not ask again for that same scope. Gate 1 and Gate 2 do not authorize the other actions above. Preserve each receiving capability's scientific decisions, action gates, and stop conditions.

## Figures and examples

- Full visual detail is the default. Use several complementary views and explanatory examples when they clarify different parts of the approved candidate; there is no fixed figure count. A brief answer or a user request for fewer/no figures takes precedence.
- Before Gate 1, illustrate only the supplied brief. After Gate 1, place figures beside the relevant map, option, component, or evaluation discussion. The final specification includes only user-selected elements after Gate 2. Inline diagram markup explains the chat specification; it is not implementation code or authorization to execute or save.
- Start with an architecture overview, then show information-flow interfaces, fitting versus application, evaluation splits, or an ablation comparison where these reveal a separate issue. Use tables for shapes, units, and candidate tradeoffs; define equations and assumptions beside the component they describe.
- Keep the same candidate IDs, modules, quantities, and notation across views. Label source-backed, project-constrained, AI-generated, blocked, and selected elements as in the option record; keep missing dimensions, parameters, and mathematical choices `unknown`.
- Explain how to read each view and what to notice, including whether arrows mean data transfer, fitting, composition, or an assumed relationship. Use small schematic examples of the candidate's operation without inventing architecture choices, observed results, or performance values.
- Prefer Mermaid, Markdown tables, and LaTeX for chat. Use another representation only when supported within the current authorization. Break crowded diagrams into simpler views; state consequential omissions. More visual detail does not expand the method family or bypass existing checks, gates, or execution boundaries.
- Check figures against the maps and specification for units, shapes, split boundaries, arrow direction, and readable labels. Inspect rendering where possible and give a useful text/table alternative when it cannot be verified. No diagram should merge training and held-out data into a shared fitting step or imply that an ablation establishes a scientific mechanism.

## Boundaries

- **No explicit scientific objective**: Return it to the user; do not infer one
  from a dataset or package.
- **Only one defensible method**: Show the fixed route and its limitations; do
  not invent alternatives.
- **Many candidate architectures**: Bound the set by scientific distinction;
  do not run a tournament.
- **User supplies one architecture**: Specify and stress-test it without
  manufacturing competitors unless the user selects comparison.
- **Package named first**: Separate its capabilities from method selection.
- **Equation supplied without assumptions**: Reconstruct only definitions and
  return missing assumptions.
- **Requested proof lacks conditions**: Label it unproved or false under shown
  counterconditions.
- **Dimensional mismatch**: Block the specification until resolved.
- **Black-box model**: State which interpretation claims are unsupported.
- **Small or clustered data**: Make effective sample, dependence, and
  validation constraints visible.
- **Cross-validation proposed**: Specify the unit, nesting, preprocessing, and
  tuning boundary.
- **Test set used for selection**: Reject an unbiased-test claim and redesign
  prospectively.
- **Ablation after seeing results**: Label it post hoc or exploratory.
- **Multiple sites**: Separate site-held-out evaluation, harmonization, and
  site leakage.
- **Generative output**: Specify validity, diversity, memorization, privacy,
  and evaluation boundaries.
- **No implementation owner**: Return a complete specification and disclosed
  gap.
- **Observed outcomes already known**: Preserve post hoc status; do not relabel
  the architecture as prospectively selected.
- **Context compaction or model switch**: Reload this skill and approved brief
  before continuing.

## Handoffs

- Use [experimental-design](../experimental-design/SKILL.md) for study-level units, conditions, assignment,
  sampling, and general design structures.
- Use [prediction-stress-test](../prediction-stress-test/SKILL.md) for prediction falsifiability,
  counterexamples, boundary conditions, and contrary-result implications.
- Use [research-critique](../research-critique/SKILL.md) to critique an existing complete computational
  method, protocol, or reported study.
- Use [research-literacy](../research-literacy/SKILL.md) for one bounded methodological claim.
- Use [paper-search](../paper-search/SKILL.md) only after separate approval for a bounded architecture,
  optimization, evaluation, or failure-mode evidence need.
- Use [experiment-controller](../../specialized_skills/experiment-controller/SKILL.md) for one checkpointed technical smoke test
  after the method and evaluation specification are approved.
- Route software syntax, implementation, training, tuning, observed-data
  diagnostics, statistical inference, and model comparison execution to the
  relevant Part 4 owner.
- Use [writing-companion](../writing-companion/SKILL.md) only after scientific content is approved for
  publication-facing prose.
- If an invoking companion routed this capability and the destination remains
  unclear, return that unresolved boundary to the invoking companion. If no
  companion invoked it, stop at this capability boundary and offer
  [research-companion](../research-companion/SKILL.md) only as an optional public routing entry.

Each destination begins its own workflow and gates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
