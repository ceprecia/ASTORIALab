---
name: polars
description: >-
  Implements and verifies one already specified tabular transformation through
  an available, version-verified Python Polars API. Use when the request names
  this skill or a verified Active execution skill routes an exact source,
  schema, expression, join, aggregation, lazy-plan, and output specification. It
  audits row grain, keys, dtypes, null and NaN semantics, ordering, join
  cardinality, query optimization, streaming, UDFs, remote access, and writes
  against approved invariants. It does not choose an analysis, install packages
  or extras, migrate code automatically, infer schema decisions, access cloud
  data, use GPU or plugins, overwrite files, or interpret results. Triggers:
  transform this table with Polars, polars dataframe operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, Polars
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Polars

Implement and verify one approved Polars table transformation while preserving
its data semantics.

## Purpose

`polars` owns:

- version and API preflight for one selected Python Polars query;
- translation of an approved table operation into explicit Polars
  expressions;
- eager or lazy query construction and plan inspection;
- schema, key, cardinality, null, ordering, and equivalence checks;
- controlled collection, streaming execution, or export;
- a Polars Query Record.

The user owns the row grain, fields, filters, joins, transformations,
aggregations, missing-data rules, ordering, output, scientific interpretation,
and claims.

[exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns descriptive dataset inspection.
[dask](../dask/SKILL.md) owns approved larger-than-memory or distributed Python execution.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `DataFrame`, `ETL`, `pandas`, `CSV`, `Parquet`, `join`,
`group by`, `lazy`, `streaming`, or `make this faster` alone.

Do not use this skill to select Polars automatically, invent transformation
logic, install extras, migrate an entire codebase, access cloud services, use
GPU execution, load plugins, or write outputs without approval.

## Inputs

Obtain or mark missing:

- approved table operation and reference semantics;
- exact source paths or authorized endpoints and data sensitivity;
- row grain, keys, expected cardinality, schema, dtypes, units, and encodings;
- null, NaN, infinity, categorical, temporal, timezone, and string behavior;
- selected columns, filters, expressions, windows, joins, reshapes, and
  aggregations;
- duplicate-key and join-validation rules;
- ordering, stable-sort, group-order, and output-row expectations;
- eager or lazy mode, streaming or in-memory engine, and query-plan boundary;
- Python UDF, Arrow, NumPy, pandas, database, cloud, GPU, or plugin boundary;
- equivalence fixtures, invariants, tolerances, and failure criteria;
- approved `collect`, sink, write, overwrite, and destination behavior;
- installed Polars and Python versions and resource limits.

If row grain, keys, schema, null behavior, join cardinality, aggregation,
ordering, access authority, equivalence criteria, or write boundary is
unresolved, stop with **Polars query specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, Polars, PyArrow, NumPy, pandas, and relevant connector versions;
- expressions, contexts, readers, scans, joins, windows, engines, and sinks;
- strictness, schema inference, optimizer, streaming, thread-pool, and
  categorical behavior;
- experimental GPU or plugin state and installed versus documented version
  mismatch.

Python Polars `1.43.0` was current on 2026-07-23. Polars releases frequently,
and GPU support was documented as open beta. Live use verifies the installed
version and matching API.

### 2. Gate 1: approve the Polars Query Contract

Show:

- source, row grain, keys, schema, dtypes, and sensitivity boundary;
- exact expressions, filters, joins, aggregations, reshapes, and ordering;
- null, NaN, categorical, temporal, and duplicate behavior;
- eager or lazy plan, engine, resource estimate, and output schema;
- small-fixture equivalence and cardinality checks;
- remote, connector, GPU, plugin, collection, and write boundaries.

Gate 1 authorizes only local schema inspection, query construction,
`explain`, and a bounded synthetic or approved fixture check. It does not
authorize full collection, streaming, remote access, credentials, GPU,
plugins, database operations, writes, overwrites, or package changes.

### 3. Query forms for the approved operation

Where applicable, compare only valid forms such as:

- the reference implementation;
- one explicit eager Polars query;
- one approved lazy or streaming Polars plan.

For each show semantic equivalence, optimizer behavior, schema and ordering
effects, memory, UDF or connector exposure, visible output, benefit, tradeoff,
and limitation. Do not select Polars only from a performance claim.

### 4. Verify table semantics

Use a representative approved fixture:

| Invariant | Source or reference | Polars result | Expected behavior | Status |
|---|---|---|---|---|
| Row grain and count | | | | |
| Keys and duplicate counts | | | | |
| Schema and dtypes | | | | |
| Nulls, NaNs, and infinities | | | | |
| Join cardinality and unmatched keys | | | | |
| Aggregates and window results | | | | |
| Ordering and categories | | | | |

Inspect the unoptimized and optimized plan when relevant. Record projection
and predicate pushdown, common-subplan behavior, streaming compatibility, and
any optimizer rewrite that could affect observability or order.

### 5. Document the exact query and write boundary

Show:

- source readers or scans and explicit schema overrides;
- every expression context and alias;
- filters, casts, string and temporal parsing, null fills, and NaN handling;
- join type, keys, validation, coalescing, suffixes, and unmatched behavior;
- aggregation, window mapping, reshape, sort, and order-maintenance behavior;
- eager, lazy, streaming, UDF, connector, Arrow, and thread-pool boundaries;
- query plan, resource estimate, numerical tolerance, and output action.

Polars has no pandas-style index. Parallel and optimized execution can change
row order unless order is explicitly part of the approved contract. Null and
NaN are distinct and must not be silently conflated. A non-strict cast can
turn failures into nulls, and the default many-to-many join validation does not
check cardinality. Both require an explicit rule and reconciliation.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- query, engine, resource envelope, remote or connector boundary, invariants,
  and expected output schema;
- one `collect`, streaming collection, sink, or write operation;
- destination, file format, partitioning, overwrite, and cleanup behavior.

Reopen Gate 2 before changing source, schema, expressions, join type or keys,
aggregation, engine, streaming state, UDF, connector, GPU, plugin, output
format, or destination.

### 7. Run and verify the approved query

Run only the approved operation. Capture:

- source, query, query-plan, environment, and version hashes;
- source and output schemas, dtypes, counts, keys, and cardinalities;
- null, NaN, infinity, category, temporal, and timezone checks;
- join and aggregation reconciliation;
- optimized plan, engine, memory, duration, warnings, and failures;
- equivalence results and approved tolerances;
- output path, format, partitioning, checksum, and overwrite state;
- deviations and artifacts.

Return:

```text
Polars Query Record
Approved table operation:
Versions and APIs:
Source, row grain, keys, and schema:
Null, NaN, categorical, and temporal rules:
Expressions, joins, windows, and aggregations:
Eager, lazy, streaming, and optimizer state:
Fixture equivalence:
Approved collection or write:
Output schema, counts, and cardinality:
Resource use, warnings, and failures:
Specification-conformance check:
What execution does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Preserve row grain, keys, cardinality, dtypes, units, and missing-value
  semantics.
- Never infer that a pandas index should be dropped, materialized, or treated
  as a column.
- Never rely on implicit row or group order when order is scientifically or
  operationally meaningful.
- Never use `strict=False` casting without approval and a count of values
  converted to null.
- Never accept default many-to-many join validation when the approved key
  contract expects one-to-one, one-to-many, or many-to-one cardinality.
- Verify the engine actually used; requested streaming or GPU behavior can
  fall back and must not be treated as an out-of-core guarantee.
- Avoid Python UDFs unless the approved operation has no verified native
  expression and the performance and semantic costs are accepted.
- Never access cloud or database sources, use GPU execution, load plugins, or
  install connectors without separate authority.
- Do not write or overwrite a source path.
- Stop on schema drift, ambiguous casts, duplicate-key surprises, join
  cardinality inflation, non-streamable plans beyond memory, remote-access
  gaps, API mismatch, failed equivalence, or unapproved output.

## Polars query and engine checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled query-plan cards.** Compare the reference operation with only the approved eager, lazy, or streaming Polars plan. This makes semantic and execution differences visible. This requires explicit reference invariants. Fixture performance may not predict full scale.
- **Polars Query Decision Record.** Show schema, nulls, joins, order, expressions, query plan, resources, and write boundary. This prevents silent table-semantic drift. This requires detailed source metadata. Upstream source semantics may still be wrong.
- **Polars Query Record.** Execute one approved collection or write and reconcile invariants. This preserves semantic and output control. This adds a gate before materialization. Verification covers only declared invariants.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended table-validity matrix.** Add adversarial duplicate, null, timezone, and cardinality fixtures. This tests common migration failures. This adds fixture design and checks. This cannot represent every real-data edge case.
- **Query sensitivity grid.** Add one prespecified engine or schema-strategy sensitivity. This tests selected plan dependence. This adds execution and review cost. This does not cover every optimizer change.
- **Verified query bundle.** Execute the prespecified engine and adversarial-fixture checks. This documents robustness to selected execution and data cases. This adds compute and maintenance. Robustness does not validate scientific meaning.

## Checks

- **Positive:** an approved lazy Parquet aggregation produces an explained
  plan, fixture reconciliation, and verified output schema.
- **Negative:** `convert my pandas pipeline to Polars` does not trigger an
  automatic codebase migration.
- **Join:** duplicate keys that inflate a supposedly one-to-one join stop
  collection.
- **Missingness:** a null-to-zero change not present in the specification is
  rejected.
- **Remote:** a cloud scan without approved access and credentials stops
  before connection.
- **Handoff:** descriptive inspection returns to
  [exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md); distributed scale may return to [dask](../dask/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Polars. (n.d.). *Lazy API*. https://docs.pola.rs/user-guide/concepts/lazy-api/
- Polars. (n.d.). *Pandas migration guide*. https://docs.pola.rs/user-guide/migration/pandas/
- Polars. (n.d.). *Polars user guide*. https://docs.pola.rs/
- Polars. (n.d.). *Python Polars* (Version 1.43.0) [Computer software]. GitHub. https://github.com/pola-rs/polars/releases/tag/py-1.43.0
