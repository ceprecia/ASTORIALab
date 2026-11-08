---
name: dipy-tool
description: >-
  Implements one already approved DIPY gradient, mask, diffusion-model, metric,
  or structural-verification operation through an available, exact-version
  public API and returns an exact input, gradient, geometry, model, validity,
  output, verification, and provenance record. Use when the request names this
  skill or dwi-coordinator routes one exact DIPY handoff. It makes image and gradient
  identity, coordinate convention, preprocessing and reorientation history,
  volume selection, model adequacy, mask geometry, fit method, invalid-value
  policy, memory, writes, and claim limits visible before execution. It does not
  choose a diffusion model, shell, b-value range, mask, fit method, metric, or
  threshold; install packages; preprocess data; compute ROI statistics; silently
  clip or replace invalid values; overwrite; interpret maps; or chain downstream
  work. Triggers: fit a diffusion model in DIPY, DIPY tractography or metric.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: dwi
  dependencies: ""
  requires: Python, DIPY
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# DIPY Tool

Implement one approved diffusion-MRI operation through the exact public DIPY
API available for the selected project.

## Purpose

`dipy-tool` owns:

- exact Python, DIPY, NumPy, SciPy, and NiBabel environment preflight;
- translation of one approved diffusion operation into inspectable public-API
  code;
- DWI, b-value, b-vector, mask, image, header, affine, and model-state
  identity control;
- gradient convention, normalization, volume-selection, and reorientation
  verification;
- explicit fit method, model arguments, validity policy, memory, output,
  collision, and side-effect control;
- one approved execution without silent repair, refit, retry, overwrite, or
  downstream chaining;
- structural verification of the requested output and preservation of
  warnings, failures, invalid regions, and provenance;
- a DIPY Operation Record and, when relevant, a neutral QC Handoff Packet.

The user owns the scientific question, acquisition suitability, preprocessing
acceptance, diffusion model, shells and volumes, b0 definition, gradient
convention, mask policy, fit method, regularization, constraints,
metrics, thresholds, aggregation, QC criteria, exclusions, interpretation,
and claims.

[dwi-coordinator](../dwi-coordinator/SKILL.md) owns checkpointed diffusion-MRI routing and method selection.
[nibabel-skill](../nibabel-skill/SKILL.md) owns approved low-level image, header, affine, and
coordinate operations. Preprocessing adapters may produce inputs, but none is
an automatic prerequisite. This adapter does not preprocess DWI data, choose
a model, decide whether an output passes QC, or interpret anatomy.
Candidate ROI aggregation uses no DIPY public API and remains outside this
adapter; geometry checks route to [nibabel-skill](../nibabel-skill/SKILL.md) and approved statistical
summaries or inference route to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `DIPY`, `diffusion MRI`, `DTI`, `FA`, `MD`, `CSD`,
`tractography`, `gradient table`, `bvec`, `tensor fit`, `ROI statistics`, or
another broad software, modality, model, or output phrase.

Do not use this skill to:

- choose among tensor, kurtosis, multicompartment, orientation-distribution,
  tractography, registration, or reconstruction methods;
- infer an acceptable b-value range, shell, direction set, b0 threshold, mask,
  fit method, or metric from candidate defaults;
- preprocess, denoise, Gibbs-correct, motion-correct, distortion-correct,
  register, resample, or rotate gradients;
- install, update, clone, or create an environment for DIPY or another
  package;
- treat finite maps, bounded values, plausible histograms, or attractive
  renderings as proof of model validity;
- convert invalid estimates to scientific zeros or silently clip values;
- compute or interpret an ROI table, metric map, tract, or group difference.

## Inputs

Obtain or mark missing:

- an approved Diffusion Operation Specification and exactly one operation:
  gradient validation, mask creation, model fit or metric export, or
  structural verification;
- scientific estimand and the method-level handoff that fixed the model,
  volumes, shells, mask, metrics, and aggregation where applicable;
