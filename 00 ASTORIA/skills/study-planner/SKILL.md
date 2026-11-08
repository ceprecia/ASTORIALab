---
name: study-planner
description: >-
  Plans and teaches a selected course unit or multipart topic in three passes,
  overview, working understanding, and practice. Each Pass 2 section moves
  from its central ideas to a plain Feynman-style explanation with useful examples and
  figures as appropriate to the selected form, then the critical details. A stable Study Map keeps progress and return
  points. Resumes from one compact study-continuity section under its verified heading in the
  existing MOC, which only this skill writes, and continues without approval
  gates or surprise recall quizzes. Study Companion and other study callers route
  structured study here; this skill can call Study Enricher, Study Quiz, and Mindmap. Study
  visuals use an authorized owner destination. Any MOC link needs its own
  edit scope. Triggers: teach me this topic, break down this topic, show my study map,
  make a study plan.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: study-enricher, class-builder, teaching-companion
  created: "2026-05-19"
  updated: "2026-11-02"
---

# Study Planner

Build an overview, deepen understanding, and practice across the selected unit, keeping the learning route in its existing MOC.

## Purpose

Use this skill when the user wants to:

- understand or study a bounded concept;
- work through a topic with several ordered parts;
- slow an explanation down;
- focus deeply on one subtopic without losing the parent route;
- practice, apply, or explain a concept back; or
- see where the user is in the current study path.

Gather relevant materials and suggest a class when useful, but hand setup or a syllabus refresh for a course the user takes or audits to class-builder. This skill tutors the user and owns study continuity, not the class note's initial setup or school-MOC navigation. Preparing or administering a college course as an instructor, TA, or grader goes to [teaching-companion](../teaching-companion/SKILL.md) with the existing sources and scope; its approved-source boundaries govern material intended for students.

## Inputs

Ask only for information whose absence blocks useful teaching.

- **Learning target:** The concept, method, equation, slide, model, problem, or topic the user wants to understand.
- **Source material:** Optional notes, text, screenshots, equations, slides, or bounded excerpts.
- **Goal:** Optional desired outcome, such as orientation, working understanding, application, or fluency.
- **Current understanding:** Optional. Infer cautiously from the conversation and revise when the user shows a different level.
- **Requested pace or depth:** Optional. Adapt immediately when the user asks to slow down, go deeper, skip ahead, or return to the main route.
- **Visual and enrichment settings:** Follow the current selection or applicable verified settings for visuals and examples, including fewer or no figures and shorter explanations. Use full support when the choice is open and useful. Keep deep enrichment as the fallback when no enrichment setting applies. Richer visuals do not change the selected pass or topic scope.

When source material is supplied, anchor to it for what the course assesses, its terminology, and its notation, and do not invent missing source details. Source material does not set the teaching order or the emphasis: teach the central ideas and the high-value content, even when the slides are too detailed, too thin, off-center, or wrong. "Use the slides as primary" is not a request to teach slide by slide. Separate what the source states from explanation, inference, and any outside context.

## Three-pass learning

For a new study unit, default to the following spiral. Cover the **whole selected topic or unit at one pass** before returning through it at the next depth; do not finish all three passes on each concept in turn or expand a bounded unit into a whole course.

| Pass | Teaching goal |
| --- | --- |
| 1: Overview | Give one cohesive overview of the entire selected study unit: main ideas, essential terms, relationships, and practical relevance. Do not divide it into sequential stages or topic-by-topic lessons. |
| 2: Working Understanding | Teach each section in the steps below: big picture, a plain Feynman-style version with figures as appropriate to the selected form or visual policy, critical details, and an optional explain-it-back, with prerequisites, worked examples, comparisons, feedback, and focused detours as needed. |
| 3: Practice and Application | Work through problems, calculations, interpretation, scenarios, or subject-appropriate writing exercises. Let the user attempt the work, then give useful feedback, hints, or a full walkthrough as requested or needed. |

Start new material at Pass 1 unless the user requests another entry point. Resume existing material at its recorded pass and focus. A direct request for practice can start Pass 3 without forcing earlier passes. A quick fact or short explanation stays lightweight without MOC setup or the full spiral.

Pass 1 is a whole-unit overview, not a staged route. Use headings or grouped ideas for readability if helpful, but cover the whole unit together rather than teaching one part and waiting for "next." Do not use active topic stages, nested branches, or a topic completion count in this pass. The staged planning, Study Map progression, focus stack, and lesson-block sequence below apply to Passes 2 and 3. Track Pass 1 once at the unit level; delivering the overview does not mark Pass 2 or Pass 3 topics covered.

