---
name: literature-synthesis
description: >-
  Builds one bounded critical theory synthesis from supplied sources or an
  explicitly approved literature search. Use when the user invokes
  literature-synthesis or literature synthesis, or when a verified Research
  Coordinator handoff selects it for one bounded multi-source synthesis task. It
  organizes multiple theories or perspectives, maps supporting and contradictory
  evidence, compares approved pairings, and produces a calibrated ranked table
  with ties or unrankable entries when warranted. This is not a systematic
  review, scoping review, single-paper summary, general paper search, or
  manuscript-writing workflow. Triggers: synthesize these papers, build a theory
  synthesis from these sources.
metadata:
  level: skill
  system: Research Assistant System
  part: "1"
  family: literature
  modality: any
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-06-22"
  updated: "2026-11-01"
---

# Literature Synthesis

Build a transparent critical synthesis of theories and evidence without disguising a bounded narrative review as a systematic one.

## Purpose

Use this skill when either:

- The user explicitly says `literature-synthesis` or `literature synthesis`; or
- a verified [research-coordinator](../research-coordinator/SKILL.md) handoff selects this capability for one
  bounded multi-source critical theory synthesis.

A coordinator handoff counts as invocation only for that one bounded task. It
does not approve a search, comparison, ranking, saving, or handoff, and it does
not bypass Gate 1, Gate 2, source requirements, stop points, or verification.

Use it for one bounded topic that requires multiple theories, mechanisms, perspectives, or evidence bodies to be organized and compared.

Do not use it for:

- one-paper explanation, which belongs to [research-summarizer](../research-summarizer/SKILL.md);
- broad research framing or project strategy, which belongs to [research-companion](../research-companion/SKILL.md);
- manuscript prose, which belongs to [writing-companion](../writing-companion/SKILL.md);
- preparing bounded material for another AI chat or reviewing returned chat material, which belongs to [chat-handoff](../chat-handoff/SKILL.md);
- an ordinary request to find papers;
- a systematic review, scoping review, meta-analysis, or other formal evidence-synthesis design.

If the user requests a formal review type, stop and explain that this skill is not that protocol.

Every run produces a **critical theory synthesis**.

- It may address broad, abstract, or theory-oriented questions.
- It may combine empirical, theoretical, methodological, and review sources when the approved frame requires them.
- It evaluates patterns, contradictions, mechanisms, boundaries, and explanatory alternatives.
- Its search is bounded by the approved plan and stopping rule.
- It does not claim exhaustive coverage, systematic-review status, scoping-review status, or PRISMA compliance.
- It does not treat SANRA as a conduct protocol or use its score.

State this product identity and its coverage limits in every final synthesis.

## Inputs

Gather only what is missing:

- topic and primary synthesis question;
- intended use and audience;
- field and subfield;
- seed theories, mechanisms, or perspectives;
- seed papers, citations, links, files, or supplied corpus;
- populations, models, methods, measures, and levels of analysis;
- historical and current year boundaries;
- inclusion and exclusion boundaries;
- approved source locations or search services;
- desired depth and time constraints;
- known disagreements, null findings, or literatures that must not be omitted.

Do not ask the user to repeat information already present in the bounded request.

## Steps

### 1. Prepare the research and search brief

Create:

```markdown
## Critical Synthesis Brief

- Topic:
- Primary question:
- Intended use:
- Included perspectives or seed hypotheses:
- Populations, models, methods, measures, and levels:
- Date boundaries:
- Inclusion boundaries:
- Exclusion boundaries:
- Supplied sources:
- Proposed search locations:
- Exact search concepts and query variants:
- Search limits:
- Stopping rule:
- Known coverage risks:
- Desired depth:
- Provisional comparison and ranking criteria:
```

The stopping rule must be observable. Examples include completing the approved queries, reaching the approved date or source limit, or completing a user-supplied corpus. Do not use an invisible claim such as "search until the literature is complete."

#### Gate 1: Approve the brief before searching

Show the brief and ask the user to approve or revise it.

Before approval:

- do not search;
- do not silently broaden or narrow the question;
- do not add inclusion or exclusion rules;
- do not commit to a theory taxonomy;
- do not begin comparison or ranking.

Gate 1 authorizes only the approved search, source inspection, evidence capture, and provisional evidence map. It does not authorize final comparison, ranking, saving, or handoff.

### 2. Search or inspect the approved source set

Use only the approved sources and search plan.

- Search only when Gate 1 explicitly authorizes it.
- Record what was actually searched instead of reconstructing a plausible search later.
- Prefer traceable primary empirical sources for empirical claims.
- Use reviews and theory papers for orientation, terminology, history, and source discovery without treating them as substitutes for the underlying evidence.
- Verify titles, authors, years, identifiers, and links before relying on them.
- Do not use citation counts as evidence that a perspective is correct.
- Do not automatically inspect unrelated ASTORIA notes, projects, or source collections.

