---
name: dcm2nii
description: >-
  Plans, executes, and verifies one bounded DICOM-to-NIfTI conversion through an
  already available, exact dcm2niix release. Use when the request, or a stage
  coordinator, hands over an explicitly matching conversion handoff. It pins the
  binary and flags, requires an approved DICOM series and output mapping,
  protects source data and identifiers, exposes grouping, scaling, orientation,
  metadata, and compression choices, writes only to a new staged destination
  after two approval gates, and preserves warnings and failed checks. It does
  not install tools, choose series meaning or BIDS labels, deidentify data,
  organize a BIDS tree, overwrite sources, claim clinical or analysis validity,
  upload, share, search, or save outside the approved staged output. Triggers:
  convert DICOM to NIfTI, convert this study with dcm2niix.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: acquisition
  modality: multimodal
  dependencies: ""
  requires: dcm2niix
  gates: converting or restructuring real data
  created: "2026-07-23"
  updated: "2026-11-02"
---

# DICOM to NIfTI

Use dcm2niix as a version-pinned conversion engine without letting command
defaults choose series grouping, scaling, orientation, naming, or privacy.

## Purpose

`dcm2nii` is the Part 3 implementation owner for one bounded DICOM-to-NIfTI
conversion through an exact, already available dcm2niix binary.

It owns:

- preflighting the exact binary, build, help output, defaults state, input
  collection, output destination, and conversion command;
- exposing series merge, ignore, scaling, reorientation, cropping, sidecar,
  naming, compression, and output tradeoffs;
- executing only the user's selected command into a new staged destination;
- preserving the DICOM sources and complete converter output;
- verifying output inventory, NIfTI headers when an approved reader is
  available, sidecar syntax and selected fields, companion counts, warnings,
  and source-to-output correspondence;
- preparing [bids](../bids/SKILL.md) and [bids-organizer](../bids-organizer/SKILL.md) handoffs.

The user owns source inclusion, series identity, intended modality and use,
scientific grouping, merge and split behavior, scaling, orientation and
cropping policy, naming, metadata expectations, privacy and deidentification
policy, BIDS mapping, destination, acceptance criteria, and all scientific or
clinical claims.

[pydicom](../pydicom/SKILL.md) owns bounded DICOM header inspection and metadata-risk mapping.
[bids](../bids/SKILL.md) owns BIDS interpretation and the BIDS Curation Specification.
[bids-organizer](../bids-organizer/SKILL.md) owns approved filesystem implementation after conversion.

The skill name is `dcm2nii`. Its implementation target is modern
`dcm2niix`, not the deprecated legacy `dcm2nii` converter.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md), [pydicom](../pydicom/SKILL.md), [bids](../bids/SKILL.md), or another verified Active
capability may route an explicitly matching conversion handoff from the live
[Skill Map](../../Skill%20Map.md).

Do not activate from:

- `convert this medical image`;
- `make this BIDS`;
- `organize these NIfTIs`;
- `anonymize these DICOMs`;
- `prepare these scans for analysis`;
- broad phrases such as `DICOM`, `NIfTI`, `dcm2niix`, `MRI conversion`, or
  `image export`.

One run covers:

- one approved DICOM source collection;
- one approved series or inseparable conversion batch;
- one exact dcm2niix release and binary hash;
- one selected conversion configuration;
- one new staged destination;
- one execution and verification cycle.

Several series may remain together only when their identities, inclusion,
grouping policy, privacy boundary, output naming, and verification plan are
already approved. Otherwise split the work.

Do not mix source inspection, deidentification policy design, BIDS mapping,
filesystem organization, and analysis into conversion.

## Inputs

Obtain or mark missing:

- exact conversion purpose and intended downstream use;
- exact source directory or approved file-list input;
- redacted source inventory and series map;
- selected series, grouping, and inclusion rules;
- source immutability and protected-access boundary;
- expected modality, frames, echoes, repetitions, diffusion volumes,
  dimensions, voxel spacing, orientation, timing, scaling, and other
  acquisition properties;
