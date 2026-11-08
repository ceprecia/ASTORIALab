---
name: wmh-segmentation
description: >-
  Executes one already approved, noncommercial research-only MARS-WMH nnU-Net
  1.0.2 inference on one fixed FLAIR and noncontrast T1w pair through an already
  available immutable container, then returns an input, command, runtime,
  output, QC-handoff, verification, and provenance record. Use when the request
  names this skill or smri-coordinator routes one exact MARS-WMH handoff. It makes
  target domain, license, nonclinical use, image identity, whole-brain coverage,
  NIfTI geometry, registration, container digest, platform, hardware, mounts,
  network, output, failure, QC, and interpretation limits visible. It does not
  choose a segmentation method, diagnose or monitor a person, install or pull
  software, use latest, convert DICOM, modify source images, broaden mounts,
  overwrite, skip registration by assumption, accept QC, interpret lesion
  burden, or chain downstream analysis. Triggers: segment white matter
  hyperintensities, MARS WMH nnU-Net inference.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: model-adapter
  modality: smri
  dependencies: ""
  requires: the MARS-WMH nnU-Net 1.0.2 environment, a FLAIR and T1w pair
  gates: training or running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-10-29"
---

# WMH Segmentation

Execute one approved MARS-WMH nnU-Net research inference without turning an
automated label map into a clinical result, a biological interpretation, or
evidence that this dataset matches the model's validation domain.

## Purpose

`wmh-segmentation` owns:

- exact MARS-WMH nnU-Net release and immutable container identity;
- one exact FLAIR and noncontrast T1w input pair;
- research-use, license, target-domain, image, geometry, registration,
  runtime, architecture, hardware, mount, network, resource, collision, and
  output preflight;
- translation of one approved segmentation specification into one
  inspectable Docker or Apptainer invocation already supported by the
  selected environment;
- one approved inference without installation, pull, build, retry,
  operator-initiated cleanup, overwrite, subject expansion, or changed
  options;
- structural verification of the mask, geometry, QC artifacts, logs, and
  provenance;
- a MARS-WMH Run Record and neutral Human QC Handoff Packet.

The user owns the scientific question, whether MARS-WMH and nnU-Net are
appropriate, target lesion meaning, population and acquisition
applicability, pathology exclusions, input acceptance, registration route,
hardware route, output use, QC criteria, pass or fail decision, exclusion,
remediation, downstream measurement, interpretation, and claims.

