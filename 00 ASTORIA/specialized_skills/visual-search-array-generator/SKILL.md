---
name: visual-search-array-generator
description: >-
  Specifies, generates, and validates deterministic layout manifests for one
  approved controlled-array visual-search task. Use when the request, or a stage
  coordinator, hands over an explicitly matching task. It maps display geometry,
  visual units, item bounds, feature assignments, target placement, spacing,
  set-size cells, randomization, seeds, and validation invariants; compares
  feasible generation algorithms; and generates only the user-selected bounded
  batch after two approval gates. It does not choose the paradigm or scientific
  parameters, use inherited defaults, build a task runner, install packages,
  analyze search performance, search, save, or render production stimuli without
  separate approval. Triggers: generate visual search arrays, visual search
  stimulus layouts.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: behavior
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Visual Search Array Generator

Generate controlled visual-search layouts without hiding scientific choices inside an array algorithm.

## Purpose

`visual-search-array-generator` is the Part 3 canonical owner for prospective specification, deterministic generation, and constraint validation of synthetic layout manifests for one approved controlled-array visual-search task.

It owns:

- translating user-selected display geometry and visual units into an explicit coordinate system;
- comparing feasible array-placement algorithms under approved spatial constraints;
- assigning target, distractor, feature, position, set-size, and condition fields from an approved design;
- generating a bounded manifest with recorded seed, runtime, algorithm, and parameter provenance;
- validating counts, boundaries, distances, positions, feature balance, target balance, reproducibility, and failed-placement behavior;
- producing a selection-bound Array Generation Specification, generated pilot or production manifest, and Constraint Validation Report.

The user owns the construct, hypothesis, prediction, decision to use visual search, search manipulation, target and distractor definitions, feature dimensions, set-size levels, target prevalence, trial-cell counts, display geometry, spacing and crowding rule, timing, condition balance, randomization constraints, outcome, estimand, analysis, and scientific claims.

[cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) owns selection and high-level specification of the visual-search paradigm. [experimental-design](../../skills/experimental-design/SKILL.md) owns conditions, units, allocation, and general counterbalancing. [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) owns participant, item, trial, session, reliability, data-loss, and effect-evidence inputs.

This skill creates array layouts and manifests. It does not create a full experiment, participant interface, response handler, trial scheduler, analysis pipeline, or real-world scene-search task.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

[research-coordinator](../../skills/research-coordinator/SKILL.md) or another verified Active capability may route an explicitly matching task from the live [Skill Map](../../Skill%20Map.md).

Do not activate from:

- `design a visual-search study`;
- `which attention task should I use`;
- `analyze my search slopes`;
- `make a natural-scene search task`;
- `render these stimuli`;
- broad phrases such as `visual search`, `arrays`, `stimuli`, `pop-out`, or `attention`.

One run covers one approved controlled-array visual-search paradigm and one display-geometry family.

Several experimental cells may share one run only when they use the same coordinate system, display geometry, item-bound rules, placement algorithm, and validation logic. Separate materially different displays, viewing distances, devices, naturalistic scenes, three-dimensional layouts, dynamic stimuli, eye-contingent displays, or modality requirements.

No source number is a default. This includes eccentricity, spacing, item size, set sizes, target prevalence, trial counts, fixation duration, deadlines, feature differences, slope thresholds, randomization limits, and algorithm settings.

## Inputs

Gather:

- approved [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) Cognitive Paradigm Specification or equivalent visual-search task decision;
- approved [experimental-design](../../skills/experimental-design/SKILL.md) condition, unit, assignment, and counterbalancing structure;
- exact target, distractor classes, feature dimensions, similarity manipulation, and nuisance controls selected by the user;
- selected set-size cells, target-presence cells, condition cells, and requested manifest count per cell;
- physical display width and height, pixel resolution, viewing distance, scaling, orientation, and usable region, or an explicit uncalibrated pixel-only boundary;
- coordinate origin, axes, units, allowed region, fixation region, edge margins, item anchors, item extents, and overlap definition;
- selected spacing or crowding constraint and its exact evidence or pilot basis;
- selected eccentricity, quadrant, hemifield, ring, or region constraints;
- feature values, device calibration, color or luminance status, line width, orientation, size, shape, and rendering assumptions;
- target-location and distractor-composition balance rules;
- trial-order or run-length constraints only when approved by [experimental-design](../../skills/experimental-design/SKILL.md);
- random seed policy, requested output schema, batch scope, file format, and preview needs;
- runtime and standard-library availability, or permission to perform a read-only availability check;
- outcome visibility, confirmatory status, protocol, preregistration, deviations, supplied evidence, desired output, and stop point.

