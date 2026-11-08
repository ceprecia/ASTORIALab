---
name: assembly-builder
description: >-
  Guides complete device assembly from documented parts through mechanical,
  electrical and software integration, coordinating the needed engineering
  specialists. Use for building or continuing a physical device, with official
  instructions first and clearly labeled alternatives. Triggers: assemble this
  device, walk me through assembly, continue this hardware build, connect these
  components.
metadata:
  level: skill
  system: Engineering System
  dependencies: circuit-builder, 3d-builder, circuit-design, wiring-design, sensing-calibration, firmware-control, fit-review, engineering-test
  created: "2026-10-25"
  updated: "2026-11-02"
---

# Assembly Builder

Build the whole device with every part, connection and next step accounted for.

## Purpose

Own one complete device build from documented parts and current progress through mechanical assembly, electrical connections, mounting, firmware installation, host setup and integration. Use Circuit Builder for a verified board subassembly and 3D Builder for mechanical models and assembly images when needed. Obtain design, harness, calibration, control, fit and verification work from their owners below, keeping the results in one coherent walkthrough.

Read `00 ASTORIA/systems/Engineering System.md` and follow its shared engineering policy and role boundaries. Standalone board requests belong to Circuit Builder; standalone modeling requests belong to 3D Builder. This skill coordinates a build rather than developing its electronics or firmware or inspecting packaged applications.

## Inputs

- The intended device, selected version, mirroring/orientation and demonstration goal; official parts list, tutorials, drawings, source models and software instructions.
- Physical inventory evidence and quantities, including fasteners, connectors, cables, consumables and tools. Reuse confirmed answers and existing progress before asking for more.
- Completed physical assembly, recorded checks, the current selected configuration, changed constraints and the immediate next task. Inspect the existing guide and canonical electrical plan when present; reconcile older instructions with the current request.
- Component interfaces: connector contacts and pitch, pin order, power requirements, mechanical mounts, cable paths, accessible controls and host connection.
- Each electrical contact's named device/control, terminal function and exact pad/hole, including the assigned branch for repeated supply/ground contacts. Keep supplied net, voltage and controller endpoint with this map. Terminal positions use an explicit photo/drawing viewing reference and distinguish user identification from independent measurements.
- Target computer and operating system, controller variant, firmware source/version, transport and intended application. Discover these from project context where possible.
- A component-and-step manifest when modeling is needed, using the same part identifiers as the inventory, electrical plan and guide.

## Steps

1. **Establish the baseline.** Read the selected official documentation, not just a local summary. Identify which version each parts list, tutorial, firmware and model belongs to. Resolve discoverable conflicts and state unresolved ones before using an affected instruction. Start a custom project as CUSTOM DESIGN when there is no official baseline.
2. **Reconcile parts and progress.** Reconcile one inventory from the official BOM and label project-specific additions. Present it in the selected reporting form. Include required quantity, confirmed quantity/status and the assembly steps affected by a gap. Preserve already completed work and its checks. Determine whether a revision changes the physical specification, documentation or both. Trace its effects to the relevant subassemblies and evidence; a local fabrication method does not replace the official device requirements.
3. **Plan the complete sequence.** Cover mechanical preparation, electrical subassemblies, connector mating, installation and retention, cable routing, firmware installation, host software, calibration and the final application test. Identify dependencies so the guide continues beyond a finished board. Mark completed, current and remaining operations from the actual build state, and revise affected steps when the selected configuration or constraints change. Keep stable step and part identifiers rather than resetting numbering in specialist sections.
4. **Check interfaces before writing instructions.** Compare the two actual mating sides and identify missing adapters or contacts explicitly. Check mounting holes and fasteners, orientation and mirroring/orientation, access to screws and USB, wire exit and strain relief. Keep proposed connector or mounting alternatives separate until selected; do not describe a connector that cannot mate as a finished connection.

   For each mounted part, identify support, separate retention, any fastener and its counterpart, and the installation/tool sequence. A board resting on posts is not fastened by the lid screws unless a clamping arrangement is designed. Integrate Fit Review's incomplete interfaces at the affected step or STL option; an export or static-clearance pass cannot make that mounting function complete. Exploratory/fit-test options remain deliverable with their missing functions explicit.

   Receive the selected mounting surfaces, functional interfaces and operating
   states. Integrate transmission routes, electrical harnesses and service
   access into installation steps where the design requires them. Use Fit
   Review's saved-model findings with their limits; digital inspection and
   physical assembly observations remain separate evidence.
5. **Obtain specialist sections as needed.** Give Circuit Builder circuit-design's verified canonical electrical plan, selected parts, interface facts, completed joints and passed checks. Request its detailed board sequence and tests. Give 3D Builder the source assets, same part and step IDs, known dimensions, placements and unresolved interfaces; request only the views or studies that help the build. Load other specialist owners below only for the work the build needs. Supply each with the current selected configuration and changed constraints, and compare returns against the baseline, actual inventory and completed state before integration.
6. **Write the walkthrough.** At each sourced operation, show OFFICIAL STEP with the part IDs, orientation, action and expected check; place any ALTERNATIVES immediately beneath it under the shared policy. Put the chosen local implementation in that alternative, including all added materials. Link or embed model renders at the matching steps and label them as model renders. Explain unfamiliar terms when they first appear.

   Use titles that directly name the action and component. Include the complete per-contact purpose map at the local board or wiring step where it is used. Present it in the selected reporting form. Do not make the reader recover device/channel assignments, reference-ground purpose, switch contacts or supply branches from another section. Integrate Circuit Builder's unresolved-purpose findings before declaring the section complete; label-only repairs preserve the circuit and passed checks.
