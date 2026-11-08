---
name: nibabel-skill
description: >-
  Performs one already approved low-level neuroimaging file, header, affine,
  coordinate, or FreeSurfer-format operation through an available,
  version-verified NiBabel API and returns an exact data-semantics, memory,
  write, round-trip, and provenance record. Use when the request names this
  skill or a verified Active method or software skill routes one exact NiBabel
  handoff. It makes the image class, proxy, shape, dtype, scaling, affine, qform
  and sform, orientation, units, coordinate frame, label mapping, surface
  metadata, memory plan, output encoding, and side effects visible before data
  loading or writing. It does not choose a preprocessing or analysis method,
  infer that world coordinates are MNI, invent label mappings, resample or
  register images, install packages, overwrite sources, or treat a load-save
  cycle as a lossless copy. Triggers: read this NIfTI header, affine and
  coordinate operation in NiBabel.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: multimodal
  dependencies: ""
  requires: Python, NiBabel
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# NiBabel Skill

Perform one approved low-level neuroimaging I/O or geometry operation with the
exact NiBabel API available in the selected Python environment.

## Purpose

`nibabel-skill` owns:

- version, image-class, proxy, header, affine, and API preflight;
- bounded metadata and array access for one selected neuroimaging file;
- explicit voxel-to-world or world-to-voxel coordinate transformation;
- one approved NIfTI or supported low-level image write with exact encoding;
- bounded FreeSurfer geometry, annotation, label, or morphometry I/O;
- memory, scaling, dtype, header, form-code, orientation, and round-trip
  verification;
- a NiBabel I/O Record.

The user owns the scientific question, file and field selection, coordinate frame,
space identity, atlas, label mapping, ROI definition, center definition,
transformation, interpolation, resampling, output dtype, missing-value policy,
write destination, interpretation, and claims.

[fsl-tool](../fsl-tool/SKILL.md) and [freesurfer-tool](../freesurfer-tool/SKILL.md) own their software execution. This adapter
may inspect or create an explicitly approved file for another owner, but it
does not run preprocessing, segmentation, registration, statistics,
visualization, or a modality pipeline.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `NiBabel`, `NIfTI`, `affine`, `voxel`, `MNI coordinate`,
`atlas`, `FreeSurfer surface`, `image header`, `save image`, or another broad
file, format, or coordinate term.

Do not use this skill to:

- select an atlas, label set, ROI center, coordinate frame, image space,
  transformation, interpolation, or output type;
- assume that an affine's world space is MNI;
- resample, register, preprocess, denoise, mask, segment, analyze, or
  visualize images;
- install or upgrade NiBabel, NumPy, pandas, or another package;
- overwrite, rewrite, or normalize a source file without a separate approved
  write contract.

## Inputs

Obtain or mark missing:

- one approved read, inspect, coordinate, FreeSurfer-I/O, or write operation;
- exact input files and hashes;
- expected file format, image class, dimensions, data grain, and integrity
  conditions;
- Python, NiBabel, NumPy, compression, and optional backend versions;
- required metadata fields, array slices, and memory limits;
- raw versus scaled value semantics;
- stored dtype, requested in-memory dtype, scaling, byte order, units,
  intents, extensions, and missing-value policy;
- affine source, qform and sform matrices and codes, fallback behavior,
  orientation, coordinate convention, and declared world or template space;
- for coordinates, voxel-index convention, transform direction, rounding,
  and bounds behavior;
- for atlases, explicit numeric-label table, background value, absent-label
  behavior, and approved center or representative-point definition;
- for FreeSurfer files, surface coordinate frame, mesh metadata, annotation ID
  mode, color table, vertex alignment, and unknown-label behavior;
- for writes, transformed data semantics, output class, header policy, form
  codes, dtype, scaling, destination, collision rule, and round-trip checks;
- read, memory, and destination authority.

If value scaling, affine authority, coordinate space, label mapping, memory,
output encoding, or write side effects are unresolved, stop with **NiBabel
I/O contract incomplete**.

## Steps

### 1. Name one low-level operation

Bound the task to one of:

- inspect file and image metadata without loading the full array;
- read one approved array slice, region, or complete array;
- transform explicitly defined coordinates with an approved affine;
- inspect FreeSurfer geometry, annotation, label, or morphometry metadata;
- create one new image from already approved data and geometry;
- save one approved new file and verify its round trip.

