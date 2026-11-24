---
name: study-quiz
description: >-
  Builds flashcard decks, quizzes and practice exams in the selected form,
  with optional Markdown and Anki exports, visual interpretation, answer keys
  and worked solutions grounded in the course's study plan and sources. Reads
  Study Planner's roadmap to choose what to
  cover and never records progress or schedules reviews; practice inside a
  study session stays with Study Planner. Triggers: make flashcards for this,
  make me a practice quiz, build a practice exam.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: study-enricher
  created: "2026-09-30"
  updated: "2026-10-29"
---

# Study Quiz

Flashcards, quizzes, and practice exams you can keep and use anywhere.

## Purpose

It creates practice material in the selected form.

- flashcard decks, with Markdown and Anki import formats available individually or together;
- quizzes with an answer key;
- practice exams with mixed topics, a time budget, worked solutions and a scoring guide.

Not for: grouped checks, Pass 3, or any practice inside a study session (Study Planner); review scheduling or progress (Study Planner); teaching (Study Planner or Study Companion).

## Inputs

- **Scope:** the course and its units or topics. Default to what the Learning Roadmap shows as covered.
- **Format:** deck, quiz, or practice exam, with count and difficulty. Defaults: 20 cards, 10 quiz questions, or an exam sized to the stated time.
- **Visual support:** Full by default. Include plots, diagrams, tables, equations, and example-based interpretation across the relevant learning outcomes, rather than limiting the whole set to one visual. Keep the requested item count and difficulty; honor fewer/no visuals or a shorter format.
- **Destination:** Resolve it only for an authorized file deliverable. Use the verified destination selected for the task. If none is selected, follow the applicable verified recipient or course placement policy. If neither resolves the destination, use the verified course owner location for course working material. Use Resources for reusable reference material. Resolve an unclear destination before writing.

Ask only when the scope or a required destination for an authorized save remains unresolved.

## Steps

1. **Read the plan.** Read the existing study-continuity section under its actual verified heading in the course note. Use its topics, passes, gaps and source pointers and read the relevant authorized source pages. Keep the course note read-only.
2. **Build items** from the topics' learning outcomes. Mix recall, calculation, interpretation, and choosing the right method. Include the recorded gaps and common misconceptions. Use visual interpretation and worked-example contexts wherever they test a relevant skill: reading axes, comparing conditions, following a sequence, identifying assumptions, or predicting a parameter change. Read `../study-enricher/references/teaching_visuals.md`, including its assessment adaptation, when making visuals or examples. Keep the authorized course sources primary. Resolve enrichment from the current task's selected setting or explicit depth request, then the applicable verified standing setting. Use deep only as the fallback when neither applies and the source scope permits outside material. When course sources run thin, ask Study Enricher for a bounded set of outside problems only if that setting and scope allow unsolicited enrichment. Off suppresses unsolicited outside problems. Handle an explicit request for outside problems within its stated scope and pass the effective setting, the specific request when present and the relevant course conventions. A one-off request does not change the standing setting.
3. **Write answers** with worked solutions. Recompute every numeric answer and cite the source page for each item; label items taken from outside material and invented quantities as worked examples tied to the sourced concept. Keep necessary labels and context in the question, but place answer-revealing highlights, reading guidance, completed derivations, and explanatory figures in the solution. A supplied posterior value may be legitimate question data; the caption should not announce the answer being tested.
4. **Format.** Use the form selected for the task first, then the applicable verified recipient or course format policy. If both leave the form open, choose a compatible fallback that serves the intended use within the authorized output scope. Markdown and Anki can be delivered separately or together when the selected form or compatible fallback calls for them.
   - When a Markdown deck is selected, use one card per block, question then answer, formulas in `$$ ... $$` display blocks.
   - When an Anki file is selected, use plain text starting with the header lines `#separator:tab` and `#html:true`, then one card per line as `front<TAB>back`. Formulas use Anki's MathJax delimiters, `\(` `\)` inline and `\[` `\]` for display, and line breaks inside a field are `<br>`.
   - For visuals in a selected Anki deck, use HTML tables, MathJax, or checked static images, not Mermaid fences or executable HTML. Reference each image as `<img src="exact_filename.png">` using a verified basename. For an authorized Anki save that includes image files, save the needed images with the deliverable under the destination rule. Reuse them in Markdown with verified relative links when that file is included. Tell the user to copy the images into Anki's `collection.media` before importing with HTML enabled. Give the exact image filenames; no subfolders inside `collection.media`. Escape quotes in quoted import fields and keep exactly two parsed tab-separated fields. If image export is unavailable, use an equivalent table or text/LaTeX representation and state the limitation.
   - Quiz: questions first, then the answer key after a separator.
   - Practice exam: instructions and time budget, the questions, then solutions and a scoring guide.
5. **Return or save.** Use the selected form. For authorized files, use the verified destination and selected filename or applicable naming policy. If the filename is open, use a snake_case name built from course, scope and kind, such as `course_101_unit_3_flashcards.md` or `course_101_unit_3_flashcards_anki.txt`. Use a new name for a new file and update an existing file only when requested. Return the verified paths. Pass a course-note link request to Study Planner through the caller only when the authorized scope includes that edit.

## Outputs

- Return the practice material in the selected form or the verified paths of the authorized saved files.
- Report coverage and item counts in the current task's requested form or under the recipient's existing reporting policy. For a delivered Anki file, give its import instructions (Anki's File > Import).
- Include any required static images in the authorized file scope with verified links and exact Anki media-copy instructions when applicable. Keep them with the deliverable.
- No progress records and no Recall Queue changes.

## Boundaries

- Never record progress, mark coverage, or change the Recall Queue; Study Planner's queue stays the only review schedule. Pass reported results through the calling skill to Study Planner only for an authorized continuity update.
- Every item traces to a source page or is labeled as outside material.
- Study Planner owns authorized course-note link edits. A quiz file save or a returned path grants no note-edit authority.

## Handoffs

- Requests may arrive through Study Companion or Study Planner; preserve the caller's context and return point.

- When outside problems are requested or allowed under the enrichment and source rules above, use [study-enricher](../study-enricher/SKILL.md).
- Route authorized course-note links and result recording, and any applicable review scheduling, to [study-planner](../study-planner/SKILL.md).

## Checks

- The answer key matches the questions, and the counts match the request.
- Every numeric answer was recomputed.
- Question figures do not reveal the answer through captions, highlights, filenames, or explanatory alternative text; solutions explain the relevant visual and agree with the question's values and notation.
- When an Anki file is delivered, verify its two header lines and exactly two tab-separated fields on every card line.
- Verify that image references resolve to delivered files. For Anki images, verify that the fields and copy instructions use the same basenames. Check that tables and MathJax match the target format. Inspect visuals for readability and disclose unavailable Anki rendering checks when an Anki file is delivered.
- Verify that delivered files open and render. Check LaTeX in Markdown and MathJax delimiters in Anki when those formats are delivered.

## References

- Anki. (n.d.). *Text files*. Anki Manual. https://docs.ankiweb.net/manual/importing/text-files