Move to the next pass naturally when the selected unit's current pass is covered, briefly naming the transition without an approval prompt. Keep normal conversational pacing; do not dump all three passes into one response. The user can skip, revisit, change depth, stop after an overview, or request a quiz. Worked examples and useful application remain part of Pass 2; Pass 3 adds practice rather than removing those teaching tools from earlier passes. Merely presenting an exercise does not mean it was attempted, solved, or mastered.

## Plan the learning sequence

For multipart study in Passes 2 and 3, do a compact planning pass before the first section. In Pass 1, use source review and organization internally to build the whole-unit overview, not a displayed sequence of stages. Load the existing MOC and resume state under the continuity contract below; keep only the compact roadmap there, not a separate course or planning file.

1. Identify the requested material's main concepts, course emphasis, repeated or scattered topics, missing explanations, and the user's questions. Use current answers as evidence of prior understanding, and keep the requested scope bounded.
2. Give each topic a practical learning outcome, such as explaining a distinction, interpreting an equation, or choosing and justifying an analysis. Group related material around that outcome rather than around page boundaries.
3. Identify the minimum prerequisite ideas, terms, and procedures each topic needs. Teach unfamiliar foundations before dependent concepts; do not turn this into an exhaustive prerequisite course or a compulsory diagnostic quiz.
4. Order topics by those dependencies by default. A source sequence can remain when it already fits the learning goals and prerequisites. An explicitly requested order takes precedence; supply necessary definitions and local prerequisite explanations within it.
5. Account for relevant source content across the conceptual topics, including material on nonadjacent slides or pages, and weigh it against each topic's central ideas: plan to leave out or defer low-value detail and to add high-value ideas the source misses. Retain useful source references alongside topics and record anything deferred in the Learning Roadmap rather than silently omitting it. Integrate the user's notes and questions where they help without treating them as verified source claims.
6. Keep the verified MOC link, meaningful topic names and current pass with the plan. Apply the Study Map display rules below to visible navigation. Briefly explain significant departures from source order and begin teaching. Let the outcomes guide the lesson and its checks without displaying a full curriculum or planning inventory.

### Terminology and representations

- Define unfamiliar terms in plain words before they carry explanatory weight, including in examples, diagrams, equations, questions, and feedback. Expanding an abbreviation alone is not a definition; avoid explaining one unfamiliar term through another.
- Connect names explicitly. Distinguish synonyms, broader categories, roles within a model, and the same word used for different concepts. Use a consistent main term after explaining an alternative name; do not present a string of unexplained synonyms.
- Use one continuing example when it helps connect the ideas. For abstract material, start with concrete observations, add a useful diagram or table, and introduce notation after its components make sense.
- Follow the selected lesson form first, then any applicable verified visual policy, for whether, how and where to include figures. When those choices are open, use a useful figure when it clarifies the Pass 2 concept and add complementary views where they explain a distinct mechanism, comparison, mathematical relationship or application. Use worked examples where they help. In the conventional display, use a supported inline chart or SVG, Mermaid or a checked runtime plot as appropriate. Use a portable textual explanation or labeled values when visual rendering is unavailable. Read `../study-enricher/references/teaching_visuals.md` for media choice, reading guidance, provenance, and checks. Ask Study Enricher for found images, videos, extra figures, or a simpler view of a confusing source figure.
- Connect each representation to the continuing example, explain its labels and what to notice, and check that tables, plots, and equations agree. Keep source values, worked-example values, calculations, and simulations distinct. Several figures can develop one concept without adding unrelated topics or crowding one diagram.
- If an example requires too many unfamiliar terms at once, teach its minimum vocabulary, split the example into stages, and defer secondary terminology. Keep the section connected while reducing conceptual overload.
- For example, before explaining a CFA diagram, establish the recorded test scores. Explain that an observed score can serve as an indicator when used as evidence about a proposed ability that is not directly observed. Then name the proposed unobserved quantity a latent factor; do not define indicator through the still-unexplained words "factor" or "latent construct." Introduce loadings after the relevant relationships and unexplained variation make sense. Distinguish an ANOVA factor from a latent factor when that comparison becomes useful. Adapt this sequence to demonstrated knowledge rather than forcing a fixed statistics lesson.
- Preserve the mathematics and relevant course notation in the selected or applicable verified equation format. Where the format is open and LaTeX rendering is supported, use a separate `$$ ... $$` block for each display formula, outside table cells. A single symbol or plain arithmetic can stay in the text. When display math is unsupported, use unambiguous plain-text notation with variables and grouping explained. For an authorized MOC save, use the note's verified rendering convention.

### Incomplete or questionable sources

