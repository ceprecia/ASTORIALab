---
name: analysis-coordinator
description: >-
  Part 4 coordinator, help me analyze the data. Routes one bounded analysis request
  to the right method guide, modality coordinator, software adapter, model adapter,
  or computing skill from its generated catalog, grouped by family and modality.
  Separates scientific method choice from software execution, reads each skill's
  requires and gates before handing over, pauses at consequential transitions,
  and returns to the invoking companion. Use when the request is about
  preprocessing, statistics, modeling, machine learning, neuroimaging, EEG,
  genomics, or running an analysis tool. Triggers: analyze my data, which
  analysis method fits this, preprocess my imaging data, run this analysis in,
  help me pick a statistical model.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "4"
  family: part-coordinator
  modality: any
  dependencies: research-coordinator
  requires: ""
  gates: choosing a method, installing software, running on real data, accepting QC
  created: "2026-09-23"
  updated: "2026-11-01"
---

# Part 4: Help Me Analyze the Data

Part 4 of scientific inquiry: process, analyze, and reason. Separate scientific method guidance from software implementation. Load only the approved method guide, modality coordinator, adapter, or conditional shelf, and pause at consequential transitions.

## Steps

1. Confirm the request belongs to this part. Design and power questions go to stress-test-coordinator; writing up established results uses shared writing-companion/writing-coordinator while analysis and interpretation stay with their current owners.
2. Decide whether the request needs a method decision, a modality route, or an execution step. Method decisions go to a method guide; neuroimaging routes go to the modality coordinator; approved steps go to the adapter.
3. Use the catalog below to select one candidate by family and modality. Verify its installed `00 ASTORIA/skills/<name>/SKILL.md` path. The optional reference shelf lists capabilities that still need separate installation. If the specialist is unavailable, report the gap. An installed alternative may cover the same work only if it preserves the requested method or tool, stays within the approved scope and meets its own gates. Otherwise stop the affected step and return the gap to the invoking companion.
4. Read the selected installed `SKILL.md` completely. Check `requires` and `gates`; report missing software or data before proposing installation or downloads. Selection alone authorizes no installation or download.
5. Hand over the approved specification or the exact operation. Return the result to the invoking companion with the skill named, and stop at the next gate.

When the selected skill creates a new source file, follow the selected or applicable verified coding conventions. If those leave the source-file structure open, the vault-root `00 ASTORIA/templates/code_template.md` is an optional scaffold when it fits the language, task and project architecture.

## Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

### Analysis procedures
- [exploratory-data-analysis](../exploratory-data-analysis/SKILL.md) (any): Performs one approval-gated descriptive inspection of a bounded research dataset and returns an inspectable Data Structure and Quality Record. Triggers: inspect this dataset descriptively, data quality and structure check.
- [statistical-analysis](../statistical-analysis/SKILL.md) (any): Plans, executes, and verifies one approved statistical analysis through an already available and pinned implementation. Triggers: run this statistical analysis, execute the approved analysis plan.

2 skills in this part.
<!-- catalog:end -->

## Handoffs

- For requested writing support, use `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`. Return actual analysis inputs, variables/estimands, decisions, model or procedure, parameter values, output locations/version and limits through the existing research owner. The shared translator and section writer describe that evidence; they do not choose a method or compute missing results.
- A bounded request to explain an existing analysis for Methods is a read-only evidence return, not a request to rerun it or start a full method-selection intake. Reuse the relevant existing method/modality/adapter specialists and return draft passages to those owners for technical fidelity review. Preserve exploratory status, failed/partial work and user-owned interpretation.
- The human-control contract in `00 ASTORIA/skills/research-coordinator/references/research_contract.md` applies to every route. The user owns thresholds, model selection, and interpretation.
- Method before software. A method guide produces an approved specification; only then does a software adapter or model adapter execute one operation from it. Never let the available software choose the method.
- For neuroimaging requests that name no tool, use the installed coordinator for that modality first (fmri-coordinator, smri-coordinator, dwi-coordinator, eeg-coordinator, asl-coordinator, meg-coordinator, pet-coordinator). It returns one checkpointed route. Verify and load the installed skill that route names. When the request names the adapter or method guide outright ("run fMRIPrep on this dataset", "specify my fMRI GLM"), hand over directly if that skill is installed. Its own inputs and gates apply. Use step 3 for any unavailable specialist.
- For statistics and general data work, use the installed method guide (cogsci-statistics, exploratory-data-analysis, statistical-analysis) or an installed software adapter when the analysis plan is already approved.
- For genomics, pathology, animal behavior and physiology, use an installed specialist only when the project's data type requires it. Use step 3 when the relevant specialist is unavailable.
- Every adapter states `requires` (software, environment, inputs) and `gates` (installing, running on real data, accepting QC or results). Read both and pause at each gate; one approval never covers a full pipeline.
- Exploratory work stays labeled exploratory. `p > alpha` is not significant and is never reframed as marginal or a trend.