- exact DWI, bval, bvec, mask, reference, and model files with hashes and
  one-to-one associations;
- image dimensions, volume count, dtype, scaling, qform, sform, affine,
  orientation, voxel sizes, units, and declared space;
- bval and bvec shape, orientation, units, finite state, norm tolerance,
  coordinate convention, b0 rule, shell structure, and selected-volume mask;
- acquisition, preprocessing, motion-correction, distortion-correction,
  resampling, and gradient-reorientation provenance;
- approved model class, public API, fit method, arguments, constraints,
  design-rank and conditioning checks, invalid-fit policy, and requested
  outputs;
- approved mask creation or supplied-mask policy, including morphological
  operations, cropping, and relationship to the DWI reference;
- exact Python and package versions, API signatures, source state, and
  licenses;
- array shapes, estimated memory, precision, thread, random-state, cache, and
  temporary-storage policy;
- output names, formats, dtype, metadata, units, validity masks, collision,
  atomic-write, rollback, and hashing policy;
- verification plan and compute and destination authority.

If the method, gradient convention, selected volumes, preprocessing or
reorientation history, geometry, mask, fit method, invalid-value policy,
exact API, or output contract is unresolved, stop with **DIPY
operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one approved operation

Choose exactly one transition:

1. validate one DWI and gradient-table association without altering it;
2. create one approved mask from one fixed image input;
3. fit one approved diffusion model and export only its approved outputs;
4. structurally verify one existing DIPY-produced artifact.

Do not combine preprocessing, mask creation, model selection, fitting,
tractography, ROI analysis, visualization, and interpretation into a
pipeline. A request for several operations returns to [dwi-coordinator](../dwi-coordinator/SKILL.md) for an
ordered, checkpointed plan, with a new execution approval for each
consequential transition.

### 2. Audit image and gradient identity

Before constructing code, show:

- exact DWI, bval, and bvec identities and their common provenance;
- DWI volume count against bval and bvec counts;
- accepted bvec layout and the transformation used to reach it;
- finite b-values and vectors, b0 classification, vector norms, and zero
  vectors;
- gradient coordinate convention and whether vectors are expressed in the
  frame expected by the approved operation;
- motion, eddy-current, distortion, registration, and resampling history;
- evidence that any required bvec reorientation was applied to the exact
  selected DWI;
- selected volumes and shells without silently dropping observations;
- image header, affine, orientation, shape, units, dtype, and scaling;
- mask and reference shape and affine correspondence.

Current official DIPY documentation warns that motion correction without
corresponding b-vector reorientation can bias model estimates. A filename
match, equal count, or unit-norm check does not establish correct gradient
orientation. Stop on missing or contradictory provenance.

### 3. Preflight the exact public API

Record:

- Python, DIPY, NumPy, SciPy, NiBabel, and relevant compiled-library versions;
- exact public class or function, signature, documentation version, and
  source identity;
- positional and keyword arguments, accepted shapes, defaults, warnings,
  deprecations, and output semantics;
- model design rank, conditioning, minimum data requirements, supported
  shells, and behavior outside valid support;
- memory required for input arrays, masks, model state, derived outputs, and
  temporary copies;
- output type, shape, dtype, affine, units, validity representation, and
  metadata;
- destination, collision, temporary-file, atomic-write, and rollback state.

The current stable software state reviewed for this design is DIPY `1.12.1`,
full commit `e78ed281628438c1bfa275b8d6c6b69c0f5f1d92`, released 2026-04-23,
requiring Python 3.11 or later. The official online API pages reviewed still
display `1.12.0`, so exact installed signatures and the `1.12.1` source state
remain execution authorities.

In the reviewed API, the current form passes `bvecs` by keyword. Positional
use remains temporarily accepted with a deprecation warning and is scheduled
to fail in DIPY 2.0. The API uses a default `b0_threshold` of 50, defines b0
with `b <= threshold`, checks unit-vector tolerance, and expects at least
seven measurements. These are API facts, not approval of 50 as the study's
b0 rule or seven observations as an adequate design.

