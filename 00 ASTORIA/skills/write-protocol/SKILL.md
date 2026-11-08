---
name: write-protocol
description: >-
  Curates established work into durable, user-reviewed protocols in selected MOC
  sections across projects. Uses an overview selection gate and a final detailed
  content and placement review before asking to publish; progress logs remain
  separate. Triggers: turn this into a protocol, document this established
  process, update the project protocol, formalize these working steps.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: ""
  created: "2026-10-27"
  updated: "2026-11-01"
---

# Write Protocol

Turn established work into a curated protocol the user can understand and use without the original conversation.

## Purpose

- Create or update protocols in the user-selected sections of an associated MOC, across research, engineering, teaching, software and other projects.
- Reconstruct the enduring procedure, its purpose and important choices from scoped conversations and relevant working materials. Organize around tasks and understanding; introduce scripts or tools where they serve the procedure.
- Keep protocol writing distinct from dated progress capture. A script inventory, development chronology or transcript is not a finished protocol.
- Use two substantive review gates followed by a publication question. Gate 2 is the last detailed gate. Additional discussion is led by the user.

## Inputs

- **Source scope:** the current conversation and user-named materials covering the established work. Read relevant implementations, configurations or execution evidence when they help resolve what actually works.
- **Destination:** the owning MOC and requested section or sections, resolved from the request and live project context. Read existing content and applicable instructions before proposing changes.
- **Reader and purpose:** use the user's stated audience and intended use. Ask only when a missing detail materially changes the proposed protocol; do not add a routine intake gate.
- **Existing choices:** retain decisions about scope, detail, commands, diagrams and placement across turns. Ask only about unresolved choices.

## Steps

### 1. Establish the source and destination

1. Follow `me.md` and applicable project instructions for context, writing conventions and placement.
2. Read the scoped source material and requested MOC sections. Identify established steps, important explanations, reusable decisions and unfinished possibilities. Do not turn a planned or merely started operation into a demonstrated success.
3. Compare the existing text with what the user wants to preserve. Distinguish a bounded insertion from a replacement or a wider protocol update.
4. Prepare a task-oriented candidate outline. Use only the sections the subject needs; there is no mandatory protocol template. Keep dated session history and internal AI working material separate from the proposed human-facing protocol.

### 2. Gate 1: Select the overview items

1. Print a concise overview of candidate topics. Give each an identifier, short description, quick include/defer/omit recommendation and one-line reason.
2. Ask which overall items the user wants included, with yes/no choices. Accept natural-language edits, selected identifiers or acceptance of the recommended set.
3. Pause for the user's selection. Recommendations are proposals, not answers. Selection at this gate defines content scope and does not authorize saving.
4. Carry the selected outline and settled preferences into Gate 2. Do not include declined topics in the detailed draft.

### 3. Gate 2: Review placement, detail and actual text

Present one consolidated detailed review for the selected content. For each affected section, print:

- **Destination:** the exact MOC and heading hierarchy.
- **Operation:** add, replace or merge, identifying the existing text that would change.
- **Detail:** the proposed depth, explanations, choices and examples, with a brief recommendation where a choice remains open.
- **Optional elements:** whether commands, setup instructions, diagrams, tables, screenshots or references belong in that section. Carry forward the user's existing choices.
- **Proposed text:** the actual wording and any proposed diagrams or other selected elements that would be saved, grouped under the destination headings. An outline or promise of later writing is insufficient.

Commands and setup instructions are optional user choices. Omit operator commands from the human-facing protocol unless the user selects them; do not automatically transfer AI Notes into it. A protocol can be complete at the user's chosen scope without command blocks.

Draft the proposed text using the protocol-writing and print conventions below. Keep the review labels (Destination, Operation, Detail and Optional elements) outside the proposed protocol text. Preserve useful existing diagrams unless the reviewed change explicitly alters them. Perform the style/printability check internally while drafting; it is not another user review gate.

Resolve concerns within this review phase. When the user requests a change, revise and show only the affected text and its placement; retain settled decisions elsewhere. Reopen overview choices only if the user changes scope. Do not introduce another detailed gate, compulsory checklist, scored review or full-draft approval round after Gate 2.

### 4. Final insertion plan and publication question

