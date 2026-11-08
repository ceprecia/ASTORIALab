---
name: brain-connectivity-modeler
description: >-
  Compares brain-connectivity method families for one user-specified neural
  signal, design, node set, edge estimand, and inference target, then produces a
  selection-bound Connectivity Method Specification. Use when the request, or a
  part coordinator, hands over that exact method-guidance handoff. It distinguishes
  association, context-dependent coupling, model-dependent directed influence,
  and graph summaries; exposes preprocessing, motion, node, edge, lag,
  threshold, multiplicity, reliability, and causal limits; and does not execute
  software, choose regions or thresholds, infer neural causality from BOLD
  timing, or interpret results. Triggers: which connectivity method fits my
  data, compare brain connectivity methods.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: multimodal
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Brain Connectivity Modeler

Compare defensible connectivity method families for one bounded neural
connectivity estimand. Preserve the distinction among connectivity
specification, software implementation, and scientific interpretation.

## Purpose

`brain-connectivity-modeler` owns:

- distinguishing structural, functional, and effective connectivity for one
  approved question;
- defining the node, time-series, edge, network, and inference grains;
- comparing association, task-modulated coupling, generative effective
  connectivity, and graph-summary routes when applicable;
- exposing preprocessing, motion, task-evoked activity, common-input,
  temporal, threshold, density, multiplicity, reliability, and model-space
  threats;
- producing one user-selected Connectivity Method Specification.

The user owns the question, hypothesis, prediction, confirmatory status, modality,
node set, edge meaning, method family, preprocessing choices, thresholds,
model space, priors, contrasts, error criterion, interpretation, and claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns general statistical method-family comparison.
[networkx](../networkx/SKILL.md) owns implementation of an already specified graph representation
and graph operation. [dwi-coordinator](../dwi-coordinator/SKILL.md) owns diffusion acquisition,
reconstruction, tractography, and connectome routing for structural
connectivity. A modality or software adapter owns execution only after the
connectivity specification is approved.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `connectivity`, `network`, `correlation`, `PPI`, `DCM`,
`Granger`, `graph theory`, `resting state`, `fMRI`, `EEG`, or another broad
method or modality term.

Do not use this skill to:

- invent a network hypothesis or select regions;
- treat correlation, prediction, temporal precedence, PPI, or a directed
  model coefficient as model-free evidence of neural causation;
- choose preprocessing, denoising, parcellation, thresholds, density, null
  graphs, priors, or a model space automatically;
- estimate connectivity, fit models, threshold matrices, calculate graph
  metrics, or run software;
- interpret a significant edge, winning model, hub, module, or group
  difference as a scientific conclusion.

## Inputs

Obtain or mark missing:

- approved question, prediction, estimand, and confirmatory or exploratory
  status;
- modality, acquisition, sampling interval, run and session structure, and
  measurement limitations;
- structural, functional, effective, or graph-theoretic target;
- participant, run, trial, condition, time, region, voxel, sensor, source, and
  edge grains;
- node source, independence from the tested effect, atlas or localizer
  version, masks, coverage, and time-series extraction rule;
- edge meaning, direction, sign, weight, conditioning set, frequency or lag,
  and within-subject versus group target;
- task design, psychological contrast, driving inputs, candidate generative
  model space, or resting-state duration as applicable;
- preprocessing, censoring, denoising, filtering, interpolation, motion,
  physiology, global-signal, and temporal-autocorrelation state;
- missing runs or nodes, excluded frames or participants, unequal data
  quantity, and reliability evidence;
- multiplicity family, threshold or density candidates, null model, and
  sensitivity plan;
- desired implementation owner only as a later feasibility constraint.

If the signal, nodes, edge estimand, design, preprocessing state, inference
grain, or confirmatory status is unresolved, stop with **Connectivity intake
incomplete**.

## Steps

### 1. Build the Connectivity Intake Record

| Field | Record |
|---|---|
| user-owned target | Question, hypothesis, prediction, estimand, status |
| Measurement | Modality, acquisition, sampling, hemodynamic or sensor limits |
| Units | Participants, sessions, runs, trials, frames, nodes, edges |
| Nodes | Source, version, independence, coverage, extraction |
| Edges | Association, conditional association, modulation, directed model parameter, or graph input |
| Time | Static, dynamic, task context, frequency, window, lag |
| Preprocessing | Motion, censoring, denoising, filtering, interpolation, physiology |
| Inference | Within-person, group, edge, network, model, or summary |
| Multiplicity | Edge family, model space, thresholds, densities, contrasts |
| Reliability | Data duration, repeated observations, stability evidence |
| Causal boundary | Claim permitted by design and model, and claim not permitted |
| Stop point | Method specification only |