In the reviewed tensor API, `TensorModel` documents WLS as its default fit
method. Pass the approved fit method explicitly. Do not let an undocumented
or drifting default choose the estimator. `median_otsu` documents
`autocrop=False` and deprecates `autocrop`; inspect the exact selected
version rather than copying the candidate call.

Verify DIPY in the selected participant runtime. Check the user-selected interpreter and required packages at invocation time. An absent or incompatible dependency stops the affected execution; it does not authorize installation, environment creation, or substitution.

### 4. Gate 1: approve inspection and the operation contract

Show a **DIPY Operation Contract**:

| Element | Approved meaning | Observed state | Risk or side effect | Verification |
|---|---|---|---|---|
| Operation and estimand | | | | |
| DWI, gradients, masks, and references | | | | |
| Geometry, spaces, and image identity | | | | |
| Volumes, shells, b0 rule, and gradient convention | | | | |
| Preprocessing and bvec reorientation | | | | |
| Model, fit method, arguments, and validity policy | | | | |
| API, versions, environment, and resources | | | | |
| Outputs, metadata, writes, and collisions | | | | |
| Verification and scientific limits | | | | |

Gate 1 authorizes only the displayed bounded metadata, header, gradient,
version, API, schema, memory, and destination inspection plus code
construction. It does not authorize package installation, full-array loading
beyond an approved bounded check, fitting, mask creation, output creation,
mutation, overwrite, or downstream work.

### 5. DIPY forms for the approved operation

Keep the selected DIPY implementation and its approved parameters. Compare
forms only when the user's approved scope leaves a material implementation
choice open and multiple already available forms perform that same
operation. The following forms may qualify.

1. the exact version-pinned DIPY public API;
2. an existing reviewed project function that calls the same public API;
3. a synthetic-fixture implementation using the same selected API and
   parameters.

For each form show source identity, argument visibility, data loading,
gradient and geometry checks, memory, output behavior, reproducibility,
visible result, benefit, tradeoff, and limitation. These are implementation
forms, not alternative models, shells, masks, fit methods, or metrics. Do not
propose installation.

### 6. Construct and audit the exact code

Display code before execution. It must:

- use the exact reviewed public API rather than candidate wrapper paths;
- bind the approved inputs by immutable identity;
- pass bvecs by keyword to the current `gradient_table` API;
- pass the approved b0 threshold and vector tolerance explicitly;
- preserve the selected-volume manifest and never silently filter by a fixed
  b-value cutoff;
- verify finite values, counts, layout, norms, convention, and preprocessing
  and reorientation provenance;
- verify shape, affine, orientation, voxel grid, and declared space before
  mask combination;
- pass the model and fit method explicitly;
- test the approved design-rank, conditioning, signal, and mask requirements;
- estimate memory before materializing large arrays;
- keep invalid, failed, excluded, and outside-mask values distinguishable
  from valid scientific zeros;
- write an explicit validity mask or failure table when the output contract
  requires one;
- preserve original precision unless a reviewed output conversion is
  approved;
- write to a fresh temporary path, verify it, then atomically commit to the
  approved destination where the filesystem supports that behavior;
- capture versions, arguments, warnings, failures, hashes, and output
  metadata.

For tensor metrics, do not copy the candidate's mixed policy of clipping
eigenvalues for FA while deriving MD, AD, and RD from an unclipped fit. The user
must approve one mathematically coherent constraint and invalid-fit policy.
Clipping FA to a display range in an official visualization example does not
authorize modifying stored scientific estimates.

Never replace NaN, infinity, a failed fit, or an excluded voxel with zero
unless the approved output schema explicitly defines that encoding and
preserves a separate validity mask.

Do not adapt the candidate ROI-summary script into DIPY ownership. It calls
NumPy, pandas, and NiBabel but no DIPY API. Route an approved ROI summary to
the geometry and statistical owners, preserving atlas identity, affine,
label values, background, analysis mask, support counts, units, and missing
or invalid values.

