---
name: prediction-stress-test
description: >-
  Prospectively stress-tests one exact user-supplied or explicitly adopted
  hypothesis and one primary prediction for testability, discriminability,
  counterexamples, boundary conditions, outcome implications, and bounded novelty
  evidence. Use when the request matches this description or names this skill, or a verified
  Research Coordinator or other Active-capability handoff selects one explicitly
  matching bounded task. Separates advisory findings from user-selected responses;
  uses existing authorization and retained action approvals. It does not generate
  hypotheses, predictions, designs, methods, power targets, or conclusions. Triggers: is this prediction testable, stress test this prediction.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: hypothesis
  modality: any
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-10-29"
---

# Prediction Stress Test

Apply prospective scientific pressure to one user-owned prediction without taking ownership of the research decision.

## Purpose

`prediction-stress-test` is the Part 3 canonical owner for prospective, prediction-centered stress testing of one exact user-supplied or explicitly adopted hypothesis and one primary prediction.

It owns:

- testability and discriminability;
- candidate results that would count against the prediction;
- counterexamples and alternative explanations;
- boundary conditions, adjacent constructs, and adjacent populations;
- implications of null, opposite-direction, and other contrary results;
- bounded novelty assessment within supplied or separately approved search evidence;
- selection-bound records and handoff packets for findings the user chooses.

The user owns the hypothesis, prediction, confirmatory status, design, method, measures, thresholds, power target, interpretation, novelty claim, scientific conclusion, and response to the stress test.

This skill may inspect a supplied design only to understand the prediction's manipulation, outcome, contrast, population, and timing. Whole-object design critique belongs to [research-critique](../research-critique/SKILL.md). Prospective design construction and comparison belong to [experimental-design](../experimental-design/SKILL.md). Quantitative power work and method implementation belong to separate capabilities.

The user may invoke this skill by name or with a bounded request matching its frontmatter description and trigger meaning.

A verified [research-coordinator](../research-coordinator/SKILL.md) or other Active-capability handoff
from the live [Skill Map](../../Skill%20Map.md) invokes one matching bounded task. Use current
instructions and choices without repeating supplied approvals; retain required
inputs, verification, and the receiving capability's existing action approvals.

Use one exact hypothesis and primary prediction the user supplies or explicitly adopts, including an AI candidate adopted by unambiguous reference without retyping. A seed or interest alone is not adoption. Review adoption establishes neither confirmatory status nor permission to implement the science.

Do not trigger from broad phrases such as:

- `stress-test this`;
- `critique this design`;
- `what am I missing`;
- `check this claim`;
- `is this novel`;
- `calculate power`.

One run covers one hypothesis and one primary prediction.

Keep up to three predictions together when the user specifies they are inseparable; ask only if unclear. Independent predictions require separate runs.

For a missing exact prediction, ask for its specification or adoption of an existing candidate. Do not derive or adopt it for the user; continue independent useful inspection with limits visible.

## Inputs

Gather only what is needed to define the stress test:

- exact hypothesis supplied or explicitly adopted by the user;
- exact primary prediction supplied or explicitly adopted by the user;
- up to two inseparable linked predictions when the user requests them;
- project, inquiry part, intended use, and decision in scope;
- population, construct, manipulation or exposure, outcome, contrast, and timing when supplied;
- intended confirmatory, exploratory, mixed, or unclear status;
- whether relevant outcomes were unseen, partly seen, or fully seen when the prediction and design decisions were made;
- supplied evidence and the permitted evidence boundary;
- relevant protocol, preregistration, analysis plan, deviations, thresholds, or decision rules;
- fixed constraints and user-owned decisions that must not be changed;
- requested stress-test lanes;
- known unknowns, unavailable material, and desired stop point.

Mark an essential missing item `unknown`. Do not fill it from assumption.

## Stress-test lanes

Use requested lanes, or the relevant lanes below for a broad stress-test request. State the scope briefly and ask only about material ambiguity:

1. **Testability and discriminability**
   - Ask whether the stated observation could distinguish the prediction from named alternatives.
   - Identify missing operational details or outcomes that several explanations would predict.

2. **Counterexamples and alternative explanations**
   - Generate clearly labeled challenge scenarios.
   - Separate a counterexample to the stated prediction from an alternative explanation for the same result.