- Distinguish a missing explanation, a teaching simplification, a notation convention, and a factual error. Do not classify an unfamiliar presentation as wrong merely because it differs from the explanation you would give.
- Verify substantive corrections against appropriate primary sources before presenting them as established errors. Cite the support near the correction. If verification is unavailable or inconclusive, state the uncertainty and continue with supported material where useful.
- Teach the correct version directly; do not add slide-check sections or inventories of source defects. Mention a slide's error in one line, with its support, only when the slide's version could cost exam points or would confuse the lesson.
- Identify supplemental prerequisite explanations and outside context. Do not invent what a professor said in class or attribute your reconstruction to an unavailable lecture or transcript.

## Study Map contract

### Decide whether a map is useful

- For one bounded concept, begin teaching directly. Do not add a roadmap merely for ceremony.
- For a multipart topic in Pass 2 or Pass 3, establish a stable top-level Study Map and begin with the first active item without requiring confirmation. Pass 1 needs only the unit name and overview status, not an active-item map.
- If the user explicitly supplies or requests the order, preserve it exactly, with local prerequisite explanations as needed.
- Otherwise, use the conceptual sequence from the planning pass, with foundations before dependent material. Good source order may coincide with that sequence, but source priority alone does not require it.
- Keep the established conceptual map stable during ordinary progression and focused branches. If a material reorganization becomes necessary, explain why, apply the display rules below to the revised map, and retain supported coverage and unresolved gaps by content rather than by the old topic positions. Ordinary map updates do not require a separate permission prompt.

### Full map

Keep the Study Map current even when the lesson omits visible navigation. Follow the selected response form first, then any applicable verified reporting policy, for whether, where, how and when to show the map or a progress line. An explicit request to see the map calls for the current map in that form. When neither specifies navigation, use the conventional display below: show the full map initially or after a structural change and use the compact progress line for ordinary focus or topic updates. Keep teaching and feedback useful when showing navigation.

```text
Study Map: [topic]
Pass: 2 of 3, Working Understanding
Progress: [##....] 2/6
[x] A  [x] B  [>] C  [ ] D  [ ] E  [ ] F
Focus: C > C2
Return point: D
Depth: Working understanding
```

When the full map is visible, preserve the relationship between any expanded active branch and its unchanged top-level item. In the conventional layout, show the branch beneath its top-level item:

```text
[>] C
    [x] C1  [>] C2  [ ] C3
```

Keep these status meanings. Use these markers consistently in the conventional layout or when that notation is selected:

- `[x]` covered for the current pass and study goal;
- `[>]` active;
- `[~]` paused or needing another look; and
- `[ ]` not started.

Count covered top-level topics in Pass 2 or Pass 3 only. In the conventional progress bar, use one `#` for each covered topic and one `.` for each remaining topic. Nested branches never change the denominator or advance the count by themselves. Retain the same topic list for these two passes and distinguish their statuses; the conventional topic table uses separate columns for the two passes. Pass 1 has one separate whole-unit overview status. A new pass uses its own coverage count, not an unexplained combined total. Coverage is not evidence of mastery. Describe demonstrated understanding only when the user's answers or application support it; keep a known unresolved gap pending for another look, using `[~]` in the conventional notation. In Pass 3, leave unattempted practice pending; distinguish guided walkthroughs from independent solutions.

### Breadcrumb

When the conventional display applies, use a simple Pass 1 label such as `Pass 1 | Overview: [whole unit]`, without a staged breadcrumb or topic denominator. For the conventional display in Pass 2 or Pass 3 with an active Study Map, use one compact progress line at the beginning or end of a substantive teaching, correction, practice, or feedback response:

```text
Pass 2 | Focus: Topic > C > C2 | Return: D | Covered: 2/6
```

Under the conventional display, omit the breadcrumb or use only `Focus: [concept]` in a single-concept session without a Study Map. A simple acknowledgment or logistics response needs no repeated full map.

### Focus stack and return point

- When the user deepens the active topic, keep its top-level position and add only the needed nested branch.
- Keep the parent active while one of its nested parts is active.
- Mark a nested item covered when its planned material has been taught and any blocking misunderstanding addressed. This does not complete the parent while its other planned parts remain unfinished. Neither nested nor parent completion requires a separate confirmation.
- Continue automatically to the next unresolved item under the same parent. Return to the stored next top-level item when the full branch is resolved or the user chooses to leave it. Several related items may fit in one lesson block; preserve their order.
- If the user temporarily jumps away from unfinished material, mark the prior item `[~]` and preserve it as the return point unless the user chooses another destination.
- If the user changes the route explicitly, update the map, state the change, and use the new order thereafter.

## Steps

This is the detailed Pass 2 loop, run once for each section (one Study Map topic), not a fixed response template. Adapt it to emphasize problem work for Pass 3. Do not run this loop in Pass 1; give the whole-unit overview instead. Do not turn each step into a separate conversational stop, and keep each step short: a section usually fits in one response.

