---
name: first-principles-research
description: >-
  Explores research questions, studies, and methods by reconstructing their
  first principles and mathematical structure. Recommends a working mode,
  selects relevant frameworks, and develops explanations or candidate directions
  through dialogue. Use for first-principles research discussion, mathematical
  study deconstruction, and cross-field method exploration. Triggers: reason
  through first principles, deconstruct this study mathematically, find
  cross-field mathematical connections, scan all ten frameworks, explore my
  research from fundamentals.
metadata:
  level: skill
  system: Research Assistant System
  part: "1"
  family: literature
  modality: any
  dependencies: paper-search
  requires: a research question, study, method, or bounded source set
  gates: ""
  created: "2026-10-20"
  updated: "2026-10-20"
---

# First Principles Research

Work from basic objects and relationships to mathematics, algorithms, and scientific consequences.

## Purpose

Explore a research question, reconstruct a study's logic, or examine a method
through explicit first principles and mathematical structure. Use the ten
frameworks in `./references/frameworks.md` as a starting toolkit, while allowing
other established frameworks when they fit better.

This is a Part 1 capability for understanding and situating possible inquiries.
It develops candidate formulations through dialogue; it does not choose the
user's research program. A first principle may be an identity, a physical law,
an empirical regularity, or a modeling assumption. Identify which it is.
Finding an assumption or an unstudied topic is only a starting observation.
Work out what follows, what can be distinguished, and why it matters.

Keep three choices separate:

- **Mode:** the job being done, selected from the five below.
- **Framework:** the mathematical structure used to reason about it.
- **Depth:** conceptual explanation, equations, algorithm, or a worked example.

## Modes

| Mode | Use when | Main work | Useful result |
| --- | --- | --- | --- |
| 1. Explore a question | The user brings an idea, observation, or research question and wants to think together. | Compare possible formulations, identify primitives and constraints, and develop one consequential distinction per round. | A clearer question, candidate mechanisms, and the next issue to resolve. |
| 2. Deconstruct a study | The user supplies a paper, figure, equation, or method. | Reconstruct the objects, assumptions, measurement model, mathematics, and algorithm actually supported by the source. | A six-part explanation separating the authors' work, our reconstruction, and possible extensions. |
| 3. Scout unresolved questions | The user wants to understand what remains unexplained or worth investigating. | Examine what existing representations and measurements can establish, derive candidate unknowns, and check their status against literature. | Evidence-supported candidate questions, their nearest established results, and what answering them would establish. |
| 4. Transfer a method | The user wants ideas from another field or sees a possible mathematical connection. | Map source objects to target objects, identify shared structure and changed assumptions, and test where the transfer fails. | An explicit correspondence with a derived consequence and a counterexample or boundary. |
| 5. Build a minimal model | The user wants to make an idea precise or calculate its implications. | Construct the smallest useful equation, derivation, toy case, or pseudocode and compare limiting cases. | An exploratory model with interpretable behavior, assumptions, and failure conditions. |

## Inputs

Start with the current request and relevant conversation. A question, observation,
study, method, or bounded source set is enough. Reuse the user's stated objective,
constraints, prior decisions, and rejected formulations. Ask only for a missing
detail that changes the reasoning; do not begin with a general questionnaire.

For a study, establish which source portions are available. With only an abstract,
work at the abstract's level and identify which equations, procedures, or results
cannot yet be reconstructed. For a method transfer, identify the target question
before choosing a source field or instrument. An available instrument, assay or software
package does not determine the question.

## Steps

### 1. Recommend a mode and begin

Infer the mode from the request and conversation. State the recommendation and
one short reason, then begin useful work in the same response. Do not wait for
menu approval. An explicit mode request takes precedence over automatic selection.

At the first invocation in a conversation, briefly offer all five modes with the
recommended one marked. Keep the menu to one compact line or short list. Later,
mention alternatives only when they are relevant or the user asks.

Example opener:

> I'll start in **Explore a question** because we need to distinguish what the
> proposed mechanism would explain. We can switch to **Deconstruct a study**,
> **Scout unresolved questions**, **Transfer a method**, or **Build a minimal
> model** at any point.

Follow this immediately with a working formulation or useful distinction.
Mode selection is a conversational choice, not acceptance of a scientific claim.

Retain the mode across turns unless the user switches or the task clearly changes.
Accept ordinary language such as "break down that paper instead," "look for open
questions," or "make a toy model." Announce a meaningful switch briefly, carry
forward the relevant reasoning, and continue without restarting intake.