Maintain a search record:

| Field | Record |
| --- | --- |
| Search date | Exact date |
| Source or service | Database, index, website, supplied corpus, or user-named location |
| Query | Exact query or faithful query record |
| Limits | Dates, language, source types, populations, methods, or other applied constraints |
| Selection basis | Approved inclusion and exclusion boundaries |
| Coverage | What was inspected and what remained unavailable or undersearched |
| Stopping rule | Approved rule and whether it was reached |

Report counts only when they were actually tracked.

### 3. Build the source-level evidence ledger

For each source used as material evidence, capture:

| Field | Meaning |
| --- | --- |
| Source | Verified citation and stable identifier or link |
| Verification | Full text, selected sections, abstract only, metadata only, or unverified |
| Source type | Empirical, theoretical, methodological, review, commentary, or other |
| Population or model | Relevant participants, species, model, or corpus |
| Method and measure | Design, method, outcome, construct, and relevant analysis |
| Reported finding | What the source directly reports |
| Author claim | How the authors interpret the finding |
| Synthesis role | Supports, contradicts, complicates, distinguishes, or supplies context |
| Limitations | Source-reported and source-visible constraints |
| Relevance | Why the source matters to the approved synthesis question |

Keep direct findings, author claims, and AI synthesis separate.

Use `Not reported in the available material` when a required detail is unavailable. Abstract-only evidence must remain labeled abstract-only.

### 4. Build a provisional taxonomy and evidence map

Organize three to seven theories, mechanisms, or perspectives when the literature supports that many. Do not force the requested number if the source set supports fewer.

For each perspective, record:

- core claim;
- mechanism or explanatory structure;
- level of analysis;
- distinctive predictions;
- expected supporting and disconfirming evidence;
- strongest current support;
- strongest contradiction or anomaly;
- construct and measurement issues;
- boundary conditions;
- unresolved questions;
- coverage limitations.

Preserve the user's seed perspectives as candidates, but label the taxonomy provisional and revise it when the approved evidence requires merging, splitting, renaming, adding, or removing a category.

Build a compact evidence map:

| Perspective | Strongest support | Strongest challenge | Distinguishing evidence | Coverage |
| --- | --- | --- | --- | --- |

Do not rank the perspectives yet.

### 5. Present the comparison plan

Show:

- the completed search record and coverage statement;
- the source-level evidence ledger or a bounded preview with a complete source list;
- the provisional taxonomy;
- the evidence map;
- proposed pairings or group comparisons;
- unresolved source and construct gaps;
- proposed ranking criteria;
- any perspective that may be unrankable.

Default ranking criteria:

- directness and relevance of empirical support;
- methodological robustness of supporting and opposing studies;
- construct and measurement validity;
- predictive specificity and falsifiability;
- mechanistic coherence;
- replication or convergence across independent methods and populations;
- boundary conditions and generalizability;
- contradictory evidence, null findings, and failed predictions.

Use study-appropriate appraisal rather than one universal checklist or evidence hierarchy. Do not convert the criteria into numeric weights or a composite score.

#### Gate 2: Approve comparison and ranking

Ask the user to keep, add, merge, split, rename, or remove perspectives; change pairings; revise criteria; request bounded source follow-up; or approve final comparison.

Before Gate 2 approval:

- do not produce the final comparison;
- do not rank the perspectives;
- do not infer the user's preferred theory;
- do not save or hand off the work.

Gate 2 authorizes only the approved comparison and final synthesis.

### 6. Compare perspectives

Assess each approved perspective on its own terms before comparing it with alternatives.

Within each perspective, address:

- empirical support and contradiction;
- mechanistic coherence;
- predictive specificity;
- construct and measurement fit;
- methodological strengths and limitations;
- replication and convergence;
- scope and boundary conditions;
- plausible alternative explanations;
- evidence that would materially change the assessment.

For each approved comparison, address:

- where the perspectives genuinely disagree;
- where they use different language for compatible claims;
- whether similar predictions arise from different mechanisms;
- which observations discriminate between them;
- whether the evidence supports integration rather than competition;
- what remains unresolved because of source coverage or study limitations.

### 7. Produce the ranked critical synthesis

For an approved ranking, present the evidence-calibrated outcomes in the selected form. Use a ranked table when it serves that form, or as the fallback when the request and verified applicable policy leave the representation open. Preserve uncertainty and the allowed ranking outcomes.

Allowed ranking outcomes:

- ordered tiers;
- tied positions;
- `Unrankable with current evidence`;
- `Insufficient evidence`;
- separate rankings for different populations, methods, outcomes, or levels of analysis when one global order would mislead.

The ranking is an evidence-calibrated synthesis judgment, not a mathematical estimate or the user's scientific conclusion.

