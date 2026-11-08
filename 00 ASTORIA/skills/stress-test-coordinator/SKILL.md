---
name: stress-test-coordinator
description: >-
  Part 3 coordinator, help me stress-test my hypothesis and design. Routes one
  bounded request to the right hypothesis, design, power, paradigm, acquisition,
  or dataset skill from its generated catalog, grouped by family and modality,
  then returns to the invoking companion. Chooses no hypothesis, design, sample
  size, or dataset. Use when the request is about testability, experimental
  design, power, stimulus or task design, data standards, or whether a dataset
  can support a study. Triggers: stress test my hypothesis, design my
  experiment, is my sample big enough, which dataset can support this study, set
  up my data in BIDS.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "3"
  family: part-coordinator
  modality: any
  dependencies: research-coordinator
  requires: ""
  gates: ""
  created: "2026-09-23"
  updated: "2026-09-23"
---

# Part 3: Help Me Stress-Test My Hypothesis and Design

Part 3 of scientific inquiry: hypothesize and design. Stress-test a user-provided hypothesis, prediction, or design. Compare implications, counterexamples, power, feasibility, and threats without selecting the scientific approach.

## Steps

1. Confirm the request belongs to this part. Literature goes to scout-coordinator; an analysis of collected data goes to analysis-coordinator.
2. Read the catalog below. Match family, then modality (fmri, smri, dwi, eeg, behavior, multimodal, any), then population for datasets.
3. Open `00 ASTORIA/skills/<name>/SKILL.md` and read it completely. Check `requires` and `gates`.
4. Hand over the hypothesis, design, or dataset question exactly as the user stated it.
5. Return the result to the invoking companion with the skill named. If no skill fits, report the gap.

## Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

### Hypothesis and prediction stress testing
- [prediction-stress-test](../prediction-stress-test/SKILL.md) (any): Prospectively stress-tests one exact user-supplied or explicitly adopted hypothesis and one primary prediction for testability, discriminability, counterexamples, boundary conditions, outcome implications, and bounded novelty evidence. Triggers: is this prediction testable, stress test this prediction.

### Experimental, paradigm, and assessment design
- [experimental-design](../experimental-design/SKILL.md) (any): Compares prospective experimental-design structures for one bounded user-supplied research question, hypothesis, or prediction and constraint set. Triggers: compare experimental designs for this question, which design fits my hypothesis.
- [method-design](../method-design/SKILL.md) (any): Compares and specifies prospective computational method architectures for one user-supplied scientific objective and approved evaluation boundary. Triggers: design a computational method for this objective, compare method architectures.

### Power and sample size
- [statistical-power](../statistical-power/SKILL.md) (any): Quantifies prospective sample-size, power, minimum-detectable-effect, and operating-characteristic scenarios for one approved design and analysis specification. Triggers: power analysis for this design, how many participants do I need.

4 skills in this part.
<!-- catalog:end -->

## Handoffs

- The human-control contract in `00 ASTORIA/skills/research-coordinator/references/research_contract.md` applies to every route. The user owns the hypothesis, the predictions, the confirmatory status, and the design choices.
- Pick by family first, then by modality and population: hypothesis (testability of a prediction), design (experimental structures, paradigms, task timing, stimulus norming, assessment batteries), power (inputs specifications and sample-size calculation are separate skills), acquisition (BIDS, DICOM, conversion), datasets (whether one public dataset can support a design; each dataset skill needs its own access and data-use terms).
- Power comes in two steps. Behavioral: cogsci-power-analysis writes the Power Inputs Specification, then statistical-power calculates from it. Imaging: neuroimaging-power-guide writes the specification, then neuroimaging-sample-size-calculator calculates. A request that jumps to "how many participants" still starts at the specification unless one already exists.
- Boundary with part 2: this part stress-tests and develops the user's own prospective hypothesis or design. Critiquing an existing research object (a paper, a draft, someone else's design) belongs to challenge-coordinator and research-critique.
- A dataset skill evaluates suitability and access from public metadata. It does not create accounts, handle credentials, or download.
- One approval covers one step; the next step is a new route.
