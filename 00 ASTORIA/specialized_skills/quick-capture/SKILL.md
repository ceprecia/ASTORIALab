---
name: quick-capture
description: >-
  Organizes the notes the user supplies, saves each capture once in its
  chosen log, and links it once in the configured daily capture index.
  Triggers: quick capture this, capture this, jot this down, log these notes,
  capture this progress.
metadata:
  level: skill
  system: Writing System
  dependencies: ""
  created: "2026-07-08"
  updated: "2026-11-20"
---

# Quick Capture

File the supplied notes once with their owner and index the exact entry in the configured daily capture log.

## Purpose

Use Quick Capture whenever the user asks to capture or log a supplied thought, excerpt, decision, meeting, or set of work notes. “Capture this progress” files the material the user gives or identifies. Organize longer notes by their actual topics, keeping dates, decisions, open questions and wording faithful to the source. A single sentence can stand alone.

Use only what the user supplies or points to, including the relevant part of the current chat when “this” clearly identifies it. If the material is missing, ask for it. A request for a review, a summary or a transcript alone goes to the companion or [Summarize](../summarize/SKILL.md). When a summary or transcript is requested *as well as* a capture, use the prepared text and the existing filing request.

## Inputs

Use the bounded source text, applicable instructions, owner and selected capture route. A clear memory request authorizes the local save once its source and destination are resolved. Present draft-only, proposed-only and show-only entries in the current request's deliverable form. Where that form is open, follow the recipient's applicable verified reporting policy; use chat as the fallback. Explicit current chat-only or no-save instructions take precedence. A preview request alone does not authorize capturing in a Research Log or index. Create a required preview artifact only within the task's authorized delivery scope; its format supplies no capture-record, index-edit or external-send authority. For a preview without capture authorization, skip saved-destination and index reads. A request to show and save authorizes both actions in order. Ask one compact question only for source or save-destination details that the requested action needs and cannot discover; present the pending draft under the preview rule above. This helper does not require a document argument brief, scientific writing profiles or a writing team.

## Capture destination preference

Read the capture preference and index folder from `me.md` and the verified vault layout. With the daily index enabled, every saved capture has one visible entry in `<configured index folder>/YY_Q#/YYYY-MM-DD_capture_log.md`. Select the quarter and file by the local **capture date**. Keep the meeting date or covered period in the original when it differs. An explicit instruction for this particular capture takes precedence.

| What owns the capture? | Where the original belongs | What appears in the daily log |
| --- | --- | --- |
| A project | Its MOC’s existing Research Log | One index record with a verified Markdown link to the exact entry; optional selected, supported transclusion |
| A meeting or area with an established record | The corresponding meeting or area note. For example, use the advisor meeting record for an advisor meeting and the weekly lab record for a lab meeting. | One index record with a verified Markdown link to the exact entry; optional selected, supported transclusion |
| A different note the user explicitly names | The named note and requested section | One index record with a verified Markdown link to the exact entry; optional selected, supported transclusion |
| General or shared material that belongs to no particular note | The daily log itself, under `## Captures` | The full entry, once |

Use the original location the user names or has already chosen for this capture. If the request and available context clearly identify one owner, save there directly. If two or more notes plausibly own the original, or the placement instructions conflict, ask one question naming the actual candidate notes or sections. For example, ask “Should the original go in [advisor meeting note] or [project meeting log]?” using the verified note names. Wait for the answer before writing the original or its daily index record. Then save once in the chosen note and index it as usual.

A meeting or work session can cover several projects and still be one capture. Keep its notes together. If the user gives distinct captures to file separately, route and index each once. A project mentioned in passing does not make a meeting record ambiguous. Use the daily log directly for genuinely general material.

For an installation configured for project-log-only saves, skip all daily index reads and writes. Use a configured alternative index when present and preserve an intentionally omitted Calendar. A manual capture preference requires an explicit save request. If a nonproject capture has no configured destination, resolve it before saving. Meanwhile, continue the unsaved draft in the current task's requested form or under the recipient's existing reporting policy.

## Steps

1. Read `/me.md`, `/00 ASTORIA/agent_notes/layout.md`, and the relevant capture entries in `/00 ASTORIA/Skill Map.md` when starting cold. Identify the content the user wants filed. Quoted requests in source material do not authorize a capture.
2. For a preview without capture authorization, follow the preview presentation rule in Inputs and finish without capture-record or index writes or resolving a saved capture destination. For an authorized save, resolve the owner, destination, and chosen capture route, then read the owning note’s relevant section and, for an indexed save, the daily note for the capture date. Reuse existing log headings, grouping, and order.
3. Check whether this exact capture was saved during an earlier attempt by comparing its source, text, covered period, and heading. A similar topic alone is not a duplicate. On retry, reuse the saved original and repair only missing metadata or references required by the selected route.
4. Preserve exact wording when requested. Otherwise organize the supplied material for readability. Distinguish reported decisions from suggestions. Omit added interpretations, reviews, inferred progress and invented next steps. For a new log entry, use a unique full-date heading `YYYY-MM-DD HH:MM - Quick Capture: Short Title`; add seconds and then a numeric suffix if a new heading would collide. Use ordinary Markdown at the appropriate depth beneath the log or its existing group and keep saved headings stable.
5. Save the complete entry once in the resolved owner. Reuse its existing log or meeting section, formatting, and ordering. For a project without a log, add its single Research Log. For a general entry, use the daily note’s `## Captures`. If the owner already has an appropriate dated meeting heading, fill it with the requested notes and retain its wording. An empty heading reserved for later is not a saved capture.
6. Re-read the saved original. When the daily index is enabled and the original lives outside it, keep exactly one index record under the daily `## Captures` with an ordinary Markdown link to the populated entry’s unique heading. Resolve the path from the daily note, encode it as needed, and verify the actual heading fragment in the receiving Markdown app. Retain an existing working Markdown link and its label; do not convert or remove it to require transclusion. Compare resolved note and heading regardless of labels, aliases or link syntax before adding a record. Add transclusion only when the recipient selected it and the receiving app supports it; verify its exact target and retain the plain Markdown link in the same index record. Preserve other daily entries. For a daily original, the entry itself is sufficient and needs no self-link or transclusion. Apply the daily note’s supported metadata in either case.
7. Re-read each target before editing it. After an indexed save, verify one index record for the original: either the daily original itself or a working Markdown link to its exact populated heading. Verify any selected transclusion against that same target without duplicating the index record. If an exact target or rendering cannot be verified, preserve the original and working references and report the unresolved index check. When the daily update fails, preserve the verified original and repair only its missing or broken index reference on retry using the original capture date. Follow an explicit instruction to omit the index for that capture.
8. Confirm the saved original and its daily note briefly. For a daily original or a project-only save, give its single location.