- exact installed dcm2niix version and binary path;
- exact output format, compression, filename template, and sidecar policy;
- merge, ignore, scaling, Philips, crop, rotation, trigger-time, verbosity,
  and defaults-file decisions;
- approved non-sensitive output keys;
- new staged destination and collision policy;
- expected output groups and companions;
- independent header, spatial, pixel, metadata, and privacy checks;
- BIDS Curation Specification when BIDS naming or organization is intended;
- stop point.

If source inclusion, series identity, grouping, privacy, or output mapping is
unresolved, return it to the user or the appropriate owner.

## Steps

### 1. Build the Conversion Brief

Show:

| Field | Required content |
|---|---|
| Purpose | Exact conversion question and downstream use |
| Source | Bounded files or directory and protected access |
| Series | Approved identities, inclusion, grouping, and exclusions |
| Converter | Binary, version, build, and release state |
| Configuration | Every selected flag and default |
| Output | New staged root, format, compression, names, and companions |
| Privacy | Source values, filenames, sidecars, logs, permissions, storage, and synchronization |
| Verification | Inventory, headers, spatial state, pixels, metadata, and warnings |
| Exclusions | Install, deidentification, BIDS inference, organization, analysis, upload, and sharing |
| Stop point | Verified or explicitly limited staged conversion record |

Classify the request:

- **Ready for read-only preflight**
- **Needs DICOM inspection**
- **Needs series decision**
- **Needs BIDS mapping**
- **Privacy blocked**
- **Converter unavailable**
- **Verification unavailable**

### 2. Gate 1: approve source access and preflight

Before reading source files or probing the converter, show the brief and ask
The user to approve:

- exact source and series boundary;
- exact content that may be inspected;
- path and value redaction;
- source, scratch, log, and output storage backends, mount state, placeholder
  behavior, and synchronization;
- binary path, version, hash, and local help checks;
- defaults and environment checks;
- proposed flags and their evidence;
- expected output and staged destination;
- verification plan;
- stop point before execution.

Gate 1 authorizes only the displayed read-only preflight.

It does not authorize:

- conversion or any write;
- update checks or other network access;
- installation;
- source modification;
- series, merge, scaling, orientation, crop, naming, metadata, or privacy
  decisions;
- BIDS organization;
- upload, sharing, analysis, or another capability.

Do not infer approval from silence.

### 3. Pin the executable state

Record:

- resolved binary path and SHA-256;
- exact `--version` output;
- release tag, commit, and release date when verifiable;
- platform and architecture;
- exact local help output hash;
- tagged release-source help hash and any difference from the prose manual;
- compression and optional codec support;
- external `pigz` availability and version if `-z y` is proposed;
- defaults-file location, presence, and whether it will be ignored;
- environment variables or wrapper layers that can alter behavior;
- current working directory and output resolution;
- release-note changes relevant to the modality.

Do not run the update-check option. Do not install or download a converter,
codec, wrapper, container, or compressor.

If an exact release cannot be tied to the binary, label the state unverified
and do not execute.

### 4. Build the source and series map

Use an approved [pydicom](../pydicom/SKILL.md) record when available. Otherwise perform only the
minimum approved read-only source inventory.

Record:

| Field | Required content |
|---|---|
| Source key | Non-sensitive stable key |
| Series evidence | Series, study, frame, echo, acquisition, geometry, and transfer-syntax evidence |
| Intended output | user-approved scientific identity |
| Inclusion | Include, exclude, split, combine, or unresolved |
| Expected dimensions | Spatial, temporal, echo, gradient, or frame structure |
| Expected companions | JSON, bval, bvec, or other converter outputs |
| Privacy risk | Filenames, DICOM values, logs, sidecars, or pixels |
| Verification | Source-to-output checks |

Do not infer scientific identity from protocol or series descriptions. Do not
assume a directory is homogeneous.

### 5. Build the option and flag matrix

For every relevant flag or default, show:

| Decision | Options | Scientific or operational consequence | Evidence | The user's selection |
|---|---|---|---|---|
| Sidecar | Exact `-b` mode shown by local help | `y` pairs NIfTI and JSON; `n` emits NIfTI without a sidecar; `o` emits sidecar only; parser-only `i` is disputed and cannot be assumed |
| BIDS-sidecar anonymization | Enabled or disabled | Limited sidecar fields only, not dataset deidentification |
| Filename | Exact safe template | Collision, provenance, and identifier exposure |
| Compression | Exact modes shown by the local build | Toolchain, codec, size, speed, and compatibility |
| Merge | Exact `-m` mode shown by local help | Split, forced merge, or auto behavior; mode `2` sets `isIgnoreSeriesInstanceUID=true` in the tagged parser |
| Ignore | `-i n`, `-i y`, or `-i o` only when shown by local help | Derived, localizer, or 2D data visibility; tagged parser mode `o` keeps non-planar direction-varying localizers and does not ignore derived or 2D images |
| Integer scaling | `-l y`, `-l n`, or `-l o` only when shown by local help | Dynamic-range scaling, uint16-to-int16 behavior, or preservation of original data and type |
| Philips scaling | `-p y`, `-p n`, or `-p o` only when shown by local help | `y` uses precise-float scaling; `n` uses display scaling; `o` ignores variable intensity scaling |
| Crop and rotation | Exact selected behavior | Field of view and orientation |
| Timing metadata | Preserve or exact verified behavior | Timing metadata; do not infer a `-t` override |
| Directory query | Exact `-q` mode shown by local help | `y` reports a query-only count and `l` also lists paths; either prevents conversion; `n` leaves query-only mode off |
| Search depth | Exact `-d` value shown by local help | Recursion boundary; approved source inclusion still comes from the source map |
| Verbosity | Exact `-v` mode shown by local help | Warnings versus value exposure |
| Existing-file behavior | Exact `-w` mode shown by local help | Skip, overwrite, or suffix behavior and collision visibility |
| Defaults | Exact `-g` mode shown by local help | Read, ignore, reset, or write preferences and possible writes outside staging |

Rules:

- Current documentation defines `-x` as crop and rotation control, not
  anonymization.
- The tagged prose manual documents `-t` as saving patient details to text
  notes, while the tagged release source marks the option deprecated and
  comments it out of current help even though the parser still accepts it.
  Preserve this disagreement. Reject every `-t` use in this skill, and do not
  describe it as slice-timing preservation.
- Tagged source help documents `-b o` as sidecar-only. The parser also accepts
  `-b i` as input-only, but that mode is not consistently documented. Do not
  use a disputed sidecar mode unless the exact local help and release evidence
  agree on its behavior.
- `-ba y` limits selected fields in generated BIDS sidecars. It is not DICOM,
  NIfTI, filename, pixel, log, or dataset deidentification.
- Filename specifiers may expose patient name, ID, UIDs, time, folder names,
  descriptions, comments, or other sensitive content. Use only the exact
  approved non-sensitive template.
- Reject `%h`, `%H`, and any template that creates directories or BIDS-like
  hierarchy. In the pinned release, these experimental specifiers can derive
  paths from patient ID or study description, create boilerplate, and perform
  organization that belongs to [bids](../bids/SKILL.md) and [bids-organizer](../bids-organizer/SKILL.md).
- An unspecified output directory may write into the source directory. Always
  use the exact new staged output directory.
- The merge default uses converter logic. In the tagged parser, `-m 2` is the
  automatic mode and sets `isIgnoreSeriesInstanceUID=true`. Never accept it
  silently. The user must explicitly select the mode after reviewing factors that
  could require splitting.
- `-i y` may ignore derived, localizer, or 2D images. In the tagged parser,
  `-i o` sets `isKeepDirectionVaries=true` and
  `isIgnoreDerivedAnd2D=false`, keeping non-planar direction-varying localizers
  without enabling the derived or 2D ignore. The release notes instead
  describe `-i o` as an output-image scaling override, so this mode is
  disputed and must not be used unless the exact binary help and observed
  non-writing evidence resolve it.
- `-l y`, `-l n`, and `-l o` are not equivalent. Tagged help distinguishes
  lossless dynamic-range scaling, uint16-to-int16 conversion, and preservation
  of original data and type. Expose the exact behavior before selection.
