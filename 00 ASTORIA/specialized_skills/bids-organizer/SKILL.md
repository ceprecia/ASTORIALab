---
name: bids-organizer
description: >-
  Implements and verifies one approved BIDS Curation Specification as a new
  staged filesystem tree. Use when the request, or a part coordinator, hands over an
  explicitly matching implementation handoff. It preflights an exact
  source-to-destination manifest, preserves source files, exposes collisions and
  privacy risks, copies or writes only user-selected items after two approval
  gates, and verifies paths, bytes, hashes, companions, JSON, TSV, and
  provenance. It does not infer scientific labels, design a BIDS mapping,
  convert DICOM or EEG, install tools, overwrite or delete sources, interpret
  validator findings, analyze data, upload, share, release, search, or save
  outside the approved staged destination. Triggers: build the BIDS tree from
  the spec, organize files into BIDS.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: acquisition
  modality: multimodal
  dependencies: ""
  requires: an approved BIDS Curation Specification; bids-validator
  gates: converting or restructuring real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# BIDS Organizer

Implement an approved BIDS curation plan as a staged tree without turning
filesystem convenience into scientific or privacy decisions.

## Purpose

`bids-organizer` is the Part 3 implementation owner for transforming one
complete, approved BIDS Curation Specification into one new staged filesystem
tree.

It owns:

- resolving and preflighting an exact source-to-destination manifest;
- creating the approved directory structure;
- copying approved source or converted files without altering their bytes;
- assigning only the approved filenames and paths;
- writing exact approved JSON, TSV, README, and other text content;
- keeping linked companions together;
- preserving sources and recording every operation;
- verifying output paths, file counts, bytes, hashes, structured-text syntax,
  companion sets, permissions, and manifest agreement;
- preparing a separate [bids](../bids/SKILL.md) validation handoff.

The user owns the dataset purpose, BIDS release, dataset layer, scientific labels,
subject and session identities, task and acquisition meaning, run identity,
source-to-output mapping, metadata values, missing-data actions, privacy and
deidentification decisions, exclusions, destination, release decision, and all
scientific claims.

[bids](../bids/SKILL.md) owns BIDS interpretation, mapping, metadata inheritance, provenance
requirements, privacy review, and validator interpretation. [pydicom](../pydicom/SKILL.md) owns
bounded DICOM inspection or approved metadata transformation. [dcm2nii](../dcm2nii/SKILL.md) owns
DICOM-to-NIfTI conversion and sidecar extraction.

This skill performs selected filesystem work. It does not decide what a BIDS
dataset means or certify that one is valid, complete, private, or safe to
share.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md), [bids](../bids/SKILL.md), or another verified Active capability may
route an explicitly matching implementation handoff from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `make this BIDS`;
- `convert my DICOMs`;
- `organize this neuroimaging folder`;
- `validate this BIDS dataset`;
- `upload this dataset`;
- broad phrases such as `bidsify`, `BIDS conversion`, `raw data`, `rename
  files`, or `dataset organization`.

Those requests first need the appropriate design, conversion, privacy, or
validation owner.

One run covers:

- one approved BIDS Curation Specification;
- one bounded source set;
- one new staged destination root;
- one exact operation manifest;
- one execution and verification cycle.

Do not combine datasets, BIDS releases, source policies, privacy boundaries,
destinations, or unrelated transformation manifests.

The destination must be a new staging root or an exact empty project-owned
staging root that the user explicitly selected. Never treat an existing BIDS
dataset as an overwrite target.

## Inputs

Require a complete specification that records:

- exact BIDS release and dataset layer;
- source paths or non-sensitive source keys;
- destination root and every relative destination path;
- operation for each item;
- approved entities, labels, suffixes, extensions, and entity order;
- exact generated JSON, TSV, README, and other text content;
- source, companion, inheritance, and provenance relationships;
- expected hashes or byte-preservation rules;
- privacy and access boundary;
- collision, case, symlink, permission, and failure policy;
- expected file and directory counts;
- post-write structural checks;
- separate BIDS validation handoff;
- stop point.

An approved [bids](../bids/SKILL.md) BIDS Curation Specification is the normal source. A
user-supplied equivalent may be used only after its completeness and BIDS
version are verified.

