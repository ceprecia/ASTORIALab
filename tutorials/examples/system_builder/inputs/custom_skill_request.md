# A small custom skill

Tess repeatedly turns seed-inventory rows into labels. Build one skill named
`format-seed-labels` that reads `packet_inventory.csv` and makes a Markdown label
for each row. The label has exactly three lines:

```text
Crop: <crop>
Lot: <lot_id> | Packed: <packed_year>
Packets: <packet_count>
```

Keep values as supplied. Flag missing fields or a non-integer packet count
instead of inventing a value. This skill formats inventory text; it gives no
planting, food-safety or seed-viability advice.

Use Skill Builder's naming, overlap and dependency checks. A suitable existing
skill should be reused if one already owns this exact job. Put the reusable
format in the skill folder's `references/label_format.md` and have `SKILL.md`
point to it. The folder, not just its main file, is the deliverable.

This is an explicitly requested individual custom addition. Assign its system
according to the current vocabulary; the illustrative version uses Writing
System because its output is formatted copy. Do not install the whole optional
Writing System merely to add this one skill.
