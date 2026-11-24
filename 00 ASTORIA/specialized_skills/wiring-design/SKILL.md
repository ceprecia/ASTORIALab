---
name: wiring-design
description: >-
  Designs the physical wiring that implements an electrical plan. Use for
  connector mating, branch identities and moving cable routes; retain the
  supplied net table as the electrical authority. Triggers: design this cable
  harness, map these connector contacts, plan moving cable routes.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-11-02"
---

# Wiring Design

Connect the named devices through an explicit, physically plausible harness.

## Purpose

Own connector mating, terminations, wire selection, routing and installation data
for a supplied electrical plan. The plan retains electrical connectivity; the
harness makes its physical implementation inspectable. Revise routes as fit,
component evidence or user decisions change.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.

## Inputs

- Current net table, exact devices, controller endpoints and voltage/current domains.
- Existing board drawing, contact maps, actual cable ends and completed connections.
- Assembly geometry, motion/service needs and selected termination method.
- Wire/contact specifications, installation evidence, stock and required quantities.

## Steps

1. **Reuse the existing circuit and build.** Identify the requested harness scope and
   completed joints. Find the board and connection references already supplied.
   Distinguish a missing label from a changed electrical connection.
2. **Identify both mating ends.** Record contact versus housing, series, pitch,
   pin order, keying, polarity, face and insertion orientation. Check accessories,
   factory tails and adapters. Verify the manufacturer's complete mating
   specification and installation access; show any unresolved compatibility
   or missing component at the affected operation.
3. **Map each physical contact.** Give contact ID, hole/pad, device/control,
   terminal purpose, net, supplied voltage and controller endpoint. Name each repeated
   power/ground branch and explicitly unused position. Retain a supplied photo's
   viewing reference and attribution; do not guess pin order from color or index.
4. **Select the physical construction.** Check wire gauge, insulation, contact
   capacity, flexibility and termination method against the actual domain and use.
   Separate shared power distribution from individual signals. Explain local
   alternatives and retain a selection already made by the user.
5. **Route through the combined assembly.** Account for connector approaches,
   bends, sleeves, restraint, moving joints, tool access and service removal.
   Inspect required poses with the actual mechanism and board arrangement; do not
   hide a cable gap or use a rigid bundle to bridge required movement.

   Supply CAD/Fit Review with occupied contact/connector geometry or dimensions,
   insertion depth, tails, insulation, wire/bundle thickness, route and bend/loop
   space in the shared frame. Compare terminal and entry heights. Mark sourced,
   measured and assumed values separately; an empty corridor or uniform allowance
   does not establish contact engagement, routed wire packing or a minimum box height.
   Follow the actual mounting surface and moving neighbors, including curved
   supports when relevant. Check the selected operating and service states
   with the restrained harness in place. Exchange mechanical-transmission
   constraints with Mechanism Design; electrical conductors and load-bearing
   elements have different interfaces and acceptance criteria.
6. **Define lengths and stock.** Separate route centerlines, termination allowances,
   service loops, reserve and measured cuts. A straight board-distance helper is
   not an installed cable measurement. Reconcile whole packs, shared spools and
   replaced leads once; keep factory tails distinct from new purchased cable.
7. **Prepare the implementation views.** Produce endpoint and wire tables, relevant
   connector views and the requested routing/assembly details from the same map.
   Every contact's purpose appears at the operation where it is used, not only in
   an earlier overview. Keep diagrams and complete captions consistent with tables.
8. **Check and hand off.** Compare all conductors to the supplied net table and both
   mating ends. Define applicable continuity, polarity and flex observations using
   source-based criteria. Report unmeasured cuts, missing parts and open routes;
   preserve unaffected wiring and bench passes after a documentation repair.

## Outputs

- One endpoint/wire/termination implementation with clear domain and branch identities.
- Requested connector/routing views, stock quantities and assembly/test inputs.
- Report findings in the current task's requested form or under the recipient's existing reporting policy. Return delegated findings to the invoking session. Saved deliverables follow
  `me.md` and reuse the existing project owner instead of a second wiring hub.

## Boundaries

- Do not change the electrical net table to make a chosen cable arrangement fit.
- A visible path or zero nominal collision does not prove bend life, contact grip,
  installed wire length, voltage drop or physical solder/tool access.
- A user's chosen termination may update the plan; do not call it an official part.
- Unknown contact identity remains unresolved; continue unrelated routing work.

## Handoffs

- Return electrical conflicts to circuit-design, mechanical clashes to fit-review
  and geometry requests to 3D Builder. These are handoffs, not copied design owners.
- Assembly Builder and Circuit Builder receive precise endpoint purposes and the
  selected physical connection steps; Engineering Test receives measurement needs.
- Return bounded findings to the invoking session without starting another guide.

## Checks

- Every required conductor has two identified endpoints and a purpose at each end.
- Contacts, viewing faces, pin numbers and installed mating parts agree across outputs.
- Supplies and returns name their branches; signal paths remain individually identified.
- Rendered wires reach actual terminals, with unresolved geometry labeled.
- The combined candidate includes both mates and the occupied harness or explicitly
  identifies reservations, missing dimensions and unreviewed motion/service states.
- Quantities distinguish installed use, trial allowances and complete purchases.