Mark an essential missing item `unknown`. Do not substitute a value from the source YAML.

## Steps

### 1. Build the Array Generation Brief

Show:

| Field | Required content |
|---|---|
| Study and stage | Exact bounded study and Part 3 task |
| Scientific target | The user's exact construct, question, hypothesis, or prediction |
| Approved paradigm | Exact controlled-array visual-search family and variant |
| Approved design | Conditions, cells, units, set sizes, target presence, and counterbalancing |
| Target and distractors | Exact classes, features, similarity manipulation, and controls |
| Display geometry | Physical dimensions, resolution, scaling, viewing distance, usable region, and calibration status |
| Coordinate system | Origin, axes, units, anchors, extents, boundaries, fixation, and margins |
| Spatial constraints | Spacing, crowding, overlap, eccentricity, quadrant, and region rules |
| Feature constraints | Color, luminance, orientation, size, shape, and calibration |
| Balance constraints | Target positions, distractor composition, conditions, cells, and order |
| Batch scope | Pilot or production, trials per cell, item rows, expected size, and output format |
| Randomness | Seed policy, runtime, algorithm version, and reproducibility requirement |
| Validation | Exact invariants and preview or inspection plan |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Evidence boundary | Supplied material that may be inspected |
| Excluded work | Scientific parameter selection, task runner, rendering, deployment, power, analysis, search, installation, and saving |
| Stop point | Exact output or decision that ends the run |

Estimate the output scale before approval: number of trials, number of item rows, approximate serialized size, and requested previews. Do not generate an unbounded manifest.

### 2. Gate 1: approve the constraint and algorithm-comparison boundary

Ask the user to approve or correct the Array Generation Brief, constraint definitions, candidate algorithm classes, validation plan, and batch-size estimate.

Gate 1 authorizes only:

- inspection of the displayed inputs and evidence;
- geometry and feasibility checks;
- comparison of placement and assignment algorithms;
- design of the manifest schema and validation invariants;
- preparation of response options.

It does not authorize:

- selecting a scientific parameter, algorithm, seed, relaxation rule, or batch size;
- generating arrays, running code, rendering stimuli, installing software, saving, or starting another capability.

If the paradigm, target, distractors, set sizes, display geometry, spatial rule, feature rule, balance rule, output schema, runtime, or batch scope changes materially, rebuild the brief and repeat Gate 1.

### 3. Build the Display Geometry and Constraint Map

| Field | Required content |
|---|---|
| Geometry source | Measured, manufacturer reported, platform reported, user supplied, or unknown |
| Coordinate domain | Degrees, pixels, centimeters, normalized units, or another exact unit |
| Conversion | Formula, inputs, axes, scaling, pixel aspect, and rounding rule |
| Usable region | Shape, bounds, masks, margins, and excluded regions |
| Fixation region | Center, extent, item exclusion, and verification |
| Item geometry | Anchor, visual extent, collision shape, orientation, and stroke |
| Spacing rule | Center or edge metric, direction dependence, item pair types, and evidence |
| Eccentricity rule | Reference point, radial definition, bins, limits, and evidence |
| Feature calibration | Color space, luminance, contrast, gamma, device status, and limits |
| Post-conversion check | Exact pixel-space invariants |

For degrees-to-physical-size conversion, show the geometry and units. Do not assume small-angle approximations when exact conversion is feasible. Convert horizontal and vertical axes separately when physical dimensions or pixel scaling differ.

### 4. Build the Constraint and Evidence Register

Create one row per constraint:

| Field | Required content |
|---|---|
| Constraint ID | Stable identifier |
| Constraint | Exact mathematical or categorical rule |
| Scope | Item, pair, array, cell, block, batch, or display |
| Value or function | user-selected value, supplied range, or `unknown` |
| Unit and geometry | Exact measurement basis |
| Provenance | The user supplied, verified exact source, verified translation, external candidate, or AI-generated option |
| Applicability | Stimulus, task, eccentricity, population, device, and setting match |
| Hard or soft | Whether generation may violate it |
| Failure behavior | Reject candidate, retry, fail trial, fail batch, or return to the user |
| Validation | Exact test and tolerance |
| Status | Eligible, eligible with translation, unresolved, or reject |

