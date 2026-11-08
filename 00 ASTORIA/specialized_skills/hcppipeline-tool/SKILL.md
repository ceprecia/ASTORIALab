---
name: hcppipeline-tool
description: >-
  Executes one already approved HCP Pipelines stage through an available,
  version-pinned official environment and returns an exact source, environment,
  command, runtime, artifact, failure, provenance, and QC-handoff record. Use
  when the request names this skill or a verified Active modality or method
  skill routes one exact HCP Pipelines handoff. It makes the stage, prerequisite
  derivatives, release state, scripts, configurations, templates, licenses,
  dependency versions, input manifest, acquisition choices, resources, writes,
  collisions, defaults, and verification limits visible before execution. It
  does not choose a pipeline or stage; install software; infer inputs; disable
  distortion correction; accept an unsupported dependency; silently resume,
  retry, clean, overwrite, or chain stages; accept QC; or claim that HCP-style
  processing is universally superior. Triggers: run an HCP Pipelines stage, HCP
  minimal preprocessing.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: multimodal
  dependencies: ""
  requires: verified HCP Pipelines environment and prerequisites for the selected stage and release
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# HCP Pipelines Tool

Execute one approved HCP Pipelines stage through the exact official
environment available for the selected project.

## Purpose

`hcppipeline-tool` owns:

- release, commit, modification, script, configuration, template, and license
  preflight for one selected HCP Pipelines stage;
- exact participant, session, run, acquisition, stage, and prerequisite
  derivative scope;
- stage-specific FSL, FreeSurfer, Connectome Workbench, gradunwarp, MSM,
  Python, FIX, MATLAB Runtime, scheduler, and environment verification;
- translation of an approved HCP stage specification into one inspectable
  command or scheduler submission;
- one approved execution without silent part expansion, retry, repair,
  cleanup, resume, or overwrite;
- structural verification of expected artifacts, logs, warnings, failures,
  and provenance;
- an HCP Stage Run Record and a neutral QC Handoff Packet.

The user owns the scientific question, modality, pipeline and stage choice,
acquisition suitability, preprocessing choices, distortion-correction route,
gradient correction, structural and surface strategy, ICA-FIX or MSMAll use,
resources, participant scope, deviations, rerun or resume decision, QC
criteria, exclusions, interpretation, downstream use, and claims.

[smri-coordinator](../smri-coordinator/SKILL.md), [fmri-coordinator](../fmri-coordinator/SKILL.md), and [dwi-coordinator](../dwi-coordinator/SKILL.md) own checkpointed modality
routing. The applicable method guide owns the scientific preprocessing
specification. [freesurfer-tool](../freesurfer-tool/SKILL.md) and [fsl-tool](../fsl-tool/SKILL.md) own standalone operations
through those software families. This adapter does not treat BIDS
organization as proof of HCP compatibility, run a multistage pipeline, or
absorb downstream modeling.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `HCP`, `HCP pipeline`, `HCP preprocessing`, `HCP-style`,
`best pipeline`, `high-quality preprocessing`, `ICA-FIX`, `MSMAll`,
`bedpostx`, `probtrackx`, `structural preprocessing`, `fMRI preprocessing`,
`diffusion preprocessing`, or another broad method, modality, or quality
phrase.

Do not use this skill to:

- decide whether HCP Pipelines fit an acquisition or scientific aim;
- choose among PreFreeSurfer, FreeSurfer, PostFreeSurfer, fMRIVolume,
  fMRISurface, DiffusionPreprocessing, ICA-FIX, MSMAll, or another stage;
- select the first T1w, T2w, fieldmap, functional, or diffusion file found;
- install, clone, download, update, patch, or license HCP Pipelines or a
  prerequisite;
- run on an unsupported host or substitute package versions because they are
  available;
- treat bedpostx, tractography, task analysis, or connectivity as automatic
  parts of preprocessing;
- declare visual or scientific QC success.

## Inputs

Obtain or mark missing:

- an approved modality and method handoff naming exactly one HCP Pipelines
  stage and one bounded processing unit;
- exact participant, session, run, acquisition, and output identifiers;
- approved acquisition-suitability and processing-mode decision;
- complete explicit input manifest with hashes, image identities, repeats,
  metadata, gradients, and selection rationale;
- verified prerequisite-stage derivative manifest and QC state;
- exact stable release, release candidate, development commit, or approved
  modified source state;
