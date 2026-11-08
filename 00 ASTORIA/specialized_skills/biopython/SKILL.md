---
name: biopython
description: >-
  Implements one approved sequence, alignment, feature, or biological-file
  operation through an already available verified Biopython environment while
  preserving sequence identity, coordinate conventions, source records,
  versions, writes, and interpretation boundaries. Triggers: sequence or
  alignment operation in Biopython.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, Biopython
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Biopython

Perform one approved biological-file or sequence operation without silently
changing coordinates, records, alphabets, or biological meaning.

## Purpose

This is a conditional Part 4 data/software adapter. It audits input format,
record and sequence identity, strand and coordinate conventions, feature
locations, alignment columns, annotations, parser warnings, version, output,
and round-trip verification. It does not choose an analysis, reference, search,
alignment, or biological claim.

The user owns the operation, reference, coordinates, parameters, and claim.
[pysam](../pysam/SKILL.md) owns selected SAM/BAM/VCF operations; [anndata](../anndata/SKILL.md) owns annotated
matrix structure.

Activate only for exact `biopython` or an approved handoff naming one operation.
Do not trigger from generic genetics, sequence, or genomics requests. In scope:
one parse, inspect, transform, align, translate, feature, or format-conversion
operation. Out of scope: database searches, downloads, full pipelines,
automatic annotation, and biological interpretation.

## Inputs

Obtain or mark missing: source format and identity, sequence or record units,
strand, coordinate convention, reference, operation, parser version, output,
collision policy, round-trip check, and claim. If identity, coordinates, or
format is missing, return **Biopython intake incomplete**.

## Steps

### Gate 1: approve the operation

Show source and record identity, format, coordinates, operation, version,
outputs, round-trip checks, limitations, and claim. Gate 1 authorizes a method
plan only.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize downloads, installs,
database access, overwrites, or interpretation.

Return:

```text
Biopython Operation Record
Source, format, records, and sequence identity:
Strand, coordinates, annotations, and operation:
Environment, parser warnings, and output:
Round-trip verification and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Preserve record IDs, descriptions, sequence case, alphabet assumptions,
  strand, feature coordinates, and metadata. Never infer 0- or 1-based meaning.
- Report parser warnings, malformed records, ambiguous bases, gaps, and
  dropped annotations. Do not repair silently.
- Validate output counts, coordinate mappings, checksums, and bounded round
  trips before writing. Do not overwrite source records.
- A sequence transformation or alignment is not evidence of homology, function,
  expression, or phenotype.

Stop for unknown coordinate or strand convention; malformed or unverified
records; hidden annotation loss; unavailable environment; a request to search,
download, install, overwrite, or auto-annotate; or a request to interpret a
sequence operation biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Biopython Project. (n.d.). *Biopython documentation and API references*. https://biopython.org/docs/latest/