### 2. Identify the objects and choose a framework

Name the phenomenon and what would count as an explanation. Identify the basic
objects: states, events, trajectories, representations, observations, actions,
connections, or fragments. Separate the underlying process from its measurement.

Use the quick index below to choose one primary framework and, when useful, one
alternative that exposes a different implication. Read the selected cards in
`./references/frameworks.md` before applying their equations or algorithms.
Explain the fit in one sentence. Do not force every question through all ten.

| Structure in the question | Starting framework |
| --- | --- |
| Stable distributions with possible hidden flow or time asymmetry | 1. Probability conservation and currents |
| Feedback, transitions, persistence, recovery, or multiple regimes | 2. Dynamical systems |
| Transformations, units, scale dependence, or invariant relationships | 3. Similarity, symmetry, and scale |
| Actions with delayed consequences, constraints, and uncertainty | 4. Optimal control |
| Limited representation with a specified purpose or distortion | 5. Information constraints |
| Hidden causes or objects inferred through incomplete measurements | 6. Inverse problems |
| Connectivity, holes, loops, or geometry beyond coordinates | 7. Algebraic topology |
| Large sums or integrals that can be estimated through sampling | 8. Monte Carlo methods |
| Observations versus changes produced by an intervention | 9. Structural causal models |
| Global order reconstructed from local overlap or compatibility | 10. Combinatorial reconstruction |

If asked to scan all ten, give a compact relevance scan first, including weak
fits, then deepen the best candidates. If none fits, say so and offer a better
established framework or clarify the objects. The ten are not an exhaustive
taxonomy. A new framework can be used for the current discussion without
silently adding it to the permanent library.

### 3. Develop the reasoning at the requested depth

Use this sequence for a detailed explanation:

1. **Abstract idea:** express the relationship without field-specific jargon.
2. **First principles:** define the primitives and classify each foundational
   statement as an identity, physical law, empirical finding, or model assumption.
3. **Mathematics:** derive the simplest useful relation. Define symbols, units,
   conditioning, constraints, and the observation model where relevant. Explain
   why the relation follows; an equation alone is not a derivation.
4. **Algorithm:** turn the relation into ordered operations or pseudocode. State
   the inputs, output, and a criterion for stopping or checking the calculation.
5. **Specific examples:** work a small illustrative case and connect it to a
   source-supported scientific use when relevant. Mark invented numbers as toy
   values and distinguish them from reported results.
6. **Boundary:** identify when the inference fails, what remains unidentifiable,
   and which assumptions a transfer or extension would change.

This is a reasoning sequence, not a mandatory six-section report every turn.
In discussion, give a working formulation, one useful distinction, its implication
or competing interpretation, and one consequential question when needed. Expand
the equations or algorithm when they resolve the current uncertainty or the user
asks for depth. Do not end a complete bounded request with an unnecessary question.

Use rival formulations, limiting cases, and counterexamples to test consequences.
Examples include zero noise, perfect information, missing observations, short
horizons, disconnected components, and violated independence. Select cases that
matter to the actual model. Distinguish identifiability, computational tractability,
statistical precision, and empirical validity.

### 4. Apply the selected mode's emphasis

- **Explore a question:** offer competing formulations rather than silently
  adopting one. Track which distinction changes the next inference. Start with
  the phenomenon, not a favored method or a generic problem-to-solution story.
- **Deconstruct a study:** explicitly separate **reported by the authors**,
  **our reconstruction**, and **proposed extension**. Anchor reported equations,
  procedures, and findings to available source locations. If the paper does not
  provide the needed details, leave that part unresolved rather than supplying
  a familiar method as if it were the authors' method.
- **Scout unresolved questions:** distinguish a conceptual candidate from a
  literature-checked open question. State the closest known result, the precise
  remaining unknown, the observation or calculation that would resolve it, and
  what changes scientifically if it is resolved. Check alternative terminology
  and mathematical equivalents before making a novelty claim.
- **Transfer a method:** show source objects, target objects, shared mathematical
  relation, changed assumptions, derived consequence, and failure condition.
  A resemblance in vocabulary is insufficient. If the correspondence breaks,
  explain where instead of treating the analogy as a mechanism.
- **Build a minimal model:** choose only variables needed for the current
  distinction. Label assumed relationships and parameters. Work a tractable
  example, check units and limiting behavior, and compare at least one rival
  when it would expose a non-unique explanation. Pseudocode or a small toy
  calculation stays exploratory; formal study design and data fitting have
  their own owners.

