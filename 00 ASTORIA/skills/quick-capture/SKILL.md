---
name: quick-capture
description: >-
  Saves short text or chat excerpts in the owning MOC's Research Log and
  follows the chosen project-only or Calendar-indexed capture preference.
  Nonproject or shared captures use the configured shared destination. Keeps entries
  minimal and saves directly on request. Triggers: quick capture this, jot this down, add this to today's
  capture.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: ""
  created: "2026-07-08"
  updated: "2026-11-01"
---

# Quick Capture

Save a short item directly in its project MOC's Research Log, with a Calendar index only when the chosen capture preference includes it.

## Purpose

Use when:

- The user wants to save one short thought, phrase, decision, snippet, or AI chat excerpt quickly.
- The user says `quick-capture`, `quick capture`, `jot this down`, or asks to add something to today's capture.
- The content is worth preserving but does not need a full structured progress entry. The capture request authorizes saving; do not add a separate draft approval.

Not for:

- Use [capture-progress](../capture-progress/SKILL.md) when the work needs context, decisions, current state, open loops, next actions, or a broader source scan.
- Use [summarize](../summarize/SKILL.md) when the full conversation must be kept word for word, or when the main job is a structured summary or BLUF.

## Capture destination preference

Resolve capture routing from the current request, `me.md`, and the layout reference before reading or writing a destination.

- **Project log only:** Save the original in the owning MOC's Research Log. Do not read, create, or update a Calendar index for that capture.
- **Project log plus Calendar:** Save the MOC original once and add the exact dated Calendar reference described below.
- **Unspecified:** Preserve the established capture convention. In the unchanged default layout, this is the MOC original plus Calendar index; a recorded project-only choice takes precedence.
- **Calendar intentionally omitted or replaced:** Use the configured replacement for shared captures and indexing, if one was chosen. Never recreate an intentionally omitted Calendar. If a nonproject capture has no configured destination, resolve it before saving. Meanwhile, continue the unsaved draft in the current task's requested form or under the recipient's existing reporting policy.

A current explicit capture request may override an earlier preference for that request. A preference to write one's own notes does not authorize automatic capture. Both capture skills use the same selected route, and Calendar-specific steps and metadata apply only when that route includes Calendar.

## Steps

1. Read `/me.md`, `/00 ASTORIA/agent_notes/layout.md`, and the relevant capture entries in `/00 ASTORIA/Skill Map.md` when starting cold. Identify the short content the user wants saved; ask for it if missing.
2. Resolve the owner, destination, and chosen capture route. Read the MOC's Research Log and only the selected index or shared destination. Reuse existing log headings, grouping, and order.
3. Check whether this exact capture was saved during an earlier attempt by comparing its source, text, covered period, and heading. A similar topic alone is not a duplicate. On retry, reuse the saved original and repair only missing metadata or references required by the selected route.
4. Keep the captured text succinct and minimally transformed. Remove obvious chat scaffolding only when meaning is preserved. Do not invent claims, decisions, or context. Use a unique full-date heading `YYYY-MM-DD HH:MM - Quick Capture: Short Title`; add seconds and then a numeric suffix if needed. Use ordinary Markdown at the appropriate depth beneath the log or its existing group and keep saved headings stable.
5. Save the full original once, directly in the owning MOC's Research Log, or in the resolved shared capture destination for nonproject/shared content. Preserve existing content and MOC frontmatter. Create one Research Log only if absent, or `## Captures` only when needed in the selected shared destination; use newest first if a new log has no established order. For a selected Calendar original, update its supported metadata aggregates. Re-read and verify the saved text and heading before creating any selected index reference.
6. Only when the selected route includes Calendar, add one project-original Calendar embed on its own line outside callouts: `![[<full vault-relative MOC path>#<exact entry heading>]]`. Preserve existing aliases. Convert a plain link to the same target in place rather than adding another reference. Aggregate supported entry metadata into Calendar. Nonproject/shared originals in Calendar need no self-embed.
7. Verify the original, exact anchor, the index reference only when selected, metadata, and absence of duplicates. Compare resolved targets, not display labels. Make writes sequentially and re-read each target before writing. If an authorized Calendar update fails, keep the verified MOC entry, report the missing pointer, and repair it on retry without appending another copy.
8. Confirm the original's resolved path and entry heading in one sentence.

## Calendar Format and Metadata

Apply this daily-file frontmatter only when the selected route uses Calendar. Do not apply it to a project MOC or replace the MOC's existing properties.

