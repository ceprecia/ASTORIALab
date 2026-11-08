---
name: bids
description: >-
  Designs and reviews one version-pinned Brain Imaging Data Structure curation
  specification for an approved source, raw, derivative, or study dataset. Use
  when the request, or a part coordinator, hands over an explicitly matching task.
  It maps dataset layers, entities, filenames, metadata, provenance,
  deidentification boundaries, and validation requirements against the selected
  official BIDS release, then records only user-selected mappings after two
  approval gates. It may run an approved read-only local validation with an
  already available validator, but it does not choose scientific labels, convert
  DICOM, rename or organize files, edit metadata, install tools, run BIDS Apps,
  upload or share data, search, save, or start another capability without
  separate approval. Triggers: curate my dataset to BIDS, BIDS curation
  specification.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: acquisition
  modality: multimodal
  dependencies: ""
  requires: bids-validator; a dataset inventory
  gates: converting or restructuring real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# BIDS

Design and review a BIDS curation specification without turning a standard, schema snapshot, or validator into an automatic data pipeline.

## Purpose

`bids` is the Part 3 canonical owner for version-pinned Brain Imaging Data Structure interpretation, prospective curation design, compliance review, and validation planning for one bounded dataset.

It owns:

- identifying the source, raw BIDS, derivative BIDS, and study-dataset boundaries;
- mapping approved scientific and acquisition concepts to BIDS datatypes, entities, suffixes, filenames, tables, sidecars, and provenance fields;
- checking required, recommended, optional, forbidden, inherited, and custom metadata against one exact official BIDS release and schema;
- exposing label, metadata, privacy, deidentification, provenance, and validation decisions for the user;
- preparing a selection-bound BIDS Curation Specification;
- optionally running and interpreting an approved read-only local validator with an already available exact version.

The user owns the study concepts, participant and session structure, task and acquisition labels, run identity, source-to-output mapping, scientific metadata, dataset type, selected BIDS release, deidentification policy, privacy and consent decisions, missing-data treatment, curation exceptions, repository target, release decision, and all scientific claims.

[bids-organizer](../bids-organizer/SKILL.md) owns approved filesystem transformation into a staged BIDS tree. [dcm2nii](../dcm2nii/SKILL.md) owns DICOM-to-NIfTI conversion through a verified converter. [pydicom](../pydicom/SKILL.md) owns bounded DICOM inspection or explicitly approved staged metadata transformation through the pydicom library. Part 4 capabilities own analysis, querying for analysis, and BIDS-App execution.

This skill specifies and reviews the standard. It does not perform conversion or curation writes.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `convert these DICOMs`;
- `rename this dataset`;
- `run fMRIPrep`;
- `query my BIDS data`;
- `upload this to OpenNeuro`;
- broad phrases such as `neuroimaging files`, `metadata`, `dataset`, or `validation`.

One run covers one bounded dataset, one approved dataset layer or linked layer set, one selected BIDS release and schema, and one curation or compliance decision.

Several modalities may remain together only when they belong to the same dataset boundary and share the selected release, identifiers, privacy rules, and curation plan. Otherwise split them.

Do not mix:

- a non-BIDS acquisition source with a raw BIDS dataset;
- raw BIDS data with derivatives as if they have identical rules;
- an accepted BIDS release with an unmerged BIDS Extension Proposal;
- validator conformance with scientific correctness, data quality, consent, deidentification, or readiness to share.

## Inputs

Gather:

- project and dataset purpose;
- source, raw, derivative, or study dataset type;
- selected BIDS release or a request to compare compatible releases;
- modalities, datatypes, acquisition families, tasks, sessions, runs, sites, scanners, and participant structure;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) and task specifications where applicable;
- exact source inventory or a bounded representative inventory;
- current directory and filename patterns;
- candidate subject, session, task, acquisition, direction, reconstruction, run, echo, part, recording, space, description, and other labels;
- source metadata and its provenance;
- event, behavioral, physiological, phenotypic, sample, scan, session, and participant tables when applicable;
- source-to-raw and raw-to-derivative provenance relationships;
- repository, collaborator, pipeline, or downstream-tool requirements;
- consent, governance, access, deidentification, date, face, free-text, identifier, linkage-key, and sharing constraints;
- validator availability and exact version if validation is requested;
- known missing or ambiguous series, metadata, files, or relationships;
- outcome visibility, confirmatory status, desired output, and stop point.

