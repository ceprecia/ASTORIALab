---
name: fmri-coordinator
description: >-
  Routes one bounded functional-MRI task from its verified current state to one
  next approved method guide, QC checkpoint, software adapter, or export
  decision. Use when the request, or a part coordinator, hands over that exact
  modality-planning handoff. It distinguishes task, resting-state, connectivity,
  decoding, ROI, volume, surface, and existing-derivative paths; exposes
  acquisition, metadata, preprocessing, space, transform, denoising, model,
  provenance, and output gaps; and returns a checkpointed fMRI Route and Handoff
  Packet without choosing the scientific method or software, running a pipeline,
  loading every adapter, or treating one approval as authorization for the full
  workflow. Triggers: route my fmri task, next step for my fmri analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: fmri
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-11-01"
---

# fMRI Skill

Route one functional-MRI task to one next bounded owner. This is a modality
coordinator, not an fMRI method guide, software adapter, pipeline, or scientific
decision-maker.

## Purpose

`fmri-coordinator` owns:

- identifying the verified current fMRI workflow state and the one next
  consequential transition;
- distinguishing raw, organized, preprocessed, denoised, modeled,
  quality-controlled, and export-ready states;
- comparing applicable next-owner routes without loading the full modality
  catalog;
- enforcing separate preprocessing, QC, modeling, and export checkpoints;
- producing one user-selected fMRI Route and Handoff Packet.

The user owns the question, hypothesis, prediction, confirmatory status,
acquisition, preprocessing, QC, denoising, method, model, ROI, atlas, spaces,
thresholds, exclusions, software, export, interpretation, and claims.

