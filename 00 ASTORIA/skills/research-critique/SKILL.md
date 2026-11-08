---
name: research-critique
description: >-
  Critiques one bounded research object through a rapid blind-spot scan,
  targeted critique, or full scientific critique. For consequential inference
  links and supplied quantitative results, it conditionally audits warrants,
  rivals, quantitative meaning, and the least burdensome adequate response while
  preserving the strongest inference licensed by the design. It begins with a
  clearly labeled provisional critique and may continue through two user-control
  gates for a controlled Critique Response Record. When an invoking companion
  routed the task, every result returns to that companion with provisional
  findings kept distinct from user-selected findings that may inform the current
  scientific frame or an optional Research Writing Roadmap. It does not rewrite
  manuscripts, start writing specialists, execute analyses, or search independently.
  Triggers: critique this paper, find the blind spots in this design, full
  scientific critique.
metadata:
  level: skill
  system: Research Assistant System
  part: "2"
  family: critique
  modality: any
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-05-10"
  updated: "2026-11-01"
---

# Research Critique

Apply direct scientific friction without taking ownership of the research judgment.

## Purpose

`research-critique` is the Part 2 canonical owner for detailed scientific critique of one bounded research object. The object may be one study, proposal, protocol, preregistration, analysis plan, or manuscript. An integrated multi-study manuscript may be treated as one object only when the user approves that boundary.

The user owns the research question, hypotheses, predictions, confirmatory status, design choices, thresholds, models, interpretation, conclusions, claims, and response to the critique. This skill identifies strengths, blind spots, contradictions, missing links, and threatened inferences. It does not silently decide what the user should adopt.

This skill may be used across inquiry parts, but its home is Part 2 because its primary function is to challenge clarity, validity, scope, inference, and claim boundaries.

Use this skill when the request matches its description:

- the trigger phrases in this skill's frontmatter `description` (the model matches meaning, not exact strings; the skill's name also works as a direct call)

The input must identify or permit bounded extraction of one research object. Do not trigger this skill from generic requests such as `what am I missing`, `give me feedback`, `thinking partner`, `review this`, or `what do you think`.

[research-coordinator](../research-coordinator/SKILL.md) may route a clearly matching task to this capability from the live registry when the user asks for research-task routing.

## Inputs

The initial provisional critique requires only an identifiable research object and access to the material the user supplied or exactly named. Gather other information only when it is already available:

- exact research object and version;
- inquiry part and intended decision or use;
- The user's stated research question, claims, or goals;
- critique mode and selected lenses;
- supplied sources and permitted evidence boundary;
- whether outcomes were unseen, partly seen, or fully seen when consequential decisions were made;
- intended confirmatory, exploratory, mixed, or unclear status;
- relevant protocol, preregistration, analysis plan, deviations, thresholds, or decision rules;
- known constraints and missing material.

For the initial pass, infer a narrow working critique boundary from the supplied object, choose a provisional mode and relevant lenses, and mark missing facts `unknown`. Do not ask the user to approve these working assumptions before beginning. Do not generate the user's question, hypothesis, prediction, design, interpretation, or claim to fill a gap.

Use only the supplied research object and sources during the provisional pass. This skill does not search independently. A later controlled pass uses the evidence boundary the user approves at Controlled Gate 1.

## Critique modes

Use the user's selected mode when the user names one. Otherwise choose a provisional mode without asking:

### Rapid blind-spot scan

Return no more than five of the most consequential findings. Label the scan `non-comprehensive`. Do not imply that unreported problems were ruled out.

Use this as the default for a general request to critique a paper or study.

Keep this pass compact in the selected form or applicable verified reporting policy. When the display is open, use a concise presentation:

- summarize the provisional brief and keep each Study Logic Map link concise;
- use one compact row per finding if a matrix serves the selected or fallback form, or carry the same evidence in prose or another supported form;
- present no more than three priority tensions;
- apply the conditional inference micro-checks to no more than one or two
  central links or results unless another finding independently changes the
  claim boundary;
- consolidate overlapping explanations while retaining the reasoning needed to support each finding.

### Targeted critique

Apply only the lenses the user selects. Do not add unrelated review domains merely because they are available.

Choose this provisionally when the user's request already names a narrow concern, section, inference, or methodological domain.

