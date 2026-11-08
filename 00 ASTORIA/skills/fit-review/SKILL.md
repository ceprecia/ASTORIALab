---
name: fit-review
description: >-
  Independently reviews assembly fit, service access, routing and motion
  against source geometry. Use to challenge proposed arrangements through
  reproducible virtual fit experiments;
  return corrections without becoming its CAD author. Triggers: review whole
  assembly fit, find motion and access conflicts, check this packaging
  arrangement.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-11-02"
---

# Fit Review

Challenge the complete arrangement before trusting its appearance.

## Purpose

Independently inspect assembly fit, motion, access and packaging. Review the actual
combined candidate, including connected parts and service operations, rather than
accepting each isolated module's envelope. Return specific findings to its owners;
3D Builder remains the CAD author. Earlier arrangements remain revisable.

Use the mounting surface appropriate to the selected design, including a
body or fixture when relevant. CAD, Blender and optional immersive VR can
expose geometric, routing and motion conflicts. Choose the representation
and solver for the claim; rendered appearance does not establish fidelity.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.

## Inputs

- Requested fit claim and exact assembly, configuration, units and coordinate frames.
- Existing native geometry, board drawings, part references and actual measurements.
- Current saved assembly, exports and delivered views, with component IDs, included
  hardware, reservations and the assembly/retention method for each mounted part.
- Required motion, assembly/service operations, cable approaches and surrounding space.
- Dimension tolerances, body/fixture measurements and unresolved geometry or inventory.
- Sourced or explicitly approximate mounting and surrounding surfaces, scale,
  reference landmarks, moving interfaces and contact layers when relevant.
  Include curvature, access regions and uncertainty needed by the actual claim.
- Function-to-component map: actuator, sensor, passive return, guide and derived
  output roles; actual module/channel bindings, cable endpoints and required counts.
- For virtual experiments: current scene/configuration, collision representation,
  constraints, boundary conditions, pose sequence and any material/load assumptions.

## Steps

1. **Identify what is being reviewed.** Read the supplied arrangement and the current
   constraints. Separate included hardware from reservations and excluded equipment.
   Identify what the arrangement must support, retain, connect and allow to move.
   An omitted essential function is an incomplete design, even when the included
   solids do not collide. Keep exploratory/mockup scope without silently excluding
   a required fastener, connector or movement from a broader fit conclusion.
   Reconcile the component list with the required functions and channel assignments.
   A passive support does not satisfy a drive requirement, and a visible module
   does not establish an implemented function. Explain redundant components.
   A corrected view or changed user decision may replace an earlier placement.
2. **Recover the existing references.** Use the actual board drawing, part files and
   completed-assembly evidence before proposing proxies or requesting another image.
   Compare part identities, units, origins, mirroring/orientation and front/back viewing faces.
   For wearables, compare relevant target views and body landmarks with the modeled
   surface and articulations, including wraparound paths rather than only top views.
   A curved approximate body can support bounded geometry work; name its measurement
   gaps instead of treating it as a personalized fit or flattening the anatomy.
3. **Review the whole occupied space.** Include mounts, fasteners, connector mates,
   protrusions, cable bends, covers and required external devices. Report component
   bounds separately from combined bounds; avoid stacking mutually exclusive variants.
   Distinguish intentional contact, demonstrated interference and unresolved geometry;
   bounding-box overlap alone is not solid interference, and a nominal gap is not
   a physically qualified fit.
   For body-mounted devices, inspect contact, stand-off, local surface normals,
   padding and how supports follow curvature. Measure projections relative to the
   body/garment surface as well as global bounds. Identify rigid bridges across
   moving regions and conflicts with adjacent body parts; a tabletop arrangement
   is not sufficient evidence of worn fit.
4. **Check support and retention separately.** For each mounted part, trace how it
   rests on its support and how the selected restraint keeps it there. Inspect both
   mating sides: holes, fastener head/shaft, nuts/inserts/threads or other chosen
   restraint, engagement, protrusions and load path to the mount. Check their occupied
   space and tolerances. Aligned PCB holes on posts do not establish fastening;
   cover locks do not retain the PCB unless that clamping function is designed.
   Name absent hardware as absent, rather than only calling its physical strength
   untested. Do not invent clamp force or material performance from geometry.