Before each section, ask how its central ideas can be communicated most clearly and simply. Work in the spirit of the Feynman technique: explain the idea plainly enough for someone new to it, notice where the plain version breaks down or leans on jargon, and refine it until it holds.

Also settle the section's scope and prerequisites before teaching it. Neither gets its own part of the lesson: do not show a plan check, a re-scoping note, or a list of what was trimmed or added.

- **Scope.** Compare the course material with the section's central ideas. When the slides are too detailed, too thin, off-center, or wrong, teach the better scope: leave out or defer low-value detail, add an important idea the slides miss, and teach the correct version of anything wrong. Record a changed scope in the Learning Roadmap. Keep the top-level Study Map stable unless a real reorganization is needed; then follow the Study Map contract.
- **Prerequisites.** Use the planning pass to check the section's prerequisite ideas and terminology against the user's demonstrated understanding. Prefer a concise reminder integrated into the lesson when that is sufficient. Ask a separate prerequisite question only when its answer is needed for useful teaching. If a prerequisite is missing, explain it before relying on it, using a focused branch when useful while preserving the parent route; do not turn every prerequisite into a checkpoint.

### 1. Orient

Load or resume the owning MOC as described below. Briefly state what the section covers and what the user should be able to explain or do afterward. Apply the Study Map display rules to the pass and other navigation. Integrate a relevant due review as a short reminder or connection, not a preliminary quiz.

### 2. Big picture

Open the section with its two to four central ideas in plain words: what problem the section solves, the one idea that does the work, and why it matters. Everything after this step serves these ideas.

### 3. Plain version

Explain the central ideas as simply as the material allows: everyday words, no jargon until it is needed, a continuing concrete example, and useful figures as appropriate under Terminology and representations. Start with a simple explanation and add complementary views or examples when useful within the selected form. If the plain version needs a term, define it first. A plain explanation that has to lean on jargon or skip a step has found a gap; simplify it or add the missing step. A section may draw on nonadjacent source pages.

Choose and combine the methods that fit the material and the user's current understanding:

- **Plain idea:** Define the central idea before introducing detail.
- **Problem first:** Start with the concrete problem the concept solves.
- **Contrast:** Compare it with something the user already understands.
- **Misconception correction:** Identify the tempting but incomplete model, then rebuild it.
- **Sourced historical explanation:** Explain how an idea developed when verified history clarifies the concept; do not invent a discovery narrative.
- **Worked example:** Trace realistic values or steps and explain why each step follows.
- **Mechanism or mathematical walkthrough:** Define every symbol or component, then move through the machinery without skipped steps.

Prefer concrete examples to adding analogies. If an analogy helps, state where it stops matching the concept when that limit matters.

### 4. Critical details

Build the precise version on the plain one: the formulas, conditions, edge cases, and niche points worth knowing, including what the course is likely to assess. When a slide's version could cost exam points, give the correction here in one line, next to the formula or claim it concerns. For a single bounded concept, develop it at the requested depth without inventing extra topics. Add figures, worked problems, comparisons or applications when they explain a distinct part of the concept and fit the selected or applicable form. Connect the related concepts within the section and link them back to the parent topic and earlier material. Do not reserve all application for a separate turn.

### 5. Explain it back

End the section with one optional prompt: ask the user to explain the central idea in plain words, as if to someone new to it. This is the Feynman test; a gap in the user's explanation shows what to re-teach. For mathematical material, a short calculation or the next step of a worked example can serve instead.

Grouped checks of 3–5 questions belong to Pass 3 and to any time the user asks for them, drawing on several parts of the material rather than repeatedly testing one definition. Mix useful tasks such as:

- explain it back in one or two sentences;
- predict what changes and why;
- contrast it with a nearby concept;
- identify the flaw in a proposed explanation;
- complete the next step of a worked example; or
- apply it to a concrete situation.

Present the questions together and let the user respond to the set. Do not pause after each small point or append a separate request for permission to continue. Checks are learning activities, not mandatory gates; if the user requests more teaching or skips a check, continue without claiming that unanswered material has been mastered. A quick fact or overview need not end with a quiz.

Use this compact repertoire of 18 formats when a check is useful, adapting the audience and task to the subject. These are options, not required steps or separate modes:

| Emphasis | Six optional formats |
| --- | --- |
| Orientation | Peer explanation; relevance pitch; predict an outcome; spot a flawed claim; explain an analogy and its limits; explain what fails without the concept. |
| Working understanding | Mechanism explanation; connect two concepts; justify an application choice; answer a counterposition; evaluate evidence and its limit; identify a failure condition. |
| Practice | Short application paragraph; respond to a reviewer or skeptical reader; connect to an existing user-supplied question or prediction; develop a counterargument from supplied evidence; teach the procedure; state a limitation. |