### Full scientific critique

Apply every relevant lens below. Mark a lens `not applicable` when the research object or inquiry part does not require it. Do not invent work to fill the template.

Use this when the user explicitly asks for a full, comprehensive, or exhaustive scientific critique.

## Scientific critique lenses

Use only lenses that bear on the approved object:

- research-question clarity, testability, and scope;
- theoretical coherence and relevant alternative explanations;
- construct definition and operationalization;
- measurement validity, reliability, timing, scale, and scoring;
- design, comparison, confounding, selection, attrition, missingness, dependence, clustering, and internal validity;
- sampling, population fit, setting, exclusions, and generalization;
- estimand, contrast, model, unit of analysis, and analysis alignment;
- result-to-claim alignment;
- causal, mechanistic, comparative, predictive, and absence inferences;
- confirmatory versus exploratory status, outcome visibility, and deviations;
- transparency or reporting gaps that prevent scientific evaluation.

Flag a reporting omission only when it prevents evaluation of the science. A formal reporting-guideline audit belongs to check-research-reporting. Separate citation, substance, structure and argument-reasoning checks belong to their shared writing specialists; this skill retains detailed scientific critique.

Audit the coherence and threats of a supplied design. Prospective construction or comparison of design structures belongs to [experimental-design](../experimental-design/SKILL.md). Prospective prediction-centered falsifiability analysis, counterexample generation, bounded novelty assessment, and stress testing belong to [prediction-stress-test](../prediction-stress-test/SKILL.md).

## Steps

The default launch is a provisional critique without user gates. The controlled workflow becomes available after the user has something concrete to react to.

### 1. Build the Provisional Research Critique Brief

Faithfully describe the research object without rewriting it. Capture the following fields and present them within the selected deliverable:

| Field | Required content |
|---|---|
| Research object | Type, title or identifier, version, and exact bounded scope |
| Inquiry part | Planning, preregistration, data collection, analysis, interpretation, manuscript, or mixed |
| Intended decision | The user's stated aim, or the provisional aim `identify the most consequential strengths and threats to inference` |
| User-owned question and claims | The user's wording, or `unknown` |
| Critique mode | user-selected mode, or the AI-selected provisional mode and reason |
| Selected lenses | AI-selected relevant lenses for the provisional pass |
| Evidence boundary | Exact supplied object and sources inspected |
| Outcome visibility | What outcomes were available when consequential decisions were made |
| Confirmatory status | The user's stated status and basis, or `unknown` |
| Missing material | Methods, supplements, data, protocol, preregistration, results, or other limits |
| Excluded work | Independent objects, search, claim audit, rewriting, implementation, saving, and unapproved handoffs |

Do not ask the user to approve this brief before the initial critique. Label the brief `Provisional Gate 1 assumptions: AI-selected`. These are working assumptions for generating useful friction, not user decisions or authorization for additional access.

### 2. Build the Provisional Study Logic Map

Trace the research logic without filling missing links from assumption:

`question -> constructs -> operationalization -> design and comparison -> estimand and analysis -> result -> claim`

For every link, record:

- what the object explicitly states;
- what is supported by supplied evidence;
- assumptions needed for the link to hold;
- missing or conflicting information;
- the implication if the link fails.

For a pre-results object, map planned results and claims only when the user supplied them. Otherwise mark those links `not yet available`.

#### Conditional inference micro-checks

Use these inside the existing Study Logic Map and Critique Matrix. Do not turn
them into separate artifacts, mandatory output sections, approval gates,
searches, analyses, or downstream routes. Surface only findings that materially
change an inference, claim boundary, required disclosure, response option, or
route.

**Warrant-and-Rival Audit.** Activate this check only for a consequential
logic-map link:

`claim -> exact evidence -> warrant -> backing when needed -> qualifier -> strongest credible rival -> distinguishing evidence -> claim boundary`

- State the inferential rule or assumption that connects the evidence to the
  claim. Do not treat a citation or statistical result as self-interpreting.
- Identify one strongest credible rival by default. Add another only when it
  is independently decision-relevant. Do not generate an exhaustive objection
  catalog.
- State whether the supplied study rules the rival out, weakens it, leaves it
  viable, or never tests it.

