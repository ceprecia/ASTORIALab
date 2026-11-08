---
name: qsiprep-tool
description: >-
  Executes one already approved participant-level QSIPrep preprocessing
  specification through an available, version-pinned environment and returns an
  exact command, runtime, derivative, gradient, report, provenance, and
  QC-handoff record. Use when the request names this skill or dwi-coordinator routes
  one exact QSIPrep handoff. It makes BIDS validity and compatibility,
  participant and session scope, scan grouping, gradients, phase-encoding
  metadata, output resolution, image identity, mounts, resources, TemplateFlow,
  network, telemetry, license state, work and output state, expected
  derivatives, and verification limits visible before execution. It does not
  choose preprocessing, install software, rewrite BIDS, silently fetch
  templates, resume, retry, clean, overwrite, accept QC, fit diffusion models,
  invoke QSIRecon, or chain downstream work. Triggers: run QSIPrep, qsiprep
  preprocessing.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: dwi
  dependencies: ""
  requires: verified QSIPrep executable or immutable container, BIDS dataset, FreeSurfer license when required by the selected route
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# QSIPrep Tool

Execute one approved diffusion-MRI preprocessing specification through the
exact QSIPrep environment available for the selected project.

## Purpose

`qsiprep-tool` owns:

- exact QSIPrep release, executable or container, digest, and command-line
  preflight;
- exact BIDS root, participant, session, run, and analysis-level scope;
- QSIPrep-specific BIDS and metadata compatibility inspection;
- DWI grouping, gradient, fieldmap-association, output-resolution,
  TemplateFlow, FreeSurfer-license, network, telemetry, resource, work, and
  output-state control;
- translation of an approved preprocessing specification into one
  inspectable participant-level command;
- one approved execution without silent retry, resume, repair, cleanup,
  overwrite, or participant expansion;
- structural verification of derivatives, corrected gradients, reports,
  quantitative QC, logs, and provenance;
- a QSIPrep Run Record and a neutral QC Handoff Packet.

The user owns the scientific question, acquisition suitability, preprocessing
method, scan grouping, output resolution, anatomical reference, denoising,
unringing, bias correction, b0 harmonization, head-motion model, distortion
correction, fieldmap and SyN use, resampling, participants, resources,
network access, telemetry, rerun or resume choice, QC criteria, exclusions,
reconstruction, interpretation, and claims.

[dwi-coordinator](../dwi-coordinator/SKILL.md) owns checkpointed diffusion-MRI routing. [bids](../bids/SKILL.md) owns BIDS
specification guidance; [bids-organizer](../bids-organizer/SKILL.md) owns an approved staged curation
operation; and [dcm2nii](../dcm2nii/SKILL.md) owns approved DICOM conversion. This adapter does
not curate the source, choose a diffusion method, fit a diffusion model,
perform tractography, or absorb QSIRecon.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `QSIPrep`, `diffusion preprocessing`, `DWI
preprocessing`, `BIDS diffusion`, `topup`, `eddy`, `motion correction`,
`distortion correction`, `gradient rotation`, `tractography`, `QSIRecon`,
`DIPY`, or another broad software, method, or modality phrase.

Do not use this skill to:

- decide which diffusion preprocessing pipeline or options to use;
- choose whether scans are merged, averaged, or processed separately;
- choose an output resolution from original voxel size or a downstream
  package recommendation;
- organize or rewrite BIDS metadata to satisfy QSIPrep;
- install, pull, build, update, or license QSIPrep, Docker, Apptainer,
  TemplateFlow, FreeSurfer, or another dependency;
- use `latest`, `unstable`, or a mutable image identity for observed research
  data;
- fit FA, MD, DKI, CSD, NODDI, tractography, tractometry, or connectomes;
- infer a QC pass from a command exit, report, or correction flag.

## Inputs

Obtain or mark missing:

- an approved DWI Preprocessing and QC Specification;
- exact BIDS input root, dataset identity, validation record, and write
  protection;
- participant, session, acquisition, direction, run, and DWI scope;
- DWI, bval, bvec, JSON, anatomical, fieldmap, and relevant table manifests
  with hashes and one-to-one associations;
- volume and gradient counts, gradient coordinate convention, finite state,
  shell structure, b0 definition, and acquisition provenance;
- `PhaseEncodingDirection`, valid effective-readout-time route,
  `IntendedFor`, `B0FieldIdentifier`, `B0FieldSource`, and `MultipartID`
  state;
