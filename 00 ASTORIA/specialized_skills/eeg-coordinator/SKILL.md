---
name: eeg-coordinator
description: >-
  Routes one bounded nonclinical scalp EEG task from a verified current
  checkpoint to one next Active method, power, statistical, software, or
  specialist owner, then stops after a user-approved handoff record. Use when
  the request names this skill or a verified Active capability hands off one
  exact EEG routing question. It preserves project, scientific, data-state,
  approval, privacy, clinical, package, write, and verification boundaries
  without choosing a task, signal target, preprocessing method, parameter,
  software, model, threshold, interpretation, or claim; accessing data; invoking
  another skill; installing anything; executing code; writing files; or chaining
  a pipeline. Triggers: route my EEG task, next step for my EEG analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: eeg
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-24"
  updated: "2026-11-02"
---

# EEG Skill

Route one EEG checkpoint without turning a modality coordinator into a scientific
decision-maker, package launcher, or full pipeline.

## Purpose

`eeg-coordinator` is the conditional Part 4 coordinator for one bounded nonclinical
scalp EEG task. It owns:

- reconstruction of the verified current EEG project state;
- classification of one current checkpoint;
- comparison of applicable verified Active owners;
- one approval-gated handoff record; and
- an explicit stop after that handoff.

It does not own task, acquisition, power, method, preprocessing, measurement,
statistics, software execution, visualization, interpretation, clinical work,
or scientific claims.

The user owns the question, hypothesis, prediction, confirmatory status, task,
signal target, estimand, population, acquisition, preprocessing, measurement,
exclusion, statistical, software, implementation, interpretation, and claim
decisions. Routing narrows the next owner. It never supplies a missing
scientific decision.

[research-coordinator](../../skills/research-coordinator/SKILL.md) owns research-project continuity and inquiry-part
routing across modalities. [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) owns one approved
sensor-space ERP or event-related time-frequency method specification.
`eeg-coordinator` owns only the EEG-internal checkpoint and next-owner boundary.

Activate only when:

- The user invokes the exact trigger `eeg-coordinator`; or
- a verified Active capability hands off one exact EEG routing question with
  the current project state and requested decision or action.

Do not trigger from `EEG`, `ERP`, `MNE`, `preprocess`, `brain waves`,
`analyze my EEG`, `run the EEG pipeline`, a file extension, a dataset name, a
component label, or another broad modality, software, signal, or action
phrase.

An `.edf`, `.bdf`, `.set`, `.fif`, `.vhdr`, `.mff`, or other filename does
not establish modality, data state, owner, method, or permission.

This coordinator supports one bounded transition among:

- task, event, and marker design;
- acquisition or input-state clarification;
- participant or retained-trial power planning;
- sensor-space ERP or event-related time-frequency method specification;
- implementation of a completed method specification through one verified
  software adapter;
- inferential method selection or approved statistical execution;
- decoding, RSA, connectivity, or another separately owned method;
- bounded QC, reporting, export, or interpretation handoff; and
- a declared capability gap.

This coordinator excludes:

- clinical EEG, diagnosis, seizure detection, sleep staging, prognosis,
  monitoring, neurofeedback, treatment, and person-specific interpretation;
- MEG, OPM, iEEG, ECoG, sEEG, fNIRS, eye tracking, and automatic multimodal
  fusion;
- raw-data inspection, file conversion, preprocessing, feature extraction,
  model fitting, statistics, visualization, export, or interpretation;
- task selection, signal-target selection, parameter choice, threshold choice,
  and method selection;
- environment creation, package or plugin installation, downloads, shell
  commands, background processes, credentials, services, or repositories;
- creating `eeg_output`, logs, state files, feature matrices, reports, or any
  other artifact; and
- invoking, simulating, or automatically chaining the selected owner.

When the request crosses a boundary, identify the verified owner or capability
gap and stop.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Project identity | Current research project or bounded standalone task |
| Scientific contract | user-approved question, prediction if any, estimand, status, and permitted claim |
| Population and design | Population, conditions, sessions, repeated measures, grouping, and relevant governance |
| Modality boundary | Nonclinical scalp EEG, with any auxiliary or other modality stated separately |
| Current checkpoint | Last approved and verified stage, action, artifact, and stop point |
| Input identity and state | Exact supplied artifact or description, provenance, raw or transformed state, prior operations, and known defects |
| Existing approvals | Decisions already approved, decisions still open, deviations, and outcome-contact state |
| Requested next step | One exact decision, review, execution, QC, export, or handoff request |
| Access boundary | What may be read, what must remain unread, privacy lane, credentials, and external restrictions |
| Environment boundary | Relevant software and version only if already verified and directly needed for routing |
| Write boundary | Chat-only routing record unless a later owner obtains separate write approval |

