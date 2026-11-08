---
name: dwi-coordinator
description: >-
  Routes one bounded diffusion-MRI task from its verified current state to one
  next approved preprocessing, QC, model, tractography, connectome, feature,
  statistical, or export owner. Use when the request, or a part coordinator, hands
  over that exact modality-planning handoff. It distinguishes raw DWI,
  preprocessed DWI, scalar maps, tractograms, and connectomes; exposes gradient,
  shell, phase-encoding, distortion, motion, anatomy, space, model,
  parcellation, provenance, and QC gaps; and returns a checkpointed DWI Route
  and Handoff Packet without choosing a diffusion model or software, running a
  pipeline, treating streamlines as axons, or treating one approval as
  authorization for the full workflow. Triggers: route my diffusion MRI task,
  next step for my diffusion analysis.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: modality-coordinator
  modality: dwi
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-10-29"
---

# DWI Skill

Route one diffusion-MRI task to one next bounded owner. This is a modality
coordinator, not a preprocessing method, diffusion model, tractography pipeline,
software adapter, or white-matter interpretation capability.

## Purpose

`dwi-coordinator` owns:

- identifying the verified current DWI workflow state and one next
  consequential transition;
- distinguishing raw, organized, preprocessed, quality-controlled, modeled,
  tractography-derived, connectome-derived, feature-ready, and export-ready
  states;
- comparing applicable next-owner routes without substituting a weaker model
  or loading the full diffusion catalog;
- enforcing separate preprocessing, QC, modeling, and export checkpoints;
- producing one user-selected DWI Route and Handoff Packet.

The user owns the question, hypothesis, prediction, confirmatory status,
acquisition, preprocessing, QC, diffusion model, metric, tractography,
parcellation, connectome, exclusions, software, export, interpretation, and
claims.

[smri-coordinator](../smri-coordinator/SKILL.md) owns structural-anatomical routing. [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md)
owns connectivity-method comparison after structural-edge semantics are
defined. `qsiprep-tool`, `fsl-tool`, and `dipy-tool` own only approved
implementations after they become verified Active capabilities. QSIRecon and
MRtrix3 remain explicit capability gaps unless separately authorized and
built.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `DWI`, `DTI`, `diffusion MRI`, `FA`, `MD`, `eddy`,
`topup`, `QSIPrep`, `tractography`, `connectome`, `white matter`, `bvec`,
`bval`, or another broad modality, model, metric, or software term.

Do not use this skill to:

- invent or choose a white-matter hypothesis, diffusion model, scalar,
  tractography algorithm, response function, tissue model, parcellation,
  seeding, stopping, filtering, weighting, or connectome definition;
- convert, organize, preprocess, rotate gradients, fit a model, generate or
  filter streamlines, build a connectome, extract features, model, save, or
  export;
- substitute tensor analysis for a requested higher-order model or vice
  versa because an adapter is available;
- treat FA, MD, AD, RD, an FOD, a streamline, or a connectome edge as a
  specific biological mechanism, anatomical axon, or ground truth;
- install or invoke software, packages, containers, plugins, credentials,
  licenses, external compute, or services;
- support clinical diagnosis, treatment, or surgical navigation.

## Inputs

Obtain or mark missing:

- approved task, inquiry part, diffusion estimand, confirmatory or
  exploratory status, and permitted claim;
- source location, type, identifiers, checksums, privacy state, immutable
  boundary, and provenance;
- DICOM, NIfTI with gradients, BIDS, preprocessed DWI, model map, tractogram,
  connectome, feature table, or export state;
- volumes, b-values, b-vectors, gradient coordinate convention, image affine,
  shell structure, directions, b0 images, gradient nonlinearity state, and
  missing or excluded volumes;
- phase-encoding direction, total readout time, echo spacing, reversed
  phase-encoding or fieldmap inputs, acquisition groups, and metadata;
- motion, eddy-current, susceptibility, signal-dropout, slice-to-volume,
  denoising, Gibbs, bias, intensity-normalization, resampling, interpolation,
  and gradient-rotation state;
- T1w or other anatomy, tissue segmentation, lesion or pathology state,
  registration, transforms, spaces, masks, parcellation, label table, and
  node order when applicable;
