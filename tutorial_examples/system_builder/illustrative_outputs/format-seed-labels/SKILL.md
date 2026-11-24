---
name: format-seed-labels
description: >-
  Formats supplied seed-inventory rows into three-line Markdown labels and
  reports incomplete rows. Use for this inventory-to-label procedure.
  Triggers: make packet labels, format this seed inventory.
metadata:
  level: skill
  system: Writing System
  dependencies: ""
  created: "2026-11-23"
  updated: "2026-11-23"
---

# Format Seed Labels

Turn supplied inventory fields into consistent labels.

## Purpose

Format inventory text. Do not infer seed quality or provide planting advice.

## Inputs

A CSV with `crop`, `lot_id`, `packed_year` and `packet_count` columns.

## Steps

1. Read the supplied CSV and [label format](references/label_format.md).
2. Check each required value is present and `packet_count` is a nonnegative
   integer. List invalid rows and the missing or invalid field.
3. Format each valid row using the reference exactly. Preserve crop, lot and
   year values. Do not silently correct or fill source data.
4. Return the labels in chat, or save them to the destination the user requested.

## Outputs

One three-line label per valid row and a separate list of any invalid rows.

## Checks

Every valid source row appears once. Label values match that row. Incomplete
rows are reported rather than completed with guessed data.