- HCP Pipelines root, `show_version` result, full commit when available, and
  hashes for the selected stage script, setup script, batch template,
  configurations, templates, and lookup files;
- exact command interface from the selected script and source state;
- 64-bit Linux host or an already authorized compatible remote execution
  environment;
- stage-specific FSL, FreeSurfer, Workbench, gradunwarp, MSM, Python, FIX,
  MATLAB Runtime, CUDA, and license state;
- effective `HCPPIPEDIR`, `FSLDIR`, `FREESURFER_HOME`, `CARET7DIR`,
  `MSMBINDIR`, `FSL_FIXDIR`, `MATLAB_COMPILER_RUNTIME`, and other
  stage-required environment values;
- approved fieldmap, echo-spacing, phase-encoding, unwarp, gradient
  coefficient, template, mask, registration, resolution, smoothing, seed,
  processing-mode, and accepted-default choices;
- output and work locations, permissions, free space, collision, partial
  state, reuse, resume, rollback, and overwrite policy;
- CPU, memory, GPU, threads, temporary storage, wall time, scheduler, queue,
  and job-isolation limits;
- network, credential, license, and external-service boundaries;
- expected artifacts, logs, warnings, stop conditions, structural checks,
  and outcome-blind visual QC handoff.

If the stage, prerequisite state, source identity, environment, input
manifest, acquisition choice, command, side effects, resources, or QC plan is
unresolved, stop with **HCP stage execution contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one part and one processing unit

Accept exactly one already approved transition, such as:

1. PreFreeSurfer for one explicit session;
2. FreeSurfer for one explicit session;
3. PostFreeSurfer for one explicit session;
4. fMRIVolume for one explicit functional run;
5. fMRISurface for one explicit, already volume-processed run;
6. DiffPreprocPipeline for one explicit diffusion acquisition set;
7. one exact ICA-FIX or MSMAll invocation after its required derivatives
   exist.

The list is not a recommendation or automatic sequence. Verify the exact
entry point in the selected release. A structural trio, volume-to-surface
pair, preprocessing-to-FIX transition, participant batch, or downstream
analysis is several operations and requires separate routing and approvals.

Return method or acquisition uncertainty to the applicable method guide and
modality coordinator. Do not choose a stage because an executable is present.

### 2. Verify official source identity

Record:

- repository or release archive identity;
- stable, release-candidate, post-release development, or modified status;
- tag, full commit, release date, and `show_version` output;
- source-tree cleanliness when a Git checkout is used;
- selected stage, setup, batch-template, configuration, template, and lookup
  file hashes;
- main HCP Pipelines license and any bundled-component licenses relevant to
  the stage;
- differences among the selected release, current official documentation,
  candidate examples, and local wrappers.

Do not label an RC, post-release checkout, unknown archive, or modified tree
as a stable release. A tag, commit, `show_version` result, or hash mismatch
stops before execution.

The selected official stable authority reviewed for this design is HCP
Pipelines `v5.0.0`, full commit
`b97bfeafc20acdbac3b26c2d04e19b031b525c35`, released 2024-12-02. A later
`v5.1.0-rc.1` tag is a release candidate, not a stable substitution.

### 3. Audit prerequisites and the effective environment

Before sourcing anything, inspect the version-matched setup script and
selected stage script. Then, only within the Gate 1 boundary, source the
approved setup script in the approved shell and capture its effective
environment without exposing license contents or credentials.

Verify only the tools needed for the selected stage. Current official
installation guidance for the reviewed release family identifies:

- a 64-bit Linux operating system;
- FSL `6.0.2` or later;
- FreeSurfer `6.0` with a readable license for the structural route, while
  the official guidance says FreeSurfer 7.x is unsupported;
- Connectome Workbench `2.0.1` or later;
- HCP gradunwarp `1.2.3` or later when gradient nonlinearity correction is
  selected;
- MSM_HOCR for MSMSulc or MSMAll routes;
- stage-dependent Python packages, FIX, and MATLAB Runtime components.

These are source observations, not installation instructions. Verify the
exact selected release and stage. Do not use Octave as a general MATLAB
Runtime substitute unless the exact official stage documentation supports
that route.

Record host architecture, paths, executable versions, environment
collisions, shell initialization, scheduler, resources, file permissions,
licenses, and all external access. The setup script must be sourced when the
selected official instructions require sourcing; executing it as a child
process does not establish the parent execution environment.

