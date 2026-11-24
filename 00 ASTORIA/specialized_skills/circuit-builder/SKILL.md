---
name: circuit-builder
description: >-
  Guides a beginner through building and checking a circuit board from a
  verified wiring plan: how to read the board and the drawing, a parts and tools
  table, hole-by-hole steps naming each contact's device and purpose, and a
  generated continuity and power-up test table; runs the engineer's verification
  gates (design, before the first joint, before power, staged power-up) as fault
  finding with corrections. Use for perfboard and solderable-breadboard builds,
  stuffing a through-hole PCB, a two-pad SMD swap, or a solderless-breadboard
  prototype; it never designs the circuit or chooses parts, and sends unverified
  designs back to circuit-design first. Triggers: walk me through soldering
  this, help me build this board, check my wiring before power, is my circuit
  wired correctly, guide me through this PCB build.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  requires: a placement table and wire list or a PCB with BOM; multimeter with continuity mode; python3 with matplotlib for the helper scripts
  gates: before the first joint, before power, before the device touches a person
  created: "2026-10-06"
  updated: "2026-10-31"
---

# Circuit Builder

Build it hole by hole, understand every joint, and test it before power.

## Purpose

Turns a verified wiring plan (placement table plus wire list, with or without a drawing; or a fabricated PCB plus its BOM) into a walkthrough that a person who has never soldered can follow and check, and runs the engineer's verification gates around that build. The reader does not know what a rail is, which side is soldered, or which end of a diode is which; every step tells them.

Covers solderable breadboards and perfboard using their verified connectivity and geometry, stuffing a through-hole PCB from a silkscreen and BOM, a two-pad SMD swap (a shunt or pull-up resistor), and solderless-breadboard prototyping before soldering.

Read `00 ASTORIA/systems/Engineering System.md` and follow its shared engineering policy and role boundaries. The official BOM remains the baseline when a project uses a local board implementation. Return the electrical subassembly to Assembly Builder when it owns the complete device guide; standalone circuit walkthroughs keep the detailed Part 0 to Part 4 workflow below.

Never designs the circuit, chooses parts, or models the electronics; when the plan is unverified it names what is missing (net table, pinouts, analysis) and sends the work back to circuit-design first. That skill owns electrical design, part selection and the canonical electrical plan. Not for SMD rework beyond two pads or for enclosure machining.

## Inputs

- Board type and verified geometry. Use the supplied photo or drawing to identify the board when possible. Ask if its identity or geometry remains unresolved.
- Placement table (part, holes, orientation) and wire list (number, net, from, to, what it connects). For a PCB: BOM with designators and the silkscreen.
- The drawing and its colour legend, if there is one.
- The selected device revision, official BOM and wiring/assembly documentation, plus the project's physical inventory evidence. Use the shared inventory states; an order list alone does not confirm a part is on hand.
- Both sides of every external connection: actual contact type, pitch, pin order, polarity, orientation and cable/adapter availability. Include completed joints and passed checks when continuing a build.
- A per-contact purpose map: contact ID, exact hole/pad, named device or control, terminal function, and supplied voltage/net/controller endpoint. Shared power or ground contacts still name their assigned device branch. Do not infer device order from consecutive contact numbers. State unused contacts explicitly.
- The viewing reference for terminal positions: source photo or drawing, component face, orientation landmarks and which way terminals point. Preserve a user-supplied pin assignment as that user's identification; do not present it as an independently measured pinout or silently apply it to the reverse view.
- Which modules plug in (never soldered) and which parts are polarised.
- A photo of every module's top side with the printing readable, and the module set on the board once to see which columns its pin rows drop into (Gate 0b); the plan's sockets and artwork use that measured spacing, never a look-alike's datasheet.
- Gate 0 evidence: the net table, ERC and netlist comparison, layout check, electrical analysis. If none exists, say so before writing steps.
- A plan file for the helpers (`plan.json` with board, parts, wires, rails, pins, components, joins, polarised and headers). Include the verified connector map in `connectors` when it applies. Use a matching `ref` on the part and connector, and list the connector contacts in `pins` with their verified `pin`, `hole` and `net`. Set `board` to the verified preset name or supply a verified geometry object. Write the plan from the placement table and wire list before Part 3. It drives the steps, the tests and every figure.

A wire list without a "what it connects" column is completed from the nets before writing; a step without a reason is not acceptable.

