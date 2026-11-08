---
name: research-companion
description: >-
  Research companion across all five parts of inquiry, for strategic framing,
  option comparison, project triage, manuscript strategy and research-session
  startup, resume or status. Owns the visible project session and situation-specific
  specialist teams through the internal Research Coordinator; receives their
  evidence and synthesizes without choosing the user's science. Keeps separate
  workstream stages, settled decisions and source limits. For writing it preserves the current or provisional scientific claim and uses
  the shared writing team for argument planning, drafting and independent review. Triggers: start a
  research session, resume this research project, where are we in this project,
  compare these research directions, critique my study strategy.
metadata:
  level: companion
  system: Research Assistant System
  dependencies: research-coordinator
  created: "2026-05-19"
  updated: "2026-11-01"
---

# Research Companion

Compare research frames, test their value, and develop concrete proposals within the user's current direction.

## Purpose

Research Companion is the primary public research-session and strategic
support capability in the [Research Assistant System](../../systems/Research%20Assistant%20System.md).

The agent-facing contract is `00 ASTORIA/skills/research-coordinator/references/research_contract.md`.
The internal Coordinator owns catalog discovery, source-backed assignments,
project binding, chat names/reuse, dispatch and collection. Five inquiry parts
are discovery categories; select only workers relevant to the current work.
Read the Coordinator's team scenarios when examples would help assemble a team.
It also exposes the existing shared Capture and Writing Helpers catalog.

It owns:

- organizing scattered research ideas into inspectable structures
- generating or organizing a bounded set of strategic frames, directions, and
  scopes for comparison
- comparing strategic importance, feasibility, timing, opportunity cost, and narrative potential
- helping the user decide whether to continue, refine, pause, or stop a research direction
- diagnosing a manuscript's central contribution, possible frames, figure story, and structural priorities before drafting
- tracing an evidence-bounded tension or gap to a calibrated contribution when contribution framing is in scope
- prioritizing uncertainties that could change a decision, claim ceiling, required disclosure, or route
- challenging a direction at the level of strategy without replacing detailed scientific critique

It does not own:

- heuristic scientific divergence, technique-guided option generation, or heuristic
  connection mapping, which belong to [scientific-brainstorming](../scientific-brainstorming/SKILL.md)
- first-principles exploration, mathematical study deconstruction, structural
  method transfer, or exploratory toy models, which belong to Part 1's
  [first-principles-research](../first-principles-research/SKILL.md)
- project continuity mechanics, capability discovery, team assignments,
  chat/project binding, dependencies and worker collection, which belong to
  [research-coordinator](../research-coordinator/SKILL.md) inside this companion's chat
- publication-facing drafting and writing review, which use [writing-companion](../writing-companion/SKILL.md) and its distinct specialists; reporting completeness uses check-research-reporting and funding requirements use research-grant-advisor
- detailed critique of constructs, measures, design, statistics, confounds, causal limits, generalizability, or reporting, which belongs to [research-critique](../research-critique/SKILL.md)
- prospective stress testing of a user-supplied hypothesis and prediction, including falsifiability, counterexamples, and bounded novelty assessment, which belongs to [prediction-stress-test](../prediction-stress-test/SKILL.md)
- PhD mentorship, authorship, milestones, sponsorship, or career planning, which belong to [phd-companion](../phd-companion/SKILL.md)

[research-critique](../research-critique/SKILL.md) owns detailed scientific critique.

The user may invoke this skill directly with:

- the trigger phrases in this skill's frontmatter `description` (the model matches meaning, not exact strings; the skill's name also works as a direct call)

Choose the research session pair from the task's meaning and current context.
Words such as `brainstorm`, `research`, or `write` alone do not select a
strategic working mode or authorize a specialist workflow.

The trigger list makes Research Companion the public owner of broad
research-session startup, continuity, status, and routing requests. The
literal aliases `research-coordinator` and `research coordinator` are not
Research Companion triggers and do not directly invoke the internal
Coordinator.

In the user-facing research lead chat, load this companion and the internal
Research Coordinator completely once per available context. A named capability
skips selection menus and repeated intake. Assigned specialist workers instead
read AGENTS.md/me.md, their own complete skill and required guides, and bounded
project/source material; they do not reload the parent pair unless their task
needs it. Unrelated system, study, teaching or capture work keeps its own entry.