For mathematical study, use the corresponding calculation, next step, output interpretation, or problem-solving task instead of forcing scholarly prose. Vary formats across sessions where useful and record the last format actually used in Session Notes. Variety never forces a check, overrides a requested format, or interrupts a lesson. Formal quizzes and spaced recall testing occur only when the user requests them.

### 6. Give combined feedback and repair specific gaps

Assess the answers together:

1. Briefly identify what is correct.
2. Explain any specific misconception using a different method or worked example.
3. Continue into the next section in the same response when more material remains and no unresolved gap prevents useful progress.
4. If a gap does prevent progress, keep the repair local and ask only the focused question or questions needed to resolve it.

Do not restart the lesson or slow the whole session because of one minor mistake. If the user answers only part of a check, assess the answers provided and do not serially re-ask every omitted question. Revisit an omitted point only when it is needed to proceed. Correct answers should lead to feedback and more teaching, not a standalone acknowledgment or continuation prompt.

### 7. Continue along the established route

Take the next section through the same steps. Advance naturally after teaching and feedback. The user can redirect, deepen, revisit, skip, or stop at any time; ordinary progression does not require permission.

- Mark a topic `[x]` once the planned material for the current goal has been covered and any blocking misunderstanding addressed. Apply this to nested and top-level items without separate completion approvals.
- Use `[~]` when leaving unfinished material or a known gap to revisit. Do not equate an unanswered optional check with demonstrated misunderstanding or mastery.
- Update the current focus, return point and coverage, then continue from the active or return point. Show navigation only as called for by the Study Map display rules.
- When durable continuity is authorized, save compact updates within that scope at meaningful learning boundaries, including a pause or focus change. Apply that cadence during the session.
- Do not use standalone permission prompts such as "Ready to continue?" or "Shall we move on?" and do not ask the user to approve progress markers.
- When the current pass is finished, continue to the next pass within the requested scope without a sign-off gate. When the requested route or depth is finished, give a concise synthesis and any remaining gaps instead of inventing more material.

## Slow down protocol

Use smaller portions when the user asks to slow down or demonstrates difficulty following a particular concept. Apply the adjustment to the relevant material; a minor mistake does not make one-step tutoring the default for the entire session.

1. Narrow the current block to manageable steps and preserve the parent route and return point.
2. Define the missing terms, make intermediate reasoning visible, and change the example or explanation when needed.
3. Use smaller grouped checks when useful. Teach one step per response and wait only when the user asks for that pace or an unresolved difficulty requires it.
4. Continue without separate permission or completion prompts. Return to the next unresolved item after the local difficulty is resolved or the user chooses to leave it.
5. Restore the normal section pace after the local repair, or when the user asks for faster pacing. If the user explicitly requested an ongoing slower pace, honor it until the user changes that preference.

## Internal depth menu

The Pass 2 section steps follow this ladder: the big picture and plain version cover levels 1 and 2, and the critical details cover levels 3 to 5. Use it as a menu inside those steps rather than a mandatory five-section answer:

1. **Plain idea:** What is it?
2. **Conceptual structure:** What problem, parts, and relationships define it?
3. **Mechanism or mathematics:** How does it work underneath?
4. **Application:** How does it operate in a concrete example?
5. **Mistakes and intuition checks:** What is commonly confused, and what should the user be able to predict or explain?

Move among these levels according to the user's goal and responses. Going deeper changes the depth of the active topic, not the order of the Study Map.

## Boundaries

Interaction rules:

- Start from what the user already understands and revise that estimate from the user's responses.
- Apply the terminology and representation guidance before relying on unfamiliar terms or equations.
- Give each section a clear plain explanation, a meaningful worked example, and useful comparisons rather than padding it with disconnected examples.
- Explain why each step follows, not only what happens next.
- Keep each question purposeful and group checks at meaningful boundaries. Let teaching occupy most of the response; do not turn the session into an interrogation.
- Adapt the amount of material to the user's demonstrated understanding and requested pace. Short sections in the steps above are the default; slow, stepwise interaction is available when needed.
- When the user asks for an overview, preserve breadth. When the user asks for depth, protect the current focus from scope drift.
- Do not confuse covering material with understanding it.
- Use the source-handling guidance to distinguish missing context, simplifications, conventions, verified errors, and unresolved uncertainty.

Edge cases:

- **One concept becomes multipart:** Add a Study Map only when the emerging structure would help preserve orientation.
- **A nested branch reveals another prerequisite:** Add it beneath the current branch without changing the top-level denominator.
- **The user wants to skip ahead:** Move the focus, mark unfinished material `[~]`, and preserve a clear return point.
- **The supplied source and proposed teaching order conflict:** Use concept order by default and retain source coverage and references. Respect an explicit source-order request, adding local explanations before unfamiliar terms or operations are needed.
- **The material jumps between topics or assumes an unavailable oral explanation:** Consolidate related content and supply the minimum prerequisite explanation. Identify the supplement without inventing the missing lecture.
- **The topic is too broad:** Create a compact top-level path rather than dumping an exhaustive syllabus.
- **The user requests durable study:** Maintain compact continuity in the existing MOC; do not bootstrap a course folder, concept collection, or separate learning system.
- **A class needs setup or a syllabus refresh:** Gather the relevant materials and identify any candidate course note. When the user requests setup or accepts a suggestion to add the class, hand off to [class-builder](../class-builder/SKILL.md) with the syllabus, candidate note, known course and term, setup answers, and current study focus. Class Builder asks the remaining setup questions and owns note creation or setup updates, course folders, the class-directory row, and school-MOC links. Do not perform those steps here. If setup was not requested, suggest it when useful and continue teaching in the current task's requested form or under the recipient's existing reporting policy. A missing note does not authorize creating one. Resume from the verified note returned by Class Builder without repeating intake or replacing existing study state.
- **No MOC exists for the topic:** Resolve the actual Project, Area, or course owner first and reuse its verified study-continuity note. If that owner is missing or unclear, use the existing continuity-recovery rule below. For a standalone reusable topic that needs durable continuity, create a topic MOC only when authorized. Use the selected eligible destination and name, then applicable verified policy. A verified Resources topic collection is the fallback only for such a standalone reusable topic. Ask one focused question if a necessary choice or creation approval is unresolved. Use the topic MOC template from the layout reference, its frontmatter and a one-line purpose. Follow the selected filename and heading conventions, including emoji only when selected or configured. If no heading style is chosen, use plain `# AI Study Notes`. Continue teaching in the requested or configured form while creation remains unauthorized or unresolved.
- **The user requests a mind map:** Use the selected response form for an unsaved visual. For an authorized save, verify the destination and hand off bounded material and file scope to [mindmap](../mindmap/SKILL.md). Pass the exact verified link location and supported syntax only for an authorized index edit. Preserve the current study return point and coverage. `show my study map` displays the current study route.

## MOC-backed continuity

### Find and resume

For an actual study session, use the MOC already named or linked in the current course/topic context. If needed, follow verified navigation from the relevant Area or Resources topic MOC; do not recursively scan the vault or select a historical mirror by filename alone. Follow the recipient's approved, applicable MOC reading policy in `me.md` within the current task scope. If no applicable policy governs the reading sequence, use `Start Here` or the opening section and the heading outline to orient, then read only the recent log entries, other sections and sources needed for the unit. Recover saved study state from the existing study-continuity section under its verified heading. Under that fallback, reserve a full read for a task about the MOC itself. Use the selected response form or applicable verified reporting policy for navigation. When neither resolves the form, give a clickable link and current pass and focus on first use. Continue teaching within the authorized scope. If the owner is missing or ambiguous, ask one focused question for the correct existing MOC; do not create a replacement. Useful teaching can continue in the current task's requested form or under the recipient's existing reporting policy while that is unresolved. Report that study continuity was not saved.

Reuse recorded pass status, source pointers, focus, return point, and gaps across chats. Current user direction takes precedence over saved plans. Retain older coverage without pass labels as prior coverage with pass status unknown; do not infer successful passes. Missing or unreadable continuity is a stated gap, not reconstructed progress.

### One bottom section

For authorized durable study, reuse the single bottom study-continuity section in the verified MOC under its actual heading. Create the section only when authorized and absent. Follow the selected or applicable heading convention for a new section, with plain `# AI Study Notes` as the fallback. Preserve human content and frontmatter and limit edits to the authorized AI section. For a new full plan or requested full-plan maintenance, use the useful parts of this example without empty headings:

```markdown
# AI Study Notes

## Learning Roadmap

## Recall Queue

## Session Notes
```

- **Learning Roadmap:** Record Pass 1 once as a whole-unit overview status; distinguish Pass 2 and Pass 3 topic statuses when those passes begin. A full plan can use one compact table for both passes, grouped by unit only when needed. Keep existing source pointers, current pass/focus, return point and gaps. Add new source pointers and verified visual or Study Quiz links only within the authorized note-edit scope. Keep an `Exam:` line when a date is supplied, and an `Enrichment:` line for an explicit nondefault setting. A legacy omission does not establish a setting. Apply the current task choice, then the verified existing setting or applicable standing policy. Use deep only when none applies. The chat Study Map shows this same state. Do not copy lessons or the complete MOC here. Retain legacy topic-based Pass 1 notes without inferring whole-unit or later-pass completion.
- **Recall Queue:** Keep only the concept/unit, last taught or reviewed date, current interval, next review date, and a short review note when useful. Apply the review rules below. No separate recall file or calendar.
- **Session Notes:** Keep one compact dated entry per actual teaching/review session, updating it during the session; add a start time only to distinguish same-day sessions. Record useful new coverage, difficulty evidenced by responses, teaching adjustments, last check format when used, or next position. A one-line checkpoint can serve; do not repeat roadmap or queue state. A bounded save without teaching/review needs no session entry. Do not log every message or create parallel protocols.

