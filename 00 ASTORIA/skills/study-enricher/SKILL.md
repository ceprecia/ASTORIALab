---
name: study-enricher
description: >-
  Takes one study concept beyond the course material: finds, checks, and
  packages deeper explanations, connections, applications, outside practice
  problems, checks of slide claims, and media such as figures it makes, images
  it finds, and checked YouTube videos. Uses selected or verified standing enrichment settings,
  with deep as the fallback. Returns one concept-focused
  labeled packet to the skill that called it, usually Study Planner during a
  lesson or Study Companion in open chat; it never writes notes and never runs a literature
  review. Triggers: go beyond the slides, what did the lecture leave out, find
  a video on this, show me a diagram of this.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: ""
  created: "2026-09-30"
  updated: "2026-10-10"
---

# Study Enricher

Go past the slides: the deeper why, the bigger picture, and the right picture or video.

## Purpose

What it can add, chosen for the concept, the user's goal, and the setting:

1. **Deeper mechanism.** Derivations, proof sketches, and the reasons the slides skip, from the model's own reasoning, labeled as such.
2. **Another explanation.** A different angle, an intuition, or an analogy with its limits stated.
3. **Connections.** Earlier units, the user's other courses, and where the idea leads next in the field and in current tools.
4. **The user's field.** Where the concept applies in the user's stated field and projects, with pointers to related research skills (for example pymc or drift-diffusion-model). For project context, read only the project MOC's Start Here.
5. **Misconceptions and exam traps.**
6. **Outside practice.** Textbook exercises with references (for a class, the textbooks in its `docs/` folder) and exam-style problems with worked solutions, for Study Planner's Pass 3 or Study Quiz.
7. **Slide checks, on request.** Confirm, correct, or mark a slide claim uncertain, with the source. Lessons do not carry slide-check sections.
8. **Media.**
   - Figures it makes: diagrams, charts, and plots, as Mermaid (Obsidian renders it), inline SVG or HTML where the app shows it, or a plot drawn with an available runtime.
   - Images it finds, linked to their source page rather than copied.
   - YouTube videos, checked for title and channel, with the part worth watching and why.
   - Existing interactive demos, with checked links. Building an interactive HTML example stays with Study Planner.

When the task has no selected setting and no applicable verified standing setting, use deep enrichment. In deep mode, develop the current concept with complementary figures, worked examples, derivations, comparisons, and checked sources where they help. Several visuals may be useful; do not limit the packet to one figure or one or two items. Broader reading or a short research plan belongs only when it serves the requested concept. Standard is a shorter option; off disables unsolicited enrichment. Depth expands understanding of the current point, not the scope into a literature review.

Not for: literature reviews, paper summaries, or paper evaluation (a research skill); concept maps (the current study owner, with Mindmap for authorized map saves); saving anything (Study Planner).

## Inputs

From the calling skill, or from the user directly:

- the concept and, inside a study session, the pass, focus, and return point;
- what the course material says about it, with page pointers;
- The user's goal: exam, understanding, or research use;
- the current task's selected enrichment setting, then the applicable verified standing setting, then deep when neither applies. A request for full enrichment selects deep. Honor the selected or applicable verified media setting. Include media when useful and that choice is open;
- any specific ask: a video, a diagram, a check of one slide.

## Steps

1. **Gap scan.** Compare what the course material gives with what a solid understanding needs: missing steps, unexplained terms, missing intuition, a questionable claim, a missing picture.
2. **Choose.** Honor explicit requests, such as a diagram and a video together. Use the current task's selected enrichment setting, then the applicable verified standing setting, and fall back to deep only when neither applies. In deep mode, choose a coherent sequence of explanations, figures, and worked examples across the useful parts of the menu, without a fixed figure count or a one-image/video cap. Each addition should clarify a distinct relationship, step, comparison, or misconception. Standard adds one or two enrichment items and a small selection of media; off adds no unsolicited enrichment, while an explicit request is handled without changing the saved setting. Read `./references/teaching_visuals.md` when making or adapting a visual, equation, or worked example. Reuse a clear caller figure, simplify a confusing one, or add a complementary view when it addresses the current gap.
3. **Look up, in this order:**
   1. the course material, which stays the authority for course conventions and exam answers;
   2. the course textbooks;
   3. reputable outside references: other textbooks, university course notes, official software documentation;
   4. papers, lightly: one illustrative application at most, while any literature search goes to a research skill;
   5. the model's own knowledge and reasoning, labeled as such and never the only support for a specific fact.

