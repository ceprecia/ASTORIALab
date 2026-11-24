# Polarity cheat sheet, common faults, SMD two-pad swap

## Polarity: what to look at before heating

| Part | Mark | Rule |
| --- | --- | --- |
| Axial diode (for example 1N4001 or 1N5819) | commonly one cathode band | verify the exact component documentation; the conventional forward-current direction is anode to cathode. Zener reverse operation uses its specified circuit and limits |
| LED | long leg, flat edge on the rim | long leg = anode (+); flat edge = cathode (−) |
| Electrolytic capacitor | stripe with − signs, shorter leg | striped side = negative; the other leg to the + pad |
| Tantalum capacitor | stripe or + sign | stripe = positive (opposite to electrolytics) |
| IC, socket | package-specific notch, dot or other mark | use the package pin-numbering drawing and viewing side; do not infer pin 1 from a generic shape |
| Header, connector footprint | sometimes a square pad or pin-1 mark | confirm pin 1 and viewing side against the footprint and connector documentation |
| Battery connector (including JST-PH) | wire colors and mating orientation | colors alone do not establish polarity; verify the actual plug pinout, mating board marks and the plan before connection |
| Plug-in interface board | assembly revision and printed contact labels | read the markings on the installed board and match each contact to the selected revision's pinout and viewing side. Resolve any mismatch before soldering |
| Ceramic capacitor, resistor, inductor, crystal | none | no polarity |

For each applicable part in the build, put the verified orientation check
with the step before soldering. Name the required position and its reference
mark or viewing side. Include the corresponding verified test at its required
stage. Use the selected reporting form and preserve the build and verification
sequence.

## Common beginner faults and the fix

| Symptom | Cause | Fix |
| --- | --- | --- |
| Solder sits as a ball on the leg, pad bare | incomplete wetting; possible contamination or insufficient heating | follow the specified flux, wetting and rework process within the component and board limits |
| Cracked or incompletely wetted joint | movement, contamination or inadequate process; dull finish alone is not a fault | inspect wetting and geometry against the specified process; rework if required |
| Two neighbouring pins joined | too much solder, iron dragged across | clean tip, touch between the pins and draw it away; wick if needed |
| Header leans | all pins soldered before checking | reheat one end pin while pressing the header flat, then the other end |
| Module will not plug into its two headers | headers soldered without the module as jig | reheat and reposition one header pin at a time, or desolder and redo with the module in place |
| Wire pulls out | stranded wire not tinned, or joint cold | tin the end, redo |
| Pad lifts off the board | excessive heat or mechanical stress | stop and assess the damaged pad and connection against the plan; use a documented repair or replace the board |
| Nothing lights, rail reads 0 V | possible input, enable or supply issue | remove power and compare the actual input polarity and switch wiring with the verified plan |
| Rail-to-rail beep outside the planned criterion | possible bridge, misplaced wire or expected path through components | compare with the circuit and test procedure before isolating the cause |

## SMD two-pad swap (for example replacing a 0805/1206 shunt resistor)

1. Add a drop of liquid flux on the part. Tin the iron.
2. Heat one end while pushing the part sideways with tweezers; when it moves, heat
   the other end and slide it off. Or use a wide tip across both pads.
3. Clean both pads: a little fresh solder, then wick, so each pad has a thin flat film.
4. Tin one pad with a small dome. Hold the new part with tweezers against that pad,
   touch the iron to the dome until the part sinks in, remove the iron, hold still
   until the joint has cooled according to the specified process.
5. Solder the other end: iron to pad and part end, feed a little solder.
6. Inspect: both ends wetted, part flat, no bridge to a neighbour. Measure the value
   across the pads with the meter (for a shunt, expect the new value; for an
   in-circuit part the reading may be lower because of parallel paths).
7. Clean flux only with the process and solvent compatible with the flux, board and components; follow the specified cleanliness requirements.

Specify the iron tip, temperature, contact time and rework limits from the solder,
component and board process documentation. Do not treat a generic time or
temperature as an acceptance rule. Practice the applicable method on scrap first.