5. **Check wiring and connector space.** Include both connector mates, inserted
   contacts, solder tails, insulation/sleeves, wire or bundle thickness, approach
   directions, bends, restraint and service slack. Compare the proposed route with
   the actual terminals, entry height and opening. Identify dimension sources and
   assumed allowances. Empty reservations, straight lines and room above a board
   do not demonstrate a connected harness or a minimum enclosure height. Return
   unresolved contact engagement or bend/packing questions to Wiring Design.
6. **Trace mechanical transmission paths separately from electrical wiring.**
   When the selected design uses a cable, belt, linkage or another transmission,
   follow it between its actual drive, guides and load. Include occupied size,
   supported bends, neighboring parts and contact with the mounting surface.
   Identify endpoint ownership and distinguish actuation from measurement.

   Compare required travel with the supplied mechanism's usable range and
   recovery behavior. Inspect relevant operating, stopped and service states.
   An animation cannot supply an absent constraint or tensioning mechanism.
   Mark unsourced friction, stretch, tension and bend limits as assumptions.
   Mechanism Design owns transmission constraints; Sensing and Calibration
   owns measurement geometry; Wiring Design retains electrical harness ownership.
7. **Review motion and surroundings.** Use the sourced axes, travel limits and
   required individual and coupled operating poses. Include moving cables/strings,
   neighboring mechanisms and rigid structures across flexible joints. Identify
   sampled states and the unsampled intervals; neutral clearance does not support
   full travel. Missing motion geometry or ranges leave that claim unresolved.
   Derive individual and coupled operating states from the selected mechanism
   and its task. Preserve the relative reference frames rather than translating
   the whole assembly to hide a conflict. Include the complete transmission
   and routing geometry; independently posed parts do not establish a
   mechanically constrained motion.
8. **Run a claim-specific virtual experiment.** Inspect the actual saved candidate,
   not only its prose or rendered overview. Record the configuration, component and
   route IDs, axes/range, sampled intervals, tool/method and deciding output: contact,
   minimum clearance, route-length/travel conflict or an explicit unresolved input.
   Use a reproducible model locator and an inspectable section, annotated view or
   motion trace where it explains the finding. Choose sampling from the critical
   geometry and check intermediate/coupled states; endpoint images alone are partial.

   Keep CAD, Blender and optional VR aligned in units, transforms, joints, geometry
   and occupied paths. Inspect collision shapes, margins, disabled pairs and scene
   membership; a proxy collider can erase a real modeled opening or obstruction.
   Distinguish posed geometry, kinematic sweep, contact/dynamic simulation and
   structural analysis. For load/strength claims, obtain suitable material/contact
   properties, supports, loads and a solver appropriate to that claim; examine
   numerical resolution and a relevant reference comparison. Without them, return
   a bounded geometric finding and the missing analysis, not an invented stress pass.
   VR is an optional inspection/input interface; a headset or animation does not
   establish measured force, comfort or physical operation.
9. **Review assembly and service.** Follow the proposed installation, wiring,
   fastening, disconnection and extraction sequence. Check actual approach volumes
   for hands, tools and fastener insertion, including access to both screw and nut.
   State when a module must be removed first or a connected lead traps a part;
   do not silently assume access through installed components.
10. **Challenge the representation.** Inspect the current saved geometry and exports
   alongside the delivered renders and source references. Use a section, underside
   or exploded view when a cover obscures support, retention or terminals. Identify
   missing mates, discontinuous wires, wrong mirroring and assumed body fit. Empty
   space reservations must be distinguishable from hardware and must not conceal
   the interfaces being judged. Distinguish a source defect from a render defect.
11. **Return findings by claim.** For each issue give part IDs, state, evidence,
   practical consequence, correction option, owner and the missing physical check.
   Say supported within checked scope, conflicting, or unresolved, and explicitly
   name incomplete required functions. For support/retention, wiring, motion and
   assembly/service, give the evidence and limit or explain why the topic is not
   applicable. A clean static check cannot become a whole-assembly fit pass while
   an essential interface is absent. Review affected corrections while preserving
   unrelated accepted work.
   Include body conformity and working-cable function when applicable. State which
   model inputs and uncertainty could change the result. Ask the creator for the
   smallest correction that resolves the actual conflict; reconsider the overall
   arrangement when repeated local patches preserve the same excessive bulk.