Do not combine inspection, transformation, atlas summarization, surface
export, and file writing merely because NiBabel can perform them.

### 2. Preflight the exact API and file semantics

Record:

- Python, NiBabel, NumPy, compression, and relevant optional versions;
- public image class and API signature;
- file map, compression, size, hash, and read permissions;
- image shape, stored dtype, proxy type, header, zooms, units, intent,
  extensions, and byte order;
- selected image affine plus qform, sform, codes, and fallback state;
- axis codes and array-to-world orientation;
- raw scaling fields and whether requested values are stored, scaled, or
  converted;
- post-load proxy scaling from `img.dataobj.slope` and
  `img.dataobj.inter`, recognizing that consumed header scaling can be reset
  to undefined after load;
- estimated memory for proxy slices, raw arrays, and `get_fdata` with the
  selected dtype and cache policy;
- output destination and collision state for a write;
- surface metadata, annotation mode, vertex count, and label-table alignment
  where relevant.

Current official review found NiBabel `5.4.2` current on 2026-07-23. Verify NiBabel in the participant's selected interpreter; absence stops execution without authorizing installation. Every invocation checks the exact
environment and matching official documentation.

### 3. Gate 1: approve inspection and the I/O contract

Show a **NiBabel I/O Contract**:

| Element | Approved meaning | Observed state | Risk or side effect | Verification |
|---|---|---|---|---|
| Operation and files | | | | |
| Image class, proxy, and format | | | | |
| Shape, dtype, scaling, and units | | | | |
| Affine, qform, sform, and orientation | | | | |
| Coordinate or label semantics | | | | |
| Surface or annotation semantics | | | | |
| Memory and cache plan | | | | |
| Output header, dtype, and destination | | | | |
| Round-trip and stop conditions | | | | |

Gate 1 authorizes only bounded metadata reads, version and API checks, file
inventory, memory estimation, and code construction. It does not authorize a
full array load, output creation, overwrite, header change, coordinate
rounding, label inference, or transformation.

### 4. I/O forms that preserve the approved semantics

Use the selected I/O form when it preserves the approved semantics. Compare
forms only when the user's approved scope leaves a material I/O choice open
and multiple already available forms implement that same operation. The
following forms may qualify.

1. proxy-based metadata or slice access;
2. bounded array materialization with an explicit dtype and cache policy;
3. an existing reviewed project function that preserves the same declared
   semantics.

For each show memory, scaling, dtype, header, coordinate, reproducibility,
visible output, benefit, tradeoff, and limitation. These are implementation
forms, not alternative scientific transformations or ROI definitions.

For an exact byte-for-byte copy, do not propose a NiBabel load-save round
trip. A semantic rewrite and a file copy are different operations.

### 5. Audit the operation-specific semantics

#### Image inspection or data access

Specify:

- proxy versus materialized array;
- requested slice or complete shape;
- raw versus scaled values;
- output dtype and memory estimate;
- cache mode and repeated-read behavior;
- finite-value and range checks that are descriptive only.

`get_fdata()` returns scaled floating-point data and can materialize and cache
the array. It is not a neutral metadata operation and is never the default for
a large file. When the approved operation requires stored, unscaled NIfTI
values, use the supported proxy API `img.dataobj.get_unscaled()` and record
proxy `slope` and `inter`; do not infer absent scaling from the post-load
header alone.

#### Coordinates

Specify:

- source voxel or world frame;
- zero-based voxel-index convention;
- exact affine and transform direction;
- continuous versus rounded output;
- bounds and inverse-transform behavior;
- declared world-space identity.

NiBabel uses RAS+ world-axis convention, but scanner RAS+, an anatomical
space, a template space, and MNI space are not interchangeable. Call a result
MNI only when the source image is verifiably aligned to the named MNI
template.

#### Atlas labels and representative points

Specify:

- actual integer label values and explicit label table;
- background and missing labels;
- center of mass, median voxel, medoid, peak, centroid, or another approved
  definition;
- whether the point must lie inside the region;
- disconnected components and empty-region behavior.

Never map names with `labels[roi_id - 1]`, return `[0, 0, 0]` for an absent
label, or assume a median voxel is a meaningful anatomical representative.

