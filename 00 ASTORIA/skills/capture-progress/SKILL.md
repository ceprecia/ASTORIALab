---
name: capture-progress
description: >-
  Saves project progress in the owning MOC's Research Log and follows the
  chosen project-only or Calendar-indexed capture preference. Nonproject or
  shared captures use the configured shared destination. Scales detail to the
  request, preserves source attribution, and returns an unsaved draft in the requested form or under the recipient's
  reporting policy unless saving is explicitly requested. WOOP requests keep their dedicated
  workflow. Triggers: capture this progress, log this progress, capture this
  work session, capture this system change.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: ""
  created: "2026-07-08"
  updated: "2026-11-01"
---

# Capture Progress

Save project progress directly in the project MOC's Research Log, with a Calendar index only when the chosen capture preference includes it.

## User Q&A

The user's configured choices persist across runs.

- **Where do project captures live?** In the owning MOC's existing Research Log. Both capture skills share that section; there are no separate project capture files or folders.
- **What stays in Calendar?** When the selected preference includes Calendar, `02 📅 Calendar/capture-logs/YY_Q#/YYYY-MM-DD_capture_log.md` contains live embeds of exact MOC entries and full originals for nonproject or shared captures with no clear owner. Project-only capture skips Calendar; an intentionally omitted Calendar is not recreated.
- **How much detail?** Match the request. A concise milestone may need only a few bullets; use fuller structure when the session requires it.
- **What metadata?** Keep MOC frontmatter unchanged. Add only needed entry attribution or covered dates; maintain Calendar aggregates only when the chosen route includes Calendar.
- **Should the skill save immediately?** Return an unsaved draft in the current task's requested form or under the recipient's existing reporting policy unless the user explicitly asks to save or create the entry.
- **What source material?** The current chat or named source notes/files. Broader scans require the user to ask for them.

## Purpose

Use when:

- The user wants a progress record from a work session, project, system change, research planning pass, or life-operations check-in.
- The user wants to preserve what changed, why, decisions, current state, open loops, and next actions.

Not for:

- Use [quick-capture](../quick-capture/SKILL.md) for a short thought or chat excerpt.
- Use [summarize](../summarize/SKILL.md) for a requested meeting or transcript summary. A verbatim record or save needs its own authorization.
- Use [woop-skill](../woop-skill/SKILL.md) for WOOP plans, reviews, revisions, or updates in `02 📅 Calendar/woop-captures/`.

## Capture destination preference

Resolve capture routing from the current request, `me.md`, and the layout reference before reading or writing a destination.

- **Project log only:** Save the original in the owning MOC's Research Log. Do not read, create, or update a Calendar index for that capture.
- **Project log plus Calendar:** Save the MOC original once and add the exact dated Calendar reference described below.
- **Unspecified:** Preserve the established capture convention. In the unchanged default layout, this is the MOC original plus Calendar index; a recorded project-only choice takes precedence.
- **Calendar intentionally omitted or replaced:** Use the configured replacement for shared captures and indexing, if one was chosen. Never recreate an intentionally omitted Calendar. If a nonproject capture has no configured destination, resolve it before saving. Meanwhile, continue the unsaved draft in the current task's requested form or under the recipient's existing reporting policy.

A current explicit capture request may override an earlier preference for that request. A preference to write one's own notes does not authorize automatic capture. Both capture skills use the same selected route, and Calendar-specific steps and metadata apply only when that route includes Calendar.

## Resolve the destination

1. Read `/me.md`, `/00 ASTORIA/agent_notes/layout.md`, and the relevant capture entries in `/00 ASTORIA/Skill Map.md` when starting cold.
2. Identify the requested content, source basis, covered dates, and chosen capture route. Use today's local date for a new entry and any selected Calendar note unless the user specifies another date; retain the actual covered period when different.
3. Assign a project owner only from the user's explicit scope or unambiguous current project context. A project mentioned in the content is not automatically its owner. Shared work without a clear owner uses the configured shared capture destination, with relevant project attribution.
4. Verify the owning MOC from live instructions, the existing note, or the user's supplied path. Do not guess project mappings or create a project home. Resolve an ambiguous or missing named destination with the user.
5. Read the MOC's Research Log and only the selected index or shared destination before writing. Reuse the existing log heading and grouping. Neither capture skill needs a project capture folder or a note template.

## Steps

