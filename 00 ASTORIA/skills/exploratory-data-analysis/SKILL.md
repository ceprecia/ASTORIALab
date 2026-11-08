---
name: exploratory-data-analysis
description: >-
  Performs one approval-gated descriptive inspection of a bounded research
  dataset and returns an inspectable Data Structure and Quality Record. Use when
  the request, or a part coordinator, hands over an exact descriptive-inspection
  handoff. It inventories source identity, schema, observation grain,
  missingness, ranges, distributions, duplicates, coding, dependence clues, and
  candidate next analyses without choosing an inferential test, changing data,
  installing readers, treating anomalies as errors, or converting exploratory
  patterns into confirmatory claims. Triggers: inspect this dataset
  descriptively, data quality and structure check.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: analysis
  modality: any
  dependencies: ""
  requires: ""
  gates: reading real data
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Exploratory Data Analysis

Inspect one bounded dataset before inferential analysis. Keep description,
quality assessment, scientific meaning, and later model choice separate.

## Purpose

`exploratory-data-analysis` owns:

- source and file identity;
- schema, dimensions, types, labels, units, and observation grain;
- missingness, invalid values, duplicates, ranges, distributions, and coding;
- dependency clues such as repeated observations, participants, items,
  sessions, sites, families, regions, channels, or time;
- transparent sampling and truncation records;
- descriptive quality findings and candidate next analyses;
- a Data Structure and Quality Record.

The user owns the scientific question, data-use boundary, variable meaning,
quality criteria, anomaly disposition, exclusion, transformation, imputation,
aggregation, analysis plan, interpretation, and claims.

[cogsci-statistics](../../specialized_skills/cogsci-statistics/SKILL.md) owns later statistical method-family comparison.
[research-literacy](../research-literacy/SKILL.md) owns evidence audits for explicit scientific claims.

Use only for:

- `exploratory-data-analysis`

Do not trigger from `explore`, `analyze`, `summarize this file`, `quality
check`, `statistics`, `plot this`, or a file extension alone.

Do not use this skill to:

- infer file meaning from an extension alone;
- install a reader or parser;
- scan an unbounded directory;
- modify, clean, impute, recode, convert, or overwrite data;
- label a value erroneous merely because it is unusual;
- select an inferential test or model;
- hunt for significance, clusters, subgroups, or a preferred story;
- treat an exploratory association as confirmatory evidence.

One inspection covers one coherent dataset or an explicitly bounded set of
files that share a source, observation grain, schema, and scientific purpose.
Obtain or mark missing:

- exact source files or supplied table;
- provenance, version, hash, and processing state when available;
- approved read boundary and privacy classification;
- data dictionary, codebook, units, missing-value codes, and expected schema;
- observation, participant, item, session, site, and time identifiers;
- expected ranges, cardinalities, constraints, and known exceptions;
- sampling or chunking plan for large data;
- requested descriptive questions;
- output and save boundary.

If identity, authorization, privacy, parser availability, or observation grain
cannot be established, stop with **Inspection boundary unresolved**.

## Steps

### 1. Build the Inspection Brief

Show:

| Field | Required record |
|---|---|
| Source | Exact files, supplied object, or table |
| Provenance | Origin, version, processing state, hash, and known transformations |
| Authorization | Read boundary, privacy class, and excluded fields |
| Grain | What one row, record, image, sample, or event represents |
| Schema evidence | Codebook, embedded metadata, inferred fields, and conflicts |
| Scale plan | Full scan, bounded chunks, or deterministic sample |
| Requested checks | Structure, quality, missingness, distributions, or linkage |
| Prohibited actions | Cleaning, inference, selection, writes, installs |
| Stop point | Return the unsaved inspection record in the current task's requested response form or under the recipient's existing reporting policy. A save requires separate approval. |

Distinguish documented meaning from structural inference.

### 2. Gate 1: approve bounded read-only inspection

Ask the user to approve:

- exact sources and fields that may be read;
- privacy and redaction controls;
- parser already available for the exact format;
- full-scan, chunk, or deterministic-sample plan;
- requested descriptive checks;
- memory, time, and output limits;
- no-change and no-inference boundary.

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize installation, conversion, cleaning, export, network access, model
fitting, or saving.

### 3. Inspection routes for the brief

Use the inspection route the brief calls for. Compare routes only when the brief leaves an unresolved inspection choice.

Offer only routes needed by the brief:

1. **Schema and grain audit**: source identity, dimensions, fields, types,
   units, identifiers, relations, and codebook agreement.
2. **Quality and missingness profile**: nulls, sentinels, invalid values,
   duplicates, constraints, missingness patterns, and unresolved causes.
3. **Distribution and dependence overview**: bounded descriptive summaries,
   category counts, ranges, quantiles, repeated-measure structure, time order,
   and candidate visual checks.

