---
name: pydicom
description: >-
  Plans, performs, and verifies one bounded DICOM inspection or explicitly
  approved staged metadata transformation through an already available, exact
  pydicom version. Use when the request, or a part coordinator, hands over an
  explicitly matching DICOM operation. It pins the DICOM and library state,
  minimizes identifiable-data exposure, maps tags, sequences, transfer syntax,
  pixel requirements, and referential integrity, and executes only the
  user-selected operation after two approval gates. It does not install
  packages, browse PACS, choose deidentification policy, claim anonymity or
  diagnostic validity, overwrite source data, convert DICOM to NIfTI or ordinary
  images, organize BIDS files, analyze images, upload, share, search, or save
  outside the approved staged output. Triggers: inspect these DICOM headers,
  DICOM metadata check.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: acquisition
  modality: multimodal
  dependencies: ""
  requires: Python, pydicom
  gates: converting or restructuring real data
  created: "2026-07-23"
  updated: "2026-11-02"
---

# pydicom

Use pydicom as a bounded DICOM implementation adapter without turning a Python
library or example script into a privacy, conversion, or scientific workflow.

## Purpose

`pydicom` is the Part 3 canonical owner for one version-pinned pydicom
operation on a bounded DICOM file or collection:

- privacy-minimized header and file-meta inspection;
- data-element, sequence, value-representation, multiplicity, character-set,
  and transfer-syntax review;
- separately approved pixel-decoding or encoding feasibility checks;
- implementation of an exact, externally approved metadata action table into
  a new staged destination;
- verification of source preservation, output readability, changed elements,
  UID and reference consistency, and declared operation limits.

The user owns the purpose, source boundary, scientific meaning, selected files,
permitted identifiers, selected DICOM edition, transformation policy,
deidentification profile and options, UID policy, date policy, private-element
policy, pixel policy, output destination, acceptance criteria, release or
sharing decision, and all scientific and clinical claims.

[bids](../bids/SKILL.md) owns version-pinned BIDS mapping, metadata, provenance, privacy
registers, and compliance specifications. [dcm2nii](../dcm2nii/SKILL.md) owns DICOM-to-NIfTI
conversion. [bids-organizer](../bids-organizer/SKILL.md) owns approved filesystem
organization into a staged BIDS tree. Part 4 capabilities own image analysis.
An institutional privacy, governance, or qualified DICOM owner must define any
deidentification policy before this skill implements it.

This skill is a software adapter. It does not make pydicom a DICOM conformance
validator, a deidentifier, a PACS client, a diagnostic viewer, or a scientific
method.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an
explicitly matching operation from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `convert these DICOMs to NIfTI`;
- `make this BIDS`;
- `anonymize everything`;
- `download this study from PACS`;
- `show me the scan`;
- broad phrases such as `medical images`, `DICOM`, `metadata`, `MRI files`, or
  `image processing`.

One run covers:

- one exact file, bounded file list, or approved collection root;
- one operation family: inspection, pixel feasibility, or staged metadata
  transformation;
- one exact pydicom version and one declared DICOM standard edition;
- one access, privacy, output, and verification boundary.

Do not combine unrelated patients, projects, modalities, destinations,
transformation policies, or release purposes merely because one command can
iterate over them.

An inspection may prepare a transformation plan. It does not authorize the
transformation. A transformation begins only after Gate 2 selects the complete
action table, destination, and verification plan.

## Inputs

Obtain or mark missing:

- exact operation and purpose;
- exact source files or bounded root and access permission;
- source immutability requirement and backup state;
- whether headers, file meta, sequences, private elements, pixel data,
  overlays, waveforms, structured content, encapsulated documents, or only
  named tags may be read;
- permitted display and output values, including redaction rules;
- expected modalities, SOP Classes, transfer syntaxes, and file count;
- selected DICOM edition;
- already available Python and pydicom versions;
- already available pixel decoders or encoders when pixel work is requested;
- transformation action table, UID map, date policy, private-element policy,
  and pixel policy when mutation is requested;