- approved scan grouping and `--separate-all-dwis` behavior;
- approved output resolution and resampling implications;
- approved anatomical-reference, normalization, denoising, unringing, bias,
  b0-harmonization, head-motion, eddy, fieldmap, PEPOLAR, SyN, and
  distortion-group choices;
- selected executable or container route, exact QSIPrep version, and
  immutable image digest or executable identity;
- exact version-matched command help and official documentation;
- verified read-only input protection and explicit output, work,
  TemplateFlow, BIDS database, temporary, and required FreeSurfer license
  paths, with mounts specified where the selected route uses them;
- output collision, partial-run, reuse, resume, overwrite, and cleanup
  policy;
- CPU, memory, threads, GPU, temporary storage, wall time, scheduler, and
  job-isolation limits;
- TemplateFlow inventory, network boundary, telemetry choice, and license
  requirement for the exact selected route;
- expected derivative, gradient, report, QC, log, and provenance inventory;
- compute and destination authority.

If the preprocessing specification, grouping, metadata compatibility, output
resolution, exact version, input scope, side effects, runtime authority, or
QC plan is unresolved, stop with **QSIPrep execution contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm the method handoff

Verify that the incoming specification fixes, where applicable:

- acquisition and BIDS assumptions;
- DWI grouping and multipart behavior;
- anatomical-reference and dwi-only behavior;
- output resolution and resampling;
- denoising and unringing order;
- bias correction and b0 harmonization;
- head-motion and eddy configuration;
- susceptibility-distortion and fieldmap route;
- distortion-group merge behavior;
- output and reconstruction compatibility;
- outcome-blind QC criteria.

Do not infer a missing choice from QSIPrep defaults, a container example, or
the software already available. Return unresolved scientific choices to
[dwi-coordinator](../dwi-coordinator/SKILL.md) for method routing or a disclosed missing-owner decision.

### 2. Audit BIDS, acquisition, and gradients

QSIPrep requires a BIDS-valid input root. Validation is enabled by default.
Using `--skip-bids-validation` requires a current validation record for the
exact dataset state and processing scope.

Inspect:

- dataset and participant files plus selected DWI, bval, bvec, JSON,
  anatomical, and fieldmap files;
- equal DWI-volume, bval, and bvec counts;
- finite b-values and vectors, b0 classification, direction norms, and the
  approved gradient convention;
- JSON `PhaseEncodingDirection` and effective readout timing;
- fieldmap links and all related file identities;
- short reverse-PE series and whether QSIPrep expects them in `fmap` rather
  than `dwi`;
- `MultipartID` and the exact grouping QSIPrep would infer;
- session boundaries and effects of `--separate-all-dwis`;
- complex-data, magnitude, phase, and inherited-sidecar behavior;
- participant age and infant-route metadata when relevant.

Filename entities such as `dir-AP` or `dir-PA` do not replace JSON
`PhaseEncodingDirection`. Current BIDS `1.11.1` requires
`PhaseEncodingDirection` for EPI field-map files and requires an available
route to effective readout time.

QSIPrep `26.0.0` documents two current compatibility gaps: it does not
support BIDS-URI values for `IntendedFor`, and it does not support
`B0FieldIdentifier` or `B0FieldSource`. If the approved source uses only
those current BIDS forms, stop and expose the gap. Do not rewrite the dataset
or silently substitute relative paths.

### 3. Preflight the selected environment

Record:

- host, operating system, architecture, scheduler, and available resources;
- Docker, Apptainer, site-managed, or exact executable route;
- QSIPrep version output and exact command help;
- image registry, tag, immutable digest, build provenance, or executable
  environment;
- BIDS, output, work, TemplateFlow, database, temporary, and license paths;
- mount modes, permissions, free space, and collisions;
- local TemplateFlow inventory and whether missing assets would trigger
  network access;
- telemetry behavior and any other external communication;
- unfinished work, prior configuration, logs, and version compatibility.

The current official stable release reviewed for this design is QSIPrep
`26.0.0`, full commit
`4409bd9d111fc403880c01921c17190e4964c88f`, released 2026-04-20. Its current
container namespace is `pennlinc/qsiprep`, not the candidate's
`pennbbl/qsiprep`. Official installation guidance says not to use `latest`
or `unstable` except for limited testing. For an observed-data run, verify
the exact version's help and the selected route's identity. Record the
immutable digest for a container or the executable identity and environment
for an executable route.