For each route state its read cost, sampling limits, visible output, benefit,
tradeoff, and what it cannot establish.

### 4. Inspect without changing the source

Preserve:

- input paths or object names;
- hashes or source identifiers when available;
- parser and runtime version;
- exact columns, dimensions, dtypes, units, and labels;
- row counts before and after any read-time filtering;
- sampling seed, rule, strata, chunk order, and coverage;
- parse warnings, coercions, truncation, and unreadable records;
- calculations used for every reported metric.

If a required reader is unavailable, return a reader and inspection plan.
Do not install it.

### 5. Quality evidence and its coverage

Use:

| Finding | Evidence | Grain affected | Expected or observed | Possible explanations | Consequence | Decision owner |
|---|---|---|---|---|---|---|

Check only where applicable:

- duplicate identifiers versus legitimate repeated observations;
- missing-value codes versus true nulls;
- impossible values versus rare but valid values;
- unit, timezone, encoding, and category inconsistencies;
- join-key uniqueness and unmatched records;
- participant, item, session, site, family, and temporal dependencies;
- range, floor, ceiling, sparsity, censoring, and class imbalance;
- processing-state mixtures and leakage-prone fields;
- deterministic-sample limits and uninspected regions.

Report facts, plausible explanations, and unresolved meaning separately.

### 6. Gate 2: approve the integrated record

Before expanding a scan, producing additional plots, saving, or handing off,
show:

- completed checks and coverage;
- unresolved schema or provenance conflicts;
- descriptive findings and their limits;
- candidate next analyses without selection;
- proposed record and destination.

The user selects what to retain and whether any later action is authorized.

### 7. Return the Data Structure and Quality Record

```text
Data Structure and Quality Record
Scope and source state:
Authorization and privacy boundary:
Observation and dependency grain:
Schema and codebook agreement:
Coverage and sampling:
Missingness and invalid-value evidence:
Duplicates, keys, and linkage:
Ranges, distributions, and category structure:
Parse warnings and quality conflicts:
Candidate next analyses:
Decisions still owned by the user:
Uninspected or unresolved areas:
Provenance and calculations:
Approved handoff or stop:
```

No inferential conclusion belongs in this record.

## Boundaries

- An anomaly is a review candidate, not an error verdict.
- Missingness mechanisms are hypotheses unless supported by design and source
  evidence.
- Correlation, separation, clustering, or a visible pattern does not establish
  a scientific group, mechanism, or claim.
- Sampling must be deterministic, documented, and identified as incomplete.
- Never expose direct personal identifiers, credentials, protected health
  information, or participant-level records beyond the approved boundary.
- Do not silently discard parse failures, duplicates, nulls, or outliers.
- A descriptive inspection cannot authorize a transition to inferential
  analysis.

## EDA findings and validation

Use these notes for the relevant source and findings. Keep the requested inspection read-only and record only the descriptive findings selected at Gate 2.

- **Evidence, grain, consequence, and uncertainty fields.** Build the quality evidence table with coverage and competing explanations. This separates observed defects from unresolved meaning. This leaves anomaly disposition to the user. This does not reproduce upstream processing.
- **Labeled inspection routes.** Offer only schema, quality, and distribution routes applicable to the approved source. This keeps the read boundary small. This may defer domain-specific checks. This does not validate a modality standard.
- **Verified Data Structure and Quality Record.** Preserve only selected descriptive findings in the record. This prevents silent cleaning or inference. This defers corrections and analysis. The record does not repair data.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Inspection routes plus validator plan.** Add exact domain validators and format-specific probes. This increases domain coverage. This requires verified adapters and tool states. A validator cannot establish scientific validity.
- **Lineage reproduction record.** Reproduce selected upstream transformations from pinned sources. This tests provenance and processing claims. This requires source code, environments, and more data access. Reproduction may remain incomplete.
- **Modified dataset plus change manifest.** Clean or transform a staged copy under explicit rules. This tests proposed repairs. This creates a new data product and scientific choices. This requires a separate implementation capability and approval.

## Checks

- **Positive:** an approved tabular dataset yields schema, grain, missingness,
  range, duplicate, and sampling records without an inferential test.
- **Negative:** `find significant patterns` does not trigger or redirect this
  skill into model search.
- **Edge:** a large binary format without an available reader returns a bounded
  parser plan and no installation.
- **Privacy:** unapproved direct identifiers remain unread and unreported.
- **Handoff:** method comparison waits for [cogsci-statistics](../../specialized_skills/cogsci-statistics/SKILL.md) and a separate
  invocation.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Wickham. (2014). Tidy data. https://doi.org/10.18637/jss.v059.i10
- Wilkinson et al. (2016). The FAIR guiding principles. https://doi.org/10.1038/sdata.2016.18