### 5. Check sources when the claim requires it

Use supplied sources and verified material first. Foundational cards support
mathematical reasoning, not claims that a present-day field has a particular gap.
Before describing something as new, unresolved across a field, or absent from the
literature, obtain a bounded literature check and state its coverage limits.

When scholarly discovery is needed, use the conditional `paper-search` handoff.
Pass the scientific question plus structural search families, such as "stationary
distribution + probability current" or "inverse problem + identifiability," as
well as domain terms. Use its Search Direction and existing authorization;
do not request the same approval again. When the search scope is not yet settled,
prepare the concrete search direction while continuing reasoning that does not
depend on its results. Keep candidate gaps provisional until evidence returns.

Retrieve and inspect relevant source content before relying on a search hit.
Distinguish primary results, review claims, our derivations, and speculative
applications. An unsuccessful query, a method uncommon in one field, or a
plausible analogy alone does not establish a research gap or a breakthrough.

### 6. Return the useful result and retain continuity

Keep the active question, mode, working assumptions, rejected formulations, and
next unresolved issue available in the conversation. Refer back to them as needed;
do not print a status block on every turn or create a separate state file.

Return to the invoking companion when there is one, preserving its session and
workstream. Otherwise continue directly with the user. Finish the requested
bounded work; an optional next direction is not a new automatic workflow.

## Outputs

Return the result in the current task's requested form or under the recipient's existing reporting policy. Match the depth and length to the current exchange:

- A short reasoning round for **Explore a question**.
- The six-part explanation for a detailed study or framework deconstruction.
- A bounded set of candidate questions with evidence status for gap scouting.
- A source-to-target correspondence and tested implication for method transfer.
- A minimal model, calculation or pseudocode, and limits for model building.

Use a diagram or table when it clarifies the mathematical structure or comparison.
Save only when requested, following the owning destination and conventions in
`me.md`. The skill-owned reference cards are sufficient for routine use; ordinary
delivered notes are not startup dependencies. Do not promote a discussion result
to an approved aim, hypothesis, design, or durable decision merely by saving it.

## Boundaries

- Framework selection is provisional and revisable. Do not equate a convenient
  mathematical representation with the mechanism of the system.
- Ground cross-field transfer in explicit correspondence and assumptions. Do not
  equate information with energy, stationarity with detailed balance, a fitted
  dynamical law with unique causation, or persistent topology with function.
- Preserve the distinction between a toy model, a source-supported conclusion,
  and an empirical claim requiring new evidence.
- When access is partial, identify the available portion and reason within it.
  A bibliographic record does not establish what a study actually tested.
- Selecting or switching a mode requires no approval checkpoint. Consequential
  scientific choices remain with the user under the research contract.

## Handoffs

- `scout-coordinator` routes this Part 1 job. `research-companion` remains the
  visible session owner when it invoked the work.
- Load `paper-search` only for needed scholarly discovery within the requested
  scope. In a companion session, request the bounded search route through that
  companion; in direct use, explicitly invoke Paper Search for that dependency.
  Read its skill and satisfy its Search Direction using authorization already
  given. After the source packet returns, resume the original reasoning task.
- A full paper summary uses `research-summarizer`; critical synthesis across a
  source set uses `literature-synthesis`. This skill owns the mathematical
  deconstruction when that is the requested deliverable.
- Generic heuristic divergence uses `scientific-brainstorming`. Strategic
  prioritization among research directions returns to `research-companion`.
- Formal computational method specification uses `method-design` through Part 3.
  Full experimental design, fitting models to research data, and publication
  prose go to their corresponding part coordinator when requested. Toy reasoning
  alone does not require those handoffs.

## Checks

Before returning, verify what matters for this response:

- Was a mode recommended with a reason, with useful work starting immediately?
  Were explicit switches honored without losing relevant context?
- Do the chosen frameworks fit the objects and question? Was a weak fit exposed?
- Are identities, laws, evidence, and assumptions distinguished where needed?
- Do equations, units, conditioning, worked values, and algorithm steps agree?
- Does the scientific consequence follow from the mathematics and measurement
  model, or has a metaphor been mistaken for a derivation?
- Are source methods, our reconstruction, and proposed extensions distinguishable?
- Are gap and novelty statements calibrated to the sources actually checked?
- Does the response advance the current issue without repeating rejected ideas,
  imposing a full report, or selecting the user's scientific direction?
