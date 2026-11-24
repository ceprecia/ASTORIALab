---
name: firmware-control
description: >-
  Implements device firmware and its control and communication behavior. Use for
  embedded drivers, timing and recovery; distinguish host tests from execution
  on the target hardware. Triggers: implement this device controller, write this
  hardware driver, debug this embedded protocol.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-10-30"
---

# Firmware and Control

Implement the specified device behavior and expose what has actually run.

## Purpose

Own embedded drivers, scheduling, command handling, control states and device
communication. Implement the selected circuit and measurement contracts rather
than inventing their physical meaning. Revise code as evidence or requirements
change; preserve the user's completed hardware and unrelated working behavior.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.
Assembly Builder retains the complete firmware-installation and host setup guide.

## Inputs

- Exact target board, source version, build tools, pin map and existing firmware.
- Circuit behavior, actuator interfaces, measured/calculated limits and control needs.
- Sensor identities, units, conversion, clock/freshness and validity contract.
- Host/transport requirements, expected messages and available hardware test access.

## Steps

1. **Identify the implementation task.** Reuse the selected source and configuration.
   Separate code changes from installation, static inspection and read-only review.
   Check whether the requested behavior is present, proposed or physically untested.
2. **Bind exact interfaces.** Match pins, addresses, rails, polarities and commands
   to current circuit/device documentation. Match channel and calibration identities;
   do not substitute a different driver API or infer physical units from a variable
   name. Read and adapt `00 ASTORIA/templates/code_template.md` before writing new source files.
3. **Make behavior explicit.** Define startup, normal operation, invalid input,
   communication loss, reset, recovery and shutdown transitions as applicable.
   State what output each transition requests and what requires observed feedback.
   A stop message, disabled pulse or zero command is not proof of mechanical release.
4. **Implement acquisition and timing.** Respect required sampling/read sequences,
   timestamp domains, sensor validity, freshness and bounded device timing. Specify
   scheduling/resource budgets from the task and evidence, leaving unknown hardware
   latencies explicit. Do not convert failed reads into apparently fresh cached data.
5. **Implement transport and control.** Define message units, identities, bounds,
   framing and error responses. Check duplicates, truncation, reordered messages and
   connection changes where relevant. Distinguish the last accepted command from
   current measured state; do not silently continue a stale command by assumption.
6. **Test meaningful logic.** Exercise state transitions, boundary values and faults
   with deterministic host tests or mocks. Include contradictory or missing feedback
   cases. Compile for the exact target when available and report unavailable tooling
   accurately; a host pass is not a target build or an observed output waveform.
7. **Check hardware within the authorized task.** Compare actual bus, timing and
   output observations with the specified behavior when hardware is available.
   Record conditions and failures; otherwise supply the exact remaining measurement.
   Do not describe planned I/O, simulated traces or compilation as device operation.
8. **Return implementation and integration facts.** Give source/configuration,
   commands, expected readings, tests run and remaining board/host checks. Identify
   affected interfaces and rerun dependent checks after changes, preserving others.

## Outputs

- Requested readable firmware/control code, configuration and message definitions.
- Claim-specific results separated into host logic, compilation, board execution
  and complete application behavior, with missing evidence explicit.
- Integration instructions returned to the invoking session or Assembly Builder;
  requested files follow `me.md`, without a competing device setup guide.

## Boundaries

- Simulation and manual fixture behavior do not establish automatic closed-loop control.
- Do not infer calibrated force, response time or release from an output duty value.
- Existing firmware behavior may differ from a bench sketch; document the actual
  startup, command range and communication-loss semantics of the selected version.
- Do not change circuit connections or measurement geometry to hide a code mismatch.
- Limit a missing requirement to its affected behavior while continuing useful work.

## Handoffs

- Return electrical mismatches to circuit-design and measurement questions to
  sensing-calibration; Engineering Test receives hardware timing/functional claims.
- Assembly Builder receives target, installation, calibration and host connection
  details, including expected behavior and what remains unexecuted.
- Return bounded findings to the invoking session; ordinary source reading uses
  coding tools, while packaged-application inspection remains a separate REA task.

## Checks

- Target, source, pin map, protocol and calibration correspond to the same selection.
- Startup/recovery and stale/invalid input behavior agree with the stated contract.
- Tests challenge behavior rather than merely duplicating implementation branches.
- Every execution claim identifies host, compiler, board or application evidence.
- Documentation fixes do not reset passed hardware or alter unrelated configuration.
