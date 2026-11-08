---
name: run-models
description: >-
  Compares a bounded set of verified Active neuroimaging deep-model cards
  against one already approved prediction specification and returns an evidence,
  compatibility, tradeoff, limitation, compute, and handoff record without
  selecting or running a model. Use when the request names this skill or
  neural-decoding-analysis routes one exact post-specification deep-model
  comparison. It keeps the individual-card lane separate from the overlapping
  NeuroSTORM platform lane, loads only normalized comparator summaries before
  selection, and loads only the user's selected full card afterward. It does not
  formulate a target, choose a model, compare headline performance across
  incompatible studies, install software, inspect a sealed test set, preprocess
  data, fit or evaluate a model, load every card, write files, or chain
  implementation. Triggers: which deep model fits my prediction, compare
  neuroimaging deep models.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: fmri
  dependencies: ""
  requires: an approved prediction specification; the Active model-card skills (bnt, neurostorm)
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Run Models Comparator

Compare verified neuroimaging deep-model implementation cards without turning
the catalog, package availability, or reported benchmark performance into an
automatic scientific decision.

## Purpose

`run-models` owns:

- the ASTORIA catalog of eligible neuroimaging deep-model cards;
- separation of the standalone individual-card lane from the overlapping
  NeuroSTORM platform lane;
- bounded inspection of normalized comparator summaries from only the
  approved candidate set;
- comparison of exact source, intended task, input, output, validation,
  leakage, baseline, interpretability, compute, license, availability, and
  limitation evidence;
- explicit incompatible, unresolved, and not-comparable states;
- one user-selected full-card handoff without implementation authority;
- a Deep Model Comparison Record.

The user owns the question, hypothesis, prediction, target, estimand,
confirmatory status, population, input representation, evaluation design,
generalization target, candidate lane, candidate set, metrics, baselines,
fairness questions, compute budget, model selection, implementation,
interpretation, and claims.

[neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) owns the predictive estimand, target,
generalization, validation, leakage, metric, null, multiplicity, baseline,
and broad estimator-family specification. [fmri-coordinator](../fmri-coordinator/SKILL.md) and [smri-coordinator](../smri-coordinator/SKILL.md)
own modality routing and approved preparation handoffs. Each selected model
card owns only its bounded implementation intake and execution after a
separate invocation and approval. `run-models` does not replace any of those
owners.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `run models`, `model card`, `deep learning`, `machine
learning`, `phenotype prediction`, `BrainGNN`, `BNT`, `FM-APP`,
`NeuroSTORM`, `best model`, `classifier`, `diagnosis`, `fMRI`, `sMRI`, or
another broad model, task, modality, or implementation phrase.

Do not use this skill to:

- formulate a prediction target or decide that deep learning is appropriate;
- compare classical GLM, ICA, DictLearning, clustering, SVM, SpaceNet,
  filtering, detrending, or harmonization methods;
- compare the NeuroSTORM platform and its overlapping standalone model cards
  in one candidate set;
- treat an external-catalog candidate or uninstalled model card as Active;
- load full instructions for every card;
- choose a model, hyperparameter, input representation, split, metric,
  baseline, threshold, or compute route;
- compare accuracy, AUC, loss, or another metric across different targets,
  populations, datasets, preprocessing, splits, or evaluation units as if
  they were commensurable;
- install, clone, pull, download weights, create environments, preprocess,
  train, tune, evaluate, infer, inspect a sealed test set, or write output;
- call an attention map, pooling score, saliency map, or learned embedding a
  neural mechanism or validated explanation;
- diagnose, prognose, monitor, or recommend treatment for a person.

## Inputs

Obtain or mark missing:

- one approved Neural Decoding Method Specification or equivalent fixed
  prediction specification;
- question, target, prediction unit, permitted claim, exploratory or
  confirmatory status, and prohibited clinical use;
- population, sites, acquisitions, modalities, preprocessing state, input
  representation, atlas, shape, feature timing, and missingness;