## Outputs

- A concise list of actionable fit findings, or the exact scope with no findings.
- Required views, measurements or motion states that would resolve uncertainties.
- Reproducible configuration/pose/route references and actual virtual-check results,
  with omitted functions and approximation limits. Annotated views or traces use the
  existing owning artifacts when authorized; no separate review hub is required.
- Findings returned to the invoking session; save an annotated deliverable only when
  requested, following `me.md`, rather than creating a parallel guide or review hub.

## Boundaries

- Review independently; do not silently repair the CAD and then review your own fix.
- Do not infer personalized or ergonomic fit from an approximate body model.
- A flat body proxy cannot qualify body-conforming fit or a wraparound route.
  Visual detail, mesh density and photorealism are not measures of model validity.
- Static clearance does not establish stiffness, heat behavior, cable fatigue,
  loaded function or the feasibility of an unmodeled installation sequence.
- Export success, watertight meshes, matching hashes and roundtrip agreement verify
  artifact properties; they cannot establish functional completeness or source fit.
- A digital review can expose modeled conflicts and omissions. Physical fit and
  wiring/mechanism behavior require observations or measurements of the build.
  Continue authorized mockups and fit-test exports with their unresolved functions
  explicit; physical testing is not a prerequisite for exploratory geometry.
- Digital experiments can reject a modeled arrangement and compare proposals;
  report the geometry/kinematics/physics actually evaluated. Physical observations
  are still needed for installed fit, friction, compliance, temperature and release.
- A user's clarified location or mirroring/orientation is a changed constraint, not proof that
  an earlier response disobeyed the previous selection.
- Missing evidence limits its specific claim, not unrelated authorized work.

## Handoffs

- Return geometry/render defects to 3D Builder, operating conflicts to mechanism-design,
  cable/mating issues to wiring-design and board-interface conflicts to circuit-design.
- Give 3D Builder body surfaces/landmarks, critical poses and curved placement/route
  constraints. Mechanism Design owns tensile-cable/return changes; Sensing and
  Calibration owns channel meaning and geometry-dependent measurement changes.
- Engineering Test receives physical fit/measurement questions; Assembly Builder
  receives any affected installation or service instructions.
- The invoking session resolves cross-domain tradeoffs; this review supplies evidence.

## Checks

- The review covers the combined candidate and its required neighbors, not just pods.
- Mechanism counts are explained by function, and actual module-to-channel bindings
  are received or explicitly missing. A derived output does not satisfy an added
  independent actuation or sensing requirement.
- Curved support geometry, moving interfaces and contact assumptions are included
  when required by the selected claim. Boundary-crossing routes occupy actual space.
- Every finding has a reproducible location/state and distinguishes inference from fact.
- Proposed corrections preserve completed hardware unless the actual defect requires change.
- The source asset and face used by every comparison are identifiable.
- Each required mounted part has a checked support and retention method or a named
  incomplete interface; missing hardware is not hidden in a generic bench caveat.
- Wiring reservations, connected hardware and motion coverage remain distinguishable
  in both the findings and the delivered views.
- Required working cables have endpoints, finite occupied paths, route-length and
  travel/slack/return coverage for the checked motion, or a named unresolved function.
- Each virtual result names the saved configuration, method, critical states and
  deciding output. Collision simplifications, solver assumptions and unsampled
  intervals remain visible; physical and numerical stress tests are distinct.
- No rendered, sampled or nominal result is presented as a measured fit qualification.

## References

- Blender Foundation. (n.d.). *Collisions*. In *Blender 4.5 LTS manual*. https://docs.blender.org/manual/id/4.5/physics/rigid_body/properties/collisions.html
- Blender Foundation. (n.d.). *RigidBodyWorld*. In *Blender 4.5 Python API*. https://docs.blender.org/api/4.5/bpy.types.RigidBodyWorld.html
