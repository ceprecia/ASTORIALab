---
name: zarr-python
description: >-
  Plans, implements, or verifies one approved Zarr array-store operation through
  an available, version-verified Zarr-Python API. Use when the request names
  this skill or a verified Active execution skill routes an exact source,
  target, format, schema, access-pattern, layout, open-mode, concurrency, and
  validation specification. It compares bounded chunk, shard, and codec layouts,
  records effective metadata and resource estimates, prevents whole-array
  materialization, and gates every write or conversion. It does not choose an
  analysis, install packages or backends, infer v2 or v3, use cloud credentials,
  assume codec or chunk defaults, permit overlapping writers, overwrite stores,
  or interpret data. Triggers: store this array in Zarr, zarr array store
  operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: computing
  modality: any
  dependencies: ""
  requires: Python, Zarr
  gates: running on real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Zarr Python

Plan and verify one bounded Zarr array-store operation with explicit format,
layout, access, and write semantics.

## Purpose

`zarr-python` owns:

- version and API preflight for one selected Zarr-Python operation;
- inspection or creation of an approved group and array schema;
- bounded comparison of chunk, shard, codec, and store layouts;
- controlled local or already authorized remote read, write, append, resize,
  or blockwise conversion;
- structural, round-trip, checksum, and sampled-value verification;
- a Zarr Store Operation Record.

The user owns the scientific data, array semantics, dimensions, coordinates,
attributes, format version, layout, store, access pattern, concurrency,
output, interpretation, and claims.

[dask](../dask/SKILL.md) owns separately approved parallel or distributed computation over
array stores.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `Zarr`, `chunked array`, `cloud array`, `compression`,
`S3`, `Xarray`, `Dask array`, `convert HDF5`, or `.zarr` alone.

Do not use this skill to select Zarr automatically, install Zarr or backends,
obtain credentials, choose a scientific schema, infer format version, add
Dask or Xarray, use experimental features, or write or overwrite a store
without approval.

## Inputs

Obtain or mark missing:

- approved operation and exact source and target;
- source manifest, data sensitivity, store type, and access authority;
- required Zarr format 2 or 3 and interoperability target;
- group and array paths, shape, dtype, dimensions, fill values, attributes,
  codecs, and metadata;
- expected access pattern, read and write slices, append axes, and performance
  goal;
- selected chunk, shard, codec, compression and order settings, with bounded candidates only for unresolved layout choices;
- array and dataset size, memory, storage, request, time, and cost limits;
- explicit open mode, collision, overwrite, append, resize, and recovery rules;
- concurrent reader and writer model, overlap policy, and synchronization;
- local, ZIP, memory, remote, `fsspec`, `obstore`, credential, network, Dask,
  Xarray, NumPy, and backend boundaries;
- structural, checksum, round-trip, and sampled-value validation;
- installed Python, Zarr, NumPy, numcodecs, and backend versions.

If the source, target, format, schema, open mode, access pattern, layout,
concurrency, authority, resource limit, or validation plan is unresolved, stop
with **Zarr operation specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, Zarr-Python, NumPy, numcodecs, google-crc32c, and approved backend
  versions;
- store, group, array, create, open, codec, indexing, resize, append, metadata,
  and configuration APIs;
- v2 versus v3 defaults, removed APIs, effective codecs, experimental state,
  and installed versus documented version mismatch;
- target existence, permissions, free space, remote authority, and concurrent
  writers.

Zarr-Python `3.2.1` was current on 2026-07-23 and required Python `3.12` or
higher. Verify Zarr in the participant's selected interpreter and selected backend. Absence does not authorize installation. Live execution stops unless an already available
compatible environment and backend are selected.

### 2. Gate 1: approve the Storage Layout Contract

Show:

- operation, source, target, store type, authority, and sensitivity boundary;
- Zarr format, group and array schema, shapes, dtypes, dimensions, attributes,
  fill values, and interoperability needs;
