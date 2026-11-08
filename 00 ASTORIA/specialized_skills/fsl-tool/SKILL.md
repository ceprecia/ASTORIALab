---
name: fsl-tool
description: >-
  Executes one already approved FSL software operation through an available,
  release-and-subtool-verified environment and returns an exact command, input,
  configuration, runtime, output, log, QC-handoff, and provenance record. Use
  when the request names this skill or a verified Active method or modality
  skill routes one exact FSL handoff. It makes the selected FSL program, release
  and package build, inputs, image geometry, configuration files, references,
  resources, environment, license context, outputs, overwrites, side effects,
  failure policy, and verification visible before execution. It does not choose
  an imaging method, pipeline, registration, segmentation, model, threshold,
  atlas, denoising strategy, tractography route, or interpretation; install
  software; silently chain commands, repair, retry, clobber, or accept QC.
  Triggers: run this in FSL, FSL command for this step.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: multimodal
  dependencies: ""
  requires: FSL
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# FSL Tool

Execute one approved FSL operation with the exact subtool and software state
available for the selected research project.

## Purpose

`fsl-tool` owns:

- release, package-build, subtool, command-help, environment, and license-use
  preflight;
- translation of one approved imaging operation into one inspectable FSL
  command or one inseparable same-step invocation;
- explicit inputs, image geometry, configurations, references, resources,
  outputs, and side effects;
- one approved execution without automatic pipeline chaining, repair, retry,
  or clobber;
- structural output verification and an operation-specific QC handoff;
- an FSL Operation Record.

The user owns the scientific question, modality, method, subtool, model, design,
registration direction and degrees of freedom, segmentation target, masks,
references, interpolation, thresholds, fieldmap route, diffusion model,
tractography, atlas, QC criteria, exclusions, interpretation, and claims.

[smri-coordinator](../smri-coordinator/SKILL.md), [fmri-coordinator](../fmri-coordinator/SKILL.md), and [dwi-coordinator](../dwi-coordinator/SKILL.md) own modality routing.
Method guides own the scientific specification. A specialized adapter such as
[fmriprep](../fmriprep/SKILL.md) or [freesurfer-tool](../freesurfer-tool/SKILL.md) keeps its own execution when already
selected. This adapter does not absorb a full modality pipeline.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `FSL`, `BET`, `FAST`, `FLIRT`, `FNIRT`, `FEAT`, `MELODIC`,
`TOPUP`, `eddy`, `DTIFIT`, `bedpostx`, `probtrackx`, `XTRACT`, `registration`,
`segmentation`, `fMRI`, `DWI`, or another broad software, method, or modality
term.

Do not use this skill to:

- select among FSL programs or imaging methods;
- assemble an anatomical, functional, diffusion, or multimodal pipeline;
- install, upgrade, modify, or license FSL;
- create scientific configuration values from defaults or observed outcomes;
- run clinical or diagnostic interpretation;
- chain outputs into statistics, writing, or another adapter automatically.

## Inputs

Obtain or mark missing:

- an approved method and FSL Implementation Specification;
- one exact FSL subtool and bounded operation;
- input files, hashes, modality, dimensions, voxel sizes, orientations, units,
  coordinate spaces, and immutable source state;
- masks, transforms, matrices, gradients, b-values, timing, acquisition
  parameters, design files, training data, atlases, standard images, and
  configuration files required by that operation;
- exact FSL release, component-package builds, binary or wrapper path,
  architecture, operating system, and installed command help;
- `FSLDIR`, environment initialization, standard-data identity, locale,
  threading, scheduler, GPU or CUDA state where relevant;
- noncommercial or separately authorized license context;
- exact command, accepted defaults, resources, random state where applicable,
  and expected runtime stop point;
- output destinations, filename and collision rules, implicit outputs,
  overwrite behavior, temporary files, and rollback policy;
- operation-specific structural checks and outcome-blind QC criteria;
- compute and destination authority.

If the method, subtool, geometry, configuration, version, component build,
license context, side effects, or QC specification is unresolved, stop with
**FSL operation contract incomplete**.

## Steps

### 1. Confirm one method-to-software handoff

Name:

- scientific operation already selected;
- exact FSL program;
- input and output grain;
- fixed parameters and configurations;
- expected artifacts;
- one stop point before the next scientific transition.

Examples of separate transitions include field estimation, distortion
correction, registration, segmentation, model fitting, ICA, tensor fitting,
and tractography. Do not treat their coexistence in FSL as authorization to
chain them.

### 2. Preflight the exact FSL state