3. **Boundary conditions and adjacency**
   - Test construct, population, setting, task, timing, scale, and measurement boundaries.
   - Identify adjacent constructs or populations only as candidate challenges, not as adopted extensions.

4. **Null and contrary-result implications**
   - Distinguish nonsignificant, opposite-direction, equivalence-supported absence, and insensitive or inconclusive outcomes.
   - Identify what each result would and would not license.

5. **Bounded novelty evidence**
   - Identify the exact novelty proposition and its comparison class.
   - Assess only supplied evidence or a separately approved bounded [paper-search](../paper-search/SKILL.md) result.

The user may select one or more lanes. Respect an explicitly limited selection; do not add a lane merely because it is available.

## Steps

### 1. Build the Prediction Stress-Test Brief

Preserve exact supplied or adopted wording. Use only the fields needed to make the requested review inspectable:

| Field | Required content |
|---|---|
| Project and stage | Exact project and inquiry part |
| Intended decision | What the user wants the stress test to help the user evaluate |
| Verbatim hypothesis | Exact supplied or explicitly adopted statement |
| Verbatim primary prediction | Exact supplied or explicitly adopted statement |
| Linked predictions | Up to two, only when the user says they are inseparable |
| Prediction components | Population, construct, manipulation or exposure, outcome, contrast, direction, and timing as supplied |
| Design context | Only context needed to interpret the prediction |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Outcome visibility | Unseen, partly seen, fully seen, or `unknown` |
| Selected lanes | Exact stress-test lanes requested |
| Evidence boundary | Supplied material that may be inspected |
| Fixed constraints | User-owned decisions that must not be changed |
| Missing material | Information needed but unavailable |
| Excluded work | New hypotheses, new predictions, design construction, power analysis, method selection, and any search, saving, or handoff outside current authorization |
| Stop point | The output or decision that ends the current run |

### 2. Resolve the stress-test boundary

A clear request with exact supplied or adopted inputs authorizes the review.
Ask only about missing specification or unresolved material choices; continue
unaffected work. Update the brief as context changes without automatically
reopening approval. Design construction, power, method choice, and
implementation retain their owners. Search, saves, and routes use existing
authorization and the retained approvals specified below.

### 3. Build the Prediction Logic Map

Use this structure when useful; a short targeted review needs no separate map:

`verbatim hypothesis -> verbatim prediction -> observable outcome or contrast -> result that would count against it -> required auxiliary assumptions`

For each link, record:

- the exact statement supplied or adopted by the user;
- what the supplied material directly supports;
- assumptions required for the link to hold;
- missing or conflicting information;
- whether multiple explanations predict the same observation;
- what cannot be assessed without design, power, or evidence work owned elsewhere.

Do not expand this into the whole-object question-to-claim map owned by [research-critique](../research-critique/SKILL.md).

### 4. Record What Survives Stress Testing

List aspects that remain coherent within the approved boundary, such as:

- an explicit comparison;
- a measurable outcome;
- a prespecified direction or pattern;
- a stated result that would count against the prediction;
- a construct or population boundary;
- a transparent auxiliary assumption.

Label each entry by basis:

- user-supplied or explicitly adopted statement, with AI authorship noted when applicable;
- supplied-evidence support;
- methodological inference;
- unverified assessment.

This section preserves useful structure. It does not validate the hypothesis or establish evidential support.

### 5. Build the Stress-Test Matrix

Create one row per candidate challenge:

| Field | Required content |
|---|---|
| Stress ID | Stable identifier |
| Lane | Approved stress-test lane |
| Target | Exact prediction component or auxiliary assumption under pressure |
| Challenge scenario | Clearly labeled candidate counterexample, alternative, boundary condition, or result pattern |
| Basis | User-supplied, source-supported, methodological inference, or unverified concern |
| Discriminating question | What the challenge tests or separates |
| Result implication | What a specified outcome would and would not count against |
| Auxiliary assumptions | Measurement, manipulation, sampling, sensitivity, model, or implementation assumptions |
| Stress status | One status below with a reason |
| Uncertainty and limits | Missing material, ambiguity, evidence limits, or competing explanations |
| Evidence needed | Exact missing evidence or source question |
| Downstream owner | The user or the appropriate existing or future capability |