- Integer and vendor-specific scaling can change stored values and
  quantitative meaning. In the pinned source, `-p o` is an override that
  ignores variable intensity scaling rather than a synonym for the ordinary
  yes or no modes.
- `-g n` does not prove inherited preferences are ignored. Tagged help uses
  `-g i` to ignore or reset in-memory defaults, while `-g y` and `-g o` can
  write preferences outside staging. Prohibit preference-writing modes and
  require the exact locally verified ignore mechanism before execution.
- Cropping or rotation can change field of view or orientation.
- `-w 1` permits overwriting and is prohibited. Use a new empty staged
  destination and treat any skip, suffix, collision, or existing output as a
  failed preflight or manifest mismatch.
- Terse naming can cause collisions and overwrites. Do not use it.
- The converter may append letters or postfixes to resolve collisions or
  distinguish outputs. Treat every unexpected name as a manifest mismatch.
- `-z` modes are build-dependent. The pinned source can expose external
  `pigz`, optimal `pigz`, internal zlib or miniz, zstd when built, and other
  modes. In tagged help, `y` requests gzip through external `pigz` when
  available, `i` selects the internal compressor, `n` produces uncompressed
  output, `o` uses piped optimal `pigz`, `s` requires a zstd-enabled build,
  and `3` means uncompressed 3D output rather than ordinary uncompressed
  output. Use only the modes printed by the exact local build. Pin any
  external binary or select an internal or uncompressed route.
- Generated JSON is vendor-normalized metadata, not proof that every required
  field is correct or complete.
- The tagged prose manual, tagged source help, and local compiled help are not
  interchangeable. Record their differences and let the local compiled help
  constrain the exact command. Stop if observed behavior still disagrees.

If only one configuration is defensible, explain why. Do not manufacture
alternatives.

### 6. Build the exact command record

Record:

- binary path and hash;
- complete ordered argument list without shell interpolation;
- approved source and output paths;
- ignored-defaults behavior;
- filename template;
- expected outputs;
- runtime, disk, memory, and privacy estimates;
- captured standard output and error policy;
- exit and warning criteria;
- stop conditions.

Never use an unquoted shell string, unresolved glob, command substitution, or
source-derived filename as executable syntax.

The command must:

- identify an explicit staged output;
- avoid patient-detail text notes;
- avoid network update checks;
- avoid source rename mode;
- avoid terse overwrite-prone naming;
- prohibit `-w 1` and require a new empty staged destination;
- preserve every selected flag explicitly;
- leave the source unchanged.

### 7. Preflight the destination and verification

Check:

- staged root is new and outside the source;
- staging, scratch, and logs are local and non-synced unless the user separately
  approved the exact governed external-transfer behavior;
- expected output safely fits available storage;
- no source or destination symlink, alias, or overlap is unresolved;
- output naming is non-sensitive and collision-free;
- expected output groups are listed;
- an approved NIfTI header reader and JSON parser are already available;
- an independent spatial or pixel check is available when required;
- DWI, field-map, multi-echo, PET, ASL, enhanced-DICOM, or other specialist
  checks are assigned;
- partial outputs can remain isolated without touching sources.

If required verification is unavailable, the user may select conversion with
**Pending independent verification** or defer. Do not call it verified.

### 8. Gate 2: The user selects conversion

Ask the user to select:

- exact source and series set;
- exact binary and command record;
- every grouping, scaling, orientation, crop, metadata, naming, compression,
  and privacy behavior;
- staged destination;
- verification criteria;
- failure and partial-output handling;
- selected handoff packets.

Gate 2 authorizes only that exact command and staged destination.

It does not authorize:

- another source, series, flag, binary, destination, or output;
- source mutation;
- install or update check;
- deidentification claim;
- BIDS mapping or organization;
- analysis;
- upload, sharing, release, or another capability.

Do not infer selection from silence.

### 9. Execute once into staging

Before execution:

- recheck source inventory and hashes or selected integrity markers;
- recheck binary and command hashes;
- recheck that the output root is new;
- show the exact command record without sensitive values.