The helpers accept `contacts` on each header, pigtail or panel part. Each entry uses `pin`, `hole`, `device`, `function`, and optional `net`, `voltage`, `controller_endpoint`, `no_connect`. Use `no_connect: true` with a null/NC net and an explicit unused role when the plan leaves a contact unassigned. `contact_purpose_rows(part, connectors)` matches these annotations to the referenced connector's pin/hole/net identity and returns one row per physical hole. It reports missing purpose as UNRESOLVED and rejects duplicate or conflicting identities. These annotations describe the verified plan; they never change its electrical connections. Add transient annotations in an existing guide generator when only documentation needs repair, without rewriting a completed circuit plan.

## Steps

1. **Gate 0, design verification.** Use circuit-design's canonical electrical plan and run `./references/verification.md` Gate 0: one net table as truth, bought-board nets re-derived from the copper, module pinouts from the vendor page, every pin on a net or no-connect, ERC 0 and netlist match, `layout_check` (in `./scripts/board_tools.py`; `python3 ./scripts/board_tools.py plan.json` prints steps, tests and findings) with no findings, electrical analysis including the fault matrix. A passed gate is recorded and not repeated unless the design changed. Unverified design: stop here, name what is missing and return that design work to circuit-design.
2. **Gate 0b, parts in hand.** Before any hole is fixed, run `./references/verification.md` Gate 0b for every module and bought board: identity from the printing, pin count and order read label by label, row spacing by fitting the module on the actual board (`row_spacing_from_columns`, `columns_for_spacing`), body size, markings and jumpers, accessories fitted or missing, polarity references. Every plan assumption gets a dated evidence line in the project's verified facts; a difference updates the net table or layout first, then everything is regenerated from it. `parts_check_table` renders the checklist the user works through.
3. **Part 0, how to read the board.** The primer for the board type from `./references/boards.md`: row and column naming, which holes copper already joins (strips, rails, taps), parts in from the printed side and soldered on the back, left and right swap on the back, mark row 1 and the used rails on both sides first. Include the board-reading primer even for a repeat build. Adapt its presentation to the selected reporting form.
4. **Part 1, how to read the drawing.** Decode every colour and every drawn block; name the wires hidden under a module (they are soldered first). For a PCB, explain designators, silkscreen outlines and polarity marks. A square pad or silkscreen mark can be a clue to pin 1. Confirm pin 1 and the viewing side against the selected footprint and component documentation.
5. **Part 2, what you need on the table.** Present the tools, consumables and parts with their quantities and shared inventory states in the selected reporting form. Include supplies and tools an order list usually omits (solder wire, flush cutters, stripper, foam tape, screws, tip cleaner, safety glasses). Flag stranded wire (twist and tin before it goes in a hole) and header strips that need cutting (cut through the next position). Keep official requirements and local board additions distinguishable. Explain the verified soldering process once: heat the pad and lead together, feed solder to the joint, remove solder then heat, and let it solidify without movement. Use the component/board/alloy guidance for temperature, dwell and wetting; inspect joint geometry and bridges without imposing universal shine or timing. Keep heat away from header plastic and modules according to their ratings. Show `./assets/joint_guide.png` (good wetting, incomplete wetting, starved and bridged, with process-specific checks) here. **Gate 1** closes here after checking the parts against the verified inventory, finding polarity marks, reading the silkscreen, marking the board and checking the meter against a known reference.
6. **Part 3, the steps in build order.** `order_build_steps(parts, wires, board=plan["board"], connectors=plan.get("connectors"))` checks contact annotations against the verified connector map when supplied and gives the phases: hidden wires under a module footprint; polarised parts with the mark checked before heat; headers pushed onto the module first so the module is the jig, one end pin per header, check it stands square, then the rest within the verified component and process heat limits, module out; remaining wires; leads that leave the board with strain relief; trim and inspect; modules plugged in only after Gate 2. Each step states the exact holes, how (bend, insert, flat, solder, trim), the check before heat for anything orientation-dependent, and what it does: which pins it joins and why the circuit needs it. Figures, all generated from the plan by `./scripts/draw_build.py` so no hole is placed by eye: the step panels (`<prefix>_steps.png`, one board per step, finished work faded, current holes ringed and named), the mirrored back view (`<prefix>_back.png`, every solder point numbered in build order, the view the user has while soldering), `./assets/header_jig.png` at the header step, and, for an actual diode with both terminal holes verified, the diode terminal map (`polarity_guide.png`). Supply explicit anode and cathode hole fields in the verified plan. They must match the declared diode holes and any matching build part. An unresolved mapping omits the terminal map. Verify package markings from the component documentation and supply an explicit `marked_terminal` when displaying a marked end. Other polarized parts get their component-specific orientation view. For a PCB, fit the lowest parts first, then sockets and headers, capacitors and tall parts, and connectors. Socketed integrated circuits (ICs) go in last. Keep them out through the applicable Gate 2 checks. After those checks pass, follow the verified Gate 3 sequence, including any earlier stages that call for empty sockets. With power removed and stored energy discharged as the plan specifies, seat only the ICs required for the upcoming stage. Apply power with that stage's required loads and isolation in place. For a solderless breadboard, keep power off while wiring the supply rails first, then the ground wires, then the signal wires. Keep removable modules out during the applicable Gate 2 checks. After the required checks pass, keep power off while inserting the modules specified for the next stage, then follow the verified plan's Gate 3 power-up sequence.

   Name the operation and component directly in each title, such as “Connect the servos.” Inside each connection step, list **every contact separately** with its exact hole, named device/control and terminal function; retain supplied voltage, net and controller endpoint. A header range, net name, general purpose paragraph or link to an earlier wiring section does not replace this map. Keep the complete contact map with the step being followed, including middle contacts, shared supply/ground branches and calibration/reference contacts. Generic figures keep the complete map in their caption area rather than truncating it to fit. Preserve existing geometry when only labels or explanations change.
