---
name: tiledbvcf
description: >-
  Performs one approved TileDB-VCF variant-store ingestion, query, sample-add,
  or export operation through an already available verified environment while
  preserving variant identity, reference, schema, sample scope, concurrency,
  remote access, outputs, and claim boundaries. Triggers: variant store in
  TileDB-VCF.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, TileDB-VCF
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# TileDB-VCF

Operate on one approved variant store without silently changing samples,
reference builds, schemas, query regions, or cloud scope.

## Purpose

This conditional Part 4 variant-data adapter audits VCF/BCF identity, reference
build and contigs, samples, alleles, schema, ingestion or query operation,
region, consolidation, concurrency, local or remote store, version, output, and
provenance. It does not choose a variant model, filter, cohort, cloud service,
or biological claim.

The user owns the operation, reference, sample scope, filters, output, and claim.
[pysam](../pysam/SKILL.md) owns low-level VCF/BCF checks; [zarr-python](../zarr-python/SKILL.md) owns general array
store operations.

Activate only for exact `tiledbvcf` or an approved handoff naming one store
operation. Do not trigger from generic VCF, variants, TileDB, or population
genomics requests. Out of scope: variant calling, annotation, unapproved cloud
access, installs, downloads, and interpretation.

## Inputs

Obtain or mark missing: VCF/BCF source, reference and contigs, samples and
alleles, schema, store identity, operation, region and filters, concurrency,
local/remote scope, environment, output, collision policy, and claim. If
reference, sample scope, schema, or store is missing, return **TileDB-VCF
intake incomplete**.

## Steps

### Gate 1: approve the variant-store operation

Show source, reference, samples, schema, operation, region, filters,
concurrency, store scope, output, verification, and claim. Gate 1 authorizes a
method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, local or remote scope,
output, and verification. Gate 2 authorizes one action only; it does not
authorize installation, cloud access, downloads, parallel writes, or
interpretation.

Return:

```text
TileDB-VCF Operation Record
Source, store, reference, contigs, samples, and schema:
Region, filters, operation, concurrency, and access scope:
Environment, output, skipped records, and verification:
Provenance, collision policy, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Validate reference build, contig naming, sample IDs, allele fields, headers,
  schema, and index/store state before ingestion or query.
- Preserve variant, sample, genotype, INFO, FORMAT, filter, and ordering
  semantics. Record skipped records and schema changes; do not rewrite silently.
- Separate local and remote access, credentials, parallel writers, and
  consolidation. Never permit overlapping writes without explicit approval.
- Query results and variant counts are data artifacts, not evidence of disease,
  association, or population structure.

Stop for reference or schema mismatch; unknown sample scope; stale index/store;
unapproved cloud or credentials; overlapping writers; unavailable environment;
a request to install, download, call or annotate variants, overwrite, or
interpret variant counts biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- TileDB. (n.d.). *TileDB-VCF documentation*. https://tiledb-inc.github.io/TileDB-VCF/documentation/index.html
