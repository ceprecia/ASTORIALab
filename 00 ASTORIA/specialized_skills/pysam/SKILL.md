---
name: pysam
description: >-
  Performs one approved SAM, BAM, CRAM, VCF, BCF, FASTA, FASTQ, tabix, or
  coverage operation through an already available verified pysam environment
  while preserving reference identity, coordinates, headers, indexes, formats,
  provenance, writes, and claim boundaries. Triggers: read BAM or VCF with
  pysam.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, pysam
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Pysam

Operate on one approved htslib-backed genomic file without silently changing
coordinates, references, filters, or variant meaning.

## Purpose

This conditional Part 4 adapter audits file type, reference and contig names,
headers, coordinate convention, sort and index state, read or variant fields,
region query, filters, version, output, and round-trip verification. It does
not choose a reference, caller, filter, annotation, or biological claim.

The user owns the operation, reference, region, filters, output, and claim.
[biopython](../biopython/SKILL.md) owns sequence and annotation operations; [bulk-rnaseq](../bulk-rnaseq/SKILL.md) owns
workflow routing.

Activate only for exact `pysam` or an approved handoff naming one file
operation. Do not trigger from generic sequencing, BAM, variant, or coverage
requests. In scope: inspect, query, count, convert, index, or bounded coverage
operation. Out of scope: variant calling, annotation, pipeline execution,
downloads, installs, and interpretation.

## Inputs

Obtain or mark missing: file type, reference and contigs, coordinate convention,
header, sort and index state, region, operation, filters, version, output,
collision policy, and claim. If file identity, reference, coordinates, or index
state is missing, return **pysam intake incomplete**.

## Steps

### Gate 1: approve the file operation

Show file and reference identity, headers, coordinates, index, region, filters,
operation, output, verification, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installation,
downloads, pipeline chaining, overwrites, or interpretation.

Return:

```text
pysam Operation Record
File type, source, reference, contigs, and header:
Coordinates, sort/index state, region, and filters:
Operation, environment, warnings, and output:
Checksums, round-trip verification, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Validate reference names, lengths, header, sort order, index compatibility,
  and coordinate convention before region queries.
- Preserve raw fields, flags, MAPQ, qualities, variant alleles, INFO, FORMAT,
  and sample identity. Do not filter or rewrite silently.
- Distinguish alignment coverage, read depth, and variant counts. A pileup or
  count is not a quality judgment or biological conclusion.
- Record warnings, skipped records, reference mismatches, and output checksums;
  never overwrite source files.

Stop for reference or coordinate mismatch; missing or stale index; malformed
header; silent field loss; unavailable environment; a request to install,
download, call variants, annotate, overwrite, or interpret counts or coverage.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