TemplateFlow lazily retrieves missing assets. On an offline or
network-controlled node, verify a complete persistent `TEMPLATEFLOW_HOME`
accessible to the selected route. Bind it for a container or point the
native environment to the existing cache and verify access. Missing assets
stop without a fetch. QSIPrep usage reporting is enabled
unless `--notrack` is selected, so telemetry is a Gate 2 choice.

FreeSurfer license need is route and version specific. Verify the exact
selected workflow rather than requiring or omitting a license universally.
Do not read or display license contents.

Verify the selected QSIPrep environment before execution. For a container,
verify its supported runtime and immutable image. For an executable, verify
its identity and environment. Record any FreeSurfer license requirement for
that exact workflow and version. Missing software or images do not authorize
installation or retrieval.

### 4. Gate 1: approve inspection and the execution contract

Show a **QSIPrep Execution Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| BIDS input, validation, and scope | | | | |
| DWI, metadata, fieldmaps, and gradients | | | | |
| Grouping and preprocessing specification | | | | |
| Version, exact help, and executable identity or image digest | | | | |
| Input, output, work, cache, and applicable license paths and mounts | | | | |
| Output resolution and accepted defaults | | | | |
| Resources, scheduler, network, and telemetry | | | | |
| Existing outputs, work, and partial state | | | | |
| Expected derivatives, gradients, reports, and QC | | | | |
| Failure, stop, and downstream boundaries | | | | |

Gate 1 authorizes only the displayed bounded read-only dataset, validation,
metadata, gradient, grouping, version, image, help, resource, cache,
collision, and destination inspection plus command construction. It does not
authorize processing, downloads, image pulls, template fetching,
installation, directory creation, BIDS mutation, license registration,
cleanup, resume, retry, or overwrite.

### 5. Execution forms for the approved preprocessing

Use the selected QSIPrep execution form for the approved preprocessing
specification. Compare forms only when a material execution choice remains
open under the user's approval and multiple already available forms
implement that same specification. The following forms may qualify.

1. an immutable `pennlinc/qsiprep` container with explicit read-only input
   and bounded writable mounts;
2. an existing site-managed or project-pinned QSIPrep environment;
3. an existing reviewed scheduler wrapper only when its emitted command and
   side effects remain fully visible.

For each form show version and digest control, environment isolation, mount
behavior, resource and scheduler control, TemplateFlow and network behavior,
reproducibility, visible output, benefit, tradeoff, and limitation. These are
execution forms, not alternative preprocessing methods, resolutions, or
grouping designs. If only one form is verified, show that fixed route and
its limitation. Do not propose installation.

### 6. Construct and audit the exact command

Build the command from the approved contract, then display:

- exact executable identity and environment or immutable container image
  and digest, with matching command help for the selected route;
- BIDS input protection and output, work, TemplateFlow, database, temporary,
  and required license paths, with mount modes where applicable;
- participant, session, filter, and `participant` analysis-level scope;
- explicit `--output-resolution`;
- grouping, denoising, unringing, bias, b0, head-motion, eddy, PEPOLAR,
  fieldmap, SyN, anatomical, and distortion-group options;
- every nondefault flag and every intentionally accepted default;
- validation behavior;
- CPU, memory, thread, GPU, scheduler, network, and telemetry settings;
- destination, expected side effects, and collision behavior;
- command, runtime log, crash, and provenance destinations;
- exact stop point.

For current `26.0.0`, `--output-resolution` is mandatory and controls
resampling or upsampling. Its official parser accepts `--mem` and
`--mem-mb` as aliases for the same `MEMORY_MB` destination. Record the exact
alias used and preserve its megabyte semantics. Verify exact flags against
`--help` from the selected executable or immutable container image.

Keep the BIDS source immutable. For a container, verify the image digest and
a read-only input mount. For a native route, independently verify that the
exact executable's execution identity has read-only access to the BIDS
source, without attempting a source write. Keep output and work separate
from the source for either route.
Do not run `mkdir`, pull an image, populate TemplateFlow, or create a BIDS
database unless the displayed Gate 2 explicitly includes that bounded write.

### 7. Review adaptive behavior and verification limits

Explicitly disclose:

- differences among the approved specification, candidate examples, exact
  command help, and current official documentation;
- the mandatory output resolution and interpolation implications;
- how `MultipartID`, session boundaries, phase-encoding groups, and
  `--separate-all-dwis` determine grouping;
- denoising-before-or-after-combining assumptions;
- b0 harmonization and distortion-group behavior;
- metadata-driven fieldmap and anatomical adaptation;
- current BIDS-URI and B0-field compatibility gaps;
- executable identity or image tag and immutable digest, external assets,
  applicable license state, network, and telemetry;