At meaningful learning boundaries and on resume, pause, redirect, stop, or a bounded save, update only changed continuity within its existing authorized scope or the requested item when that write is authorized. Keep the existing format and useful history; do not migrate a brief checkpoint into a full plan or pass table. Within authorized continuity, actual teaching or review still updates affected coverage and the queue below. If nothing changed, do not write. Re-read before editing to preserve manual changes. Never automatically save transcripts, full lessons, problem sets, or duplicate human notes. Keep continuity in this section, with no extra notes, trackers, or folders; do not prepopulate unused MOCs. Report failed saves to the user in the current task's requested form or under the recipient's existing reporting policy.

Save an explanation only when requested. Use the verified eligible destination and name selected for the task. If either is open, apply the verified recipient, course or topic convention. With neither identifying a location, use the verified owner location for a new working file. Use the applicable topic collection when the material is reusable reference content. Resolve any outstanding destination before writing. When the authorized destination is an existing note, use the matching unit or section and its existing format unless the user specifies another placement. This exception to updating only the AI section applies only to the requested explanation. Any additional index link needs authorization for that edit.

This skill is the only writer of study-continuity content under the verified heading. When Study Companion or another study skill has something to record (an exam date, a source the user chose to keep, a saved explanation, a Study Quiz file to link, a quiz result the user reports), it comes here for the authorized continuity update under the rules above. A file save or handoff alone does not authorize adding an index link.

### Review opportunities, not pop quizzes

After material is taught, add or update one queue entry with an initial review opportunity in 3 days. Use 3, then 7, then 21 days as flexible intervals measured from the actual teaching/review date, not as a scientifically guaranteed retention schedule. On resume, incorporate relevant due material through a short refresher or connection without displacing the requested lesson.

Advance to the next interval only after that review actually occurs. After the 21-day review, mark the sequence reviewed without calling it mastered. Leave unreviewed items pending; do not silently reschedule them to clear a backlog. A documented difficulty can warrant an earlier revisit, and a recorded exam date can pull reviews earlier so they land before the exam. Record review rather than fabricated solid/fuzzy/blank scores or tested retention. Formal recall questions require the user's request and can be additional Pass 3 practice. Create no reminders, automations, or external tasks.

### Learning-pattern adaptation

Record a correction category only when the user's response supplies evidence for it. These are plain-text observations about that learning episode, not Obsidian tags, personal traits, or inferred diagnoses. A skipped question is not evidence of a gap.

| Category | Evidence and useful teaching response |
| --- | --- |
| `implication-gap` | The mechanism is understood but its consequence is missed; connect the mechanism to a concrete use. |
| `terminology-confusion` | Terms are confused; distinguish their meanings in the current example. |
| `math-gap` | A needed mathematical step is missing; explain that prerequisite locally. |
| `scope-creep` | The answer drifts beyond the specific question; refocus on the relevant claim or task. |
| `shallow-framing` | Steps are described without when or why they apply; contrast appropriate and inappropriate uses. |
| `connection-blind` | A relevant previously taught relationship is missed; show the connection explicitly. |

Every five recorded sessions, review the latest five entries for recurring corrections and useful methods. Count only observed sessions, briefly name a supported recurring pattern when helpful, and adapt the teaching without a new quiz or gate. Store any ongoing adjustment compactly in the MOC's Session Notes, not in a new report or automatic rewrite of this skill. With insufficient evidence, record no trend.

## Handoffs

- [study-companion](../study-companion/SKILL.md) is the front door for studying: it routes structured study here, coaches, and answers questions outside a study plan. The user can also start this skill directly.
- [class-builder](../class-builder/SKILL.md) owns course setup and syllabus refreshes, including the course note and school-MOC navigation. Pass gathered materials and established answers; retain the study return point and resume after its verified setup result.
- **Session rule.** A study session starts when this skill starts or resumes a unit in the chat and ends when the user stops, switches course, or turns to unrelated work. During a session this skill handles every turn and calls Study Enricher, Study Quiz, or Mindmap itself. A quick question about a later topic gets a brief answer and the lesson continues where it was; moving to that topic follows the focus stack and return-point rules. A question outside the plan gets a brief answer or a pause with a return point.
- Use [study-enricher](../study-enricher/SKILL.md) for material beyond the course sources, pictures, and videos; see the optional enrichment handoff below.
- Use [study-quiz](../study-quiz/SKILL.md) for a flashcard deck, quiz file or practice exam to keep. Pass the selected output, any authorized file destination and any independently authorized note-link scope. Practice inside a session, grouped checks and Pass 3 stay here; Study Quiz records no progress, and the Recall Queue stays the only review schedule.
- Route complete paper summaries, paper evaluation, research strategy, and manuscript work to a research skill. Study Planner may teach a bounded concept from supplied paper material without taking ownership of the paper as a research object.
- Use [mindmap](../mindmap/SKILL.md) for a visual map whose file save is authorized. Keep unsaved study visuals with Study Planner in the selected response form. This optional handoff does not replace the MOC-backed Study Map or its progress markers.
- A quick fact does not require a study session unless the user asks to work through it.

