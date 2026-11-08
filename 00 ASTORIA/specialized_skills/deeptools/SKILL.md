---
name: deeptools
description: >-
  Performs one approved deepTools coverage, QC, comparison, heatmap, profile, or
  track-conversion operation through an available verified environment while
  preserving reference, normalization, regions, replicates, parameters, outputs,
  provenance, and interpretation boundaries. Triggers: coverage tracks and
  heatmaps with deepTools.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: deepTools
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# deepTools

Perform one approved NGS coverage or QC operation without silently selecting a
normalization, reference region, comparison, or biological interpretation.

## Purpose

This is a conditional Part 4 NGS visualization and QC adapter. It audits BAM
and region inputs, reference and coordinate conventions, normalization,
replicates, bins, blacklist, effective genome size, parameters, version,
outputs, and verification. It does not choose the assay design, normalization,
regions, threshold, or claim.

The user owns the operation, reference, regions, normalization, comparison, and
claim. [pysam](../pysam/SKILL.md) owns low-level file checks; [bulk-rnaseq](../bulk-rnaseq/SKILL.md) owns workflow
routing.

Activate only for exact `deeptools` or an approved handoff naming one operation.
Do not trigger from generic sequencing, coverage, ChIP-seq, ATAC-seq, or heatmap
requests. In scope: `bamCoverage`, `bamCompare`, correlation, fingerprint,
PCA, matrix, heatmap, profile, or one selected conversion. Out of scope: full
pipelines, downloads, installs, peak calling, and biological interpretation.

## Inputs

Obtain or mark missing: assay, BAM and index identity, reference and contigs,
replicates, regions or annotation, effective genome size, normalization,
strandedness, operation, version, output, and claim. If file identity,
reference, normalization, or region is missing, return **deepTools intake
incomplete**.

## Steps

### Gate 1: approve the operation

Show assay, files, reference, regions, replicates, normalization, parameters,
operation, output, verification, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installation,
downloads, pipeline chaining, overwrites, or interpretation.

Return:

```text
deepTools Operation Record
Assay, files, indexes, reference, and regions:
Replicates, strand, normalization, genome size, and bins:
Operation, environment, parameters, and output:
Verification, warnings, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Match normalization to the assay and estimand; do not infer it from a
  command default or compare incompatible tracks.
- Preserve replicate, sample, strand, fragment, blacklist, and coordinate
  choices. Record effective genome size and bin size.
- Validate indexes, headers, regions, output tracks, matrix dimensions, and
  checksums. Do not overwrite sources.
- Correlation, PCA, heatmaps, and profiles are descriptive summaries; they do
  not establish binding, accessibility, expression, or mechanism.

Stop for reference or index mismatch; incompatible normalization; missing
replicate or region definition; failed matrix or track validation; unavailable
environment; a request to install, download, call peaks, overwrite, or
interpret visual summaries biologically.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- deepTools developers. (n.d.). *deepTools documentation*. https://deeptools.readthedocs.io/en/develop/