- output, work, database, cache, and partial-run reuse behavior;
- resource estimates as project-specific planning evidence, not promises;
- expected outputs according to the exact selected version;
- which command and artifact properties can be verified mechanically;
- which motion, distortion, registration, signal, gradient, and anatomical
  judgments require human review;
- what a zero exit status or complete HTML report cannot establish.

Preprocessing corrections and rotated gradients do not prove image quality.
Quantitative QC supports comparison but does not choose pass thresholds,
exclusions, or downstream use.

### 8. Gate 2: approve one exact execution

Ask the user to approve:

- one complete command or scheduler submission;
- one immutable image or exact executable identity;
- one participant, session, and file scope;
- all mounts, writable paths, resources, flags, and accepted defaults;
- grouping, output resolution, preprocessing, and distortion choices;
- validation, network, telemetry, templates, and license behavior;
- existing-output, work, database, cache, and partial-state policy;
- runtime and verification records;
- no-retry, no-resume, no-cleanup, no-overwrite, no-QSIRecon, and
  no-downstream-chain boundary.

Gate 2 authorizes only the displayed execution and verification. A canary,
additional participant, batch, changed image, changed flag, new output path,
template fetch, BIDS edit, cleanup, resume, or retry is a distinct action
requiring its own approval.

### 9. Run one approved QSIPrep invocation

Run only the approved command. Capture:

- exact command and scheduler submission;
- host and runtime environment;
- QSIPrep version, container tag and digest or executable identity;
- exact command help and documentation state used to verify flags;
- input dataset identity, validation record, and selected scope;
- DWI, gradient, metadata, fieldmap, grouping, and preprocessing manifest;
- mount, resource, TemplateFlow, network, and telemetry state, plus the
  selected route's license requirement and any required license path;
- start and end time, exit status, stdout, stderr, warnings, and crash files;
- work, output, database, and cache paths plus pre-existing state;
- generated dataset description, logs, reports, derivative inventory,
  corrected-gradient inventory, quantitative QC, and selected hashes;
- missing, partial, unexpected, or version-divergent outputs;
- any deviation from the approved command.

Do not retry failed nodes, resume a work directory, change resources, weaken
validation, ignore fieldmaps, alter grouping or output resolution, fetch a
template, delete a lock or work item, clean, or modify a license or cache
without a new approved contract.

### 10. Verify and stop at the QC checkpoint

Verify according to the exact selected version. For reviewed `26.0.0`,
expected evidence can include:

- subject summary report at
  `<output_dir>/qsiprep/sub-<label>.html`;
- ACPC-space preprocessed DWI, reference, and mask;
- corrected FSL-style bval and bvec files;
- separate MRtrix `.b` gradient table;
- confound, image-QC, motion, and model-quality tables;
- anatomical derivatives and transforms when the selected route produces
  them;
- dataset description, logs, warnings, crashes, and provenance.

Pair every DWI with the corrected gradients from the same exact run and
source identity. QSIPrep documents that its FSL-style bval and bvec outputs
are not the direct MRtrix import route; use the separate `.b` table for an
approved MRtrix handoff.

Separate:

1. **Execution conformance:** exact executable identity and environment or
   immutable image and digest, matching command help, command, scope, input
   protection, applicable mounts, resources, network behavior, process
   status, logs, and deviations.
2. **Structural and gradient verification:** expected directory structure,
   DWI identity, dimensions, geometry, finite state, volume and gradient
   counts, corrected gradient pairing, reports, and provenance.
3. **Human QC packet:** report locations, q-space and gradient evidence,
   motion, distortion, registration, masks, quantitative QC, warnings, and
   the approved outcome-blind criteria.
4. **Scientific decision:** the user decides pass, fail, exclusion, remediation,
   rerun, reconstruction, downstream use, interpretation, and claims.

Do not calculate FA or MD as a verification step. That is diffusion-model
fitting. QSIRecon, DIPY, MRtrix, tractography, tractometry, and connectivity
are separate capabilities or disclosed capability gaps.

Return:

```text
QSIPrep Run Record
Approved DWI preprocessing specification:
BIDS dataset, validation state, and scope:
DWI, metadata, fieldmap, and gradient manifest:
Grouping, output resolution, and accepted defaults:
Version, exact help, and executable identity or immutable image digest:
Exact command and scheduler submission:
Mounts, work, output, database, cache, and applicable license paths:
Resources and wall time:
TemplateFlow, network, and telemetry state:
Existing-output and partial-run policy:
Exit state, stdout, stderr, warnings, and crash files:
Expected and observed derivatives:
Corrected-gradient pairing and format inventory:
Reports, quantitative QC, and human QC packet:
Command-conformance and structural-verification result:
Deviations, failures, limitations, artifacts, and hashes:
user-owned QC, rerun, reconstruction, interpretation, and next decision:
```