### 7. Review gradient assumptions and verification limits

Show:

- which choices came from the approved method specification and which came
  from the exact API;
- discrepancies among the candidate, official documentation, installed
  signature, and source;
- the gradient-frame evidence and remaining orientation uncertainty;
- volume and shell inclusion and what data were excluded;
- model identifiability, rank, conditioning, constraints, and numerical
  behavior;
- mask geometry, interpolation history, partial volume, and support;
- finite, invalid, clipped, constrained, excluded, and outside-mask states;
- memory, precision, threading, randomness, and reproducibility limits;
- warnings and failures without suppressing or recoding them;
- which output properties can be checked mechanically;
- which image-quality, model-validity, biological, and clinical judgments
  require human review.

A successful fit, finite value, value within a familiar range, or smooth map
does not establish acquisition quality, model suitability, tissue
specificity, biological truth, or clinical meaning.

### 8. Gate 2: approve one exact execution

Ask the user to approve:

- one complete code block or exact command;
- one operation, input manifest, selected-volume manifest, and output set;
- exact versions, public APIs, arguments, and accepted defaults;
- gradient convention, b0 rule, fit method, validity policy, and geometry
  assumptions;
- memory, threads, randomness, temporary files, and runtime;
- every writable path, new file, collision policy, and atomic commit;
- verification steps and preservation of warnings and failures;
- no-install, no-repair, no-refit, no-overwrite, no-retry, no-interpretation,
  and no-chain boundary.

Gate 2 authorizes only that displayed execution and verification. A changed
input, selected volume, mask, model, argument, fit method, output,
destination, retry, repair, or downstream operation requires a new contract.

### 9. Run the approved DIPY operation once

Run only the approved code. Capture:

- exact code or command and working directory;
- Python, DIPY, dependency, operating-system, and hardware state;
- input hashes, header and affine state, and selected-volume manifest;
- bval, bvec, convention, b0, norm, and reorientation record;
- model class, fit method, arguments, constraints, rank, conditioning, mask,
  and validity policy;
- memory, threads, random state, start and end time, exit status, stdout,
  stderr, warnings, and exceptions;
- temporary and final destinations plus prior collision state;
- output names, shapes, dtypes, affines, units, validity state, support
  counts, and hashes;
- missing, partial, invalid, unexpected, or version-divergent outputs;
- every deviation from the approved contract.

Do not repair gradients, change b0 rules, discard volumes, relax geometry,
switch fits, clip estimates, replace invalid values, change masks, rerun, or
overwrite without a new approved contract.

### 10. Verify and stop

Separate:

1. **Execution conformance:** exact environment, API, code, arguments,
   inputs, selected volumes, resources, writes, process status, and
   deviations.
2. **Structural verification:** output existence, shape, dtype, affine,
   orientation, units, finite and invalid states, validity mask, metadata,
   and hashes.
3. **Method and QC handoff:** model diagnostics, residual or fit evidence,
   gradient and geometry evidence, warnings, and the approved outcome-blind
   QC criteria.
4. **Scientific decision:** the user decides validity, exclusion, remediation,
   downstream use, interpretation, and claims.

Return:

```text
DIPY Operation Record
Approved operation and estimand:
Method-level handoff:
Input, mask, and reference manifest:
Geometry and declared spaces:
Gradient, b0, shell, selected-volume, and reorientation record:
Model, fit method, arguments, constraints, and validity policy:
Versions, public APIs, environment, and source state:
Exact code or command:
Memory, threads, randomness, runtime, and writes:
Exit state, warnings, exceptions, and deviations:
Output inventory, metadata, validity state, and hashes:
Execution-conformance result:
Structural-verification result:
QC evidence and limits:
user-owned validity, remediation, interpretation, and next decision:
```

## Boundaries

- Stop on a DWI, bval, or bvec identity or count mismatch.
- Stop on nonfinite b-values, malformed vectors, unresolved layout,
  unexplained zero vectors, or norms outside the approved tolerance.