Read only the bounded environment and record:

- `fslversion`, `FSLDIR`, executable and wrapper paths;
- FSL release plus component package or binary build relevant to the selected
  subtool;
- architecture, operating system, environment initialization, and standard
  data;
- installed `--help` or usage output for the exact command;
- license-use context and any commercial-use restriction;
- input and configuration hashes, image headers, dimensions, voxel sizes,
  orientation, units, spaces, and mutual alignment needed for the operation;
- referenced templates, masks, matrices, warps, gradients, acquisition files,
  design files, and training data;
- output and temporary paths, permissions, free space, collisions, and
  implicit write behavior;
- CPU, memory, threads, GPU, CUDA, scheduler, and wall-time state;
- prior outputs, logs, partial state, and concurrent writers.

Current official review found FSL `6.0.7.22` current on 2026-07-23. The participant's installed release and modifications are verified independently. A mismatch does not authorize updating or substituting a release. Every invocation
rechecks the exact release, component package, command help, and environment.

### 3. Gate 1: approve inspection and the operation contract

Show an **FSL Operation Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| Method and FSL subtool | | | | |
| Inputs, geometry, and spaces | | | | |
| Configurations and references | | | | |
| Release, package build, and command help | | | | |
| FSLDIR, environment, and standard data | | | | |
| License-use context | | | | |
| Resources and scheduler | | | | |
| Outputs, collisions, and implicit writes | | | | |
| Structural checks and QC handoff | | | | |
| Failure and rollback boundary | | | | |

Gate 1 authorizes only the displayed read-only inspection, header and
configuration review, version and help checks, and command construction. It
does not authorize processing, installation, updates, downloads, license
changes, configuration changes, clobbering, or output creation.

### 4. Available FSL execution forms

Use the selected FSL environment for the approved operation. Compare forms
only if the user's approved scope leaves a material execution choice open
and more than one already available form can perform that same operation.
The following forms may qualify.

1. the selected installed FSL environment;
2. an immutable existing FSL container;
3. an existing site-managed module or scheduler route.

For each show release and package-build control, environment isolation,
standard-data identity, CPU or GPU behavior, write surface, reproducibility,
visible output, benefit, tradeoff, and limitation. These are execution forms,
not alternative programs or methods. Do not propose installation.

### 5. Construct and audit the exact command

Display:

- environment initialization and executable identity;
- complete command with shell-safe quoting;
- every input, mask, transform, design, configuration, reference, gradient,
  timing, and training-data argument;
- every parameter and intentionally accepted default;
- coordinate-space direction, interpolation, units, and output geometry where
  relevant;
- CPU, memory, thread, GPU, CUDA, scheduler, and wall-time settings;
- explicit and implicit output paths and files that may be replaced;
- logging, temporary-state, completion, and stop point;
- no-clobber and no-chain boundary.

Never insert candidate constants such as BET `-f 0.5`, FLIRT 12 degrees of
freedom, MELODIC dimension 30, FIX threshold 20, three bedpostx fibers, or
fixed TOPUP and EDDY files unless they are in the approved specification.
Never add `--clobber`.

Reject the candidate's unsafe or stale command patterns. In particular:

- do not use a brain-extracted moving image for FNIRT when the approved route
  and current official guidance require non-brain-extracted inputs;
- do not use the candidate's incomplete low-level `first` syntax, and audit
  either an approved `run_first_all` invocation or every required low-level
  argument against live help;
- do not pass a legacy FIX `.RData` classifier to current pyFIX without an
  approved and verified conversion route;
- after EDDY, require its `.eddy_rotated_bvecs` output for approved downstream
  diffusion fitting rather than silently reusing the original b-vectors;
- require the approved XTRACT species argument and stop on local versions
  affected by a relevant native-space target-ordering defect;
- treat a FEAT design as an inspectable method artifact, and surface its
  output-directory collision behavior before execution.

When official prose and installed help disagree, preserve the conflict and use
the exact installed help as command-syntax authority for that invocation. Do
not assume a cross-version `fsl_anat` bias-correction default; verify it against the exact installed help.

### 6. Review tool assumptions and verification limits

Show:

- differences among the approved specification, candidate example, installed
  help, and current official documentation;
- release and component-package drift;
- input-format, header, orientation, geometry, unit, space, and transform
  assumptions;
- command defaults, experimental behavior, training-data dependence, and
  version-sensitive output;
- registration, segmentation, model, ICA, diffusion, and tractography
  assumptions relevant to the selected subtool;