- staged destination, collision policy, storage budget, and acceptance checks;
- BIDS Curation Specification when the operation supports BIDS work;
- confirmatory, exploratory, operational, or governance status;
- exact stop point.

If the operation, access boundary, source set, privacy boundary, or destination
for a requested write is unresolved, stop.

## Steps

### 1. Build the DICOM Operation Brief

Show:

| Field | Required content |
|---|---|
| Purpose | Exact inspection or staged-transformation question |
| Source | Explicit files or bounded root |
| Unit | File, instance, series, study, subject, or declared collection |
| Operation family | Inspection, pixel feasibility, or transformation |
| Permitted content | Exact tags, sequences, file meta, private elements, pixels, and embedded content |
| Privacy boundary | Identifiers that may be accessed, displayed, logged, retained, or synchronized |
| Standard state | DICOM edition and applicable confidentiality profile |
| Tool state | Python, pydicom, decoder, encoder, and validation modes |
| Output | Chat record, staged files, manifest, or handoff |
| Exclusions | PACS, install, conversion, analysis, upload, sharing, and other out-of-scope work |
| Stop point | Exact artifact or blocked result |

Classify the request as:

- **Ready for bounded inspection**
- **Ready for option comparison**
- **Blocked by access or privacy**
- **Blocked by missing policy**
- **Blocked by tool state**
- **Needs another owner**

### 2. Gate 1: approve access and inspection

Before opening a DICOM file, show the brief and ask the user to approve:

- source files and collection boundary;
- content that may be read;
- values that may be displayed or recorded;
- source, scratch, log, and proposed output storage and synchronization
  behavior;
- pydicom and DICOM versions to verify;
- read-only checks;
- whether pixel payloads may be accessed;
- scratch and log behavior;
- intended transformation question, if any.

Gate 1 authorizes only the displayed read-only access, environment preflight,
inventory, and inspection.

It does not authorize:

- package installation;
- source mutation;
- broad recursion outside the listed root;
- pixel decoding unless explicitly included;
- full metadata printing;
- a transformation, deidentification action, conversion, upload, sharing, or
  persistent output.

Do not infer approval from silence.

### 3. Pin the tool and standard state

Record:

- Python implementation and version;
- pydicom version, release tag, and documentation URL;
- DICOM dictionary edition embedded in that pydicom release;
- selected DICOM standard edition and applicable parts;
- reading and writing validation modes;
- `future_behavior` state when relevant;
- requested API and its exact signature;
- source transfer syntaxes;
- installed decoder and encoder plugins and versions;
- known deprecations, default mutations, and version conflicts.

Do not install missing packages or codecs. If pydicom or a required plugin is
unavailable, return **Blocked implementation** with the exact missing
capability.

### 4. Inventory without exposing content

Before parsing:

- resolve only the approved paths;
- record count, size, extension distribution, and non-file entries without
  assuming that DICOM files end in `.dcm`;
- detect duplicate paths, symlinks, destination overlap, and filename
  collisions;
- confirm that the source and staged destination are different;
- keep scratch and logs outside the source tree;
- decide how parse failures and non-DICOM files remain visible.
- identify local, cloud-sync, shared, network-mount, and placeholder behavior
  for source, scratch, logs, and any proposed output.

Do not print filenames when they contain identifiers. Use a non-sensitive
operation key in the record.

### 5. Inspect headers and structure minimally

Use the least-content read that answers the approved question.

Prefer:

- `stop_before_pixels=True` when pixel payloads are not needed;
- `specific_tags` for a small named tag set;
- `defer_size` when large values need not be loaded;
- `force=False` by default;
- redacted presence, VR, VM, length, and consistency summaries instead of
  values;
- recursive sequence inspection only when the approved question requires it.

Record:

| Field | Required content |
|---|---|
| Operation key | Non-sensitive stable identifier |
| Parse status | Parsed, invalid preamble or file meta, truncated, non-DICOM, or unresolved |
| SOP identity | Class and instance consistency without exposing unnecessary values |
| File meta | Transfer syntax, media-storage identity, implementation fields, and conflicts |
| Encoding | VR, byte order, character set, and observed anomalies |
| Structure | Required named elements, sequences, private creators, and embedded content |
| Acquisition mapping | Approved tags needed by BIDS, conversion, or acquisition review |
| Privacy flags | Direct identifiers, dates, free text, UIDs, private values, pixels, overlays, or documents |
| Limit | What was not read or cannot be established |

Do not use `force=True` to convert a parse failure into a valid-DICOM claim.
If a rescue read is scientifically necessary, present it as a separate option
and preserve the original failure.

### 6. Map pixel and transfer-syntax requirements

Access pixel data only when Gate 1 included it and the question cannot be
answered from headers.

Map:

- transfer syntax UID and encapsulation state;
- samples, rows, columns, frames, photometric interpretation, planar
  configuration, bit allocation, stored bits, high bit, representation, and
  related consistency;
- decoder or encoder and exact version;
- output color-space behavior;
- memory estimate and bounded frame plan;
- lossy or lossless status and scientific consequences;
- default SOP Instance UID behavior;
- before and after pixel checksum or approved equivalence check;
- independent verification method.

Pydicom's own documentation warns that decoder output needs independent
verification. A successful `pixel_array` access is not proof that pixel values,
geometry, color, intensity, or diagnostic meaning are correct.

Do not normalize pixels to 8-bit, window an image, stack slices, decompress,
compress, or export an ordinary image. This skill may inspect feasibility and
risks for a separately owned pixel operation, but it does not execute that
  operation. DICOM-to-NIfTI belongs to [dcm2nii](../dcm2nii/SKILL.md).

### 7. Build a transformation action table

For a requested metadata transformation, require:

| Field | Required content |
|---|---|
| Tag or structure | Numeric tag, keyword, sequence path, file meta, preamble, private block, overlay, or pixel content |
| Source state | Presence, VR, VM, and redacted value class |
| Action | Keep, remove, zero, replace, clean, UID-map, date-map, or inspect |
| Authority | Exact policy, DICOM profile action, BIDS specification, or the user decision |
| Replacement rule | Deterministic source, type, units, format, and collision handling |
| Cross-file scope | Instance, series, study, subject, collection, or external map |
| Referential integrity | Every linked UID or reference that must change together |
| Scientific consequence | Information lost, retained, or transformed |
| Privacy consequence | Risk reduced, retained, or unresolved |
| Verification | Exact post-write check |

Never derive a deidentification policy from a short tag list. The DICOM Basic
Application Level Confidentiality Profile and selected options require
element-specific actions, recursive sequence handling, UID consistency, file
meta and preamble handling, private-element decisions, pixel and embedded
content review, and a documented conformance boundary.

If the approved action table is incomplete for any encountered content, mark
the operation blocked. Do not silently keep, drop, blank, or regenerate it.

### 8. Compare operation options

Present only applicable options:

- stop after the redacted inspection record;
- inspect a narrower or broader approved tag set;
- authorize bounded pixel feasibility;
- repair the action table through its policy owner;
- dry-run the selected transformation without writing;
- write the exact transformation to a new staged destination;
- prepare a [bids](../bids/SKILL.md), [dcm2nii](../dcm2nii/SKILL.md), [bids-organizer](../bids-organizer/SKILL.md), privacy, or Part 4
  handoff;
- defer because the tool, policy, source, or verification state is inadequate.

For each option, expose privacy, information-loss, referential-integrity,
compatibility, runtime, storage, and verification tradeoffs.

Do not rank options by convenience or installed-package availability.

### 9. Gate 2: The user selects the operation

Ask the user to select:

- exact operation and source set;
- permitted output values;
- action table and policy authority, if writing;
- UID, date, private-element, embedded-content, and pixel rules;
- pydicom and plugin versions;
- staged destination and collision behavior;
- verification and acceptance criteria;
- selected handoff packets.

Gate 2 authorizes only the displayed operation.

It does not authorize:

- a different file, collection, action table, destination, or tool version;
- source overwrite;
- installation;
- PACS access;
- BIDS organization;
- DICOM-to-NIfTI or ordinary-image conversion;
- scientific analysis;
- upload, sharing, release, or a claim of deidentification.

Do not infer selection from silence.

### 10. Execute the selected operation

For inspection:

- access only the selected paths and elements;
- keep displayed values within the approved redaction boundary;
- preserve failures and unknowns;
- produce no persistent file unless separately approved.

For transformation:

- recheck source and destination paths;
- record source hashes before writing;
- create only new staged outputs;
- refuse collisions unless the selected plan resolves them;
- use explicit no-overwrite behavior and the selected file-format enforcement;
- apply the exact action table recursively and consistently;
- make UID and date mappings deterministic within the approved scope;
- preserve a non-sensitive operation manifest;
- stop on an unhandled element, invalid replacement, parse error, write error,
  or verification failure;
- never delete or overwrite the source.

Do not use a candidate helper script, generic `Dataset.save_as()` example, or
automatic package default as the transformation specification.

### 11. Verify the result

Verify:

- source paths and hashes are unchanged;
- expected and actual file counts agree;
- every output reparses under the pinned pydicom state;
- file meta, SOP Class, SOP Instance, transfer syntax, and dataset encoding are
  internally consistent;
- every selected action occurred and no unselected action occurred;
- nested sequences and cross-instance references obey the selected map;
- private elements, UIDs, dates, file meta, preamble, overlays, embedded
  content, and pixels match the approved policy;
- `PatientIdentityRemoved`, deidentification-method fields, and DICOMDIR
  content match the selected profile and operation when applicable;
- pixel operations pass the selected independent check;
- parse warnings, validation limits, and failures remain visible;
- a separate DICOM conformance validator or expert review remains identified
  when needed;
- outputs stay inside the approved staged destination.

Return **Failed verification** when any required check fails. Preserve the
source and staged evidence. Do not promote the output.

## Outputs

Return:

1. **DICOM Operation Brief**
2. **Pinned Tool and Standard State**
3. **Privacy-Minimized Inventory**
4. **Header and Structure Map**
5. **Pixel and Transfer-Syntax Record**, when applicable
6. **Transformation Action Table**, when applicable
7. **Operation Options**
8. **Gate Decisions**
9. **Execution Manifest**, when selected
10. **Verification Record**
11. **Unresolved Risks and Limits**
12. **Selected Handoff Packets**

Do not expose raw identifiers in chat or durable output unless the user explicitly
approved the exact values and destination.

Default to ephemeral inspection. Report findings in the current task's requested form or under the recipient's existing reporting policy.

Before any persistent output:

1. show the exact destination, files, count, size, identifiers, overwrite
   behavior, and retention plan;
2. show source-preservation and rollback evidence;
3. ask for separate approval unless Gate 2 already approved that exact staged
   output;
4. write only the approved destination;
5. verify afterward.

Never install a package, connect to PACS, use a remote service, upload, share,
or release data through this skill.

## Boundaries

For each operation, use:

1. the approved institutional policy, consent, data-use agreement, and
   governance decision;
2. the exact selected DICOM standard edition, including PS3.15 when
   confidentiality is relevant;
3. the exact pydicom release documentation and API behavior;
4. verified transfer-syntax decoder or encoder documentation;
5. the source dataset and its acquisition or export documentation;
6. project conventions that do not conflict with the authorities above.

The pydicom data dictionary is a versioned implementation aid, not the whole
DICOM standard. Pydicom value validation is incomplete and does not establish
IOD, privacy, clinical, or scientific conformance.

If documentation, implementation behavior, source files, and policy disagree,
preserve the disagreement for the user. Do not choose the convenient interpretation.

This skill may implement an already approved deidentification action table. It
does not design that policy and never declares data anonymous, deidentified,
safe, compliant, releasable, or shareable on pydicom output alone.

Required external decisions include:

- purpose, recipients, jurisdiction, consent, and data-use constraints;
- exact DICOM confidentiality profile and options;
- private-element retention basis;
- UID and longitudinal-date strategy;
- pixel, face, burned-in text, overlay, waveform, structured-report,
  encapsulated-document, DICOMDIR, specimen, and other modality-specific
  handling;
