---
name: polars-bio
description: >-
  Performs one approved genomic-interval or bioinformatics-file operation
  through an already available verified Polars-Bio environment while preserving
  coordinate conventions, reference identity, row grain, joins, streaming,
  remote access, outputs, and claim boundaries. Triggers: genomic intervals in
  Polars-Bio.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, Polars-Bio
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Polars-Bio

Operate on one approved genomic interval or bioinformatics table without
silently changing coordinates, joins, schema, or remote-data scope.

## Purpose

This conditional Part 4 data adapter audits BED, VCF, BAM, CRAM, GFF/GTF,
FASTA, or FASTQ input, reference and coordinate system, row grain, interval
semantics, joins, overlap policy, lazy or streaming execution, remote paths,
versions, outputs, and verification. It does not choose the analysis, reference,
filters, cloud access, or biological claim.

The user owns the operation, coordinates, reference, joins, output, and claim.
[polars](../polars/SKILL.md) owns general tabular operations; [pysam](../pysam/SKILL.md) owns low-level genomic
file checks.

Activate only for exact `polars-bio` or an approved handoff naming one bounded
interval or file operation. Do not trigger from generic Polars, BED, VCF,
overlap, or genomics requests. Out of scope: unapproved cloud access, installs,
full pipelines, and interpretation.

## Inputs

Obtain or mark missing: format and source, reference and coordinate convention,
row and interval grain, strand, operation, overlap or join policy, lazy or
streaming mode, remote path and credentials, environment, output, and claim.
If source, coordinates, or row grain is missing, return **Polars-Bio intake
incomplete**.

## Steps

### Gate 1: approve the interval operation

Show source, format, reference, coordinates, row grain, operation, join and
overlap policy, execution mode, output, and claim. Gate 1 authorizes a method
plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, remote state, output, and
verification. Gate 2 authorizes one action only; it does not authorize installs,
cloud access, downloads, or overwrites.

Return:

```text
Polars-Bio Operation Record
Source, format, reference, coordinates, and row grain:
Interval, strand, join, overlap, and null policy:
Lazy/streaming, remote, environment, and output:
Verification, warnings, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Make 0/1-based, half-open/closed, chromosome naming, strand, and genome
  build explicit. Never infer them from column names.
- Preserve interval and sample identity, duplicates, null semantics, join
  cardinality, ordering, and sortedness. Validate overlaps and counts.
- Keep lazy, streaming, and out-of-core behavior explicit; do not materialize
  large data silently.
- Remote URIs and credentials require a separate bounded access approval.
  Outputs are data artifacts, not biological conclusions.

Stop for coordinate or build mismatch; ambiguous row or interval grain;
unvalidated join cardinality; hidden materialization; unapproved cloud or
credential use; unavailable environment; or a request to install, download,
overwrite, or interpret interval results biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Apache Software Foundation. (n.d.). *Apache Arrow documentation*. https://arrow.apache.org/docs/
- Polars. (n.d.). *Polars user guide*. https://docs.pola.rs/
- BioDataGeeks. (n.d.). *Polars-Bio documentation*. https://biodatageeks.org/polars-bio/