During execution:

- capture version, arguments, exit status, standard output, standard error,
  warnings, runtime, and produced paths;
- redact only values, not warning identities or failure evidence;
- stop on source drift, destination collision, unexpected network action,
  missing dependency, tool mismatch, or write outside the staged root;
- do not retry with different flags automatically.

After execution, preserve all outputs and warnings in staging. Never delete,
move, rename, or overwrite a source.

### 10. Verify source and output correspondence

Verify:

- source inventory and integrity are unchanged;
- actual outputs equal the expected output groups or are marked unexpected;
- every NIfTI file has the expected sidecar and diffusion companions when
  applicable;
- JSON parses and contains the selected expected fields;
- NIfTI dimensions, voxel sizes, data type, qform, sform, affine, orientation,
  units, time dimension, and scaling match the approved expectations when an
  independent reader is available;
- echo, frame, volume, gradient, and timing counts match source evidence;
- bval and bvec counts match diffusion volumes and receive specialist
  orientation review;
- field-map and phase-encoding metadata remain linked to the approved source
  evidence;
- output names contain no disallowed identifiers;
- logs and sidecars remain within the approved privacy boundary;
- converter warnings and release-specific changes remain visible;
- any crop, rotation, reorientation, scaling, merging, splitting, or
  compression is documented;
- no output is labeled BIDS-valid, deidentified, clinically valid,
  analysis-ready, or safe to share.

For spatial or pixel verification, use the approved independent tool or human
review. A successful exit code and readable NIfTI header are insufficient.

Return one status:

- **Converted and verified within stated checks**
- **Converted, pending independent verification**
- **Partial conversion, not promotable**
- **Failed conversion or verification**
- **Blocked before conversion**

### 11. Prepare handoffs

For [bids](../bids/SKILL.md), provide:

- exact converter and command record;
- source series map;
- output inventory and hashes;
- sidecars and companion relationships;
- warnings, version-specific behavior, privacy risks, and unresolved metadata.

For [bids-organizer](../bids-organizer/SKILL.md), provide:

- approved BIDS Curation Specification;
- exact converted source files;
- selected destination mapping;
- conversion and verification records;
- expected byte-preserving copy behavior.

Each handoff requires separate approval and begins the destination's own gates.

## Outputs

Return:

1. **Conversion Brief**
2. **Pinned Binary and Release Record**
3. **Source and Series Map**
4. **Flag and Option Matrix**
5. **Exact Command Record**
6. **Destination and Verification Preflight**
7. **Gate Decisions**
8. **Execution Record**
9. **Output and Companion Inventory**
10. **Spatial, Pixel, Metadata, and Privacy Verification**
11. **Warnings, Failures, and Limits**
12. **Selected Handoff Packets**

The exact staged conversion selected at Gate 2 is the only normal persistent
output.

Before writing:

1. show the source, command, destination, expected files, size, runtime,
   identifier exposure, and no-source-mutation evidence;
2. confirm the output root is new;
3. obtain Gate 2 selection;
4. execute once;
5. verify.

Never install, update, upload, share, release, or promote outputs through this
skill.

## Boundaries

For each run, use:

1. approved institutional privacy, consent, and data-use rules;
2. the exact source acquisition and export record;
3. the exact dcm2niix release source, release notes, and locally compiled help;
4. the selected DICOM and NIfTI standard requirements;
5. the approved BIDS Curation Specification when BIDS is the destination;
6. project conventions that do not conflict with the sources above.

The locally installed binary, `--version` output, and locally compiled help
determine executable behavior. Tagged source help is the next authority for
the pinned release. The tagged prose manual is supporting evidence and may
lag the release source. Documentation for `latest`, `master`, a wrapper, or
another build does not substitute for the exact binary.

If the binary, help, release documentation, and observed behavior disagree,
stop and preserve the mismatch.

Edge cases:

- **No dcm2niix binary**: Return the plan and blocked implementation. Do not
  install it.