Mark an essential missing item `unknown`. Do not infer scientific labels from filenames, series descriptions, acquisition order, or a candidate example.

## Steps

### 1. Build the BIDS Curation Brief

Show:

| Field | Required content |
|---|---|
| Dataset and project | Exact bounded object |
| Dataset layer | Source, raw, derivative, study, or explicitly linked layers |
| Purpose | Collection planning, mapping, compliance review, validator interpretation, or handoff |
| Selected release | Exact BIDS version and schema, or unresolved |
| Modalities and scope | Included and excluded data families |
| Scientific decisions | user-owned concepts and labels |
| Source inventory | Exact material that may be inspected |
| Privacy boundary | Permitted identifiers, dates, faces, free text, linkage data, and access |
| External actions | Network, upload, install, conversion, write, or sharing, normally none |
| Missing inputs | User-owned or technical unknowns |
| Stop point | Exact specification or validation record that ends the run |

If the dataset layer, scientific meaning, selected release, or privacy boundary is unresolved, stop and return it to the user.

### 2. Gate 1: approve the standards-review boundary

Before inspecting source material or building mappings, show the brief and ask the user to approve:

- dataset layers and modalities in scope;
- exact BIDS release or release-comparison question;
- files and metadata that may be inspected;
- privacy and access boundary;
- mapping and validation questions;
- any proposed read-only local validator preflight;
- any separately approved evidence handoff.

Gate 1 authorizes only the displayed standards review, bounded source inspection, and read-only availability checks.

It does not authorize:

- choosing scientific labels, dataset type, release, deidentification policy, or repository target;
- installing software, converting, renaming, moving, copying, deleting, editing, validating through an external service, uploading, sharing, saving, or running an analysis or BIDS App.

Do not infer approval from silence.

### 3. Pin the specification and tool state

Record:

- BIDS release and tag;
- release date and exact specification URL;
- schema version, commit, URL, or local verified file;
- validator name, version, bundled or selected schema, and invocation mode;
- accepted extensions included in the release;
- experimental BEPs, if any, kept separate;
- downstream repository or pipeline requirements and their exact versions;
- known disagreements among specification text, schema, validator, and downstream tool.

Do not treat a bundled schema from an external candidate as current. Do not equate `stable` with a fixed reproducible version.

### 4. Build the Dataset Layer and Provenance Map

Map:

| Layer | Required decisions |
|---|---|
| Source | Original acquisition representation, access boundary, identifiers, and preservation policy |
| Raw BIDS | Curated data closest to acquisition, selected transformations, and deidentification status |
| Derivative BIDS | Generating process, input sources, pipeline identity, spaces, descriptions, and retained metadata |
| Study dataset | Relationships among source, raw, derivative, and other component datasets |
| Code and documentation | Curation code, README, changes, data dictionary, and provenance without identifiers |

Rules:

- BIDS `sourcedata/` is a structural location, not a privacy control.
- For BIDS 1.11.1, account explicitly for both required root files:
  `dataset_description.json` and one `README`, with the exact allowed README
  extension and encoding checked against that release. Recheck this rule for
  any other selected release.
- Do not place identifiable DICOMs or linkage keys in a dataset intended for sharing merely because the validator ignores or permits the location.
- Preserve original source data only inside the approved protected boundary.
- Keep generated outputs separate from source data and never overwrite the sole source copy.
- A defaced image may be raw BIDS when defacing is part of curation; preserve any pre-deface source only within the approved protected source boundary.
- Record every transformation between layers.

### 5. Build the Entity and Naming Map

For each source series or file family, record:

| Field | Required content |
|---|---|
| Source identity | Non-sensitive stable source key |
| Scientific meaning | user-approved acquisition, task, condition, or measure |
| BIDS datatype and suffix | Exact selected-release rule |
| Entities | Required, allowed, forbidden, and omitted entities |
| Labels | Proposed label, meaning, source, and collision status |
| Entity order | Exact schema order |
| Extension and companions | Data file and required or associated files |
| Duplicate handling | Scientific run identity, repeated acquisition, or unresolved collision |
| Layer | Raw, derivative, or study component |
| Status | Ready, conditional, blocked, or rejected |

Rules:

- Do not copy patient, accession, medical-record, scanner-subject, or other direct identifiers into BIDS labels.
- Treat labels as pseudonyms, not anonymity.
- Keep any reidentification key outside the BIDS dataset under a separately governed boundary.
- Do not assign `run`, `acq`, `rec`, `dir`, `echo`, `part`, `space`, or `desc` merely to make filenames unique. Each entity must retain its specification meaning.
- Do not infer a task from a series description without the user's confirmation.
- Resolve case collisions and filename collisions before transformation.
- Preserve an explicit unmapped status rather than forcing an uncertain source series into a suffix.

### 6. Build the Metadata Requirement Matrix

For each file family, record:

| Field | Required content |
|---|---|
| Metadata field or companion | Exact name |
| Requirement level | Required, recommended, optional, forbidden, or conditionally required |
| Condition | Exact rule that changes the requirement |
| Value and units | Supplied value or `unknown` |
| Source | DICOM tag, acquisition protocol, task log, manual record, pipeline, or other provenance |
| Transformation | Exact translation, calculation, normalization, or no change |
| Inheritance scope | Dataset, subject, session, datatype, task, acquisition, run, or file level |
| Conflict check | Higher and lower level values and intended precedence |
| Privacy check | Identifier, date, free text, face, or sensitive value risk |
| Verification | Spec, schema, validator, cross-file, or domain check |
| Status | Ready, missing, conflicting, inapplicable, or needs the user |

Rules:

- Apply the Inheritance Principle from the selected release, not a simplified memory of it.
- Avoid value overloading and unintended inheritance.
- Do not say every data file needs an adjacent JSON sidecar. Required metadata may be inherited when the selected rule permits it.
- Do not call `SliceTiming`, `TotalReadoutTime`, `EffectiveEchoSpacing`, or another field universally required or universally essential. Verify the exact modality, suffix, use, and selected release.
- Do not manually invent acquisition values that a converter failed to extract.
- Custom TSV columns require clear definitions, units, levels, missing-value rules, and privacy review as applicable.
- Keep task-event meaning aligned with the approved task and acquisition clock; BIDS formatting does not repair incorrect timing.
- For BIDS 1.11.1 event records, use duration `0` when the event is modeled as
  effectively instantaneous. Use `n/a` only when duration is unavailable, not
  merely because the event is brief. Recheck the selected release before
  applying this rule.

### 7. Build the Privacy and Governance Register

Inspect:

- direct identifiers in filenames, folders, DICOM headers, free-text fields, tables, logs, code, and provenance;
- pseudonymization and linkage-key separation;
- dates, ages, locations, rare categories, small cells, diagnoses, and combinations that increase reidentification risk;
- face and other identifiable pixel data;
- source DICOMs, screenshots, localizers, and burned-in annotations;
- consent, data-use, repository, institutional, and jurisdictional constraints;
- derivative metadata copied from source;
- remote services, telemetry, logs, caches, and validator behavior;
- release and access-control plan.

For each item, show the evidence, applicable policy owner, proposed handling options, residual risk, and the user's decision.

BIDS compliance is not a deidentification certification. This skill does not decide that data are safe to share.

### 8. Build the Validation Plan or interpret a supplied report

Specify:

- exact local validator and version;
- exact schema version, not an unpinned `stable` alias for a final record;
- dataset root and read-only boundary;
- excluded directories and every `.bidsignore` rule with rationale;
- expected errors, warnings, and ignored non-dataset files;
- structural checks not covered by the validator;
- cross-file, count, metadata, provenance, and scientific-semantic checks;
- privacy and governance checks outside validator scope;
- output capture and comparison plan;
- pass, conditional, blocked, and unresolved criteria.

Rules:

- Do not use `.bidsignore` or ignore flags to hide required content, contradictions, or unexplained files.
- Treat validator errors and warnings according to the exact version's documented semantics.
- A validator pass establishes only the checks implemented for that schema and version.
- A validator cannot confirm scientific labels, acquisition accuracy, task timing, consent, privacy, completeness, or analysis readiness.
- Prefer local validation for sensitive data. Do not send data to a web validator or other service without separate explicit approval even when the service states that files remain local.

### 9. Present curation options

Offer only applicable choices:

- select one source-to-BIDS mapping;
- compare release-compatible alternatives;
- return a scientific label or dataset-layer decision to the user;
- preserve a source family as unmapped pending evidence;
- revise inheritance or sidecar placement;
- resolve a privacy or governance question with the appropriate owner;
- prepare a [bids-organizer](../bids-organizer/SKILL.md), [dcm2nii](../dcm2nii/SKILL.md), [pydicom](../pydicom/SKILL.md), task-event, or
  specialist handoff;
- authorize one displayed read-only local validation;
- defer because the standard, source, or tool state is unresolved.

Do not rank options by what yields fewer validator messages.

### 10. Gate 2: The user selects the BIDS specification

Ask the user to:

- select the exact BIDS release and schema;
- select dataset layers and source-to-output mappings;
- confirm entities, labels, and naming;
- select metadata values, provenance, inheritance, and missing-data actions;
- select privacy, deidentification, and governance actions that are within the user's authority;
- select the validation plan;
- select any handoff packet or read-only local validation.

Gate 2 authorizes only the selected BIDS Curation Specification, handoff packets, and displayed read-only validation.

It does not authorize conversion, file or metadata mutation, installation, network validation, upload, sharing, analysis, BIDS-App execution, persistent saving, or another capability.

Do not infer selection from silence.

### 11. Produce and verify the BIDS Curation Specification

Include:

1. dataset purpose, layers, modalities, and exclusions;
2. exact BIDS release, schema, validator, and extension state;
3. Dataset Layer and Provenance Map;
4. Entity and Naming Map;
5. Metadata Requirement Matrix;
6. participant, session, task, acquisition, run, and site label dictionary;
7. event, phenotype, scan, sample, and other table specifications as applicable;
8. Privacy and Governance Register;
9. source preservation and transformation boundary;
10. validation plan or read-only validation record;
11. missing, conflicting, unmapped, and unresolved items;
12. selected implementation handoff packets;
13. user-owned decisions that remain;
14. provenance separating official rules, project evidence, AI comparisons, and the user's selections.

Verify:

- every normative claim matches the pinned release and schema;
- raw, derivative, source, and study layers remain distinct;
- every label has scientific meaning and no direct identifier;
- inheritance is applicable and non-conflicting;
- required companions and conditional metadata are accounted for;
- privacy risks and non-validator checks remain visible;
- no source file was changed and no conversion, install, upload, sharing, or analysis occurred.

## Outputs

Always distinguish:

- **Official requirement**
- **Official recommendation**
- **Project convention**
- **user-selected scientific mapping**
- **AI-generated option**
- **Validator finding**
- **Privacy or governance issue**
- **Unknown or blocked item**

Return:

1. BIDS Curation Brief;
2. specification and tool-state record;
3. Dataset Layer and Provenance Map;
4. Entity and Naming Map;
5. Metadata Requirement Matrix;
6. Privacy and Governance Register;
7. Validation Plan or Record;
8. Gate decisions;
9. BIDS Curation Specification;
10. selected handoff packets and unresolved decisions.

Do not use numeric confidence scores or composite rankings.

Default to read-only inspection. Return findings in the current task's requested form or under the recipient's existing reporting policy. Saving remains subject to the approval and destination rules below.

Before saving a specification, transforming data, editing files, installing a tool, validating through a network service, uploading, sharing, or starting another capability:

1. show the exact proposed action;
2. show every source and destination;
3. explain what will change or leave the machine;
4. ask for separate approval;
5. verify afterward.

For an authorized write, verify and use the destination selected for this task. Otherwise apply the verified placement policy for this project or recipient. If neither resolves it, use an established location for the applicable record or package when it fits the authorized scope. Ask once if the destination remains unresolved.

## Boundaries

For each run, use:

1. the exact official BIDS release selected by the user;
2. that release's machine-readable schema;
3. that release's rendered specification;
4. the exact validator and schema version used for the check;
5. official examples and starter material as examples, not as substitutes for the specification;
6. project conventions only when they do not conflict with the selected release.

If the stable specification has changed since this skill was created, verify the current release and show the difference before applying it. Do not silently migrate a dataset to a newer BIDS version.

An active BEP is a proposal, not an accepted rule. Use a BEP preview only when the user explicitly selects that experimental boundary and the exact preview schema and tooling are verified.

Edge cases:

- **BIDS release unspecified**: Compare only release implications and return selection to the user.
- **Candidate bundled schema supplied**: Treat it as a dated snapshot, not current authority.
- **BEP requested**: Label it experimental and pin the exact preview schema, validator support, and downstream limitations.
- **Series meaning ambiguous**: Preserve it as unmapped.
- **Filename collision**: Return the scientific identity decision to the user; do not add arbitrary entities.
- **Direct identifiers in labels**: Reject the mapping and require pseudonymous labels.
- **Linkage key inside dataset**: Move only after separate governance approval; do not include it in a shareable BIDS tree.
- **Identifiable DICOM in sourcedata**: Keep it inside the protected source boundary; BIDS placement does not make it shareable.
- **Defacing requested**: Prepare a separate approved implementation and verification handoff; do not run it here.
- **Unknown acquisition metadata**: Mark unknown and recover from authoritative acquisition records or a separately approved source inspection; do not guess.
- **Inherited metadata conflict**: Show every applicable file and precedence path before resolving.
- **Instantaneous event**: Distinguish a modeled impulse with duration `0` from
  an unavailable duration recorded as `n/a`; do not substitute one meaning for
  the other.
- **Validator passes**: Continue scientific-semantic, provenance, privacy, completeness, and cross-file checks.
- **Validator fails on an intentional extra file**: Decide whether it belongs outside the dataset or has a justified ignore rule; do not blanket-ignore.
- **Tool expects a different BIDS version**: Preserve the mismatch and let the user select migration, tool, or delay.
- **Existing dataset contains outcomes**: Compliance review may proceed, but design changes remain post hoc or exploratory as applicable.
- **Derivative without source provenance**: Mark incomplete; do not invent source links.
- **Web validator proposed for sensitive data**: Require separate explicit approval after current behavior and data-flow review.
- **No local validator**: Return the specification and blocked validation plan; do not install.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.
- When the BIDS schema is used locally, record its content hash.

## Handoffs

- Use [experimental-design](../../skills/experimental-design/SKILL.md) when participant, session, condition, site, or general design structure is unresolved.
- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) or a task-specific designer when task meaning, conditions, events, or behavioral variables are unresolved.
- Use [fmri-task-design-guide](../fmri-task-design-guide/SKILL.md) when task-fMRI event timing and acquisition alignment are unresolved.
- Use [bids-organizer](../bids-organizer/SKILL.md) for approved staged filesystem transformation and
  manifest verification.
- Use [dcm2nii](../dcm2nii/SKILL.md) for bounded DICOM-to-NIfTI and sidecar conversion.
- Use [pydicom](../pydicom/SKILL.md) for bounded DICOM metadata inspection or explicitly approved
  staged metadata transformation.
- Use [research-critique](../../skills/research-critique/SKILL.md) for critique of an existing protocol or curation claim.
- Route BIDS querying for analysis, BIDS Apps, preprocessing, and observed-data work to Part 4.

Each destination begins its own workflow and gates. BIDS approval does not authorize another capability.

This skill does not choose scientific labels, convert DICOM, rename or organize files, edit sidecars or tables, deidentify data, install software, run a BIDS App or analysis, upload or release a dataset, save, or declare data safe to share.

## Checks

Run a validator only when Gate 2 selects the exact local command and all of these hold:

- the validator is already available;
- its version and schema are verified;
- the dataset is within the approved access boundary;
- it can operate without modifying the dataset;
- logs and caches will not enter the dataset or expose sensitive values;
- the exact output capture and stop point are displayed.

Return:

- validator and schema versions;
- command or operation record;
- dataset root;
- errors and warnings without hidden filtering;
- ignored files and rules;
- interpretation tied to the exact specification;
- non-validator checks;
- unresolved items.

If the validator is unavailable, return the complete plan and **Blocked automated validation**. Do not install it.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Brain Imaging Data Structure. (n.d.-a). *BIDS machine-readable schema* (Version 1.11.1). https://bids-specification.readthedocs.io/en/v1.11.1/schema.json
- Brain Imaging Data Structure. (n.d.-b). *BIDS Validator* (Version 3.0.1) [Computer software]. https://bids-standard.github.io/bids-validator/
- Brain Imaging Data Structure. (2026, February 19). *BIDS specification* (Version 1.11.1). https://bids-specification.readthedocs.io/en/v1.11.1/
- Gorgolewski, K. J., Auer, T., Calhoun, V. D., et al. (2016). The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Scientific Data, 3*, 160044. https://doi.org/10.1038/sdata.2016.44
