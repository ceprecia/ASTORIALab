---
name: freesurfer-tool
description: >-
  Executes one already approved FreeSurfer operation through an available,
  version-and-build-verified environment and returns an exact command, runtime,
  subject-state, output, log, edit-history, and provenance record. Use when the
  request names this skill or a verified Active modality skill routes one exact
  standalone FreeSurfer handoff. It makes the reconstruction stream, inputs,
  subject identifier, SUBJECTS_DIR, version, build, operating system, patches,
  license, resources, existing subject state, manual edits, side effects, rerun
  boundary, outputs, and visual-QC handoff visible before execution. It does not
  choose cross-sectional or longitudinal processing, stages, atlases, T2 or
  FLAIR use, edits, exclusions, thresholds, or interpretation; install or
  license software; silently resume, retry, clean, overwrite, or declare a
  reconstruction scientifically valid. Triggers: run FreeSurfer recon-all,
  FreeSurfer surface operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: smri
  dependencies: ""
  requires: FreeSurfer, T1w images
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# FreeSurfer Tool

Execute one approved standalone FreeSurfer operation with the exact software
state available for the selected project.

## Purpose

`freesurfer-tool` owns:

- version, build, patch, operating-system, license, and command preflight;
- translation of one approved FreeSurfer operation into an inspectable
  command;
- exact input, subject identifier, `SUBJECTS_DIR`, resource, and side-effect
  control;
- one approved cross-sectional, base-template, longitudinal-timepoint,
  rerun-stage, statistics, conversion, or inspection operation at a time;
- preservation of existing subject state, manual-edit history, logs, status,
  outputs, and failures;
- structural output verification and a neutral visual-QC handoff packet;
- a FreeSurfer Operation Record.

The user owns the scientific question, input images, cross-sectional or
longitudinal design, subject and timepoint identity, stages, T2 or FLAIR use,
atlases, parcellations, segmentation targets, resources, manual edits, rerun
point, QC criteria, exclusions, interpretation, and claims.