7. **Part 4, testing before power.** Pass `board=plan["board"]` to `continuity_checks` and render its rows with `markdown_table`. Each row names probe locations, meter mode, the verified plan's acceptance criterion and its source. Include every wire and applicable adjacent header pair. Differently named rails or polarized parts do not establish a universal silence or diode criterion; missing criteria remain UNRESOLVED. Use the plan-driven test figures to locate checks. They label red and black leads only for complete meter checks with an explicitly verified probe assignment and a numeric measurement criterion and a numbered plan source. Free-text criteria identify locations with neutral markers. A check with a structured assignment must omit free-text `expect` and `basis`. Use the verified table for the exact acceptance criterion and source, and resolve any conflict before testing. Gate 2 closes only for the tests actually specified and checked. Gate 3 uses the verified design's power stages, required loads, applicable bus/sensor inputs, functional tolerances and device-specific connection sequence.
8. **Fault finding.** Report each failed check with its symptom, cause and correction using the tables in `./references/verification.md` and `./references/polarity_and_faults.md`. Repeat the checks affected by the correction and preserve unchanged passes. Report unresolved results as UNRESOLVED. Resume the affected work only after the required checks pass. Other authorized work may continue when it does not depend on those checks.
9. **Close.** A short list of what is still needed from the user (which module variant is in hand, whether a part has arrived) and what the next session covers. Define terms at first use in the walkthrough, using `./references/glossary.md` as the fallback list. Include a standalone build glossary when the reader requests one or the applicable configured reporting form calls for one.

## Outputs

- Present the walkthrough in the current task's requested form or under the recipient's existing reporting policy. Keep the technical sequence from board and drawing orientation through preparation, construction, and verification. When a standalone task authorizes a saved walkthrough, save one guide at the verified eligible destination and check the saved contents and exact path before returning it. Fulfill an authorized file-only request with the saved guide. Provide a separate report or preview when selected for the task or needed to resolve outstanding authorization. When invoked by Assembly Builder, return the ordered technical content, stable part and step IDs, and check results for inclusion in its single device guide.
- Save authorized build figures (`<prefix>_steps.png`, `<prefix>_back.png`, `<prefix>_tests.png`, `polarity_guide.png`) and any authorized plan file once at the verified destination selected for the task. If none is selected, use the applicable verified placement policy. Use an established location for the owning build plan as a fallback when it fits the authorized scope. Ask once if the required destination remains unresolved. Keep each figure tied to the verified build plan. Reference saved artifacts from the existing owning note when the selected workflow calls for it and the link edit is authorized. The generic guides stay in `./assets/` and are not copied into projects.
- Report gate findings in the current task's requested form or under the recipient's existing reporting policy. For each gate include what was checked, what passed with the numbers and what was corrected. Keep the gate tables with the build plan.
- Save a gate summary only when authorized, at the verified destination selected for this task. If none is selected, use the applicable verified note conventions. Use the existing project hub as a fallback only when it fits the authorized summary. Do not create a companion guide, README or separate checklist file.