- prior tool, exact version, configuration, commands, logs, QC, deviations,
  failures, and partial outputs;
- candidate preprocessing, tensor, kurtosis, orientation-distribution,
  tractography, tractometry, ROI-metric, or connectome target;
- desired output, units, observation and inference grain, acceptance
  criteria, destination, overwrite, compute, network, credential, license,
  and external-action boundary;
- Active method or implementation owner available for the exact next step.

If gradient provenance, shell or acquisition structure, phase-encoding state,
current preprocessing, anatomical alignment, model estimand, QC, or next
deliverable is unresolved, stop with **DWI route intake incomplete**.

## Steps

### 1. Build the DWI Current-State Record

| Field | Record |
|---|---|
| user-owned target | Question, diffusion estimand, status, permitted claim |
| Current state | Raw, organized, preprocessed, QC reviewed, modeled, tractogram, connectome |
| Source | Location, identifiers, checksums, privacy, immutable boundary |
| Acquisition | Volumes, shells, directions, b0, phase encoding, readout, fieldmaps |
| Gradients | b-values, b-vectors, coordinate frame, affine, rotations, exclusions |
| Processing | Corrections, denoising, interpolation, spaces, transforms, versions |
| Anatomy | T1w, tissue model, lesions, registration, parcellation, labels |
| Evidence | Logs, visual QC, quantitative QC, failures, deviations |
| Next transition | Preprocessing, QC, modeling, or export |
| Candidate owner | One bounded method or implementation owner per route |
| Stop point | One selected handoff only |

Do not infer valid gradients or spatial alignment from matching filenames.

### 2. Gate 1: approve the bounded route review

Show:

- the current-state record and every gradient, acquisition, provenance, or
  alignment gap;
- the one next transition under review;
- the eligible owner for the requested transition, applicable alternatives when
  ownership is unresolved, and every unsupported implementation gap;
- exact documentation, metadata, header, log, or existing-QC inspection
  needed;
- operations, models, adapters, and later transitions excluded.

Gate 1 authorizes only route comparison and read-only inspection of approved
metadata, gradients, headers, provenance, logs, reports, and existing QC
evidence. It does not authorize data transformation, preprocessing, model
fitting, tractography, connectome construction, package changes, saving,
export, or external actions.

### 3. Route the current diffusion checkpoint

Use the eligible owner for the requested transition. Compare owners only when the verified state leaves a material routing choice open.

Depending on the verified state, route cards may include:

- **Input and organization route:** conversion and BIDS organization preserve
  images, JSON metadata, b-values, b-vectors, acquisition groups, and source
  lineage.
- **Preprocessing-specification route:** define acquisition-compatible
  denoising, motion, eddy-current, susceptibility, dropout, resampling,
  gradient, anatomy, and QC requirements.
- **Preprocessing-implementation route:** one version-verified adapter
  implements only the approved correction plan. Current QSIPrep preprocesses
  DWI; it no longer owns reconstruction.
- **QC route:** inspect gradient distribution, distortion, motion, dropout,
  residual alignment, anatomy, masks, and usable data before modeling.
- **Diffusion-model route:** compare only models supported by the acquisition
  and estimand, such as tensor, kurtosis, orientation-distribution, or other
  approved representations.
- **Existing-map route:** verify geometry, space, units, model provenance, and
  labels before extracting only the requested scalar or ROI summaries.
- **Tractography or connectome route:** require approved reconstruction,
  anatomy, seeding, stopping, filtering or weighting, parcellation, assignment,
  and edge semantics. Stop at a missing-owner gap when QSIRecon or MRtrix3 is
  required because neither is currently authorized in this catalog.
- **Existing-tractogram route:** do not regenerate preprocessing or
  tractography when the approved task starts from a verified tractogram.
- **Export route:** package approved research derivatives with gradients,
  spaces, transforms, labels, weights, units, provenance, privacy, and
  destination checks.

For every card state the acquisition eligibility, estimand, owner, required
inputs, expected output, QC, model assumptions, anatomical dependence,
external boundary, benefit, tradeoff, limitation, and stop point. Do not rank
routes by installed software or pipeline fashion.

### 4. Document the DWI Routing Decision Record

Record the selected route and its relevant evidence. Add comparison rows only for an unresolved choice.