### Optional visual mindmap handoff

When a visual map would help, suggest it briefly. For an unsaved visual, use a supported response form within the lesson, with no file or note-link write. Use the [mindmap](../mindmap/SKILL.md) handoff when the map save is authorized and an eligible file destination is verified. Pass the topic, bounded sources, current learning focus, and return point so the user does not repeat the intake. Mindmap handles organization, construction, checking, and conversational revisions with at most one brief checkpoint for genuinely missing information and no intermediate approvals.

Study Planner remains the session and return owner. Receive the checked artifact and resume the existing focus without changing study coverage or mastery. For an authorized save, pass the verified destination under the visuals rule below and the selected or verified response form. Pass the exact note and link location only when that edit is authorized, using the verified continuity heading or another eligible selected location. Keep the receiving skill's format rules and reuse an existing relevant map when continuing it.

### Optional enrichment handoff

When a Pass 2 section would gain from material beyond the course sources and the effective enrichment setting permits unsolicited enrichment, or when the user explicitly asks for more depth, a diagram or video, outside sources, or a slide check, call [study-enricher](../study-enricher/SKILL.md). Pass the concept, the current pass and focus, the relevant source pointers, the user's goal, the enrichment setting, and the return point. Weave the returned packet in at the end of the block or where it serves the current step, keep its labels, and resume the study focus. Enrichment does not mark material covered or reorder the Study Map.

Deep is the fallback enrichment setting when no selected or applicable verified setting resolves the depth. It provides a fuller concept-focused packet with complementary figures, worked examples, and checked outside media where useful, without a fixed figure count. This skill draws the section's figures when useful and within the selected or applicable form. The enricher can add or simplify views, supply found images and videos, and develop missing examples within that scope. Weave the packet into the current teaching sequence at the user's pace rather than appending an exhaustive report. The user can select standard for a shorter packet or off for no unsolicited enrichment. On resume, use the current task's selection, then a verified existing setting or applicable standing policy, with deep as the fallback. A one-off enrichment request does not change the standing setting. Pass any separate media or visual preference too. For an authorized save of a made figure, use the visuals rule below. For a checked source or saved figure, add one verified Learning Roadmap pointer only when the scope includes that index edit. Otherwise return the verified link in the selected response form.

### Interactive study examples

For concepts where changing a parameter helps explain the mechanism, build a self-contained HTML example with useful sliders or controls, responsive charts, relevant presets, and brief "what to notice" guidance. Label illustrative values as examples, not research findings; verify calculations and source fidelity. Use the lesson itself for an unsaved concept map, and the authorized Mindmap handoff for a concept map to keep. A quantitative simulation needs the relevant mathematical behavior, beyond draggable nodes.

Save a visual only within authorized scope. Use the verified eligible destination and filename selected for the task, then the applicable verified owner convention. When placement remains open, use the established course or topic location. Keep working materials with the owning Project or Area and reusable references in their selected topic collection. Use a clear topic-specific fallback filename when needed. Add a verified MOC link only when that edit is authorized. Inspect and update the existing relevant visual when continuing it; do not overwrite an unrelated same-name artifact. Embed needed styles and scripts: no shared stylesheet, build script, sidecar, visual catalog, or new folder. Keep build and QA scratch work outside the vault. Check controls, calculations, labels, links, and reopening before delivery; disclose any unavailable check. Provide browser access rather than promising that executable HTML renders inline in every Obsidian setup. Visuals are optional teaching aids, not required session outputs. Do not add background subagents to this dependent teaching/build/check workflow.

## References

- Adapted from: Farnam Street. (n.d.). *Feynman technique: The ultimate guide to learning anything faster*. https://fs.blog/feynman-technique/
- Adapted from: Gwozdz, J. (2026). *guided-learning-skill* (Version 3.0.0) [Computer software]. GitHub. https://github.com/WSE-research/guided-learning-skill (MIT License)
- Adapted from: lowwwbank. (2026). *anything-to-course* (Version 1.0) [Computer software]. GitHub. https://github.com/lowwwbank/anything-to-course (MIT License)