- dependence groups, train, validation, tuning, calibration, and sealed-test
  boundaries;
- generalization target, primary metric, uncertainty unit, descriptive
  baseline, statistical null when applicable, and multiplicity plan;
- negative controls, confound controls, fairness or subgroup questions,
  sensitivity analyses, and acceptance criteria;
- approved deep-model family scope and candidate lane;
- approved candidate set from the current eligible catalog;
- compute, hardware, memory, storage, time, energy, scheduler, and local or
  managed-environment constraints;
- license, privacy, data-governance, weight-access, network, and credential
  boundaries;
- exact catalog snapshot date and card verification dates;
- handoff and no-save boundary.

If the target, prediction unit, input representation, split, generalization
target, metric, baseline, candidate lane, compute budget, or permitted claim
is unresolved, stop with **deep-model comparison contract incomplete** and
return the missing scientific design to [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md).

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm a post-specification comparison

Verify that the incoming specification already fixes:

- what is predicted and at what observation grain;
- the intended population and generalization boundary;
- the exact input representation available before outcome contact;
- train, tuning, calibration, validation, and sealed-test boundaries;
- primary metric, uncertainty unit, baseline, null when applicable, and
  multiplicity;
- leakage, confound, subgroup, and negative-control plan;
- permitted and prohibited claims;
- why a deep-model implementation comparison is in scope.

Do not convert `which model is best?` into a comparison contract. Do not
infer a target from available labels or a model from available packages.

### 2. Choose one catalog lane

Choose exactly one:

1. **Individual-card lane:** compare eligible standalone ASTORIA model
   cards. Each card later owns its own exact implementation.
2. **NeuroSTORM platform lane:** evaluate NeuroSTORM as one platform route
   through the `neurostorm` card. Do not simultaneously load or compare its
   overlapping standalone cards.

Show the workflow change, visible outputs, benefit, tradeoff, and limitation
of each applicable lane. The individual lane supports implementation-level
separation but may expose heterogeneous repositories and environments. The
platform lane may offer one integrated route but carries platform-wide data,
environment, and orchestration assumptions. These are design implications,
not a recommendation.

### 3. Build the Deep Model Comparison Contract

Create:

| Element | Approved meaning | Evidence required | Missing or conflicting state | Stop rule |
|---|---|---|---|---|
| Target and prediction unit | | | | |
| Population and generalization | | | | |
| Input representation and timing | | | | |
| Split, tuning, calibration, and sealed test | | | | |
| Metric, uncertainty, baseline, and null | | | | |
| Candidate lane and set | | | | |
| Leakage, confounds, fairness, and controls | | | | |
| Interpretability and claim boundary | | | | |
| Compute, license, privacy, and availability | | | | |
| Handoff and stop point | | | | |

### 4. Gate 1: approve lane, candidates, and comparison criteria

Show:

- fixed prediction and evaluation specification;
- current eligible catalog plus pending or blocked candidates;
- individual-card versus platform-lane implications;
- proposed candidate set;
- exact comparison fields and non-comparable conditions;
- catalog and card verification dates;
- missing evidence, source conflicts, license concerns, package or weight
  blockers, and sealed-test boundary;
- the rule that no full card, repository, package graph, weights, data, or
  result are loaded at this gate.

Gate 1 authorizes comparison of only the selected candidates by reading their
frontmatter and bounded Comparator Summaries. It does not authorize full-card
loading, repository or network access, installation, weight access, data
inspection, preprocessing, fitting, tuning, evaluation, inference,
sealed-test contact, saving, or model selection.

If the user changes the lane, target, input representation, split, metric,
baseline, candidate set, or compute boundary, rebuild the contract.

### 5. Load only bounded summaries

For each approved candidate:

- verify the card skill folder exists, canonical ownership, description fit, lane, source,
  license, and verification date;
- read only frontmatter and the Comparator Summary;
- preserve every unresolved, conflicting, absent, stale, or non-comparable
  field;