Verify the selected HCP Pipelines environment and `HCPPIPEDIR` before
execution. Check each dependency and license applicable to the exact stage
and release, including Workbench, gradunwarp or FreeSurfer where required.
An absent or incompatible stage requirement stops that route. Installation,
downgrades and remote execution retain their existing authorization boundaries.

### 4. Audit inputs, prerequisites, and stage-specific decisions

Show an explicit manifest. Never use `find | sort | head` or another
first-match rule to choose an input.

For the relevant stage, audit:

- **PreFreeSurfer:** all T1w and T2w inputs in approved order, session and
  StudyFolder, templates, template brains and masks, FNIRT configuration,
  brain size, sample spacing, fieldmap inputs, echo spacing, phase and unwarp
  directions, gradient coefficients, processing mode, and custom-brain
  state;
- **FreeSurfer:** prerequisite PreFreeSurfer outputs, session directory,
  T1w, brain, T2w or FLAIR state, seed, processing mode, existing-session
  status, edits, and every extra `recon-all` argument;
- **PostFreeSurfer:** prerequisite FreeSurfer outputs, surface atlases,
  grayordinate resolution, mesh resolutions, label tables, reference myelin
  maps, registration, longitudinal state, and structural-QC mode;
- **fMRIVolume:** structural prerequisites, time series, run name, resolution,
  scout, motion route, bias correction, distortion-correction method,
  fieldmaps, echo spacing, unwarp direction, gradient coefficients,
  slice-timing state, functional reference, registration, masking, and
  processing mode;
- **fMRISurface:** completed volume and structural prerequisites, run name,
  mesh and grayordinate resolutions, smoothing, registration, good-voxel
  behavior, and fMRI-QC mode;
- **DiffPreprocPipeline:** positive and negative phase-encoding input lists,
  direction mapping, bval and bvec identity, echo spacing in seconds,
  gradient coefficients, b0 definition, TOPUP configuration, eddy arguments,
  GPU and CUDA route, slice behavior, and output name;
- **ICA-FIX or MSMAll:** exact prior functional products, run and
  concatenation names, FIX implementation and training state, registration
  products, MSM configuration and templates, Python or MATLAB Runtime mode,
  rerun behavior, and every stage-specific option.

`NONE`, `HCPStyleData`, `LegacyStyleData`, default smoothing, default
registration, GPU use, correction omission, and rerun behavior are
consequential values. Do not insert or accept them silently.

### 5. Gate 1: approve inspection and the execution contract

Show an **HCP Stage Execution Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| Modality handoff and one part | | | | |
| Source release, commit, modification, and hashes | | | | |
| Script, setup, templates, configurations, and licenses | | | | |
| Host, environment, dependencies, and license paths | | | | |
| Input manifest and prerequisite derivatives | | | | |
| Acquisition and processing choices | | | | |
| Exact command and accepted defaults | | | | |
| Resources, scheduler, network, and credentials | | | | |
| Work, output, collision, and partial state | | | | |
| Expected artifacts, failure policy, and QC handoff | | | | |

Gate 1 authorizes only the displayed bounded read-only source, environment,
metadata, prerequisite, version, help, manifest, resource, collision, and
destination inspection plus command construction. It does not authorize
processing, downloads, installation, license registration, configuration
editing, directory creation, cleanup, resume, retry, overwrite, or another
stage.

### 6. Execution forms for the approved HCP stage

Carry forward the selected HCP execution form for the approved stage and
parameters. Compare forms only when the user's approved scope leaves a
material execution choice open and multiple already available forms can run
that same stage with those parameters. The following forms may qualify.

1. the direct official stage script in the version-pinned environment;
2. an existing reviewed scheduler wrapper that emits the same official
   command and preserves all arguments and side effects;
3. an already authorized container or site-managed environment when its
   source, contents, licenses, paths, and exact command remain inspectable.

For each form show release identity, environment isolation, scheduler and
resource control, configuration and template access, logs, writes,
reproducibility, visible output, benefit, tradeoff, and limitation. These are
execution forms, not alternative preprocessing methods or stages. If only
one form is verified, show one fixed route and its limitation. Do not propose
installation as an option.

### 7. Construct and audit the exact command

Use the exact selected script's parser and `--help`, not a synthesized
`<stage>/<stage>Pipeline.sh` convention. Current official entry points are
nonuniform. For example, reviewed `v5.0.0` uses:

- `PreFreeSurfer/PreFreeSurferPipeline.sh`;
- `FreeSurfer/FreeSurferPipeline.sh`;
- `PostFreeSurfer/PostFreeSurferPipeline.sh`;
- `fMRIVolume/GenericfMRIVolumeProcessingPipeline.sh`;
- `fMRISurface/GenericfMRISurfaceProcessingPipeline.sh`;
- `DiffusionPreprocessing/DiffPreprocPipeline.sh`;
- stage-specific ICA-FIX and MSMAll entry points.

Display:

- approved shell and sourced setup command;
- exact executable path and script hash;
- every argument, quoted path, ordered list, and intentionally accepted
  default;
- input and prerequisite hashes;
- configuration, template, lookup, training, and license paths;
- effective environment and dependency versions;
- output and work paths;
- resource, scheduler, queue, GPU, CUDA, network, and credential behavior;
- stdout, stderr, job record, and provenance destinations;
- expected writes and the exact stop point.

A BIDS source may inform the explicit manifest but is not a native HCP
StudyFolder contract by itself. Do not rewrite, reorganize, symlink, or copy
the dataset under this gate.

### 8. Review acquisition, release drift, and output limits

Explicitly disclose:

- acquisition assumptions and any use of `LegacyStyleData`;
- missing, repeated, ambiguous, or manually selected inputs;
- prerequisites that are present structurally but not yet QC accepted;
- differences among official release scripts, wiki examples, batch
  templates, candidate commands, and local wrappers;
- stable, RC, development, or modified source implications;
- stage-specific version and license constraints;
- fieldmap, echo-spacing, phase-encoding, gradient correction, registration,
  smoothing, filtering, rerun, and accepted-default implications;
- resource estimates as host-specific planning evidence rather than
  promises;
- existing outputs, partial state, and whether a command may resume or
  overwrite;
- which artifacts can be checked mechanically;
- which anatomy, registration, distortion, motion, surface, diffusion, or
  denoising judgments require human review;
- what a successful exit or expected file inventory cannot establish.

HCP Pipelines contains preprocessing and later analysis families. Repository
membership does not make ICA-FIX, MSMAll, task analysis, bedpostx, or
tractography an automatic next step.

### 9. Gate 2: approve one exact execution

Ask the user to approve:

- the complete command or scheduler submission;
- exact release, commit, script, setup, configuration, and template hashes;
- one part and one enumerated processing unit;
- effective environment and dependency versions;
- all inputs, prerequisites, accepted defaults, and acquisition choices;
- writable paths, side effects, resources, queue, network, licenses, and
  credentials;
- output, collision, partial-state, and failure policy;
- no-retry, no-resume, no-cleanup, no-overwrite, no-stage-chain, and
  no-QC-acceptance boundary.

Gate 2 authorizes only the displayed command and verification. A changed
source, environment, input, script, configuration, template, argument,
resource, destination, stage, participant, resumed state, or retry is a new
action requiring renewed approval.

### 10. Run one approved HCP stage and retain evidence

Run only the approved command. Capture:

- exact command, sourced environment, and scheduler submission;
- host, architecture, resources, queue, and job identifier;
- HCP Pipelines release, full commit, modification state, `show_version`
  result, and selected source hashes;
- prerequisite software versions and relevant license evidence;
- input, prerequisite, configuration, template, and training manifests;
- start and end time, exit status, stdout, stderr, warnings, and scheduler
  records;
- work and output paths plus all observed writes;
- expected, missing, partial, and unexpected artifacts;
- selected output hashes and command-conformance result;
- any deviation from the approved contract.

Failure stops. Preserve logs and partial artifacts. Do not alter resources,
edit configuration, change a fieldmap or correction choice, invoke a
prerequisite, switch to a legacy mode, remove lock files, resume, retry,
clean, or call the next part automatically.

### 11. Verify and stop at the QC checkpoint

Separate:

1. **Execution conformance:** source, environment, script, command, scheduler,
   exit status, logs, writes, and deviations.
2. **Structural artifact verification:** expected-versus-observed paths,
   identities, headers, dimensions, geometry, transforms, surfaces,
   gradients, registrations, reports, and provenance appropriate to the
   selected stage.
3. **Outcome-blind QC handoff:** stage-specific visual and quantitative
   evidence, warnings, missing panels, and unresolved concerns.
