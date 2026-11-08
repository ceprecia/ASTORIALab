---
name: pydeseq2
description: >-
  Implements one approved bulk RNA-seq differential-expression operation through
  an already available verified PyDESeq2 environment while preserving count
  semantics, design, contrasts, replicates, normalization, dispersion, multiple
  testing, diagnostics, outputs, and claim boundaries. Triggers: differential
  expression with PyDESeq2.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, PyDESeq2
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# PyDESeq2

Implement one approved differential-expression checkpoint without silently
choosing a design, contrast, filter, shrinkage rule, or biological conclusion.

## Purpose

This is a conditional Part 4 differential-expression adapter. It audits count
matrix orientation and integer semantics, sample metadata, biological and
technical replication, formula, reference levels, contrast, filtering,
normalization, dispersion, fit, diagnostics, shrinkage, multiple testing,
effect reporting, and output provenance. It does not choose the user's design,
contrast, thresholds, or claim.

The user owns the estimand, design, contrast, reference, filters, shrinkage,
thresholds, and interpretation. [bulk-rnaseq](../bulk-rnaseq/SKILL.md) owns workflow routing;
[cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential interpretation.

Activate only for exact `pydeseq2` or an approved handoff naming one bulk
RNA-seq differential-expression operation. Do not trigger from generic gene
expression, RNA-seq, or enrichment requests. Out of scope: single-cell models,
automatic contrasts, downloads, installs, and biological interpretation.

## Inputs

Obtain or mark missing: count orientation and integer meaning, sample metadata,
biological and technical replicates, design formula, reference levels,
contrast, low-count filter, normalization, dispersion and fit state, software
version, diagnostics, multiple-testing rule, output, and permitted claim. If
design, contrast, replication, or count semantics is missing, return **PyDESeq2
intake incomplete**.

## Steps

### Gate 1: approve the differential-expression specification

Show counts, metadata, replication, formula, reference, contrast, filters,
normalization, dispersion, test, shrinkage, multiple testing, diagnostics,
output, and claim. Gate 1 authorizes method review only.

### Gate 2: approve one bounded implementation action

Ask the user to select the exact environment, operation, output, and verification.
Gate 2 authorizes one action only. It does not authorize installation,
automatic contrast selection, unapproved filtering, or interpretation.

Return:

```text
PyDESeq2 Implementation Record
Counts, orientation, samples, and replication:
Design, reference levels, and contrast:
Filtering, normalization, dispersion, and test:
Shrinkage, multiple testing, diagnostics, and environment:
Outputs, deviations, and verification:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Count rows or columns must be mapped to samples and genes explicitly; do not
  transpose by intuition or treat normalized values as counts.
- Preserve biological replicate identity and model batch or covariates only as
  specified. Technical replicates require an explicit aggregation policy.
- Reference levels and contrasts are scientific decisions. No automatic
  "first level" or sign convention is a substitute for selection.
- Record independent filtering, normalization, dispersion fit, shrinkage,
  Wald or other test, FDR method, effect estimates, intervals, and diagnostics.
- A thresholded gene list is not the complete result. Report the tested
  universe, missingness, effect scale, uncertainty, deviations, and exploratory
  status before any downstream enrichment.

Stop for non-count or unknown count data; missing biological replication;
ambiguous design, reference, or contrast; technical replicate ambiguity;
failed diagnostics; outcome-selected filters or contrasts; unavailable
environment; a request to install, download, overwrite, or interpret gene
lists as biological conclusions.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Love, M. I., Huber, W., & Anders, S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biology, 15*, Article 550. https://doi.org/10.1186/s13059-014-0550-8
- PyDESeq2 developers. (n.d.). *PyDESeq2 documentation*. https://pydeseq2.readthedocs.io/en/latest/