1. Once the details are sufficient for the user, show a short final insertion plan: MOC, selected headings, add/replace/merge operations and the agreed optional elements. Refer to the reviewed text rather than printing the entire draft again.
2. Ask: **"Can we publish this protocol into [MOC and selected sections] now, or is there anything you still want to discuss?"** Substitute the exact destination.
3. In this skill, publication means saving the approved protocol into the selected local MOC sections. Content approval alone is not publication approval. If the user explicitly authorizes publishing the reviewed text while accepting Gate 2, honor that authorization without asking again.
4. If the user requests more discussion, address those concerns and revise the affected content. Do not restart settled gates or keep proposing more detail unasked. If the user declines or postpones publication, return the draft in the current task's requested form or under the recipient's existing reporting policy and leave the files unchanged.

### 5. Publish and verify

1. After publication approval, re-read the target sections and apply only the reviewed additions or replacements. Preserve unrelated content and retained diagrams.
2. Re-read the result. Verify the approved wording, heading hierarchy, links and placement, and check for duplicate insertions if the write is retried. Follow the existing MOC architecture; do not create a second hub.
3. Confirm briefly which MOC sections were updated and report any incomplete write. Do not create extra publication reports or another copy of the protocol.

## Protocol writing and print conventions

Use these conventions for the proposed protocol body. They do not change the two review gates or make any optional element mandatory.

### Build a readable task section

- Use a descriptive heading that names the task or work phase, such as "Prepare the session" or "Transfer the collected files." Nest it at the appropriate level under the existing MOC section; do not introduce a second document title or another hub.
- Open with one or two short sentences that orient the reader: what this task accomplishes and the local starting condition or necessary reason. Give only context needed for this section to stand on its own.
- Lead the reader through concrete actions in a usable order. Use short connected paragraphs for a straightforward procedure, numbered steps when order matters, and bullets for choices, equipment, criteria or parallel items. Choose the form that serves the task; do not number every sentence.
- Use familiar, active verbs: open, enter, select, change, run, copy, save, check and repeat. Address the reader directly. Use "First," "Next," "Then" or "Once it finishes" when a transition helps, without mechanically starting every step the same way.
- Name the relevant object where it is used: application, button, field, filename, script, folder, participant ID or other literal value. Use an exact entry-point name available in the scoped material instead of chat shorthand such as "script 01" or "the other script." Retrieve a missing name from that material or keep the unresolved question in the review discussion; do not invent it. Give a small worked example when it resolves an ambiguity. Explain placeholders that the reader must replace.
- Explain a consequential choice beside the action it affects. Show the expected response, resulting file or recognizable end state near that action, then say what to do next when useful. Distinguish normal progress from completion when that distinction matters.
- Place a short **Note:** or an if/then branch beside the relevant exception. Retain only established, useful troubleshooting; do not turn the section into a development diary.
- End when the task reaches its stated result. Avoid repeated conclusions, generic scope disclaimers, reminders of every excluded task or commentary about what the supplied source does not establish. Keep unresolved drafting questions in the review discussion unless the user selects them as necessary protocol content.
- Do not format every task as Purpose / Inputs / Use / Outputs / Status. State these naturally where useful. A compact reference table can hold genuinely comparable settings or definitions when selected.

### Make selected details legible in Markdown and print

- Use semantic Markdown headings, short paragraphs, ordinary lists and restrained emphasis. Use bold for an important UI label or a brief local note, and inline code for filenames, paths, literal input or other technical strings. Do not reproduce the source documents' font changes, colored commands, empty headings or inconsistent numbering.
- When commands are selected, introduce what the command accomplishes, put concise syntax in a fenced block and explain its expected result. Commands support the procedure; they do not replace the surrounding instructions. When commands are excluded, explain the user interaction without smuggling command lines into prose.
- When visuals are selected, place the diagram or image beside the step it supports and add a brief description of what the reader should notice. Explain the essential action/result in text so the instruction does not depend on an uncaptioned screenshot. Preserve retained Mermaid diagrams and keep labels understandable without color.
- Use tables for reference comparisons, mappings or settings with a genuine parallel structure, not as containers for long procedures. Keep columns and cell text narrow enough for a printed section.
- Make the selected subsection understandable on its own: retain a meaningful heading, the necessary starting condition, concrete actions and a recognizable result. Replace dangling "as before," "above," "below" or "see AI Notes" references with the minimal needed context or a specifically named dependency. Do not duplicate the whole MOC to accomplish this.
- Keep essential meaning in the text, not in hover text, collapsed callouts, color or links alone. A link can provide supplementary detail; the chosen printed section should still communicate its selected procedure.
- Avoid long unbroken strings, oversized figures and wide tables. Keep commands exact; do not insert line breaks that alter their meaning. Use verified language-appropriate continuations only when needed.
- Adapt to the user's existing Obsidian theme and selected format. Do not inject CSS, HTML layouts, font installations or a universal page template. Exact fonts and pagination depend on the print renderer; do not claim they were verified without inspecting that output.