**Strongest-design-licensed inference.** Preserve the strongest inference the
design actually licenses. Before weakening causal or comparative language,
identify the manipulation, assignment process, unit of assignment, temporal
order, counterbalancing, interference or carryover, and bundled condition
components.

- Preserve a condition-level causal effect when adequate manipulation and
  assignment support it, even when the mechanism remains unknown.
- Keep participant-generated behavior, post-assignment variables, mediators,
  bundled components, and specific mechanisms distinct from the assigned
  condition. Randomizing a condition does not randomize each process within it.
- Attach the local boundary to the licensed claim rather than automatically
  relabeling every experimental contrast as an association.

**Quantitative Meaning Check.** Activate this check when a supplied,
consequential quantitative result affects the claim. Before results, activate
only when an explicit planned quantitative inference makes the eventual
reporting schema decision-relevant:

`estimand or contrast -> direction -> magnitude -> precision or compatible range -> justified reference -> scientific meaning -> applicability and claim boundary`

- Use only reported or supplied values and justified reference points. Do not
  calculate missing quantities, invent a smallest effect of interest, or start
  a new analysis.
- Record missing magnitude, precision, or reference information as missing or
  not assessable, not automatically invalid.
- Before results, record only the reporting schema the planned inference would
  need. Do not simulate an estimate or conclusion.

### 3. Apply direct scientific friction

Identify what survives scrutiny so strengths that should be protected remain visible. Present that evidence in the order selected for the deliverable.

For each finding, retain the fields below. Use a Critique Matrix only when the selected form calls for it or the form is open and a matrix serves the deliverable:

| Field | Required content |
|---|---|
| Finding ID | Stable identifier |
| Location | Exact section, statement, table, figure, or decision when available |
| Observation | What is present, missing, inconsistent, or unsupported |
| Basis | Directly observed, source-supported, methodological inference, or unverified concern |
| Threatened inference | What conclusion, comparison, interpretation, or decision is affected |
| Assumptions | Conditions required for the current reasoning to hold |
| Uncertainty and limits | Missing material, ambiguity, source limits, or competing interpretations |
| Impact | One calibrated category with a reason |
| Response options | Defensible clarification, investigation, revision, or handoff options |

Use exactly these impact categories:

- **Inference-blocking**: The supplied object does not currently license a central inference, or essential information is missing such that the inference cannot be evaluated.
- **Materially limiting**: The issue substantially narrows validity, scope, confidence, interpretation, or generalization without invalidating every contribution.
- **Clarification or reporting needed**: Missing or inconsistent information prevents adequate evaluation or reproducibility and may become more serious if unresolved.

Do not assign numerical scores, average findings, count votes, or treat the impact label as an objective verdict. State the reason and uncertainty for every label.

Be direct when an inference is not licensed. Do not soften a scientific error into a vague suggestion. Directness does not authorize choosing the remedy for the user.

For each consequential finding, apply the Smallest-Defensible-Response
procedure inside `Response options`:

`earliest unsupported link -> failure type -> least burdensome scientifically adequate repair -> remaining limitation`

- Preserve the strongest supported contribution. This is not an automatic
  claim-weakening ladder.
- Clarify or report when existing information is merely omitted; verify and
  reconcile when facts or sources conflict; propose a separate analysis
  decision or handoff only when existing data could answer a central question;
  and park or identify a future-study need when the current design cannot
  answer it.
- Defer or park a noncentral concern that does not affect accuracy, a central
  inference, required disclosure, or reproducibility.
- Keep the proposed repair provisional. Research Companion may organize
  user-selected responses in the current scientific frame or an explicitly
  requested roadmap, and the user owns the scientific response.

### 4. Present priority tensions and response options

Summarize the most consequential tensions across the Study Logic Map and Critique Matrix. For each, offer only defensible options and show:

- what the option would address;
- evidence and assumptions supporting it;
- tradeoffs and remaining uncertainty;
- what the option would not resolve;
- the capability that owns any downstream work.

Do not create artificial choices. When only one scientifically defensible boundary remains, state that constraint and explain why.

When a response option concerns a claim, describe the scientific boundary or type of change needed without drafting alternative claim wording. Wording candidates and final selected claim wording belong to [research-literacy](../research-literacy/SKILL.md) after its own approval gates.

