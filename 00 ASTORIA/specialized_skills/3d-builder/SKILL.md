---
name: 3d-builder
description: >-
  Creates editable mechanical models and assembly scenes with matching step
  renders using parametric CAD and Blender. Use to model parts or illustrate a
  documented assembly, preserving source geometry and distinguishing measured
  dimensions from approximations. Triggers: model this part, make an exploded
  view, render these assembly steps, prepare this model for printing.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-25"
  updated: "2026-11-02"
---

# 3D Builder

Model the parts, show how they assemble, and keep every unknown visible.

## Purpose

Create editable mechanical geometry, assemblies, exploded views, simple fit and motion studies, and step images. Use CadQuery for dimensioned parametric parts and Blender for assembly scenes and rendering. Import supplied official parts without changing their source geometry; model local additions separately.

Read `00 ASTORIA/systems/Engineering System.md` and follow its shared engineering policy and role boundaries. This skill can work alone on a model or return a bounded modeling section to Assembly Builder. It does not author electrical connections or claim that a digital assembly has passed physical tests.

## Inputs

- Intended object, currently selected revision/variant/mirroring/orientation, current functional and packaging constraints, official source assets and drawings, and the requested deliverable or assembly steps to illustrate.
- Dimensions with their units and evidence: source drawing, direct measurement or approximation. Identify unknown dimensions, reference frames and independent source landmarks explicitly; include front and underside references when they determine orientation or interfaces.
- Stable component IDs, quantities, source paths, selected alternatives, placements and mating relationships in the component-and-step manifest; use the same IDs as the guide.
- Existing verified board layout and electrical plan references when an electronics proxy is needed, with evidence for actual module bodies, mounting features and terminal/contact positions. Geometry may represent the board and connectors; circuit-design's canonical electrical plan remains the connection authority, and wiring-design supplies physical harness interfaces.
- Required motion axes, travel and constraints with their source; printing requirements only when a printable part is requested.
- For constrained or articulated assemblies: mounting surfaces and reference
  landmarks, component-to-function map, transmission and routing geometry,
  guide dimensions and operating/service states required by the selected design.
- The installed CadQuery and Blender runtimes, outside the vault. Baseline versions are CadQuery 2.8.0 with Python 3.12 and Blender 4.5 LTS. Verify the available versions and the Blender executable for the current host before execution.
- Use [the component manifest and tool commands](references/model_manifest.md) for the shared scene format, validation, rendering and native-scene reopening.

## Steps

1. **Inspect inputs and preserve sources.** Inventory the actual assets and verify their format, revision, units, bounds and mirroring/orientation. Establish the source-to-model frame from independently identified body, mounting and terminal landmarks; check front and underside orientation where relevant. Agreement between an export and its reimport is not this source comparison. Keep original official files unchanged, recording their identity in the manifest. An imported STL is a mesh, not recovered parametric history. Treat unsupported or incomplete inputs as specific modeling gaps.
2. **Define the shared manifest.** Record part IDs and quantities, source files, official/local status, selected alternatives, dimensions and their evidence, local coordinate systems, placements, mating relationships and associated step IDs. Reference the electrical plan by path rather than copying its netlist. Keep proposed alternatives as separate selectable configurations.
3. **Build editable geometry.** Before writing new CadQuery or Blender Python, read and adapt the vault-root `00 ASTORIA/templates/code_template.md`. Write readable parameterized CadQuery Python for dimensioned local parts. Preserve known dimensions and name uncertain parameters. Use clearly marked proxies for unknown parts or context, including a mounting fixture or surrounding envelope; do not manufacture a fitted mount from a visual guess. Maintain millimeters in engineering data and explicitly convert to meters for Blender and glTF exchange.
4. **Assemble and constrain.** Place source parts using the documented mating relationships and declared coordinate frames. Keep orientations, axes and mirroring/orientation explicit. Show missing connectors and unresolved fasteners or mounts rather than closing gaps with fabricated geometry. Use the verified layout for an electronics board, checking actual terminal/contact locations against their source rather than matching only the housing. Use wiring-design's route and exit constraints; label any unmeasured thickness, cable route or envelope as approximate.

   Account for support and retention separately for each mounted part. Include the selected restraint, engagement and access, with fasteners and counterparts where used, or explicitly identify the missing retention design. Include inserted connector contacts and underside protrusions where relevant. Aligned mounting holes and cover locks do not imply that the enclosed board is secured. Record these interfaces using the manifest's existing relationships and notes.
5. **Check fit and motion within the evidence.** Check known dimensions, placements, mating features, clearances and accessible assembly paths. Use declared axes and travel to sample interference during motion. Report the sampling and approximation limits; unsourced travel remains unverified. Distinguish intentional contact, potential collision and unresolved geometry.

   Place components relative to the actual support and adjacent mechanisms,
   including curved surfaces when applicable. Represent complete occupied
   routes and transmission elements, not only centerlines. Compare demanded
   movement with the documented mechanism's travel and recovery limits.
   Keep source geometry and recorded transforms consistent after placement.
   Supply reproducible pose/sweep results and inspectable views for Fit Review;
   a posed render or attractive animation is not a physics or strength test.