- access pattern and selected chunk, shard, codec and store settings, with bounded alternatives only when a material layout choice remains unresolved;
- open mode, collision, append, resize, concurrency, and recovery policy;
- memory, storage, object count, requests, time, and cost estimates;
- synthetic or sampled layout benchmark and validation plan;
- remote, credential, network, Dask, Xarray, experimental, and write boundary.

Gate 1 authorizes only read-only metadata inspection and a bounded synthetic
layout test in an isolated in-memory or temporary store, including the
minimum writes required to measure round-trip behavior, compression, and
throughput. It does not authorize observed-data reads, target-store creation,
conversion, append, resize, metadata consolidation, remote access,
credentials, concurrent writes, observed-data or target-store output writes,
overwrite, or package changes.

### 3. Storage layouts for the approved operation

Compare eligible implementations only when a real choice remains. Otherwise use the approved implementation and report any material incompatibility before proceeding.

An assessment may address chunk shapes aligned to approved access patterns,
chunk-only or chunk-plus-shard layouts, or an approved codec or format
compatibility route. When comparing, consider only bounded, scientifically
equivalent forms supplied by the user.

For each assessed layout show access amplification, object count, chunk and shard memory,
compression, interoperability, concurrency, experimental state, visible
output, benefit, tradeoff, and limitation. Do not apply universal chunk or
codec rankings.

### 4. Inspect or benchmark safely

Use a synthetic or separately approved representative sample. Record the result
for the approved layout or once per eligible layout if a material comparison
remains.

| Check | Result for the assessed layout | Approved limit or invariant |
|---|---|---|
| Format and effective codecs | | |
| Chunk and shard bytes | | |
| Object and metadata count | | |
| Read amplification by access pattern | | |
| Write memory and throughput | | |
| Compression ratio | | |
| Round-trip and sample equality | | |
| Reader interoperability | | |

Estimate every slice and conversion before execution. Never use `[:]`,
`np.asarray`, or an equivalent operation when it would materialize the full
array beyond the approved memory boundary.

### 5. Document the exact store operation

Show:

- source and target stores, group and array paths, format, schema, and
  attributes;
- explicit open mode and every key, chunk, shard, or metadata object affected;
- effective serializers, filters, codecs, compression levels, chunk grids,
  shards, fill behavior, and order;
- blockwise read and write slices, memory bound, concurrency, overlap,
  atomicity, and recovery boundary;
- remote backend, credential, request, consistency, network, and cost state;
- experimental rectilinear chunks, v3 consolidated metadata, or other
  experimental feature when applicable;
- structural, checksum, sampled-value, round-trip, and interoperability tests.

Zarr format 3 is the current default for new arrays, but it is never inferred
for a task. `zarr.open` mode can depend on store writability, so the mode is
always explicit. A successful read does not prove store completeness or
scientific validity.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- source, target, format, schema, layout, codecs, open mode, slices,
  concurrency, backend, resources, and validation;
- one create, read, write, append, resize, convert, consolidate, or export
  action;
- store keys or paths affected, overwrite, rollback, recovery, and cleanup.

Reopen Gate 2 before changing format, schema, chunking, sharding, codec, store,
open mode, write range, concurrency, backend, credential, experimental
feature, source, target, or output destination.

### 7. Run and verify the approved store operation

Run only the approved operation. Capture:

- source, code, environment, and version hashes;
- source and target manifests, store type, format, group tree, array schema,
  attributes, effective codecs, chunks, and shards;
- exact open mode, affected paths or keys, block ranges, concurrency, and
  recovery state;
- source, target, memory, storage, object, request, time, and cost totals;
- structural, checksum, sampled-value, round-trip, and interoperability
  results;
- warnings, partial writes, metadata state, deviations, rollback, and cleanup.

Return:

