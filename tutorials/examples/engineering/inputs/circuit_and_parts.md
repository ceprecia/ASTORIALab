---
related: []
created: 2026-11-23
---

# Indicator circuit and parts

Original fictional design exercise. The schematic is proposed wiring, not a photograph or verified assembly.

## Schematic

```text
3.0 V DC positive
       |
     S1 switch
       |
      N1
       |
   R1 1 kΩ
       |
      N2
       |
   D1 anode A
      |>|       red LED
   D1 cathode K
       |
      GND ---------------- DC source negative
```

The resistor and LED are in series. `N1`, `N2` and `GND` name electrical nodes, not particular breadboard row numbers. Verify the connections of the actual board before assigning holes to these nodes.

| Connection | First endpoint | Second endpoint |
| --- | --- | --- |
| Supply feed | DC positive | S1 first terminal |
| Switched feed | S1 second terminal | R1 first lead, node N1 |
| Limited feed | R1 second lead | D1 anode A, node N2 |
| Return | D1 cathode K | DC negative, node GND |

## Parts and equipment

| Item | Selection for this exercise | Before physical use |
| --- | --- | --- |
| D1 | Kingbright WP7113ID red LED, one | Verify the exact part and identify A/K from its package drawing; do not infer polarity from trimmed lead length. |
| R1 | 1 kΩ resistor, ±5%, rated at least 0.25 W, one | Measure it with power disconnected and at least one lead isolated. |
| S1 | Maintained two-terminal switch suitable for this low-current DC circuit, one | Identify its open/closed contacts with a meter. |
| Supply | Isolated, regulated DC bench source set no higher than 3.0 V, current limit set to 5 mA | Use the source's own manual to establish and verify its controls. |
| Assembly | Solderless breadboard and short insulated jumpers | Map its connected holes and any split rails with power disconnected. |
| Meter | Digital multimeter with resistance, DC voltage and diode modes | Know the meter's terminals and modes. This plan measures current through resistor voltage, not a meter placed across the supply in current mode. |

No hardware purchase or physical assembly is required to complete the tutorial's paper review.

## Manufacturer evidence

Primary source: [Kingbright WP7113ID datasheet](https://www.kingbrightusa.com/images/catalog/SPEC/WP7113ID.pdf), specification DSAF0012, revision V.14A, dated 2026-01-08, inspected for this example on 2026-11-23.

- Page 1 identifies the WP7113ID package and provides its mechanical drawing.
- Page 2 lists a 30 mA absolute maximum DC forward current at 25 °C. An absolute maximum is a limit, not a recommended operating target.
- Page 2 characterizes forward voltage at 10 mA. Those values do not establish this circuit's forward voltage at its much lower operating current.
- Page 3 shows typical current/voltage and brightness curves. A typical curve is not a measurement of the user's LED.

Read the current exact-part datasheet before a physical build. No manufacturer drawing or PDF is copied into this example.

## Design calculation

Assumptions for this calculation: the source stays at or below 3.0 V, R1 is at least 950 Ω, and the circuit is wired as shown with no resistor bypass.

Ignoring the LED's voltage drop gives a conservative current bound:

```text
I ≤ 3.0 V / 950 Ω = 3.16 mA
P_R ≤ (3.0 V)² / 950 Ω = 9.48 mW
```

These are calculated bounds, not predicted measured readings. They depend on the stated source, resistor and wiring assumptions. They do not establish actual LED brightness, a correct breadboard assembly or fault-free operation.

During a physical test, record the voltage across R1 and the measured resistor value. Calculate current as `I = V_R / R_measured`. Do not replace this measurement with the datasheet's forward-voltage value.
