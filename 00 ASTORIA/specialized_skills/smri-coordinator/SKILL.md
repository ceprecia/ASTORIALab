---
name: smri-coordinator
description: >-
  Routes one bounded structural-MRI task from its verified current state to one
  next approved preprocessing, QC, morphometry, segmentation, feature,
  statistical, or export owner. Use when the request, or a part coordinator, hands
  over that exact modality-planning handoff. It distinguishes T1w, T2w, FLAIR,
  longitudinal, lesion, volumetric, surface, and existing-derivative paths;
  exposes acquisition, population, pathology, template, version, edit, space,
  provenance, privacy, and QC gaps; and returns a checkpointed sMRI Route and
  Handoff Packet without choosing software or scientific methods, running a
  pipeline, loading every adapter, or treating one approval as authorization for
  the full workflow. Triggers: route my structural MRI task, next step for my
  structural MRI analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: smri
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-10-29"
---

# sMRI Skill

Route one structural-MRI task to one next bounded owner. This is a modality
coordinator, not a segmentation method, morphometry workflow, software adapter, or
clinical interpretation capability.

## Purpose

`smri-coordinator` owns:

- identifying the verified current structural-MRI state and one next
  consequential transition;
- distinguishing raw, organized, reconstructed, segmented, surface-derived,
  quality-controlled, feature-ready, modeled, and export-ready states;
- comparing applicable next-owner routes for the approved anatomical target;
- enforcing separate preprocessing, QC, modeling, and export checkpoints;
- producing one user-selected sMRI Route and Handoff Packet.

The user owns the question, hypothesis, prediction, confirmatory status,
population, anatomical target, modality combination, segmentation,
registration, template, surface, lesion, longitudinal, QC, editing, exclusion,
software, feature, model, export, interpretation, and claims.

[exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns general structure and quality inspection.
`freesurfer-tool`, `fsl-tool`, `fmriprep`, `hcppipeline-tool`, and conditional
model adapters own only their approved software implementations after they
become verified Active capabilities. [fmri-coordinator](../fmri-coordinator/SKILL.md) and `dwi-coordinator` own their
respective modality routes.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `sMRI`, `structural MRI`, `T1w`, `T2w`, `FLAIR`,
`cortical thickness`, `volume`, `segmentation`, `FreeSurfer`, `recon-all`,
`brain extraction`, `MNI`, `WMH`, or another broad modality, measure, or
software term.

Do not use this skill to:

- select a segmentation, parcellation, atlas, template, morphometric feature,
  lesion model, statistical method, or software automatically;
- convert, deface, organize, register, segment, reconstruct surfaces, edit,
  extract features, model, save, or export;
- diagnose disease, interpret an individual scan, perform radiological review,
  support treatment, or produce a clinical or PACS deliverable;
- install or invoke software, packages, containers, plugins, licenses,
  credentials, external compute, or services;
- authorize the full structural workflow from one confirmation.

## Inputs

Obtain or mark missing:

- approved task, inquiry part, anatomical estimand, confirmatory or
  exploratory status, and population target;
- source location, type, identifiers, checksums, privacy state, consent or
  sharing boundary, and immutable-input rule;
- DICOM, NIfTI, BIDS, existing derivative, segmentation, surface, feature
  table, model output, or export state;
- T1w, T2w, FLAIR, quantitative, contrast-enhanced, repeated, or longitudinal
  images and their acquisition metadata;
- participants, sessions, repeats, scanner or site, resolution, orientation,
  coverage, artifacts, and missing modalities;
- age, development, species, lesions, tumors, resections, implants, severe
  pathology, atrophy, motion, contrast, and template limitations;
- prior conversion, defacing, bias correction, brain extraction,
  registration, segmentation, surface reconstruction, editing, resampling,
  smoothing, harmonization, and QC;
- exact prior tool, build, operating system, version, configuration, license,
  logs, reports, edits, failures, and partial artifacts;
- desired volume, thickness, area, curvature, tissue, lesion, ROI, surface,
  atlas, longitudinal, or other bounded output and its units and grain;
- proposed next owner, output, acceptance criteria, destination, overwrite,
  compute, network, credential, license, and external-action boundary.

If source provenance, current derivative state, anatomical estimand,
population or pathology compatibility, version, edit history, QC state, or
next deliverable is unresolved, stop with **sMRI route intake incomplete**.

## Steps

### 1. Build the sMRI Current-State Record

| Field | Record |
|---|---|
| user-owned target | Question, anatomical estimand, status, population |
| Current state | Raw, organized, preprocessed, segmented, surfaced, QC reviewed, modeled |
| Source and privacy | Location, identifiers, checksums, consent, defacing, immutable boundary |
| Acquisition | Modalities, repeats, resolution, orientation, site, artifacts |
| Population limits | Age, development, species, lesions, pathology, implants |
| Derivatives | Tool, version, build, OS, configuration, spaces, labels, edits |
| Evidence | Logs, visual QC, quantitative QC, failures, deviations |
| Next transition | Preprocessing, QC, modeling, or export |
| Candidate owner | One bounded method or implementation owner per route |
| Stop point | One selected handoff only |

Do not infer a valid cortical surface or segmentation from file presence.

### 2. Gate 1: approve the bounded route review

Show:

- the current-state record and unresolved provenance or compatibility issues;
- the one next transition under review;
- the eligible owner for the requested transition, applicable alternatives when
  ownership is unresolved, and any unsupported capability gap;
- exact documentation, metadata, or existing-QC inspection needed;
- operations, modalities, adapters, and later transitions excluded.

Gate 1 authorizes only route comparison and read-only inspection of approved
metadata, provenance, logs, reports, and existing QC evidence. It does not
authorize image access beyond that boundary, conversion, defacing,
preprocessing, segmentation, surface reconstruction, manual editing, feature
extraction, modeling, package changes, saving, export, or external actions.

### 3. Route the current structural imaging checkpoint

Use the eligible owner for the requested transition. Compare owners only when the verified state leaves a material routing choice open.

Depending on the current state, route cards may include:

- **Input and organization route:** conversion, deidentification review,
  privacy-preserving defacing, or BIDS organization is the next bounded owner.
- **Volumetric preprocessing route:** bias correction, brain extraction,
  tissue segmentation, registration, or standardized anatomical derivatives
  for an approved volumetric target.
- **Surface reconstruction and morphometry route:** cortical and subcortical
  reconstruction for an approved surface, thickness, area, curvature, or
  parcellation estimand.
- **Special-population or lesion route:** a method and implementation
  compatible with development, aging, lesions, resection, tumors, nonhuman
  anatomy, or other ordinary-assumption failures.
- **Longitudinal route:** within-person templates, version consistency, and
  timepoint handling for a prespecified change estimand.
- **QC and edit route:** outcome-blind visual and quantitative review followed
  by separately approved, fully recorded manual intervention when necessary.
- **Feature and model route:** extract only approved measures after QC, then
  route the resulting table to an appropriate statistical owner.
- **Export route:** package approved nonclinical derivatives with units,
  spaces, labels, privacy, provenance, and destination verification.

For every card state the eligible data and population, scientific target,
exact owner, inputs, outputs, QC checkpoint, edit policy, version constraint,
external boundary, benefit, tradeoff, limitation, and stop point. Do not
select by speed, installed software, or apparent image quality.

### 4. Document the sMRI Routing Decision Record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Eligible source and population | Anatomical target | Canonical owner | QC and edit checkpoint | Version and provenance | Stop point | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- raw, defaced, skull-stripped, registered, segmented, and previously edited
  images confused with one another;
- preprocessing, segmentation, or reconstruction applied twice;
- T1w, T2w, FLAIR, contrast, resolution, orientation, or repeated
  acquisitions used as though interchangeable;
- adult healthy templates or priors applied to incompatible development,
  species, lesions, resection, tumors, severe atrophy, or implants;
- output spaces, surface templates, parcellation versions, label tables,
  transform directions, resampling, and units left undefined;
- cross-sectional processing used for a longitudinal change estimand without
  a selected longitudinal design;
- software versions, operating-system builds, patches, or thread behavior
  mixed within a cohort without a compatibility analysis;
- manual edits made with outcome, diagnosis, group, or desired-result
  knowledge and applied inconsistently;
- automated metric bounds or outlier flags treated as proof of valid anatomy;
- cortical thickness, volume, lesion load, or ROI measures routed to modeling
  before visual QC and exclusion decisions;
- a research derivative treated as a clinical scan or diagnostic measure;
- identifying facial anatomy, headers, filenames, exports, or reports exposed
  beyond the approved privacy boundary;
- an inactive, missing, incompatible, or unverified adapter treated as
  available.

Stop when a population or pathology invalidates an ordinary route, when image
quality requires expert anatomical judgment not available in scope, when
clinical use is requested, or when the next step requires an unapproved
dependency, package, plugin, service, credential, license, installation, or
external write.

### 5. Gate 2: The user selects one next handoff

Ask the user to select, revise, or reject one route and approve:

- the current state, anatomical estimand, population boundary, and next
  transition;
- one canonical next owner;
- inputs, modality combination, version, build, spaces, templates, labels,
  edit policy, expected output, verification, and stop point;
- approved privacy, read, compute, network, credential, license, write,
  overwrite, and destination boundaries for the later owner.

Gate 2 authorizes only creation of the handoff packet. It does not invoke the
next owner or authorize later QC, modeling, export, or saving. Do not infer
selection from silence.

### 6. Return the sMRI Route and Handoff Packet

Return:

```text
sMRI Route and Handoff Packet
Approved task, anatomical estimand, and inquiry part:
Confirmatory or exploratory status:
Population, pathology, and clinical-use boundary:
Verified source, privacy state, and provenance:
Acquisition, modality, repeat, and artifact state:
Existing preprocessing, segmentation, surfaces, spaces, edits, and versions:
Completed QC evidence and unresolved failures:
Selected next transition:
Selected canonical owner:
Why this owner is eligible:
Bounded inputs and modality combination:
Expected output, units, grain, and acceptance criteria:
Version, build, template, atlas, label, and transform requirements:
Privacy, read, compute, network, license, and write boundaries:
Explicitly excluded later steps:
Known limitations:
Required next checkpoint:
Stop conditions:
```

Stop after the packet. Invoke the named owner separately. Return to this
coordinator only when another structural transition requires routing.

## Handoffs

- Route one transition per invocation. Preprocessing, QC, modeling, and export
  remain separate approvals.
- Structural contrast, segmentation, surfaces, labels, and morphometric
  measures are method- and version-dependent.
- Preserve immutable source images, exact acquisition metadata, derivative
  lineage, manual edits, software version, build, patches, and operating
  system.
- Existing skull stripping, bias correction, registration, segmentation, or
  resampling must be identified before another route is proposed.
- Population, pathology, lesion, development, species, resolution, and
  contrast compatibility precede software selection.
- Visual QC and prespecified quantitative summaries precede feature extraction
  and modeling. Automated bounds alone do not establish validity.
- Manual corrections remain outcome-blind where feasible, consistently
  governed, and fully recorded.
- Do not mix software versions or processing streams within an inferential
  cohort without an approved compatibility or sensitivity plan.
- Research morphometry is not clinical diagnosis or surgical guidance.
- A missing implementation owner remains an explicit capability gap.
- No route card, handoff, segmentation, or successful reconstruction
  establishes a scientific conclusion.

## Structural imaging transition and handoff records

Use the records relevant to the verified state and the one requested transition. A routing record or handoff does not authorize the next operation.

- **Labeled sMRI route cards.** Compare only eligible owners for one next sMRI transition. This preserves population, pathology, and state compatibility. This requires exact provenance and anatomical target. This does not process anatomy.
- **sMRI Routing Decision Record.** Show source state, population, method role, version, QC, edit, privacy, and stop boundaries. This makes hidden anatomical and provenance assumptions reviewable. This may stop for expert review or a missing owner. It cannot establish anatomical validity.
- **Verified sMRI Route and Handoff Packet.** Produce one handoff packet and stop before invocation. This prevents one approval from authorizing a pipeline. This requires a new invocation for each transition. This does not execute the selected step.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended routing and comparability audit.** Add blinded dual-review QC and cross-version or cross-route sensitivity planning. This detects selected edit and version dependence. This adds reviewers, data access, and compute. Agreement does not prove measurement validity.
- **Full checkpoint graph plus next-step cards.** Map a full prospective multimodal structural workflow with separately gated branches. This reveals modality and longitudinal prerequisites early. This loads more catalog context and can imply a pipeline. The graph does not authorize later steps.

**Excluded handoff plus executed checkpoint.** Invoking the selected adapter and proceeding through its QC automatically is outside this coordinator’s authority. This reduces routing overhead. This creates automatic chaining and broader authority. Rejected for this coordinator.

## Checks

- **Positive:** a T1w cohort with a fixed cortical-thickness estimand and no
  approved implementation produces surface and applicable alternative route
  cards, not a `recon-all` command.
- **Negative:** `process these T1 images` does not trigger this skill.
- **Prior processing:** a skull-stripped image presented as raw stops before a
  second extraction.
- **Population:** an adult healthy-template route is not offered silently for
  an infant, lesion, resection, tumor, or nonhuman dataset.
- **Version:** mixed FreeSurfer major versions require a compatibility or
  reprocessing decision before pooled modeling.
- **QC:** completed segmentation without visual QC stops before feature
  extraction.
- **Clinical boundary:** a request to diagnose a participant or prepare a PACS
  deliverable is declined or handed to an appropriate licensed clinical
  process outside this system.
- **Authorization:** approval of reconstruction never authorizes manual edits,
  exclusions, modeling, export, or saving.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Brain Imaging Data Structure. (n.d.). *MRI specification* (Version 1.11.1). https://bids-specification.readthedocs.io/en/stable/modality-specific-files/magnetic-resonance-imaging-data.html
- Fischl (2012). https://doi.org/10.1016/j.neuroimage.2012.01.021
- FreeSurfer. (n.d.). *QA tools*. https://surfer.nmr.mgh.harvard.edu/fswiki/QATools
- FreeSurfer. (n.d.). *recon-all*. https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all
- FreeSurfer. (n.d.). *Release notes*. https://surfer.nmr.mgh.harvard.edu/fswiki/ReleaseNotes
- FSL. (n.d.). *fsl_anat*. https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/fsl_anat.html
- Washington University. (n.d.). *HCP Pipelines* [Computer software]. GitHub. https://github.com/Washington-University/HCPpipelines