List any **Claim-Audit Candidates** by quoting the exact vulnerable claim and explaining why a source-grounded audit may matter. Do not assign [research-literacy](../research-literacy/SKILL.md) evidence statuses or draft alternative claim wording of any status.

### 5. Produce the Provisional Critique Record

Complete the first pass without asking the user to select findings. Preserve the following fields in the provisional record and convey the applicable content in the selected form:

| Field | Required content |
|---|---|
| Research object | Provisional object, version, and scope |
| AI-selected boundary | Intended decision, mode, lenses, evidence boundary, and working assumptions |
| What survives scrutiny | Strengths identified provisionally |
| Priority findings | The most consequential findings supported by the provisional pass |
| Response options | Defensible options and their tradeoffs, without selecting one for the user |
| AI-provisional responses | The AI's recommended provisional response or next question for each priority finding, with its basis, tradeoff, and remaining uncertainty |
| Claim-audit candidates | Exact vulnerable claims when applicable |
| Missing evidence | Material that could change or sharpen the critique |
| Limits | Why the pass is provisional and what was not assessed |

Label the priority findings and recommended responses `Provisional Gate 2 recommendations: AI-selected`. Do not present them as a user disposition, confirmed strength, final selected response, or authorized downstream action. AI prioritization gets the critique moving; it does not become the user's scientific decision.

### 6. Controlled continuation when requested

Finish with the provisional deliverable unless the user requests a controlled pass. Discuss the option only when requested, when the selected response form or applicable verified reporting policy calls for it, or when a concise mention is useful and the task leaves it open. For a file-only memo, reserve a separate continuation discussion for a separate request. The two controls apply when continuing:

1. **Controlled Gate 1:** confirm or revise the object, intended decision, mode, lenses, and evidence boundary.
2. **Controlled Gate 2:** respond to the resulting strengths and findings before a final Critique Response Record is produced.

A provisional deliverable, silence, or approval to save the memo does not authorize a controlled pass.

### 7. Controlled Gate 1: approve the critique boundary

When the user requests a controlled pass, show the provisional brief with any requested changes and ask the user to approve or correct it.

Controlled Gate 1 authorizes only:

- inspection of the displayed research object and supplied sources;
- the displayed mode and lenses;
- the displayed evidence boundary;
- production or refinement of the Study Logic Map and critique outputs.

It does not authorize search, another research object, claim auditing, rewriting, method selection, statistical execution, saving, or a handoff.

If the user changes the object, mode, lenses, intended decision, or evidence boundary, rebuild the brief before proceeding.

### 8. Refine the critique under the approved boundary

Re-run or refine the Study Logic Map, What Survives Scrutiny, Critique Matrix, Priority Tensions and Response Options, and Claim-Audit Candidates under the Controlled Gate 1 boundary.

Reuse provisional material only when it still fits the approved boundary. Clearly identify findings that were added, changed, narrowed, or removed.

### 9. Controlled Gate 2: The user selects the response

Ask the user to confirm which strengths from What Survives Scrutiny should be preserved and to accept, reject, revise, investigate, or hand off each consequential finding.

Controlled Gate 2 authorizes only the confirmed strengths and selected findings for the Critique Response Record. It does not authorize changing the research object, running an analysis, starting another skill, saving, drafting claim wording, or implementing a proposed remedy.

Do not infer selection from silence. If the user rejects a finding, preserve the user's stated reason in the record without silently removing the underlying evidence or uncertainty. If the user's selected response exceeds the evidence, state the mismatch and do not present it as verified.

### 10. Produce and verify the Critique Response Record

After Controlled Gate 2, produce:

| Field | Required content |
|---|---|
| Research object | Approved object, version, and scope |
| Critique mode and lenses | Approved review boundary |
| Evidence boundary | Material inspected and important access limits |
| What survives scrutiny | Only strengths the user confirmed at Controlled Gate 2 |
| Selected findings | Only findings addressed at Controlled Gate 2 |
| The user's disposition | Accept, reject, revise, investigate, or hand off |
| Selected response | Exact user-selected action or next question |
| Evidence needed | Missing material or verification required |
| Owner | The user or the selected downstream capability |
| Prohibited overreach | Claims or actions not licensed by this critique |
| Open items | Unresolved scientific or access questions |
| Provenance | The user's decisions, AI critique, and any user revisions kept separate |

