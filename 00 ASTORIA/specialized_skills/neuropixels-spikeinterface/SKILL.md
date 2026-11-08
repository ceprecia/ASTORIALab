---
name: neuropixels-spikeinterface
description: >-
  Implements one approved nonclinical extracellular Neuropixels or
  high-density-probe checkpoint through an already available, version-verified
  SpikeInterface environment. It separates loading, preprocessing, sorting, QC,
  curation, and export; returns a source-preserving checkpoint record; and never
  treats automated curation as a unit verdict. Triggers: spike sort my
  Neuropixels recording, SpikeInterface checkpoint.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: ephys
  dependencies: ""
  requires: Python, SpikeInterface, a spike sorter
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Neuropixels SpikeInterface

## Purpose

This is the conditional Part 4 owner for one approved extracellular
Neuropixels or high-density-probe checkpoint in one existing verified
SpikeInterface environment. The checkpoints remain separate: loading and
inventory; preprocessing or materialization; sorting; post-sorting analysis
and QC; curation; and export. Approval of one never authorizes the next.

The user owns the recording, probe, population, question, acquisition,
preprocessing, sorter, parameters, QC evidence, curation, exports,
interpretation, and claims. [neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md) owns
population methods and [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inference.

Activate only for exact `neuropixels-spikeinterface` or an exact approved
handoff with a complete specification. Do not trigger from `Neuropixels`,
`spike sorting`, `Kilosort`, `SpikeGLX`, `NWB`, `unit QC`, `curate units`, or
a broad probe request.

Required intake: checkpoint; exact action and parameters; scientific status;
source, format, probe and stream, segment, channels, units, sampling,
geometry, sync, provenance, and prior transforms; existing interpreter,
Python, SpikeInterface, optional packages, sorter, platform, and hardware;
permitted reads, privacy, storage, memory, runtime, network and sealed-test
boundaries; exact staging path, output manifest, collision policy, source
preservation, verification; and visible QC or curation evidence, reviewer,
uncertainty, selected action, and affected unit IDs.

Missing facts return **Neuropixels checkpoint intake incomplete**. Never infer
them from a file, probe generation, default, metric, recipe, or package.

## Steps

### Gate 1: approve checkpoint and read-only preflight

Show specification, source and probe identity, current stage, open decisions,
selected environment, allowed reads, resources, outputs, QC or curation
evidence, and stop. Gate 1 authorizes inventory only, not computation,
installation, network, writing, curation, export, or another stage.

### Preflight and Gate 2

Verify interpreter, package and API versions, optional packages, sorter,
source and companions, geometry, resources, containment, free space,
collisions, and input invariants. Show version-qualified code or command,
exact parameters, output manifest, preservation behavior, and verification.
No fallback, glob, retry, container, download, or overwrite behavior.

Gate 2 authorizes one input, checkpoint, command, parameter set, resource
boundary, write set, verification, and return point in the existing foreground
environment. It does not authorize reruns or the next part.

### Execute once, verify, and stop

Preserve sources and partial outputs. Verify versions, command hash, warnings,
source and output hashes, paths, manifest, channels, units, sampling, time,
probe geometry, segments, state, unit IDs and spike times when relevant,
finite values, shapes, containment, no source mutation, no overwrite, and no
unexpected files.

```text
Neuropixels SpikeInterface Checkpoint Record
Approved checkpoint and specification:
Scientific status and prohibited claims:
Recording, probe, stream, segment, channel, unit, and transformation identity:
Environment, package, sorter, optional-package, platform, and hardware facts:
Preflight evidence and approved command hash:
Parameters, resource, access, output, and source-preservation boundary:
QC or curation evidence, reviewer, affected IDs, unresolved cases:
Structural verification, warnings, errors, and unexpected-file audit:
Bounded next owner and mandatory stop:
```

Success does not accept QC, validate a unit, select a sorter, interpret a cell
type, or authorize another stage.

## Boundaries

Stage rules:

- **Loading:** verify reader, AP versus LF or auxiliary stream, segments,
  sampling, channel IDs and order, units, gain or offset, geometry and probe,
  sync, companions, time base, and read mode. Multiple streams require an
  explicit selection.
- **Preprocessing:** implement only the approved ordered transform. Preserve
  channels, timing, units, probe mapping, lazy or materialized state, and
  storage effects. Source examples are not universal filter, reference,
  phase-shift, bad-channel, motion, or drift rules.
- **Sorting:** require approved sorter, exact version and parameters,
  hardware, resources, input state, output, validation, and sealed-test
  boundary. Availability is not selection. Do not install, pull containers,
  download weights, or alter parameters after failure.
- **QC and curation:** metrics, templates, waveforms, correlograms, drift,
  agreement, and model probabilities are review evidence, not unit identity or
  biological conclusions. Automated, threshold, model, or AI curation may
  prepare candidates only. It cannot delete, merge, split, classify, or export
  units without the user's separate action, visible evidence, rationale, and IDs.
  Never use credentials, remote models, or AI visual verdicts.
- **Export:** require selected artifact, format, recipient, unit set, privacy,
  manifest, destination, collision rule, and structural verification. Export
  does not validate units or authorize analysis.

Stop for missing inputs; broad pipelines; clinical or invasive-care requests;
unavailable packages or sorters; dependencies, containers, network,
credentials, downloads, missing probe or stream; insufficient storage;
collisions; automatic curation; opaque model verdicts; missing unit evidence;
source mutation; unexpected files; or failed verification. Handoff population
questions to [neural-population-analysis-guide](../neural-population-analysis-guide/SKILL.md), inference to
[cogsci-statistics](../cogsci-statistics/SKILL.md), and missing methods, sorters, or curation to a verified
owner or explicit gap.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- [SpikeInterface Neuropixels guide]. (n.d.). SpikeInterface documentation. https://spikeinterface.readthedocs.io/en/stable/how_to/analyze_neuropixels.html
- *SpikeInterface documentation*. (n.d.). https://spikeinterface.readthedocs.io/en/stable/
