---
name: pathway-enrichment
description: >-
  Implements one approved gene-set or pathway-enrichment operation through an
  available verified environment while preserving gene identifiers, ranked or
  thresholded input, universe, database version, null, multiplicity, output, and
  biological-claim boundaries. Triggers: do a pathway enrichment analysis, gene
  set enrichment analysis.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: genomics
  dependencies: ""
  requires: Python, gseapy or an equivalent enrichment library
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# Pathway Enrichment

Implement one approved enrichment checkpoint without silently choosing ORA,
GSEA, a gene universe, database, or biological interpretation.

## Purpose

This is a conditional Part 4 enrichment adapter. It audits gene identifiers,
input ranking or threshold, universe, organism, gene-set source and version,
method, null, permutations, multiple testing, redundancy, visualization, and
output provenance. It does not choose the contrast, gene list, background,
method, or claim.

The user owns the scientific contrast, input, universe, database, method,
multiplicity, and interpretation. [pydeseq2](../pydeseq2/SKILL.md) owns selected differential
expression; [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential interpretation.

Activate only for exact `pathway-enrichment` or an approved handoff naming one
enrichment operation. Do not trigger from generic pathway, gene list, GO, or
RNA-seq requests. In scope: one ORA, preranked GSEA, GSEA, or sample-level
scoring operation when selected. Out of scope: automatic method choice,
database downloads, installs, remote APIs without approval, and biological
claims from pathway names alone.

## Inputs

Obtain or mark missing: organism, identifier namespace and mapping, input list
or complete ranking, universe, contrast, gene-set database and version, method,
weighting, null and permutations, multiple-testing rule, redundancy policy,
environment, output, and permitted claim. If identifier, universe, method, or
database version is missing, return **pathway-enrichment intake incomplete**.

## Steps

### Gate 1: approve the enrichment specification

Show identifiers, input type, universe, organism, database, method, null,
permutations, multiplicity, redundancy, output, and claim. Gate 1 authorizes
method review only.

### Gate 2: approve one bounded implementation action

Ask the user to select the exact method, database snapshot, environment, output,
and verification. Gate 2 authorizes one action only. It does not authorize
downloads, installs, remote writes, automatic method choice, or interpretation.

Return:

```text
Pathway-Enrichment Implementation Record
Identifiers, mapping, input type, and universe:
Organism, gene-set source, and version:
Method, null, permutations, and multiplicity:
Environment, output, redundancy, and verification:
Unmapped genes, sensitivity, and limitations:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- ORA requires a thresholded list and a justified tested universe. GSEA
  requires a complete ranked list and must not be reconstructed from a
  thresholded list.
- Preserve unmapped genes, duplicates, identifier version, direction, and
  ranking score. Do not silently drop or remap genes.
- Gene-set databases, annotations, organism, release, and background determine
  the estimand. Record exact versions and access route.
- Control multiplicity and report effect, uncertainty, overlap, leading edge or
  contributing genes, and sensitivity. Redundancy reduction is descriptive.
- Enrichment is association with a set definition, not proof of pathway
  activity, mechanism, causality, or cell-type identity.

Stop for missing identifier namespace, universe, database version, or method;
thresholded input presented as GSEA without a full ranking; unapproved database
download or remote API; failed mapping or missingness audit; outcome-selected
gene sets; or a request to interpret enrichment as pathway activity, mechanism,
causality, or cell identity.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- GSEApy developers. (n.d.). *GSEApy documentation*. https://gseapy.readthedocs.io/en/latest/
- Subramanian, A., Tamayo, P., Mootha, V. K., Mukherjee, S., Ebert, B. L., Gillette, M. A., Paulovich, A., Pomeroy, S. L., Golub, T. R., Lander, E. S., & Mesirov, J. P. (2005). Gene set enrichment analysis: A knowledge-based approach for interpreting genome-wide expression profiles. *Proceedings of the National Academy of Sciences, 102*(43), 15545–15550. https://doi.org/10.1073/pnas.0506580102
