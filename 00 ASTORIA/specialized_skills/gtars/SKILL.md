---
name: gtars
description: >-
  Performs one approved genomic-interval overlap, coverage, tokenization, or
  reference operation through an already available verified Gtars environment
  while preserving genome build, coordinates, interval identity, memory, remote
  scope, outputs, and claim boundaries. Triggers: genomic interval overlap with
  gtars.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, gtars
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Gtars

Operate on one approved genomic interval task without silently changing builds,
coordinate semantics, or data-access scope.

## Purpose

This conditional Part 4 interval adapter audits BED and related interval
inputs, genome build, coordinate and strand conventions, overlap and coverage
semantics, tokenization, reference access, Rust/Python versions, memory,
streaming, outputs, and provenance. It does not choose the genomic question,
reference, overlap policy, or biological claim.

The user owns the operation, build, coordinates, reference, output, and claim.
[polars-bio](../polars-bio/SKILL.md) owns tabular interval operations; [geniml](../geniml/SKILL.md) owns selected
interval-ML operations.

Activate only for exact `gtars` or an approved handoff naming one interval
operation. Do not trigger from generic BED, overlap, coverage, tokenization, or
Rust requests. Out of scope: unapproved reference downloads, cloud access,
installs, full pipelines, and interpretation.

## Inputs

Obtain or mark missing: source and format, genome build, coordinates, strand,
operation, overlap or coverage policy, reference scope, memory and streaming,
environment, output, and claim. If source, build, coordinates, or operation is
missing, return **Gtars intake incomplete**.

## Steps

### Gate 1: approve the interval operation

Show source, build, coordinates, operation, overlap/coverage policy, reference,
memory, output, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installs, downloads,
cloud access, or overwrites.

Return:

```text
Gtars Operation Record
Source, format, build, contigs, coordinates, and strand:
Operation, overlap/coverage/token policy, and memory mode:
Environment, reference scope, output, and verification:
Warnings, provenance, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Validate build, coordinate convention, contig names, strand, sortedness, and
  interval identity before overlap or coverage.
- Preserve row grain, duplicate policy, nulls, and output ordering. Record
  whether calculations are half-open or closed and whether intervals are
  merged.
- Keep reference and cloud access bounded and explicit; do not fetch genomes or
  install Rust/Python bindings to repair an environment.
- Coverage, overlap, and tokens are data summaries, not biological conclusions.

Stop for build or coordinate mismatch; ambiguous overlap or coverage policy;
missing reference scope; hidden downloads or cloud access; unavailable
environment; or a request to install, fetch, overwrite, or interpret interval
summaries biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
