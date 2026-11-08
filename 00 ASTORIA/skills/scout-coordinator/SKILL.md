---
name: scout-coordinator
description: >-
  Part 1 coordinator, help me scout the field. Routes one bounded literature or
  first-principles research request to the matching skill in its generated
  catalog, then returns to the invoking companion. Chooses no
  scientific question, source, or claim; it identifies the one capability whose
  contract fits the request and hands over the exact scope. Use when the request
  is about finding, reading, explaining, or synthesizing papers, or exploring
  the mathematical foundations of a research question or method. Triggers: help
  me find papers on this, summarize what the literature says, what do we know
  about this topic.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "1"
  family: part-coordinator
  modality: any
  dependencies: research-coordinator
  requires: ""
  gates: ""
  created: "2026-09-23"
  updated: "2026-10-20"
---

# Part 1: Help Me Scout the Field

Part 1 of scientific inquiry: observe and situate. Gather, organize, compare, and explain evidence, and explore the foundations of possible inquiries while separating source claims, observations, and AI interpretation.

## Steps

1. Confirm the request belongs to this part. Explicit first-principles exploration, mathematical study deconstruction, unresolved-question scouting, method transfer, and exploratory minimal models belong to `first-principles-research`. Formal critique, study design, and research-data analysis use their respective part coordinators.
2. Read the catalog below and pick the one skill whose first sentence and triggers fit the request.
3. Open `00 ASTORIA/skills/<name>/SKILL.md` and read it completely. Check `requires` and `gates` in its frontmatter before acting.
4. Hand over the exact scope: the sources, the question, and the boundaries the user gave. Do not widen it.
5. Return the result to the invoking companion with the skill named. Start no additional workflow automatically. A selected skill's declared conditional dependency may support the requested job within its scope and existing authorization.

## Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

### Literature discovery and synthesis
- [first-principles-research](../first-principles-research/SKILL.md) (any): Explores research questions, studies, and methods by reconstructing their first principles and mathematical structure. Triggers: reason through first principles, deconstruct this study mathematically, find cross-field mathematical connections, scan all ten frameworks, explore my research from fundamentals.
- [literature-synthesis](../literature-synthesis/SKILL.md) (any): Builds one bounded critical theory synthesis from supplied sources or an explicitly approved literature search. Triggers: synthesize these papers, build a theory synthesis from these sources.
- [paper-search](../paper-search/SKILL.md) (any): Runs one researcher-directed scholarly discovery task through a short Search Direction and one upfront approval, then searches the approved public, institutional, browser-assisted, and user-provided routes within a stated budget. Triggers: search the literature for, find papers on this topic.
- [research-summarizer](../research-summarizer/SKILL.md) (any): Explains one or more bounded research papers through a separate source-verified seven-part summary for each paper, covering plain-language and expert explanations, statistical methods and results, key findings, strengths, weaknesses, and discussion questions. Triggers: summarize this paper, explain this study to me, what does this paper claim.

4 skills in this part.
<!-- catalog:end -->

## Handoffs

- The human-control contract in `00 ASTORIA/skills/research-coordinator/references/research_contract.md` applies to every route. The user owns the question and the claims; a coordinator only finds the capability.
- Select one primary skill for the requested job. Summarizing supplied papers goes to research-summarizer; building a synthesis across supplied or approved sources goes to literature-synthesis; discovering new sources goes to paper-search with its Search Direction and any approval already supplied.
- Mathematical first-principles exploration goes to first-principles-research. It recommends one of its five modes and begins immediately; the user can switch naturally without a mode-selection gate. Generic heuristic divergence remains with scientific-brainstorming in Part 2.
- First-principles-research may identify a bounded paper-search dependency to check a candidate gap or source. Preserve the current question and return point, use the existing search authorization when it covers the direction, and return the source packet to that reasoning task. Do not turn this into an automatic multi-part research pipeline.
- Never invent a citation or initiate an unrelated search. A coordinator selects capabilities; it does not choose a research question or accept a scientific claim.
- Keep source claims, observations, and AI interpretation labeled and separate in whatever the selected skill returns.
- The selected skill returns to the invoking companion; outside a companion-led session it returns to the user directly.