[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns preprocessing, denoising,
filtering, detrending, and QC method specification.
[fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md) owns mass-univariate GLM specification.
`brain-connectivity-modeler` owns connectivity-method comparison.
`neural-decoding-analysis` owns predictive and representational method
comparison. A named software adapter owns only the approved implementation.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `fMRI`, `BOLD`, `functional connectivity`, `resting
state`, `task activation`, `PPI`, `DCM`, `ROI`, `MNI`, `fMRIPrep`, `CONN`,
`FSL`, or another broad modality, method, or software term.

Do not use this skill to:

- invent or reformulate a scientific question, contrast, ROI, or model;
- choose a preprocessing, denoising, connectivity, GLM, decoding, atlas,
  software, threshold, or export route automatically;
- convert DICOM, organize BIDS, preprocess, denoise, model, analyze, render,
  save, or export;
- install or invoke tools, containers, packages, plugins, services, licenses,
  credentials, or external compute;
- authorize an end-to-end pipeline from one confirmation;
- infer scientific meaning from a derivative, report, statistical map, or
  connectivity matrix.

## Inputs

For a bounded writing-support request about existing work, return the requested
facts from actual acquisition, method, processing and QC records through the
invoking owner. Read `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`.
This selects provenance inspection and technical fidelity review only, not the
route-comparison or execution workflow below. Locate the existing relevant
method/adapter/QC owner, preserve unknown fields and do not rerun processing to
fill prose. Report actual spaces, transformations, confounds, model inputs and
targets/comparisons with versions and source locators. Keep execution verification,
image review and user acceptance separate. A new method or analysis request
retains its normal owner and transitions.

For an explicit, bounded walkthrough of existing fMRIPrep reports, obtain
only the report location, processing version when available, and requested
participant/run/panel scope. Carry forward supplied project context; mark
unsettled methods or acceptance criteria as pending without blocking visual
observations. The user's request already selects the QC route and authorizes
that read-only walkthrough: skip the route-comparison menus and repeated
approvals in Gates 1 and 2, and return the selected handoff to the invoking
companion. User acceptance decisions and saving remain separate. A general
request about what to do next permits suggesting QC, not opening study images.

Obtain or mark missing:

- approved task and current inquiry part;
- question, estimand, confirmatory or exploratory status, and user-selected
  method specification when one already exists;
- source location, source type, immutable-input boundary, identifiers,
  checksums, privacy state, and provenance;
- raw DICOM, NIfTI, BIDS, existing derivative, report, model output, or export
  state;
- task, resting-state, multiecho, surface, volume, connectivity, decoding,
  ROI, or other bounded fMRI branch;
- participants, sessions, runs, tasks, events, contrasts, missing scans, and
  exclusion state;
- acquisition and sidecar metadata, including timing, echo, phase encoding,
  distortion inputs, and anatomical references as applicable;
- preprocessing, interpolation, output spaces, transforms, surfaces,
  denoising, filtering, smoothing, confounds, and QC already completed;
- exact prior tool, version, command or configuration, logs, reports,
  deviations, and failed or partial artifacts;
- proposed next output, acceptance criteria, destination, overwrite policy,
  compute, network, license, credential, and external-action boundary;
- Active method guide or software adapter available for the exact next step.

If the current source state, provenance, modality branch, method ownership,
previous checkpoint, or proposed next deliverable is unresolved, stop with
**fMRI route intake incomplete**.

## Steps

### 1. Build the fMRI Current-State Record

| Field | Record |
|---|---|
| user-owned target | Question, estimand, status, approved method choices |
| Current state | Raw, organized, preprocessed, QC reviewed, modeled, or export-ready |
| Source | Location, identifiers, checksums, privacy, immutable boundary |
| Acquisition | Runs, tasks, timing, echoes, phase encoding, fieldmaps, anatomy |
| Derivatives | Tool, version, configuration, spaces, transforms, confounds |
| Evidence | Logs, reports, visual QC, quantitative QC, deviations, failures |
| Next transition | Preprocessing, QC, modeling, or export |
| Candidate owner | One method guide or one implementation adapter per route |
| External boundary | Compute, network, credentials, license, writes, overwrite |
| Stop point | One selected handoff only |

An output filename is not evidence of how the file was produced.

### 2. Gate 1: approve the bounded route review

Show:

- the current-state record and every unresolved field;
- the one next transition under review;
- the applicable owner for the requested transition, eligible alternatives when
  ownership is unresolved, and any unsupported capability gap;
- exact documentation or metadata inspection needed;
- operations, adapters, data, and later parts excluded from this invocation.

Gate 1 authorizes only route comparison and read-only inspection of approved
metadata, provenance, logs, reports, and existing QC evidence. It does not
authorize data access beyond that boundary, conversion, preprocessing,
denoising, modeling, software execution, package or environment changes,
saving, export, or external actions.

### 3. Route the current fMRI checkpoint

Use the eligible owner for the requested transition. Compare owners only when the verified state leaves a material routing choice open.

Depending on the verified state, route cards may include:

- **Input and organization route:** conversion or BIDS organization is the
  next bounded owner when raw inputs and metadata are not yet suitable for a
  method or adapter.
- **Preprocessing-specification route:** the fMRI preprocessing guide is the
  next owner when acquisition-compatible preprocessing, denoising, filtering,
  spaces, or outcome-blind QC is not approved.
- **Preprocessing-implementation route:** one version-verified software
  adapter is the next owner only after a compatible method specification
  exists.
- **QC route:** existing fMRIPrep report/image walkthroughs and review
  documentation belong to [review-fmriprep-qc](../review-fmriprep-qc/SKILL.md).
  Visual observations can begin while acceptance rules are pending; adopting
  or revising those rules remains a method decision. Pass the derivative
  root/version, selected scope, intended analysis and existing resume point.
  A specific request to read reports resolves the owner without reopening
  the full preprocessing intake. Reports not yet available support preparation
  only. QC acceptance remains a separate decision before modeling.
- **Model-specification route:** one GLM, connectivity, decoding, or other
  method guide is the next owner when the scientific estimand is fixed but
  the model is not.
- **Model-implementation route:** one software adapter executes only an
  already approved method specification.
- **Export route:** one bounded packaging or visualization owner verifies
  provenance, space, units, labels, privacy, and destination after the
  scientific output is approved.

For every card state the eligibility evidence, missing inputs, exact owner,
input and output contract, approval required, verification, benefit,
tradeoff, limitation, and stop point. Do not select by software availability.

### 4. Document the fMRI Routing Decision Record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Eligible current state | Required inputs | Canonical owner | Output and verification | External boundary | Stop point | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- raw data, derivatives, and reports confused with one another;
- missing events or contrasts silently changing task fMRI into resting-state
  analysis;
- missing timing, echo, phase-encoding, readout, fieldmap, or anatomical
  metadata hidden by a software default;
- prior preprocessing applied again or an undocumented derivative treated as
  raw;
- native, anatomical, standard-volume, surface, and grayordinate spaces
  conflated;
- transform direction, interpolation history, reference image, atlas version,
  label table, or ROI independence left undefined;
- preprocessing success mistaken for QC acceptance;
- denoising or exclusion selected after viewing target outcomes;
- a GLM, connectivity, decoding, or ROI request routed directly to software
  before method specification;
- an inactive, missing, incompatible, or unverified adapter treated as
  available;
- one approval propagated across preprocessing, QC, modeling, and export;
- partial outputs, failed reports, version drift, destination collision,
  privacy, license, credential, or external-write risk hidden.

Stop when the next owner is not Active and verified, when a scientific choice
would be made for the user, or when the next step requires a new dependency,
package, plugin, service, credential, license, installation, or external
write that lacks separate approval.

### 5. Gate 2: The user selects one next handoff

Ask the user to select, revise, or reject one route and approve:

- the exact current state and next transition;
- one canonical next owner;
- bounded inputs, method specification, expected output, verification, and
  stop point;
- approved read, compute, network, credential, license, write, overwrite, and
  destination boundaries for the later owner.

Gate 2 authorizes only creation of the handoff packet. It does not invoke the
next owner or authorize any subsequent checkpoint. Do not infer selection
from silence.

### 6. Return the fMRI Route and Handoff Packet

Return:

```text
fMRI Route and Handoff Packet
Approved task and current inquiry part:
Question, estimand, and confirmatory status supplied by the user:
Verified current state and provenance:
Acquisition and metadata state:
Existing processing, spaces, transforms, confounds, and versions:
Completed QC evidence and unresolved failures:
Selected next transition:
Selected canonical owner:
Why this owner is eligible:
Bounded inputs:
Approved method specification:
Expected output and acceptance criteria:
Read, compute, network, credential, license, and write boundaries:
Explicitly excluded later steps:
Known limitations:
Required next checkpoint:
Stop conditions:
```

Stop after the packet. Invoke the named owner separately. After that owner
finishes, return to this coordinator only if another transition needs routing.

## Handoffs

- Route one transition per invocation. Preprocessing, QC, modeling, and export
  remain separate approval checkpoints.
- A BOLD series is an indirect hemodynamic measurement. The coordinator does not
  turn it into a neural or causal claim.
- Task fMRI requires its actual events, timing, contrasts, and design state.
  Missing task inputs do not justify silently switching to resting state.
- BIDS compliance, software completion, and the presence of derivative files
  are different claims.
- Inspect provenance and metadata rather than inferring processing, spaces, or
  units from filenames.
- Current fMRIPrep provides adaptive minimal preprocessing and confound
  estimates. It does not choose the scientifically appropriate denoising
  strategy.
- XCP-D is a separate postprocessing pipeline for resting-state or
  pseudo-resting-state functional connectivity. Do not route standard task
  GLMs, PPI, or beta-series work to it, and do not treat it as an integrated
  fMRIPrep step.
- Route preprocessing choices to [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) before
  a preprocessing adapter.
- Route a mass-univariate model to [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md), connectivity
  to `brain-connectivity-modeler`, and predictive or representational work to
  `neural-decoding-analysis` before implementation.
- QC acceptance precedes modeling. Target outcomes do not determine QC or
  exclusion rules.
- Use only the exact Active owner needed for the selected next step. Do not
  load or simulate a full modality catalog.
- A missing implementation owner remains an explicit capability gap.
- No route card, handoff, or successful run establishes a scientific
  conclusion.

## fMRI transition and handoff records

Use the records relevant to the verified state and the one requested transition. A routing record or handoff does not authorize the next operation.

- **fMRI Routing Decision Record.** Show provenance, state, ownership, eligibility, missing inputs, external boundaries, and stop points. This makes hidden handoff assumptions reviewable. This may stop at an unsupported gap. It cannot establish image or model quality.
- **Labeled fMRI route cards.** Compare only eligible owners for one next fMRI transition. This keeps the modality catalog selective and checkpointed. This requires a verified current state. This does not produce or analyze data.
- **Verified fMRI Route and Handoff Packet.** Produce one handoff packet and stop before invocation. This prevents one approval from authorizing a pipeline. This requires a new invocation for each transition. This does not execute the selected step.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended routing and compatibility audit.** Add independent provenance reconstruction and cross-adapter feasibility checks. This detects undocumented processing and version conflicts. This adds source inspection and adapter context. Feasibility does not validate the method.
- **Full checkpoint graph plus next-step cards.** Map the complete prospective workflow as a dependency graph while keeping every transition separately gated. This reveals downstream prerequisites early. This loads more catalog context and can imply a pipeline. The graph does not authorize any later step.

**Excluded handoff plus executed checkpoint.** Invoking the next owner automatically and returning after its verification is outside this coordinator’s authority. This reduces manual routing overhead. This creates automatic chaining and broader authority. Rejected for this coordinator.

## Checks

- **Positive:** a task-fMRI dataset with approved preprocessing but no model
  specification routes one next handoff to
  [fmri-glm-analysis-guide](../fmri-glm-analysis-guide/SKILL.md), not to a software command.
- **Negative:** `analyze this BOLD scan` does not trigger this skill.
- **Missing input:** absent task events are reported; the route does not
  become resting-state connectivity.
- **QC checkpoint:** completed preprocessing without reviewed reports stops
  before modeling.
- **QC owner:** a report-review request selects `review-fmriprep-qc`, not
  another preprocessing run; missing figure assets remain uninspected.
- **Space:** an ROI and BOLD derivative in undefined or incompatible spaces
  block extraction routing.
- **Ownership:** a connectivity question routes to
  `brain-connectivity-modeler`, not directly to CONN, FSL, or Nilearn.
- **Unsupported adapter:** a requested AFNI or XCP-D implementation remains a
  documented gap if no verified Active adapter owns it.
- **Authorization:** approval of preprocessing never authorizes QC, modeling,
  export, or saving.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *BIDS Specification: Magnetic resonance imaging* (Version 1.11.1). (n.d.). https://bids-specification.readthedocs.io/en/stable/modality-specific-files/magnetic-resonance-imaging-data.html
- Esteban et al. (2019). https://doi.org/10.1038/s41592-018-0235-4
- NiPreps. (n.d.). *fMRIPrep workflows* (Stable). https://fmriprep.org/en/stable/workflows.html
- Nichols et al. (2017). https://doi.org/10.1038/nn.4500
- Poldrack et al. (2008). *Guidelines for reporting an fMRI study*. https://doi.org/10.1016/j.neuroimage.2007.11.048
- XCP-D. (n.d.). *XCP-D documentation* (Stable). https://xcp-d.readthedocs.io/en/stable/