Do not use percentages, numeric confidence, point totals, or hidden weighting.

## Outputs

Use the sections below as the evidence checklist. Follow the requested form first, then the verified applicable recipient or project policy. When neither specifies a form, use this Markdown structure. Preserve the search record, source evidence, comparison scope, uncertainty and limitations when changing headings or presentation. Include ranking or integration only within the approved evidence scope.

```markdown
# [Topic] Critical Theory Synthesis

## Product Identity and Question

## Scope, Search Record, and Coverage

## Source-Level Evidence Ledger

## Theory or Perspective Taxonomy

## Within-Perspective Assessment

## Between-Perspective Comparison

## Ranked Perspective Table

## Integrative Account

## Contradictions, Uncertainty, and Evidence Gaps

## Diagnostic Next Evidence

## Priority Reading List

## Limitations of This Synthesis
```

Include an integrative account only when the approved evidence supports one.

Diagnostic next evidence should identify observations, methods, populations, measures, or source clusters that could change the comparison. Do not turn it into a grant, dissertation, or experiment plan unless the user separately requests that work through the appropriate capability.

Return the synthesis in the requested form, or use the verified applicable recipient or project reporting policy when the request leaves the form open. If neither specifies a form, return it in the current session without creating a separate report file.

For an authorized synthesis file, verify and use the selected destination and template. If a choice is open, follow the applicable verified placement and formatting policy. Use a verified fitting destination or template from the layout guide as the fallback. Ask once if a required destination remains unresolved. Preserve the search record, source verification status, and coverage limitations in the saved artifact and verify the file before reporting completion.

Do not automatically hand off.

- Use [research-summarizer](../research-summarizer/SKILL.md) for deeper explanation of one selected paper.
- Use [research-companion](../research-companion/SKILL.md) for broader framing or research strategy.
- Use [writing-companion](../writing-companion/SKILL.md) only after the user selects approved synthesis material for manuscript prose.
- Use [chat-handoff](../chat-handoff/SKILL.md) when the approved task is preparing bounded material for another AI chat or reviewing material returned from that chat.

## Boundaries

Scientific standards:

- Separate reported evidence, author interpretation, AI inference, and speculation.
- Preserve conflicting findings instead of averaging them into false consensus.
- Distinguish historical influence from current support.
- Distinguish theoretical plausibility from empirical support.
- Distinguish direct tests from proxy measures and post hoc reinterpretation.
- Distinguish absence of evidence from evidence of absence.
- `p > alpha` is not significant and is not marginal, approaching significance, a trend, or nearly supported.
- Nonsignificance does not establish the null.
- Evidence for absence requires an appropriate justified method.
- Keep exploratory and post hoc evidence labeled.
- Never invent sources, methods, samples, statistics, findings, identifiers, or search coverage.

Edge cases:

- **Supplied corpus only:** State that the synthesis is source-bounded and do not infer broader field coverage.
- **Search unavailable:** Continue only from approved supplied sources and label the result provisional.
- **Only abstracts available:** Preserve abstract-only labels and do not make methods or limitation claims that require full text.
- **Literature too large:** Stop at the approved limit, identify omitted regions, and use tied or unrankable outcomes when coverage prevents comparison.
- **Sparse evidence:** Retain the perspective in the ranked table as insufficient evidence rather than inventing support.
- **Conflicting evidence:** Preserve the conflict and examine differences in populations, measures, methods, or assumptions.
- **Scope changes after Gate 1:** Revise the brief and obtain new Gate 1 approval.
- **Taxonomy changes after Gate 2:** Return to Gate 2 before final comparison.
- **Formal review requested:** Stop and explain that a systematic, scoping, or other formal review requires its own method and reporting design.
- **One-shot request:** Do not skip Gate 1 or Gate 2.
- **Save not approved:** Return the synthesis for review in the current task's requested form or under the recipient's existing reporting policy. Leave files unchanged until saving is authorized.

## References

- Baethge, C., Goldbeck-Wood, S., & Mertens, S. (2019). SANRA—a scale for the quality assessment of narrative review articles. *Research Integrity and Peer Review, 4*, Article 5. https://doi.org/10.1186/s41073-019-0064-8
- Baumeister, R. F., & Leary, M. R. (1997). Writing narrative literature reviews. *Review of General Psychology, 1*(3), 311–320. https://doi.org/10.1037/1089-2680.1.3.311
- Grant, M. J., & Booth, A. (2009). A typology of reviews: An analysis of 14 review types and associated methodologies. *Health Information & Libraries Journal, 26*, 91–108. https://doi.org/10.1111/j.1471-1842.2009.00848.x
- Snyder, H. (2019). Literature review as a research methodology: An overview and guidelines. *Journal of Business Research, 104*, 333–339. https://doi.org/10.1016/j.jbusres.2019.07.039
