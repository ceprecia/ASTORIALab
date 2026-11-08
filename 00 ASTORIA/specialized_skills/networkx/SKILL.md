---
name: networkx
description: >-
  Constructs, inspects, and analyzes one already specified graph through an
  available, version-verified NetworkX API. Use when the request names this
  skill or a verified Active method or execution skill routes an exact graph
  specification. It records node and edge meaning, graph type, direction,
  weights, signedness, duplicate and self-loop policy, missing-edge semantics,
  thresholds, disconnectedness, selected algorithms, null models, seeds,
  sensitivity checks, and exports. It does not choose a scientific graph
  representation, install packages or backends, optimize thresholds from
  outcomes, equate centrality with importance or communities with scientific
  groups, or interpret results. Triggers: analyze this graph with NetworkX,
  graph metrics in networkx.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: any
  dependencies: ""
  requires: Python, NetworkX
  gates: installing software, running on real data, accepting QC
  created: "2026-07-23"
  updated: "2026-10-29"
---

# NetworkX

Construct and verify one approved graph representation, then run only the
selected graph operations.

## Purpose

`networkx` owns:

- version and API preflight for one selected NetworkX graph operation;
- implementation of an approved node, edge, attribute, and graph-type schema;
- structural quality checks before any graph statistic;
- bounded execution of selected graph algorithms;
- approved null-graph, threshold, weight, direction, and disconnectedness
  sensitivity checks;
- a NetworkX Graph Record.

The user owns the scientific entities, relations, direction, weights, signedness,
thresholds, graph class, selected algorithms, comparison graph, interpretation,
and claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns scientific method-family comparison.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software execution control.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `network`, `graph`, `connectivity`, `centrality`,
`community`, `shortest path`, or a graph algorithm name alone.

Do not use this skill to invent nodes or edges, select a threshold from an
outcome, choose a community method automatically, or treat a graph metric as a
scientific construct. Do not install NetworkX, visualization packages,
accelerated backends, or optional readers.

## Inputs

Obtain or mark missing:

- approved scientific purpose and graph estimand;
- node identity, grain, attributes, inclusion rules, and duplicate policy;
- edge definition, source, direction, multiplicity, and missing-edge meaning;
- weight name, units, domain, sign, zero meaning, and transformation;
- approved `Graph`, `DiGraph`, `MultiGraph`, or `MultiDiGraph` form;
- self-loop, parallel-edge, isolated-node, and disconnected-component policy;
- threshold or sparsification rule and whether it was prespecified;
- selected algorithms and their weighted, directed, signed, and connectedness
  assumptions;
- approved comparison or null graph, randomization constraints, and seeds;
- sensitivity checks, output fields, export format, and destination;
- installed NetworkX and Python versions and compute limits.

If node or edge meaning, direction, weight semantics, threshold, graph class,
or algorithm compatibility is unresolved, stop with **Graph semantics
incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, NetworkX, NumPy, SciPy, pandas, and relevant reader versions;
- graph class, constructors, algorithms, I/O functions, and optional backend;
- weight parameter names, default edge weights, random-state behavior, and
  unsupported graph types;
- installed versus documented version mismatch.

NetworkX `3.6.1` was current on 2026-07-23. Live use always verifies the
installed version and matching documentation.

### 2. Gate 1: approve the Graph Semantics Contract

Show:

- node and edge definitions with observation grain and provenance;
- graph class, direction, multiplicity, signedness, and weight domain;
- duplicate, self-loop, isolate, missing-edge, and disconnectedness policies;
- threshold or sparsification rule and its scientific basis;
- selected algorithm assumptions and compatibility;
- comparison or null-graph proposal, compute, and artifacts;
- structure-only or synthetic verification plan.

Gate 1 authorizes only schema inspection, graph construction in memory, and
structural quality checks. It does not authorize graph statistics, random
graphs, community detection, visualization, exports, writes, backend changes,
or scientific interpretation.

### 3. Graph forms for the approved specification

Where scientifically plausible, compare only user-supplied alternatives such
as:

- weighted versus approved binary-threshold representation;
- directed versus justified undirected representation;
- full graph versus an approved component or multilayer representation.

For each show changed semantics, algorithm compatibility, information lost,
null-model implications, visible output, benefit, tradeoff, and limitation.
Do not manufacture representations to create a larger comparison.

### 4. Construct and check structure

Build the approved graph and report:

| Check | Approved rule | Observed result | Action |
|---|---|---|---|
| Nodes and unique identifiers | | | |
| Edges and duplicate relations | | | |
| Direction and reciprocity | | | |
| Weight range, signs, zeros, and missingness | | | |
| Self-loops and parallel edges | | | |
| Isolates and connected components | | | |
| Threshold and retained density | | | |
| Attribute completeness | | | |

Preserve the original edge table or adjacency representation. Never silently
coerce a directed, signed, weighted, or multigraph representation into a
simpler graph.

