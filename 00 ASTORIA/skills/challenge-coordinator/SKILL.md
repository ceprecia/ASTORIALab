---
name: challenge-coordinator
description: >-
  Part 2 coordinator, help me challenge my question. Routes one bounded request to
  scientific-brainstorming, research-literacy, or research-critique from its
  generated catalog, then returns to the invoking companion. Makes no scientific
  judgment itself. Use when the request is about generating candidate
  directions, auditing a claim against evidence, or critiquing a research
  object. Triggers: is my research question worth asking, brainstorm directions
  for this question, check this claim against the evidence, critique this study.
metadata:
  level: coordinator
  system: Research Assistant System
  part: "2"
  family: part-coordinator
  modality: any
  dependencies: research-coordinator
  requires: ""
  gates: ""
  created: "2026-09-23"
  updated: "2026-09-23"
---

# Part 2: Help Me Challenge My Question

Part 2 of scientific inquiry: question and scope. Challenge clarity, constructs, validity, scope, alternatives, and claim boundaries without independently choosing the research program.

## Steps

1. Confirm the request belongs to this part. A literature question goes to scout-coordinator; a hypothesis or design question goes to stress-test-coordinator.
2. Read the catalog below and pick the one skill whose first sentence and triggers fit.
3. Open `00 ASTORIA/skills/<name>/SKILL.md` and read it completely. Check `requires` and `gates`.
4. Hand over the exact object and the boundaries the user gave.
5. Return the result to the invoking companion with the skill named.

## Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

### Question, claim, and study critique
- [research-critique](../research-critique/SKILL.md) (any): Critiques one bounded research object through a rapid blind-spot scan, targeted critique, or full scientific critique. Triggers: critique this paper, find the blind spots in this design, full scientific critique.
- [research-literacy](../research-literacy/SKILL.md) (any): Audits one explicit research claim and its directly linked subclaims against supplied and bounded verified evidence. Triggers: audit this claim against the evidence, does the evidence support this claim.
- [scientific-brainstorming](../scientific-brainstorming/SKILL.md) (any): Runs bounded scientific divergence from a user-supplied seed, using ideation heuristics when useful. Triggers: brainstorm scientific directions, divergent ideas from this seed.

3 skills in this part.
<!-- catalog:end -->

## Handoffs

- The human-control contract in `00 ASTORIA/skills/research-coordinator/references/research_contract.md` applies to every route.
- Divergence from a supplied seed goes to scientific-brainstorming; auditing one explicit claim and its subclaims against bounded evidence goes to research-literacy; critiquing a bounded research object (a paper, a design, a draft, a plan) goes to research-critique, which picks its own depth (blind-spot scan, targeted, or full).
- The Companion and Critique heuristics are internal micro-checks inside their existing workflows, not new skills, parts, mandatory output sections, approval gates, searches, analyses, or routes. Companion stops its uncertainty loop when remaining uncertainty would not change the current decision, claim ceiling, required disclosure, or route. Critique embeds its checks in the Study Logic Map, Critique Matrix, and response options, uses one strongest credible rival by default, and never calculates or invents missing quantitative information. Before weakening causal or comparative language, Critique checks manipulation, assignment, unit, temporal order, counterbalancing, interference, and bundled components so caution narrows the claim to the design-supported level instead of automatically reducing an experimental contrast to association.
- Scientific critique and shared writing specialists do not launch each other automatically; preserve the requested service and original return owner.
- Boundary with part 3: this part challenges and critiques an existing research object or claim. Developing or stress-testing the user's own prospective hypothesis, design, power, or dataset choice belongs to stress-test-coordinator.
