---
name: scientific-brainstorming
description: >-
  Runs bounded scientific divergence from a user-supplied seed, using ideation
  heuristics when useful. Proposes concrete candidate questions, hypotheses,
  predictions, or design sketches grounded in available evidence and constraints.
  Uses task-sized options without ranking or adopting a scientific direction;
  strategic recommendations and implementation retain their specialist owners.
  Triggers: brainstorm scientific directions, divergent ideas from this seed.
metadata:
  level: skill
  system: Research Assistant System
  part: "2"
  family: critique
  modality: any
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Scientific Brainstorming

Widen one scientific possibility space and make concrete proposals the user can evaluate. Keep generated candidates distinct from adopted scientific decisions.

## Purpose

`scientific-brainstorming` is the Part 2 owner for explicit structured
scientific divergence and heuristic connection mapping.

First-principles exploration, mathematical study deconstruction, structural
method transfer, and exploratory toy models belong to Part 1's
[first-principles-research](../first-principles-research/SKILL.md).
Resolve that boundary before the brainstorming steps below. An explicit
request for that work authorizes the bounded route; use its automatic mode
recommendation and ordinary-language switching without adding this skill's
technique or presentation choices. If a companion owns the session,
return the route through that companion.

It owns:

- establishing one bounded scientific seed for an ideation session
- using relevant brainstorming heuristics, with user selection when requested
- generating a diverse set of clearly labeled possibilities
- exposing assumptions, evidence needs, limitations, tensions, and possible
  connections without ranking the ideas
- producing a bounded proposed idea brief, or developing the user-selected direction

It does not own:

- strategic comparison, a provisional recommendation, project triage, or
  selected-direction development, which belong to [research-companion](../research-companion/SKILL.md)
- evidence auditing for an explicit claim, which belongs to
  [research-literacy](../research-literacy/SKILL.md)
- literature, gap, or novelty checking, which belongs to [paper-search](../paper-search/SKILL.md)
- detailed scientific critique, which belongs to [research-critique](../research-critique/SKILL.md)
- prospective stress testing of a user-supplied hypothesis and prediction, which
  belongs to [prediction-stress-test](../prediction-stress-test/SKILL.md)

The user owns scientific choices. This skill generates labeled proposals, not
adopted decisions. Use the user's current selections; an exact candidate can
be adopted by reference without retyping. Interest or silence is not adoption.
Current authorization covers requested bounded work and routing; preserve the
receiving skill's existing approvals. Ask only for material missing inputs or
choices, and continue unaffected work.

Use this skill when the user names it, the bounded scientific request matches its frontmatter description and trigger meaning, or a verified coordinator or capability handoff selects that same task.

These triggers apply only to a scientific or research seed. Do not use this
skill for slogans, marketing, fiction, personal planning, general creativity,
or other non-scientific brainstorming.

If the user explicitly invokes `research-companion`, that capability owns the
session. Use this skill when the user wants a wider, technique-guided option space;
use Research Companion when the user wants strategic comparison, a provisional
recommendation, or development of a selected direction.

## Inputs

Use current context and gather only what the task needs:

- **Scientific seed:** One question, problem, observation, tension, construct,
  limitation, or opportunity supplied by the user.
- **Fixed constraints:** Decisions, resources, populations, data, methods, or
  boundaries that must not be changed.
- **Open dimensions:** Parts of the seed that the user permits the session to vary.
- **Evidence boundary:** Supplied sources or project context that may be used,
  plus material that remains unavailable or intentionally unloaded.
- **Desired output:** A quick option set, a deeper connection map, or a selected
  idea brief.

Do not ask the user to repeat information already present in the bounded context.
If several projects or seeds are mixed together, identify their boundaries and
ask which to use first only when the request does not resolve that material choice.

## Steps

A clear request needs no separate scope, technique, idea, or handoff approval.
Use only the steps and visible structure the output needs.

### 1. Establish the bounded scope