If the organizer would need to infer a subject, session, task, acquisition,
direction, run, echo, part, reconstruction, space, description, datatype,
suffix, or metadata value, return the missing decision to the user or [bids](../bids/SKILL.md).

## Steps

### 1. Build the Organization Brief

Show:

| Field | Required content |
|---|---|
| Specification | Exact source, version, and approval state |
| BIDS state | Release, layer, modalities, and extensions |
| Source set | Bounded files, roots, count, size, and access |
| Destination | Exact new staged root |
| Operations | Directory creates, byte-preserving copies, and exact text writes |
| Generated content | Approved content and encoding |
| Privacy boundary | Identifiers, sensitive values, permissions, storage and sync behavior, logs, and scratch |
| Exclusions | Conversion, inference, source mutation, validation interpretation, analysis, upload, and sharing |
| Verification | Counts, paths, bytes, hashes, companions, syntax, and provenance |
| Stop point | Staged tree plus verification and handoff record |

Classify the handoff:

- **Ready for manifest preflight**
- **Incomplete specification**
- **Source mismatch**
- **Destination conflict**
- **Privacy blocked**
- **Needs conversion**
- **Needs BIDS interpretation**

### 2. Gate 1: approve preflight

Before inspecting sources or the destination, show the brief and ask the user to
approve:

- exact source paths and read boundary;
- exact proposed destination;
- specification and manifest to inspect;
- count, size, free-space, permission, link, collision, and hash checks;
- values that may appear in chat or logs;
- source, staging, scratch, and log storage backends, mount state, and
  synchronization behavior;
- scratch location and cleanup boundary;
- exact stop point before writing.

Gate 1 authorizes only read-only preflight and a dry-run manifest.

It does not authorize:

- creating directories or files;
- copying, moving, renaming, deleting, overwriting, linking, or editing;
- conversion;
- label or metadata inference;
- package installation;
- validator execution;
- upload, sharing, release, analysis, or another capability.

Do not infer approval from silence.

### 3. Pin the specification state

Record:

- BIDS release, schema, and accepted extension state;
- upstream specification hash or complete chat-state identifier;
- source inventory state;
- destination filesystem and case-sensitivity behavior;
- text encodings and line-ending requirements selected by the specification;
- available implementation tools;
- exact verification tools;
- any drift since approval.

If the BIDS release, source set, destination, or approved specification changed,
return to Gate 1.

### 4. Build the dry-run operation manifest

For every item, record:

| Field | Required content |
|---|---|
| Operation ID | Non-sensitive stable key |
| Source | Exact path or generated-content record |
| Source state | Type, size, hash, and permission |
| Operation | Create directory, copy bytes, or write exact text |
| Destination | Exact path beneath the staging root |
| BIDS mapping | Approved datatype, entities, suffix, and extension |
| Companion group | Image, JSON, bval, bvec, events, channels, scans, or other linked set |
| Expected output | Size, hash, syntax, or exact content hash |
| Privacy class | Approved handling and access |
| Provenance | Upstream mapping and transformation source |
| Verification | Exact post-write checks |

Rules:

- resolve every source and destination path before writing;
- reject absolute or parent-traversal paths inside relative manifest fields;
- reject duplicate, case-colliding, Unicode-normalization-colliding, reserved,
  or overlong destination paths;
- reject source and destination overlap;
- reject symlinks, hard links, special files, sockets, devices, and unresolved
  aliases unless the user approved an exact treatment;
- preserve companion relationships explicitly;
- do not use filename heuristics to assign BIDS meaning;
- do not scan for additional modalities or expand the source set;
- do not create a catch-all `misc`, review, or quarantine folder inside the
  BIDS dataset unless the approved BIDS specification defines it lawfully;
- do not put audit logs, cache files, timestamps, temporary files, or manifests
  inside the BIDS root unless the selected release and specification explicitly
  allow the exact file.

### 5. Preflight resources and source integrity

Check:

- every source exists, is permitted, and matches its approved size and hash;
- every generated-content record has exact content, encoding, delimiter,
  quoting, newline, and missing-value behavior;
- destination parent is allowed and writable;
- destination root does not exist, or is the exact approved empty staging root;
- source, staging, scratch, and log paths have identified local, cloud-sync,
  shared, network-mount, and placeholder behavior;