### Embedded examples

These fictional situations illustrate the writing pattern. They are not project inputs, current institutional procedures or a template that every protocol must copy. Use only facts supplied for the task and the user's selected details.

**Example 1: A laboratory handoff, commands excluded**

#### Prepare sample labels for review

Open the approved sample manifest and the label preview. Match each proposed label to its manifest record using the supplied identifier and required fields. Leave unmatched records unresolved rather than inventing an identifier.

Send the matched preview to the designated operator for verification before labels are printed or attached. Record which records were verified and which remain pending. A completed preview does not establish that samples were relabeled.

**Example 2: A short technical procedure, commands selected**

#### Create a weekly results archive

Save a weekly copy of the project's `results/` folder while leaving the working files in place. In a Linux terminal, move to the project directory and create the archive:

```bash
cd /work/demo
tar -czf results_backup.tar.gz results/
```

Once the command finishes, you should have `results_backup.tar.gz` in the project directory. The original `results/` folder remains in place. Next, inspect the archive contents:

```bash
tar -tzf results_backup.tar.gz
```

Check that the listing contains the expected files from `results/`.

**Example 3: A nontechnical procedure, commands excluded**

#### Collect reflection forms

Reflection forms are due Friday. Tell the class the deadline, then collect the forms after class in the existing course folder.

Check each form for the student's name and course section. If a name is missing, return that form for correction.

**Example 4: A UI procedure with a local decision, commands excluded**

#### Import a session file

Open **FieldBook** and select **Import**. Choose `session.csv`, then select `ParticipantID` as the matching field.

Click **Preview**. You should see 12 rows. If the preview shows 12 rows, click **Save**. If the count differs, leave the import unsaved and check that you selected the intended file.

## Outputs

- **Before publication:** return the selected overview, detailed proposed text with destinations and a concise final insertion plan in the current task's requested form or under the recipient's existing reporting policy.
- **After publication:** the approved protocol in the selected sections of the existing MOC, plus a brief confirmation.
- Update the protocol at the requested scope when implementation changes; preserve the distinction between current instructions and dated progress records.

## Boundaries

- Apply the same workflow to any requested project domain; do not impose research-specific sections, fields or method choices.
- AI Notes remain the AI's technical working area. Include only user-selected material in the curated protocol; operator commands are never a mandatory protocol component.
- Document established behavior accurately. Make unfinished portions visible when the user chooses to retain them; do not invent missing procedures or silently settle substantive choices.
- Present draft text and placement decisions in the current task's requested form or under the recipient's existing reporting policy. Leave the files unchanged until publication is authorized. There are exactly two substantive review gates; the final publication question is a short write decision, not another detailed review.
- Publishing a protocol does not automatically create a Research Log entry, Calendar capture, separate protocol file or additional technical record. Those require their own requested scope.
- Writing the protocol does not execute the process being documented.

## Handoffs

- Use capture-progress for a separately requested dated progress record and quick-capture for a separately requested short note. Do not call either automatically after publishing a protocol.
- Use an applicable document-format skill if the user separately requests a file-format deliverable; retain the agreed content and destination scope.

## Checks

- The current owner and exact target headings are established; the proposed changes fit those sections.
- Gate 1 selected the overview; Gate 2 showed actual text, exact placement, change operations and optional content choices.
- The writing is useful without reconstructing the conversation and reflects the user's chosen depth. It uses task headings, brief context, direct actions and nearby results/examples, without becoming a script catalog or session log.
- The selected subsection remains intelligible when printed alone; review labels, temporary status and unselected commands do not enter the protocol body. Selected tables, code and visuals fit the intended reading width. Inspect an actual rendered print preview when the task includes print-layout verification, and otherwise state the validation limit.
- Commands, diagrams and other optional elements match the user's choices; omitted commands do not cause a new completeness gate.
- Settled choices persist. After Gate 2, move to the concise insertion plan and publication question, with further discussion only when requested by the user.
- A saved result matches the reviewed text and publication authorization, preserves unrelated content and contains no duplicate insertion.
