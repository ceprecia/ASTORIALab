---
name: dask
description: >-
  Executes one already approved larger-than-memory or parallel Python workload
  through an available, version-verified Dask API and already authorized compute
  environment. Use when the request names this skill or a verified Active
  execution skill routes an exact collection, partition, scheduler, resource,
  and output specification. It audits data locality, schema or array shape,
  divisions or chunks, task graph, memory, shuffles, scheduler, workers,
  retries, determinism, credentials, and writes. It does not choose an analysis,
  install packages, deploy or scale clusters, obtain credentials, access remote
  storage, submit external jobs, rewrite scientific logic, or interpret results.
  Triggers: parallelize this with Dask, larger than memory workload in dask.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, Dask, authorized compute
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Dask

Execute and verify one approved Dask workload without changing its scientific
meaning or silently expanding its infrastructure.

## Purpose

`dask` owns:

- version and API preflight for one selected Dask collection or task graph;
- translation of an approved pandas, NumPy, or Python computation into an
  equivalent bounded Dask workload;
- partition, chunk, task-graph, scheduler, worker, and memory planning;
- local or already authorized cluster execution after a small equivalence
  test;
- controlled persistence or export of approved outputs;
- a Dask Execution Record.

The user owns the scientific operation, data inclusion, transformation semantics,
aggregation, scheduler or cluster authorization, resource budget, output,
interpretation, and claims.

[exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md) owns descriptive dataset inspection.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns scientific computation and result verification.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `big data`, `parallel`, `distributed`, `out of memory`,
`cluster`, `DataFrame`, `array`, or `speed up` alone.

Do not use this skill to decide that Dask is necessary, change analytical
logic, install Dask or extras, deploy infrastructure, request credentials,
open remote storage, or write outputs without approval.

## Inputs

Obtain or mark missing:

- approved computation and reference single-process behavior;
- measured scale, memory, or task evidence showing why Dask is warranted over
  the available bounded local implementation;
- exact source paths or authorized remote endpoints and data sensitivity;
- file formats, schema, dtypes, row or array grain, shape, index, divisions,
  chunks, and size estimates;
- selected Dask DataFrame, Array, Bag, Delayed, or Futures interface;
- partition or chunk plan and rationale;
- scheduler, local or cluster endpoint, worker count, threads, processes,
  memory, spill, timeout, retry, and resource limits;
- shuffle, join, groupby, rechunk, reduction, and custom-function behavior;
- deterministic ordering, seeds, floating-point tolerance, and equivalence
  criteria;
- credentials, network, cluster, dashboard, and logging boundaries;
- approved compute, persist, gather, export, overwrite, and destination
  operations;
- expected materialized-result size and whether it can fit the receiving
  process;
- installed Dask, Distributed, Python, pandas, PyArrow, NumPy, and storage
  backend versions.

If the computation, data location, collection type, partition plan, scheduler,
resource budget, access authority, equivalence test, or write boundary is
unresolved, stop with **Dask execution specification incomplete**.

## Steps

### 1. Preflight the exact environment

Record:

- Python, Dask, Distributed, pandas, PyArrow, NumPy, and relevant storage
  package versions;
- collection, scheduler, optimizer, serialization, and storage APIs;
- scheduler address, worker resources, spill directories, dashboard exposure,
  and security settings;
- defaults, deprecations, query-planning behavior, and installed versus
  documented version mismatch.

Dask `2026.7.1` was current on 2026-07-23. Live use verifies both Dask and
Distributed versions and the matching API. A version check never authorizes a
cluster, credential, network connection, or package change.

### 2. Gate 1: approve the Dask Execution Contract

Show:

- scientific computation held invariant;
- source, data locality, collection type, schema or shape, and size estimate;
- evidence that the approved workload needs Dask rather than a simpler
  available local implementation;
- partition or chunk plan and expected task-graph size;
- scheduler, workers, memory, spill, shuffle, retries, and compute budget;
- credential, network, dashboard, logging, and privacy boundary;
- small representative equivalence and failure test;
- proposed persist, gather, export, and artifact behavior.

Gate 1 authorizes only local metadata inspection and a bounded synthetic or
approved small-fixture test. It does not authorize full computation, cluster
deployment or scaling, remote access, credentials, external job submission,
persisting, writing, overwriting, or package changes.

### 3. Partition and execution choices

Where applicable, compare only valid forms such as:

- the reference single-process operation;
- one approved high-level Dask collection plan;
- one approved alternate partition or scheduler plan.

For each show semantic equivalence, task count, partition size, peak memory,
shuffle and transfer cost, determinism, operational exposure, visible output,
benefit, tradeoff, and limitation. Do not recommend Dask merely because it is
available.

### 4. Verify the small workload

Run or specify one approved representative small-fixture comparison. Do not
treat `head()` from the first partition as representative by default:

| Check | Reference | Dask result | Tolerance or invariant | Status |
|---|---|---|---|---|
| Schema, shape, and row count | | | | |
| Keys, index, and divisions | | | | |
| Missingness and dtypes | | | | |
| Aggregates or array values | | | | |
| Ordering and partition boundaries | | | | |
| Warnings, tasks, memory, and time | | | | |

Inspect the task graph, known and unknown divisions, chunks, metadata
inference, category state, serialization, custom-function purity, and output
cardinality before scaling.

