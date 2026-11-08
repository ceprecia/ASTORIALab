# Handoff packets (experimental-design)

Read this reference when the skill or the user asks for it.

## Handoff packets

Prepare a packet only when the user selects it.

### Prediction Stress Test

Use [prediction-stress-test](../../prediction-stress-test/SKILL.md) for prediction falsifiability, counterexamples, contrary-result implications, or bounded novelty:

- exact user-supplied hypothesis and prediction;
- approved design context needed to interpret them;
- selected stress-test question;
- outcome visibility and confirmatory status;
- fixed decisions, evidence boundary, unknowns, and stop point.

### Existing-design critique

Use [research-critique](../../research-critique/SKILL.md) when the request is to evaluate a supplied whole study or design rather than prospectively construct options:

- exact research object and version;
- critique mode or lenses requested;
- supplied question, claims, design, evidence boundary, outcome visibility, confirmatory status, constraints, and unknowns.

### Power work

Use [cogsci-power-analysis](../../../specialized_skills/cogsci-power-analysis/SKILL.md) first when a cognitive or behavioral design needs participant, item, trial, session, reliability, data-loss, or effect-evidence input specification. Use [statistical-power](../../statistical-power/SKILL.md) for the quantitative power, sample-size, MDE, or operating-characteristic calculation after inputs are approved. Use a narrower modality power owner when its inputs are required. The packet must include:

- selected Design Specification;
- exact primary estimand and decision criterion supplied by the user;
- clustering, repeated-measure, blocking, attrition, multiplicity, and allocation structure;
- candidate effect-size basis and uncertainty, without silently selecting an effect;
- feasible sample-size or resource bounds;
- simulation need and unresolved inputs.

### Task, modality, or specialist design

Use an Active task-specific, neuroimaging, acquisition, dataset, adaptive, regulatory, ethics, or domain research capability when the design depends on that expertise. Provide only the approved specification and exact unresolved question. Clinical research design stays within the research question; patient care questions require qualified human expertise outside this assistant-capability dispatch.

Use [cognitive-paradigm-design](../../../specialized_skills/cognitive-paradigm-design/SKILL.md) when a cognitive or behavioral construct still needs prospective comparison of task architectures, operationalizations, trial events, outcomes, and task-impurity risks. Experimental Design retains ownership of the general design family, units, conditions, allocation, assignment, and broad timing structure.

Use [alternative-uses-task-designer](../../../specialized_skills/alternative-uses-task-designer/SKILL.md) after AUT and the general design are approved when the unresolved work is AUT-specific instruction, objects, timing, response capture, task flow, quality control, or assistance-access specification. Experimental Design retains ownership of conditions, units, allocation, assignment, and the broader counterbalancing structure.

Use [visual-search-array-generator](../../../specialized_skills/visual-search-array-generator/SKILL.md) after controlled-array visual search and its scientific parameters are approved when the unresolved work is deterministic layout-manifest generation and constraint validation. Experimental Design retains ownership of conditions, set-size or prevalence factors, cell allocation, and broad counterbalancing.

Use [fmri-task-design-guide](../../../specialized_skills/fmri-task-design-guide/SKILL.md) after the task, neural estimand, primary contrast, proposed first-level model, and acquisition-timing family are approved when the unresolved work is model-aware task-fMRI timing and schedule validation.

Use [bids](../../../specialized_skills/bids/SKILL.md) after the relevant design structure and scientific labels are
approved when the unresolved work is version-pinned source, raw, derivative,
entity, metadata, provenance, privacy, or compliance specification. Experimental
Design retains ownership of the study structure and scientific meaning.

Use [method-design](../../method-design/SKILL.md) after the study objective, units, inputs, outputs, and
evaluation boundary are approved when the unresolved work is prospective
computational architecture, information flow, objective, leakage, validation,
or ablation specification. Experimental Design retains ownership of the study
structure.

Every destination begins its own workflow and gates. Experimental Design approval does not authorize another capability.