Use exactly these stress statuses:

- **Discriminating within the supplied specification**: The stated observation separates the prediction from the named alternative within the displayed assumptions and evidence boundary.
- **Conditionally discriminating**: The distinction depends on unresolved auxiliary assumptions, measurement validity, sensitivity, implementation, or evidence.
- **Non-discriminating within the supplied specification**: The same stated observation is compatible with materially different explanations, or the supplied design context cannot separate them.
- **Not assessable from supplied material**: Essential prediction, design, sensitivity, or evidence information is unavailable.

Do not average statuses, assign numerical scores, count votes, or convert a status into a verdict about whether the hypothesis is true.

Every generated challenge scenario must be labeled `AI-generated challenge scenario`. It is not part of the user's research unless the user selects and adopts an action in response.

### 6. Separate outcome implications

Keep these cases distinct:

- **Nonsignificant result**: Does not by itself establish absence or falsify the hypothesis.
- **Opposite-direction estimate**: May count against the directional prediction, but interpretation still depends on uncertainty, measurement, design, and auxiliary assumptions.
- **Equivalence-supported absence**: Bears on effects outside prespecified, substantively justified equivalence bounds. It does not establish exact zero.
- **Insensitive or inconclusive result**: Cannot distinguish the prediction from alternatives because the design, measurement, sample, analysis, or evidence is insufficiently informative.
- **Result outside a prespecified prediction region**: Counts against the prediction only under the displayed decision rule and auxiliary assumptions.

Do not describe `p > alpha` as marginal, approaching significance, a trend, or nearly supported.

### 7. Handle evidence and bounded novelty

When a stress item requires evidence beyond the approved boundary, create an **Evidence Needs Register**:

| Field | Required content |
|---|---|
| Stress ID | Linked matrix finding |
| Evidence question | Exact question that cannot be answered from supplied material |
| Evidence type | Empirical, theoretical, methodological, dataset, or metadata |
| Comparison class | Construct, population, paradigm, prediction, method, or date boundary |
| Current status | Supplied, missing, inaccessible, conflicting, or unverified |
| Coverage risk | Provider, terminology, indexing, date, access, or source-type limitation |
| Proposed owner | [paper-search](../paper-search/SKILL.md), [research-summarizer](../research-summarizer/SKILL.md), [literature-synthesis](../literature-synthesis/SKILL.md), [research-literacy](../research-literacy/SKILL.md), or the user |

For novelty, use only:

- **Overlap candidate identified**
- **No close overlap identified within the bounded evidence**
- **Unresolved because of coverage or access**
- **Not assessed**

Never report a global `novel`, `not novel`, exhaustive, comprehensive, or complete verdict.

If the user selects [paper-search](../paper-search/SKILL.md), prepare:

| Field | Required content |
|---|---|
| Exact hypothesis and prediction | Exact supplied or explicitly adopted wording |
| Novelty or counterevidence question | Exact bounded verification target |
| Comparison class | Construct, population, task, method, outcome, or prediction pattern |
| Search route | Broad discovery, known item, one hop, or manual gap check |
| Concepts and variants | Proposed query families and permitted within-scope adaptations |
| Boundaries | Dates, source types, population, method, and exclusions |
| Seed papers or leads | Supplied identifiers or citations |
| Providers and access routes | Proposed public, institutional, or user-provided routes |
| Search budget | Exact total raw-record cap and stopping rule |
| Intended return | Complete candidate set, exact search record, shortlist logic, and coverage limits |

Show the complete packet as Paper Search's Search Direction and sole Gate 1.
If the user approves it or explicitly says to run it, Paper Search proceeds without
a separate handoff approval followed by another Gate 1.

When search evidence returns, require its complete candidate set, exact search record, and coverage limitations. If that evidence materially changes the stress-test boundary, update the brief and resolve only the consequential choices not covered by current instructions.

### 8. Present response options

For every consequential Stress-Test Matrix row, offer only applicable options:

- retain the current specification;
- return the item to the user for revision;
- investigate or gather evidence;
- prepare a bounded handoff;
- reject the stress finding while preserving the user's reason and the underlying basis and uncertainty.

Route requested replacement candidates to the brainstorming, framing, or
design owner. Verify only exact revisions the user supplies or adopts, without
strengthening or completing them.