- the staging, scratch, and log boundary is local and non-synced unless the user
  separately approved the exact governed external-transfer behavior;
- free space safely exceeds the bounded output estimate;
- expected counts agree across the specification, manifest, and source;
- source permissions and sensitive-data boundary are understood;
- no operation mutates, moves, deletes, or overwrites a source;
- rollback means abandoning the new staging root, not restoring altered source
  data.

If any check fails, return **Blocked preflight** with the exact manifest rows.

### 6. Verify generated structured content before writing

For each generated file:

- JSON must parse as JSON, not as a language-specific dictionary
  representation;
- TSV must have the exact approved columns, ordering, row count, delimiter,
  quoting, escaping, encoding, and missing values;
- README content and extension must match the selected BIDS release and
  approved specification;
- filenames and contents must not expose identifiers beyond the approved
  privacy boundary;
- metadata values must come from the approved specification, not organizer
  defaults;
- the declared BIDS version must equal the selected release;
- links and provenance references must use approved relative paths.

This skill verifies syntax and manifest agreement. [bids](../bids/SKILL.md) remains the owner
of normative BIDS meaning.

### 7. Present implementation options

Show only applicable choices:

- correct named manifest defects and repeat preflight;
- narrow or split the source set;
- choose a new empty staging destination;
- stop after the dry-run manifest;
- execute the exact complete manifest;
- prepare a conversion, [pydicom](../pydicom/SKILL.md), privacy, or [bids](../bids/SKILL.md) handoff;
- defer because required evidence or authority is missing.

This is a mostly fixed-route implementation skill. Do not invent competing
organization plans after [bids](../bids/SKILL.md) has supplied one approved mapping.

For any real option, expose time, storage, privacy, collision, partial-failure,
and verification implications.

### 8. Gate 2: The user selects the implementation

Ask the user to select:

- exact manifest and its hash;
- exact staged destination;
- generated content;
- permitted source reads and output permissions;
- failure and partial-output handling;
- verification plan;
- selected handoff packets.

Gate 2 authorizes only the displayed manifest at the displayed destination.

It does not authorize:

- a changed source, mapping, filename, metadata value, destination, or BIDS
  release;
- source overwrite, move, rename, deletion, or permission change;
- inferred or additional files;
- conversion;
- install;
- validator interpretation;
- upload, sharing, release, analysis, or another capability.

Do not infer selection from silence.

### 9. Execute into the staged destination

Implementation rules:

- recheck the manifest hash and destination immediately before writing;
- create only the approved staging root and listed directories;
- copy binary and supplied text sources byte for byte;
- write generated text from the exact approved content;
- use exclusive creation and fail on every existing destination;
- never follow a source or destination link implicitly;
- preserve or set permissions exactly as approved;
- record completion status per operation;
- stop at the first unhandled collision, source drift, write error, permission
  error, or verification failure;
- never delete a partial staging tree automatically;
- never change a source.

Do not shell-expand unresolved globs or build operations from untrusted
filenames. Use the resolved manifest.

### 10. Verify the staged tree

Verify:

- source hashes and permissions remain unchanged;
- actual directories and files exactly equal the manifest;
- no extra temporary, hidden, audit, cache, or platform files exist;
- copied files match expected byte size and hash;
- generated files match approved content hashes;
- JSON and TSV syntax still parses;
- every companion group is complete and consistently named;
- case and Unicode normalization collisions are absent;
- all paths remain beneath the staged root;
- output permissions match the privacy plan;
- failures and partial outputs remain visible;
- no conversion, inference, validation claim, upload, sharing, or analysis
  occurred.

Return one status:

- **Staged and structurally verified**
- **Partial staging, not promotable**
- **Failed verification**
- **Blocked before write**

Do not label the tree BIDS-valid, deidentified, complete, analysis-ready, or
release-ready.

### 11. Prepare the BIDS validation handoff

Provide [bids](../bids/SKILL.md):

- exact BIDS release and schema;
- staged root;
- source-to-destination manifest;
- generated-content hashes;
- operation and verification records;
- known warnings, unresolved metadata, exclusions, and privacy risks;
- exact local validator availability, if already known;
- requested read-only validation boundary.

