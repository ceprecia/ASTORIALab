---
related: []
created: 2026-11-23
---

# Optional build and test plan

This is an unperformed procedure for the [proposed circuit](circuit_and_parts.md). Reading or reviewing it does not establish that a circuit is safe, correctly wired or working. Complete the paper review without hardware if the listed equipment or instrument skills are unavailable.

## Assemble with the source disconnected

1. Disconnect both source leads from the breadboard. Leave the source output off.
2. Identify the actual part as WP7113ID. Use its manufacturer package drawing to identify the anode and cathode. A meter's diode mode can provide a second polarity check; record what it shows instead of assuming a result.
3. Measure R1 with at least one lead isolated. Use a 1 kΩ ±5% part; record the reading and meter resolution. Resolve an unexpected value before continuing.
4. Map the board's connected holes and split rails using resistance/continuity mode. Draw where N1, N2 and GND will be placed. Do not infer connections from the printed stripes alone.
5. Place R1 between N1 and N2. Place D1 with its anode at N2 and cathode at GND. Keep those nodes distinct.
6. Connect S1 between the future positive source lead and N1. Connect the future negative source lead to GND. Compare each wire with the endpoint table in the circuit file.
7. With no source attached, verify the switch's open/closed behavior and inspect for an unintended wire bypassing R1 or shorting the power rails. The LED makes some resistance readings direction-dependent; a continuity beep alone is not a full circuit check.
8. Keep the circuit disconnected while setting and independently checking the source at no more than 3.0 V with a 5 mA current limit, following that source's manual. If the settings or terminals cannot be verified, stop the physical exercise.

## Optional powered check

Only consider this after resolving the power-off checks. Connect the source with S1 open and the source output off. Verify polarity, enable the output, then close S1 briefly. Observe the source and LED. If the source is in current limit, a component warms, or the behavior is unexpected, turn the output off and disconnect before investigating. Do not raise the voltage or remove R1 to make the LED brighter.

Measure the voltage across R1 with the meter in DC voltage mode. Record the actual source voltage and LED observation. Turn power off and disconnect after recording. Calculate current from the measured resistor voltage and resistance.

## Record evidence

| Check | Acceptance criterion for this proposed design | Actual result in this fixture |
| --- | --- | --- |
| Exact LED and A/K identification | Exact part and polarity resolved from its drawing and corroborating check | NOT MEASURED |
| Isolated R1 resistance | Consistent with a 1 kΩ ±5% part, considering meter accuracy | NOT MEASURED |
| Breadboard node map | Intended connections established and unintended shorts resolved | NOT MEASURED |
| Switch | Intended terminals open and close as expected | NOT MEASURED |
| Disconnected source | Correct polarity, no more than 3.0 V, 5 mA current limit verified | NOT MEASURED |
| Powered circuit | No unexpected limiting, warming or behavior | NOT MEASURED |
| Voltage across R1 | Reading recorded with units and meter mode | NOT MEASURED |
| Calculated current from measurements | Calculation traceable to measured V_R and R1 | NOT MEASURED |
| LED visibility | Observation recorded for the actual conditions | NOT MEASURED |

The illustrative CSV output is a blank record example. Replace a status only with an actual reported observation. Keep the measured conditions and any failed check; do not manufacture a passing run.