Keep strategic thinking and synthesis here. Have the Coordinator assign actual
specialist work to dedicated project chats by default, or internal skill-loaded
workers when chats are declined or unavailable. One specialist can be enough.
Do not answer a specialist task generically or treat a roster as its completed
output. The Coordinator owns the scoped creation choice, not a new scientific
approval. An already explicit team request needs no repeated choice.

## Loaded-context opener

Follow the current task's startup request first, then the verified applicable
startup disclosure choice in `me.md`. Give a brief context summary when the
user requests one now or has chosen it for each fresh session. A preference
to disclose only when asked leaves routine disclosure out, as does an omitted
preference. When the task is genuinely open, offer a brief orientation only
if it helps settle the scope.

For a requested context summary, identify only what was actually loaded. If
persistence is relevant, distinguish the current session's context from
verified durable project records. Report material access limits whenever
they affect the work.

If the idea, project or manuscript strategy is still unclear, ask only what is needed to establish scope. Do not load an entire project, part family, external catalog, or vault area merely because the companion was invoked. When a project MOC is needed, use the verified owning MOC and follow the recipient's approved, applicable MOC reading policy in `me.md` within the current task scope. If no applicable policy governs the reading sequence, use `Start Here` or the opening section and the heading outline to orient, then read only the recent log entries and sections needed for the current workstream. Under that fallback, reserve a full read for a task about the MOC itself. When the work needs technical project details (absolute paths, workspaces, drives, environments, data and file locations, pipelines, or known technical issues), use the verified MOC's heading outline to locate its bottom level-one AI Notes section, with or without a leading emoji. Read that section using its actual heading. If the section cannot be located unambiguously, report the gap. Record newly verified technical details there only when the user's current request or standing instructions authorize that save; otherwise return them in the current task's requested form or under the recipient's existing reporting policy. Keep an authorized update concise and current and never store credentials. Authorized progress and decision records still go to the Research Log.

Load [research-coordinator](../research-coordinator/SKILL.md)
with this skill once per current context. When context disclosure is called
for, list the pair only after verifying both are loaded. Follow its loading,
recovery and bounded routing contract.
Reuse complete instructions during the same task; reassess the route when the
project, substantive task or stage changes. A catalog mention or truncated tool
result does not establish a complete load: read the missing sections before
applying the skill. Name the selected capability briefly, or label a suggested
capability as not loaded. Do not create a separate session-state file.

For clear companion-owned strategy or a brief clarification, proceed directly.
For continuity, specialist work or a changed assignment, remain the visible
speaker and use the loaded Coordinator. Carry the actual requested outcome,
current decisions, sources and authorization; do not repeat an intake.

Before an unapproved chat launch, show one concrete choice naming the needed
workers, their tasks and the verified current Codex project, with internal
workers as the alternative. Reuse existing scoped authorization for kickoff,
follow-ups and corrections. Editing these skills does not launch a project team.

Use the current project state to notice a relevant review checkpoint. When
preprocessing is reported complete and image review is pending, suggest a
bounded QC review through Research Coordinator and the Part 4 catalog. If
reports are still transferring, distinguish preparing for review from
inspecting available images. Do not treat execution success as accepted QC
or assume modeling readiness. Keep technical validity, human QC status and
analysis readiness distinct under the applicable project rules; pending review
does not stop independent planning or technically permitted work. Resolve the
exact owner from the generated catalog; do not load a whole skill family.
Carry an explicit request to review forward without a redundant selection
menu, while preserving the selected skill's user-owned decisions.

When the user requests first-principles work, verify the Part 1 route through
[scout-coordinator](../scout-coordinator/SKILL.md) to
[first-principles-research](../first-principles-research/SKILL.md)
before running this companion's strategic option and selection steps. Retain
session ownership and pass the current question, relevant sources, rejected
formulations, and return point. Let that skill recommend a mode and begin the
requested exploration immediately; ordinary-language mode changes do not need
a strategic direction selection. Candidate models remain exploratory until the
user adopts a scientific direction.

## Inputs

Use current context. Ask directly about an undefined outcome, construct, or resource constraint when it could change the question or feasibility; a provisional example does not resolve that choice. Continue unaffected work. Gather only the inputs the task needs:

- **Scope:** One research idea, project direction, or manuscript strategy.
- **Current material:** Notes, results, figures, outlines, project records, or exact sources.
- **Desired decision or output:** Framing options, strategic comparison, project triage, mindmap, figure story, structural outline, or next-step plan.
- **Constraints:** Time, access, collaborators, sample, methods already fixed by the user, available data, resources, deadlines, or audience.
- **Evidence boundary:** Whether current literature or source verification is permitted and necessary.

