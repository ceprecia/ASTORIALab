---
name: mne-eeg-tool
description: >-
  Implements one already approved nonclinical sensor-space scalp EEG operation
  through an already available, version-verified MNE-Python environment and
  returns a source-preserving execution and verification record. Use when the
  request names this skill or an Active capability makes one explicit approved
  implementation handoff. It does not choose methods or thresholds, run a full
  pipeline, install software, fetch data, overwrite sources, interpret results,
  or chain later analysis. Triggers: run this in MNE-Python, MNE epochs or
  evoked operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: eeg
  dependencies: ""
  requires: Python, MNE-Python
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-11-02"
---

# MNE EEG Tool

Implement one selected EEG operation without turning a package default, an
archived wrapper, or an available environment into a method decision.

## Purpose

`mne-eeg-tool` is the conditional Part 4 implementation owner for one
already approved nonclinical sensor-space scalp EEG operation through an
already available MNE-Python environment. It owns:

- a read-only environment, API, input, and write-boundary preflight;
- translation of one completed specification into version-qualified code;
- foreground execution of one selected operation after two gates;
- structural and operation-specific verification; and
- one neutral MNE Execution Record followed by a stop.

Loading, header inspection, staging, writing, and verification may support
the one approved operation. They do not authorize a later processing step.