Verify that:

- the record matches the object, mode, lenses, and evidence boundary approved at Controlled Gate 1;
- no question, hypothesis, prediction, method, threshold, model, interpretation, conclusion, or claim was silently chosen;
- every selected entry matches the user's Controlled Gate 2 disposition;
- every recorded strength matches the user's Controlled Gate 2 confirmation;
- observed content, source support, methodological inference, and unverified concern remain distinguishable;
- missing and conflicting information remains visible;
- no [research-literacy](../research-literacy/SKILL.md) evidence status, wording candidate, or final claim wording was duplicated;
- no unapproved search, rewrite, execution, save, or handoff occurred.

## Outputs

Start the provisional critique without stopping for approval. Use the form and order selected for this task, then the applicable verified reporting policy for open choices. When neither specifies a form or order, use a concise report organized around the current decision. Carry the applicable content into that deliverable:

- the provisional object, scope, working assumptions and evidence boundary;
- the Study Logic Map's supported and unresolved links;
- strengths that survive scrutiny and the findings with their required evidence fields;
- priority tensions, defensible response options and remaining uncertainty;
- exact claim-audit candidates when applicable;
- the provisional status and limits of the record.

The brief, map, matrix and provisional record describe the underlying evidence. Use separate display sections only when appropriate to the selected or fallback form. Offer a controlled continuation only under the rule above.

The initial rapid pass should be easy to scan and should normally remain under about 1,200 words. Preserve the full pipeline by compressing repeated material, not by omitting the reasoning needed to support a consequential finding. Targeted and full modes may be longer when the requested scope requires it.

For a controlled continuation, use Controlled Gate 1, refine the critique, use Controlled Gate 2, and then return the **Critique Response Record**. Do not simulate user approval during the controlled pass.

When an invoking companion routed the critique, return the compact
Companion return and writing-relevant packet to that companion as part of
the approved route. Keep the user-facing deliverable within the selected form.
Returning the packet does not authorize writing specialists or another capability.

Return the critique in the selected form or under the applicable verified reporting policy for open choices. When the task authorizes a file-only provisional memo, put the critique in that verified file and return a concise completion status and path in the conversation. Show a separate preview only when the preview rule below applies. The provisional pass, Controlled Gate 1, and Controlled Gate 2 do not authorize saving, modifying a source, searching, downloading, starting another skill, or initiating a handoff. Returning a completed result to an invoking companion is part of the approved route, not a new handoff or authorization to start writing work.

Verify the exact content or change and its destination or recipient before acting. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

For an authorized write, verify and use the destination selected for this task. Otherwise apply the verified placement policy for this project or recipient. If neither resolves it, use an established location for the applicable record or package when it fits the authorized scope. Ask once if the destination remains unresolved.

## Boundaries

- **Several independent research objects**: Separate them and ask the user which one is in scope. An integrated multi-study manuscript may remain one object only with an explicit approved boundary.
- **General paper-critique launch**: Default to a provisional rapid blind-spot scan and continue immediately.
- **Narrow concern named at launch**: Choose a provisional targeted critique around that concern and continue immediately.
- **Full critique named at launch**: Run a provisional full scientific critique without asking the user to select lenses first.
- **Provisional boundary is imperfect**: Keep the initial findings clearly provisional and finish the requested deliverable. Apply the continuation rule above if the user wants to refine the boundary.
- **Incomplete or inaccessible methods or supplement**: Limit the critique and record `not assessable from supplied material` under Uncertainty and limits. Use one of the three impact categories for any finding and do not infer the missing scientific content.
- **Abstract-only evidence**: Critique only what the abstract permits. Do not infer unreported methods, estimates, analyses, or limitations.
- **No supplied evidence**: Critique internal logic only. Do not make evidence-based novelty, feasibility, or validity claims.
- **Unknown preregistration or outcome visibility**: Mark the status `unknown`. Do not infer confirmatory standing.
- **Conflicting sections, tables, or figures**: Preserve the conflict and its locations. Do not silently choose one account.
- **Causal overclaim**: State directly when the supplied design does not license causal wording.
- **Experimental condition effect**: Before downgrading a causal claim, inspect
  manipulation, assignment, unit, timing, counterbalancing, interference, and
  bundled components. Preserve a supported condition-level effect while
  withholding unsupported mediator, participant-behavior, or mechanism claims.
