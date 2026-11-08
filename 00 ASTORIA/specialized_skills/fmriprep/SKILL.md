---
name: fmriprep
description: >-
  Executes one already approved fMRI preprocessing specification through an
  available, version-pinned fMRIPrep environment and returns an exact command,
  runtime, derivative, report, and provenance record. Use when the request names
  this skill or a verified Active method or modality skill routes an exact
  fMRIPrep handoff. It makes the dataset scope, image or executable, mounts,
  resources, output spaces, fieldmap behavior, FreeSurfer state, TemplateFlow
  and network access, work and output directories, side effects, failure
  handling, and verification visible before execution. It does not choose
  preprocessing, denoising, filtering, QC thresholds, exclusions, output spaces,
  participants, or scientific interpretation; install software; silently resume,
  retry, repair, clean, overwrite, or chain into analysis. Triggers: preprocess
  my BIDS dataset with fMRIPrep, fmriprep command and outputs.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: fmri
  dependencies: ""
  requires: verified fMRIPrep executable or immutable container, BIDS dataset, FreeSurfer license when required by the selected route
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-11-01"
---

# fMRIPrep

Execute one approved participant-level fMRI preprocessing specification with
the exact fMRIPrep environment available for the selected project.

## Purpose

`fmriprep` owns:

- version and command-line preflight for one selected fMRIPrep execution;
- exact participant, session, task, echo, and processing-level scope;
- executable or container identity, mounts, resources, cache, license path,
  work directory, output directory, telemetry, and network behavior;
- translation of an approved specification into one inspectable command;
- one approved execution without silent retry, repair, cleanup, or expansion;
- structural verification of expected derivatives, logs, reports, and
  provenance;
- an fMRIPrep Run Record and a neutral QC handoff packet.

The user owns the preprocessing method, participant scope, anatomical-reference
strategy, distortion correction, slice-timing behavior, output spaces,
surface and CIFTI outputs, FreeSurfer use, processing level, exclusions,
resources, network access, telemetry, resume or rerun choice, QC criteria,
denoising, interpretation, and claims.