### 5. Document the exact graph computation

Show:

- constructor and node, edge, and attribute mappings;
- algorithm names, parameters, weight fields, normalization, and direction;
- mathematical and API assumptions for signed weights, negative distances,
  connectivity, multigraphs, and self-loops;
- component, isolate, and undefined-value handling;
- threshold, null-graph constraints, random generator, repetitions, and seeds;
- computational complexity, memory limits, backend, warnings, and failures;
- planned sensitivity checks and neutral output fields.

Centrality is an algorithmic quantity, not inherent scientific importance.
Communities are partitions produced under a specified graph and algorithm, not
confirmed biological or social groups. A visualization is not evidence of a
mechanism.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- graph state and structural quality report;
- algorithm, parameters, component policy, null model, seeds, sensitivities,
  compute, and destination;
- metric, community, path, generator, visualization, or export operation.

Reopen Gate 2 before changing the graph representation, threshold, edge
transformation, algorithm family, null constraints, backend, output format, or
destination.

### 7. Run and verify the approved graph operation

Run only the approved operation. Capture:

- source, graph-schema, code, environment, and version hashes;
- node and edge counts before and after every approved transformation;
- exact graph class, attributes, threshold, component policy, and seed;
- algorithm parameters, warnings, undefined values, and failures;
- approved threshold, weight, direction, component, or null-model
  sensitivities;
- neutral numerical output and export preview;
- specification deviations and artifacts.

Return:

```text
NetworkX Graph Record
Approved purpose and graph estimand:
Versions and API:
Node and edge semantics:
Graph class and attribute schema:
Threshold, weight, direction, and component policies:
Structural quality checks:
Approved algorithms and parameters:
Null graph, randomization, and seeds:
Neutral results:
Sensitivity results:
Warnings, undefined values, and deviations:
Specification-conformance check:
What the results do not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never infer missing-edge meaning from a file format.
- Never convert similarity to distance, signed to unsigned, directed to
  undirected, or multigraph to simple graph without approval.
- Never select a threshold, component, or community solution because it gives
  a preferred outcome.
- Verify every selected algorithm against the actual graph type and weight
  domain.
- Preserve isolates and disconnected components unless the approved
  specification says otherwise.
- Random or surrogate graphs must preserve the approved constraints and record
  the generator, parameters, repetitions, and seeds.
- Do not call central nodes important, communities natural groups, or paths
  causal routes without separate scientific evidence.
- Stop on invalid weights, unsupported graph types, outcome-dependent
  thresholds, unbounded randomization, incompatible algorithms, or graph size
  beyond the approved in-memory NetworkX boundary.

## Graph invariants and robustness checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Graph Decision Record.** Show the Graph Semantics Contract, structural checks, algorithm assumptions, and sensitivities. This prevents silent graph coercions and semantic drift. This requires detailed relation metadata. Upstream edge construction may still be biased.
- **Labeled graph-form cards.** Compare only user-approved graph representations or operation plans. This makes representational consequences visible without automatic selection. This requires an explicit candidate set. Unconsidered graph forms remain outside scope.
- **NetworkX Graph Record.** Execute one approved graph operation and verify structure before and after it. This preserves the selected graph semantics and audit trail. This slows exploratory iteration. One graph specification may be fragile.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended robustness matrix.** Add constrained null ensembles and robustness across approved graph forms. This tests selected structural alternatives. This adds compute and null-model decisions. Null ensembles remain model-dependent.
- **Graph sensitivity grid.** Add prespecified threshold, component, and null-model alternatives. This exposes dependence on consequential graph choices. This adds computations and multiplicity. This cannot eliminate construct uncertainty.
- **Verified graph-analysis bundle.** Execute the prespecified robustness grid with constrained null graphs. This quantifies sensitivity to selected choices. This requires more compute and careful multiplicity control. Robustness does not establish scientific truth.

## Checks

- **Positive:** an approved weighted directed graph produces a semantics
  contract, structural checks, compatible metric plan, and exact record.
- **Negative:** `find the important nodes` does not trigger metric selection or
  interpretation.
- **Edge:** a shortest-path request with negative distance weights stops before
  execution.
- **Threshold:** an outcome-optimized edge threshold is rejected.
- **Disconnected:** a path or centrality algorithm records component and
  undefined-value behavior rather than silently dropping nodes.
- **Handoff:** method choice returns to [cogsci-statistics](../cogsci-statistics/SKILL.md); general
  execution control may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- NetworkX. (n.d.). *NetworkX* (Version 3.6.1) [Computer software]. GitHub. https://github.com/networkx/networkx/releases/tag/networkx-3.6.1
- NetworkX. (n.d.). *NetworkX documentation* (Version 3.6.1). https://networkx.org/documentation/stable/
- NetworkX. (n.d.). *Tutorial*. https://networkx.org/documentation/stable/tutorial.html
