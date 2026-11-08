---
name: sensing-calibration
description: >-
  Defines and verifies the conversion from hardware measurements to useful
  quantities. Use for sensor suitability, calibration and measurement
  uncertainty; hand acquisition requirements to firmware work. Triggers:
  calibrate this hardware sensor, define this measurement conversion, assess
  sensor accuracy.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-30"
  updated: "2026-10-30"
---

# Sensing and Calibration

Define what a reading means and how well that meaning is supported.

## Purpose

Own sensor suitability, measurement conversion, calibration and uncertainty.
Separate the quantity of interest from raw readings and from inferred quantities.
Revise a calibration or measurement approach when its mounting, mechanism or
observed behavior changes; keep synthetic examples distinct from installed values.

Read `00 ASTORIA/systems/Engineering System.md` for the shared engineering policy.
Firmware implementation and board acquisition drivers belong to firmware-control.

## Inputs

- Measurand, units, required range, resolution, rate and applicable error criteria.
- Exact sensor, mounting/transmission geometry, electrical interface and channel IDs.
- Raw records with timestamps, known inputs, calibration history and reference method.
- Existing conversion code, configuration and evidence of physical installation.

## Steps

1. **Define the measurement.** Name the physical quantity and location being measured.
   Distinguish raw counts, angle, displacement, force and other derived quantities.
   A position channel does not measure force merely because an actuator is present.
2. **Check sensor suitability.** Compare range, usable sensing region, resolution,
   bandwidth and environmental sensitivity with the intended input. Check the actual
   component and mechanical coupling; a generic electrical label does not prove
   rotation range, fit or useful response over the mechanism's full stroke.
3. **Specify acquisition requirements.** Define channel identity, raw units, sample
   time and clock domain, validity/status, sequence and required freshness. Include
   mux selection, settling, addressing or read ordering where applicable. Mark
   failures as failed samples rather than silently substituting cached values.
4. **Define the conversion.** Give equations, polarity, zero/reference state, ratios,
   coefficients, limits and missing-value behavior. Tie calibration to the actual
   sensor/mounting/configuration. Do not adopt an older ratio or endpoint after a
   mechanism change merely because the channel name is unchanged.
5. **Collect or plan calibration inputs.** Use known physical reference inputs with
   recorded method and units. Include useful endpoints, intermediate values,
   repeated readings and opposing directions when hysteresis matters. Preserve raw
   observations; label generated data and unperformed acquisition explicitly.
6. **Evaluate error.** Separate bias, repeatability, hysteresis, drift and reference
   uncertainty as relevant. Use independent check inputs when possible; fitting
   error alone does not establish predictive accuracy. State sample scope and
   distinguish sensor resolution from whole-system measurement accuracy.
7. **Check failure behavior.** Exercise meaningful invalid/status, stale, missing,
   out-of-range, reset and discontinuity cases in the conversion contract. Test
   mathematical behavior with synthetic inputs without calling it sensor validation.
8. **Return the measurement contract.** Supply units, identities, conversion,
   supported range, uncertainty, acquisition requirements and remaining physical
   checks. Identify which geometry or firmware changes require new calibration.

## Outputs

- The requested calibration/conversion contract, supporting data and readable code.
- Explicit numeric status: measured, documented, calculated or synthetic as applicable.
- Results and limitations returned to the invoking session; place requested outputs
  with their existing owner under `me.md`, without another calibration hub.

## Boundaries

- Read and adapt `00 ASTORIA/templates/code_template.md` before authoring a new source file.
- Do not replace raw records or apply a new calibration outside the requested scope.
- A precise repeated reading can still be biased; a simulated conversion pass does
  not establish physical sensing, interference immunity or installed repeatability.
- Do not treat a failed bus transaction as a valid unchanged measurement.
- A missing physical reference limits accuracy claims, not useful conversion work.

## Handoffs

- Firmware Control receives acquisition and conversion requirements; Circuit Design
  receives electrical/range conflicts; Mechanism Design receives coupling limits.
- Engineering Test receives error criteria and physical measurement questions;
  Assembly Builder receives the actual calibration procedure and expected readings.
- Return bounded findings to the invoking session; retain one conversion authority.

## Checks

- Every quantity, coefficient and limit has explicit units and a compatible geometry.
- Channel identity, sign and timestamps survive acquisition-to-conversion handoff.
- Missing/invalid readings remain distinguishable from valid zero and from stale data.
- Reported accuracy is bounded by reference quality and independent observations.
- Measured calibration cannot be mistaken for a synthetic example or older mounting.