Do not convert `how are these regions connected?` into an estimand.

### 2. Gate 1: approve the bounded connectivity review

Show the intake record, unresolved fields, exact evidence to inspect, method
families to compare, and excluded operations. Ask the user to approve:

- the fixed scientific target, nodes, edge meaning, and inference grain;
- the preprocessing and data-quality state used for comparison;
- the bounded candidate method families;
- any source lookup;
- the fact that no connectivity estimate or graph will be produced.

Gate 1 authorizes only method comparison. It does not authorize data access,
ROI construction, preprocessing, denoising, model fitting, software
execution, thresholding, graph construction, saving, or external writes.

### 3. Eligible connectivity routes

When a connectivity decision is unresolved, present only routes that answer the
approved estimand. Record a single eligible route on its own. The eligible forms
may include:

- **Functional association:** full or conditional association between
  specified time series, with an explicit conditioning and temporal model.
- **Structural edge representation:** an already approved and verified
  tractography-, streamline-weight-, tractometry-, or anatomy-derived edge
  representation with explicit node, assignment, weight, direction,
  missing-edge, and uncertainty semantics. Route any unresolved diffusion
  reconstruction, tractography, or connectome construction to [dwi-coordinator](../dwi-coordinator/SKILL.md)
  before comparing structural edge summaries.
- **Context-dependent coupling:** a PPI-style interaction for an approved
  task contrast, seed, and design. It estimates context modulation, not
  direction or causal influence.
- **Generative effective connectivity:** a prespecified directed generative
  model and bounded model space, such as DCM, when the design and prior
  scientific structure support it.
- **Graph representation:** an approved edge matrix followed by selected
  graph summaries, with explicit signedness, weights, density, threshold, and
  null-graph semantics.
- **Lag-based prediction:** consider only when sampling, observation,
  stationarity, and hemodynamic or conduction assumptions are defensible.
  Current evidence makes fMRI use contested and highly assumption-sensitive,
  not categorically invalid. Report directed predictive dependence and do not
  promote BOLD lag order to neural causal direction.

For every route state the estimand, node and edge grain, assumptions,
preprocessing needs, design requirements, inferential scope, multiplicity,
sensitivity checks, implementation burden, benefit, tradeoff, and main
limitation. Do not rank by available software.

### 4. Document identification in the Connectivity Decision Record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Estimand fit | Node and edge meaning | Identification assumptions | Preprocessing sensitivity | Multiplicity | Reliability | Causal limit | Main limitation |
|---|---|---|---|---|---|---|---|---|

Audit:

- circular node definition or selection and testing on the same effect;
- shared task-evoked responses mistaken for coupling;
- common input, global or physiological signal, scanner drift, and motion;
- filtering, censoring, interpolation, and regression performed in an
  incompatible order;
- temporal autocorrelation, unequal observation counts, or invalid
  exchangeability;
- regional hemodynamic differences used to infer neural direction;
- edge selection, parcellation, model space, or threshold chosen after
  viewing the result;
- graph comparisons confounded by density, sign, weight, disconnectedness, or
  node definition;
- dynamic windows too short for stable estimation or treated as independent;
- weak test-retest reliability hidden by precise group estimates;
- a model comparison interpreted as validation of the true biological
  network.

Keep disagreements among defensible routes visible.

### 5. Gate 2: The user selects one method specification

Ask the user to select, revise, or reject a route and approve:

- modality, nodes, time-series extraction, edge estimand, and inference grain;
- preprocessing, denoising, filtering, censoring, and missing-data handling;
- task contrast, conditioning set, generative model space, or graph semantics;
- multiplicity, threshold or density sensitivities, null model, and
  reliability checks;
- causal-language boundary, implementation owner, and stop point.

Do not infer selection from silence. If outcomes changed a confirmatory node,
edge, model, contrast, or threshold choice, record the deviation and label the
affected work exploratory.

### 6. Return the Connectivity Method Specification

Return:

```text
Brain Connectivity Method Specification
Scope and approved question:
Scientific decisions supplied by the user:
Confirmatory or exploratory status:
Modality, acquisition, and measurement limits:
Participant, run, time, node, and edge grains:
Node definition and independence:
Time-series extraction:
Selected connectivity family and estimand:
Task, context, conditioning, direction, or model space:
Preprocessing and denoising requirements:
Missingness, censoring, and exclusion rules:
Multiplicity and threshold or density plan:
Null model and sensitivity checks:
Reliability and negative controls:
Causal-language boundary:
Known limitations:
Implementation owner and verification:
Stop conditions:
```

The specification does not authorize execution. Route it to one verified
software adapter only through a separate invocation and approval.

## Boundaries

- Functional connectivity is statistical dependence, not direct anatomical
  connection or causation.
- PPI estimates context-dependent association. It does not establish
  direction, mediation, or a causal pathway.
- Effective-connectivity parameters are conditional on the selected
  generative model, inputs, priors, and model space.
- Temporal precedence in BOLD signals does not establish neural direction.
- Granger analysis of fMRI is neither automatically invalid nor self-validating.
  Its claim depends on sampling, downsampling, stationarity, model order,
  conditioning, regional hemodynamic response properties, preprocessing, and
  sensitivity analyses.
- A graph metric inherits every node, edge, sign, weight, threshold, density,
  and null-model choice.
- Network comparison requires comparable observation and preprocessing
  support. Matching density can also remove meaningful strength information,
  so both consequences remain visible.
- A significant model or edge does not validate the whole network.
- Nonsignificance does not establish absence of connectivity.
- Post hoc node, edge, contrast, model-space, or threshold choices remain
  exploratory.
- Successful software execution does not establish measurement validity,
  model identification, or a scientific conclusion.

## Connectivity design and verification

Use the checks relevant to the approved estimand and design. Carry forward a selected method unless a material issue requires the decision owner to review it.

- **Connectivity Decision Record.** Build the decision matrix and threat audit. This makes node, edge, preprocessing, reliability, and causal limits reviewable. Genuine method disagreements remain. Source evidence may not match the user's acquisition.
- **Labeled connectivity route cards.** Compare only connectivity families that answer the fixed edge estimand. This separates association, modulation, directed models, and graph summaries. This requires complete node and signal definitions. This does not estimate an edge.
- **Verified Connectivity Method Specification.** Integrate only user-selected fields into the method specification. This preserves scientific ownership and method-software separation. This defers computation. This cannot establish estimability from prose alone.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Estimated connectivity bundle.** Execute the selected estimator, nulls, and sensitivities. This tests the method against data. This introduces data, software, and outcome-contact risks. This belongs to a separately approved adapter.
- **Extended robustness plan.** Add negative-control, repeated-session, and alternative-node analyses. This tests selected motion, node, and stability threats. This requires more data and multiplicity control. Robustness does not prove causality.
- **Route cards plus recovery scenarios.** Add prespecified simulated-network and preprocessing sensitivity scenarios. This reveals selected identification failures. This adds simulation assumptions and compute. Simulations cannot prove the real network.

## Checks

- **Positive:** a task-fMRI context-modulation question with a fixed,
  independent seed produces PPI and applicable alternative route cards, not a
  fitted model.
- **Negative:** `analyze this resting-state scan` does not trigger this skill.
- **Causality:** a request to infer neural direction from regional BOLD lags
  stops as unsupported.
- **Graph:** a request for hubs without node, edge, signedness, density, or
  null semantics stops before routing to [networkx](../networkx/SKILL.md).
- **Circularity:** a seed selected from the same contrast being tested is
  flagged and requires an independent definition or exploratory label.
- **Overlap:** general statistical questions return to
  [cogsci-statistics](../cogsci-statistics/SKILL.md); graph implementation waits for [networkx](../networkx/SKILL.md).
- **Structural handoff:** raw DWI, reconstruction, tractography, or connectome
  construction returns to [dwi-coordinator](../dwi-coordinator/SKILL.md) before structural-edge comparison.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Friston. (2011). https://doi.org/10.1089/brain.2011.0008
- Novelli et al. (2025). https://doi.org/10.1002/hbm.70285
- O'Reilly et al. (2012). https://doi.org/10.1093/scan/nss055
- Power et al. (2012). https://doi.org/10.1016/j.neuroimage.2011.10.018
- Rubinov & Sporns. (2010). https://doi.org/10.1016/j.neuroimage.2009.10.003
- Smith et al. (2011). https://doi.org/10.1016/j.neuroimage.2010.08.063