Present:

| Route | Acquisition and state eligibility | Diffusion estimand | Canonical owner | QC and anatomy checkpoint | Output meaning | Stop point | Main limitation |
|---|---|---|---|---|---|---|---|

Audit:

- b-values, b-vectors, volume count, affine, gradient coordinate frame, or
  rotated-gradient lineage missing or inconsistent;
- phase-encoding direction, readout time, fieldmap, or reversed-encoding
  metadata guessed from file order or labels;
- corrected images paired with original rather than transformed gradients;
- raw, preprocessed, tensor-derived, FOD-derived, tractogram, and connectome
  products confused with one another;
- single-shell, multishell, Cartesian, DSI, or other q-space sampling treated
  as interchangeable;
- distortion, motion, dropout, resampling, or anatomy-to-DWI registration not
  reviewed before modeling;
- tensor scalars, FODs, streamlines, or edge weights treated as direct
  biological properties without model limits;
- scalar maps or tractograms restarted from raw processing when a verified
  downstream product already exists;
- tractography proposed without acquisition support, valid anatomy,
  registration, tissue model, seed and stop rules, or matched null and
  sensitivity plan;
- atlas, parcellation, label table, node order, streamline assignment, edge
  weight, symmetry, zero diagonal, and missing-edge meaning left undefined;
- streamline counts compared as anatomical connection strength without an
  approved quantitative model and sensitivity checks;
- a DIPY adapter mislabeled as an MRtrix3 or QSIRecon implementation;
- QSIPrep routed to reconstruction even though current reconstruction belongs
  to QSIRecon;
- an inactive, missing, incompatible, or unverified adapter treated as
  available.

Stop when model eligibility cannot be established, when anatomical alignment
or gradient provenance is invalid, when clinical or surgical use is
requested, or when the next step requires an unapproved dependency, package,
plugin, service, credential, license, installation, or external write.

### 5. Gate 2: The user selects one next handoff

Ask the user to select, revise, or reject one route and approve:

- the current state, diffusion estimand, acquisition eligibility, and next
  transition;
- one canonical next owner;
- exact gradients, correction state, anatomy, spaces, model, parcellation,
  outputs, verification, and stop point;
- approved privacy, read, compute, network, credential, license, write,
  overwrite, and destination boundaries for the later owner.

Gate 2 authorizes only creation of the handoff packet. It does not invoke the
next owner or authorize later QC, reconstruction, tractography, modeling,
connectome construction, export, or saving. Do not infer selection from
silence.

### 6. Return the DWI Route and Handoff Packet

Return:

```text
DWI Route and Handoff Packet
Approved task, diffusion estimand, and inquiry part:
Confirmatory or exploratory status and permitted claim:
Verified source and provenance:
Acquisition, q-space, shell, phase-encoding, and fieldmap state:
Gradient files, coordinate frame, rotations, and exclusions:
Existing correction, interpolation, spaces, transforms, and versions:
Anatomy, tissue, lesion, registration, parcellation, and label state:
Completed QC evidence and unresolved failures:
Selected next transition:
Selected canonical owner or explicit capability gap:
Why this owner and model are eligible:
Bounded inputs:
Expected output, units, grain, and acceptance criteria:
Privacy, read, compute, network, license, and write boundaries:
Explicitly excluded later steps:
Known limitations:
Required next checkpoint:
Stop conditions:
```

Stop after the packet. Invoke the named owner separately. Return to this
coordinator only when another diffusion transition requires routing.

## Handoffs

- Route one transition per invocation. Preprocessing, QC, modeling, and export
  remain separate approvals.
- Preserve the exact relationship among image volumes, b-values, b-vectors,
  affines, gradient frames, rotations, exclusions, and processing versions.
- Do not infer phase encoding or readout timing from filenames. Use verified
  metadata.
- Acquisition and q-space support determine which models are eligible. The
  coordinator does not choose the model.
- Current QSIPrep owns preprocessing. Current QSIRecon owns reconstruction,
  model fitting, tractography, tractometry, and regional connectivity
  workflows. They are not interchangeable.
- QSIRecon and MRtrix3 are not Active Part 4 adapters in this build. Keep
  their required routes as explicit gaps rather than silently substituting
  `dipy-tool` or shell commands.
