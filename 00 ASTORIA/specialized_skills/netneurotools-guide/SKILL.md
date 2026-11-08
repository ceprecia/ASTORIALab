---
name: netneurotools-guide
description: >-
  Implements one already approved netneurotools dataset, interface,
  network-construction, null-model, metric, modularity, statistical, spatial, or
  plotting operation through an available, exact-version public API and returns
  an exact node, space, matrix, parameter, randomness, side-effect, output,
  verification, and provenance record. Use when the request names this skill or
  a verified Active method skill routes one exact netneurotools handoff. It
  makes node order, atlas and surface identity, matrix semantics, distance and
  weight transforms, signedness, null preservation, exchangeability, stochastic
  settings, dataset downloads, optional backends, writes, and claim limits
  visible before execution. Triggers: network null models with netneurotools,
  netneurotools operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: multimodal
  dependencies: ""
  requires: Python, netneurotools
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# NetNeuroTools Guide

Implement one approved network-neuroscience operation through the exact
public netneurotools API available for the selected project.

## Purpose

It does not choose a network method, null, threshold, transform, community resolution, test, atlas, template, visualization, or scientific interpretation; install packages; fetch data without approval; use development HEAD; overwrite; or chain operations.

`netneurotools-guide` owns:

- exact Python, netneurotools, dependency, optional-backend, and public-API
  preflight;
- translation of one approved network-neuroscience operation into
  inspectable version-pinned code;
- node, parcel, vertex, hemisphere, atlas, template, coordinate, matrix,
  label, and file identity control;
- explicit matrix semantics, transform, signedness, diagonal, symmetry,
  distance, density, randomization, seed, iteration, and output control;
- explicit network, cache, dataset-fetch, overwrite, rendering, and file
  side-effect control;
- one approved execution without silent method substitution, data fetch,
  rerun, overwrite, or downstream chaining;
- structural and method-conformance verification while preserving warnings,
  failed randomizations, invalid outputs, and provenance;
- a NetNeuroTools Operation Record.

The user owns the scientific question, graph construction, node definition,
edge estimand, thresholding, weight-to-length transform, directedness,
signed-edge policy, consensus rule, null model, preserved properties,
communication metric, community model and resolution, spatial weights,
exchangeability, statistic, multiplicity, atlas, template, visualization,
acceptance criteria, interpretation, and claims.

[brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md) owns connectivity and network-method
comparison. [statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns inferential and resampling design.
[networkx](../networkx/SKILL.md) owns implementation through NetworkX rather than
netneurotools. Modality, preprocessing, and parcellation owners retain source
data, space, QC, and node-definition decisions. This adapter does not select
a method because netneurotools implements it.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `netneurotools`, `network neuroscience`, `connectome`,
`graph theory`, `brain network`, `community detection`, `null model`,
`Moran's I`, `spatial autocorrelation`, `Schaefer atlas`, `fsaverage`,
`fsLR`, `surface plot`, or another broad package, method, atlas, template, or
modality phrase.

Do not use this skill to:

- choose a network representation, threshold, transform, metric, null,
  modularity model, resolution, spatial-weight matrix, permutation scheme,
  atlas, template, or visualization;
- install, update, clone, or create an environment for netneurotools,
  PyVista, PySurfer, numba, BCTpy, neuromaps, or another dependency;
- use the package's development branch or current online documentation as a
  substitute for an immutable installed or released source state;
- download a dataset, atlas, template, or surface without separate network
  and write approval;
- infer node order, hemisphere order, medial-wall handling, parcel labels,
  coordinate space, or matrix meaning from shape;
- interpret a graph metric, module, null comparison, spatial statistic,
  surface map, or group result.

## Inputs

Obtain or mark missing:

- an approved Network-Neuroscience Operation Specification and one exact
  named public function in one operation family: dataset fetch, interface conversion, network
  construction, randomization or null, metric, modularity, statistic,
  spatial statistic, or plot;
- scientific estimand and the method-level handoff that fixed every
  consequential analytical choice;
- exact source arrays, matrices, labels, surfaces, coordinates, maps, and
  files with hashes and aligned identities;
- node or vertex order, hemisphere order, parcel and medial-wall labels,
  atlas and template name, version, density, species, coordinate system,
  space, and citation;
- matrix shape, dtype, finite state, diagonal, symmetry, direction,
  signedness, edge definition, weight units, missing-edge encoding,
  sparsity, density, connectedness, and node alignment;
- approved weight-to-length or distance transformation with zero, negative,
  missing, and disconnected-edge behavior;
- approved threshold, consensus, randomization, preserved properties,
  rewiring or annealing controls, convergence or mixing checks, seeds, and
  number of realizations;
- approved metric, modularity objective, null matrix, resolution, repeats,
  spatial-weight matrix, exchangeability blocks, permutations, alternatives,
  multiplicity, and minimum attainable p-value where applicable;
- exact dataset or template identifier, upstream host, version, license,
  citations, expected files, checksums, cache path, network authority, and
  overwrite policy for a fetch operation;
- exact renderer, backend, headless behavior, colors, limits, masking,
  annotations, output format, and accessibility decisions for a plot;
- exact Python, netneurotools, NumPy, SciPy, scikit-learn, NiBabel, Nilearn,
  BCTpy, neuromaps, optional-backend, and compiled-library versions;
- exact public function, signature, parameters, accepted defaults, output
  semantics, memory, threads, randomness, and runtime limits;
- destination, cache, temporary, collision, atomic-write, rollback,
  metadata, and hashing policy;
- verification plan and compute, network, and destination authority.

If the operation, node or space identity, matrix semantics, transform,
preserved null properties, exchangeability, randomness, exact API, external
access, or output contract is unresolved, stop with **netneurotools
operation contract incomplete**.

> [!info] References
> Recorded forward tests are in `./references/forward_tests.md`; read them only when re-verifying the skill.

## Steps

### 1. Confirm one approved operation

Choose exactly one transition:

1. fetch one approved named dataset, atlas, template, or surface into one
   approved cache;
2. convert one approved parcel, vertex, CIFTI, GIFTI, or annotation
   representation;
3. construct one approved empirical or consensus network;
4. generate one approved randomized network or null realization set;
5. calculate one approved network metric;
6. calculate one approved modularity or consensus-clustering output;
7. run one approved general or spatial statistical operation;
8. render one approved plot from already approved data and assets.

Each transition binds one named public function or one exact documented
public callable sequence that cannot be reduced without changing the
approved operation. Do not treat a module or candidate reference page as one
operation.

Do not turn these families into the candidate's fetch, construct, analyze,
null, test, and plot pipeline. A request spanning multiple transitions
returns to the owning method or coordinator skill for a checkpointed plan.

### 2. Audit semantic identity

For every operation, show:

- participant or group provenance and whether the input is empirical,
  simulated, averaged, thresholded, or transformed;
- exact node, parcel, vertex, hemisphere, label, and coordinate order;
- atlas, template, density, species, space, and surface identity;
- matrix direction, symmetry, diagonal, signedness, edge units, missing
  values, zeros, density, connectedness, and duplicate nodes;
- alignment among adjacency, distance, coordinate, annotation, community,
  label, and map arrays;
- every prior threshold, normalization, consensus, transform, or projection;
- the scientific meaning of a zero, negative, missing, infinite, or
  disconnected edge.

Never infer correspondence from equal shapes. A graph operation can return a
numerically valid matrix after a node-order mismatch.

For weight-to-length conversion, display the exact mathematical transform,
its domain, monotonicity, scale dependence, handling of zeros and negative
weights, and effect on disconnected paths. Do not copy the candidate's
`-log(W / (max(W) + 1))` expression as a universal transform.

### 3. Preflight the exact release and API

Record:

- Python and every imported package version;
- netneurotools release, full commit, installation source, and license;
- exact public module, function, signature, source, defaults, return objects,
  warnings, and deprecations;
- whether the function is stable public API, deprecated, private, or in the
  explicitly alpha `experimental` module;
- array orientation, accepted signed or directed forms, mutation behavior,
  random-number interface, parallel behavior, and output semantics;
- optional plotting or acceleration backend and whether its absence changes
  behavior;
- memory, combinatorial or iterative cost, threads, temporary files, cache,
  external access, and output side effects.

The current stable release reviewed for this design is netneurotools `0.3.0`,
full commit `202b98afafc3b170b1406b0f5869b0ee2ce7e4da`, released
2025-10-02. Its release notes describe a major reorganization from the
`0.2.x` line, and PyPI classifies the project as Alpha. The current online
documentation displays post-release development builds such as
`0.3.0+21.ge8838dd`. Therefore every execution is checked against the exact
selected installed source or immutable release, not a remembered `0.2.x`
path, candidate quick reference, development HEAD, or unversioned web page.

The reviewed `0.3.0` package requires Python 3.8 or later. Check the user-selected interpreter and required packages at invocation time. An absent or incompatible dependency stops the affected execution; it does not authorize installation, environment creation, or substitution.

For each invocation, use this evidence order:

1. installed version, package path, and `inspect.signature`;
2. matching tagged or full-commit source and tests;
3. matching stable official documentation;
4. candidate material only as extraction evidence.

The candidate mixes stable `0.3.0` behavior with unreleased development
APIs. For example, stable `pv_plot_surface` lacks candidate-documented
`panel_size` and `show_silhouette` parameters, and candidate names including
`pv_plot_parcellated_data`, `pv_plot_subcortex`, `fetch_aparc`, and
`fetch_bazinet_assortativity` are not all available in stable `0.3.0`.
Availability is checked from the exact selected source, never inferred from
the candidate.

Do not call private functions or the alpha `experimental` module under this
adapter. A requested experimental operation is a separate, explicitly
nonstable design decision.

### 4. Gate 1: approve inspection and the operation contract

Show a **NetNeuroTools Operation Contract**:

| Element | Approved meaning | Observed state | Risk or side effect | Verification |
|---|---|---|---|---|
| Operation and estimand | | | | |
| Nodes, parcels, vertices, labels, and spaces | | | | |
| Matrices, maps, distances, and transforms | | | | |
| Method, null, statistic, or plot specification | | | | |
| Randomness, iterations, exchangeability, and multiplicity | | | | |
| Release, API, dependencies, and optional backends | | | | |
| Network, cache, external assets, and licenses | | | | |
| Memory, outputs, writes, and collisions | | | | |
| Verification and scientific limits | | | | |

Gate 1 authorizes only the displayed bounded metadata, header, array-schema,
version, API, source, cache, network-plan, memory, and destination inspection
plus code construction. It does not authorize data fetching, package
installation, full computation, randomization, plotting, cache mutation,
directory creation, output creation, overwrite, or downstream work.

### 5. Eligible implementations of the approved graph operation

Use the selected implementation of the approved graph operation. Compare
forms only if a material implementation choice remains open under the user's
approval and multiple already available forms preserve the approved method
and parameters. The following forms may qualify.

1. the exact version-pinned netneurotools public API;
2. an existing reviewed project function that calls the same public API;
3. a synthetic-fixture route using the same selected API and parameters.

For each form show source state, input semantics, randomness, external
access, optional backends, memory, writes, output schema, reproducibility,
visible result, benefit, tradeoff, and limitation. These are implementation
forms, not alternative graphs, transforms, nulls, metrics, tests,
parcellations, or visual designs. Do not propose installation.

### 6. Construct and audit the exact code

Display code before execution. It must:

- import only the exact reviewed public function;
- bind every input, node-order record, atlas, template, and matrix by
  immutable identity;
- validate dimensions, finite state, alignment, labels, spaces, diagonal,
  symmetry, signedness, density, and connectedness required by the approved
  operation;
- apply only the approved weight, length, distance, threshold, consensus, or
  projection transform;
- pass consequential parameters explicitly, including seeds, repeats,
  permutations, resolution, null, preservation controls, force, cache, and
  renderer settings;
- preserve original inputs and record whether the public function copies or
  mutates arrays;
- estimate memory and iterative or combinatorial cost;
- capture failed rewires, acceptance, convergence, preservation error, null
  diagnostics, and stochastic variability required by the method;
- preserve invalid, disconnected, undefined, excluded, and masked outputs
  distinctly from scientific zeros;
- use a fresh temporary destination and atomic final commit where supported;
- record versions, code, warnings, failures, outputs, and hashes.

For fetch operations:

- use the exact approved public fetcher and an explicit bounded `data_dir`;
- disclose that fetchers can contact external hosts, create directories,
  download, extract, move, or replace files;
- keep `force=False` unless a separately approved replacement action names
  every target;
- verify source identity, license, required citations, expected file
  inventory, checksums when available, and cache state before scientific use;
- do not default to `~/nnt-data`, use `NNT_DATA` implicitly, or accept an
  undocumented cache.

For randomized networks or nulls:

- state exactly which degree, strength, length, density, connectedness,
  signedness, direction, weight, or spatial properties are intended to be
  preserved;
- measure those properties in each output rather than infer preservation
  from the function name;
- use the approved number of swaps, annealing schedule, iterations,
  realizations, and seed policy;
- never use the candidate's `nodes * 20` swap count as universal evidence of
  mixing or adequacy.
- treat an achieved swap or rewire count below the approved request as an
  incomplete randomization, preserve it, and stop without automatic retry or
  downstream use.

For inferential operations:

- preserve the approved exchangeability structure and paired, blocked,
  spatial, family, or repeated-measures design;
- report the finite resampling space and minimum attainable p-value;
- keep multiplicity and directional alternatives explicit;
- never replace a spatially constrained null with unrestricted shuffling
  because the latter is easier to call.

For plotting:

- use only already approved atlas, surface, data, mask, limits, and backend;
- make the color-limit policy explicit; do not silently accept `clim=None`
  when automatic limits could materially change comparison or
  interpretation;
- expose any template fetch that the plotting call could trigger;
- distinguish numerical data verification from visual inspection;
- do not use a private plotting helper or deprecated PySurfer route without
  an explicit version-compatible exception.

### 7. Review graph and null assumptions and limits

Show:

- differences among the candidate, `0.3.0` release, installed signature,
  current development documentation, and original method source;
- all node, surface, parcel, coordinate, matrix, and transform assumptions;
- what the chosen graph representation omits or conflates;
- which network and null properties are preserved, approximate, changed, or
  unchecked;
- stochastic variability, convergence or mixing evidence, seeds, and
  sensitivity to parameters;
- exchangeability, spatial dependence, finite permutations, multiplicity,
  and minimum attainable p-value;
- dataset host, cache, license, citation, checksum, and upstream availability
  limits;
- plotting backend, hidden fetch, headless, color-scale, and visual-review
  limits;
- which properties can be verified mechanically;
- which graph, biological, anatomical, inferential, and visual judgments
  require human review.

A successful function call, preserved degree sequence, high modularity,
short path, low p-value, smooth surface, or plausible network does not
establish method suitability, biological mechanism, directionality,
causality, replication, or scientific importance.

### 8. Gate 2: approve one exact execution

Ask the user to approve:

- one complete code block and exact public API;
- one operation, input manifest, node and space identity, and output set;
- every transform, method parameter, random seed, iteration, realization,
  permutation, resolution, and accepted default;
- exact release, dependency, optional-backend, and source state;
- network access, external host, license, citations, cache, force, and
  expected file actions when applicable;
- memory, threads, temporary files, renderer, runtime, and writable paths;
- collision, rollback, verification, warning, and failure behavior;
- no-install, no-development-HEAD, no-method-substitution, no-unapproved
  fetch, no-overwrite, no-retry, no-interpretation, and no-chain boundary.

Gate 2 authorizes only the displayed execution and verification. A changed
input, node order, atlas, space, graph, transform, null, seed, parameter,
asset, backend, destination, retry, or next operation requires a new
contract.

### 9. Run one approved NetNeuroTools operation

Run only the approved code. Capture:

- exact code, function, arguments, working directory, and source state;
- Python, netneurotools, dependency, optional-backend, operating-system, and
  hardware versions;
- input hashes, node and label order, atlas, template, density, species,
  space, and coordinate identities;
- matrix semantics, transforms, signedness, diagonal, symmetry, density,
  connectedness, and missing-edge policy;
- null properties, seeds, iterations, acceptance, convergence, resampling,
  exchangeability, and multiplicity records;
- network calls, upstream URLs, cache actions, licenses, citations,
  checksums, and file inventory for a fetch;
- memory, threads, start and end time, exit status, stdout, stderr, warnings,
  and exceptions;
- temporary and final destinations plus prior collision state;
- output names, shapes, dtypes, labels, spaces, validity states, and hashes;
- missing, partial, invalid, unexpected, or version-divergent outputs;
- every deviation from the approved contract.

Do not change a graph transform, zero negative edges, add connectivity,
switch nulls, raise iterations, alter seeds, relax exchangeability, fetch a
missing asset, change renderer, rerun, or overwrite without a new approved
contract.

### 10. Verify and stop

Separate:

1. **Execution conformance:** exact release, API, code, arguments, inputs,
   randomness, external access, resources, writes, process status, and
   deviations.
2. **Structural verification:** output existence, shape, dtype, node order,
   labels, space, finite and invalid states, expected assets, metadata, and
   hashes.
3. **Method-conformance verification:** approved invariants, transform,
   null-preservation diagnostics, convergence, exchangeability, p-value
   resolution, rendering inputs, and stated limitations.
4. **Scientific decision:** the user decides adequacy, sensitivity analysis,
   exclusion, remediation, downstream use, interpretation, and claims.

Return:

```text
NetNeuroTools Operation Record
Approved operation and estimand:
Method-level handoff:
Input, node, label, atlas, template, and space manifest:
Matrix semantics and transforms:
Method, null, statistic, spatial, or plot specification:
Randomness, iterations, exchangeability, and multiplicity:
Release, public API, environment, and source state:
Exact code:
Network, cache, asset, license, and citation actions:
Memory, threads, runtime, temporary files, and writes:
Exit state, warnings, exceptions, and deviations:
Output inventory, metadata, validity state, and hashes:
Execution-conformance result:
Structural and method-conformance result:
Limitations and unresolved uncertainty:
user-owned adequacy, interpretation, and next decision:
```

## Boundaries

- Stop if the requested method, null, statistic, atlas, template, or plot was
  selected from package availability or a candidate quick start.
- Stop on unresolved node, parcel, vertex, hemisphere, atlas, template,
  species, density, coordinate, or space identity.
- Stop on mismatched adjacency, distance, coordinate, annotation, community,
  label, or surface order.
- Stop on unresolved diagonal, symmetry, direction, signedness, zero,
  missing-edge, density, connectedness, or weight semantics.
- Stop before applying an unapproved weight-to-length, threshold,
  normalization, negative-edge, or consensus transform.
- Stop when the selected null's preserved properties, randomization
  diagnostics, seed, iterations, or realizations are unresolved.
- Stop when achieved rewires or swaps are fewer than requested and preserve
  the incomplete result without retry.
- Stop when exchangeability, spatial dependence, finite permutations,
  multiplicity, or p-value resolution is unresolved.
- Stop on a private, deprecated, alpha, missing, or version-mismatched API
  without a separately approved compatibility design.
- Stop before package installation, source cloning, development HEAD,
  unapproved network access, hidden template fetch, implicit home-directory
  cache, or `force=True`.
- Stop before a write if the destination exists or collision, temporary, and
  rollback behavior is unresolved.
- Never set negative edges to zero, force symmetry, clear a diagonal, connect
  components, or discard nodes silently.
- Never treat a universal swap count, iteration count, resolution, p-value,
  atlas, or color scale as validated for the current study.
- A zero exit status, structurally valid output, or attractive plot does not
  establish network, inferential, anatomical, or biological validity.
- Never invoke a second network, statistic, plot, export, or interpretation
  operation automatically.
- netneurotools asks users to cite the original methods and redistributed datasets named in each function's docstring and API reference.

## Graph operation evidence and diagnostics

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled public-API, reviewed-project-function, or synthetic-fixture forms.** Compare only already available code forms that implement the same approved netneurotools operation and parameters. This makes source, randomness, external access, memory, and writes visible without reopening method choice. This adds implementation-form review. This cannot resolve a missing graph, null, test, atlas, or plot decision.
- **NetNeuroTools Operation Contract.** Audit node and space identity, matrix semantics, transforms, null properties, exchangeability, API state, external access, randomness, writes, and claim limits. This prevents hidden graph, stochastic, dataset, and version choices. This requires detailed method and provenance evidence. Numerical, upstream, and data-quality failures may still occur.
- **NetNeuroTools Operation Record.** Execute one exact operation once, preserve failures and stochastic diagnostics, verify structures and invariants, and stop before interpretation. This preserves authorization, semantic identity, method conformance, and inspectability. Any repair, retry, or next operation needs approval. Verification cannot determine biological meaning.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Fixture design, expected invariants, and comparison record.** Add one separately approved synthetic graph, map, or surface fixture with known structural expectations. This can expose API drift, node-order, preservation, geometry, and output defects earlier. This adds fixture design and execution work. Passing synthetic behavior does not establish observed-data validity.
- **Fixture record and observed-data readiness decision.** Execute the approved synthetic fixture first, compare expected invariants, then require a new Gate 2 for observed data. This can catch environment and implementation defects before observed-data writes. This adds a consequential checkpoint and compute. A passing fixture cannot validate the empirical graph or inferential design.
- **Independent implementation audit.** Add independent code review plus immutable input, node-order, environment, asset, and expected-output manifests. This improves detection of drift, misalignment, hidden downloads, and silent output changes. This adds review and manifest work. Agreement does not prove scientific suitability.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Liu et al. (2026). *netneurotools: A trainee-oriented approach to network neuroscience* [Preprint]. bioRxiv. https://www.biorxiv.org/content/10.1101/2026.04.21.650363v1
- Network Neuroscience Lab. (2025). *netneurotools* (Version 0.3.0) [Computer software]. GitHub. https://github.com/netneurolab/netneurotools/releases/tag/0.3.0
- Network Neuroscience Lab. (n.d.). *API reference*. netneurotools. https://netneurotools.readthedocs.io/en/latest/api.html
- Network Neuroscience Lab. (n.d.). *Installation*. netneurotools. https://netneurotools.readthedocs.io/en/latest/installation.html