```text
Zarr Store Operation Record
Approved operation:
Versions and APIs:
Source, target, store type, and authority:
Zarr format and interoperability:
Group and array schema:
Chunks, shards, codecs, fill, and attributes:
Access pattern and layout benchmark:
Open mode, concurrency, and affected paths:
Resource and materialization estimates:
Approved operation and status:
Structural, checksum, and sampled-value checks:
Warnings, partial writes, recovery, and deviations:
Specification-conformance check:
What storage success does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Always specify Zarr format and open mode explicitly.
- Never infer that a writable store may be appended to, created, resized, or
  overwritten.
- Never use a universal chunk, shard, or codec default. Record the effective
  codec pipeline from the created or opened array.
- Never materialize an entire source array when the approved memory envelope
  requires blockwise work.
- Do not use rectilinear chunks, v3 consolidated metadata, or another
  experimental feature without explicit selection and current verification.
- Never permit overlapping writes without a separately approved,
  backend-appropriate synchronization design.
- Never install Zarr, remote extras, provider backends, Dask, Xarray, NumPy,
  codecs, or credentials.
- Stop on unspecified format or mode, target collision, unavailable backend,
  absent credentials, unknown writers, unsafe overlap, insufficient storage or
  memory, whole-array materialization risk, unsupported dtype or codec,
  incompatible reader, stale metadata risk, experimental feature without
  approval, unapproved remote access, or unapproved write.

## Zarr layout, preservation, and recovery

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Storage layout cards.** Compare only bounded approved chunk, shard, codec, store, or format layouts. This makes access and interoperability consequences visible. This requires a representative access pattern. A sample benchmark may not predict full scale.
- **Storage Layout Decision Record.** Show format, schema, layout, effective codecs, mode, resources, writers, and validation. This prevents implicit formats, defaults, and writes. This requires detailed store metadata. Backend behavior can still change.
- **Zarr Store Operation Record.** Execute one approved store action and run structural and sampled-value checks. This preserves data and write control. This adds a gate before materialization. Sampling does not prove every value.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended storage-validity matrix.** Add failure-recovery and multi-reader interoperability fixtures. This tests selected recovery and reuse paths. This adds fixtures and storage operations. Fixture success is not production proof.
- **Layout sensitivity matrix.** Add prespecified reader, concurrency, and scale sensitivities. This tests selected portability and operational risks. This adds storage, time, and backend work. This cannot cover every reader or store condition.
- **Verified Zarr storage bundle.** Execute the prespecified blockwise round-trip, recovery, and reader checks. This documents selected robustness and portability. This adds I/O, storage, and cleanup. Robust storage does not validate scientific meaning.

## Checks

- **Positive:** an approved local v3 array creation produces an assessed
  layout, explicit mode, isolated write, and round-trip record. Include a
  layout comparison when a material choice remains.
- **Negative:** `convert this large file to Zarr` does not choose a schema,
  format, chunking, or destination automatically.
- **Collision:** an existing target with mode `w` stops before modification.
- **Memory:** a proposed `dataset[:]` conversion beyond RAM is replaced only
  after approval with a blockwise plan.
- **Remote:** an object-store path without approved backend and credentials
  stops before connection.
- **Handoff:** separately approved parallel array computation may return to
  [dask](../dask/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Zarr-Python. (n.d.-a). *Arrays*. https://zarr.readthedocs.io/en/stable/user-guide/arrays/
- Zarr-Python. (n.d.-b). *Consolidated metadata*. https://zarr.readthedocs.io/en/stable/user-guide/consolidated_metadata/
- Zarr-Python. (n.d.-c). *Performance*. https://zarr.readthedocs.io/en/stable/user-guide/performance/
- Zarr-Python. (n.d.-d). *Storage*. https://zarr.readthedocs.io/en/stable/user-guide/storage/
- Zarr-Python. (n.d.-e). *v3 migration*. https://zarr.readthedocs.io/en/stable/user-guide/v3_migration/
- Zarr-Python. (n.d.-f). *Zarr-Python* (Version 3.2.1) [Computer software]. GitHub. https://github.com/zarr-developers/zarr-python/releases/tag/v3.2.1