- output collisions, partial state, randomness, parallelism, and GPU
  differences;
- which files and numerical invariants can be structurally verified;
- which overlays, residuals, masks, surfaces, registrations, segmentations,
  outliers, gradients, and model results require operation-specific QC;
- what successful execution, finite values, or plausible numerical bounds
  cannot establish.

Do not infer method validity because FSL provides a command. Do not infer
brain-extraction quality, registration accuracy, segmentation validity,
diffusion validity, or scientific meaning from file existence.

### 7. Gate 2: approve one exact FSL operation

Ask the user to approve:

- release, component build, environment, and exact command;
- input and configuration identities;
- parameters, accepted defaults, resources, and scheduler;
- license-use context;
- output paths, implicit writes, collision policy, and rollback boundary;
- structural checks, QC packet, and stop point;
- no-install, no-update, no-download, no-clobber, no-repair, no-retry,
  no-program-change, and no-chaining boundary.

Gate 2 authorizes only the displayed operation and verification. A second FSL
program, changed parameter, retry, GPU substitution, new participant, expanded
batch, overwrite, or downstream transition requires a new approval.

### 8. Run one approved FSL operation

Run only the approved command. Capture:

- exact environment setup, command, and scheduler submission;
- FSL release, component package or binary build, executable path, operating
  system, architecture, and container digest where used;
- input, configuration, template, standard-data, mask, transform, design,
  gradient, timing, and training-data hashes;
- image geometry and space record;
- resources, runtime, exit status, stdout, stderr, warnings, logs, and failure
  files;
- explicit and implicit created or changed outputs;
- random, thread, GPU, and CUDA state where applicable;
- deviations from the approved contract.

On failure or partial output, stop and preserve evidence. Do not change the
tool, parameter, mask, transform, reference, thread count, GPU route,
configuration, or output path; clobber; repair; retry; or continue a pipeline
without a new approval.

### 9. Verify and stop at the QC handoff

Separate:

1. **Execution verification:** command conformance, release and package state,
   process status, logs, expected outputs, geometry, metadata, and provenance.
2. **Operation-specific QC packet:** selected overlays, residuals, masks,
   transformations, segmentations, reports, outlier summaries, gradients, or
   diagnostics required by the approved method.
3. **Scientific decision:** the user decides QC acceptance, remediation,
   exclusion, next operation, interpretation, and claims.

Return:

```text
FSL Operation Record
Approved method and subtool:
Inputs, geometry, spaces, and hashes:
Configurations, references, and training data:
Release, package build, executable, and command help:
FSLDIR, environment, standard data, and license context:
Exact command and scheduler submission:
Resources, threads, GPU, and random state:
Outputs, implicit writes, and collision policy:
Exit state, stdout, stderr, logs, warnings, and failures:
Structural-verification result:
Operation-specific QC handoff:
Deviations and limitations:
Artifacts and hashes:
user-owned QC, remediation, next operation, and interpretation:
```

## Boundaries

- Stop if the method or program is selected only because FSL is available.
- Stop on a release, component-build, executable, wrapper, help, `FSLDIR`,
  standard-data, or license-context mismatch.
- Stop on unresolved image geometry, orientation, units, coordinate space,
  transform direction, gradient, timing, mask, design, reference, or training
  data.
- Stop on unapproved defaults, implicit writes, nonempty outputs, concurrent
  writers, insufficient resources, or ambiguous rollback.
- Stop if an approved post-EDDY operation points to original rather than
  rotated b-vectors.
- Stop an XTRACT operation when species is unspecified or the installed
  release lacks a relevant correction required by the approved output space.
- Stop before any install, update, package change, download, commercial use
  without authorization, credential use, environment mutation, or external
  write not in the contract.
- Never use `fsl_anat --clobber` or another overwrite option by default.
- Never turn a warning, failed check, outlier, registration mismatch, or
  implausible map into an automatic parameter change.
- Never treat finite values or fixed FA, MD, thickness, probability, or
  registration ranges as universal QC acceptance.
- Never transform a file header or orientation as a repair without a separate
  method and provenance decision.
- A completed FSL command does not establish a valid method, accurate anatomy,
  causal effect, tract, or scientific conclusion.