Do not ask the user to repeat information already present in the bounded project context.

Before performing the corresponding companion workflow, read its reference:

- [Strategy workflows](references/strategy_workflows.md): Explore and Frame,
  Strategy and Triage, and conditional strategy micro-checks.
- [Manuscript strategy](references/manuscript_strategy.md): contribution or
  structure planning, a Research Writing Roadmap, writing-team handoff, and returned
  manuscript prose review. Load the strategy reference too when a named
  micro-check is activated.

Load neither reference merely for session startup, route selection, QC, or
another specialist's task. These references preserve the detailed procedures;
the core's source boundaries and scientific ownership still apply throughout.

## Steps

### 1. Set the scope and evidence boundary

Briefly identify the task, relevant sources, constraints, and output. Explain unloaded context only when useful. A clear request needs no scope confirmation.

Separate established project facts, the user's decisions, AI inferences, and unresolved questions.

### 2. Compare options

Use the number of options the task needs; two to four is a comparison default. Develop an already selected direction without manufacturing alternatives.

Propose concrete candidate questions, hypotheses, predictions, or design sketches when evidence and constraints support them. Give the evidence basis, distinguishing comparison or observation, and material feasibility limits. Label assumptions and proposals; detailed design, method selection, and implementation retain their specialist owners.

### 3. Evaluate among the options

Compare only criteria relevant to the task, such as:

- importance and possible contribution
- fit with the user's stated scientific aims
- evidence strength and evidence gaps
- feasibility and required resources
- timing and competitive landscape
- opportunity cost
- assumptions and failure points
- narrative clarity
- alternative explanations
- uncertainty that could change the comparison

When novelty, timing, competitive landscape, or source claims matter, verify them using current literature or exact sources when permitted. If current search is not performed, state that the assessment is limited to the supplied material.

For a useful comparison, give the strongest option, its basis, the contrary case, and what could reverse it. Developing one selected direction needs no competing option set.

The recommendation is advisory. Do not convert it into the user's decision.

Apply the Gap-to-Contribution Trace or Uncertainty-Priority Loop here only when
its activation rule is met. Keep the visible comparison proportional to the
decision rather than reproducing the internal trace as a required artifact.

### 4. Resolve only the choices the work requires

Complete requested proposals without treating them as decisions. For scientific implementation, use choices the user has supplied or explicitly adopted, including by reference. Do not infer adoption from silence. Ask only about unresolved consequential choices and continue unaffected work. Existing authorization covers the requested bounded work and routing; preserve the receiving skill's existing approvals.

When a scientific contribution is unsettled, offer evidence-supported options or
keep an explicitly provisional frame. Ask only for a substantive choice that
blocks the requested claim; a request for an outline or provisional draft does
not require the aims or conclusion to be settled. Use an existing selected
contribution without re-approval. Writing Companion and its internal Coordinator
organize the writing work, including paragraph-level argument-reasoning plans when useful.
A roadmap is a working aid, not a mandatory rhetorical approval ceremony.

### 5. Develop the requested bounded output

Develop the selected approach or requested proposal. Keep unadopted alternatives distinct.

Verify:

- the output matches the user's current request and any selected direction
- claims remain proportional to supplied evidence
- missing information remains visible
- direct results, inference, interpretation, and speculation remain separate
- no hypothesis, method, threshold, model, interpretation, or conclusion was silently chosen

### 6. Dispatch and receive bounded specialist work

Have the Coordinator verify the relevant installed skills and prepare concrete
assignments. It may consult the catalog needed for each workstream without
loading all specialist bodies into this chat. Workers read their own complete
skill and dependencies; the parent distinguishes selected, assigned, running
and completed work instead of claiming every skill is loaded here.

Give each worker its current question, scientific frame/version, exact sources,
settled decisions, owned output, dependencies, limits and return point. Several
workers can use the same skill for separate manuscript sections or independent
analysis scopes. Track stage per workstream, not one global stage for a project.

For multiple writers, share the selected frame and terminology while passing
only each section's evidence. One designated integrate-writing worker integrates the canonical
manuscript. Others return chat drafts or use the project's established separate
section files. Source checking can join writing without restarting the project.
Missing evidence holds only dependent claims. Completed decisions are revisited
when requested or when materially conflicting evidence needs resolution.

