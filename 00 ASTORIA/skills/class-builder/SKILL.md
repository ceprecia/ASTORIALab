---
name: class-builder
description: >-
  Creates or updates one class in the vault from a supplied syllabus, with
  focused setup questions, a course note, filed materials, and linked course
  navigation. Use for course setup or a syllabus refresh; preserve populated
  notes for courses the user takes or audits and hand study progress to study-planner. Triggers: add
  this class, set up this course, organize this syllabus, update my course
  setup.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: teaching-assistant-builder
  created: "2026-10-15"
  updated: "2026-10-20"
---

# Class Builder

Turn a syllabus into a usable class note and course navigation, preserving what is already there.

## Purpose

Set up or refresh one class the user takes or audits. Identify the course, ask focused questions, create or update its note, and file supplied materials within the requested scope. Use the recipient’s verified course navigation. Edit its owning MOC or other navigation only when that specific change is authorized. Return a proposal in the current task's requested form or under the recipient's existing reporting policy. A proposal request does not authorize setup changes. Tutoring the user, study plans, practice, and study progress belong to study-planner. Before setup, route an instructor, TA, or grader offering to [teaching-assistant-builder](../teaching-assistant-builder/SKILL.md) with the supplied sources and settled answers. Do not create student-course records for teaching work.

## Inputs

- The syllabus or other supplied course material and the user's setup request.
- The current `me.md`, applicable school `AGENTS.md`, layout reference, school MOC, and Class Template. Resolve destinations and naming from those sources; do not maintain a second copy of their conventions here.
- Existing course notes, eligible navigation entries, and course files found through verified owner links or the bounded course folder.
- Answers already given in this conversation or passed by another skill, including the user's course number, role, term, and intended owner.

### Setup questions

Begin with a short setup conversation after inspecting the sources. Briefly name the course and proposed semester placement, then ask one small batch of up to three questions about unresolved choices that affect the setup. Reuse established answers; do not make the user repeat syllabus facts or approve every file operation.

| Choice | Ask when |
| --- | --- |
| Course number and role | A crosslisted syllabus does not establish which code the user takes, or taking, auditing, and teaching would lead to different owners. Do not infer registration from graduate-student status alone. |
| Offering term and placement | Supplied sources and existing course conventions leave the intended offering or its location unclear. Ask for program year only when needed by the applicable convention. |
| Existing owner and organization | More than one note could own the course, prior-term material needs a distinct home, or a meaningful grouping choice remains after checking the existing note and syllabus. |

Ask only the applicable questions, with concrete choices when useful. When all answers are already established, state the resulting setup and proceed. If a required answer is pending, continue independent source inspection and defer the dependent write. Keep course-specific answers in the course note's appropriate properties or sections, not in this skill or a separate setup record.

## Steps

1. **Find the owner and current conventions.** Read the applicable instructions and template. Inspect the verified applicable school navigation and candidate notes. Check course code, title, term and role together. Follow eligible links and bounded folder listings before creating anything. A missing navigation entry alone does not establish that the note is absent.
2. **Read the supplied source.** Extract the course identity, term, format, instructor and contact details, office hours, stated meeting times, required materials, assessments, grading, dates, and source grouping. Use tools appropriate to the file; inspect the rendered page when text extraction loses a table, symbol, or date. Keep exact date windows, stated times and timezones, and tentative labels. Leave missing credit units, deadline times, meeting details, or course-system links unspecified. Flag material contradictions instead of silently choosing a value.
3. **Resolve setup choices.** Use the Setup questions above. For a repeat offering, preserve prior-term notes and files and use the school's established term naming. Ask about representation only if those conventions cannot settle it. Do not apply a new term's syllabus over an old term's populated note merely because the course code matches.
4. **Classify the existing note.** Read the full candidate before editing it, including properties, user notes, logs and the existing study-continuity section under its verified heading. Use the preservation rules below. Resolve the exact note and folder destinations from the school instructions before writing. Keep course notes and materials together inside the verified course folder, normally under the School Area's `files/`.
5. **File supplied materials.** Create or reuse the verified class folder and copy incoming originals with their filenames unchanged, following the school's organization. A syllabus with no narrower group belongs at the class-folder root. Compare an existing same-name file: reuse an identical copy; preserve different content in a distinct folder consistent with the course organization, resolving a material version conflict with the user. Verify the saved copy against its source. Add groups only when actual materials need them.
6. **Create or update the course note.** Use the current Class Template for a new or empty note; make targeted updates to a populated one. Fill only supported properties and useful sections. Link the verified filed syllabus under the template's selected link convention, using portable Markdown as the fallback and embedding only when selected or configured. Add a concise chronological list of assessment dates or windows, and include brief grading or required-material information where useful. Link actual course files and supplied lectures using the course's own grouping. Use the selected note navigation and link form, then the applicable verified convention. Where neither resolves the form, use the template's portable Markdown list. Apply the local folder shortcut only when within the selected navigation and supported. Verify the actual file and heading targets and remove template placeholders and instructions. On a new note, if setup includes a study-continuity placeholder, keep it last under the selected heading or applicable verified convention, with plain `# AI Study Notes` as the fallback. Include a study-continuity navigation entry only when the section exists and the selected navigation calls for it. Use the actual heading and a verified target in the selected link form. Preserve the existing heading and study content on updates.
7. **Connect the class.** Follow the selected or verified recipient navigation. If the exact school MOC or other navigation edit is authorized, update its existing course entry or add a verified course link in the applicable selected place. Preserve existing information and unrelated entries. Verify link and heading targets after authorized changes. Leave optional directory, year, semester and shortcut conventions to the recipient’s selected structure.
8. **Verify and return.** Re-read the changed course note and any authorized navigation edits. Check the saved files, links, dates, duplicate prevention, and preservation below. Report what was created or updated, link the class note, and name any unresolved course facts. Return to the invoking study skill with the note path, source paths, settled setup answers, and its prior study focus.