## Boundaries

- Stop if the input is not a BIDS-valid root, is writable, is nested in the
  output, or is not the approved dataset.
- Stop if `--skip-bids-validation` lacks a current, scope-matched validation
  record.
- Stop on DWI, bval, bvec, JSON, anatomy, or fieldmap identity and count
  mismatches.
- Stop when filename direction conflicts with JSON metadata; JSON is the
  acquisition authority and the conflict remains visible.
- Stop on missing phase-encoding or effective-readout evidence required for
  the approved distortion route.
- Stop on a current BIDS-URI-only `IntendedFor` or
  `B0FieldIdentifier`-only association that selected QSIPrep does not
  support.
- Stop on unresolved `MultipartID`, grouping, merge, denoising-order,
  b0-harmonization, output-resolution, fieldmap, anatomical, or HMC choices.
- Stop when the container namespace conflicts with the exact selected
  release. For `26.0.0`, require `pennlinc/qsiprep`; older official releases
  may require their historically valid namespace after exact-version review.
- For a container route, stop on `latest`, `unstable`, an unresolved tag,
  a mutable image identity, or a digest mismatch.
- Stop when a proposed flag is absent from the exact version's `--help`.
- Stop if required TemplateFlow assets are missing under a network-disabled
  contract. Do not fetch them.
- Stop on unapproved network, telemetry, license, credential, database, or
  cache behavior.
- Stop on a writable input, output nested under input, nonempty destination,
  active shared work directory, or unexplained partial state.
- Stop if `--sloppy` is proposed for observed research data.
- Preserve failures, warnings, logs, crash files, and partial outputs without
  retry, resume, cleanup, or altered flags.
- A correction flag, zero exit status, expected file count, or complete HTML
  report does not prove correction quality or QC acceptance.
- Never invoke QSIRecon, DIPY, MRtrix, tractography, diffusion-model fitting,
  export, or interpretation automatically.

## QSIPrep run and gradient QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled immutable-container, site-managed, or reviewed-wrapper forms.** Compare only already available execution forms that implement the same approved preprocessing specification. This makes reproducibility, mounts, network behavior, and side effects visible without reopening method choice. This adds execution-form review. This cannot resolve a missing preprocessing or grouping decision.
- **QSIPrep Execution Contract.** Audit BIDS and gradient state, grouping, exact CLI, digest, defaults, resources, templates, network, telemetry, collisions, outputs, and QC limits. This prevents hidden metadata, grouping, resolution, and environment choices. This requires detailed data and runtime evidence. Runtime and image-quality failures may still occur.
- **QSIPrep Run Record and QC Handoff Packet.** Execute one exact approved invocation once, preserve failures, verify structures and corrected gradients, and stop at QC. This preserves authorization, provenance, and gradient identity. Any retry or remediation needs new approval. Structural verification cannot determine image quality.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and batch-readiness comparison.** Run one approved canary, then require a new Gate 2 for any enumerated participant batch. This can expose study-specific runtime and output problems before larger writes. This adds a consequential checkpoint and compute. A passing canary does not authorize or guarantee a batch.
- **Fixture or canary execution plan.** Add a separately approved synthetic fixture or canary-participant plan before a larger run. This can reveal command, metadata, mount, and output defects earlier. This adds compute and fixture or canary maintenance. This does not establish study-data quality or cohort-wide success.
- **Independent execution audit.** Add independent command review plus immutable image, TemplateFlow, and expected-output manifests. This improves detection of drift and hidden external access. This adds review and inventory work. Agreement does not establish preprocessing validity.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *BIDS specification* (Version 1.11.1). (n.d.). https://bids-specification.readthedocs.io/en/stable/
- PennLINC. (n.d.). *Usage*. QSIPrep documentation. https://qsiprep.readthedocs.io/en/stable/usage.html
- PennLINC. (2026, April 20). *QSIPrep* (Version 26.0.0) [Computer software]. GitHub. https://github.com/PennLINC/qsiprep/releases/tag/26.0.0
- [TemplateFlow Python client]. (n.d.). TemplateFlow. https://www.templateflow.org/usage/client/