6. **Create the assembly scene.** Keep part IDs as object identifiers and choose consistent cameras, mirroring/orientation and label conventions. Prepare overview, exploded and step-highlighted configurations from the same saved scene, hiding or fading completed work consistently. Match each image to the guide's part IDs, orientation and operation. Label every output as a model render, with approximations and unresolved interfaces visible.

   Show empty space reservations as labeled outlines, transparency or separate views so they cannot be mistaken for mounted hardware. Keep the board, its support plane and retention visible in a suitable section, underside or exploded view when obscured in the overview. Assumed wire allowances are space budgets, not measured minimum heights or completed routes.
7. **Export and reopen.** Keep CadQuery Python and the Blender `.blend` scene as editable sources. Export STEP for solid interchange, STL when printing is appropriate, GLB for portable viewing and PNG for requested views. Reimport exports and reopen the saved scene to check units, dimensions, part counts and transforms. Render headlessly from the saved scene and visually inspect the result.
8. **Return bounded findings.** Return deliverables, matched step IDs, the selected configuration, source comparisons, checks performed, mismatches and unresolved inputs to the requesting build. Carry changed constraints into the affected model and views without resetting completed physical work. A digital fit or sampled collision result stays a computational result; physical fit, movement and wiring remain observations for the physical build.

## Outputs

- Editable CadQuery Python and Blender scene files, plus the small component-and-step manifest and only the exports/views needed for the request.
- Overview, exploded and step-highlighted PNG model renders with consistent IDs and visible approximation labels where applicable.
- STEP, STL and GLB when appropriate to the requested use, with units and coordinate conversion explicit.
- Report digital checks, mismatches and unresolved facts separately in the current task's requested form or under the recipient's existing reporting policy. When invoked by Assembly Builder, return the findings to it. Save project deliverables with their owning resources under `me.md` and the layout reference; do not create a parallel project hub.

## Boundaries

- Generate assembly images from the saved model. Do not substitute AI-generated photographs or illustrations for evidence of the modeled mechanism or physical build.
- Do not overwrite source geometry to make an assembly fit. Local modifications remain separate alternatives with their own editable sources.
- A proxy supports context or a declared envelope check; it does not establish application-specific physical fit, contact geometry or a measured dimension.
- This version covers geometry, fit, declared motion and representation of verified wiring. Force, stress, spring behavior and application-specific physical fit need additional measured inputs and an appropriate analysis before making those claims.
- Numerical comparison tolerances are regression criteria, not manufacturing specifications. State the tolerance and the evidence supporting each dimension.

## Handoffs

- Own geometry, placements, saved scenes, exports, renders and the limits of digital checks.
- Return requested model views and unresolved interfaces to the invoking build. A standalone modeling request can finish here.
- Refer electrical inconsistencies and part substitutions to circuit-design, which owns electrical design, part selection and the canonical electrical plan. Do not turn a visual cable into a second wiring plan.
- Exchange connector positions, cable exits, bend space and assembly access with wiring-design, which owns the physical harness. Exchange sensor mounting geometry and travel with sensing-calibration, and implemented motion/control limits with firmware-control when they affect the model.
- Supply the current saved assembly, requested exports/views, source assets, model frames, selected configuration, support/retention interfaces, wiring evidence or reservations, motion states and unresolved functions to fit-review. Request whole-assembly review for combined fit claims, including proposed usable mounting/STL options; a standalone exploratory model may finish with its omissions explicit. Supply the relevant model and check conditions to engineering-test for claim-specific cross-domain verification; local geometry checks remain this skill's responsibility.
- Include applicable body curvature/landmarks, functional component counts, cable
  endpoints/occupied routes, collision approximations and critical coupled states.
  Fit Review checks the saved candidate independently; CAD remains the author.

## Checks

- Source identities, selected variants and quantities match the inputs, and original assets remain unchanged.
- Independent source landmarks agree with the model in the declared frame, including front/underside orientation and actual terminal/contact order and locations where relevant. Identify which source features were checked and which remain approximate; a round trip or matching overall bounds alone cannot pass this check.
- Known dimensions and mating transforms match their references. For regression comparisons, use 0.01 mm and 0.1 degrees unless the task defines another criterion; allow equivalent global positioning and symmetric orientations.
- A known-size calibration object survives CAD export, Blender import and portable export with correct scale, translations and rotations.
- Exported/reimported geometry and the reopened `.blend` agree on part count, units, bounds and placements. Headless rendering succeeds from that saved scene.
- Reversed parts, wrong scale, missing mating components and unknown geometry are identified rather than concealed. Electrical connectivity is checked against the referenced plan by its owner.
- Every required mounted part has a represented support and retention arrangement or an explicit incomplete interface. Assembly/tool access is checked in its actual installation state. Artifact integrity checks cannot pass these functional checks.
- Every requested step image agrees with its scene configuration and written assembly instruction. Render quality does not count as evidence of physical completion.

## References

- CadQuery Development Team. (n.d.). *Importing and exporting files*. https://cadquery.readthedocs.io/en/latest/importexport.html
- CadQuery Development Team. (n.d.). *Assemblies*. https://cadquery.readthedocs.io/en/latest/assy.html
- Blender Foundation. (n.d.). *Command line arguments*. In *Blender 4.5 LTS manual*. https://docs.blender.org/manual/en/4.5/advanced/command_line/arguments.html
- Blender Foundation. (n.d.). *Importing and exporting files*. In *Blender 4.5 LTS manual*. https://docs.blender.org/manual/en/4.5/files/import_export/index.html
