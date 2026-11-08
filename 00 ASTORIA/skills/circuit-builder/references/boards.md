# Board primers

Include the verified facts for the selected board in the board-reading primer.
Keep the walkthrough's technical sequence and adapt the wording and layout to
the recipient's selected form.

## Solderable breadboard

Use the verified board geometry to name the rows and columns and show which
holes the copper joins. On a custom board, use the actual column labels,
same-row copper groups, rails and taps. A board can have different columns,
split rails or no rails. Describe each verified split segment as a separate
connection. The figure and check helpers treat one rail label as one
continuous connection. Use a verified representation that keeps split
segments separate before relying on generated checks for them.

For the verified ElectroCookie half-size (`electrocookie_half`) and Adafruit
Perma-Proto half (`permaproto_half`) presets, hold the board with the long
side vertical and the printed text readable:

- Rows are numbered down the side, columns lettered A to J across. "C14" = column C,
  row 14, one hole.
- Holes A–E of a row are one copper strip. F–J of the same row are another. The
  centre channel separates the two strips. Place module header rows using the
  measured fit and verified hole assignments.
- These presets have two rails per side. Each rail is continuous end to end.
  Say which rails the build uses and which stay empty.
- ElectroCookie half-size only: the pair of holes at each end of the centre channel
  are taps to the rails (top left = left outer, top right = right inner, bottom left
  = left inner, bottom right = right outer). Two M3 holes on the centre line at rows
  1 and 30.
- Parts go in from the printed side; legs stick out of the back; solder on the back
  to the copper ring around the hole. Left and right swap when the board is flipped:
  the right rails become the left side. Mark row 1 and the used rails on both sides
  before starting.

Geometry (mm, origin top-left, row 1 at the top), as in [board_tools.py](../scripts/board_tools.py) `BOARDS`:

| Board | Rows | Row 1 y | Pitch | Columns A–E x | Columns F–J x | Rails L1, L2, R1, R2 x | Outline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ElectroCookie half-size | 30 | 7.60 | 2.54 | 12.16, 14.69, 17.24, 19.77, 22.31 | 29.94, 32.47, 35.02, 37.55, 40.09 | 2.64, 5.18, 47.09, 49.63 | 52.07 × 88.90 |
| Adafruit Perma-Proto half (approx.) | 30 | 6.35 | 2.54 | 13.97 … 24.13 | 31.75 … 41.91 | 3.81, 6.35, 49.53, 52.07 | 55.9 × 81.3 |

The ElectroCookie numbers were measured from the vendor's Fritzing part; the
Perma-Proto numbers are nominal from the Adafruit layout and should be checked
against the board with a ruler before lengths are quoted.

## Stripboard (Veroboard)

Copper strips run the full length of the board in one direction, every hole on a
strip is joined. There are no rails and no centre channel. Joints are broken where
needed with a strip cutter or a 3 mm drill bit twisted by hand in the hole; list
every cut as a step with its hole, before any part goes in, and test each cut
silent. Orientation: say which way the strips run relative to the reader.

## Plain perfboard (no copper joins)

Every hole is an island. Every connection is a wire or a bent leg soldered to the
next pad. Steps therefore name both ends of every leg route; use short bare legs
only where they cannot touch anything else, insulated wire otherwise.

## Custom PCB with silkscreen (stuffing a board from a BOM)

- The white print is the silkscreen: a designator per part (R1, C3, D2, U1, J1) and
  an outline showing where it sits. The BOM maps designator → value → part.
- A square pad, dot, or notch can be a clue to pin 1. Confirm pin 1 and the
  viewing side against the selected footprint and component documentation.
  A band on an axial diode can be a clue to the cathode. On a polarized
  capacitor, look for a body stripe or a printed + or −. Confirm which terminal
  each mark identifies in the selected component documentation and match it to
  the verified board footprint. For an IC or socket, match the documented
  orientation mark to the verified footprint.
- Fit the lowest parts first (resistors, diodes), then IC sockets and small
  headers, small capacitors, tall capacitors, connectors and other heavy parts.
  Socketed integrated circuits (ICs) go in last. Keep them out through the
  applicable Gate 2 checks. After those checks pass, follow the verified
  Gate 3 sequence, including any earlier stages that call for empty sockets.
  With power removed and stored energy discharged as the plan specifies,
  seat only the ICs required for the upcoming stage. Apply power with that
  stage's required loads and isolation in place.
- Bend legs slightly outward on the back to hold a part while soldering; solder
  one leg, check the part sits flat, then the other.
- Pads connected to a ground plane can draw heat away from the joint. Follow
  the verified board, component and soldering process guidance for temperature,
  dwell and technique. If a joint fails to wet, inspect pad and lead condition,
  flux and heat transfer before choosing a correction.

## Solderless breadboard (prototyping before soldering)

A solderless breadboard joins groups of holes without solder. Use the
verified board geometry to identify its strips and rails. Some rails have a
split. Verify which segments are joined and treat separate segments as
separate connections. A gap in the printed
line can be a clue to a split. Bridge verified split segments only
where the plan calls for it and with power removed. With power off, wire the
supply rails, then the ground wires, then the signal wires. Keep removable
modules out during the applicable [Gate 2 checks](verification.md), with power
removed and stored energy discharged according to the verified plan.
Each rail check needs its specified meter mode, probe orientation, acceptance
criterion and source; missing criteria remain UNRESOLVED. Once the required
Gate 2 checks pass, keep power off while inserting the modules specified for
the next stage. Then follow the verified plan's Gate 3 power-up sequence.
Module pins bend easily. Push straight down with both hands. Loose jumpers
can cause intermittent faults. Before touching or reseating a jumper,
disconnect power and discharge stored energy according to the verified plan.