- **Historical study**: Distinguish what the original design and report license
  from what a current reuse or redesign would require. Do not silently
  modernize the method or treat current reporting expectations as though they
  were part of the original protocol.
- **Current-method update**: Route current-source verification and prospective
  method selection to the applicable search, design, or analysis owner. The
  conditional inference checks do not establish current best practice. When
  more than one owner is plausible, return the routing ambiguity to the
  invoking companion or offer [research-companion](../research-companion/SKILL.md) in a direct session; do
  not select a method owner silently.
- **Difference from significance labels**: Require the direct contrast or interaction rather than comparing one significant result with one nonsignificant result.
- **Nonsignificant result**: Do not describe it as marginal, approaching significance, a trend, or nearly supported. Do not treat it as evidence of absence.
- **Only one defensible response**: State the constraint instead of inventing alternatives.
- **The user asks for a final answer or remedy**: Give the strongest evidence-bounded critique directly, but preserve the user's selection of the scientific response.
- **Selected response exceeds the evidence**: Preserve the critique and disclose the mismatch. Do not label the response verified.
- **Evidence boundary expands during a controlled pass**: Rebuild the Research Critique Brief and repeat Controlled Gate 1.
- **Writing or implementation request**: If a companion invoked the critique,
  return the writing-relevant packet to it and stop. Otherwise prepare the
  bounded handoff and wait for separate approval.
- **Generic feedback request**: Do not activate this skill from a vague feedback phrase alone.
- **Context compaction or model switch**: Reload this skill, the exact bounded
  research object, and the current Critique Brief before continuing. Preserve
  whether the boundary is provisional or Controlled Gate 1 approved rather
  than treating an AI-selected provisional boundary as user approval.

## Handoffs

When an invoking companion routed this capability, return every completed
result to that companion, including a provisional pass, controlled pass, or
bounded result limited by missing evidence. Do not start [writing-companion](../writing-companion/SKILL.md) or
another capability.

Give the invoking companion a compact return packet containing:

- research object, version, and writing unit when identifiable;
- critique status: provisional or controlled;
- strengths that survived scrutiny, labeled provisional unless the user confirmed
  them;
- each writing-relevant finding and its status: provisional, accepted,
  rejected, revised, investigate, hand off, or unresolved;
- The user's reason for a disposition when supplied;
- prohibited overreach;
- terminology and construct constraints supported by the critique;
- evidence and citation boundary;
- missing evidence and unresolved scientific decisions;
- invoking companion and return owner.

Provisional findings and AI-selected recommendations remain nonbinding.
Preserve rejected findings with their evidence, uncertainty, and the user's reason,
but do not implement them as writing instructions. Only user-confirmed
strengths and user-selected responses may inform the current scientific frame
or an optional Research Writing Roadmap.

When the user selects a claim for [research-literacy](../research-literacy/SKILL.md), prepare this packet:

| Field | Required content |
|---|---|
| Exact primary claim | Verbatim or faithfully transcribed wording |
| Linked subclaims | Only subclaims required to support, qualify, or interpret the primary claim |
| Intended use and audience | Where and why the claim will be used |
| Claim types | Descriptive, associational, causal, predictive, mechanistic, generalizing, comparative, absence, or other |
| Supplied evidence | Exact sources already available |
| Evidence boundary | Material the user permits the audit to inspect |
| Outcome visibility | What outcomes were known when decisions were made |
| Confirmatory status | The user's stated status and basis |
| Preregistration and deviations | Relevant protocol, plan, timing, changes, and reasons |
| Thresholds and rules | Applicable decision rules supplied by the user |
| Unknowns | Missing facts that may limit the audit |

Show the complete packet and ask for separate approval before starting [research-literacy](../research-literacy/SKILL.md). That skill then begins with its own Claim Audit Brief and Gate 1. Do not treat Research Critique approval as Research Literacy approval.

Boundaries and handoffs:

- Use [research-literacy](../research-literacy/SKILL.md) to audit one explicit claim bundle against bounded evidence and produce calibrated evidence statuses and user-selected wording.
- Use [research-companion](../research-companion/SKILL.md) for broad framing, strategic comparison, project triage, or manuscript strategy.
- Use [scientific-brainstorming](../scientific-brainstorming/SKILL.md) for explicit structured divergence and connection mapping.
- Use [research-summarizer](../research-summarizer/SKILL.md) to explain one bounded paper rather than independently critique the full research object.
- Use [paper-search](../paper-search/SKILL.md) when the evidence need requires broader discovery, citation expansion, gap checking, or novelty checking.
- Use [writing-companion](../writing-companion/SKILL.md) for publication-facing drafting and revision, and check-research-reporting for formal reporting-guideline audits. Requested prose review does not automatically launch a scientific critique.
- If an invoking companion routed this capability, return every successful,
  boundary-limited, or unresolved result to that companion. If no companion
  invoked it, stop at this capability boundary and offer
  [research-companion](../research-companion/SKILL.md) only as an optional public routing entry.
- Route statistical execution or method implementation to the relevant approved Part 4 capability. If none is Active, disclose the gap and stop.
- Route prediction-centered falsifiability analysis, counterexamples, bounded novelty assessment, and prospective stress testing to [prediction-stress-test](../prediction-stress-test/SKILL.md) through a separately approved handoff.
- Route prospective construction or comparison of design structures to [experimental-design](../experimental-design/SKILL.md) through a separately approved handoff.
- Route prospective comparison of cognitive or behavioral paradigm architectures and construct operationalizations to [cognitive-paradigm-design](../../specialized_skills/cognitive-paradigm-design/SKILL.md) through a separately approved handoff.
- Route prospective administration design for an already-selected Alternative Uses Task to [alternative-uses-task-designer](../../specialized_skills/alternative-uses-task-designer/SKILL.md) through a separately approved handoff.
- Route deterministic layout-manifest generation for an approved controlled-array visual-search task to [visual-search-array-generator](../../specialized_skills/visual-search-array-generator/SKILL.md) through a separately approved handoff.
- Route model-aware timing design for an approved task-fMRI estimand and proposed first-level model to [fmri-task-design-guide](../../specialized_skills/fmri-task-design-guide/SKILL.md) through a separately approved handoff.
- Route prospective MRI neuroimaging power-method and input specification to [neuroimaging-power-guide](../../specialized_skills/neuroimaging-power-guide/SKILL.md) through a separately approved handoff.
- Route numerical execution of an approved MRI-specific Power Inputs Specification to [neuroimaging-sample-size-calculator](../../specialized_skills/neuroimaging-sample-size-calculator/SKILL.md) through a separately approved handoff.
- Route prospective cognitive or behavioral participant, item, trial, reliability, data-loss, or effect-evidence input specification to [cogsci-power-analysis](../../specialized_skills/cogsci-power-analysis/SKILL.md) through a separately approved handoff.
- Route prospective quantitative power, sample-size, MDE, or operating-characteristic calculation from approved inputs to [statistical-power](../statistical-power/SKILL.md) through a separately approved handoff.
- Route version-pinned BIDS curation, metadata-inheritance, provenance,
  privacy-boundary, or compliance specification to [bids](../../specialized_skills/bids/SKILL.md) through a
  separately approved handoff.
- Route prospective computational architecture, objective, leakage,
  validation, baseline, or ablation specification to [method-design](../method-design/SKILL.md) through
  a separately approved handoff.

This skill does not search, rewrite the source, draft alternative claim wording, generate a hypothesis, choose a design, method, threshold, or model, execute statistics, adjudicate novelty, verify a claim's evidence status, or make a scientific conclusion for the user.

## References

- Cornell Engineering Communications Program. (n.d.). *Toulmin model of argument* [PDF]. https://courses.cit.cornell.edu/engrwords/handouts/Culver_Hu_Rubin_Tundo_TMI_Handout.pdf
- Harvard College Writing Center. (n.d.). *Counterargument*. https://writingcenter.fas.harvard.edu/counterargument
- Harvard Law School Institute for Global Law and Policy. (n.d.). *The IGLP approaches*. https://iglp.law.harvard.edu/the-iglp-approaches/
- Oxford Centre for Evidence-Based Medicine. (n.d.). *Critical appraisal tools*. https://www.cebm.ox.ac.uk/resources/ebm-tools/critical-appraisal-tools