Hard constraints may never be silently relaxed. A retry cap is an engineering guard, not permission to weaken the design.

### 5. Build the Generation Algorithm Option Matrix

Generate two to four `AI-generated generation algorithm option` entries only when feasible. Common candidate classes include:

- approved candidate locations followed by constrained sampling;
- grid or lattice positions with bounded jitter;
- rejection or dart-throwing placement under an exact distance rule;
- concentric or region-stratified candidate positions;
- a user-supplied deterministic layout family.

| Field | Required content |
|---|---|
| Option ID | Stable label |
| Candidate-space method | How positions are defined |
| Placement order | Target-first, all-items jointly, stratified, or supplied order |
| Constraint enforcement | Exact hard and soft checks |
| Balance method | Target position, eccentricity, quadrant, feature, and cell balance |
| Randomness | PRNG, seed derivation, draw order, and determinism |
| Infeasibility behavior | Retry cap, diagnostics, and stop |
| Bias risk | Edge, density, order, discretization, rejection, or target-placement bias |
| Computational burden | Expected attempts, scaling, and batch limits |
| Evidence status | Verified method, user supplied, external candidate, or AI-generated |
| Validation plan | Invariants, simulations, preview, and reproduction test |

If only one algorithm can satisfy the approved constraints, explain why and do not invent alternatives.

Do not select an algorithm because a package implements it. Do not import the source YAML's `max_attempts`, grid jitter, rings, target balance, or run-length values.

### 6. Define the manifest and balance plan

At minimum, each trial record must preserve:

- trial ID, cell ID, condition labels, set size, and target-presence status;
- master seed, trial seed or deterministic derivation, algorithm ID, and generator version;
- display and coordinate-system ID;
- requested target location stratum and realized location;
- generation attempts, status, and failure reason;
- item records in a stable order.

At minimum, each item record must preserve:

- item ID and role;
- target or distractor class;
- continuous and rendered coordinates;
- anchor and extent;
- eccentricity and region labels when applicable;
- feature values with units and calibration status;
- pairwise or nearest-neighbor validation summary;
- any source-item or stimulus-family identifier.

Define exact expected counts and balance tolerances before generation. A target-position balance plan is not the same as participant allocation or trial order.

### 7. Build the Array Threat Register

Assess:

- set size confounded with display area, density, eccentricity, or item spacing;
- target location, quadrant, eccentricity, or edge bias;
- target-distractor and distractor-distractor similarity drift;
- unintended color, luminance, contrast, size, orientation, shape, or spatial cues;
- crowding, overlap, fixation masking, clipping, and pixel-rounding violations;
- candidate-position or rejection-sampling bias;
- infeasible dense cells and selective loss of difficult layouts;
- repeated arrays, repeated positions, feature imbalance, and accidental regularity;
- predictable seed derivation, runtime-version drift, and nonreproducible iteration order;
- target prevalence or sequence constraints altering behavior;
- calibrated-lab assumptions applied to uncontrolled remote devices;
- rendered output differing from the manifest;
- naturalistic or scene-search claims inferred from synthetic arrays.

For each threat show affected cell, indicator, severity, mitigation candidates, residual risk, owner, and unresolved decision.

### 8. Present response options

For every consequential choice, offer only applicable options:

- retain an eligible constraint or algorithm;
- return the value or function to the user;
- translate evidence with displayed geometry and assumptions;
- reduce or change the approved design through its owner;
- generate a small pilot batch for constraint testing;
- request a bounded [research-literacy](../../skills/research-literacy/SKILL.md) audit or [paper-search](../../skills/paper-search/SKILL.md);
- prepare a display-calibration, task-runner, rendering, accessibility, privacy, power, or analysis handoff;
- defer generation.

Do not recommend a scientific parameter.

### 9. Gate 2: The user selects the generation specification and batch

Ask the user to select:

- coordinate and conversion rules;
- hard and soft constraints;
- placement and assignment algorithm;
- seed policy and deterministic draw order;
- manifest schema and balance tolerances;
- exact pilot or production batch size;
- runtime and permitted execution boundary;
- preview and validation requirements;
- unresolved items and selected handoff packets.

Gate 2 authorizes only the selected bounded in-chat generation and validation run when a verified available runtime can perform it without installation.

It does not authorize:

- changing scientific parameters or silently relaxing constraints;
- installing packages;
- writing files, rendering production assets, building a task runner, deploying, collecting data, searching, or analyzing performance.

File creation, production rendering, or another capability requires separate approval. Do not infer selection from silence.

### 10. Generate and validate the selected arrays

Before execution:

1. echo the exact generation specification, runtime, algorithm, seed, batch size, expected rows, and output mode;
2. run a deterministic preflight on the smallest meaningful cell;
3. fail visibly if any required input or runtime feature is unavailable;
4. generate only the approved batch;
5. validate every trial and batch invariant;
6. rerun a deterministic sample from the recorded seed and compare exactly;
7. report all failures, retries, and exclusions without replacement bias;
8. return a compact manifest preview and validation summary.

Do not regenerate until a passing batch appears. If a trial is infeasible, retain the failure record and return the constraint conflict to the user.

## Outputs

Include the applicable evidence and outputs below in the form and order selected for this task. If the user leaves these choices open, follow the recipient's applicable reporting policy. With neither specified, use a concise report organized around the current decision. Keep the technical steps and gate-dependent records in their required sequence.

- **Array Generation Brief**
- **Display Geometry and Constraint Map**, after Gate 1
- **Constraint and Evidence Register**
- **Generation Algorithm Option Matrix**
- **Manifest and Balance Plan**
- **Array Threat Register**
- **Response Options**
- **Array Generation Specification**, only after Gate 2
- **Generated Manifest Preview**
- **Constraint Validation Report**
- **Selected Handoff Packets**, when requested

At either gate, stop after showing the material needed for the user's decision. Do not simulate approval.

Return the results in the current task's requested form or under the recipient's existing reporting policy. Gate 2 may authorize the displayed bounded computation, but neither gate authorizes file writes, production rendering, task construction, deployment, software installation, source modification, searching, or another capability.

Before any separately approved save or external action:

1. show the exact destination or action;
2. show the exact format, file count, row count, size estimate, and overwrite behavior;
3. show validation and recovery behavior;
4. ask for approval;
5. verify the result afterward.

For an authorized save, use the verified destination selected for the task. If none is selected, use the workflow's established project-owned scientific destination where it applies. For other supporting content, use a destination established by the recipient's placement policy, including Resources when that policy selects it. Skill and system work stays in `00 ASTORIA/`. Ask once if required ownership or destination remains unresolved. Add a verified link at the selected location only when the authorized scope includes that edit.

## Boundaries

Geometry and unit rules:

- Prefer degrees of visual angle only when physical display dimensions, resolution, scaling, and viewing distance are known and verified.
- Preserve both continuous design coordinates and final pixel coordinates when conversion occurs.
- State whether an extent is radius, diameter, bounding-box width, center-to-center distance, or edge-to-edge distance.
- Validate constraints again after pixel rounding, because rounding can create boundary, overlap, or spacing violations.
- If display geometry is unknown or uncontrolled, use pixels and explicitly prohibit visual-angle, acuity, crowding, or eccentricity claims.
- Do not describe RGB values as device-independent or isoluminant without calibration evidence.
- Do not use one scalar crowding rule as a universal law. Critical spacing depends on eccentricity, direction, stimulus, task, similarity, and other conditions.

Edge cases:

- **Visual search not selected**: Route to [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) and stop.
- **No approved design or cells**: Route to [experimental-design](../../skills/experimental-design/SKILL.md).
- **No calibrated display geometry**: Use pixels and prohibit visual-angle or crowding claims.
- **Remote uncontrolled devices**: Preserve device variability and do not claim lab-calibrated size, spacing, color, luminance, or timing.
- **Unknown item extent**: Do not validate center spacing as if it guaranteed edge clearance.
- **Dense cell is infeasible**: Report the exact conflicting constraints; do not shrink items, expand the region, reduce spacing, or drop trials silently.
- **Pixel rounding creates a violation**: Reject or regenerate according to the approved rule and retain the failure record.
- **Only one feasible algorithm**: Explain the constraint and do not invent alternatives.
- **Source supplies a default number**: Mark it unverified until exact-match evidence and the user selection.
- **Color or luminance manipulation**: Require device and calibration evidence; RGB values alone are insufficient.
- **Crowding rule requested**: Require the exact task, stimulus, eccentricity, direction, population, and criterion basis.
- **Low-prevalence condition**: Preserve it only when the user and [experimental-design](../../skills/experimental-design/SKILL.md) selected it; flag behavioral consequences and do not change it.
- **Target-absent trials**: Validate distractor composition independently rather than copying a target-present array and deleting the target if that changes density or balance.
- **Repeated seed or duplicated layout**: Report it and apply only the approved uniqueness rule.
- **Runtime unavailable**: Return the specification and stop. Do not install software.
- **Naturalistic scenes or real images**: Route to a scene-search specialist and stop.
- **Rendering requested**: Prepare a separate bounded render and visual-QA handoff.
- **Observed RT, accuracy, or slope data supplied**: Route to Part 4. Do not classify search type here.
- **Outcomes already inspected**: Do not alter generation parameters and relabel the change confirmatory.
- **Context compaction or model switch**: Reload this skill and the approved brief before continuing.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when visual search is not selected or the paradigm, target, distractor, manipulation, outcome, or estimand is unresolved.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) for conditions, units, set-size factors, target-prevalence factors, trial-cell allocation, participant assignment, and broad counterbalancing.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) for participant, item, trial, session, reliability, data-loss, and effect-evidence inputs.
- Use [statistical-power](../../skills/statistical-power/SKILL.md) for numerical sample-size, power, MDE, or operating-characteristic calculation.
- Use [research-critique](../../skills/research-critique/SKILL.md) to critique an existing visual-search design or generator.
- Use [research-literacy](../../skills/research-literacy/SKILL.md) for one bounded methodological claim and [paper-search](../../skills/paper-search/SKILL.md) for a separately approved evidence search.
- Route display calibration, rendering, task-runner implementation, eye tracking, EEG, MEG, fMRI, naturalistic scenes, accessibility, deployment, and observed-data analysis to their approved owners.

Each destination begins its own workflow and gates. Array Generator approval does not authorize another capability.

This skill does not select the paradigm or scientific parameters, classify a result as pop-out or serial search, infer a cognitive process from a slope, choose a target-prevalence condition, install software, build or deploy a task, render production assets, search, save, collect data, analyze outcomes, or make a scientific conclusion for the user.

## Checks

For every trial verify:

- exact item count and target count;
- every item is within the approved usable region after rendering conversion;
- fixation, margin, mask, and excluded-region rules;
- no overlap under the selected item geometry;
- every applicable pairwise spacing or crowding rule;
- exact target and distractor feature assignments;
- approved feature ranges and calibration labels;
- target position, eccentricity, quadrant, and region requirements;
- no unapproved constraint relaxation;
- stable item ordering and complete provenance.

For the batch verify:

- exact trial count per approved cell;
- target-presence, set-size, target-location, feature, and distractor-composition balance within tolerances;
- no unapproved duplicate layouts;
- retry and failure rates by cell;
- no selective omission of dense or difficult cells;
- deterministic regeneration under the recorded runtime and seed;
- manifest schema, types, units, and identifiers;
- output-size and preview limits;
- a separately rendered sample matches the manifest when rendering is later approved.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Duncan, J., & Humphreys, G. W. (1989). Visual search and stimulus similarity. *Psychological Review, 96*(3). https://doi.org/10.1037/0033-295X.96.3.433
- Pelli, D. G., & Tillman, K. A. (2008). The uncrowded window of object recognition. *Nature Neuroscience, 11*. https://doi.org/10.1038/nn.2187
- Strasburger, H. (2020). Seven myths on crowding and peripheral vision. *i-Perception, 11*(3). https://doi.org/10.1177/2041669520913052
- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin and Review, 28*(4). https://doi.org/10.3758/s13423-020-01859-9
- Wolfe, J. M., Horowitz, T. S., & Kenner, N. M. (2005). Rare items often missed in visual searches. *Nature, 435*. https://doi.org/10.1038/435439a