### Preserve and update

| Existing state | Action |
| --- | --- |
| No note | Create one from the current Class Template at the verified destination. |
| Empty note or template-only placeholder | Populate or replace the empty scaffolding, retaining the intended note identity and valid links. A short title alone may be a placeholder; meaningful properties, annotations, files, or progress make it populated. |
| Populated note | Update it in place with the smallest supported changes. Retain user prose, additional properties, annotations, file links, logs, and study state. Do not rebuild it from the template or create a second hub. |
| Unclear whether content is meaningful | Treat the note as populated and make targeted edits. |

Before changing a populated note, identify the sections and fields the request affects. Preserve unrelated content exactly, and review every deletion or replacement in the resulting diff. Keep substantive information attached to a replaced placeholder or link. A later syllabus can update supported course facts for the same offering; conflicts with user annotations or newer approved course information require clarification rather than erasure.

## Outputs

- One created or updated course note, in the location and naming style defined by the school instructions.
- The class folder and supplied materials, with verified links or selected embeds and file navigation.
- Any authorized course links in the recipient’s selected or verified navigation.
- A concise completion report in the current task's requested form or under the recipient's existing reporting policy. Keep setup questions with the active conversation as needed; any separate saved report requires authorization. Do not create an extra index or tracking note.

## Boundaries

- Setup ownership stays here. Study Planner may gather materials and suggest a class, then hand off setup. Class Builder owns the class note, course folder and authorized school navigation edits.
- Preserve incoming originals and populated notes under the user's existing file rules. Do not silently overwrite a different same-name syllabus or replace populated content with a blank template.
- Apply a repeated request to the existing course and term. Reuse verified files, rows, links, and sections rather than appending duplicates.
- Keep source dates as supplied. A quiz window is a window; a date without a time does not become an invented midnight deadline. Do not infer degree credit or requirement completion from a course's title or level.
- Study-continuity content belongs to study-planner. Class Builder can initialize only the empty heading within course setup scope and preserves existing study content under its verified heading, including user-reported results and return points.
- Apply the authorization and external-action rules in `me.md` and the school instructions. Class setup alone does not request reminders, task-service changes, calendar events, or course-system writes.

## Handoffs

- Accept setup requests directly or from [study-companion](../study-companion/SKILL.md) and [study-planner](../study-planner/SKILL.md), with their source pointers and already answered questions.
- Return the verified course note and material paths to study-planner when an ongoing study request needs to resume. Do not create a study plan or imply that setup is learning progress.
- If the user only asked for class setup, finish after the verified setup report.

## Checks

- Course code, role, term, program year, and owner agree with the supplied sources and settled setup answers.
- Every added note link, embed, file link, Finder target, and heading anchor resolves; the course note exists before linking it from the school MOC.
- Assessment counts, grading weights, and dates match the source. Note source inconsistencies without silently correcting or normalizing them.
- A repeated import reuses the existing course note, verified syllabus copy and any matching navigation entries or sections.
- Populated-note changes preserve unrelated text and properties, existing files and links, logs, and all content in the existing study-continuity section.
- The course note's navigation matches its actual headings; file groups match actual folders under the school rules; no template placeholders or invented materials remain.
- School-MOC edits affect only the requested course and the navigation needed for it. Existing populated entries and other courses remain intact.
