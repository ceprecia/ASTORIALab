---
name: neurokit2
description: >-
  Implements one already approved nonclinical physiological time-series
  operation through an already available, version-verified NeuroKit2 environment
  and returns a source-preserving execution and verification record. Use when
  the request names this skill or an Active capability makes one explicit
  approved implementation handoff. It does not choose a signal-processing
  method, automate a multimodal or full analysis pipeline, install software,
  fetch data, overwrite sources, diagnose, interpret results, or chain later
  analysis. Triggers: process physiological signals with NeuroKit2, ECG EDA or
  respiration pipeline.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: behavior
  dependencies: ""
  requires: Python, NeuroKit2
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-11-02"
---

# NeuroKit2

Implement one approved physiological-signal operation without turning a
convenience wrapper or duration heuristic into a research decision.

## Purpose

`neurokit2` is the conditional Part 4 software adapter for one already
approved nonclinical physiological time-series operation through one already
available, version-verified NeuroKit2 environment. It owns a read-only
environment and input preflight, version-qualified code for one action,
foreground execution after two gates, structural verification, and one neutral
NeuroKit2 Execution Record followed by a stop.

It supports a selected action on ECG, PPG, EDA, respiration, EMG, EOG, an
approved event channel, or an approved generic signal. It does not decide the
signal, method, metric, or claim.

[experimental-design](../../skills/experimental-design/SKILL.md) owns design and measurement choices.
[cogsci-statistics](../cogsci-statistics/SKILL.md) owns inference and statistical interpretation.
`eeg-analysis-guide` and `mne-eeg-tool` own nonclinical scalp EEG method and
implementation work. This adapter does not compete for EEG preprocessing,
sensor-space ERP or time-frequency measurement, source analysis, or MNE work.

The user owns the question, hypothesis, status, signal meaning, population,
acquisition, method, parameters, metric, exclusions, interpretation, and
claim.

Activate only when the user invokes the exact trigger `neurokit2`, or a verified
Active owner makes one exact approved implementation handoff with a completed
incoming specification.

Do not trigger from `ECG`, `HRV`, `EDA`, `GSR`, `PPG`, `respiration`, `EMG`,
`EOG`, `biosignal`, `heart rate`, `clean my data`, `analyze physiology`, a
package name, a file extension, or an automatic analysis request.

This adapter can implement one selected action, such as an input inventory,
unit or sampling check, approved filter, resampling, artifact annotation,
peak, event, epoch, ECG, PPG, EDA, RSP, EMG, EOG, HRV, event-related,
interval, generic-signal, complexity, QC, serialization, or synthetic-fixture
operation. The action must be fully specified before implementation.

A function such as `bio_process`, `bio_analyze`, `ecg_process`, or `hrv` is an
API operation, not approval for every hidden method, feature, and output it
can generate.

This skill excludes:

- selection of a signal, modality, acquisition, event, metric, method,
  threshold, band, artifact, peak, epoch, baseline, quality, exclusion, model,
  or claim;
- clinical, diagnostic, prognostic, therapeutic, monitoring, triage, or
  person-specific interpretation, including rhythm and autonomic-health
  conclusions;
- EEG method or MNE implementation, source localization, microstates,
  connectivity, decoding, unsupported continuous EEG, and multimodal fusion;
- automatic event-related versus interval-related selection based on duration;
- automatic all-metric extraction, plotting, report generation, or full
  pipeline execution;
- installing, updating, switching, creating, or activating environments or
  packages, downloads, network access, credentials, background work, or
  automatic retries; and
- source mutation, overwrite, out-of-tree writes, or automatic owner
  invocation.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Approved operation | One exact NeuroKit2 operation and its completed method or implementation specification |
| Scientific boundary | Target, estimand, status, permitted claim, and method owner if applicable |
| Signal identity | Modality, device, channel, units, sampling, time base, event source, and acquisition metadata |
| Input identity and state | Exact immutable input, provenance, transformations, missingness, artifacts, calibration, and outcome contact |
| Parameter record | Every selected parameter, method, random state, copy semantics, and unresolved value |
| Environment | Existing interpreter, Python and NeuroKit2 versions, package path, optional packages, platform, and API source |
| Access and resources | Permitted reads, privacy, network prohibition, memory, compute, storage, and foreground limit |
| Write and verification boundary | Staging directory, expected files, collision policy, source preservation, invariants, warnings, and mandatory stop |

