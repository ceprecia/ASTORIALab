---
name: engineering-test
description: >-
  Plans and evaluates tests of engineering claims across a complete device. Use
  for claim-specific acceptance evidence and integration faults; keep
  construction walkthroughs with Assembly Builder. Triggers: plan this device
  verification, test this hardware claim, review engineering test coverage.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-11-02"
---

# Engineering Test

Choose evidence that can decide the engineering claim.

## Purpose

Own cross-domain verification plans, measurement methods and evaluation of device
claims. Distinguish computational checks, documentation checks, physical tests and
application behavior. Keep acceptance tied to current requirements and revise the
test or design when evidence changes. This is not the construction walkthrough.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.

## Inputs

- The exact claim, requested decision, current design/configuration and requirements.
- Source drawings, connection and measurement contracts, code and previous results.
- Completed assembly/checks, available instruments/fixtures and physical unknowns.
- Proposed change and the functions or interfaces it could affect.

## Steps

1. **State the claim.** Identify what decision the test should support and which
   configuration it concerns. Separate changed user requirements from defects and
   isolate target-device claims from proposed implementation claims.
2. **Choose suitable evidence.** Map each important claim to a calculation, source
   comparison, semantic/visual check, instrumented bench test or application test.
   Identify the input, observable, units and relevant criterion with its basis.
   Missing acceptance values remain open questions, not invented pass thresholds.

   For mounting/packaging, distinguish missing functional design from untested
   physical performance. Inspect support, retention, connector mates, occupied
   wiring, installation access and required motion through Fit Review. A model
   missing its selected fastening hardware cannot support a fastening-completeness claim;
   saying strength is untested does not account for the absent design.
   For constrained or moving assemblies, receive Fit Review's mounting,
   complete occupied routes, functional interfaces and operating/service
   state evidence. Name the exact digital experiment, geometry, collision model,
   inputs and coverage. Posed clearance, kinematic sweeps, dynamic contact and
   structural stress analysis answer different questions. Select adequate material,
   contact, constraint, solver and reference evidence for a load/strength claim;
   a Blender render or optional immersive VR inspection alone does not supply it.
3. **Reuse current evidence.** Read the existing guide, parts and recorded results
   before requesting new inputs. Preserve completed hardware and passes unless the
   change affects them. Inspect the final delivered artifact when the claim concerns
   labels, views or instructions; source tables alone cannot prove correct delivery.
4. **Design a discriminating test.** Specify setup, exact interfaces, stimulus/load,
   reference, procedure, expected observation and uncertainty. Include a useful
   negative case or counterexample. Separate component tests from the combined
   system, and nominal conditions from the limits they cannot establish.
   Before authoring test or analysis source files, read and adapt
   `00 ASTORIA/templates/code_template.md`.
5. **Execute or mark unperformed.** Run only the relevant checks within the current
   authorized task, using available tools and hardware. Record the actual outcome
   and conditions. An unavailable instrument or physical device leaves a specific
   test unperformed; it does not convert a simulation into bench evidence.
6. **Interpret narrowly.** Report supported, contradicted or unresolved for each
   claim with the deciding evidence. Diagnose the observation before proposing a
   correction; a beep, export success or assertion count is not a general verdict.
7. **Check correction effects.** Return the issue to its owner, then repeat affected
   tests and dependencies. Preserve unrelated passes. A chosen new architecture or
   clarified placement changes the test baseline; it does not prove an earlier
   instruction was disobeyed.
8. **Return the practical result.** State what works within tested scope, what
   remains untested and the next measurement that could change the conclusion.
   Use the [illustrative cases](references/replay_cases.md) when evaluating
   workflow behavior; they are examples to adapt, not required tests for every device.

## Outputs

- A claim/method/criterion/result view scaled to the question, plus actionable findings.
- Requested measurement procedures, fixtures or analysis with explicit conditions.
- Report routine verification findings in the current task's requested form or under the recipient's existing reporting policy. Return delegated findings to the invoking session.
  Requested artifacts follow `me.md`, without creating an extra audit or project hub.

## Boundaries

- Do not create new approval gates, universal thresholds or device requirements.
- A model pass cannot certify physical fit, strength, heat, sensing or loaded release.
- Successful compilation does not establish board execution; host mocks do not
  establish an installed driver, transport or final application behavior.
- Report planned, attempted, failed and passed checks separately and preserve
  meaningful null/adverse results instead of selecting only favorable examples.
- Keep a historical replay's inputs limited to what was available at that point.

## Handoffs

- Return technical failures to the relevant design, fit, wiring, sensing or firmware
  owner with exact evidence and expected correction, not an unscoped redesign.
- Circuit Builder retains its detailed electrical assembly checks; Assembly Builder
  retains the complete build sequence and integrates the returned test instructions.
- The invoking session resolves tradeoffs; this skill supplies claim-specific evidence.

## Checks

- Every conclusion identifies its actual method, configuration and remaining limits.
- Observables and criteria can discriminate the stated alternatives or failure.
- The saved guide/figure or complete assembly is checked when that is the claim.
- Integrity checks and repeated self-consistency comparisons do not replace a
  source/interface comparison or expose absent required functions by themselves.
- Physical and synthetic data, nominal calculations and measured results stay distinct.
- A replay tests substantive behavior, not preferred wording or a keyword count.