### 9. Distinguish findings from selected responses

Return advisory findings without requiring item-by-item acceptance. Record
only actual user dispositions; leave others unresolved. Ask for a disposition
only when the next requested output depends on it. Selecting a finding does
not authorize protocol changes or scientific execution. Preserve a rejection's
reason alongside the finding's basis and uncertainty.

### 10. Produce and verify the Prediction Stress-Test Record

For a requested record with supplied dispositions, use the needed fields below. Otherwise return an advisory review with choices unresolved.

| Field | Required content |
|---|---|
| Approved scope | Project, hypothesis, prediction, linked predictions, lanes, and evidence boundary |
| What survives | Only items the user selected for this record |
| Selected stress findings | Only findings with supplied user dispositions |
| The user's disposition | Retain, return for revision, investigate, hand off, or reject |
| User-supplied or adopted revision | Exact wording with its source and explicit adoption distinguished |
| Verification result | Whether the revision addresses the selected finding without broader scientific endorsement |
| Evidence needs | Missing or conflicting evidence and coverage limits |
| Bounded novelty status | One permitted status with its evidence boundary |
| Handoff packets | Only packets the user selected for preparation |
| Prohibited overreach | Conclusions and actions not licensed by this run |
| Open items | Unresolved assumptions, evidence, design, sensitivity, or ownership questions |
| Provenance | The user's statements, AI-generated challenges, supplied evidence, and user decisions kept separate |

Verify that:

- the record matches the requested boundary and actual user dispositions;
- the hypothesis and prediction preserve the exact supplied or explicitly adopted wording;
- linked predictions were explicitly specified as inseparable;
- every AI-generated challenge remains labeled;
- no whole-design critique duplicated [research-critique](../research-critique/SKILL.md);
- no [research-literacy](../research-literacy/SKILL.md) evidence status or claim wording was assigned;
- nonsignificant, opposite-direction, equivalence-supported absence, and inconclusive results remain distinct;
- no bounded or empty search became a global novelty conclusion;
- no design, method, power target, threshold, model, interpretation, conclusion, or claim was silently selected;
- no unapproved search, save, source change, execution, or handoff occurred.

## Outputs

Select the sections needed for the requested depth:

1. **Prediction Stress-Test Brief**, when scope needs explanation
2. **Prediction Logic Map**, when useful
3. **What Survives Stress Testing**
4. **Stress-Test Matrix**, or a concise targeted review
5. **Outcome Implications**, when relevant
6. **Evidence Needs Register**, when evidence is missing
7. **Bounded Novelty Status**, when applicable
8. **Response Options**, when useful
9. **Prediction Stress-Test Record**, when requested and user dispositions exist

Return the stress-test results in the current task's requested form or under the recipient's existing reporting policy. Do not simulate approval or adoption. An unresolved choice
pauses only affected work. A review request alone does not authorize searches,
saves, source or data changes, or execution; use existing authorization for
requested work and retain the receiving capability's approvals. Before a save
or external action, make its destination and content reviewable, obtain any
outstanding required approval, and verify the result. A skill boundary adds no
new approval.

For an authorized saved output, use the destination the user names. Otherwise follow the recipient's configured placement policy, including an established operational project destination when that policy selects it. Apply the configured Area-folder boundary and keep skill and system implementation files in `00 ASTORIA/`. Verify current paths from `me.md` and the layout reference. Link from the existing owning MOC when the selected workflow calls for it and the link edit is authorized. Ask only when required ownership or destination remains unresolved.

## Boundaries