7. **Complete software and integration.** Use firmware-control's actual target, source/version, build configuration and interface contract for the installation procedure, controller/port selection and configuration; return new control logic or firmware changes to that owner. Integrate sensing-calibration's calibration procedure and acceptance criteria. Then cover the host dependencies, transport, driver/plugin and application connection for the user's computer. Include expected readings or behavior for each stage. Follow the selected host application's documented interface and dependency path; a successful transport example does not establish application compatibility.
8. **Verify and continue.** Compare the final guide to the official parts list and full assembly sequence. Check written steps against scene state and the canonical electrical plan. Obtain fit-review's independent whole-assembly findings and engineering-test's claim-specific verification when those claims form part of the requested result. Separate modeled checks from the user's physical observations and live software results. Report unresolved items at the steps they affect and finish with the next actionable build step, without resetting passed work.

## Outputs

- One usable end-to-end walkthrough from the user's current completed state to the intended application, in the current task's requested form or under the recipient's existing reporting policy. For an authorized saved walkthrough, use the verified eligible destination and check the saved guide's contents and exact path before returning it. When the task authorizes updating the existing guide, revise it in place under the project's conventions. Fulfill an authorized file-only request with the saved guide. Provide a separate report or preview when selected for the task or needed to resolve outstanding authorization.
- One consolidated parts inventory and one assembly sequence, with the official path, selected local implementations and remaining gaps visible.
- Specialist figures and editable models with their matching step IDs, referenced from the guide rather than competing guides.
- Concise verified context in the owning MOC when authorized by the task; project artifacts and technical context follow `me.md` and the layout reference.

## Boundaries

- Keep the complete build as the unit of work. Completion requires the selected device's integrated functions, not just one finished subassembly.
- Do not silently select missing replacement parts, invent fitted mounts or claim firmware compatibility. Continue independent assembly work while the specific affected interface remains unresolved.
- Let the verified electrical plan own connections and the model source own geometry. Keep their IDs and selected variants aligned without duplicating either authority.
- Use the project's actual requirements and existing checks. Do not add a separate approval process to ordinary assembly.

## Handoffs

- Load `circuit-builder` only for detailed electrical assembly and checks; integrate its returned section into the device guide.
- Load `3d-builder` only for mechanical geometry, assembly scenes, fit or motion studies, and model renders; return corrections when those disagree with the written assembly.
- Load `circuit-design` for electrical design, part selection, substitutions, simulation and the canonical electrical plan; retain its outputs' place in the assembly sequence. Circuit Builder constructs and checks that design.
- Load `wiring-design` for the physical harness: connector mating, cable routes and lengths, wire exits, retention, strain relief and assembly access, consistent with the canonical electrical plan.
- Load `sensing-calibration` for sensor behavior, measurement mapping, calibration procedures and their acceptance criteria; integrate the resulting installation and calibration steps here.
- Load `firmware-control` for firmware and control development, builds and device interfaces. Firmware installation, host setup and whole-device integration stay here.
- Load `fit-review` for an independent review of the selected whole assembly, and `engineering-test` for claim-specific cross-domain verification. Integrate their findings into the affected steps; neither substitutes for the physical results it has not observed.
- Use `rea` only for a separate question about inspecting a supplied packaged application.

## Checks

- Every official required part has a quantity and inventory status; every local addition and missing mating part is explicit.
- Every assembly operation has the applicable source path or custom designation, the selected variant and a check with an observable result.
- Rendered parts, labels, mirroring/orientation, connectors and step order agree with the written guide and saved model.
- Parts lists and steps account for support, retention hardware/counterparts, harness occupation and installation access. The guide carries current fit findings and does not upgrade nominal or sampled checks into full fit or motion acceptance.
- The selected configuration and latest constraints agree across specialist returns and the final guide; physical changes and documentation changes have separately identified evidence requirements. A genuine design change identifies its affected steps and dependent checks.
- For repeatable tool checks, use `scripts/benchmark_suite.py prepare --output-dir /tmp/<fresh-run>` to freeze source inputs and separate references. Give the builder only `inputs/`, save its output, then use `evaluate --run /tmp/<fresh-run> --candidate /tmp/<fresh-run>/candidate --blender "$BLENDER_EXECUTABLE"` with the verified Blender 4.5 LTS executable. Omit `--blender` only when the verified `blender` is on `PATH`. Keep the reference and evaluator withheld; label any retuned case as development. This tests digital behavior, not physical assembly.
- Electrical connections agree with the referenced verified plan; changes affect only the corresponding assembly and dependent checks.
- Every electrical endpoint in the delivered step identifies the contact/pad, device/control and function, plus supplied net/voltage/controller mapping. No middle contacts or shared ground/power branches disappear during generation; headings name the component/action and source-photo pin orientation remains explicit.
- The guide reaches the intended working application, or identifies the exact uncompleted physical or software step and its missing input. Digital checks and physical completion are reported separately.
