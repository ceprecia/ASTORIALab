---
name: mechanism-design
description: >-
  Analyzes mechanical operating principles and develops bounded mechanism
  concepts. Use for transmission, load, travel and fabrication tradeoffs; return
  geometry requests to 3D Builder. Triggers: compare mechanical transmissions,
  size this actuator mechanism, explain how this mechanism moves.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-10-30"
---

# Mechanism Design

Explain the motion, load path and practical construction of one mechanism.

## Purpose

Own operating principles, mechanical concepts and bounded sizing for a device or
subassembly. For reverse engineering, distinguish observed target behavior,
documented claims, comparison mechanisms and proposed implementations. Revise or
abandon a hypothesis when the evidence changes; a previous concept is not a rule.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.
CAD authoring stays with 3D Builder; this skill supplies its mechanical brief.

## Inputs

- Intended function, load, travel, speed, duty and dimensional or material constraints.
- Exact target or candidate, drawings, source parts, measurements and existing work.
- Available components and fabrication methods, with unknown access or stock explicit.
- Current electrical, sensing and packaging interfaces; distinguish targets from ratings.

## Steps

1. **Bound the question.** Identify the mechanism and requested decision. Reuse the
   selected baseline and completed work. Keep a target explanation separate from a
   replica design, and name any unsupported feature needed by the latter.
2. **Inspect the interfaces.** Read the actual part sources before inventing geometry.
   Identify shaft, bore, thread, bearing, attachment and cable interfaces on both
   sides. A generic part label or plausible render does not establish compatibility.
3. **Trace operation.** Show input, transmission, reaction, output and return paths.
   Describe engaged, released and travel-limit states, including slack, friction,
   backlash and backdrive where relevant. Name what prevents or permits motion.
4. **Calculate within known inputs.** Use explicit units and equations for travel,
   ratios, torque, force or spring behavior as needed. State assumptions and their
   sensitivity. Do not translate holding-force advertising into delivered output
   without the contact geometry and applicable load model.
5. **Compare practical concepts.** Compare only useful alternatives against the same
   function. Include fabrication operations, tools, materials, access and tradeoffs.
   Separate consumed material, purchased stock and unfinished-part fabrication cost.
6. **Specify the chosen proposal.** Give stable part IDs, datums, axes, travel,
   mating features and dimension evidence. Identify critical tolerances and load
   paths without inventing manufacturing precision. Keep unselected options explicit.
7. **Define the discriminating check.** For the main uncertainty, describe one
   calculation or measurement, expected observation and criterion that would change
   the proposal. Check one critical coupling through its required stroke before
   assuming a repeated assembly works. Separate proposed tests from observations.
8. **Return an actionable handoff.** Supply the geometry brief, operating states,
   required clearances and unresolved interfaces. State which dependent designs
   need reconsideration; preserve checks unaffected by the change.

## Outputs

- A concise operating explanation and requested concept, calculation or layout.
- Mechanical interfaces and a bounded comparison with the next useful check.
- Requested editable deliverables in their owning location, with findings and limitations in the requested report or the recipient's chosen reporting form. Return through the invoking session; saving a separate artifact requires authorization.

## Boundaries

- CAD dimensions, analytical estimates and physical measurements remain distinct.
- Do not invent a fitted part from an image or claim strength, fatigue, friction,
  spring return or loaded release from a collision-free model.
- Do not redesign a completed assembly to repair labels or explanatory figures.
- A missing critical dimension limits the affected claim; continue useful analysis
  with named assumptions instead of adding a project-wide approval checkpoint.

## Handoffs

- Give 3D Builder the dimensioned mechanical brief; fit-review critiques the whole
  arrangement independently. Return their findings without taking over CAD files.
- Give circuit-design actuator demand and interfaces; sensing-calibration receives
  transmission geometry and intended measurement. Assembly Builder owns construction.
- Return bounded findings to the invoking session; do not start another project hub.

## Checks

- Equations, units, source dimensions and load directions agree with the explanation.
- Every important mating feature and return path is accounted for or visibly unknown.
- Concept comparisons have equivalent scope and do not duplicate shared stock costs.
- Claimed motion and performance stay within inspected states and evidence.
- A contrary observation can revise the mechanism without preserving an old conclusion.
