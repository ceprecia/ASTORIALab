---
name: summarize
description: >-
  Summarizes a supplied conversation, meeting, or transcript in the selected
  form, including a brief BLUF. Produces a verbatim transcript or a combined
  summary and transcript only when expressly requested. Saves only with
  authorization to a verified destination. Triggers: save this verbatim, keep
  this exchange word for word, summarize this conversation, summarize this
  meeting, give me a BLUF.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: ""
  created: "2026-09-24"
  updated: "2026-11-01"
---

# Summarize

Return the requested summary of the bounded source. Use the form selected for
the task or the recipient's established reporting form. Producing a verbatim
record and saving are separate choices that require explicit direction.

## Modes

- **Summary.** Return only the requested summary of the exchange, meeting or
  transcript. Use a concise form when no format is specified.
- **BLUF (bottom line up front).** Give the main point in one sentence. Add a
  second only if it needs a material qualification.
- **Transcript.** Reproduce the authorized text verbatim only when expressly
  requested. Add a short preamble only if asked.
- **Summary and transcript.** Use this mode only when both are expressly
  requested. Keep the summary and verbatim record distinct.

## Steps

1. **Scope.** Use the supplied source or the exchange the request clearly
   identifies. Clarify only a material ambiguity about scope or output. Keep
   other conversations, attachments, protected files and private history
   outside the task unless specifically included and authorized.
2. **Destination.** Resolve the exact eligible destination only for an authorized write. Use the user's selected path and filename first. Where a choice is open, follow the recipient's applicable verified destination and naming conventions. If neither identifies a location, use the verified owner location for Project or Area working material and the selected topic collection for reusable references. Use `00 ASTORIA/agent_notes/` only for authorized system or agent records that belong there under a selected or verified convention. For an ownerless user record such as a meeting transcript, ask for an eligible destination if the selected or verified policy leaves it open. The fallback filenames are `YYYY-MM-DD_transcript_<description>.md` for a transcript or `YYYY-MM-DD_summary_<description>.md` for a summary or combined note. Saving does not authorize a separate note edit or index link. The capture-log family remains with [quick-capture](../quick-capture/SKILL.md) and [capture-progress](../capture-progress/SKILL.md).
3. **Prepare.** Produce only the selected mode. Ground the summary in the
   source. Keep decisions, proposals and unresolved points distinct. Preserve
   material figures, units and qualifications. Give owners and dates only
   when the source establishes them. Keep different meetings identifiable.
4. **Existing file.** A file named as a source can be read within scope.
   Edit it only when the exact file, change and placement are authorized.
   Add or update only the summary at the authorized placement. Preserve the
   original text, transcript, headings and other content in place. Show the
   diff before replacing an existing partial summary. If the request already
   authorizes the exact edit, proceed under that authorization.
5. **Return or save.** Return the selected output in the requested or configured
   form. Save only when the request authorizes the write and the exact destination
   is verified. For an authorized Markdown note, follow applicable note
   conventions. Verify any write and report the filename and location.

## Verbatim records

Preserve the authorized text, role order, repetitions, line breaks and code.
When the source is partial, report the gap. A summary uses what is available,
and a requested transcript quotes only the available authorized text.

Include visible tool calls, results or image markers only when the request
expressly includes them and the source is authorized. Leave hidden tool
traces, other history and unrelated attachments outside the record. Replace
credentials or other secrets in newly produced content with `[REDACTED]` and
note the redaction. Preserve the original source.

## Optional summary layout

Use this layout when the user selects it or it fits the requested reporting
form. Choose the headings and detail that the source and task support.

```markdown
In summary, {{main point and any material qualification}}

## Key Takeaways & Headlines

- {{finding and supporting evidence}}

## Topics & Things

- {{relevant people, dates, numbers or concepts}}

## Next Steps

- {{stated action with an owner and deadline when known}}
```

Use literal text blocks and role markers for a Markdown transcript. Choose
fences longer than any fence in the source. In a requested combined output,
place the summary above the transcript unless the selected form specifies
another order.

`````markdown
# Transcript

**User:**

````text
<exact authorized message>
````

**Assistant:**

````text
<exact authorized reply>
````
`````

## Examples and checks

- “Summarize this meeting.” Return a summary of the supplied meeting in the
  selected form.
- “Just the BLUF.” Return the brief bottom line.
- “Give me this exchange verbatim.” Return the scoped transcript. If the user
  also requests a save, verify and use the authorized destination.
- “Give me a summary and verbatim record.” Return both as distinct sections.
- “Add a summary above the transcript in this file.” Apply that authorized
  insertion after verifying the exact file. Preserve the transcript and other
  source content in place.

Check that the output contains only the selected mode and stays within the
authorized source. Verify any stated decisions, actions and material details.
Compare a requested verbatim record with its available source, allowing only
disclosed redactions and marked gaps. Confirm authorization and the exact
destination before reporting a save.