- record whether the candidate requires an unapproved package, service,
  credential, weights file, network action, license acceptance, or external
  write later;
- do not inspect full workflow instructions, scripts, repositories, code,
  weights, data, results, or examples.

If the candidate's exact source or license is unclear, exclude it from
selection and preserve the reason.

### 6. Compare without a winner score

Create:

| Candidate | Target and output fit | Input and domain fit | Validation and leakage | Baselines and comparability | Interpretability limits | Compute and availability | License and governance | Missing evidence |
|---|---|---|---|---|---|---|---|---|

Use only four field states:

- **Compatible within recorded evidence**
- **Incompatible with the approved specification**
- **Unresolved**
- **Not comparable**

Do not total, weight, average, rank, or color these states into a composite
score. Do not use reported performance as a tiebreaker when evaluation
contexts differ.

For every candidate expose:

- exact workflow and representation implications;
- evidence versus assumptions;
- validation and leakage risks;
- baseline and ablation adequacy;
- domain, subgroup, calibration, and fairness limits when relevant;
- interpretability artifact versus permitted interpretation;
- compute and environment costs;
- license, privacy, weight, and governance constraints;
- benefit, tradeoff, limitation, and unresolved evidence.

### 7. Audit comparison validity

Stop or mark not comparable when candidates differ materially in:

- prediction target, outcome timing, class ontology, or prediction unit;
- participant, session, scan, site, family, or longitudinal split;
- dataset, population, acquisition, atlas, input representation, modality,
  preprocessing, or missingness handling;
- target access during feature construction, harmonization, nuisance
  removal, model selection, or hyperparameter tuning;
- training size, external validation, sealed-test status, or evaluation unit;
- metric definition, threshold, calibration, uncertainty, subgroup, or
  multiplicity handling;
- baseline strength, data access, pretrained weights, or compute budget.

Model-card performance is descriptive evidence tied to its exact evaluation
context. It does not predict performance on the user's data and does not establish
superiority.

Interpretability artifacts remain model behavior. Attention, pooling,
saliency, learned communities, or selected nodes do not by themselves
identify neural mechanisms, causes, biomarkers, or clinically meaningful
regions.

### 8. Produce the comparison record

Return:

```text
Deep Model Comparison Record
Approved prediction and evaluation specification:
Catalog snapshot, lane, and approved candidate set:
Eligible, pending, excluded, and unresolved cards:
Candidate source, license, and verification states:
Target, output, input, and domain comparison:
Split, validation, leakage, calibration, and uncertainty comparison:
Baseline, ablation, and performance-comparability record:
Interpretability artifact and claim limits:
Compute, runtime, package, weight, privacy, and governance constraints:
Benefits, tradeoffs, limitations, and missing evidence:
Non-comparable fields and reasons:
No-selection and sealed-test boundary:
user-owned selection, revision, rejection, or deferral:
```

### 9. Gate 2: The user selects, revises, rejects, or defers

Ask the user to:

- select one exact eligible card;
- revise the comparison contract or candidate set;
- reject all candidates; or
- defer because evidence, resources, license, or implementation readiness is
  insufficient.

Do not infer selection from silence, ordering, availability, familiarity,
reported performance, or a single compatible state. If only one card remains
eligible, explain the fixed route and still require explicit selection.

Gate 2 authorizes loading only the selected full ASTORIA card and
preparing one handoff packet. It does not authorize external source access,
installation, environment changes, weights access, preprocessing, fitting,
tuning, evaluation, inference, output writing, saving the comparison, or
downstream interpretation.

### 10. Load one selected card and hand off

After explicit selection:

- verify that the selected card state and summary have not changed;
- load only that full ASTORIA card;
- compare its full required inputs and stop conditions with the approved
  specification;
- expose any new package, service, credential, license, download, write, or
  scientific decision;
- return a bounded handoff packet to that card;
- stop before implementation.