## FSL operation evidence and QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **FSL Operation Contract.** Audit release, package build, geometry, spaces, configurations, defaults, resources, writes, and QC limits. This prevents silent tool and parameter assumptions. This requires detailed implementation inputs. Runtime and operation-specific QC failures may remain.
- **FSL Operation Record and QC packet.** Execute one approved operation once, preserve failure evidence, verify structure, and stop at QC. This preserves exact authorization and provenance. Any repair or next command needs new approval. Structural checks cannot accept the result.
- **Labeled installed, container, or site-managed forms.** Compare only already available execution forms for the same approved FSL operation. This makes package, environment, and write differences visible without reopening method choice. This adds an execution-form review. This cannot resolve a missing method, tool, or runtime.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and batch-readiness comparison.** Run one approved canary input before a separately approved batch. This can expose version, resource, and output issues early. This adds a consequential checkpoint and compute. A passing canary does not guarantee batch-wide quality.
- **Fixture execution plan.** Add an isolated synthetic or nonstudy fixture for the exact subtool. This can expose command, geometry, and output defects before observed-data contact. This adds fixture and compute work. This does not validate the study method or images.
- **Independent implementation audit.** Add independent command review and a before-state output manifest. This improves detection of drift and unintended writes. This adds review and storage. Agreement does not establish scientific validity.

## Checks

- **Positive:** one approved FLIRT operation with fixed images, transform
  direction, degrees of freedom, reference, interpolation, version, command,
  and empty output produces one FSL Operation Record and QC packet.
- **Negative:** `which registration method should I use?` routes to the
  relevant method or modality owner.
- **Broad phrase:** `use FSL` does not trigger this adapter.
- **Pipeline:** `preprocess all my fMRI` routes through [fmri-coordinator](../fmri-coordinator/SKILL.md) rather
  than expanding into BET, MCFLIRT, FEAT, and MELODIC.
- **Structural:** a broad `fsl_anat` request returns to [smri-coordinator](../smri-coordinator/SKILL.md) until
  its method and outputs are fixed.
- **Diffusion:** TOPUP and EDDY remain separate approved transitions through
  [dwi-coordinator](../dwi-coordinator/SKILL.md).
- **Version:** an installed older or locally modified release is not silently
  updated to a newer release.
- **License:** unclear commercial use stops for license authorization.
- **Geometry:** mismatched dimensions or an ambiguous transform direction
  stops before execution.
- **Collision:** candidate `fsl_anat --clobber` is rejected for a nonempty
  destination.
- **Configuration:** fixed BET, MELODIC, FIX, or bedpostx values are not
  inherited from the candidate.
- **FNIRT:** candidate use of a brain-extracted moving image is rejected when
  it conflicts with the approved route and current official guidance.
- **FIRST:** the candidate's incomplete low-level command is rejected before
  execution.
- **FIX:** a legacy `.RData` classifier is not passed directly to current
  pyFIX.
- **EDDY:** an approved downstream tensor fit using original b-vectors is
  blocked in favor of the verified `.eddy_rotated_bvecs` artifact.
- **XTRACT:** a missing species argument or a local release predating a
  required native-space target-ordering correction stops.
- **FEAT:** an existing output directory exposes suffixing or partial-write
  behavior before approval.
- **Failure:** partial output is preserved without changing the command,
  clobbering, retrying, or continuing to the next FSL program.
- **QC:** file existence, finite values, or bounded tensor metrics do not
  produce a QC pass.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- FSL. (n.d.-a). *Diffusion tools*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/index.html
- FSL. (n.d.-b). *EDDY*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/eddy/index.html
- FSL. (n.d.-c). *EDDY QC*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/eddyqc.html
- FSL. (n.d.-d). *FEAT*. https://fsl.fmrib.ox.ac.uk/fsl/docs/task_fmri/feat/index.html
- FSL. (n.d.-e). *FIRST*. https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/first.html
- FSL. (n.d.-f). *FIX*. https://fsl.fmrib.ox.ac.uk/fsl/docs/resting_state/fix.html
- FSL. (n.d.-g). *FNIRT*. https://fsl.fmrib.ox.ac.uk/fsl/docs/registration/fnirt/index.html
- FSL. (n.d.-h). *fsl_anat*. https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/fsl_anat.html
- FSL. (n.d.-i). *Installation and environment*. https://fsl.fmrib.ox.ac.uk/fsl/docs/install/index.html
- FSL. (n.d.-j). *License*. https://fsl.fmrib.ox.ac.uk/fsl/docs/license.html
- FSL. (n.d.-k). *TOPUP*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/topup/index.html
- FSL. (n.d.-l). *XTRACT*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/xtract.html
- FSL. (2026). *FSL* (Version 6.0.7.22) [Computer software]. https://fsl.fmrib.ox.ac.uk/fsl/docs/development/history/index.html