- Corrected DWI must remain paired with the correct transformed gradient
  table and complete provenance.
- QC acceptance and anatomy-to-DWI alignment precede model fitting,
  tractography, feature extraction, and connectome construction.
- Tensor scalars are model-dependent and biologically nonspecific.
- Streamlines are reconstructions, not observed axons. A structural
  connectome inherits acquisition, preprocessing, model, seeding, tracking,
  filtering, parcellation, assignment, and weighting choices.
- Research DWI is not clinical diagnosis or surgical navigation.
- No route card, successful preprocessing, map, tractogram, or connectome
  establishes a scientific conclusion.

## DWI transition and handoff records

Use the records relevant to the verified state and the one requested transition. A routing record or handoff does not authorize the next operation.

- **DWI Routing Decision Record.** Show gradient, acquisition, state, model, anatomy, QC, ownership, and output-meaning boundaries. This makes hidden q-space and tractography assumptions reviewable. This may stop at a missing owner. It cannot establish model or tract validity.
- **Labeled DWI route cards.** Compare only eligible owners for one next DWI transition. This preserves acquisition, model, and anatomy compatibility. This requires exact gradient and processing provenance. This does not preprocess or reconstruct diffusion data.
- **Verified DWI Route and Handoff Packet.** Produce one handoff packet and stop before invocation. This prevents one approval from authorizing a pipeline. This requires a new invocation for each transition. This does not execute the selected step.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended routing and robustness audit.** Add cross-model, gradient-perturbation, registration, and tracking-sensitivity planning. This reveals selected reconstruction dependence. This adds models, compute, and multiplicity. Sensitivity does not recover ground truth.
- **Full checkpoint graph plus next-step cards.** Map a full prospective reconstruction and connectome workflow with every transition separately gated. This reveals anatomy and model prerequisites early. This loads deferred tools and can imply a pipeline. The graph does not authorize or supply missing adapters.

**Excluded executed diffusion pipeline.** Invoking preprocessing, reconstruction, tractography, and connectome owners automatically is outside this coordinator’s authority. This reduces manual routing overhead. This creates automatic chaining and broad scientific authority. Rejected for this coordinator.

## Checks

- **Positive:** raw multishell DWI with verified metadata and no preprocessing
  specification produces eligible preprocessing route cards, not a QSIPrep
  command.
- **Negative:** `calculate FA` does not trigger this skill.
- **Gradients:** a corrected image paired with original b-vectors stops before
  model fitting.
- **Metadata:** missing phase-encoding or readout information is reported; no
  distortion route is guessed.
- **Existing map:** supplied FA and atlas maps route to geometry and label
  verification rather than restarting DWI preprocessing.
- **Capability gap:** an approved QSIRecon or MRtrix3 tractography request
  stops with a missing-owner record.
- **Meaning:** a streamline count is not promoted to axon count or direct
  connection strength.
- **Authorization:** approval of preprocessing never authorizes QC, model
  fitting, tractography, connectome construction, export, or saving.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Brain Imaging Data Structure. (n.d.). *MRI specification* (Version 1.11.1). https://bids-specification.readthedocs.io/en/stable/modality-specific-files/magnetic-resonance-imaging-data.html
- Cieslak et al. (2021). https://doi.org/10.1038/s41592-021-01185-5
- FSL. (n.d.). *EDDY*. https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/eddy/index.html
- Maier-Hein et al. (2017). https://doi.org/10.1038/s41467-017-01285-x
- MRtrix3. (n.d.-a). *ACT*. https://userdocs.mrtrix.org/en/latest/quantitative_structural_connectivity/act.html
- MRtrix3. (n.d.-b). *SIFT*. https://userdocs.mrtrix.org/en/latest/quantitative_structural_connectivity/sift.html
- MRtrix3. (n.d.-c). *Structural connectome*. https://userdocs.mrtrix.org/en/latest/quantitative_structural_connectivity/structural_connectome.html
- QSIPrep. (n.d.). *QSIPrep* (Version 26.0.0) [Computer software]. https://qsiprep.readthedocs.io/en/stable/
- QSIRecon. (n.d.). *QSIRecon* (Version 26.0.0) [Computer software]. https://qsirecon.readthedocs.io/en/stable/
