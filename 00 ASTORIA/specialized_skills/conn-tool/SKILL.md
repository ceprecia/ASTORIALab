---
name: conn-tool
description: >-
  Executes one already approved CONN batch or project operation through an
  available, version-verified MATLAB, SPM, and CONN environment or exact
  standalone CONN runtime and returns an exact project-state, batch-field,
  command, write, log, verification, and provenance record. Use when the request
  names this skill or a verified Active method or modality skill routes one
  exact CONN handoff. It makes the project, batch, runtime, license, path
  precedence, versions, subjects, operation family, overwrite fields, parallel
  settings, resources, command, outputs, side effects, recovery boundary, and QC
  handoff visible before execution. It does not choose preprocessing, denoising,
  connectivity, ROI, atlas, model, contrast, threshold, statistics, or
  interpretation; install or activate software; run a multistage pipeline;
  silently use defaults, background execution, overwrite, resume, retry, clean,
  accept QC, or chain results. Triggers: run this in CONN, CONN toolbox batch.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: fmri
  dependencies: ""
  requires: MATLAB + SPM + CONN for the embedded route, or CONN standalone + matching MATLAB Runtime for the standalone route
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# CONN Tool

Execute one approved CONN operation with the exact project, batch, runtime,
and software state available for the selected research project.

## Purpose

`conn-tool` owns:

- CONN, SPM, MATLAB or standalone-runtime, path, command, and license-use
  preflight;
- distinction between a CONN project and a CONN batch definition;
- translation of one approved CONN operation into an inspectable batch and
  command;
- exact project, subject, batch-field, overwrite, parallel, output, and
  side-effect control;
- one approved project-definition, Setup, Denoising, Analysis, Results, or QA
  operation at a time;
- preservation of before-state, logs, failures, outputs, and undeclared-write
  evidence;
- structural verification and an operation-specific QC handoff;
- a CONN Operation Record.

The user owns the scientific question, preprocessing, denoising, nuisance
regressors, filters, ROIs, atlases, seeds, connectivity estimand, first-level
model, PPI or gPPI design, dynamic or multivariate model, second-level design,
contrasts, thresholds, multiplicity, QC criteria, exclusions, interpretation,
and claims.