#### FreeSurfer I/O

Specify:

- surface coordinate frame and metadata;
- vertex and face counts;
- annotation `orig_ids` behavior;
- unlabeled vertices and `-1` handling;
- color-table rows, stored annotation values, positional indices, names, and
  byte decoding;
- equality of surface and annotation vertex grain.

#### Image construction or save

Specify:

- source data and approved transformation;
- image class, shape, dtype, scaling, affine, qform, sform, codes, intent,
  units, extensions, and header fields;
- clipping, rounding, overflow, NaN, and Inf behavior;
- output path, temporary file, atomic replacement policy, and collision rule;
- post-save reload and semantic comparison.

Providing both a copied header and a different affine can reset qform and
sform codes. Set and verify form matrices and codes deliberately. Before
setting or comparing a qform, check whether the target affine contains shear
or another component that qform cannot represent exactly. Do not silently
coerce an arbitrary affine into qform-compatible geometry.

### 6. Review scaling, coordinates, and possible loss

Show:

- difference between stored and scaled values;
- proxy, cache, memory, and dtype consequences;
- qform, sform, fallback, and orientation disagreements;
- whether a proposed rewrite changes binary representation, compression,
  header fields, extensions, scaling, precision, or NaN representation;
- whether the affine proves only a world coordinate or a named template;
- label-table gaps, duplicate names, disconnected regions, and representative
  point limitations;
- FreeSurfer annotation positional versus original ID semantics;
- what round-trip equality will and will not test;
- which scientific or anatomical interpretation remains outside this adapter.

Do not repair a header, prefer qform or sform, reorient an array, rename a
space, coerce a label, or change a dtype automatically.

### 7. Gate 2: approve one exact data contact or write

Ask the user to approve:

- exact environment, public APIs, and code;
- files, hashes, array regions, and memory plan;
- raw or scaled value semantics and in-memory dtype;
- affine, form-code, coordinate, label, or surface semantics;
- output class, header, dtype, scaling, path, and collision policy;
- round-trip checks and stop point;
- no-install, no-overwrite, no-inference, no-reorientation, no-resampling,
  no-header-repair, and no-downstream-chain boundary.

Gate 2 authorizes only the displayed operation and verification. A full-array
load, changed dtype, new coordinate frame, different label definition, output
write, overwrite, or second file is a new action requiring approval.

### 8. Perform the approved I/O operation and verify preservation

Capture:

- Python, NiBabel, NumPy, backend, and compression versions;
- exact code and APIs;
- input paths, hashes, image classes, file maps, and compression;
- proxy, shape, stored dtype, scaling, units, intent, extensions, and byte
  order;
- affine, qform, sform, codes, axis orientation, and declared space;
- data slice, materialization dtype, memory, and cache behavior;
- coordinate, label, or FreeSurfer semantics;
- output class, header policy, dtype, scaling, temporary and final paths;
- warnings, exceptions, deviations, and runtime;
- output hash and post-save reload comparison where a write was approved.

On mismatch or exception, stop. Do not change the affine, header, dtype,
scaling, label mapping, coordinate definition, memory route, or destination;
retry; or overwrite.

Return:

```text
NiBabel I/O Record
Approved operation:
Environment and API:
Input files, classes, formats, and hashes:
Proxy, shape, dtype, scaling, units, intent, and extensions:
Affine, qform, sform, codes, orientation, and declared space:
Data region, materialization, memory, and cache:
Coordinate, label, or FreeSurfer semantics:
Output class, header, dtype, scaling, and path:
Round-trip and semantic-verification result:
Warnings, failures, deviations, and limitations:
Artifacts and hashes:
user-owned transformation, interpretation, and next decision:
```

## Boundaries

- Stop when the requested world or template space is inferred only from a
  filename, affine values, atlas name, or user expectation.
- Stop on unresolved qform and sform disagreement, unknown form codes,
  invalid affine, ambiguous orientation, or unsupported file class.
- Stop before setting qform when the intended affine is not exactly
  representable by qform and no explicit approximation policy was approved.
- Stop before a full array load that exceeds the approved memory plan.
- Stop when stored versus scaled values, output dtype, scaling, rounding,
  clipping, or missing-value behavior is not fixed.
- Stop on an absent, duplicated, noninteger, or unmapped atlas label.
- Stop when a surface and annotation differ in vertex grain or coordinate
  provenance.