### 5. Review the task graph and execution plan

Show:

- collection constructors, paths, glob expansion, schema, and metadata;
- partition or chunk sizes and number of tasks per operation;
- shuffles, joins, rechunks, reductions, repeated computes, and persisted
  intermediates;
- scheduler, worker topology, threads, processes, memory, spill, and retries;
- data movement, serialization, remote calls, credentials, and dashboard
  visibility;
- expected size and location of every `compute`, `persist`, and `gather`
  result;
- floating-point order, seeds, nondeterminism, and equivalence tolerances;
- full-run estimate, stop thresholds, monitoring fields, and output writes.

Parallel execution can change order, floating-point accumulation, failure
surface, and data exposure. A successful graph does not validate the
scientific computation.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- source, collection, graph, scheduler, worker and resource envelope,
  credentials, network boundary, retries, and monitoring;
- one `compute`, `persist`, `gather`, or export action;
- destination, overwrite behavior, and cleanup plan.

Reopen Gate 2 before changing the scheduler, cluster, worker count, memory,
partitioning, task graph, source, credential, remote endpoint, retry policy,
persisted state, or output destination.

### 7. Run the approved Dask operation and verify invariants

Run only the approved operation. Capture:

- source, code, configuration, environment, and version hashes;
- scheduler and worker state, resources, dashboard boundary, and security
  state;
- collection schema or shape, partitions or chunks, graph size, and
  optimization state;
- task counts, retries, failures, spills, transfers, memory, and duration;
- equivalence checks against the reference or approved invariants;
- output counts, schema, checksums, destination, and overwrite state;
- deviations, partial artifacts, and cleanup state.

Return:

```text
Dask Execution Record
Approved computation:
Versions and APIs:
Source and data-locality boundary:
Collection, schema or shape, and grain:
Partitions, chunks, and task graph:
Scheduler, workers, resources, and security:
Small-fixture equivalence:
Approved full operation:
Tasks, memory, transfers, retries, and failures:
Output verification:
Warnings and deviations:
Specification-conformance check:
What execution does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Preserve the approved scientific computation and verify small-fixture
  equivalence before scaling.
- Never infer credentials, connect to a cluster, access remote storage, expose
  a dashboard, or submit an external job without explicit authority.
- Never install Dask, Distributed, cloud filesystems, deployment tools, or
  optional packages.
- Avoid graphs and partitions that exceed the approved scheduler and worker
  envelope; do not apply a universal chunk-size rule.
- Do not use Dask when an available bounded local implementation meets the
  approved workload and resource limit without distributed overhead.
- Never call `compute()` on a result expected to exceed receiving-process
  memory.
- Do not hide failed partitions, retries, spills, worker loss, or partial
  writes.
- Treat floating-point reordering and nondeterministic task completion as
  possible result differences.
- Stop on semantic mismatch, unknown data location, sensitive-data exposure,
  unavailable scheduler, incompatible versions, task-graph explosion, unsafe
  memory pressure, an oversized materialized result, unapproved remote access,
  or unapproved writes.

## Dask execution and recovery

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Dask Execution Decision Record.** Show locality, task graph, partition, scheduler, memory, security, and equivalence records. This makes scale and exposure risks reviewable. This requires infrastructure details. Runtime conditions can still change.
- **Dask Execution Record.** Execute one approved action and verify it against the reference or invariants. This preserves semantic and infrastructure control. This adds a checkpoint before scale. Equivalence is limited to checked outputs.
- **Labeled execution-plan cards.** Compare the reference computation with only the approved Dask collection and scheduler plan. This shows whether parallelism is justified without changing science. This requires a working reference or invariant set. A small fixture may not predict scale behavior.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended execution-risk matrix.** Add dry-run estimates, dashboard review, and fault-injection criteria on an approved fixture. This tests selected operational failures. This adds setup and compute. Fixture failures do not cover every cluster event.
- **Resource sensitivity grid.** Add one prespecified partition or scheduler sensitivity plan. This exposes performance and memory dependence. This adds runs and operational complexity. This does not guarantee cluster-scale stability.
- **Verified scale-and-recovery bundle.** Execute the prespecified resource sensitivity and recovery plan. This documents robustness to selected conditions. This adds compute and operational burden. Robust execution does not validate scientific meaning.

## Checks

- **Positive:** an approved larger-than-memory aggregation produces a small
  equivalence check, bounded task graph, resource plan, and verified output.
- **Negative:** `make this faster` does not trigger Dask selection or a cluster
  launch.
- **Remote:** an S3 path without approved credentials and access stops before
  connection.
- **Scale:** millions of tiny tasks return a graph-design failure.
- **Write:** an export request without destination and overwrite approval does
  not persist data.
- **Handoff:** dataset structure returns to [exploratory-data-analysis](../../skills/exploratory-data-analysis/SKILL.md);
  scientific computation returns to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Dask. (n.d.). *Best practices*. https://docs.dask.org/en/stable/best-practices.html
- Dask. (n.d.). *Dask* (Version 2026.7.1) [Computer software]. GitHub. https://github.com/dask/dask/releases/tag/2026.7.1
- Dask. (n.d.). *Dask documentation*. https://docs.dask.org/en/stable/