[eeg-analysis-guide](../eeg-analysis-guide/SKILL.md) owns ERP and event-related time-frequency method
selection, including filtering, resampling, reference, rank, channels,
artifacts, interpolation, epochs, baselines, measurements, exclusions, QC,
and statistical handoff. [eeg-coordinator](../eeg-coordinator/SKILL.md) may route a checkpoint but does not
authorize execution. [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) owns task schedules, event
markers, and physical timing. [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential model
selection and statistical interpretation.

The user owns the question, hypothesis, prediction, scientific status, task,
signal target, estimand, population, acquisition, method, parameters,
software route, inputs, outputs, exclusions, interpretation, and claims.

Activate only when:

- The user invokes the exact trigger `mne-eeg-tool`; or
- a verified Active owner hands off one exact approved implementation action
  with its completed incoming specification and explicit authority boundary.

Do not trigger from `MNE`, `EEG`, `ERP`, `P300`, `preprocess`, `clean my
EEG`, `analyze my EEG`, a package name, a file extension, a dataset, or a
request for an end-to-end pipeline.

This skill may implement one selected action on a supplied nonclinical,
sensor-space scalp EEG artifact when an approved specification defines its
scientific and operational choices. Eligible actions include:

- a format-aware load or header inventory;
- one approved filter, notch, resampling, rereference, annotation,
  bad-channel, interpolation, projection, or rank-aware transformation;
- one approved ICA fitting, component-review preparation, or application
  action;
- one approved event, epoch, baseline, averaging, or event-related
  time-frequency action;
- one approved descriptive QC, serialization, or structural verification
  action; and
- one exact MNE ecosystem action supplied by a verified dedicated method
  owner, when its package is already available and version-qualified.

The last category does not make this a method owner. For example,
connectivity, decoding, CSP, source analysis, microstates, continuous or
resting spectra and BCI require an exact completed
specification from their dedicated owner. If no such owner exists, report a
capability gap.

This skill excludes:

- task, marker, acquisition, power, method, feature, model, statistic,
  threshold, or claim selection;
- clinical EEG, diagnosis, seizure review, sleep staging, neurofeedback,
  monitoring, prognosis, treatment, or person-specific interpretation;
- MEG, OPM, iEEG, ECoG, sEEG, fNIRS, eye tracking, and automatic multimodal
  fusion;
- source localization, inverse modeling, anatomical claims, or unsupplied
  method specifications;
- installing, updating, downloading, activating, creating, or silently
  switching environments, packages, plugins, services, or credentials;
- network access, dataset fetching, repository access, background jobs,
  `tmux`, automatic retries, or automatic owner invocation;
- mutating source inputs, clearing provenance, overwriting, or writing beyond
  the approved staging directory; and
- running an archived full-pipeline wrapper, automatic preprocessing, feature
  extraction, ICA rejection, interpolation, connectivity, CSP, asymmetry,
  microstate, or export bundle.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Approved operation | One exact operation and its completed method or implementation specification |
| Scientific boundary | Approved target, estimand, status, permitted claim, and relevant owner |
| Input identity | Exact file or object, immutable source location, format, hash or equivalent identity, and provenance |
| Input state | Prior operations, montage, channel types and units, reference, sampling, filters, annotations, events, rank, bads, and outcome contact |
| Parameter record | Every operation parameter, evidence source, fixed choice, random state, copy or in-place semantics, and unresolved value |
| Environment | Selected existing interpreter, Python and MNE versions, package paths, optional package versions, platform, and API verification source |
| Resource boundary | Expected memory, compute, storage, runtime, and foreground-only limits |
| Access boundary | Permitted reads, privacy and governance restrictions, network prohibition, and sealed-test state |
| Write boundary | Exact staging directory, expected files, collision policy, source-preservation rule, and verification destination |
| Acceptance boundary | Structural invariants, operation-specific checks, warnings, failure handling, and next mandatory stop |

If the operation, completed specification, input identity or state, parameters,
selected existing environment, write boundary, or verification rule is
missing, return **MNE implementation intake incomplete**. Do not infer it
from a filename, source wrapper, MNE default, familiar recipe, or package
availability.

## Steps

### 1. Build the MNE Implementation Intake Record

Separate supplied facts, verified environment facts, specification-bound
choices, open decisions, permitted reads, proposed writes, outcome contact,
and the exact one-operation stop point.

Do not access data, switch environments, generate executable code, or write
an artifact while required intake is missing.

### 2. Gate 1: approve method readiness and read-only preflight

Show:

1. the completed incoming specification and its owner;
2. the exact input, transformation history, and scientific boundary;
3. the one proposed operation and excluded later operations;
4. the selected existing environment and API facts to verify;
5. permitted read-only metadata and input access;
6. anticipated package, resource, privacy, sealed-test, and write risks; and
7. missing parameters, source companions, or verification conditions.

Ask the user to approve, revise, or reject the **MNE Method-Readiness Boundary**.

Gate 1 authorizes only read-only environment/API checks and the exact bounded
input inventory needed to prepare an execution specification. It does not
authorize transformation, code execution, installation, network access,
writing, output inspection, scientific QC acceptance, or later analysis.

### 3. Perform read-only preflight

After Gate 1, verify the selected interpreter and the required imports and API
signatures. Inventory the approved source without altering it. Check path
containment, companion files, source identity, read permission, output
directory existence, free-space estimate, collision state, and the expected
input-object invariants.

If the environment, input, path, or API cannot be verified, stop with the
exact evidence. Do not retry through a different environment or package.

### 4. Build the MNE Execution Specification

Show exact version-qualified code or command before execution, together with:

- interpreter, package, platform, and API identity;
- source and proposed output manifests;
- approved parameters and copy or mutation semantics;
- resource estimate and foreground-only limit;
- expected warnings and failure behavior;
- structural and operation-specific verification checks; and
- the mandatory stop after this action.

Code may use only the selected existing environment and approved paths. It
must not contain installation, download, network, background, retry,
unbounded glob, automatic parameter selection, or overwrite behavior.

### 5. Gate 2: approve one execution and write set

Ask the user to select, revise, or reject:

- the exact code or command and version-qualified API;
- one input and one operation;
- the complete output manifest and staging directory;
- resource and side-effect boundary;
- invariant and warning checks; and
- the return point and stop condition.

Gate 2 authorizes only that one foreground action and exact write set. It does
not authorize the next preprocessing step, additional data, parameter
changes, reruns, QC acceptance, statistical analysis, interpretation, export,
or another skill.

### 6. Execute once and verify

Run once in the approved existing environment. Preserve source inputs and
retain any partial output for review. Do not silently change parameters or
retry after a warning or failure.

Verify as applicable:

- return status, emitted warnings, code or command hash, and exact versions;
- input and output identities, paths, hashes, object types, and file manifest;
- channel count, order, types, units, sampling, time bounds, montage,
  reference, bads, annotations, events, metadata, and rank state;
- expected shapes, dtypes, finite values, retained and rejected counts, and
  operation-specific timing or filter invariants;
- output containment, no source mutation, no overwrite, and no unexpected
  files; and
- the boundary between structural verification and scientific acceptance.

If verification fails, return **MNE execution verification failed**, preserve
the artifacts and record, and stop. Do not interpret the failure or execute a
remedy.

### 7. Produce the MNE Execution Record and stop

Return:

```text
MNE Execution Record
Approved operation and incoming specification:
Scientific status and permitted claim:
Input identity, state, and transformation history:
Interpreter, Python, package, API, and platform identity:
Read-only preflight evidence:
Approved code or command hash:
Approved parameters and copy semantics:
Resource and access boundary:
Output manifest and source-preservation state:
Execution status, warnings, and errors:
Before and after structural state:
Operation-specific invariants and verification:
Unexpected-file and overwrite audit:
Known limitations, deviations, and outcome contact:
Scientific-QC status: not accepted here
Bounded next owner and mandatory stop:
```

Do not invoke the next owner. A successful MNE operation is not a scientific
conclusion, QC acceptance, or permission to continue.

## Boundaries

Package and API discipline:

- Confirm the selected interpreter, Python version, MNE version, import path,
  package location, optional package version, and relevant API signature at
  invocation time. Capture them in the execution record.
- The environment must already be available. If MNE or a required optional
  package is absent or incompatible, return **MNE environment unavailable**
  with exact version and import evidence. Do not install, upgrade, downgrade,
  create, activate, or substitute an environment.
- Verify the selected installed API against the official documentation for
  that version before generating code. A documented default is an
  implementation fact, not scientific authorization.
- Use format-aware readers. A BDF input requires the verified BDF reader, not
  an assumed EDF route. BIDS requires an exact `BIDSPath`, an already
  available version-verified MNE-BIDS installation, and an approved BIDS
  operation.
- Treat MNE core, MNE-BIDS, AutoReject, MNE-Connectivity, and any other
  package as separate runtime facts. Their availability is never implied by
  MNE, an archive, or an extra such as `mne[full]`.
- Never run `eeg_pipeline_reference.py`, a `claw-shell` command, or a source
  example as executable authority.

### Preserve inputs and scientific selections

- Keep source recordings and source derivatives immutable. Use copies or an
  approved staging artifact, and record every transformation in order.
- Never choose or silently accept a reference, filter, notch, resampling
  rate, line frequency, bad channel, interpolation route, ICA component,
  rejection threshold, event channel, epoch, baseline, time window, sensor,
  frequency band, CSP component count, connectivity measure, or microstate
  count.
- Do not assume `STI 014`, EOG, ECG, F3, F4, electrode locations, line
  frequency, a montage, full rank, or a canonical band from their absence or
  a source recipe.
- Treat automated artifact labels, component scores, bad-channel scores, and
  rejection suggestions as review candidates. Do not apply them without the
  completed specification and explicit approved action.
- Preserve event IDs, sample indices, channel order and types, units,
  reference state, annotations, bad-channel markings, metadata, and rank
  accounting unless the approved operation explicitly changes them.

### Bind the operation to the specification

For every action, make the following inspectable before Gate 2:

| Field | Required record |
|---|---|
| API binding | Installed version, module, function or method, signature, and documentation source |
| Inputs | Exact source identity, required companion files, object type, read mode, and allowed fields |
| Parameters | Completed approved values, units, defaults observed but not adopted, and random state if relevant |
| Effects | Expected timing, rank, channel, unit, annotation, event, shape, and file effects |
| Resources | Memory, compute, disk, runtime, and foreground execution boundary |
| Writes | Exact staging paths, file formats, collision check, overwrite prohibition, and output manifest |
| Verification | Before and after invariants, operation-specific checks, warning policy, and failure stop |

If an action would require a method choice, return it to the relevant method
owner. If it requires a new package or unavailable API, stop rather than
rewriting the method around what is installed.

### Operation-specific safeguards

- **Read and inventory:** verify format-specific reader, companion files,
  object type, header fields, channel types, units, sampling, montage,
  reference, filters, annotations, events, and known transformations. Do not
  crawl a directory or fetch missing files.
- **Filtering or resampling:** implement only a complete approved filter or
  resampling specification, preserve source sampling and event reconciliation
  records, and verify expected channel, sample, timing, and finite-value
  invariants. Record the actual MNE design settings and warnings.
- **Bad channels, reference, rank, and interpolation:** require the approved
  evidence and ordered plan. Verify montage suitability, channel identities,
  reference change, bads before and after, and rank consequences. Never clear
  bad-channel provenance merely to make an operation succeed.
- **ICA or other correction:** require the approved fitting state, high-pass
  state, picks, rank, component count, random state, review evidence,
  exclusions, and copy/application target. A requested count above available
  rank is a stop, not a value to clip automatically.
- **Events and epochs:** require exact event source, event IDs, timing,
  `tmin`, `tmax`, baseline, selection, rejection, metadata, and drop policy.
  Verify event/sample correspondence, counts by condition, timing, retained
  and rejected records, and no later averaging or feature action.
- **ERP or time-frequency action:** require the completed independent
  measurement definition. Never search for a largest peak, select a window,
  infer a band, or create a mechanism claim from an output.
- **Connectivity, decoding, CSP, or microstates:** require the dedicated
  method owner's completed specification, the already available exact package,
  and a leakage, split, or stability rule where applicable. Do not fit CSP on
  all data for later evaluation, serialize opaque objects as results, or use
  pickled output by accident.

Stop when:

- the request is broad, clinical, another modality, or a full pipeline;
- the method specification or a material parameter is incomplete;
- the selected environment, package, API, input, companion file, resource,
  path, privacy boundary, output manifest, or verification rule is unknown;
- MNE or a required optional package is absent, incompatible, or unverified;
- an operation would choose a scientific method, read a sealed test set,
  download data, use a network service, or install a
  dependency;
- source mutation, output collision, overwrite, out-of-tree write, automatic
  retry, background execution, or an unexpected file is proposed;
- montage, reference, event, rank, unit, timing, channel, or provenance state
  prevents safe implementation; or
- a structural or operation-specific verification check fails.

Handoff only after stopping:

- method questions to [eeg-analysis-guide](../eeg-analysis-guide/SKILL.md);
- task, marker, and timing questions to [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md);
- power questions to [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) or [statistical-power](../../skills/statistical-power/SKILL.md);
- inferential questions to [cogsci-statistics](../cogsci-statistics/SKILL.md);
- decoding or RSA to [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md);
- connectivity to [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md); and
- missing specialist methods, packages, or owners to an explicit capability
  gap or a verified canonical owner.

## Checks

The skill must:

- activate only for `mne-eeg-tool` or an exact approved handoff;
- stop without a completed specification, selected existing environment, or
  exact write and verification boundary;
- reject broad cleaning, analysis, full-pipeline, installation, source-script,
  background, network, and overwrite requests;
- distinguish BDF from EDF and BIDS from ordinary file loading;
- stop for missing events, montage, units, reference, line frequency,
  companion file, rank, or required optional package rather than inventing a
  fallback;
- preserve selected event, timing, channel, unit, rank, and source state;
- expose an approved code or command and full write set before Gate 2;
- execute only one operation after Gate 2 in an existing verified environment;
- detect output collision, source mutation, unexpected file, NaN or Inf,
  shape, channel, timing, event, or verification drift;
- report neutral structural facts without accepting QC or interpreting a
  result; and
- end with an uninvoked bounded handoff.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- AutoReject. (n.d.). *AutoReject* (Version 0.4.4) [Computer software]. https://autoreject.github.io/stable/
- MNE-BIDS. (n.d.). *mne_bids.read_raw_bids* (Version 0.19.0). https://mne.tools/mne-bids/stable/generated/mne_bids.read_raw_bids.html
- MNE-Connectivity. (n.d.). *mne_connectivity.spectral_connectivity_epochs* (Version 0.8.1). https://mne.tools/mne-connectivity/stable/generated/mne_connectivity.spectral_connectivity_epochs.html
- mne-microstates. (n.d.). *mne-microstates* (Version 0.3) [Computer software]. PyPI. https://pypi.org/project/mne-microstates/
- MNE-Python. (n.d.-a). *MNE-Python* (Version 1.12.1) [Computer software]. https://mne.tools/stable/
- MNE-Python. (n.d.-b). *mne.io.read_raw_bdf*. https://mne.tools/stable/generated/mne.io.read_raw_bdf.html
- MNE-Python. (n.d.-c). *mne.preprocessing.find_bad_channels_lof*. https://mne.tools/stable/generated/mne.preprocessing.find_bad_channels_lof.html
- MNE-Python. (n.d.-d). *mne.preprocessing.ICA*. https://mne.tools/stable/generated/mne.preprocessing.ICA.html