Return:

```text
Selected Deep Model Handoff
Selected card and exact trigger:
Why it remains compatible within recorded evidence:
Approved target, input, split, metric, baseline, and claim boundary:
Full-card requirements and newly exposed blockers:
Source, license, environment, weights, compute, and data boundaries:
Required later approvals:
No execution or saving authority:
```

## Boundaries

The package includes individual BNT and NeuroSTORM platform cards. Verify their current installed state, source and input requirements before selection. Other model cards are not supplied by this package and remain ineligible until a separately reviewed capability is installed and verified.

The live [Skill Map](../../Skill%20Map.md) and the card itself determine current eligibility. A
candidate is eligible only when:

- one Active ASTORIA skill owns it canonically;
- it has one exact trigger and no conflicting active owner;
- its exact source state, license, retained and rejected elements, runtime
  boundary, and verification date are recorded;
- it contains the normalized Comparator Summary below;
- its known inputs, outputs, validation evidence, leakage risks, baselines,
  compute, limitations, and missing evidence are explicit;
- the current comparison does not require an unapproved package, service,
  credential, installation, download, or external write merely to inspect
  the card.

Pending, missing, stale, conflicting, or incomplete cards are visible but not
selectable. Do not reconstruct their contents from an external catalog, an upstream wrapper,
chat memory, or another model's card.

Rules and stops:

- Stop if the prediction specification or deep-model family decision is
  missing.
- Stop if both catalog lanes are requested in one comparison.
- Stop if a candidate is Pending, inactive, stale, conflicting, missing its
  Comparator Summary, or lacks exact source or license evidence.
- Stop before reading every full model card.
- Stop on target, input, split, metric, baseline, or evaluation-context
  mismatches that make performance non-comparable.
- Stop on preprocessing, feature selection, harmonization, nuisance removal,
  or tuning performed outside the applicable training boundary.
- Stop before sealed-test access or result-driven candidate changes.
- Stop before installation, cloning, downloading weights, environment
  creation, external service use, credentials, data writes, model execution,
  or automatic saving.
- Never select by reported accuracy, architecture novelty, interpretability
  branding, local package availability, or source popularity.
- Never turn an unresolved field into a favorable assumption.
- Never call model outputs diagnostic, causal, mechanistic, clinically
  validated, or generalizable beyond their exact evidence.
- A selected card is a handoff decision, not implementation authority.
- Apply TRIPOD+AI reporting considerations only when the approved task is an applicable health prediction study; it is not a clinical-use authorization or a universal model selector.

## Required Comparator Summary in every eligible card

Read only frontmatter and this bounded section before Gate 2:

```text
Model Card Comparator Summary
Canonical owner and exact trigger:
Lane:
Model, paper, code, release or commit, license, and verification date:
Intended research task and prohibited uses:
Target type, prediction unit, and output semantics:
Required modalities, input representation, shape, atlas, and preprocessing:
Training, fine-tuning, inference, and pretrained-weight state:
Population, acquisition, site, and domain evidence:
Partition, tuning, evaluation, calibration, and uncertainty evidence:
Leakage controls and unresolved leakage risks:
Baselines, ablations, and comparison fairness:
Performance evidence with exact dataset and evaluation context:
Interpretability artifact and permitted claim:
Runtime, package, hardware, memory, storage, and time requirements:
Determinism, provenance, failure, and verification behavior:
Known limitations, missing evidence, and implementation blockers:
```

If a summary is incomplete, mark the corresponding field unresolved. Do not
open the full card to fill it before the user selects that card.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Collins et al. (2024). TRIPOD+AI. https://doi.org/10.1136/bmj-2023-078378
- Kapoor & Narayanan (2023). Leakage and the reproducibility crisis in machine-learning-based science. https://doi.org/10.1016/j.patter.2023.100804
- Mitchell et al. (2019). Model cards for model reporting. https://doi.org/10.1145/3287560.3287596