If project identity, modality, current checkpoint, requested next step, input
state, or existing approval state is unknown, return **EEG routing intake
incomplete** and list only the missing fields. Do not inspect raw data or infer
state from filenames, folders, package objects, output presence, or source
defaults.

## Checkpoint model

Classify only the current checkpoint:

| Checkpoint | Routing question | Candidate owner |
|---|---|---|
| Project or part unclear | What bounded research part and owner applies? | Return to the invoking companion; otherwise stop and optionally offer [research-companion](../../skills/research-companion/SKILL.md) as the public routing entry |
| Task, schedule, events, or markers | What approved task implementation and timing specification is needed? | [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) |
| Power or usable-data planning | What participant, trial, or reliability calculation is approved? | [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) or [statistical-power](../../skills/statistical-power/SKILL.md) |
| Sensor-space ERP or event-related time-frequency method | What complete software-neutral method specification is needed? | [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) |
| MNE implementation | Is there a complete approved EEG Analysis Method Specification and one exact software action? | `mne-eeg-tool` only when verified Active |
| Inferential method | What estimand, dependence, multiplicity, and evidence rule must be selected? | [cogsci-statistics](../cogsci-statistics/SKILL.md) |
| Approved statistical execution | Is there a complete Analysis Method Specification and pinned environment? | [statistical-analysis](../../skills/statistical-analysis/SKILL.md) or a verified software adapter |
| Decoding, encoding, RSA, or temporal generalization | Is one predictive or representational estimand approved? | [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md) |
| Connectivity or network inference | Are signal, node, edge, design, and inferential targets approved? | [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) |
| Task-specific implementation, source analysis, continuous spectra, microstates, BCI, or another modality | Does a verified Active canonical owner exist? | Verified owner or explicit capability gap |

The presence of an owner does not establish readiness. Verify that owner's
required incoming artifact and approval conditions before proposing the
handoff.

## Steps

### 1. Build the EEG Current-State Record

Separate:

- supplied facts;
- verified observations;
- AI routing interpretation;
- user-owned approvals;
- unresolved decisions;
- deviations and outcome contact;
- access and write boundaries; and
- the exact requested next step.

Name the last approved artifact and its verification state. If the record
cannot distinguish planned, executed, quality-controlled, accepted, and
interpreted states, stop.

### 2. Gate 1: approve the routing boundary

Show:

1. project, modality, population, and scientific contract;
2. current checkpoint and last verified artifact;
3. decisions already approved and decisions still open;
4. requested next step;
5. information permitted and prohibited for routing;
6. plausible owners and any ownership conflict;
7. missing prerequisites, capability gaps, and stop conditions.

Ask the user to approve, revise, or reject the **EEG Routing Boundary**.

Gate 1 authorizes only chat-based routing from supplied records. It does not
authorize data access, method selection, implementation, code, package
changes, result inspection, file writing, or invocation of another skill.

Reopen Gate 1 after a material project, question, modality, population,
checkpoint, input, approval, outcome-contact, access, or requested-action
change.

### 3. Compare only applicable owners

For each plausible owner, show:

- canonical responsibility;
- required incoming artifact;
- unresolved scientific or operational decision;
- allowed read boundary;
- prohibited action;
- expected output;
- verification needed before the next transition; and
- reason it does or does not match the current checkpoint.

Do not present an owner merely because its package recognizes the file type.
If one owner is fixed by the approved task and registry, explain the fixed
route without inventing alternatives.

### 4. Build the EEG Checkpoint Ledger

Return:

| Field | Record |
|---|---|
| Current checkpoint | |
| Requested next step | |
| Selected owner candidate | |
| Required incoming artifact | |
| Scientific decisions already approved | |
| Scientific decisions still open | |
| Allowed reads | |
| Prohibited actions | |
| Expected output | |
| Acceptance and verification checks | |
| Next mandatory stop | |
| Capability or environment gap | |