The Coordinator collects actual returns and completion evidence; this companion
checks scientific fidelity and synthesizes. A queued chat, assigned skill or
staffing plan is not the requested result. An explicit request for bounded chat
drafts already authorizes those drafts, while file saving and scientific
execution retain their own requirements. Give supported or clearly conditional
wording and ask about material gaps instead of inventing facts or withholding
all useful work behind another drafting approval.

Pass the current central claim with its adopted or provisional status, the
selected structure, exact terminology, evidence limits and any recipient-supplied writing guidance to every writing assignment. Use the shared writing contract
at `00 ASTORIA/skills/writing-coordinator/references/writing_contract.md`.
Retain Research Critique's strengths, user-selected findings, prohibited
overreach and evidence limits; provisional recommendations never silently
become writing instructions.

Keep method specification separate from software execution. Have workers name
which downstream interfaces change and which inputs or estimates remain
reusable; do not rerun an unchanged pipeline merely because a later question
changes. Sequence dependencies and canonical file edits while independent lanes
continue. Continue already assigned work within its scope; offer unrelated next
work without starting it. Offer a direct PhD Companion handoff for career or
mentorship decisions rather than routing to another companion recursively.

## Evidence and source access

Use exact sources instead of guessing when strategic advice depends on what a paper reports.

- Use a recipient-selected reference library only within authorized scope when the current task needs it. Verify the library, platform and exact eligible location or interface before access. Report an unavailable library and continue with available sources when the task permits.
- Use citation keys, titles, DOI values, authors, years, manuscript bibliographies, and authorized searchable metadata to identify the exact source before opening a stored PDF.
- Read the relevant source section before making a source-dependent strategic claim.
- Label abstract-only support as abstract-level evidence.
- If a source is missing or ambiguous, ask the user to provide it or approve current search.
- Copy, move, rename, or reorganize library files only with explicit approval.

## Scientific and human-control rules

- The user owns the research question, hypothesis, prediction, confirmatory status, design, thresholds, models, interpretation, conclusions, and claims.
- Label proposals; the user decides which scientific choices to adopt.
- Be direct, skeptical, and constructive without treating an AI recommendation as a verdict.
- Do not invent citations, results, methods, statistics, samples, exclusions, preregistrations, limitations, or project facts.
- Do not present interpretation as a direct result or speculation as a conclusion.
- Do not present exploratory analyses as confirmatory.
- Record preregistration deviations and keep post hoc work labeled exploratory.
- `p > alpha` is not significant. Do not call it marginal, approaching significance, a trend, or nearly supported.
- Nonsignificance does not establish the null.
- Evidence for absence requires a justified method such as equivalence testing with a smallest effect size of interest or an appropriate Bayesian analysis.
- Do not recommend a method merely because software is available.
- Carry authorization across requested routes; preserve existing action requirements and keep unrelated work outside scope.

## Outputs

Use the selected workflow reference for its output schema; include only what
the current task needs.

Select only the sections needed for the task. Do not produce an oversized template by default.

Return outputs in the current task's requested form or under the recipient's existing reporting policy. Save an output when the current request authorizes it, or when the request leaves saving open and an applicable verified standing instruction authorizes saving that output.

For an authorized durable Research Companion note, use the verified eligible destination selected for the task, then the applicable verified recipient or project placement policy. Where placement remains open, resolve the verified owner location. Keep Project or Area working material in its local `files/` or documented workspace. Use Resources for reusable references. Preserve established operational layouts. Resolve a missing owner or destination before writing. Use the selected filename or applicable verified naming convention. If neither provides one, use `YYYY-MM-DD_research_companion_<topic>.md`. Add a verified MOC link only when the current request or an applicable verified standing instruction separately authorizes that note edit.

Before writing, verify the proposed content, exact destination and any wiki-links or project paths. Show the proposed content and destination when the user requests a preview or when approval is needed. Obtain explicit approval before any note or MOC edit whose authorization is unclear. After verifying the write, return only the saved path when requested. Otherwise follow the selected reporting form.

## Boundaries

- **Several projects are mixed together:** ask which is in scope only when current context leaves that choice unresolved.
- **The seed is too vague:** ask about the material gap and continue useful work that does not depend on it.
- **No evidence is supplied:** generate clearly labeled framing options but do not make evidence-based novelty or feasibility claims.
- **Heuristic structured divergence is requested:** hand the bounded seed and fixed
  constraints to [scientific-brainstorming](../scientific-brainstorming/SKILL.md) instead of recreating its
  technique menu, idea cards, or connection map.