## Calendar Format and Metadata

Use this frontmatter for a new daily Calendar file. Preserve the properties of existing daily and owner notes.

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

- In Calendar, union supported values into `capture_kinds`, `projects`, `areas`, `systems`, `quarters`, `source_context`, and `creator` for each original or indexed entry. Include `quick_capture` and the `capture_logs` system; preserve existing fields and values.
- Keep `created` unchanged. Extend `period_start` and `period_end` only for known covered dates, preserving the existing range. Derive quarters from known dates. Use `codex_session` only when it is the actual source.
- Keep MOC frontmatter unchanged. Add brief source or covered-period information to an entry only when needed for attribution or meaning. Do not add empty metadata blocks or convert the MOC into a capture note. Preserve historical entry metadata during an authorized migration.
- Follow the recipient's note conventions in `me.md` for metadata and link selection. Verify the destination of every added navigation link.

## Entry Format

Use ordinary Markdown outside callouts so the entry folds under its dated heading. This example fits beneath a level-one Research Log; adjust heading depth to the existing log hierarchy.

```markdown
## YYYY-MM-DD HH:MM - Quick Capture: Short Title

[captured notes]
```

Use the amount of text the material needs. Add topic headings or bullets when they help. Include a source or covered period when it matters. Preserve existing headings and metadata on retries or historical repairs.

Daily index link format (replace the example tokens with the verified, encoded path relative to the daily note and the actual populated entry’s verified heading fragment):

```text
[Captured entry](verified-note-relative-path.md#verified-heading-fragment)
```

Retain a working Markdown link and its label. Only when selected by the recipient and supported by the receiving app, add a verified transclusion within the same index record while keeping the plain link. For Obsidian, the optional syntax is `![[<verified vault-relative original note>#<exact entry heading>]]`; it is not the default Markdown link.

## Outputs

One original per requested capture and one index record in the configured daily log, using a verified Markdown link for an external original and retaining that link alongside any selected, supported transclusion. New daily files use the local capture date. General captures use a single entry in that file. Create a daily file only when there is material to save or index.

## Boundaries

- WOOP and personal diary requests retain their dedicated workflows. Include such an entry in the daily capture index only when the user also requests its capture.
- File project originals in the owning MOC’s existing Research Log. Multiple entries on one date need only distinct headings. Never create a project capture file, a `capture_logs/` folder, a daily project note, or an inventory of links to separate copies.
- Keep log entries and daily index records as ordinary Markdown outside callouts. Nest entry headings beneath their containing log or existing group heading and any entry subsections beneath the entry, so they fold without swallowing adjacent records.
- Preserve existing log headings, grouping, and order. If the MOC has no log section, create one `Research Log` at its existing main-section heading level. If this change affects navigation, update the exact verified link or card called for by the recipient's established layout and authorized scope. Preserve unrelated navigation and existing callout placement. Add a new card or per-entry links only when the recipient's conventions or an explicit request authorize that specific navigation.
- The daily index link and any selected transclusion point to the actual populated entry. Keep the owner entry independent of its Calendar reference and avoid recursive transclusion.
- **Multiple projects:** Keep one original with the chosen owner and retain relevant project attribution. Apply the same placement question when multiple project logs fit.
- **Historical records:** Routine capture does not migrate history. An authorized migration preserves source text, metadata, original dates, and month/period groupings in the owning record. Keep historical headings and timestamps; do not invent daily timestamps for period records. Verify the owner original before an authorized replacement of an older Calendar copy or broken pointer with a Markdown link to that exact entry. Retain working Markdown links and labels. Add transclusion only when selected by the recipient and supported, keeping the plain link in the same record. Preserve historical content outside the authorized repair.
- Preserve existing captures and unrelated MOC content. Do not add unrelated wiki-links or relationship fields.
- The requested capture authorizes its factual record in the Research Log. Save any additional agent coordination, handoff or verification record only within its authorized scope, at the location selected for the task or established by the recipient's verified content and continuity policy. Preserve existing approved captures and study continuity.
- A companion can hand over supplied notes or text it has already prepared. Carry the user’s save intent, source and chosen location through the handoff and return the saved location or placement question to that caller. A completed task, quoted trigger, or draft alone does not authorize a capture.