[fmri-coordinator](../fmri-coordinator/SKILL.md) owns functional-MRI routing.
[fmri-preprocessing-pipeline-guide](../fmri-preprocessing-pipeline-guide/SKILL.md) owns preprocessing and denoising
methods. [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns connectivity nodes, edges,
estimands, models, inference, and claim boundaries. [fmriprep](../fmriprep/SKILL.md) may supply
approved upstream derivatives but is never an automatic predecessor.
Generic MATLAB execution does not own CONN-specific project and batch
semantics, and this adapter does not depend on another ASTORIA skill.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `CONN`, `CONN toolbox`, `connectivity`, `ROI-to-ROI`,
`seed-to-voxel`, `PPI`, `gPPI`, `ICA`, `DCM`, `denoise`, `fMRI`, or another
broad software, method, or output term.

Do not use this skill to:

- select or revise a connectivity, preprocessing, denoising, modeling, or
  inference method;
- create an entire CONN project and run it through several parts under one
  approval;
- install, update, download, add to a persistent MATLAB path, acquire or
  activate a license, or configure a cluster;
- infer that an old SPM release or a standalone runtime is compatible;
- summarize results scientifically or recommend the next analysis;
- make clinical, diagnostic, treatment, or patient-specific decisions.

## Inputs

Obtain or mark missing:

- an approved method-owner handoff and CONN Implementation Specification;
- one exact top-level operation family and stop point;
- existing CONN project path or approved new-project destination;
- genuine batch structure or batch-file path, distinct from the project file;
- project, batch, source-data, ROI, covariate, condition, and design hashes;
- exact subjects, sessions, conditions, analyses, effects, and result scope;
- every batch field, accepted default, `done`, `overwrite`, `filename`,
  `subjects`, `parallel`, and immediate-return value;
- available MATLAB plus SPM plus CONN route, or available standalone CONN plus
  matching MATLAB Runtime route;
- exact releases, updates, architecture, path ordering, shadowed functions,
  compiled components, and runtime compatibility;
- MATLAB license entitlement and successful checkout where the MATLAB route
  is selected;
- current project state, prior stages, partial outputs, logs, pending jobs,
  locks, and concurrent users;
- command, working directory, environment, resources, scheduler, network, and
  remote-execution state;
- explicit and implicit output locations, source-adjacent writes, collision,
  backup, overwrite, rollback, and recovery policy;
- structural invariants and operation-specific QC handoff;
- compute and destination authority.

If the method, operation family, project, batch, subject scope, runtime,
license, path, overwrite behavior, write surface, or QC specification is
unresolved, stop with **CONN operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one operation family

Bound the invocation to one of:

- define or update one project state without processing;
- execute one approved Setup operation;
- execute one approved Denoising operation;
- execute one approved Analysis, `vvAnalysis`, or `dynAnalysis` operation;
- execute one approved Results or `vvResults` operation;
- produce one approved QA output.

Do not run a batch that activates several consequential families, contains a
sequence of batch structures, or progresses from Setup through Denoising,
Analysis, Results, QA, or export. Split each transition into a separately
approved operation.

Do not accept the candidate's claim that CONN, PPI, gPPI, ICA, DCM, or another
named method is appropriate. Require an exact current method-owner handoff and
official support for the selected operation.

### 2. Inspect the project and batch without execution

Record:

- project file identity, hash, size, modification time, selected subjects,
  completed stages, analyses, outputs, pending jobs, and before-state;
- batch source type and hash;
- literal fields, nested operations, `done`, `overwrite`, `filename`,
  `subjects`, `parallel`, and output settings;
- referenced files, glob expansion, relative paths, current-folder
  dependence, and missing inputs;
- expected project mutations, created folders, source-adjacent outputs,
  reports, logs, jobs, temporary files, and undeclared writes;
- collision, concurrency, backup, rollback, and recovery boundary.

`BATCH.filename` identifies the `conn_*.mat` project. A file passed to
`conn_batch(batchfilename)` is instead a batch definition in a supported
`.mat`, `.json`, or `.m` form. Reject the candidate command
`conn_batch('conn_project.mat')` when it merely passes a project file as
though it were a batch.

Treat a `.m` batch as executable code. Inspect it and every called script for
`system`, shell commands, deletion, movement, network access, path
persistence, workspace-dependent behavior, dynamic evaluation, undeclared
scripts, and writes. JSON or MAT batch formats still require a full
field-and-side-effect audit.

### 3. Preflight one available runtime

For a MATLAB route, record:

- exact MATLAB executable, release and update, architecture, and working
  directory;
- successful noninteractive start and active license checkout, not only
  `license('test','MATLAB')`;
- exact CONN and SPM releases and compatible build state;
- `which -all` results for CONN, SPM, and selected functions;
- startup files, saved path, shadowing, compiled extensions, and required
  writable runtime state;
- support for `-batch`, log capture, error exit status, and command quoting.

Use current MATLAB `-batch` behavior for an approved noninteractive route
when the installed release supports it. Do not inherit the candidate's
`-r "...; exit;"` pattern or obsolete `-nosplash` assumption.

For a standalone route, record:

- exact CONN standalone release and launcher;
- matching MATLAB Runtime release and architecture;
- documented support for the selected batch format and operation;
- runtime cache, temporary, home, log, and output writes;
- exit-status and failure behavior.

Current official review found CONN `25b` and SPM `25.01` current on
2026-07-23. For each invocation, use current official sources and verify the
requirements of the selected route. In the MATLAB route, verify the MATLAB,
SPM and CONN paths, releases and applicable licenses. For standalone CONN,
verify the exact launcher, matching Runtime and any additional component or
license requirements documented for that release and operation. Stop if a
requirement for the selected route is missing or incompatible. Installation,
updates, path changes and license activation require their own authorization.

### 4. Gate 1: approve inspection and the operation contract

Show a **CONN Operation Contract**:

| Element | Approved value | Observed state | Side effect or risk | Verification |
|---|---|---|---|---|
| Method handoff and operation family | | | | |
| Project and before-state | | | | |
| Batch source, fields, and code review | | | | |
| Subjects, sessions, and analysis scope | | | | |
| MATLAB or standalone runtime | | | | |
| CONN and applicable runtime components, paths, and license evidence | | | | |
| Overwrite, parallel, and resource fields | | | | |
| Outputs, source-adjacent writes, and recovery | | | | |
| Structural checks and QC handoff | | | | |

Gate 1 authorizes only displayed read-only project and batch inspection,
version, path, runtime and license checks, side-effect inventory, and command
construction. It does not authorize project mutation, processing,
installation, downloading, path persistence, license activation, job
submission, output creation, overwrite, cleanup, or scientific decisions.

### 5. Available CONN execution forms

Use the selected CONN runtime when it supports the approved operation.
Compare forms only when the user's approved scope leaves a material runtime
choice open and more than one already available form supports that same
operation. The following forms may qualify.

1. a version-pinned MATLAB plus SPM plus CONN batch route;
2. an exact-version CONN standalone route with matching MATLAB Runtime;
3. an existing site-managed CONN route with verified module and scheduler
   state.

For each show release compatibility, license use, path isolation, batch
support, project mutation, runtime cache, parallelism, outputs,
reproducibility, visible result, benefit, tradeoff, and limitation. These are
execution forms, not alternative connectivity or denoising methods. Do not
propose an installation route.

### 6. Construct and audit one exact batch

Display:

- project filename and before-state hash;
- one top-level operation family;
- literal subject and session scope;
- every batch field and intentionally accepted default;
- all input, ROI, covariate, condition, design, and result paths;
- `done` and `overwrite` values for every relevant structure;
- parallel job count, profile, scheduler settings, and immediate-return
  behavior;
- source-adjacent outputs, project mutations, logs, reports, jobs, temporary
  files, and stop point;
- exact MATLAB or standalone command, working directory, environment, quoting,
  log path, and expected exit behavior;
- failure, partial-state, backup, rollback, and recovery policy.

Set project, subject, operation, overwrite, and parallel behavior explicitly.
Some documented CONN processing fields default to overwrite enabled. Never
inherit that default. Any overwrite is a separate destructive decision with
an exact target and recoverability review.

Use foreground local execution by default only when it matches the approved
contract. Background processing, HPC, remote execution, scheduler submission,
`parallel.immediatereturn`, or automatic status polling requires an explicit
separate design and approval.

### 7. Review project state, defaults, and QC limits

Show:

- differences among the approved method, candidate example, installed help,
  and current CONN documentation;
- CONN, SPM, MATLAB or Runtime compatibility and path-shadowing risks;
- project-versus-batch distinction and executable-script risks;
- prior project state, subject selection, stage completeness, and stale or
  partial outputs;
- every consequential default, especially overwrite, subject, filename,
  parallel, and done behavior;
- input provenance, spaces, ROI and condition identities, and analysis grain;
- source-adjacent writes, project mutation, job, cache, temporary, report, and
  log behavior;
- what exit status, project fields, output presence, shape, finite values, and
  CONN QA artifacts can verify structurally;
- which preprocessing quality, denoising adequacy, model validity,
  connectivity meaning, statistical inference, and scientific claim remain
  for the user and the method owner.

Do not infer a valid method, successful denoising, reliable connection,
activation, group effect, causal mechanism, or diagnosis because CONN
completed or produced a project, matrix, map, p-value, or QA figure.

### 8. Gate 2: approve one exact invocation

Ask the user to approve:

- project before-state, batch definition, operation family, and subject scope;
- exact selected runtime, component releases, paths, applicable license use,
  and command;
- every field, accepted default, overwrite value, resource, and parallel
  setting;
- every project mutation, output, source-adjacent write, job, cache, temporary
  file, report, and log;
- backup, collision, failure, partial-state, rollback, and recovery boundary;
- structural checks, QC handoff, and stop point;
- no-install, no-update, no-path-persistence, no-license-activation,
  no-stage-change, no-background, no-overwrite, no-retry, no-resume,
  no-cleanup, no-QC-acceptance, and no-chaining boundary unless an exception
  is listed explicitly.

Gate 2 authorizes only the displayed invocation and verification. A second
operation family, changed field, new subject scope, overwrite, parallel
submission, retry, resume, cleanup, export, result interpretation, or next
analysis requires a new approval.

### 9. Run one approved CONN operation and retain evidence

Run only the approved command. Capture:

- selected runtime, release, architecture, CONN version, applicable path
  ordering, startup state, and working directory;
- for the MATLAB route, MATLAB and SPM releases and paths, successful
  license checkout, and any other applicable license evidence;
- for the standalone route, CONN launcher and matching MATLAB Runtime, plus
  any additional component or license evidence required by the selected
  release and operation;
- exact command, batch source and hash, literal fields, project before-state,
  and subject scope;
- input, ROI, covariate, condition, design, and result hashes;
- resources, scheduler, process and job identifiers, start and end time, exit
  status, stdout, stderr, logs, warnings, and errors;
- project after-state, explicit and implicit created or changed files,
  source-adjacent writes, reports, caches, temporary files, and pending jobs;
- every deviation and unexpected write.

On failure, unexpected project mutation, undeclared write, warning escalation,
or incomplete job state, stop and preserve the project, batch, logs, and
partial outputs. Do not change fields, paths, runtime, subjects, resources,
parallel state, or method; overwrite; retry; resume; clean; or advance.

### 10. Verify and stop at the QC handoff

Separate:

1. **Execution verification:** command conformance, runtime and path state,
   exit status, logs, project transition, subject scope, expected artifacts,
   output manifest, and undeclared writes.
2. **Operation-specific QC packet:** only the approved CONN QA, diagnostic,
   design, residual, ROI, matrix, map, or model artifacts needed by the method
   owner.
3. **Scientific decision:** the user decides QC acceptance, remediation,
   exclusion, next operation, interpretation, and claims.

Return:

```text
CONN Operation Record
Approved method handoff and operation family:
Project, before-state, and subject scope:
Batch source, hash, and literal fields:
Selected runtime, applicable component releases and paths, and license evidence:
Exact command, working directory, and scheduler state:
Inputs, ROIs, conditions, covariates, designs, and hashes:
Overwrite, parallel, resource, and recovery policy:
Exit state, logs, warnings, errors, and pending jobs:
Project after-state and created or changed artifacts:
Structural-verification result:
Operation-specific QC handoff:
Unexpected writes, deviations, and limitations:
Artifacts and hashes:
user-owned QC, remediation, next operation, and interpretation:
```

## Boundaries

- Stop if the method or CONN operation is selected only because CONN exists.
- Stop when a project file is passed as a batch definition or the batch source
  is not fully inspected.
- Stop on a batch that activates more than one consequential operation family
  or contains an unapproved batch sequence.
- Stop on unresolved requirements for the selected runtime. Check applicable
  MATLAB or standalone Runtime, CONN, SPM, architecture, license checkout,
  path shadowing, compiled extensions, and startup state.
- Stop on implicit project filename, all-subject scope, overwrite, background,
  immediate-return, scheduler, output, or working-directory behavior.
- Stop on a concurrent writer, pending job, output collision, insufficient
  resources, unreviewed partial state, or ambiguous recovery.
- Stop before any install, update, download, path persistence, license
  activation, external service, remote execution, or scheduler configuration.
- Never run an `.m` batch whose arbitrary-code surface is unresolved.
- Never use output existence, finite values, expected dimensions, p-values,
  or QA figures as scientific acceptance.
- Never automatically summarize, visualize, report, or chain CONN results.

## CONN operations and QC handoff

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **CONN Operation Contract.** Audit project state, batch code and fields, releases, paths, license, defaults, writes, parallelism, recovery, and QC limits. This prevents silent stage, overwrite, subject, and runtime assumptions. This requires detailed project and batch provenance. Runtime and operation-specific QC failures may remain.
- **CONN Operation Record and QC packet.** Execute one approved operation once, preserve partial state, verify the project transition, and stop at QC. This preserves exact authorization and project provenance. Any second operation or recovery action needs new approval. Structural checks cannot accept the analysis.
- **Labeled execution-form comparison.** Compare only already available MATLAB, standalone, or site-managed forms for the same approved CONN operation. This makes license, path, runtime, project-mutation, and parallel differences visible without reopening method choice. This adds runtime review. This cannot resolve a missing method, CONN installation, or license.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Canary record and readiness comparison.** Run the approved operation on one fixture or canary subject before a separately approved study operation. This can expose version, path, resource, and write problems early. This adds a consequential checkpoint and compute. A passing canary does not guarantee cohort-wide validity.
- **Fixture execution plan.** Add an isolated synthetic project or copied nonstudy fixture for the exact batch. This can expose batch, path, overwrite, and project-state defects before observed-data contact. This adds fixture, storage, and compute. This does not validate study-specific denoising or connectivity.
- **Independent batch and mutation audit.** Add independent batch review and a copied before-state project manifest. This improves detection of hidden code, defaults, and undeclared writes. This adds review and storage. Agreement does not establish scientific validity.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- CONN. (n.d.). *conn_batch*. https://web.conn-toolbox.org/resources/conn-manual/conn_batch
- CONN. (n.d.). *Denoising pipeline*. https://web.conn-toolbox.org/fmri-methods/denoising-pipeline
- CONN. (n.d.). *HPC configuration*. https://web.conn-toolbox.org/resources/hpc-configuration
- CONN. (n.d.). *Installation*. https://web.conn-toolbox.org/installation
- CONN. (2026). *CONN* (Version 25b) [Computer software]. GitHub. https://github.com/alfnie/conn/releases/tag/v25b
- MathWorks. (n.d.). *License checks and checkout*. https://www.mathworks.com/help/matlab/ref/license.html
- MathWorks. (n.d.). *MATLAB macOS command-line options*. https://www.mathworks.com/help/matlab/ref/matlabmacos.html
- SPM. (n.d.). *SPM documentation*. https://www.fil.ion.ucl.ac.uk/spm/docs/
- SPM. (n.d.). *SPM software*. https://www.fil.ion.ucl.ac.uk/spm/software/
- Whitfield-Gabrieli & Nieto-Castanon. (2012). https://doi.org/10.1089/brain.2012.0073