- **Version differs from the plan**: Rebuild the flag matrix and repeat Gate 1.
- **Legacy dcm2nii requested**: Disclose that it is a different deprecated
  converter and stop unless the user explicitly scopes a separate adapter.
- **Defaults file exists**: Ignore it through the verified exact mechanism or
  pin and expose every value.
- **Source directory is output default**: Reject and require a new staged root.
- **Patient-detail notes requested**: Reject and hand off to a separately
  scoped protected metadata workflow. The pinned release source marks `-t`
  deprecated and omits it from current help even though the parser accepts it.
- **Anonymization requested through `-x`**: Correct the false premise; `-x`
  controls crop and rotation in the pinned release.
- **BIDS anonymization enabled**: Record its limited sidecar role and continue
  the separate privacy review.
- **Automatic merge selected**: Record it as the user's explicit choice and verify
  every output grouping.
- **Forced merge**: Require evidence that differences in echo, exposure,
  orientation, coil, time, or another factor may be combined.
- **Derived or localizer exclusion**: Preserve an excluded-file manifest and
  scientific rationale.
- **Unexpected output postfix**: Mark a naming or grouping mismatch.
- **Output collision or existing destination**: Stop before execution.
- **Manual, release source, and local help disagree**: Preserve the exact
  mismatch, use no disputed flag, and stop unless the binary behavior can be
  resolved from authoritative release evidence and a bounded non-writing
  preflight.
- **Cloud-synced, shared, network-mounted, or cloud-placeholder output**:
  Treat it as a possible external transfer and require a local non-synced
  protected staging boundary unless the user separately approves the exact
  provider, account, recipients, data flow, and governance basis.
- **Compressed source unsupported**: Return the exact build limitation; do not
  install a codec.
- **External compressor absent**: Use only a separately selected available
  route; do not install it.
- **Constant or quantitative intensities**: Verify scaling explicitly.
- **Oblique, enhanced, mosaic, multi-frame, multi-echo, DCE, PET, ASL, DWI, or
  field-map data**: Require release-specific and modality-specific checks.
- **Equidistant-slice assumption fails**: Preserve the conversion warning and
  do not force NIfTI as a faithful representation.
- **Partial batch**: Mark all outputs not promotable until reconciled.
- **No independent NIfTI reader**: Return pending verification.
- **Privacy issue in name, sidecar, or log**: Quarantine the staged output
  inside the approved protected boundary and stop.
- **Context compaction or model switch**: Reload this skill and approved command
  record before continuing.

## Handoffs

- Use [pydicom](../pydicom/SKILL.md) for DICOM header, sequence, transfer-syntax, and privacy-risk
  inspection.
- Use [bids](../bids/SKILL.md) for BIDS labels, entities, metadata requirements, inheritance,
  provenance, privacy review, and compliance.
- Use [bids-organizer](../bids-organizer/SKILL.md) for approved staged filesystem organization after
  conversion.
- Route modality-specific acquisition interpretation, spatial or pixel
  validation, DWI gradient review, PET timing, ASL context, DICOM
  deidentification and research analysis to their approved research owners.
  Diagnostic viewing requires qualified human clinical expertise outside ASTORIA.
- If an invoking companion routed this capability and the destination remains
  unclear, return that unresolved boundary to the invoking companion. If no
  companion invoked it, stop at this capability boundary and offer
  [research-companion](../../skills/research-companion/SKILL.md) only as an optional public routing entry.

This skill does not convert RTSTRUCT, RTDOSE, SEG, ultrasound, CT, PET, or
another object merely because an old source table says support exists. Verify
the exact release, object class, intended output, and specialist requirements
for every non-routine object.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Li, X., Morgan, P. S., Ashburner, J., Smith, J., & Rorden, C. (2016). The first step for neuroimaging data analysis: DICOM to NIfTI conversion. *Journal of Neuroscience Methods, 264*. https://doi.org/10.1016/j.jneumeth.2016.03.001
- rordenlab. (2026). *dcm2niix* (Version v1.0.20260416) [Computer software]. GitHub. https://github.com/rordenlab/dcm2niix/releases/tag/v1.0.20260416