- Stop before any install, package change, unapproved full-data read,
  directory creation, external write, or overwrite.
- Never claim a load-save result is byte-identical without comparing bytes.
- Never assume a copied header preserves qform and sform semantics after an
  affine or shape change.
- Never use `[0, 0, 0]` as a silent sentinel for an absent region.
- Never interpret a coordinate, label, shape, intensity, surface, or
  morphometric value scientifically.

## NiBabel I/O preservation checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled I/O implementation forms.** Compare proxy, bounded materialization, and an existing reviewed function only when they preserve the same approved semantics. This makes memory and scaling behavior visible without changing the operation. This adds an implementation review. This cannot resolve an undefined transformation or space.
- **NiBabel I/O Contract.** Audit proxy, dtype, scaling, forms, orientation, frame, labels, memory, write encoding, and round-trip limits. This prevents silent data and coordinate changes. This requires low-level metadata decisions. Malformed or unusual files may still fail.
- **NiBabel I/O Record.** Perform one approved operation once and verify its declared semantics or round trip. This preserves exact value, geometry, and write provenance. Any changed encoding needs new approval. Round-trip checks cannot validate the scientific transformation.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Cross-reader comparison plan.** Add an independent reader or file-format tool for approved cross-checks. This can reveal library-specific interpretation differences. This requires another verified tool. Agreement does not establish scientific correctness.
- **Fixture test plan.** Add an isolated synthetic image or surface fixture with known header and coordinate truth. This can expose API, form-code, scaling, and annotation mistakes. This adds fixture work. This does not validate study-file semantics.
- **Layered preservation report.** Compare source and output at byte, header, and value levels where each is meaningful. This distinguishes binary, metadata, and numerical change. This adds I/O, compute, and interpretation of expected differences. Some valid rewrites are intentionally not byte-identical.

## Checks

- **Positive:** metadata inspection of one NIfTI returns class, proxy, shape,
  dtype, scaling, affine, qform, sform, orientation, units, and memory estimate
  without loading the full array.
- **Write:** one approved derived image is saved to a new path and reloaded
  with explicit value, affine, form-code, dtype, and header checks.
- **Negative:** `which atlas should I use?` routes to a method owner.
- **Broad phrase:** `inspect this NIfTI` does not trigger this adapter.
- **Environment:** missing NiBabel stops without installation.
- **Memory:** a candidate `get_fdata()` copy that would materialize a large
  float64 array is rejected or reopened at Gate 2.
- **Copy:** a byte-preserving request rejects the candidate load-save pattern.
- **Forms:** qform and sform disagreement stops before coordinate reporting or
  writing.
- **Scaling:** post-load header fields are not used to claim that original
  NIfTI scaling was absent; proxy slope, intercept, and unscaled access are
  audited explicitly.
- **Shear:** a sheared affine cannot be silently stored or compared as an
  exact qform representation.
- **Space:** scanner-world coordinates are not labeled MNI.
- **Labels:** noncontiguous atlas IDs do not use positional `roi_id - 1`
  indexing.
- **Absent ROI:** no coordinate is emitted as a silent zero sentinel.
- **FreeSurfer:** `orig_ids=False`, unlabeled vertices, color-table semantics,
  and vertex count are made explicit.
- **Failure:** a write mismatch preserves the new artifact and record without
  overwriting the source or silently changing dtype or forms.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- NiBabel. (n.d.). *Coordinate systems and affines*. https://nipy.org/nibabel/coordinate_systems.html
- NiBabel. (n.d.). *Data-object images*. https://nipy.org/nibabel/reference/nibabel.dataobj_images.html
- NiBabel. (n.d.). *FreeSurfer I/O*. https://nipy.org/nibabel/reference/nibabel.freesurfer.html
- NiBabel. (n.d.). *Image and proxy model*. https://nipy.org/nibabel/nibabel_images.html
- NiBabel. (n.d.). *Image orientation*. https://nipy.org/nibabel/image_orientation.html
- NiBabel. (n.d.). *NiBabel* (Version 5.4.2) [Computer software]. https://nipy.org/nibabel/changelog.html
- NiBabel. (n.d.). *NIfTI forms and headers*. https://nipy.org/nibabel/nifti_images.html