If the operation, input identity or signal state, units, sampling, parameters,
existing environment, write boundary, or verification rule is missing, return
**NeuroKit2 implementation intake incomplete**. Do not infer it from duration,
a default, filename, channel label, example, or clinical convention.

## Steps

### 1. Build the NeuroKit2 Implementation Intake Record

Separate supplied facts, verified environment facts, specification-bound
choices, open decisions, permitted reads, proposed writes, outcome contact,
and the one-operation stop point. Do not access data, generate code, switch
environments, or write while intake is incomplete.

### 2. Gate 1: approve method readiness and read-only preflight

Show the completed incoming specification, signal identity and state, one
proposed operation, excluded later operations, selected existing environment,
permitted reads, package, resource, privacy, clinical and write risks, and all
missing facts.

Gate 1 authorizes only read-only environment/API checks and exact bounded
input inventory. It does not authorize transformation, execution,
installation, network use, writing, result inspection, scientific QC
acceptance, or later analysis.

### 3. Perform read-only preflight

Verify selected interpreter, imports, versions, signatures, source identity,
signal metadata, output containment, free-space estimate, collision state, and
input invariants. If a prerequisite fails, stop with evidence and do not switch
environments.

### 4. Build the NeuroKit2 Execution Specification

Show exact version-qualified code or command, input and output manifests,
approved parameters, source-preservation behavior, expected effects, resource
limit, warnings, invariant checks, and mandatory stop. Code must contain no
installation, network, background, retry, glob, implicit mode selection,
automatic parameter selection, multimodal join, or overwrite behavior.

### 5. Gate 2: approve one execution and write set

Ask the user to select, revise, or reject the exact code or command, one input,
one operation, complete write set, resource and side-effect boundary,
verification checks, and return point.

Gate 2 authorizes only that one foreground action and write set. It does not
authorize reruns, new parameters, another operation, QC acceptance,
statistics, interpretation, export, or an owner invocation.

### 6. Execute once, verify, and stop

Run once in the approved existing environment. Preserve inputs and partial
outputs. Do not silently retry or change parameters after warnings or failure.

Verify exact versions, code or command hash, warnings, input and output
identity, paths, manifest, sampling, time bounds, units, channels, events,
missingness, finite values, shapes, dtypes, approved signal-specific
invariants, output containment, no source mutation, no overwrite, and no
unexpected files. Structural verification does not accept scientific QC.

On failure, return **NeuroKit2 execution verification failed**, preserve the
record and artifacts, and stop without interpreting or remedying the output.

Return:

```text
NeuroKit2 Execution Record
Approved operation and incoming specification:
Scientific status and permitted claim:
Signal and input identity, units, sampling, and transformation history:
Interpreter, Python, package, API, optional-package, and platform identity:
Read-only preflight evidence:
Approved code or command hash and parameters:
Resource, access, and source-preservation boundary:
Output manifest and execution status:
Warnings, errors, and before and after structural state:
Signal-specific invariants and verification:
Unexpected-file and overwrite audit:
Known limitations, deviations, and outcome contact:
Scientific-QC status: not accepted here
Bounded next owner and mandatory stop:
```

Do not invoke the next owner. A successful package action is not a scientific
conclusion, quality acceptance, or permission to continue.

## Boundaries

Package and API discipline:

- Confirm interpreter, Python, NeuroKit2, optional packages, import path,
  platform, and relevant API signature at invocation time. Capture them in the
  execution record.
- If NeuroKit2 or a required optional package is absent or incompatible,
  return **NeuroKit2 environment unavailable** with exact import evidence. Do
  not install, upgrade, downgrade, create, activate, or silently substitute an
  environment.
- Verify the installed API against official documentation for that version.
  Defaults are implementation facts, never scientific justification.
- Do not call example-data download or remote-data retrieval. Synthetic
  fixtures require explicit selection and remain separate from research output.