4. **Scientific decision:** the user decides pass, fail, exclusion, remediation,
   rerun, next part, downstream use, interpretation, and claims.

Return:

```text
HCP Stage Run Record
Approved modality and method handoff:
Stage and bounded processing unit:
Stable, RC, development, or modified source state:
Release, commit, show_version, scripts, and hashes:
Setup, templates, configurations, and licenses:
Effective environment and dependency versions:
Input and prerequisite manifests:
Acquisition choices and accepted defaults:
Exact command and scheduler submission:
Resources, network, credentials, and writable paths:
Collision, partial-state, resume, and overwrite policy:
Exit state, stdout, stderr, warnings, and scheduler record:
Expected and observed artifacts:
Command-conformance and structural-verification result:
QC Handoff Packet:
Deviations, failures, limitations, and hashes:
user-owned QC, rerun, next-stage, interpretation, and claim decision:
```

## Boundaries

- Stop on a non-Linux or unsupported host unless an already authorized,
  compatible execution environment is the exact selected route.
- Stop on an unknown, RC, development, or modified source state unless the user
  approved that exact state.
- Stop on a tag, commit, `show_version`, script, setup, configuration,
  template, or license mismatch.
- Stop on a missing or incompatible stage-specific prerequisite, license, or
  environment value. Do not install, downgrade, patch, or substitute it.
- Stop if the setup script cannot be safely inspected and sourced in the
  approved shell.
- Stop when a prerequisite stage is absent, incomplete, or not QC accepted.
  Do not run it automatically.
- Stop on an ambiguous or first-match input, mismatched image identity,
  unresolved repeat, missing metadata, gradient mismatch, or unapproved
  phase-encoding, echo-spacing, fieldmap, gradient-correction, or
  processing-mode choice.
- Stop when an option is absent from the exact selected script interface or a
  candidate command omits mandatory arguments.
- Stop on an existing or active output, work, scheduler, or partial state
  without an explicit policy.
- Stop before an unapproved network request, credential use, license action,
  configuration edit, download, or write.
- Preserve exit `137`, scheduler failures, warnings, malformed artifacts,
  missing artifacts, logs, and partial outputs without retry or cleanup.
- A zero exit status, expected file count, or completed scene is not a QC
  pass.
- Never describe HCP Pipelines as universally highest quality, superior, or
  appropriate for every acquisition.
- Never chain structural stages, volume to surface, preprocessing to FIX,
  diffusion preprocessing to bedpostx, or QC to analysis.

## HCP stage records and QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **HCP Stage Execution Contract.** Audit release state, scripts, environment, licenses, prerequisites, inputs, acquisition choices, defaults, resources, writes, failures, and QC limits. This prevents hidden version, stage, command, and correction choices. This requires detailed source and runtime evidence. Runtime and image-quality failures may still occur.
- **HCP Stage Run Record and QC Handoff Packet.** Execute one exact approved stage once, preserve failures, verify structural artifacts, and stop at QC. This preserves authorization, provenance, and failure evidence. Any retry or next part needs new approval. Structural verification cannot accept image quality.
- **Labeled direct-script, scheduler-wrapper, or authorized-environment forms.** Compare only already available execution forms for the same approved stage and parameters. This makes source, resources, and side effects visible without reopening method choice. This adds execution-form review. This cannot resolve a missing part or preprocessing decision.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and batch-readiness comparison.** Run one separately approved canary unit, then require a new Gate 2 before any enumerated batch. This can expose study-specific runtime and output problems before larger writes. This adds a consequential checkpoint and compute. A passing canary does not authorize or guarantee a batch.
- **Fixture or canary execution plan.** Add an already authorized synthetic fixture or canary-unit plan before observed cohort execution. This can reveal environment, command, and artifact defects earlier. This adds compute and fixture or canary maintenance. This does not establish study-data quality or cohort-wide success.
- **Independent execution audit.** Add an independent tag, commit, hash, command, and prerequisite-output evidence review. This improves detection of drift, modified sources, and missing prerequisites. This adds review effort. Agreement does not establish scientific validity.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Washington University. (2024). *HCP Pipelines* (Version 5.0.0) [Computer software]. GitHub. https://github.com/Washington-University/HCPpipelines/releases/tag/v5.0.0
- Washington University. (2025, September 11). *Installation and usage instructions*. GitHub. https://github.com/Washington-University/HCPpipelines/wiki/Installation-and-Usage-Instructions