- **No explicit prediction**: follow the missing-input rule in Purpose; continue independent useful inspection.
- **Brainstorming brief only**: obtain the exact supplied or adopted inputs defined in Purpose before stress testing.
- **Several independent predictions**: Split them into separate runs.
- **Up to three inseparable predictions**: use the relationship specified by the user; clarify only if unresolved.
- **Outcome already seen**: Record the outcome visibility and do not retroactively label the prediction confirmatory.
- **Incomplete design context**: Mark affected rows `Not assessable from supplied material` or `Conditionally discriminating`; do not invent missing design details.
- **Whole-design critique requested**: Offer [research-critique](../research-critique/SKILL.md) and stop this workflow.
- **Claim support or wording requested**: Offer [research-literacy](../research-literacy/SKILL.md) and stop this workflow.
- **Power, sensitivity, or sample-size calculation requested**: Verify the appropriate registered power or sample-size owner against the current installed catalog and pass the bounded task within existing authorization, preserving its required inputs and gates. Report a capability or installation gap only when that check establishes one. Do not estimate from package availability or generic rules.
- **No supplied evidence**: Assess internal testability only and mark empirical, feasibility, and novelty conclusions unavailable.
- **Empty or failed search**: Preserve the search record and coverage limits. Do not infer absence or novelty.
- **Abstract-only evidence**: Use only what the abstract supports and preserve access limits.
- **Nonsignificant result**: Do not treat it as falsification or evidence of absence.
- **Opposite-direction result**: State what it counts against within assumptions without turning it into a complete scientific conclusion.
- **Unknown sensitivity**: Treat the result as conditionally discriminating or not assessable.
- **The user asks whether the work is novel**: State the bounded novelty status and coverage limits. Do not issue a global verdict.
- **Revision requested**: route candidate generation to its owner; verify exact supplied or adopted wording.
- **Selected response exceeds the evidence**: Preserve the mismatch and do not label the response verified.
- **Evidence boundary expands**: update the brief and resolve only outstanding material choices or permissions.
- **Context compaction or model switch**: reload this skill, current brief, exact inputs, and current user instructions.

## Handoffs

- Use [research-critique](../research-critique/SKILL.md) for detailed critique of one whole study, proposal, protocol, preregistration, analysis plan, design, or manuscript.
- Use [research-literacy](../research-literacy/SKILL.md) to audit the evidence status and wording of one explicit claim bundle.
- Use [paper-search](../paper-search/SKILL.md) for bounded discovery, known-item verification, one-hop expansion, or manual gap checking.
- Use [research-summarizer](../research-summarizer/SKILL.md) when one paper must be explained before it can inform the stress test.
- Use [literature-synthesis](../literature-synthesis/SKILL.md) when the task becomes an approved multi-source critical theory synthesis.
- Use [scientific-brainstorming](../scientific-brainstorming/SKILL.md) when the user has a scientific seed but has not adopted a hypothesis and prediction.
- Use [research-companion](../research-companion/SKILL.md) for broad framing, strategic comparison, and selected-direction development.
- If an invoking companion routed this capability and the project, stage, or
  destination capability remains unclear, return that unresolved boundary to
  the invoking companion. If no companion invoked it, stop at this capability
  boundary and offer [research-companion](../research-companion/SKILL.md) only as an optional public routing
  entry.
- Use [experimental-design](../experimental-design/SKILL.md) when a selected stress finding requires prospective construction or comparison of design structures.
- Use [cognitive-paradigm-design](../../specialized_skills/cognitive-paradigm-design/SKILL.md) when a selected stress finding requires prospective cognitive or behavioral construct-to-task operationalization or paradigm comparison.
- Use [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) when a cognitive or behavioral stress finding requires participant, item, trial, reliability, data-loss, or effect-evidence input specification.
- Use [statistical-power](../statistical-power/SKILL.md) when a selected stress finding requires a prospective quantitative power, sample-size, MDE, or operating-characteristic calculation from approved inputs.
- Use [fmri-task-design-guide](../../specialized_skills/fmri-task-design-guide/SKILL.md) when a selected stress finding requires model-aware task-fMRI timing or schedule validation after the neural estimand and model are approved.
- Use [neuroimaging-power-guide](../../specialized_skills/neuroimaging-power-guide/SKILL.md) when a selected stress finding requires MRI-specific inference, detection, effect-evidence, reliability, or pipeline input specification.
- Use [neuroimaging-sample-size-calculator](../../specialized_skills/neuroimaging-sample-size-calculator/SKILL.md) only after a selected MRI-specific Power Inputs Specification is approved for numerical execution.
- Route requested analysis execution or implementation to an authorized Part 4 capability with its existing requirements. If none is Active, disclose the gap and stop.

This skill does not generate or rewrite hypotheses or predictions, construct an experimental design, calculate power, select a method or threshold, audit claim support, critique an entire research object, search independently, synthesize a literature, save an unrequested record, execute an analysis, or make a scientific conclusion for the user.