[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns the scientific and
analysis-compatibility specification. [fmri-coordinator](../fmri-coordinator/SKILL.md) owns checkpointed
functional-MRI routing. This adapter stops after execution verification and a
QC handoff.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `fMRI preprocessing`, `BOLD preprocessing`, `BIDS fMRI`,
`run a pipeline`, `motion correction`, `fieldmap`, `confounds`, `quality
control`, or another broad method or modality phrase.

Do not use this skill to:

- choose or revise a preprocessing method;
- choose confounds or a denoising strategy;
- decide whether a participant or run passes QC;
- install or upgrade fMRIPrep, Docker, Apptainer, FreeSurfer, TemplateFlow,
  BIDS Validator, or any package;
- convert data to BIDS;
- run downstream modeling, connectivity, decoding, statistics, or writing.

## Inputs

For an explicitly bounded writing-support consult, inspect the existing Run Record,
command/configuration, logs, citation boilerplate and reports for the named run
instead of entering an execution intake. Return exact version/image identity,
actual preprocessing choices and source locators, deviations, generated outputs
and missing facts through the existing research/analysis owner under
`00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`.
The shared translator and write-methods prepare prose; this adapter can check
technical fidelity to the actual run. Boilerplate alone does not prove a step
occurred. Do not supply remembered defaults, choose denoising, rerun processing
or label the data QC-accepted. The execution workflow below applies only when
execution is actually requested.

Obtain or mark missing:

- an approved fMRI Preprocessing and QC Specification;
- exact BIDS input root and its validation state;
- participant, session, task, echo, and run scope;
- approved anatomical-reference, fieldmap, slice-timing, output-space,
  surface, CIFTI, FreeSurfer, and processing-level choices;
- selected executable or container route, exact fMRIPrep version, and, for a
  container, immutable image identity or digest;
- exact command-line interface from that selected version;
- verified read-only input protection for the selected route and explicit
  work, output, cache, and FreeSurfer locations;
- output-collision, partial-run, reuse, resume, and overwrite policy;
- CPU, memory, threads, temporary storage, wall-time, and scheduler limits;
- the exact release and selected route's documented FreeSurfer license
  requirement and a readable path when required, without exposing license
  contents;
- TemplateFlow cache state, allowed network access, and telemetry choice;
- expected derivative classes, reports, logs, stop conditions, and structural
  acceptance checks;
- approval authority for the compute environment and destination.

If the preprocessing specification, exact version, input scope, side effects,
runtime authority, or output policy is unresolved, stop with **fMRIPrep
execution contract incomplete**.

## Steps

### 1. Confirm the method handoff

Verify that the incoming specification fixes, where applicable:

- input acquisition and metadata assumptions;
- anatomical-reference strategy;
- susceptibility-distortion route;
- slice-timing behavior and model-time reference;
- motion and coregistration requirements;
- volumetric and surface output spaces and resolutions;
- FreeSurfer, CIFTI, multi-echo, and processing-level behavior;
- outcome-blind QC criteria and downstream compatibility.

Do not infer a missing choice from fMRIPrep defaults or from whichever
container is available. Return unresolved scientific choices to
[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md).

### 2. Preflight the selected environment

Read only the bounded execution context and record:

- host, operating system, architecture, scheduler, and available resources;
- execution route and fMRIPrep version output;
- container tag and immutable digest, or executable path and environment;
- command help for that exact version;
- BIDS root, intended scope, validation record, and relevant metadata;
- input, output, work, cache, derivative-reuse, and FreeSurfer paths;
- existing contents, permissions, mount modes, free space, and collision risk;
- local TemplateFlow assets and whether a network request would occur;
- FreeSurfer license applicability for the exact selected route and
  availability of any required license path, without reading or displaying
  its contents;
- telemetry and any other external communication;
- unfinished work, prior configuration, logs, and version compatibility.

The current design authority reviewed fMRIPrep `25.2.5`. Every invocation
must still verify its exact installed or containerized version and use the
matching official documentation and command help.

### 3. Gate 1: approve the inspection and execution contract

Show an **fMRIPrep Execution Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| BIDS input and scope | | | | |
| Version and image or executable | | | | |
| Input and derivative mounts | | | | |
| Work, output, cache, and FreeSurfer paths | | | | |
| Processing and output options | | | | |
| Resources and scheduler | | | | |
| License, network, templates, and telemetry | | | | |
| Existing outputs and partial state | | | | |
| Expected artifacts and stop conditions | | | | |

Gate 1 authorizes only the displayed read-only inspection, validation review,
version and help checks, and command construction. It does not authorize
processing, downloads, template fetching, license registration, installation,
cleanup, output creation, resume, retry, or overwrite.

### 4. Available fMRIPrep execution forms

Use the selected fMRIPrep execution route for the approved specification.
Compare routes only if the user's approved scope leaves a material
environment or launcher choice open and multiple already available routes
can implement that same specification. The following forms may qualify.

1. an immutable fMRIPrep container with explicit read-only input and bounded
   writable mounts;
2. an existing site-managed or project-pinned fMRIPrep execution route;
3. an existing reviewed wrapper only when its emitted command and side effects
   remain fully visible.

For each form show version control, environment isolation, mount behavior,
resource control, reproducibility, visible output, benefit, tradeoff, and
limitation. These are execution forms, not alternative preprocessing methods.
Do not propose installation as an option.

### 5. Construct and audit the exact command

Build the command from the approved contract, then display:

- exact executable and environment or immutable container image and digest;
- input, output, work, cache, derivative, and FreeSurfer mounts as applicable
  to the route, including a license mount when required;
- participant, session, task, echo, and analysis-level scope;
- every nondefault flag and every intentionally accepted default;
- output spaces, processing level, surface or CIFTI behavior, and FreeSurfer
  behavior;
- BIDS validation behavior;
- resource, scheduler, network, and telemetry settings;
- destination and expected side effects;
- quoting, path, and permission checks;
- runtime log and provenance destinations;
- exact stop point.

Keep the BIDS source immutable. For a container, verify the immutable image
digest, matching command help, and a read-only BIDS input mount. For a native
route, verify the exact executable identity, environment, and matching
command help. Independently verify that the execution identity has read-only
access to the BIDS source, without attempting a source write.

As a local ASTORIA
execution-safety policy, keep work and output paths outside the source for
either route, even though BIDS permits a derivatives directory inside a
dataset. Review existing output and work state before execution.

### 6. Review defaults, version drift, and failure boundaries

Explicitly disclose:

- differences between the approved specification, candidate examples, the
  selected version's help, and current official documentation;
- version-sensitive defaults and experimental or deprecated options;
- adaptive behavior caused by available metadata;
- fieldmap association, output-space, FreeSurfer, TemplateFlow, and license
  assumptions;
- output and work-directory collision or reuse behavior;
- whether the command can contact a network or report usage;
- which reports and derivatives can be structurally verified;
- which image-quality judgments still require outcome-blind human review;
- what a successful process exit cannot establish;
- the exact conditions that stop rather than trigger a retry or repair.

fMRIPrep produces minimally processed derivatives and confound estimates. It
does not select a downstream denoising model, and this adapter never inserts
every confound column into an analysis.

### 7. Gate 2: approve one exact execution

Ask the user to approve:

- the complete command or scheduler submission;
- immutable image or executable identity;
- participant and file scope;
- mounts, writable paths, resources, and wall time;
- every flag and accepted default;
- license, template, network, and telemetry behavior;
- existing-output and partial-run policy;
- runtime and verification records;
- no-retry, no-repair, no-cleanup, no-overwrite, and no-chaining boundary.

Gate 2 authorizes only the displayed execution and verification. A canary,
participant subset, resumed run, full cohort, changed version, changed flag,
new output path, cleanup, or retry is a distinct action requiring its own
approval.

### 8. Run the approved fMRIPrep command once

Run only the approved command. Capture:

- exact command and scheduler submission;
- host and runtime environment;
- fMRIPrep version, container tag and digest or executable identity;
- command help or configuration state used to verify flags;
- input dataset identity, validation record, and selected scope;
- mount, resource, template, network, and telemetry state, plus the selected
  route's license requirement and any required license path;
- start and end time, exit status, stdout, stderr, warnings, and crash files;
- work and output paths and any pre-existing state;
- generated dataset description, logs, reports, derivative inventory, and
  hashes for the approved verification set;
- missing, partial, unexpected, or version-divergent outputs;
- any deviation from the approved command.

Do not rerun failed nodes, resume a work directory, change resources, delete
lock files, use `--clean-workdir`, weaken validation, ignore fieldmaps, alter
output spaces, or modify a license or cache without a new approved contract.

### 9. Verify and stop at the QC checkpoint

Separate:

1. **Execution verification:** exact version, process status, command
   conformance, logs, expected directory structure, reports, derivatives,
   sidecars, and provenance.
2. **Image-quality review packet:** locations of the subject reports and
   relevant reportlets, acquisition and processing context, missing panels,
   warnings, and the approved outcome-blind QC criteria.
3. **Scientific decision:** the user decides pass, fail, exclusion, remediation,
   denoising, and downstream use.

For a requested walkthrough of existing reports, the next review owner is
[review-fmriprep-qc](../review-fmriprep-qc/SKILL.md). Supply the report
locations and context above through the invoking companion or fMRI routing
handoff; do not begin review solely because this execution completed.

Return:

```text
fMRIPrep Run Record
Approved preprocessing specification:
Input dataset, validation state, and scope:
Version, image or executable, and command help:
Exact command and scheduler submission:
Mounts, work, output, cache, and FreeSurfer paths:
Resources and wall time:
Route-specific license requirement and applicable path, TemplateFlow, network, and telemetry state:
Existing-output and partial-run policy:
Exit state, stdout, stderr, warnings, and crash files:
Expected and observed derivatives:
Reports and QC handoff packet:
Command-conformance and structural-verification result:
Deviations, failures, and limitations:
Artifacts and hashes:
user-owned QC, denoising, interpretation, and next decision:
```

## Boundaries

- Stop if the BIDS input is writable, nested in the output, or not the
  approved dataset.
- Stop on an unavailable or mismatched fMRIPrep version, unverified command
  flag, mutable container identity, or undocumented wrapper behavior.
- Stop on an unresolved BIDS validation error or relevant acquisition
  metadata conflict.
- Stop if `--skip-bids-validation` lacks a current, scope-matched validation
  record, or if `--sloppy` is proposed for observed research data.
- Stop on an existing output, work, cache, derivative, or FreeSurfer state
  whose reuse policy is not approved.
- Stop before any required template fetch, network request, credential use,
  license registration, installation, or environment mutation that is not
  explicitly approved.
- Stop on missing storage, permissions, resources, or scheduler authority.
- Stop when the route's license requirement is unresolved or a required
  FreeSurfer license path is missing.
- Preserve partial output and logs after failure. Do not infer that a rerun is
  safe.
- `--clean-workdir`, file deletion, lock-file removal, and overwrite are
  destructive actions and never defaults.
- A zero exit status, expected file count, or complete HTML report does not
  establish acceptable image quality or scientific validity.
- Confound files are candidate nuisance variables, not an approved denoising
  specification.
- Do not interpret activation, connectivity, decoding, anatomy, artifacts, or
  group differences.

## fMRIPrep runs and derivative QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **fMRIPrep Execution Contract.** Audit version, command, mounts, defaults, adaptive metadata behavior, resources, network, reuse, and verification limits. This prevents silent command and environment choices. This requires detailed runtime inputs. Runtime and image-quality failures may still occur.
- **fMRIPrep Run Record and QC packet.** Execute one exact approved invocation once, preserve failures, verify structure, and stop at the QC handoff. This preserves authorization, provenance, and failure evidence. Any retry or remediation needs new approval. Structural verification cannot determine image quality.
- **Labeled container, site-managed, or reviewed-wrapper forms.** Compare only already available execution forms that implement the same approved preprocessing specification. This makes reproducibility and side effects visible without reopening method choice. This adds an execution-form review. This cannot resolve a missing preprocessing decision or runtime.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and batch-readiness comparison.** Run an approved canary participant or bounded subset before a separately approved batch. This can expose study-specific runtime and output problems early. This adds a consequential checkpoint and compute. A passing canary does not guarantee cohort-wide success.
- **Fixture execution plan.** Add an isolated synthetic or nonstudy fixture dry run where the selected environment supports it safely. This can reveal command, mount, and permission defects before study-data contact. This adds compute and fixture maintenance. This does not validate behavior on the study dataset.
- **Independent execution audit.** Add an independently reviewed command plus immutable container and template inventory. This improves detection of drift and hidden external access. This adds review and inventory work. Agreement does not establish preprocessing validity.

## Checks

- **Positive:** one participant with an approved preprocessing specification,
  immutable image, read-only input, empty output, and fixed command produces
  one Run Record and QC packet.
- **Negative:** `which preprocessing pipeline should I use?` returns to
  [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md).
- **Broad phrase:** `preprocess these BOLD data` does not trigger this adapter.
- **Version:** an image tag that resolves to an unrecorded digest stops before
  execution.
- **Input:** a writable BIDS mount or output nested under the input stops.
- **Metadata:** unresolved fieldmap association or slice-timing metadata stops
  rather than selecting a fallback.
- **Multi-echo:** two-echo input under the reviewed 25.2.x behavior stops
  rather than being silently adapted to a three-echo route.
- **Collision:** a nonempty output directory with no approved reuse policy
  stops.
- **Concurrency:** a work directory shared with another active fMRIPrep
  process stops.
- **Partial run:** a prior work directory is preserved and resume requires a
  new version and configuration compatibility review.
- **Offline:** a missing TemplateFlow asset on a network-disabled node stops
  without downloading.
- **License:** a missing required FreeSurfer license path stops without
  exposing or registering license content.
- **Failure:** a crash preserves logs and partial artifacts without retry,
  cleanup, flag changes, or participant expansion.
- **QC:** missing reportlets or warnings remain visible; a zero exit status is
  not labeled a QC pass.
- **Handoff:** requested report inspection has `review-fmriprep-qc` as its
  specific owner through the invoking companion or [fmri-coordinator](../fmri-coordinator/SKILL.md); method changes return to
  [fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md).

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *BIDS Specification* (Version 1.11.1). (n.d.). https://bids-specification.readthedocs.io/en/stable/
- *BIDS Specification: Derivatives: Imaging data* (Version 1.11.1). (n.d.). https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html
- *BIDS Specification: Magnetic resonance imaging* (Version 1.11.1). (n.d.). https://bids-specification.readthedocs.io/en/stable/modality-specific-files/magnetic-resonance-imaging-data.html
- Esteban et al. (2019). *Nature Methods*. https://doi.org/10.1038/s41592-018-0235-4
- NiPreps. (n.d.). *fMRIPrep outputs* (Version 25.2.5). https://fmriprep.org/en/25.2.5/outputs.html
- NiPreps. (n.d.). *fMRIPrep usage* (Version 25.2.5). https://fmriprep.org/en/25.2.5/usage.html
- NiPreps. (n.d.). *fMRIPrep workflows* (Version 25.2.5). https://fmriprep.org/en/25.2.5/workflows.html