An unresolved scientific choice remains open. The coordinator cannot select an
owner whose required input is incomplete.

### 5. Gate 2: approve exactly one handoff

Ask the user to select, revise, or reject:

- one canonical owner;
- one exact requested action;
- one bounded incoming artifact;
- the allowed read and prohibited-action boundary;
- the expected output and verification checks; and
- the mandatory stop before any later checkpoint.

Gate 2 authorizes only the handoff record. It does not invoke the owner,
transfer data, access files, execute software, write artifacts, or authorize
the destination skill's own approval gates.

Do not infer approval from silence, a prior pipeline approval, or the
availability of a package.

### 6. Produce the EEG Routing Record and stop

Return:

```text
EEG Routing Record
Project and bounded task:
Scientific contract and status:
Population and modality boundary:
Current checkpoint:
Last approved artifact and verification:
Requested next step:
Selected canonical owner:
Required incoming artifact:
Approved decisions:
Open decisions:
Allowed reads:
Prohibited actions:
Expected output:
Acceptance and verification checks:
Known gaps, conflicts, deviations, and outcome contact:
Mandatory next stop:
Invocation status: not invoked
```

Stop after the record. The user or the active coordinating workflow must invoke
the destination owner separately.

## Boundaries

Stop and report the exact blocker when:

- the request is clinical, diagnostic, therapeutic, or person-specific;
- scalp EEG or the current modality boundary is not established;
- the current checkpoint or last approved artifact is ambiguous;
- the request combines multiple checkpoints without separate approvals;
- an open scientific decision is being disguised as routing;
- the proposed owner is inactive, missing, duplicated, or outside its scope;
- the destination's required incoming artifact is incomplete;
- the route requires a new dependency, package, plugin, service, credential,
  installation, download, repository, or external write;
- raw data or results would need inspection merely to choose the owner;
- the requested action would cross the sealed-test, privacy, licensing,
  clinical, or governance boundary; or
- no verified Active capability owns the request.

When no owner exists, return **EEG capability gap** with the missing
capability, required input, prohibited workaround, and decision needed.

## Handoffs

### Preserve scientific ownership

- Never choose the task, event lock, component, frequency band, feature,
  reference, filter, artifact procedure, epoch, baseline, sensor set,
  exclusion, model, metric, or threshold.
- Never fill an open decision from a package default, benchmark, candidate
  source, familiar pipeline, filename, or previous project.
- Never turn an ERP label, oscillation, feature, classifier, graph, or
  microstate into a cognitive mechanism, anatomical source, diagnosis, or
  individual-level conclusion.
- Record outcome-informed changes as deviations. Do not restore a
  confirmatory label through routing.

### Preserve checkpoint separation

- Route one checkpoint and one owner per invocation.
- Preprocessing approval does not authorize feature extraction, statistics,
  export, interpretation, or the next checkpoint.
- A method specification does not authorize software execution.
- Software availability does not choose a method.
- Successful execution does not constitute scientific or visual QC.
- A QC handoff does not authorize exclusion, rerunning, or interpretation.
- A handoff record does not invoke the destination skill.

### Preserve data and operational boundaries

- Use only supplied summaries, approved specifications, inventories, and
  verification records needed to route.
- Do not open raw recordings, participant-level outputs, credentials, private
  lanes, or sealed-test artifacts.
- Treat every environment, package, API, command, path, output, and version
  claim as unverified unless supported by current evidence.
- Do not install, update, download, clone, authenticate, execute, write,
  overwrite, submit, or start background work.
- Report a missing owner, unavailable environment, unresolved permission, or
  failed verification as a gap. Do not broaden this coordinator to absorb it.

## Checks

The skill must:

- activate for exact `eeg-coordinator` and reject broad EEG phrases;
- stop on missing checkpoint or approval state;
- route task and marker work to [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md);
- route a software-neutral ERP method question to
  [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md);
- refuse MNE execution without a complete approved method specification and
  a verified Active adapter;
- preserve paired, grouped, repeated-measures, and outcome-contact facts;
- reject clinical seizure interpretation;
- report source localization, continuous spectra, microstates, BCI, and
  unsupported modalities as a verified owner or explicit gap;
- produce two separate gates and one handoff record;
- leave the destination uninvoked; and
- produce no data, code, command, environment, log, folder, feature, result,
  visualization, or file mutation.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