4. **Check.**
   - Open every link before including it.
   - Confirm each video's title and channel from its page or YouTube's public oEmbed endpoint; give its length only when the page or a search result shows it.
   - Recompute every number and step of a derivation.
   - Check each visual's quantities, units, scales, arrow meanings, readability, and supported rendering under the teaching-visual rules.
   - Note where an outside source uses a different convention or notation from the course.
5. **Package and return.** When another skill invokes Study Enricher, send one bounded packet to that caller. For a direct request, return the same labeled material in the current task's requested response form or under the recipient's existing reporting policy. Lead each item with its central point in one plain sentence, then the detail. Place figures and worked examples beside the explanation they support. Give brief reading guidance and distinguish source material, model reasoning, illustrative values, calculations and simulations. The caller may teach the sequence across its current blocks.

## Outputs

Keep one concept-focused packet with the evidence and teaching fields below. For a direct request, use the selected response form.

```text
Beyond the course: [concept]  (setting: [selected setting])
1. [deeper mechanism | another explanation | connection | your field | next | misconception | practice | slide check]
   [explanation, worked example, comparison, or derivation at the selected depth]
   Source: [course page | textbook section | outside source with link | model reasoning]  Priority: [exam core | understanding | optional]
[Figures and media beside the relevant items: made figure | image: checked source-page link | video: title, channel, what to watch and why]
Convention note: [where outside material differs from the course], when relevant
Questions: [one or two why or how questions for the user]
```

- Use the requested or applicable verified equation form, including any equation format carried in a bounded handoff. Where the format is open, use the supported LaTeX or plain-text representation in the teaching visuals reference.
- Made figures identify their teaching basis briefly: sourced, schematic, worked example, calculated, or simulated, with a short explanation of how to read them. No fixed caption or metadata block is required.
- Study Enricher returns the checked source or figure without saving it. Route an authorized figure save to Study Planner with the selected destination or its visuals-rule fallback. Pass a source or figure pointer for recording only when the scope includes that index edit.

## Boundaries

- Course conventions win for exam answers; say where outside material differs.
- Never include a link, video, image, or citation that was not opened and checked.
- Link found images; do not copy them into the vault.
- Keep standard packets short; deep packets give richer visual and example support while staying on the current concept and respecting the user's pace.
- Study Enricher stays read-only. Study Planner owns authorized figure saves and any separately scoped index update.

## Handoffs

- Return to the invoking skill: Study Planner during a session, Study Companion in open chat, or the verified caller that requested this bounded support.

- Outside practice problems also feed [study-quiz](../study-quiz/SKILL.md) when it asks.
- Unsaved concept maps stay with the current study owner (Study Companion in open chat or Study Planner in a session). Route an authorized map save through that owner to [mindmap](../mindmap/SKILL.md).
- Literature searches, paper summaries, and paper evaluation go to a research skill.
- Keeping anything goes through study-planner.

## Checks

- Every link opened; every video's title and channel confirmed.
- Every number and derivation recomputed; notation matches the course, or the difference is stated.
- Each item carries a source label and a priority.
- Figures and examples agree with each other and the prose; useful earlier figures are reused or repaired, and every added view addresses a teaching gap.
- Preserve the current task's selected enrichment setting, then the applicable verified standing setting, in the packet returned to the caller. Use deep only when neither applies. With off, return outside practice only when specifically requested and within the requested scope.

## References

- Google. (n.d.). *Add or discover new sources*. Gemini Notebook Help. https://support.google.com/notebooklm/answer/16215270
- Google. (n.d.). *Guided Learning in Gemini*. https://blog.google/products-and-platforms/products/education/guided-learning/
- Google. (n.d.). *NotebookLM adds Deep Research and support for more source types*. https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-deep-research-file-types/
- lowwwbank. (n.d.). *anything-to-course* (Version 1.0) [Computer software].