1. Draft a progress entry from the bounded source material. Respect the requested brevity. Include useful progress, decisions, current state, or next actions without forcing a long template. Distinguish scientific observations, interpretations, and possibilities; do not invent results or missing context.
2. If the user has not asked to save or create it, show the unsaved draft in the current task's requested form or under the recipient's existing reporting policy and ask for approval before writing. If the current request already authorizes saving or creating it, continue without a new confirmation.
3. Check whether this exact capture was saved during an earlier attempt by matching its source, content, covered period, and heading. Similar topics alone are not duplicates. On retry, reuse the saved original and repair only missing metadata or references required by the selected route.
4. Give a new entry a unique full-date heading: `YYYY-MM-DD HH:MM - Capture Progress: Short Title`. Add seconds and then a numeric suffix if needed. Use ordinary Markdown at the appropriate depth beneath the log or its existing date/period group; preserve saved headings.
5. Save the full original once, directly in the owning MOC's Research Log, or in the resolved shared capture destination for nonproject/shared content. Preserve existing content, MOC frontmatter, grouping, and order; use newest first if a new log has no established order. Create one Research Log only if absent, or `## Captures` only when needed in the selected shared destination. For a selected Calendar original, update its supported metadata aggregates. Re-read and verify the saved entry and exact heading before creating any selected index reference.
6. Only when the selected route includes Calendar, add one project-original Calendar embed on its own line outside callouts: `![[<full vault-relative MOC path>#<exact entry heading>]]`. Preserve existing aliases. Convert a plain link to the same target in place rather than adding another reference. Update Calendar's supported metadata aggregates. Nonproject/shared originals in Calendar need no self-embed.
7. Verify the original, exact anchor, the index reference only when selected, metadata, and absence of duplicate entries or references. Compare resolved targets, not display labels. Make writes sequentially and re-read each target before writing. If an authorized Calendar update fails, retain the verified MOC entry and report what remains; retry repairs that pointer without saving another copy.
8. Confirm the original's resolved path and entry heading briefly.

## Calendar Format and Metadata

Apply this daily-file frontmatter only when the selected route uses Calendar. Do not apply it to a project MOC or replace the MOC's existing properties.

```yaml
---
related:
created: YYYY-MM-DD
type: capture_log
capture_kind: daily_capture_log
capture_kinds:
  - progress_capture
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

- In Calendar, union supported values into `capture_kinds`, `projects`, `areas`, `systems`, `quarters`, `source_context`, and `creator` for each original or embedded entry. Include `progress_capture` and the `capture_logs` system; preserve existing fields and values.
- Keep `created` unchanged. Extend `period_start` and `period_end` only for known covered dates, preserving the existing range. Derive quarters from known dates. Use `codex_session` only when it is the actual source.
- Keep MOC frontmatter unchanged. Add brief source or covered-period information to an entry only when needed for attribution or meaning. Do not add empty metadata blocks or convert the MOC into a capture note. Preserve historical entry metadata during an authorized migration.
- Follow the recipient's note conventions in `me.md` for metadata and link selection. Verify the destination of every added navigation link.

## Entry Format

Use an ordinary dated heading with only the useful content. This small example fits directly beneath a level-one Research Log; adjust heading depth to the existing log hierarchy.

```markdown
## YYYY-MM-DD HH:MM - Capture Progress: Short Title

- **Progress:** [What changed and why it matters.]
- **Next:** [The relevant next action, if any.]
```

For a substantial session, add only useful child headings such as Source Basis, Progress Logged, Decisions Made, Current State, Open Loops, or Next Actions. A brief milestone does not require them. Keep source and period notes concise, omit empty fields, and retain fuller historical metadata when migrating an existing record.

When selected, Calendar embeds the exact entry using the verified path and heading; never save these placeholders:

```text
![[<full vault-relative MOC path>#<exact entry heading>|YYYY-MM-DD HH:MM - Project: Short Title]]
```

## Boundaries

- Both capture skills write project originals into the same Research Log inside the owning MOC. Multiple entries on one date need only distinct headings. Never create a project capture file, a `capture_logs/` folder, a daily project note, or an inventory of links to separate copies.
- Keep log entries and Calendar embeds as ordinary Markdown outside callouts. Nest entry headings beneath their containing log or existing group heading and any entry subsections beneath the entry, so they fold without swallowing adjacent records.
- Preserve existing log headings, grouping, and order. If the MOC has no log section, create one `Research Log` at its existing main-section heading level. If this change affects navigation, update the exact verified link or card called for by the recipient's established layout and authorized scope. Preserve unrelated navigation and existing callout placement. Add a new card or per-entry links only when the recipient's conventions or an explicit request authorize that specific navigation.
- Do not embed a MOC into itself, link it to another copy of its own entry, or embed Calendar back into the MOC. Calendar embeds target the exact MOC entry rather than the whole MOC or Research Log.
- **Multiple projects:** Use an explicit or unambiguous primary owner when one exists and retain relevant project attribution. Otherwise use the resolved shared capture destination; do not duplicate or arbitrarily split it between MOCs.
- **Historical records:** Routine capture does not migrate history. An authorized migration preserves source text, metadata, original dates, and month/period groupings inside the MOC's Research Log. Keep historical headings and timestamps; do not invent daily timestamps for period records. Verify the MOC original before replacing an older Calendar copy or pointer with an embed of that exact entry.
- **Spanning periods:** Keep actual covered dates and source context. Do not relabel older work as today's work.
- **Sparse sources:** Record what is known and label relevant gaps.
- **Sensitive material:** Ask whether to save locally before writing unless the user has already authorized that save.