- Stop when gradient coordinate convention or required bvec reorientation is
  unverified.
- Stop when selected volumes or shells are inferred from a fixed candidate
  cutoff rather than an approved method specification.
- Stop on incompatible shape, affine, orientation, voxel grid, or declared
  space among images, masks, and references.
- Stop when model support, design rank, conditioning, mask, or signal
  requirements are not met.
- Stop when the fit method, constraints, invalid-value policy, or requested
  metrics are implicit.
- Stop when code uses a private, missing, deprecated, or version-mismatched
  API without an approved compatibility plan.
- Stop before a write if the destination exists, the temporary path is
  unsafe, or collision and rollback behavior is unresolved.
- Preserve NaN, infinity, failed fits, invalid estimates, exclusions, and
  outside-mask states explicitly.
- Never use a familiar FA, MD, AD, RD, or other numeric range as a universal
  pass threshold.
- Never absorb ROI aggregation merely because the candidate placed it beside
  DIPY code.
- A zero exit status, finite map, plausible histogram, or structural pass
  does not establish model validity or QC acceptance.
- Never invoke preprocessing, tractography, connectome construction,
  statistical analysis, visualization, export, or interpretation
  automatically.

## DIPY operation evidence and QC

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **DIPY Operation Contract.** Audit image and gradient identity, frame and reorientation, selected volumes, geometry, API, model support, fit policy, invalid states, memory, writes, and claim limits. This prevents hidden gradient, model, geometry, and failure-encoding choices. This requires detailed provenance and method evidence. Numerical and data-quality failures may still occur.
- **DIPY Operation Record and QC Handoff Packet.** Execute one exact operation once, preserve invalid states and failures, verify structures and provenance, and stop before scientific interpretation. This preserves authorization, gradient identity, validity semantics, and inspectability. Any repair, retry, or next operation needs approval. Structural verification cannot determine biological validity.
- **Labeled public-API, reviewed-project-function, or synthetic-fixture forms.** Compare only already available code forms that implement the same approved DIPY operation and parameters. This makes code provenance, data loading, memory, and writes visible without reopening method choice. This adds implementation-form review. This cannot resolve a missing model, gradient, or mask decision.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Fixture design, expected properties, and comparison record.** Add one separately approved synthetic numerical fixture with known structural expectations before observed-data execution. This can expose API drift, shape, gradient, geometry, and invalid-value defects earlier. This adds fixture design and execution work. Passing synthetic behavior does not establish observed-data validity.
- **Fixture record and observed-data readiness decision.** Execute the approved synthetic fixture first, compare expected properties, then require a new Gate 2 for observed data. This can catch environment and implementation defects before observed-data writes. This adds a consequential checkpoint and compute. A passing fixture cannot validate acquisition or model assumptions.
- **Independent implementation audit.** Add independent code review plus immutable input, gradient, environment, and expected-output manifests. This improves detection of drift, leakage between files, and silent output changes. This adds review and manifest work. Agreement does not prove diffusion-model suitability.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- DIPY. (n.d.). *dipy.core.gradients.gradient_table*. https://docs.dipy.org/stable/reference/dipy.core.html#dipy.core.gradients.gradient_table
- DIPY. (n.d.). *dipy.core.gradients.reorient_bvecs*. https://docs.dipy.org/stable/reference/dipy.core.html#dipy.core.gradients.reorient_bvecs
- DIPY. (n.d.). *dipy.reconst.dti.TensorModel*. https://docs.dipy.org/stable/reference/dipy.reconst.html#dipy.reconst.dti.TensorModel
- DIPY. (n.d.). *dipy.segment.mask.median_otsu*. https://docs.dipy.org/stable/reference/dipy.segment.html#dipy.segment.mask.median_otsu
- DIPY. (2026). *DIPY* (Version 1.12.1) [Computer software]. GitHub. https://github.com/dipy/dipy/releases/tag/1.12.1
