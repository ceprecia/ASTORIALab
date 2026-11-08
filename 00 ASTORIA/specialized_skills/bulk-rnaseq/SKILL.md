---
name: bulk-rnaseq
description: >-
  Routes one approved bulk RNA-seq checkpoint from read or quantification state
  through QC, quantification, differential-expression, enrichment, or export
  while preserving design, replication, provenance, resources, writes, and claim
  boundaries without running an end-to-end pipeline automatically. Triggers:
  analyze my bulk RNA-seq, RNA-seq QC to differential expression.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: a bulk RNA-seq quantification or read state; the named tools
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Bulk RNA-seq

Route one approved bulk RNA-seq checkpoint without silently choosing a design,
pipeline, reference, threshold, or downstream claim.

## Purpose

This is a conditional Part 4 workflow adapter. It separates samplesheet and
design, read QC, trimming, alignment or quantification, count construction,
normalization, differential expression, enrichment, and figures. It records
versions, references, parameters, resources, outputs, and gates. It does not
choose the biological contrast, strandedness, reference, toolchain, thresholds,
or interpretation.

The user owns the scientific design, replication, contrast, reference, tools,
thresholds, and claim. [pydeseq2](../pydeseq2/SKILL.md) owns selected differential-expression
execution; [pathway-enrichment](../pathway-enrichment/SKILL.md) owns selected enrichment.

Activate only for exact `bulk-rnaseq` or an approved handoff naming one
checkpoint. Do not trigger from generic RNA-seq, genomics, FASTQ, or gene-list
requests. In scope: design/QC, raw-read, quantification, count, differential-
expression, enrichment, or reporting checkpoint. Out of scope: automatic
end-to-end execution, data download, installation, unapproved cloud or cluster
use, and biological interpretation.

## Inputs

Obtain or mark missing: sample identity, biological and technical replication,
condition and covariate design, strandedness, reference and annotation,
input state, read or quantification provenance, QC state, checkpoint, software
versions, resource and storage scope, output path, and permitted claim. If
design, sample identity, reference, or checkpoint is missing, return **bulk
RNA-seq intake incomplete**.

## Steps

### Gate 1: approve one workflow checkpoint

Show design, sample sheet, input state, reference, checkpoint, software,
resources, QC and failure criteria, output, downstream handoff, and claim.
Gate 1 authorizes routing and planning only.

### Gate 2: approve one bounded action

Ask the user to select the checkpoint, exact environment, command or API, data
scope, output, and verification. Gate 2 authorizes one action only. It does
not authorize downloads, installs, cluster submission, automatic chaining,
or overwrites.

Return:

```text
Bulk RNA-seq Checkpoint Record
Design, samples, replication, and contrast:
Input state, reference, annotation, and strandedness:
Checkpoint, software, versions, and resources:
QC, output, verification, and handoff:
Deviations, exploratory state, and permitted claim:
Stop point:
```

## Boundaries

Method rules:

- Validate biological replicate identity and design before inspecting outcomes.
  Technical replicates do not automatically increase biological sample size.
- Keep raw reads, trimmed reads, alignments, quantifications, counts, and
  transformed values distinct. Record reference and annotation versions.
- QC gates precede quantification and modeling. Failed QC is surfaced, not
  silently repaired or excluded.
- Preserve strandedness, paired-end layout, batch, lane, and library metadata;
  never infer them from filename patterns alone.
- Route differential-expression and enrichment to their canonical owners with
  explicit contrasts, background, multiplicity, and exploratory labels.

Stop for missing sample identity or biological replication; unknown reference
or strandedness; failed or missing QC; batch or lane confounding; unapproved
download, installation, cluster, or external write; an end-to-end request
without checkpoint approvals; or a request to interpret expression or pathway
output as biological truth.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- ENCODE. (n.d.). *ENCODE RNA-seq guidelines*.
- Love, Huber, & Anders. (2014).