Starting [bids](../bids/SKILL.md) requires separate approval and begins its own gates.

## Outputs

Return:

1. **Organization Brief**
2. **Pinned Specification State**
3. **Dry-Run Operation Manifest**
4. **Source Integrity and Resource Preflight**
5. **Generated-Content Validation**
6. **Implementation Options**
7. **Gate Decisions**
8. **Execution Record**
9. **Staged-Tree Verification**
10. **Privacy and Residual-Risk Record**
11. **BIDS Validation Handoff**
12. **Blocked or Unresolved Items**

The approved staged tree is the only normal persistent output.

Before writing:

1. show the exact destination, manifest, file count, byte estimate, generated
   content, permissions, storage and synchronization behavior, and
   no-overwrite behavior;
2. verify the source and destination are distinct;
3. obtain Gate 2 approval for that exact state;
4. write only the new staged root;
5. verify it.

This skill never installs software, starts a network connection, uploads,
shares, releases, or promotes a staged tree into a production or repository
location.

## Boundaries

- **No approved BIDS specification**: Route to [bids](../bids/SKILL.md) and stop.
- **Raw DICOM needs conversion**: Route to [dcm2nii](../dcm2nii/SKILL.md); do not hide
  conversion inside organization.
- **DICOM metadata question**: Route to [pydicom](../pydicom/SKILL.md).
- **Existing destination**: Stop and require a new explicit staging root.
- **Empty approved destination exists**: Verify emptiness, identity, and
  permission again at Gate 2; fail if any item appears.
- **Source inside destination or destination inside source**: Stop.
- **Cloud-synced, shared, network-mounted, or cloud-placeholder path**: Treat
  access or staging as a possible external transfer. Use a local non-synced
  protected boundary unless the user separately approves the exact provider,
  account, recipients, data flow, governance basis, and files.
- **Duplicate destination**: Return the scientific identity or manifest
  conflict; do not add `run` or another entity automatically.
- **Case-only or Unicode-normalization collision**: Stop before writing.
- **Missing companion**: Mark the group incomplete; do not copy a partial set
  as complete.
- **Symlink or hard link**: Stop unless the exact safe treatment is selected.
- **Broken source link**: Preserve the failure; do not search elsewhere.
- **Source changed after Gate 1**: Rebuild the manifest and repeat Gate 1.
- **Insufficient storage**: Stop before creating the staging root.
- **Generated JSON is a Python dictionary string**: Reject it as invalid JSON.
- **README absent from a BIDS 1.11.1 plan**: Return the specification defect to
  [bids](../bids/SKILL.md).
- **Partial write**: Mark the staging root not promotable and preserve the
  operation record; do not delete or continue blindly.
- **Unexpected platform file**: Mark the staged tree failed until removed
  through an explicitly approved correction.
- **Validator requested**: Prepare the [bids](../bids/SKILL.md) handoff; do not interpret it
  here.
- **Deidentification assumed from BIDS naming**: Reject the assumption.
- **Upload or release requested**: Require a separate governance and release
  workflow.
- **Context compaction or model switch**: Reload this skill and the approved
  manifest before continuing.

## Handoffs

- Use [bids](../bids/SKILL.md) for BIDS mapping, metadata requirements, inheritance,
  provenance, privacy review, and validator interpretation.
- Use [pydicom](../pydicom/SKILL.md) for bounded DICOM header inspection or explicitly approved
  staged metadata transformation.
- Use [dcm2nii](../dcm2nii/SKILL.md) for DICOM-to-NIfTI conversion and sidecar extraction.
- Route EEG format conversion, behavioral-log transformation, privacy policy,
  deidentification, release packaging, repository deposit, and analysis to
  their approved owners.
- If an invoking companion routed this capability and the destination remains
  unclear, return that unresolved boundary to the invoking companion. If no
  companion invoked it, stop at this capability boundary and offer
  [research-companion](../../skills/research-companion/SKILL.md) only as an optional public routing entry.

Each destination begins its own workflow and gates. Organizer approval does
not authorize another capability.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- *BIDS Specification* (Version 1.11.1). (2026, February 19). https://bids-specification.readthedocs.io/en/v1.11.1/