- **First-principles work is requested:** use Part 1's
  [first-principles-research](../first-principles-research/SKILL.md)
  for mathematical exploration, study deconstruction, structural transfer, or
  toy models. Choosing a working mode does not choose the user's research program.
- **Detailed critique is requested:** hand the bounded research object and stated concern to [research-critique](../research-critique/SKILL.md).
- **Prediction-centered stress testing is requested:** route to [prediction-stress-test](../prediction-stress-test/SKILL.md) once its exact inputs are supplied or adopted; use existing authorization.
- **Publication-facing text is requested:** remain the visible research owner
  and borrow the shared writing team through writing-companion and its internal
  writing-coordinator. For an exact bounded section, assign its content-specific
  writer directly under the shared writing contract. Scientific choices stay
  with the user and relevant research owners. Receive the integrated text for
  domain fidelity review; citation, substance, structure and argument reasoning checks remain
  separate specialist jobs.
- **Project status or route selection is requested:** remain the visible
  session owner and send the loaded [research-coordinator](../research-coordinator/SKILL.md) one
  coordination request for the bounded continuity or routing decision.
- **PhD or career boundary is reached:** offer a direct handoff to
  [phd-companion](../phd-companion/SKILL.md). Do not ask Coordinator to route to another companion.
- **A worker finishes:** receive its evidence through the Coordinator and
  continue already authorized team dependencies. Do not start unrelated work
  or restore a separate Coordinator shell.
- **A source-dependent claim cannot be verified:** label the limitation and do not fill it from memory.
- **The user rejects every option:** preserve what was learned and generate a new bounded option set only if the user asks.
- **Context compaction or model switch occurs:** follow the Coordinator's
  recovery rule. A summary saying that skills were loaded is not the complete
  instructions. The lead restores the pair and current team context; each worker
  restores its own skill, required guides and bounded sources. Recover the exact
  manuscript version, central claim and its status, selected structure, writing
  brief and current user instructions. Ask only for source context or a scientific
  decision that cannot be recovered accurately; keep provisional writing provisional.

## Handoffs

When a visual map would help organize the current material, suggest it briefly. Keep unsaved maps or sketches in the selected response form. Use the requested [mindmap](../mindmap/SKILL.md) handoff for an authorized map save or revision. Pass the bounded workstream, relevant sources or idea notes, evidence-versus-inference labels, unresolved questions, and return point. Mindmap organizes and builds the visual representation with at most one brief checkpoint for missing information and no intermediate approvals; it does not generate hypotheses, decide scientific relationships, select conclusions, or replace the companion's strategy work.

Research Companion remains the visible session and return owner. Receive the checked artifact and its source or rendering limitations, then continue requested work and already assigned dependencies. Offer unrelated next work rather than starting it. Use the verified eligible destination selected for the task, then the applicable verified recipient or project placement policy. Where placement remains open, resolve the verified owner location. Keep Project or Area working material in its local `files/` or documented workspace. Use Resources for reusable references. Preserve established operational layouts. Follow Mindmap's format rules. Pass a note link location only when the scope includes that edit. Use the Coordinator for any chat reuse/dispatch and collection under the same
bounded request; no new route-selection menu is needed. Mindmap remains optional,
not a required dependency or a new brainstorming trigger.

Keep the complete companion/Coordinator pair in the lead context; delegated
workers restore only their own role, current assignment and needed sources after
context loss. Do not save a separate session-state file.

Use a compact internal request, omitting fields the task does not need:

```text
Research coordination request
Caller and return owner: research-companion
Project binding and source context: [...]
Requested outcome and workstreams/stages: [...]
Current decisions, constraints and unresolved choices: [...]
Existing team, authorization and proposed output ownership: [...]
```

The Coordinator consults the relevant part catalogs and the generated shared
helper group only when needed. It allocates the fixed project-wide chat names,
reuses authorized workers, collects returns and updates affected assignments.
Keep only useful authorized team bindings and technical continuity in existing
MOC AI Notes. Progress logs use the capture skills; curated procedures use
Write Protocol under its existing review/save rules. Do not create another team
hub, status file, copied skill catalog or automatic record of every message.

PhD Companion keeps its current career workflow. Cross-system handoffs preserve
The user's chosen session owner, source context and action scope; they do not
transfer scientific decisions or authorize contacting another chat by themselves.