## Boundaries

- Plain language: a term is defined the first time it appears; no abbreviation without its expansion once.
- Exact holes, never "nearby" or "the next row"; lengths for wires; meter readings with a tolerance and a "means" column.
- A generic “signal”, “GND”, “power” or “reference” label is insufficient when the device, branch or control can be identified. Missing meaning stays explicitly UNRESOLVED; it is not filled by guessing from header index, wire colour or an earlier step.
- Anything irreversible gets a check before it: diode direction, header orientation, connector polarity, module USB direction.
- Establish the actual board connections from copper, module pin names from its printing and socket geometry from measured fit. Record any disagreement with the official baseline and identify the local adaptation under the shared policy. A module drawn from a pin table carries its measured pitch, spacing and body size, or is labelled unverified.
- Faults a monitor cannot see get a procedural guard, written as a step.
- For a body-contact device, follow its verified connection order, power isolation and required test loads. Electrode-specific procedures apply only when the design actually uses electrodes; do not generalize a stimulation-board sequence to every wearable or sensor.
- Unverified design: no steps are written; the gap is named and the work is sent back to the design task.

## Handoffs

- Owns electrical construction instructions, the four build-verification gates and the fault-finding tables. Assembly Builder retains whole-device assembly, mounting, firmware installation and host integration when it invoked this skill; use its current part/step identifiers, selected configuration and completed state, and return missing interfaces explicitly.
- Circuit design, simulation, part selection and the canonical electrical plan belong to circuit-design. Read its verified outputs, including existing project generators and analyses, and report gaps back rather than making a competing plan.
- `wiring-design` owns the physical harness outside the board. Exchange actual connector/contact positions and pin order, cable exits and required retention with that owner; board construction follows the selected harness interfaces without changing electrical topology.
- Return sensor/interface requirements to sensing-calibration and firmware or control changes to firmware-control; this skill assembles their verified electrical interfaces. Supply the relevant plan, completed build state and observed results to engineering-test for claim-specific cross-domain verification or to fit-review for an independent whole-assembly review when requested.
- When progress logging is authorized, follow the user's selected capture route and use the existing owning note when that route calls for one.

## Checks

- Every wire in the plan appears once in Part 3 and once in Part 4.
- Every header/pigtail/panel hole has a resolved contact-purpose row in its own step; controller rows include explicitly unused contacts. `connection_purpose_findings(parts, connectors)` returns no findings before a walkthrough is described as complete. This is a documentation check, separate from electrical `layout_check` and preserved bench passes.
- Compare the final saved guide and figures, not only the plan: all per-contact rows survive generation without clipping or omission, titles name their operation/component, and photo-based terminal positions carry the correct viewing reference and evidence status.
- Board connector/contact identities and viewing orientation agree with the selected harness and actual module evidence. A label, explanation or model-only repair preserves the electrical plan, completed joints and recorded bench passes; only a change to the circuit or its construction repeats affected checks.
- Every polarized part has a verified orientation check before heat and the applicable component-specific test; a diode-mode test is used only when specified.
- Every module in the plan has a Gate 0b evidence line (photo or fit, dated) for identity, pin order and row spacing before Part 3 is written; a socket column is never written from a datasheet alone.
- `layout_check` returns `ok` on the final plan; the Part 3 lengths come from `wire_length_mm`, not from memory.
- Regenerate the board figures from the plan after a change. Use a fresh output destination with all generated target names vacant, including the optional polarity guide. The script uses Matplotlib 3.6 or newer to draw plan labels as literal text and renders the full set before writing figures to the destination. The front panels and mirrored back view share the same build sequence. Back-view numbers identify solder points in that order. Trim, inspection, and module plug-in have no numbered points.
- Every applicable rail pair has a plan-specified test mode, acceptance criterion and source; missing criteria remain UNRESOLVED. Every module has a plug-in step after Gate 2 when the verified design permits it.
- Include the board-reading primer even for a repeat build. Check that the selected presentation preserves the technical workflow order and places each required evidence check or gate before the operation it governs.

## References

- Agent Skills. (n.d.). *Specification*. https://agentskills.io/specification
- Adafruit Industries. (n.d.). *Adafruit Perma-Proto Half-sized Breadboard PCB*. https://www.adafruit.com/product/1609
- ElectroCookie. (n.d.). *Solderable breadboard PCB, half-size*. Vendor Fritzing part; verify the selected part's dimensions against the manufacturer's file and the physical board.