[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-MRI routing and checkpoint transitions. When
FreeSurfer is being invoked and managed inside an approved fMRIPrep run,
[fmriprep](../fmriprep/SKILL.md) owns that execution instead. This adapter never modifies an
fMRIPrep-managed FreeSurfer tree without a separate, explicit handoff.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `FreeSurfer`, `recon-all`, `cortical thickness`,
`segmentation`, `surface reconstruction`, `aseg`, `aparc`, `structural MRI`,
or another broad software, output, or method term.

Do not use this skill to:

- choose a reconstruction stream, stage, atlas, segmentation, surface,
  morphometric measure, longitudinal strategy, or QC threshold;
- install, upgrade, patch, download, register, or license FreeSurfer;
- create manual edits or decide whether an edit is needed;
- make clinical, diagnostic, presurgical, treatment, or patient-specific
  decisions;
- run group statistics or interpret morphometry.

## Inputs

Obtain or mark missing:

- an approved FreeSurfer Processing and QC Specification;
- exact research-only operation and stop point;
- input image paths, modalities, acquisition relationship, and immutable
  source state;
- subject, session, timepoint, and base-template identifiers;
- cross-sectional, base, longitudinal, rerun, statistics, or inspection
  stream;
- selected FreeSurfer executable or container, version, build stamp, patches,
  architecture, and operating system;
- matching installed command help and official documentation;
- `FREESURFER_HOME`, `SUBJECTS_DIR`, license path, environment setup, and
  required auxiliary software state;
- existing subject directory, prior commands, `recon-all.log`, status files,
  completion state, lock files, manual edits, and version history;
- exact input flags, stages, T2 or FLAIR options, expert options, and resource
  settings;
- output-collision, resume, rerun, backup, mutation, and rollback policy;
- expected files, statistics, logs, visual-QC views, stop conditions, and
  structural acceptance checks;
- compute and destination authority.

If the stream, input identity, existing subject state, exact build, license,
edit history, side effects, or QC specification is unresolved, stop with
**FreeSurfer operation contract incomplete**.

## Steps

### 1. Confirm the standalone operation

State one bounded operation, such as:

- create one new cross-sectional subject;
- create one approved longitudinal base from completed cross-sectional
  timepoints;
- process one approved longitudinal timepoint against that base;
- rerun one specified stage after a user-authored, recorded edit;
- extract one approved set of existing statistics;
- inspect one existing subject without modification.

Do not collapse the cross-sectional, base, and longitudinal streams into one
approval. Do not add input images, stages, T2 or FLAIR refinement, atlases,
expert options, edits, or statistics because FreeSurfer makes them available.

### 2. Preflight the exact software and subject state

Read only the bounded context and record:

- executable or container identity and immutable image digest where used;
- `recon-all -version`, build stamp, patch state, architecture, and operating
  system;
- matching command help for the selected operation;
- `FREESURFER_HOME`, `SUBJECTS_DIR`, environment setup, and license-path
  readability without displaying license contents;
- input image identities, formats, dimensions, orientation, voxel size, and
  hashes needed for the approved operation;
- existing subject directories, timepoint and base relationships, logs,
  status, done and error markers, edit files, and prior build provenance;
- active FreeSurfer processes and lock or `IsRunning` files;
- filesystem permissions, free space, output collision, and backup policy;
- requested resources and scheduler state.

Current official review found FreeSurfer `8.2.0` current on 2026-07-23. The participant's installed release is checked independently; a mismatch does not authorize an upgrade or version switch. Every invocation rechecks the
live version, build, patches, operating system, and matching help.

### 3. Gate 1: approve inspection and the operation contract

Show a **FreeSurfer Operation Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| Operation and stop point | | | | |
| Inputs and identifiers | | | | |
| Stream and stages | | | | |
| Version, build, OS, and patches | | | | |
| Environment and license path | | | | |
| SUBJECTS_DIR and existing subject state | | | | |
| Manual edits and prior provenance | | | | |
| Resources and scheduler | | | | |
| Outputs, logs, and QC packet | | | | |
| Mutation, rerun, and rollback policy | | | | |

Gate 1 authorizes only the displayed read-only inspection, version and help
checks, subject-state inventory, and command construction. It does not
authorize processing, licensing, installation, downloads, edits, cleanup,
lock removal, resume, rerun, output mutation, or statistics generation.

### 4. Available FreeSurfer execution forms

Carry forward the selected FreeSurfer build and execution environment.
Compare forms only if a material implementation choice remains open under
the user's approval and multiple already available forms can perform the
same operation. The following forms may qualify.

1. the selected installed FreeSurfer build in a verified environment;
2. an immutable existing FreeSurfer container with explicit mounts;
3. an existing site-managed cluster route with pinned module and scheduler
   state.

For each show version and build control, operating-system provenance,
environment isolation, subject-tree mutation, resources, reproducibility,
visible output, benefit, tradeoff, and limitation. These are execution forms,
not alternative streams, atlases, or scientific methods. Do not propose an
installation route.

### 5. Construct and audit the exact command

Display:

- environment initialization and executable or image identity;
- complete `recon-all` or selected FreeSurfer command;
- subject, timepoint, base, input, T2, FLAIR, and expert-option arguments;
- stage directives and every accepted default;
- `SUBJECTS_DIR`, mounts, permissions, and writable paths;
- thread, parallel, memory, scheduler, and wall-time settings;
- existing subject-tree behavior and exact files expected to change;
- logs, status files, completion markers, and stop point;
- shell quoting and identifier checks;
- failure, interruption, and rollback boundary.

Never add `-parallel`, `-openmp`, `-all`, `-i`, T2, FLAIR, a clean flag, or a
rerun directive automatically. Never assume that a prior subject can be
safely resumed merely because a directory exists.

Treat T2- or FLAIR-guided pial placement as an explicit approved operation:
the image argument alone is insufficient, and the matching installed help
must confirm the corresponding `-T2pial` or `-FLAIRpial` directive. Do not
describe this as generic segmentation improvement. Do not use
`-autorecon1 -autorecon2 -autorecon3` as a fast partial route; together those
directives cover the full reconstruction sequence.

### 6. Review version, subject state, and QC limits

Show:

- differences between the approved specification, candidate examples,
  installed help, and current official documentation;
- version 7 versus version 8 behavior, build and operating-system
  reproducibility, known issues, and applied patches;
- what the selected stage reads and writes;
- existing manual edits and whether the command will preserve or consume
  them;
- longitudinal ordering and completeness requirements where relevant;
- input, identifier, subject-tree, and parallel-run collision risks;
- which output files, logs, and statistics can be structurally verified;
- which white, pial, subcortical, intensity, topology, and registration
  judgments require human visual review;
- why file presence, completion markers, or a numerical thickness range
  cannot establish QC acceptance;
- exact stop, rerun, or escalation conditions.

Do not call FreeSurfer a gold standard, infer accuracy from automation, or
describe the software as unrestricted open source. Its registered software
license and exact use terms remain external prerequisites.

### 7. Gate 2: approve one exact operation

Ask the user to approve:

- exact environment and command;
- input images and subject identifiers;
- stream, stage, and stop point;
- version, build, OS, patches, and license-path use;
- `SUBJECTS_DIR`, existing state, files to be created or modified, and backup
  policy;
- resources and scheduler submission;
- outputs, logs, verification, and visual-QC packet;
- no-install, no-edit, no-clean, no-lock-removal, no-retry, no-stage-change,
  no-overwrite, and no-chaining boundary.

Gate 2 authorizes only the displayed operation and verification. A later
stage, longitudinal base, longitudinal timepoint, new input, edit, rerun,
resume, changed build, cleanup, statistics export, or batch expansion requires
a new approval.

### 8. Run one approved FreeSurfer operation

Run only the approved command. Capture:

- exact environment setup, command, and scheduler submission;
- version, build stamp, patch state, operating system, architecture, and image
  digest where applicable;
- inputs, hashes, subject and timepoint identifiers, stream, and stage;
- `SUBJECTS_DIR` and pre-execution subject-state inventory;
- resources, start and end time, exit status, stdout, stderr, log and status
  files, warnings, and failure markers;
- created and changed files;
- edit-history and prior-state preservation;
- output inventory and hashes for the approved verification set;
- every deviation from the approved contract.

On failure or interruption, preserve the subject tree and evidence. Do not
delete `IsRunning` files, run clean flags, change inputs or resources, add
stages, rerun, resume, or rebuild automatically.

### 9. Verify and stop at visual QC

Separate:

1. **Execution verification:** command conformance, version and build,
   process status, logs, expected stage completion, output structure, and
   provenance.
2. **Visual-QC packet:** approved volumes and overlays, white and pial
   surfaces, subcortical segmentation, normalization, topology, missing views,
   warnings, and prior edit history.
3. **Scientific decision:** the user decides QC pass, failure, exclusion, edit,
   rerun, morphometric use, and interpretation.

Return:

```text
FreeSurfer Operation Record
Approved operation and stop point:
Inputs, hashes, and identifiers:
Stream, stage, and command:
Version, build, OS, patches, and image identity:
Environment, license path, and SUBJECTS_DIR:
Existing subject state and edit history:
Resources and scheduler:
Exit state, logs, status, warnings, and failures:
Created and changed outputs:
Structural-verification result:
Visual-QC handoff packet:
Deviations, unresolved state, and limitations:
Artifacts and hashes:
user-owned QC, edit, rerun, exclusion, and interpretation decision:
```

## Boundaries

- Stop if the operation or stream is selected only because a command is
  installed.
- Stop on an unresolved version, build, operating system, patch, command-help,
  or license state.
- Stop when a subject identifier maps to the wrong person, timepoint, base, or
  existing directory.
- Stop on an active process, unexplained lock or `IsRunning` file, concurrent
  write, output collision, or insufficient storage or permissions.
- Stop if an existing subject tree lacks trustworthy input, command, build,
  completion, or edit provenance.
- Stop when longitudinal prerequisites or cross-sectional timepoints are
  incomplete or inconsistently built.
- Stop when an approved T2 or FLAIR pial-refinement route lacks its matching
  pial directive or the installed help does not support the displayed syntax.
- Stop on an unreviewed FreeSurfer `8.2.0` arm64 installation whose required
  post-release patch state is absent or unresolved.
- Stop before any unapproved input conversion, download, license
  registration, installation, patch, environment mutation, or external write.
- Never remove manual edits or use a clean flag without a separate destructive
  action approval.
- Never create a manual edit or choose a rerun point from outcome inspection.
- A completed `recon-all` process does not establish acceptable surfaces,
  segmentations, morphometry, or diagnosis.
- Do not use fixed cortical-thickness bounds as a universal QC pass rule.
- Do not mix versions, builds, operating-system states, atlas states, or edit
  policies within a cohort without an approved harmonization decision.

## FreeSurfer run and QC evidence

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **FreeSurfer Operation Contract.** Audit version, build, OS, patches, inputs, subject state, edits, command, resources, mutations, and QC limits. This prevents silent stream, state, and rerun assumptions. This requires detailed provenance. Runtime and visual-QC failures may still occur.
- **FreeSurfer Operation Record and QC packet.** Execute one approved operation once, preserve failure evidence, verify structure, and stop at visual QC. This preserves exact authorization and subject-state provenance. Any edit or rerun needs new approval. Structural checks cannot accept the reconstruction.
- **Labeled installed, container, or site-managed forms.** Compare only already available execution forms for the same approved FreeSurfer operation. This makes build and environment provenance visible without reopening stream choice. This adds an execution-form review. This cannot resolve a missing operation, license, or runtime.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and cohort-readiness comparison.** Run one approved subject or timepoint before a separately approved cohort operation. This can expose version, resource, and output issues early. This adds a consequential checkpoint and compute. A passing subject does not guarantee cohort-wide quality.
- **Fixture execution plan.** Add an isolated nonstudy fixture or copied test subject where the exact operation can be tested safely. This can reveal environment, command, and mutation defects before approved subject-state contact. This adds storage and compute. This does not validate study-specific anatomy or QC.
- **Independent state and command audit.** Add independent command review and a copied pre-operation subject-state manifest. This improves detection of unintended mutations and drift. This adds review and storage. Agreement does not establish anatomical accuracy.

## Checks

- **Positive:** one new cross-sectional subject with fixed inputs, version,
  build, command, empty destination, and QC plan produces one Operation Record
  and visual-QC packet.
- **Negative:** `which structural pipeline should I use?` routes to
  [smri-coordinator](../smri-coordinator/SKILL.md).
- **Broad phrase:** `run recon-all` does not trigger this adapter.
- **Managed route:** FreeSurfer requested as part of an fMRIPrep command routes
  to [fmriprep](../fmriprep/SKILL.md).
- **Version:** an installed older release is not silently upgraded to a newer release.
- **Build:** mixed operating-system or patch provenance stops before a cohort
  expansion.
- **Collision:** an existing subject identifier with no approved reuse policy
  stops.
- **Lock:** an `IsRunning` file triggers process and provenance review, not
  deletion.
- **Edit:** a manual edit without an edit record stops before a rerun.
- **Longitudinal:** a base request with incomplete cross-sectional timepoints
  stops.
- **Resource:** fixed candidate `-openmp 8` is rejected when it is not the
  approved allocation.
- **Stage claim:** candidate `-autorecon1 -autorecon2 -autorecon3` is rejected
  as a fast partial reconstruction because the sequence covers the full
  reconstruction stream.
- **Pial refinement:** T2 or FLAIR input without its approved corresponding
  pial directive fails command audit.
- **Patch state:** an unreviewed arm64 `8.2.0` installation stops until its
  post-release patch state is established.
- **Failure:** interrupted processing preserves the tree, log, and status
  without retry, cleanup, part change, or resume.
- **QC:** file presence and a plausible thickness distribution remain
  structural observations, not a QC pass.
- **Clinical:** a diagnostic or patient-specific request is refused or handed
  to an appropriate human clinical workflow.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Dale, Fischl, & Sereno. (1999). https://doi.org/10.1006/nimg.1998.0395
- Fischl. (2012). https://doi.org/10.1016/j.neuroimage.2012.01.021
- FreeSurfer. (n.d.-a). *8.2.0 release notes*. https://surfer.nmr.mgh.harvard.edu/fswiki/ReleaseNotes
- FreeSurfer. (n.d.-b). *8.X setup and patch notes*. https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads/rel8notes
- FreeSurfer. (n.d.-c). *Download and install*. https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall
- FreeSurfer. (n.d.-d). *Edits*. https://surfer.nmr.mgh.harvard.edu/fswiki/Edits
- FreeSurfer. (n.d.-e). *Longitudinal processing*. https://surfer.nmr.mgh.harvard.edu/fswiki/LongitudinalProcessing
- FreeSurfer. (n.d.-f). *QA tools*. https://surfer.nmr.mgh.harvard.edu/fswiki/QATools
- FreeSurfer. (n.d.-g). *recon-all*. https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all
- FreeSurfer. (n.d.-h). *ReconAllTable* [Processing table]. https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllTable
- FreeSurfer. (n.d.-i). *Registration and software license agreement*. https://surfer.nmr.mgh.harvard.edu/registration.html
- FreeSurfer. (n.d.-j). *Visual output review with Freeview* [Tutorial]. https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/OutputData_freeview
- Reuter et al. (2012). https://doi.org/10.1016/j.neuroimage.2012.02.084