Identify the seed, fixed constraints, available evidence, and output. Ask
directly about missing outcomes, constructs, populations, or resources when
they would change the candidates or feasibility. Keep unknowns visible and
continue work that does not depend on the answer.

### 2. Use a helpful technique

Follow a named technique; otherwise use a suitable heuristic or small
combination. Explain its role when useful. Offer technique choices only when
requested or materially unresolved. The optional menu below remains available;
its heuristics are not validated scientific methods.

### 3. Generate concrete candidates

Match the number and depth of ideas to the task. Use options, cards, or a table
without a fixed count or field inventory. Where evidence and constraints permit,
propose an answerable question, hypothesis, prediction, or design sketch with
its evidence basis, distinguishing observation or comparison, and feasibility
limits. Label exploratory assumptions and unsupported analogies. Do not replace
missing substance with generic headings, invented facts, or novelty claims.
Detailed design and implementation retain their specialist owners.

### 4. Expose useful connections and differences

Map clusters, tensions, combinations, or redundancies only when useful. Compare
scientific value, assumptions, evidence needs, and uncertainty without ranking,
scoring, or recommending a winner. Similarity is not scientific evidence.
Requested strategic recommendations route to Research Companion.

### 5. Develop the requested brief

An option set can complete the task. For a requested brief, organize the seed,
proposed or selected direction, evidence, constraints, and unresolved questions
in the smallest useful form. Keep unselected alternatives distinct. Ask for a
choice only when the next requested output depends on it.

### 6. Verify and route

Check request fit, specific scientific content, evidence labels, fixed choices,
and unresolved limits. Repair presentation directly; ask about a scientific
conflict without choosing for the user. Route requested searches, critique,
stress testing, or saves to their owners, retaining the invoking companion and
return point. Preserve the receiving skill's existing approvals. Offer
unrequested downstream work without starting it.

## Full optional technique menu

These are ideation heuristics from the approved SAS source. They are prompt
structures, not validated scientific methods, evidence standards, or automatic
selectors.

### SCAMPER

Transform an existing idea through substitute, combine, adapt, modify, put to
another use, eliminate, or reverse. Use it to vary a known frame without
assuming that every transformation is scientifically appropriate.

### Six Thinking Hats

Inspect the seed through facts and missing information, intuition and values,
risks, possible benefits, alternatives, and process control. Keep intuition
separate from evidence and do not let the technique decide the scientific
position.

### Morphological analysis

List a small number of important dimensions and options, then inspect selected
combinations. Do not treat the resulting combination space as exhaustive or
every combination as meaningful.

### TRIZ-style contradiction prompts

Identify competing requirements and explore moves such as segmentation,
removal, local optimization, merging, prior action, or protective preparation.
Use these as prompts only. Do not claim formal TRIZ analysis or historical
validation.

### Biomimicry

Define the function, identify possible natural analogues, abstract a candidate
strategy, and ask whether the analogy transfers. Natural examples and transfer
claims require verification before scientific use.

### Provocation

Introduce an intentionally impossible statement, identify what makes it
interesting, and extract a bounded principle that might be examined without
retaining the impossible premise.

### Random input

Use a random concept supplied by the user or selected without an external service,
describe its properties, and force tentative connections to the seed. Label
every connection as an analogy requiring review.

### Reverse assumptions

List material assumptions and reverse one at a time to expose alternative
frames. A reversal is an ideation move, not evidence that the opposite is true.

### Future backwards

Imagine a future in which the bounded problem has improved, then work backward
to identify possible enabling conditions and prior steps. Do not treat the
scenario as a forecast.

## Cross-cutting ideation moves

Any selected technique may also use:

- cross-domain analogy
- scale shifting
- temporal reframing
- constraint removal or addition
- connection making

Keep every move inside the approved scope and label unsupported scientific
content.

## Outputs

Return requested options, cards, maps, comparisons, and idea briefs in the current task's requested form or under the recipient's existing reporting policy. Saving requires authorization. These are output choices, not a mandatory
sequence or section inventory.