```yaml
---
related:
created: YYYY-MM-DD
type: capture_log
capture_kind: daily_capture_log
capture_kinds:
  - quick_capture
period_start: YYYY-MM-DD
period_end: YYYY-MM-DD
quarters:
  - YY_Q#
projects: []
areas: []
systems:
  - capture_logs
source_context: []
creator:
  - AI
---
```

```markdown
# Capture Log

## Captures
```

- In Calendar, union supported values into `capture_kinds`, `projects`, `areas`, `systems`, `quarters`, `source_context`, and `creator` for each original or embedded entry. Include `quick_capture` and the `capture_logs` system; preserve existing fields and values.
- Keep `created` unchanged. Extend `period_start` and `period_end` only for known covered dates, preserving the existing range. Derive quarters from known dates. Use `codex_session` only when it is the actual source.
- Keep MOC frontmatter unchanged. Add brief source or covered-period information to an entry only when needed for attribution or meaning. Do not add empty metadata blocks or convert the MOC into a capture note. Preserve historical entry metadata during an authorized migration.
- Follow the recipient's note conventions in `me.md` for metadata and link selection. Verify the destination of every added navigation link.

## Minimal Entry Format

Use ordinary Markdown outside callouts so the entry folds under its dated heading. This example fits beneath a level-one Research Log; adjust heading depth to the existing log hierarchy.

```markdown
## YYYY-MM-DD HH:MM - Quick Capture: Short Title

[short captured text]
```

Do not add structured progress sections. Add a brief source or period line only when needed to preserve attribution, supplied historical dates, or meaning. Keep actual source metadata during an authorized repair or migration.

When selected, Calendar embeds the exact entry using the verified path and heading; never save these placeholders:

```text
![[<full vault-relative MOC path>#<exact entry heading>|YYYY-MM-DD HH:MM - Project: Short Title]]
```

## Outputs

- **Project-owned original:** The owning project MOC's existing Research Log, shared with capture-progress. Use one section with dated entries, without separate project capture files or folders.
- **Optional Calendar index and shared originals:** When the selected route includes Calendar, `02 📅 Calendar/capture-logs/YY_Q#/YYYY-MM-DD_capture_log.md` holds live embeds of exact MOC entries and originals for nonproject/shared content. Otherwise use the configured shared destination and omit the Calendar index.

Assign ownership only from the user's explicit scope or unambiguous current project context. A project merely mentioned in the text is not necessarily its owner. Verify the owning MOC from live instructions, the existing note, or the user's supplied path. Do not guess project mappings or create a project home. Resolve an ambiguous or missing named destination with the user; genuinely nonproject/shared content uses the configured shared destination.

Use today's local date and, when Calendar is selected, its `YY_Q#` quarter unless the user specifies another date. Preserve any actual covered period. No project capture folder, separate daily project note, or note template is needed.

## Boundaries

- Both capture skills write project originals into the same Research Log inside the owning MOC. Multiple entries on one date need only distinct headings. Never create a project capture file, a `capture_logs/` folder, a daily project note, or an inventory of links to separate copies.
- Keep log entries and Calendar embeds as ordinary Markdown outside callouts. Nest entry headings beneath their containing log or existing group heading and any entry subsections beneath the entry, so they fold without swallowing adjacent records.
- Preserve existing log headings, grouping, and order. If the MOC has no log section, create one `Research Log` at its existing main-section heading level. If this change affects navigation, update the exact verified link or card called for by the recipient's established layout and authorized scope. Preserve unrelated navigation and existing callout placement. Add a new card or per-entry links only when the recipient's conventions or an explicit request authorize that specific navigation.
- Do not embed a MOC into itself, link it to another copy of its own entry, or embed Calendar back into the MOC. Calendar embeds target the exact MOC entry rather than the whole MOC or Research Log.
- **Multiple projects:** Use an explicit or unambiguous primary owner when one exists and retain relevant project attribution. Otherwise use the resolved shared capture destination; do not duplicate or arbitrarily split it between MOCs.
- **Historical records:** Routine capture does not migrate history. An authorized migration preserves source text, metadata, original dates, and month/period groupings inside the MOC's Research Log. Keep historical headings and timestamps; do not invent daily timestamps for period records. Verify the MOC original before replacing an older Calendar copy or pointer with an embed of that exact entry.
- Preserve existing captures and unrelated MOC content. Do not add unrelated wiki-links or relationship fields.
- If the content becomes a fuller progress record, use [capture-progress](../capture-progress/SKILL.md) with the same resolved MOC Research Log or Calendar destination. Do not create a parallel record.