- linkage and reidentification controls;
- residual-risk review and release authorization.

Constant replacement values, removal of person-name tags, or
`remove_private_tags()` alone are not a complete deidentification process.

Edge cases:

- **No pydicom**: Return the plan and blocked implementation. Do not install it.
- **Compressed transfer syntax without decoder**: Report the exact missing
  decode capability and stop before pixels.
- **No `.dcm` extension**: Do not exclude the file solely by extension; use the
  approved inventory and conservative parse checks.
- **Missing file-meta header**: Preserve the parse failure. Do not use
  `force=True` as proof of validity.
- **Truncated file**: Stop and preserve the failure; do not write a repaired
  source.
- **Unknown private element**: Treat it as unknown and potentially sensitive.
- **Nested sequence**: Apply or verify the action recursively according to the
  selected policy.
- **UID replacement**: Maintain referential integrity across the complete
  approved scope or block the write.
- **Date shift**: Use one approved, deterministic subject-level mapping and
  verify temporal relationships; do not invent a random offset per file.
- **Burned-in annotation or recognizable face**: Require the selected pixel
  policy and independent human or validated-tool review.
- **Structured report, waveform, encapsulated document, overlay, or graphics**:
  Do not apply an image-only action table.
- **Lossy source**: Preserve the lossy state and scientific implication.
- **Decompression or compression**: Record that pydicom 3.0 defaults may
  generate a new SOP Instance UID and may alter pixel representation; require
  the selected UID and independent pixel-verification plan.
- **Multiple decoder plugins**: Pin the selected plugin and verify output;
  first-success behavior is not scientific validation.
- **Source and destination overlap**: Stop.
- **Cloud-synced, shared, network-mounted, or cloud-placeholder output**:
  Treat it as a possible external transfer and require a local non-synced
  protected destination unless the user separately approves the exact governed
  data flow.
- **Output collision**: Stop unless the exact collision action was selected.
- **Successful save and reload**: Do not treat either as DICOM conformance.
  In pydicom 3.0.2, `save_as()` defaults do not enforce the DICOM File Format
  and permit overwrite unless explicitly controlled.
- **Partial batch failure**: Preserve the manifest and staged failures; do not
  call the collection complete.
- **Deidentification requested without a full action table**: Return
  **Blocked by missing policy**.
- **Share requested after a clean check**: Require separate governance and
  release approval. This skill cannot authorize sharing.
- **Context compaction or model switch**: Reload this skill and the approved
  brief before continuing.

## Handoffs

- Use [bids](../bids/SKILL.md) for BIDS layer, entity, filename, metadata-inheritance,
  provenance, privacy-register, and compliance decisions.
- Use [dcm2nii](../dcm2nii/SKILL.md) for DICOM-to-NIfTI conversion and sidecar extraction.
- Use [bids-organizer](../bids-organizer/SKILL.md) for approved file organization, copying,
  renaming, and staged BIDS-tree creation.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) for prospective task-fMRI event and schedule
  meaning.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when participant, session, acquisition, site, or
  study structure remains unresolved.
- Route acquisition-protocol design, DICOM networking or PACS, institutional
  deidentification policy, conformance validation, and research image analysis
  to their appropriate research owners. Diagnostic viewing requires qualified
  human clinical expertise outside ASTORIA.
- If an invoking companion routed this capability and the destination remains
  unclear, return that unresolved boundary to the invoking companion. If no
  companion invoked it, stop at this capability boundary and offer
  [research-companion](../../skills/research-companion/SKILL.md) only as an optional public routing entry.

Each destination begins its own workflow and gates. pydicom approval does not
authorize another capability.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- DICOM Standards Committee. (2026). *DICOM PS3.15* (2026c ed.). https://dicom.nema.org/medical/dicom/current/output/html/part15.html
- *pydicom* (Version 3.0.2) [Computer software]. (2026). https://pydicom.github.io/pydicom/stable/
