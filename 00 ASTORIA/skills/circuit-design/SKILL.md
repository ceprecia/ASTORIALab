---
name: circuit-design
description: >-
  Designs and analyzes the electrical plan for a device. Use for schematic,
  power and component decisions; hand verified construction inputs to Circuit
  Builder. Triggers: design this electronics circuit, select electrical
  replacement parts, analyze this power circuit.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-10-30"
---

# Circuit Design

Make the electrical plan explicit and test the behavior it claims.

## Purpose

Own electrical topology, component selection, power analysis and schematic/PCB
construction inputs. Keep one current net table as the connection authority.
Use documented behavior and calculations to compare revisable designs; an old
component choice or simulation does not establish what a device needs.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.
Detailed board assembly belongs to Circuit Builder, not this design workflow.

## Inputs

- Required electrical behavior, loads, supplies, control/sensor interfaces and limits.
- Exact existing circuit, parts, board copper/labels and completed work when applicable.
- Vendor documents, packages, fabrication constraints and available test evidence.
- Selected design scope, alternatives, hardware budget and material/inventory status.

## Steps

1. **Establish the electrical task.** Distinguish a repair, analysis, proposed circuit
   and official implementation. Reuse the existing plan. Separate required parts
   from optional improvements; do not add noise filtering or startup components
   as necessities without an applicable requirement and evidence.
2. **Inspect exact components.** Resolve manufacturer part, revision, package,
   pinout, electrical ratings and required external components from primary sources.
   Reconcile diagrams with actual copper and labels; record uncertainty rather than
   selecting a look-alike pin arrangement.
3. **Define the connection model.** Account for every used and intentionally unused
   pin, named device/control, domain and branch. Preserve controller endpoints and
   a face/orientation reference for physical contacts. Keep schematics, drawings
   and harness views generated from or compared to this one net table.
4. **Analyze operation.** Calculate relevant rail loading, signal levels, ranges,
   voltage drop, dissipation and tolerances across operating states. Include startup,
   reset, missing supply, stale command and relevant open/short cases. Identify what
   the proposed monitor or protection can detect and what remains unresolved.
5. **Develop the requested artifacts.** Produce readable schematic and selected
   component/package data. For a PCB, state outline, mounts, copper constraints,
   connectors and access. Label placement-only, unrouted and routed states accurately.
   Read and adapt `00 ASTORIA/templates/code_template.md` before authoring new generator or analysis code.
6. **Verify matching claims.** Compare exported pins and nets to the connection model;
   run applicable electrical/routing checks and analyze meaningful boundary cases.
   Distinguish ERC, DRC, simulation and measured operation. Report actual failures
   and correction effects; do not describe a logical pass as fabrication readiness.
7. **Reconcile practical scope.** Price required counts and full purchase packs with
   source/date; separate board fabrication, assembly service and unpriced materials.
   Replace obsolete parts once and reconcile shared stock without automatic credits.
8. **Return construction inputs.** Supply the selected circuit, BOM, contact-purpose
   map, placement/wiring references, analysis and device-specific measurement criteria.
   Name missing facts at the affected operation; preserve completed connections when
   only documentation changes. Circuit Builder can then supply its board walkthrough.

## Outputs

- The requested electrical plan, analysis and editable schematic/PCB or code sources.
- Required/optional parts, current prices when requested, and unresolved interfaces.
- Construction and test inputs returned to the invoking session; artifact placement
  follows `me.md`, without a competing device guide or connection authority.

## Boundaries

- A signal name or physical header position alone does not identify a device branch.
- A catalog rating, current limit or successful simulation is not a measured output.
- Do not redesign passed hardware to fix titles, pin-purpose text or render labels.
- Do not silently adopt alternatives, invent source values or turn missing evidence
  into a new approval process. Continue unaffected authorized work.

## Handoffs

- Circuit Builder receives verified construction inputs and its existing board checks.
- Wiring Design receives physical endpoint/domain requirements; 3D Builder receives
  actual board/package geometry; firmware-control receives pin and behavior contracts.
- Return cross-domain decisions to the invoking session, with evidence and options.

## Checks

- All representations agree on exact parts, pins, nets, domains and unused contacts.
- Calculations expose assumptions, units, tolerances and operating conditions.
- Optional improvements remain distinguishable from the selected required design.
- PCB and simulation completion claims match the artifacts actually checked.
- Cost scope and unmeasured hardware behavior remain explicit.
