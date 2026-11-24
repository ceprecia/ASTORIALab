# Verification: how an engineer checks a build without slowing it down

Contents:
- [Gate 0 — design verification (do once, from the source files)](#gate-0--design-verification-do-once-from-the-source-files)
- [Gate 1 — before the first joint (five minutes)](#gate-1--before-the-first-joint-five-minutes)
- [Gate 2 — before power (continuity, modules out)](#gate-2--before-power-continuity-modules-out)
- [Gate 3 — power-up, staged](#gate-3--power-up-staged)
- [Reporting](#reporting)

Place checks at **gates**. Each check needs a pass criterion and a named
correction. Use the selected reporting form and headings to record the observed
symptom, the cause supported by the evidence or its unresolved status, and the
correction. Repeat required checks affected by a correction or design change
and preserve unaffected passes. Record unresolved results as UNRESOLVED. Resume
the affected work only after the required checks pass. Other authorized work may
continue when it does not depend on those checks.

Gate 0 — before the plan is trusted. Gate 0b — parts in hand. Gate 1 — before the first joint. Gate 2 — before
power. Gate 3 — before the device touches anything valuable (a person, an expensive
module). Each gate below lists what to run, what "pass" is, and what to do on fail.

## Gate 0 — design verification (do once, from the source files)

1. **One net table is the truth.** Every connection lives in a single table
   (net, part, pin). Drawings, KiCad sheets and wire lists are generated from or
   compared to it, never edited independently. Fail: two documents disagree →
   fix the table, regenerate the rest.
2. **Derive, do not trust.** If a bought board's schematic matters, re-derive its
   net list from the copper (Gerbers) or by continuity on the bare board.
   A square pad can be a clue to header pin 1. Confirm pin 1 and the viewing
   side against the selected footprint and connector documentation.
   Fail: published BOM or schematic disagree with the copper → the copper
   wins; record the difference.
3. **Module pinouts from the selected vendor documentation**, not a generic
   drawing. Verify revision-specific contact order, address configuration
   and electrical ratings against the actual marked part. Unknown identity
   leaves the affected connection unresolved until the evidence is obtained.
4. **Every pin accounted for.** Each module pin is on a net or marked no-connect;
   unused channels of a level shifter, address pins, and unused outputs are listed
   as no-connect on purpose.
5. **Schematic ERC = 0** (KiCad `kicad-cli sch erc`), and the exported netlist
   compared pin by pin against the net table. Fail: a label placed on another
   net's wire joins them silently → move the label, re-export, re-compare.
6. **Layout check.** Run `layout_check` in `./scripts/board_tools.py` with the
   verified board geometry and supplied pins, wires, rails, component endpoints
   and internal joins. It reports duplicate hole use, net shorts or opens,
   wires between holes already joined by copper and components whose two legs
   share a node. Separately check module and header footprint clearance against
   the selected geometry. For each link between boards, verify rail assignments
   and pin order at both mating ends. Resolve discrepancies against the verified
   plan and repeat the affected checks.
7. **Electrical analysis of the complete signal and power paths.**
   - **Operating envelope.** Derive the transfer from each specified input
     to its output, including gain and offset. Check the idle point, each
     specified limit of the signed command range and any intermediate state
     where behavior changes. Use zero and both signs only where the design
     permits them. Evaluate worst-case loads and component and reference
     tolerances. Identify where output compliance or regulation is lost.
     Quantify the spread at the reference point and range limits using
     worst-case bounds and Monte Carlo when the tolerance distributions are
     supported. Trace the maximum credible signal through each measurement
     stage against its input, scaling and conversion limits. Resolve any
     clipping or inadequate headroom before accepting a reading.
   - **Supply and interface limits.** Quantify how output changes across
     each rail's verified supply range and near its applicable cutoff.
     Budget average and peak current per rail and check runtime and charger
     adequacy where applicable. Compare driver high and low levels
     (VOH and VOL) with receiver thresholds (VIH and VIL) at the selected
     supplies. Use a compatible interface wherever the margins are inadequate.
   - **Faults and transitions.** For each exposed node, assess open circuits
     and shorts to the reference and each applicable rail. Cover detached
     connectors, outputs stuck at either limit, loss of one supply while
     others remain active, and control inputs left undriven. For each fault,
     check the relevant idle, boundary and transition states from the
     operating envelope. Record the worst consequence, its condition and
     what the monitor can observe. Provide a procedural guard for any fault
     the monitor misses. Analyze power-up and shutdown with the required
     loads and record the peak and duration of uncommanded output. Use
     analysis or simulation for faults outside the approved bench procedure.
   Pass when the results meet the verified limits with margin or the plan
   documents an adequate guard and its scope.

## Gate 0b — parts in hand (before any hole is fixed)

Verify each physical module and bought board the plan will use before Part 2.
Use inspection and measurement of the hardware on the bench as evidence. Record
the hardware identity and configuration and each check in the project's verified
facts with the date and evidence (photo, fit, reading). A Gate 0b pass applies to the specific hardware and configuration
examined. When a module or board is replaced or its configuration changes,
repeat Gate 0b for the affected hardware. Update the net table or layout when
the evidence changes it, regenerate affected outputs and repeat any design,
layout or bench checks whose evidence the change invalidates before proceeding
past their gates.

For every module (controller, breakouts, bought boards):

1. **Identity**: photograph the marked surfaces with the printing readable.
   Record manufacturer, exact part, board revision and relevant assembly
   option, then match them to the controlling documentation. A shared chip
   name does not establish a breakout board's header or power arrangement.
2. **Pin count and order**: count the pins on each side; read the labels in order along
   each header. Compare with the plan's pin table name by name, not by position.
3. **Row spacing by fit, not by datasheet**: set the bare module on the actual board and
   note which columns the two pin rows drop into. Use the verified plan's board
   for both `row_spacing_from_columns(col_a, col_b, board=board)` and
   `columns_for_spacing(spacing_mm, board=board)`. The
   plan's sockets and the module artwork must use this measured value. Look-alike
   boards can differ despite a similar product name; use the measured fit.
4. **Body size**: measure length and width with a ruler; the body may cover rows the
   plan wanted for a header or a wire. Record which rows the body covers at its
   planned position.
5. **Assembly variant and contact details.** Compare installed resistor
   and inductor markings with the revision-specific BOM. Record which
   configuration links are open or bridged. Count the contacts on each
   switch or jack and confirm their functions. For a connector, check its
   keying, pitch and contact order against the actual mate.
6. **Fitted or missing hardware.** Check every accessory the plan assumes
   is installed. For example, if a panel connector arrives without the
   specified cable retainer, add a distinct installation step before the
   cable is secured.
7. **Orientation references.** Verify each polarized connection against
   its actual mating marks and pinout. Locate pin 1 using the selected
   package drawing and the matching mark on the part or board.

Pass: every plan assumption about a part has a dated evidence line. Fail: update the
net table or the layout first, regenerate drawings and figures from it, then continue.
Never patch a figure by hand to match a part.

**Drawing modules.** Module artwork drawn from a pin table (no vendor image) must take
its pitch, row spacing and body size from Gate 0b measurements and say so in its
docstring; a placeholder drawn from a datasheet is labelled "unverified" until the fit
check replaces its numbers. After any change to a module's geometry, regenerate every
board that uses it and re-run the layout checks, ERC and the netlist comparison.

## Gate 1 — before the first joint (five minutes)

- Parts in hand against the parts table; polarity marks found on each polarised
  part; module silkscreen read and matched to the plan (pin order, pin 1).
- Board marked: row 1 and used rails on both sides.
- Iron tinned, meter in continuity mode and beeping when the probes touch.

## Gate 2 — before power (continuity, modules out)

Use `continuity_checks` in `./scripts/board_tools.py` to generate the Gate 2
check rows. Keep the rows with the build plan and present the checks in the
selected reporting form. Run the checks with power removed and stored energy
discharged according to the verified plan.
The wire list supplies intended direct connections. Every other test needs its
own meter mode, probe orientation, acceptance criterion and source: differently
named rails can conduct through components; neighbouring header pins may share
a net; a capacitor or polarized connector is not tested as a diode. Include all
physically adjacent header pairs, not only the end pairs.

The helper accepts an optional `test_expectations` object in the plan. Keys are
stable check IDs printed in the function's returned rows: `rail:L1:R1` (rail names
sorted), `polarised:D1`, or `header:J1:A1:A2` (holes in supplied physical adjacency
order). For a general check, supply `mode`, text in `expect` and source text in
`basis` from the verified plan. These checks use neutral markers.
Missing criteria remain **UNRESOLVED** in general checks.

For colored meter markers, supply `mode`, `probes`, `measurement`, and `source`.
Omit `expect` and `basis` entirely. The example shows the schema using illustrative values.
Use only values, units, limits and lead assignments verified for the actual
meter, circuit and procedure.

```json
{
  "test_expectations": {
    "polarised:D1": {
      "mode": "diode",
      "source": {"reference": 4, "section": 2},
      "probes": {"red": "F6", "black": "A6", "verified": true},
      "measurement": {"unit": "V", "at_least": -0.6, "at_most": -0.3}
    }
  }
}
```

`probes` is the only lead assignment and must name both distinct holes of the
check. For `source`, cite a numbered reference recorded in the verified plan
and choose one locator (`page`, `section`, or `step`). Use whole numbers from
1 through 999999. Keep source names and details in the existing plan. The table
and colored figure render the reference and locator. `measurement` contains
a unit and at least one limit. Choose one lower bound (`at_least` includes
the limit and `above` excludes it), one upper bound (`at_most` includes the
limit and `below` excludes it), or one of each. Signed limits remain signed.
Use `V` or `mV` for diode mode. Use `mΩ`, `Ω`, `kΩ` or `MΩ` for a verified
numeric resistance or continuity reading. For visual checks and nonnumeric
meter indications, use the neutral `expect` form. A mixed or incomplete
colored check stops before any table or figure is produced. Use the verified
table for the criterion and its source before testing. A supplied diode
forward value alone does not establish the reverse criterion or the meter's
capabilities. Unknown IDs fail rather than silently dropping a planned test.
Method illustrations are labeled schematic;
actual geometry, orientation and soldering limits come from the verified plan.
Plan-driven tables and board views require an explicit `board` entry naming a
verified supported geometry or supplying the verified geometry object; they do
not silently choose an example board.

A result outside its criterion is a finding to diagnose against the circuit:
inspect for unintended bridges, wrong holes, missing connections, component
orientation, parallel paths or inadequate meter range. A beep does not identify
a cause by itself. Continuity checks do not establish powered function or
physical safety.

## Gate 3 — power-up, staged

1. **Verified power stages:** use the design's supply route, isolation, required loads, voltage/current tolerances and thermal limits; do not assume all circuits can be powered unloaded or must remain cold.
2. **Modules and loads:** connect only the components required at this stage, then check their specified rails and current budget. USB-only startup applies only to a design that supports it.
3. **Applicable interfaces and sensors:** use the plan's known test inputs and expected readings. Include bus scans or resistor loads only when appropriate to the actual circuit.
4. **Functional table:** compare measured behavior with the approved specification and its tolerances; keep structural checks distinct from powered function and body-contact suitability.
5. **Connection sequence:** follow the verified device-specific procedure and required test loads. Electrode, battery and zero-output steps apply only when established for that design; do not infer them for unrelated devices.

Examples below apply only when those components and interfaces are in the verified plan.

- **A status input stays active with its limit switch clear.** Compare the
  selected contact, idle bias and input configuration with the expected
  idle state. Measure the relevant supply, return and input at the
  interface before choosing a correction.
- **A motion reading falls during a known positive displacement.** Check
  the installed sensing direction and channel reference against the
  drawing. Correct the demonstrated wiring or configuration mismatch.
- **A bus peripheral fails to respond.** Verify power at its own contacts.
  Check line order, level compatibility, required pull-ups or termination
  and the installed address setting against the selected interface.
- **An output remains active through shutdown.** Check the supply and
  enable sequence and whether the command becomes undriven. Compare any
  uncommanded interval with the verified limits before proceeding.
- **A recorder trace flattens near a range limit.** Apply an approved test
  input and compare readings along the measurement path to locate the
  limiting stage. Repeat the Gate 0 range analysis before relying on the
  affected readings.

## Reporting

Report gate findings in the current task's requested form or under the recipient's existing reporting policy.
For each gate include what was checked, what passed with the numbers and what
was corrected. Keep the gate table with the build plan. Save a summary only
when authorized, at the verified destination selected for this task. If none is selected, use
the applicable verified note conventions. Use the existing project hub as a
fallback only when it fits the authorized summary.