[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI method and workflow routing.
[nibabel-skill](../nibabel-skill/SKILL.md) owns separately approved generic NIfTI header, affine,
value, and round-trip operations. [dcm2nii](../dcm2nii/SKILL.md) owns a separately approved
DICOM conversion. This adapter does not select a segmentation method,
convert source data, edit an input, diagnose a person, or absorb downstream
measurement or statistics. These are handoffs, not dependencies or an
automatic chain.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `WMH`, `white matter hyperintensity`, `white matter
lesion`, `MARS-WMH`, `nnU-Net`, `FLAIR`, `small vessel disease`, `lesion
segmentation`, `brain segmentation`, `diagnosis`, or another broad method,
modality, pathology, or clinical phrase.

Do not use this skill to:

- choose MARS-WMH, nnU-Net, MD-GRU, or another segmentation method;
- determine that a lesion is a vascular-origin WMH;
- use a label map for diagnosis, prognosis, monitoring, treatment, or
  another clinical purpose;
- use the official work for commercial activity or when license eligibility
  is unresolved;
- install, configure, repair, pull, build, update, tag, authenticate to, or
  license Docker, Apptainer, NVIDIA tooling, MARS-WMH, or another runtime;
- use `latest`, a tag without a digest, an unresolved SIF source, or a
  modified official image;
- convert DICOM, deface, curate, preprocess, register, or edit source images
  outside the exact container operation;
- assume that matching orientation or voxel size proves coregistration;
- mount a home directory, vault root, study root, or unrelated dataset;
- use permissive recursive permissions such as `chmod -R 777`;
- overwrite, silently reuse, retry, clean, or interpret an output.

## Inputs

Obtain or mark missing:

- one approved WMH Segmentation Specification naming MARS-WMH nnU-Net
  `1.0.2`;
- explicit confirmation that the use is noncommercial academic research and
  not diagnosis, prognosis, monitoring, treatment, or another clinical use;
- research purpose, exploratory or confirmatory status, target lesion
  definition, population, acquisition domain, pathology exclusions, and
  intended downstream use;
- one participant and session key plus one exact FLAIR and one exact
  noncontrast T1w NIfTI-1 image;
- file paths, hashes, ownership, access boundary, acquisition provenance,
  full-brain field-of-view evidence, single-volume three-dimensional state,
  shape, dtype, finite state, voxel size, orientation, qform, sform, affine,
  and header state;
- evidence that T1w was acquired without contrast;
- approved default T1w-to-FLAIR registration or approved
  `--skipRegistration` with independent coregistration evidence;
- selected already available Docker or Apptainer runtime, exact runtime
  version, host operating system and architecture, and immutable image or
  SIF identity;
- for Docker, exact context, endpoint, daemon identity, daemon operating
  system and architecture, and verified bind-source locality;
- for Apptainer, exact automatic and administrative bind configuration,
  environment-supplied bind state, containment behavior, and effective mount
  inventory;
- official image
  `ghcr.io/miac-research/wmh-nnunet@sha256:4b1ba842901ff953834067f3cfd6b03b06a7d0bcb62df5fb39ce43b5da7dcec7`
  or a verified SIF built from that exact OCI digest;
- exact version-matched container help and accepted flags;
- selected CPU or compatible NVIDIA GPU route, hardware identity, driver and
  runtime compatibility, memory, threads, temporary storage, wall-time, and
  scheduler limits;
- exact minimal read-only input mounts mapped to fixed, nonidentifying,
  shell-safe container paths and one private writable output directory;
- host and container effective user and group mapping plus output ownership,
  mode, ACL, and verified write compatibility without permission broadening;
- an explicit fresh `.nii.gz` output path, collision policy, partial-state
  policy, and failure-preservation policy;
- required enabled MARS-WMH QC, whether the optional statistics CSV is
  required, and whether debugging intermediates are justified;
- network-disabled execution plan;
- expected mask, required persistent QC HTML, optional statistics, log, and
  provenance inventory; temporary QC PNGs are expected only when an approved
  `--debug` run retains its temporary directory;
- outcome-blind structural and human visual-QC criteria;
- compute and destination authority.

If license eligibility, research-only use, method selection, target domain,
input identity, full-brain coverage, noncontrast T1w status, geometry,
registration route, exact image identity, architecture, runtime, hardware,
output, or QC is unresolved, stop with **MARS-WMH execution contract
incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm the research and license boundary

The reviewed official MARS-WMH release is licensed under CC BY-NC-ND 4.0,
limits use to noncommercial academic research, requires citation, and states
that the work is not a medical device.

Before any runtime or image inspection, record:

- the noncommercial academic research purpose;
- why the target is WMH of presumed vascular origin rather than another
  lesion class;
- population and acquisition similarities and differences relative to the
  cited validation evidence;
- any stroke, tumor, demyelination, postsurgical change, severe artifact, or
  other domain-shift concern;
- the prohibited clinical uses;
- the required software and method citations.

If use could produce financial return, is clinical, redistributes or modifies
the official work, or has unclear license eligibility, stop for explicit
license clarification. Do not infer permission from repository visibility or
the NeuroClaw candidate's MIT license.

### 2. Preserve the fixed method route

This adapter implements one fixed route: official MARS-WMH nnU-Net release
`1.0.2`. It does not compare nnU-Net with MD-GRU, another WMH model, or manual
segmentation. A method comparison or missing method decision returns to
[smri-coordinator](../smri-coordinator/SKILL.md) or the applicable model-comparison owner.

Docker and Apptainer may be compared only as already available execution
forms for the same approved image identity. For each available form show:

- exact image or SIF identity and how it is verified;
- host and container architecture compatibility;
- bind, read-only, GPU, network, temporary, and output behavior;
- visible command and artifacts;
- benefit, tradeoff, and limitation.

If only one compatible form exists, explain the fixed form. Do not install a
second runtime to create an artificial option.

### 3. Build the MARS-WMH Execution Contract

Create:

| Element | Approved meaning | Exact binding | Evidence or assumption | Verification |
|---|---|---|---|---|
| Research and license boundary | | | | |
| Target lesion and population domain | | | | |
| Participant, FLAIR, and T1w identity | | | | |
| NIfTI geometry and full-brain coverage | | | | |
| Registration route | | | | |
| Release, image, runtime, and architecture | | | | |
| CPU or GPU and resources | | | | |
| Mounts, network, and privacy | | | | |
| Output, QC, statistics, and failure policy | | | | |
| Verification and stop point | | | | |

No runtime default, candidate promise, package availability, or attractive
example fills a missing scientific or licensing decision.

### 4. Audit inputs without modifying them

For both images verify:

- exact participant and session association;
- NIfTI-1 readability, compression state, hash, size, exactly one
  single-volume three-dimensional array, shape, dtype, finite values, and
  header integrity;
- qform and sform codes, affines, best-affine behavior, axes, handedness,
  voxel sizes, and world-space bounds;
- full-brain coverage and absence of obvious truncation under the approved
  review boundary;
- modality and acquisition identity;
- that the T1w is noncontrast;
- the FLAIR resolution and slice thickness relative to the documented
  recommendations;
- that no input resides inside the proposed writable output directory.

The official pipeline copies inputs into a temporary work directory and may
reconcile qform and sform in those copies. It warns when the two forms imply
different axis orientations and may choose one affine. An unresolved qform,
sform, orientation, handedness, or world-coordinate conflict stops before
execution. The adapter never repairs the source images.

The release parser checks only file existence and filename extension, while
later inference and QC code assume three-dimensional arrays. A two-dimensional
scalar image, four-dimensional time series, or any extra-volume input stops
before the container.

### 5. Fix the registration route

Choose exactly one approved route:

1. **Default registration:** the container brain-extracts both images and
   applies affine T1w-to-FLAIR registration before inference.
2. **Skip registration:** use `--skipRegistration` only when independent
   evidence shows that FLAIR and T1w are already coregistered in the intended
   space.

Matching axes and voxel sizes alone do not prove coregistration. For the skip
route, require matching shape and affine within an approved tolerance plus
an existing visual or quantitative registration check. For the default
route, make HD-BET and BRAINSFit processing, interpolation, hardware
behavior, and required post-run registration QC visible.

Changing this route changes the operation and reopens Gate 2.

### 6. Verify exact release, image, platform, and help

The reviewed official state is:

- MARS-WMH release `1.0.2`, commit
  `8c45a10cac0aaa28b232bde4b974e4455dfa4acc`;
- nnU-Net OCI manifest digest
  `sha256:4b1ba842901ff953834067f3cfd6b03b06a7d0bcb62df5fb39ce43b5da7dcec7`;
- config digest
  `sha256:605a30174f9ee1ef634a96d05afbab86024e6e20ff0bcbb41a898d377e15ad33`;
- Linux `amd64`, nonroot user, and entrypoint
  `python /opt/scripts/pipeline_nnunet.py`.

Inspect the already available runtime and image without changing them:

- exact runtime path, version, architecture, and GPU support;
- for Docker, context, endpoint, daemon identity, daemon operating system and
  architecture, whether every bind source resolves on the daemon host inside
  the approved privacy boundary, and whether every bind destination is an
  approved absolute container path;
- for Apptainer, administrative system binds, `hostfs`, automatic home,
  current-working-directory, `/tmp`, and `/var/tmp` behavior plus
  `APPTAINER_BIND`, `APPTAINER_BINDPATH`, and `APPTAINER_MOUNT` state;
- exact OCI digest or SIF file hash and recorded OCI source digest;
- image labels and entrypoint;
- effective container user and group plus host bind-write semantics;
- exact `-h` output for the selected artifact;
- source, release, license, and hardware identity;
- whether execution can be network-disabled;
- whether minimal read-only input and writable output binds are supported.

Stop on `latest`, tag-only identity, digest mismatch, modified image,
unverified SIF ancestry, missing image, missing runtime, platform mismatch,
unsupported GPU, or unavailable resources. Do not pull, build, emulate,
install, retag, or authenticate.

A remote Docker daemon is a separate data-access boundary. Stop unless it is
separately authorized and its exact input paths, output path, transfer
behavior, and privacy controls are verified. For Apptainer, use only
version-verified containment and mount-suppression behavior, normally
including `--containall` plus exact controls for current-directory and system
binds. Reject or clear environment-supplied bind variables for the invocation
and inspect the effective mount inventory. If only the approved binds cannot
be established, stop.

### 7. Construct one no-clobber command

Build one exact invocation that:

- references the immutable image or verified SIF;
- binds only the exact input files read-only and maps them to fixed safe
  container paths such as `/inputs/FLAIR.nii.gz` and
  `/inputs/T1w.nii.gz`;
- binds one private fresh output directory writable;
- for Docker, uses the approved local daemon, an explicit unique container
  name, and no `--rm`, so a stopped container remains inspectable until a
  separately approved cleanup;
- for Apptainer, applies version-verified containment, suppresses unwanted
  home, current-directory, `hostfs`, system, and environment-supplied binds,
  and exposes only the approved effective mount set;
- disables network access when the selected runtime supports a verified
  syntax;
- passes explicit `--flair`, `--t1`, and `-o` paths;
- includes `--skipRegistration` only under the approved skip route;
- leaves the official QC enabled;
- includes `--saveStatistics` only when its descriptive output is approved;
- omits `-x`;
- omits `--quiet` so registration, reorientation, temporary-state, warning,
  and timing evidence remains in the log;
- omits `--debug` unless retained intermediates are specifically approved,
  privately stored, and covered by the failure plan;
- specifies the approved CPU or GPU exposure without changing hardware
  silently;
- writes no source-side file.

Do not use a broad working-directory mount merely because the official quick
start does. Do not copy inputs, change permissions, or tag an image.
The reviewed pipeline invokes internal subprocesses through a shell. Require
allowlisted container-side input, output, and temporary path characters and
fixed path components without quotes, newlines, substitutions, option-like
basenames, or other shell metacharacters. Outer-command quoting alone does
not repair an unsafe path consumed by the container's internal shell.

The pipeline computes descriptive voxel, volume, and connected-cluster
values for its log and can optionally write them to CSV. It normally writes
one persistent `<mask-stem>_QC.html`; source-derived PNGs and the composed QC
PNG live inside the output-derived temporary directory, are embedded in the
HTML, and are deleted with that directory after a normal successful run.
They persist only under an approved `--debug` route and are not alternative
success artifacts. These implementation outputs are not validated biological
or clinical conclusions.

### 8. Gate 1: approve contract and read-only preflight

Show:

- fixed method, research purpose, license eligibility, and nonclinical
  boundary;
- target-domain and acquisition applicability record;
- completed Execution Contract;
- input identity, coverage, header, affine, geometry, and registration audit;
- exact release, image, runtime, architecture, hardware, help, and license
  evidence to inspect;
- minimal mounts, network state, resources, fresh output, expected artifacts,
  QC plan, and stop point;
- genuine execution-form comparison or explained fixed route;
- unresolved assumptions, domain shifts, and limitations.

Gate 1 authorizes only bounded read-only file, header, affine, hash, runtime,
image, help, resource, collision, and destination inspection plus exact
command construction. It does not authorize an image pull, build, install,
inference, output write, overwrite, operator-initiated cleanup, retry, result
interpretation, or downstream analysis.

If preflight changes an input, registration route, image, runtime, platform,
hardware route, output, statistics, debugging, or QC plan, rebuild the
contract.

### 9. Gate 2: approve one exact inference

Display:

- participant, FLAIR, T1w, and hashes;
- target and nonclinical claim boundary;
- exact release, image or SIF identity, runtime, platform, and hardware;
- exact command with shell-safe argument representation;
- registration route and consequences;
- mounts, network, resources, temporary behavior, output path, and collision
  result;
- expected mask, QC, optional statistics, logs, and provenance;
- verification plan and exact stop point.

Gate 2 authorizes one execution of that exact command. It includes the exact
release's inherent deletion of its output-derived temporary directory after
a normal successful non-debug run. A changed input, participant,
registration route, digest, SIF, runtime, architecture, CPU or GPU route,
mount, network state, flag, output, retry, overwrite, operator-initiated
cleanup, or subject count requires a new contract and Gate 2.

### 10. Execute once and preserve evidence

Record:

- exact command, runtime, image or SIF, digest, platform, and hardware;
- start and end time, process state, exit code, stdout, stderr, and warnings;
- input and output mounts plus observed read and write scope;
- registration, reorientation, resampling, and temporary-work messages;
- mask, QC, optional statistics, log, and partial-artifact inventory;
- resource use and hardware variation;
- failures and deviations.

Do not retry, resume, change a flag, broaden a mount, delete a partial output,
clean a debug directory, or move to another subject. Preserve failure
evidence under the approved privacy boundary.

### 11. Verify structurally and stop at human QC

Verify:

- command and environment conformance;
- exact input hashes and immutable image or SIF identity;
- output existence, readability, hash, NIfTI form, dtype, finite state, and
  release-expected label ontology;
- output shape, affine, orientation, voxel size, and world-space bounds
  against the original FLAIR;
- no unexplained qform or sform change;
- required persistent `<mask-stem>_QC.html` and any approved statistics
  file; inventory temporary PNGs only when an approved `--debug` run retains
  its temporary directory;
- statistics-to-mask reconciliation when statistics were requested;
- logs, warnings, failures, partial state, and unexpected writes;
- provenance completeness.

Do not coerce unexpected labels or geometry. Do not infer that a zero exit
status, nonempty mask, plausible volume, attractive overlay, or complete QC
file establishes segmentation accuracy.

Prepare a Human QC Handoff Packet containing:

- original FLAIR and T1w identities;
- registration route and T1w-to-FLAIR overlay evidence;
- WMH mask overlay locations and display orientation;
- whole-brain coverage, boundary, false-positive, false-negative, artifact,
  and unusual-pathology review prompts;
- quantitative summaries labeled descriptive;
- warnings, domain-shift concerns, and limitations;
- user-owned pass, fail, exclusion, remediation, and downstream decision.

Return:

```text
MARS-WMH Run Record
Approved research purpose and license boundary:
Target lesion, population, acquisition, and domain-shift record:
Participant, FLAIR, T1w, and input hashes:
Header, affine, geometry, and coverage audit:
Registration route and evidence:
Release, image or SIF, digest, runtime, platform, and hardware:
Exact command, mounts, network, resources, and output path:
Exit state, stdout, stderr, warnings, failures, and partial artifacts:
Mask, QC, optional statistics, logs, and hashes:
Execution-conformance and structural-verification result:
Human QC Handoff Packet:
Clinical, domain, accuracy, and interpretation limitations:
user-owned QC, exclusion, downstream-use, and next decision:
```

## Boundaries

- Stop unless the use is noncommercial academic research and nonclinical.
- Stop on unresolved license eligibility, commercial use, redistribution, or
  modification of the official work.
- Stop if MARS-WMH nnU-Net `1.0.2` was not selected upstream.
- Stop if the target lesion meaning, population, acquisition domain, or
  pathology exclusions are unresolved.
- Stop on missing FLAIR, missing noncontrast T1w, non-NIfTI input, incomplete
  brain coverage, an input that is not one single-volume three-dimensional
  image, unreadable data, nonfinite values, or ambiguous identity.
- Stop on unresolved qform, sform, affine, orientation, handedness, or
  geometry conflicts.
- Stop if `--skipRegistration` lacks independent coregistration evidence.
- Stop on `latest`, tag-only identity, a digest mismatch, modified image,
  unverifiable SIF ancestry, platform mismatch, missing runtime, missing
  image, or unsupported hardware.
- Stop on an unapproved remote Docker daemon, unresolved daemon-host bind
  locality, an uncontained Apptainer invocation, unexpected system or
  `hostfs` mounts, or uncleared environment-supplied binds.
- Stop before any install, pull, build, tag, authentication, emulation, or
  runtime repair.
- Stop on broad mounts, writable inputs, unsafe container-side path
  characters, unresolved container-user write access, output nested under
  input, nonempty output, permissive recursive permissions, or unapproved
  network access.
- Stop before `-x`, source edits, DICOM conversion, retry,
  operator-initiated cleanup, subject expansion, or changed options. The
  fixed pipeline's disclosed normal-success temporary-directory deletion is
  part of the approved command, not separate cleanup authority.
- Omit `--quiet`. For Docker, omit `--rm`, use a unique name, and treat the
  stopped container as a disclosed artifact requiring separate cleanup
  approval.
- Reject `--omitQC` for this adapter. An alternative QC workflow is a
  separate handoff and does not authorize omission of the official run's
  persistent QC HTML.
- Preserve hardware and container-version differences as limitations. Do not
  mix them silently within a project.
- Never call the output a diagnosis, prognosis, clinical finding, ground
  truth, validated result for this dataset, or proof of vascular pathology.
- Never chain volume analysis, lesion counting, spatial statistics, group
  comparison, prediction, visualization, writing, or interpretation.
- The MARS-WMH license requires an acknowledgement in resulting work; check its exact wording in the license before use.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Apptainer. (n.d.). *Bind paths and mounts* (Version 1.5). https://apptainer.org/docs/user/latest/bind_paths_and_mounts.html
- Docker. (n.d.). *Bind mounts*. https://docs.docker.com/engine/storage/bind-mounts/
- Gesierich et al. (2025). Technical and clinical validation of a novel deep learning-based white matter hyperintensity segmentation tool. https://doi.org/10.1016/j.cccb.2025.100393
- MIAC. (2025). *MARS-WMH* (Version 1.0.2) [Computer software]. GitHub. https://github.com/miac-research/MARS-WMH/releases/tag/1.0.2