- Optional packages are separate runtime facts. Their availability is not
  implied by NeuroKit2 or a package extra.

### Preserve inputs and selections

- Keep research inputs immutable. Use copies or approved staging artifacts and
  record transformations in order.
- Never choose a cleaning method, peak detector, correction algorithm,
  sampling rate, cutoff, band, event threshold, epoch, baseline, HRV domain,
  complexity measure, quality cutoff, or exclusion rule.
- Do not infer event-related or interval-related status from duration.
- Treat detected peaks, components, quality scores, inferred events, and
  automated artifacts as review candidates, not biological facts or clinical
  verdicts.
- Preserve time base, channel identity, units, event IDs, sample indices,
  missingness, annotations, source provenance, and pairing or repeated-measure
  structure unless the approved operation changes them.

### Bind one operation visibly

Before Gate 2, show:

| Field | Required record |
|---|---|
| API binding | Installed version, module, function, signature, and official source |
| Inputs | Exact identity, modality, units, sampling, time base, allowed fields, and read mode |
| Parameters | Approved values, defaults observed but not adopted, and random state if relevant |
| Effects | Expected sample, timing, unit, event, missingness, shape, and file effects |
| Resources and writes | Foreground limit, exact staging paths, formats, collision check, overwrite prohibition, and manifest |
| Verification | Before and after invariants, signal-specific checks, warnings, and failure stop |

If the action needs a method choice or unavailable package,
return it to the relevant research owner or explicit capability gap.

### Signal-specific safeguards

- **ECG, PPG, and HRV:** require the approved source, units, sampling,
  peak-processing method, artifact rule, segment or event definition, metric,
  and interpretation boundary. Do not label arrhythmia, autonomic state, or
  health.
- **EDA, RSP, EMG, and EOG:** require acquisition and channel meaning, units,
  sampling, decomposition or feature method, event relation, and artifact or
  exclusion plan. Do not infer sympathetic activity, pathology, muscle state,
  attention, or emotion from an output.
- **Events and epochs:** require event source, IDs, timing, bounds, baseline if
  any, selection, retention, and paired or repeated-measure structure. Verify
  correspondence without starting a later analysis.
- **Complexity and generic signals:** require an approved signal definition,
  preprocessing state, estimator, parameterization, target, and sensitivity
  rule. A complexity value is not a mechanism or diagnosis.
- **EEG and multi-signal work:** hand EEG to its dedicated owners. A
  multi-signal request needs a completed integration specification; otherwise
  return a capability gap rather than use a convenience wrapper.

Stop when the request is broad, clinical, a full pipeline, unsupported EEG, or
automatic multimodal processing; when operation, input, units, sampling,
method, parameters, environment, path, output, or verification rule is
unknown; when a package is absent; when the route would install, download,
use a network, inspect sealed data, choose a method, or
make a clinical judgment; when source mutation, collision, overwrite,
out-of-tree write, automatic retry, background work, or an unexpected file is
proposed; or when verification fails.

Handoff only after stopping:

- design and measurement questions to [experimental-design](../../skills/experimental-design/SKILL.md);
- statistical questions to [cogsci-statistics](../cogsci-statistics/SKILL.md);
- EEG method or MNE work to [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) or `mne-eeg-tool`; and
- unavailable methods, packages, multimodal integration, or
  another modality to a verified owner or explicit gap.

## Checks

The skill must activate only for `neurokit2` or an exact approved handoff;
require sampling, units, method, environment, output, and verification facts;
reject broad and clinical activation; refuse auto mode selection and full
wrappers; stop on missing packages without installation; preserve source,
timebase, units, events, and output containment; expose code and writes before
Gate 2; execute one operation only; verify structural output without
interpretation; and end with an uninvoked handoff.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Makowski et al. (2021). *Behavior Research Methods, 53*, 1689–1696. https://doi.org/10.3758/s13428-020-01516-y
- NeuroKit2. (n.d.). *NeuroKit2 documentation* (Version 0.2.13.dev214). https://neuropsychology.github.io/NeuroKit/
- NeuroKit2. (2026). *NeuroKit2* (Version 0.2.13) [Computer software]. PyPI. https://pypi.org/project/neurokit2/