For an authorized durable note, use the verified eligible destination selected for the task, then the applicable verified recipient or project placement policy. Where placement remains open, resolve the verified owner location. Keep Project or Area working material in its local `files/` or documented workspace. Use Resources for reusable references. Preserve established operational layouts. Resolve a missing owner or destination before writing. Use the selected filename or applicable verified naming convention. If neither provides one, use `YYYY-MM-DD_scientific_brainstorming_<topic>.md`.

Verify the destination, proposed content and any paths or links before writing. Provide a preview when requested or when approval is needed. A MOC link requires authorization for the note edit.

## Boundaries

Evidence and scientific rules:

- Separate supplied facts, source-supported statements, the user's decisions,
  AI-generated possibilities, unverified analogies, and unresolved questions.
- Do not invent citations, results, methods, samples, statistics,
  preregistrations, constraints, or project facts.
- Do not call a possibility a research gap or novel direction without an
  adequate evidence check within the authorized evidence boundary.
- Keep candidates labeled as proposals until the user adopts a scientific choice.
- Do not recommend a design or method merely because it appeared in an analogy
  or because software is available.
- Do not convert exploratory possibilities into confirmatory claims.
- `p > alpha` is not significant. Do not call it marginal, approaching
  significance, a trend, or nearly supported.
- Nonsignificance does not establish absence.
- Follow the bounded authorization rule in Purpose; retain existing action requirements.

Edge cases:

- **Seed is too vague:** Ask about the material missing problem, observation,
  question, tension, or constraint; continue independent useful work.
- **Several projects are mixed:** Identify their boundaries and ask which is in
  scope only when the current request does not resolve that choice.
- **No evidence is supplied:** Brainstorm with explicit
  `AI-generated possibility` labels and make no evidence-based gap, novelty,
  feasibility, or mechanism claim.
- **The user requests several techniques:** Use a task-sized combination or
  comparison; ask only when a material conflict remains unresolved.
- **An analogy contains an unsupported fact:** Remove the factual claim or mark
  it for separate verification before using the analogy.
- **The user rejects every idea:** Preserve what was learned and generate another
  bounded round only if the user requests it.
- **The user asks for a winning idea:** Route the requested strategic comparison
  to Research Companion within existing authorization rather than ranking the set here.
- **Hypothesis or design generation requested:** use Step 3 for candidates;
  detailed design retains its owner. [prediction-stress-test](../prediction-stress-test/SKILL.md) requires an exact
  supplied or adopted hypothesis and prediction.
- **Stress testing requested with exact inputs:** use [prediction-stress-test](../prediction-stress-test/SKILL.md)
  within existing authorization once its inputs are sufficient.
- **The request becomes non-scientific brainstorming:** Stop and route outside
  this skill.
- **Context compaction or model switch occurs:** Reload this skill and the
  bounded seed before continuing.

## Handoffs

- Use [first-principles-research](../first-principles-research/SKILL.md)
  through Part 1 when the user requests mathematical first-principles work.
  Carry the seed, constraints, and already rejected formulations forward. The
  request authorizes the bounded route; preserve its existing requirements.
- Use [research-companion](../research-companion/SKILL.md) to compare brainstormed directions strategically,
  offer a provisional recommendation and contrary case, or develop a selected
  direction.
- Use [research-literacy](../research-literacy/SKILL.md) to audit one explicit claim against bounded
  evidence.
- Use [paper-search](../paper-search/SKILL.md) for a bounded literature, gap, or novelty check after
  the user approves a search brief.
- Use [research-critique](../research-critique/SKILL.md) when detailed scientific critique of one bounded
  research object is needed.
- Use [prediction-stress-test](../prediction-stress-test/SKILL.md) for requested prospective stress testing of
  exact supplied or adopted inputs; otherwise offer it as an optional next step.
- If an invoking companion routed this capability and project continuity or
  route selection becomes the task, return that unresolved boundary to the
  invoking companion. If no companion invoked it, stop at this capability
  boundary and offer [research-companion](../research-companion/SKILL.md) only as an optional public routing
  entry.

Do not start unrequested downstream work.

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
