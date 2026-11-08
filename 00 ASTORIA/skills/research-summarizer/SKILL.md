---
name: research-summarizer
description: >-
  Explains one or more bounded research papers through a separate
  source-verified seven-part summary for each paper, covering plain-language and
  expert explanations, statistical methods and results, key findings, strengths,
  weaknesses, and discussion questions. Adds a table, equation, or diagram to a
  part when it clarifies a central claim, each built from the paper's reported
  values or stated design and tagged with its source. Use when the user explicitly invokes
  Research Summarizer, asks to summarize or explain a specific research paper or a
  supplied set of papers, or when a verified Research Coordinator handoff selects it for one bounded
  paper-summary task. Do not use for general summaries, multi-paper synthesis,
  independent research critique, manuscript drafting, or contextual connections
  to the user's vault and projects. Triggers: summarize this paper, explain this
  study to me, what does this paper claim.
metadata:
  level: skill
  system: Research Assistant System
  part: "1"
  family: literature
  modality: any
  dependencies: ""
  requires: the paper text or PDF; a Python runtime with matplotlib only for a PNG plot on save
  gates: ""
  created: "2026-05-19"
  updated: "2026-11-01"
---

# Research Summarizer

Explain each supplied research paper deeply without pretending to know more than the available source provides.

## Purpose

Use this skill when any of these conditions applies.

- The user explicitly says "research-summarizer" or "research summarizer";
- The user asks for a bounded paper summary or explanation, including "summarize this paper", "explain this study to me", "what does this paper claim", "summarize these papers" or "summarize all these papers". Apply the same source and scope checks.
- a verified [research-coordinator](../research-coordinator/SKILL.md) handoff selects this capability for one
  supplied or otherwise bounded paper-summary task.

A coordinator handoff counts as invocation only for that bounded task. It
does not bypass this skill's source requirements, approval gates, stop points,
or verification.

Outside a verified coordinator handoff, do not trigger this skill for general
conversation summaries, meeting summaries, transcript summaries, BLUF
summaries, broad requests to read or analyze a paper, or multi-paper synthesis.
Ordinary summaries belong to [summarize](../summarize/SKILL.md). Multi-paper synthesis belongs to
its own Part 1 capability.

## Inputs

Ask only for missing information that blocks the summary.

- **Article source or sources:** Required. Accept PDF paths, supplied files, pasted text, abstracts, or paper links.
- **Citation details:** Optional. Title, authors, year, journal, DOI, or link.
- **Focus:** Optional. Methods, theory, statistics, clinical relevance, neuroscience relevance, critique, or discussion preparation.
- **Depth:** Optional. If unknown, provide a thorough graduate-level summary.
- **Figures:** Optional. `full` by default: a figure in every part where one clarifies a central claim, under the caps in `## Figures`. `few` keeps at most three per paper, chosen by the same test and caps, Part 3 first; `off` removes every figure. The user may also ask for one specific figure, such as the design schematic, the model equation, or a results table; a requested figure still passes every rule in `## Figures`, and when the paper does not state what it would show, say so instead of building it.
- **Output location:** Optional. Follow the requested form for this task, then the applicable verified recipient or project reporting policy. If neither specifies a form, return the summary in the current session without saving it. For an authorized save, resolve the destination under Saving.

## Steps

### 1. Load and verify the source

Read the supplied paper material before summarizing it.

- If the user provides only a title or citation, ask the user to supply the paper or approve a search. Do not search automatically.
- Identify the title, authors, year, and venue only when the supplied or verified source supports them.
- State whether access covers the full paper, selected sections, an abstract, or another partial source.
- If a file is unreadable or the available content is insufficient for the requested depth, report the limitation before continuing.
- Do not inspect ASTORIA notes, projects, Mendeley, or other local context unless the user separately supplies the exact paper from that source.
- Note which figures, tables, and equations the paper itself provides, which are clear enough to point to by number, and which design, model, pipeline, or result the prose leaves hard to see. This gap scan feeds the figure decisions in Step 2.

Verify the paper identity and access coverage before making claims about the source. Present both in the location and form selected for this task, then under the applicable verified reporting policy when either choice is open. If neither specifies placement or form, this brief header can precede the summary.

```markdown
Loaded: [paper identity supported by the source]
Coverage: [full paper | selected sections | abstract only | other partial source, including a fetch that paraphrases the text]
```

### 2. Produce the seven-part summary

Use the required output format below. Preserve the paper's distinction between reported results and author interpretation. Put critical evidence assessment in Part 6 rather than repeating it throughout the summary.

For each part, consult the per-part table in `## Figures` and add a figure only when it passes the when-to-add test there. Build it by `./references/figure_playbook.md`, use the figure block format in `## Outputs`, and place it inside the part right after the sentence it serves. When the prose carries the point, add nothing.

### 3. Offer source-bounded discussion

After the summary, offer to discuss the paper. Keep the discussion grounded in the supplied paper and do not automatically inspect the user's vault, projects, or broader literature. A follow-up request for a figure of the loaded paper (its design, model, or reported results) is handled here under the same tags, Source lines, and Boundaries, as one extra block outside the per-part caps; it is not a handoff to another skill.

### 4. Offer one bounded next action

Offer one next action that fits the request:

- continue source-bounded discussion;
- save the summary;
- hand a difficult method or concept to [study-companion](../study-companion/SKILL.md);
- hand contextual implications for the user's work to [research-companion](../research-companion/SKILL.md);
- hand approved manuscript use to [writing-companion](../writing-companion/SKILL.md).

Continue with the next action when the current request already authorizes it. Ask only when the action still needs authorization. A reporting or destination choice alone does not authorize execution, saving, search or handoff.

## Optional Subagent Delegation

Use this loop when the request contains more than one paper:

```text
paper_n = number of supplied papers

if paper_n == 1:
    run the existing Research Summarizer normally

if paper_n > 1:
    assign each paper to one subagent
    each subagent runs the existing Research Summarizer for its paper
    collect the paper-specific evidence sections in paper order with their source attribution intact
    present the sections in the grouping requested for this task or configured by the recipient
    save only when explicitly requested, using only the authorized grouping and destinations
```

Present one distinct evidence section per paper in the current task's requested form or under the recipient's existing reporting policy. Keep the papers in order and identify each by title. Preserve each paper's summary coverage, source attribution and evidence limits. Use paper-title headings when the selected form uses headings.

Do not add a combined summary or synthesis. If the host cannot use subagents,
run the same loop sequentially. Each subagent reads `./references/figure_playbook.md`
before building a figure; figure numbering restarts under each paper's heading,
and PNG names are checked across the whole run.

## Outputs

Present each paper's title and summary in the current task's requested form or under the recipient's existing reporting policy. Keep each paper separate and preserve the seven content areas below at the depth the request calls for. A selected form may group or rename headings while keeping the scientific content and source attribution clear. The example shows a full Markdown summary with level-3 paper titles and level-4 part headings.

```markdown
### [Paper Title]

#### Part 1: High-Level Feynman Summary
[Plain-language explanation of the article's primary topics.]

#### Part 2: Expert Expansion
[Deeper explanation following the framework in Part 1.]

#### Part 3: Statistical Methods and Results
[First explain the methods using the Feynman technique. Then explain them like an expert. Then explain what the results imply.]

#### Part 4: Key Findings
[Combined summary of the most important points from Parts 1 and 2.]

#### Part 5: Strengths
[The paper's strongest features.]

#### Part 6: Weaknesses
[The paper's limitations, evidence gaps, assumptions, uncertainty, and interpretive risks.]

#### Part 7: Discussion Questions
[Questions about critique, future research, and implications.]
```

Place figures with the content they serve, right after the sentence that introduces them. A table that replaces bullets follows one lead-in sentence. Label the kind by content as `Table`, `Equation`, or `Figure` (a Mermaid diagram or a PNG). Number each figure `<part>.<n>` using the corresponding content area even when visible headings differ. Count every figure in that area in order regardless of kind and restart numbering for each paper. The Markdown example below shows the label, Caption, Source and Values fields. Preserve those fields in the selected form.

```markdown
**Table 3.1. Main effects on reaction time**

[one Markdown table, one $$ display block, one Mermaid code block, or one verified PNG embed when the note edit is authorized]

Caption: [first sentence names, as the authors' claim, the central claim the figure serves; then what to look at]. Source: [Table 2 | Methods, Procedure, paragraph 2 | paper Figure 3 legend | this skill's Part 6 reading]. Values: [one tag from the list in the Figures section].
```

Saving:

- Use the task’s requested form, then the applicable verified reporting policy. If both leave disposition open, return an unsaved summary. Save only within authorized scope and verify the exact destination before writing.
- For multiple papers, keep the authorized grouping and destinations. Preserve distinct evidence sections and source attribution.
- Use the verified eligible destination selected for the task, then the applicable verified recipient or project placement policy. Where placement remains open, resolve the verified owner location. Keep Project or Area working material in its local `files/` or documented workspace. Use Resources for reusable references. Preserve established operational layouts. A note or MOC edit requires its own authorization. For an authorized separate note, use the applicable template and selected or verified naming convention. Check the exact destination filename for a collision before writing. Preserve unrelated files and resolve any conflict inside the authorized naming scope.
- Keep tables, display equations and Mermaid in the saved Markdown. Write a qualifying PNG during an authorized save under the playbook’s placement and naming rules. Add a supported embed only within an authorized note edit. Place it above the same reported values under one label and verify the file and link. Preserve unrelated files.
- Do not copy the PDF, create topic or concept pages, update state files, or emit event logs.

## Figures

A figure here is a Markdown table, one `$$` equation block, or a Mermaid diagram that this skill draws from the paper. Build every figure by `./references/figure_playbook.md`.

When to add one:

- The caption's first sentence names, as the authors' claim, the central claim the figure serves, and the figure carries either a structure of three or more related elements (a design, model, pipeline, or an argument the paper itself lays out as numbered hypotheses or steps) or values the prose would need more than three sentences to state.
- The paper leaves a gap: a design or model described but never drawn, results scattered through prose, a model stated only in words, or a figure of its own too dense to read. When the paper's own figure or table is clear, point to it by number instead.
- The figure repeats nothing written above it and adds no claim the part does not make.

Caps: one figure per part. Part 3 may hold two: the methods figure sits in the expert pass after the model or test is named, never in the Feynman pass; the results figure sits at the end of the expert pass, before the sentence on what the results imply. Part 2 may hold two when it carries a schematic and a measures table. A breakdown of one dense paper figure may hold up to three labeled panels under one caption and counts as one figure. `few` keeps at most three per paper. Abstract-only coverage gets none.

| Part | Figure under `full` | None when |
| --- | --- | --- |
| 1 | A design sketch as a Mermaid flowchart of the arms, conditions, or phases, with no numbers and no equations, only when the design has two or more factors, arms, or phases. | Fewer than two factors, arms, or phases, or the paper's own figure draws the whole design clearly. |
| 2 | A schematic of the model the paper proposes or tests, of the task or acquisition pipeline in the paper's own step names and order, or of the design when Part 1 holds no sketch; as a second figure, a measures table (construct, instrument, unit as reported or `Not reported in the provided material`, where reported) when the paper names four or more measures. | Part 1 already shows the design, the paper proposes or tests no model, and fewer than four measures are named. |
| 3 | The model as one `$$` block when the paper states one in symbols, as a worked computation, or in words that name its outcome, every term, and its functional form; never the textbook form of a named test or of a model named only by its label. Use a results table or another representation suited to the selected delivery form for the rows the central claims rest on. Include the null rows of the same analysis, eight rows at most, and name the paper's table for the rest. A plot only for a forest plot with an estimate and interval reported on every row, or an interaction pattern across six or more reported cell means. | The paper reports no statistics. |
| 4 | A selected-format findings figure that separates the reported finding, the authors' interpretation, and the implication with attribution. A table with these fields is a fallback when it serves the selected delivery. | Fewer than three findings. |
| 5 | A selected-format figure pairing each strength identified by this skill with its location in the paper. A table with these fields is an optional fallback. | Fewer than four strengths. |
| 6 | A selected-format display of claim, reported evidence and this skill's assessment for mismatch or reporting-gap entries. Keep other weaknesses in prose. An eligible alternative is one supported diagram of a confound or alternative path named in Part 6, using only paper-named measures, conditions or variables, tagged illustrative and captioned as this skill's assessment. | No mismatch, no reporting gap, and no confound named in the prose. |
| 7 | A selected-format display of the question, its group (critique, future research or implications), and the section, table or figure it draws on. A table with these fields can replace the grouped lists when useful. A follow-up design, proposed analysis or predicted result is outside the figure scope. | Fewer than four questions, or the questions already name their sources. |

Every figure carries one `Values:` tag:

- `as reported`: numbers and structure exactly as the paper gives them, each traced to a named table or passage, or to a number printed in a figure's labels or legend; a value read from a plotted mark, bar, or axis is never used. Tables and copied equations take this tag; a Mermaid diagram never does.
- `derived from reported <inputs> (<formula>)`: arithmetic on reported descriptive values only, such as a count, a percentage of a reported n, a total, a speed from a reported distance and duration, or a unit conversion, with the arithmetic shown; never a statistic the paper did not report, including a mean difference, a ratio of means, an odds or risk ratio, a standardized effect size, a standard error, an interval bound, a test statistic, or a p value. A table that mixes reported and derived cells takes this tag and shows the arithmetic in each derived cell.
- `formalized from the authors' description`: an equation for a model the paper states only in words or as a worked computation, where the paper names the outcome, each term, and the functional form; every symbol maps one to one to a named term in the symbol list under the block, each cited to its passage; a term, link, or interaction the paper does not name is left out and the list says so.
- `schematic, stated elements only`: the paper's design, model, pipeline, or numbered argument with only the elements and relations the paper states; a relation the paper implies is left out and the caption says so.
- `paper Figure N, simplified; dropped: <list>`: a breakdown of the paper's figure that names what was left out; a value or relation that appears only in the image is not reproduced.
- `illustrative, not the paper's data`: only for a Part 6 confound or alternative-path sketch, or for a sketch of a method or concept the paper names, built from elements the part's prose already states. A design, pipeline, model, or results figure of this paper is never illustrative: an element, relation, direction, order, or duration the paper does not state is left out and the caption says so. Box shapes are never values, but left-to-right or top-to-bottom order reads as the paper's order.

On a Part 4 to 7 table the tag describes the columns that quote or cite the paper; every column that holds this skill's text is headed as this skill's, and every column that holds the authors' words names them.

Values read off a paper's plot are never used; write `Not reported in the provided material`.

Rendering:

- Render the summary in the requested form, then under the applicable verified reporting policy when the request leaves it open. When using Markdown, use tables where appropriate and omit an outer code fence. If the selected surface cannot render a diagram or formula, express the same source-supported structure or mathematics in a readable form it supports. For example, describe the labeled sequence or model terms and functional relationship in text. Preserve the source, attribution and figure eligibility checks.
- Present the same reported values in the current requested form, then under the applicable verified recipient or project policy if the request leaves the form open. If neither specifies a form, return the values in the current session. Use a table when helpful. Make an eligible PNG only when its save is authorized and a matplotlib runtime is available. When the report edit is authorized, use the playbook's selected-form image rules and place any supported embed above the same reported values under one label. If an authorized PNG cannot be made, keep the values and state the limitation once. Image and data files require an authorized save.
- No inline SVG, Canvas, Excalidraw, HTML, found images, or image search. Mind maps and Canvas belong to [mindmap](../mindmap/SKILL.md), interactive examples to [study-planner](../study-planner/SKILL.md), found images and videos to [study-enricher](../study-enricher/SKILL.md).

## Boundaries

Source discipline:

- Summarize only what is in the paper or what the user provides.
- Do not invent methods, sample sizes, measures, statistical tests, results, limitations, citations, or implications.
- If a detail is missing, write `Not reported in the provided material`.
- If the paper is only partially available, label the summary as partial.
- If explaining "as the author," use that as an explanatory stance, not as a claim of private authorial knowledge.
- Separate what the authors claim from what the evidence supports.
- Never plot, tabulate, or write into an equation a value the paper does not report, except a value the `derived` tag's arithmetic produces and shows; where a figure would need any other value, write `Not reported in the provided material` and use a schematic or nothing.
- Never copy, crop, trace, or reproduce the paper's own figures or images; redraw a design or model as a schematic and name the original by number. No found or web images and no image search.
- Do not connect the paper to the user's notes, projects, research tracks, or personal knowledge base. Route that separate task to [research-companion](../research-companion/SKILL.md).

### Part 1: High-Level Feynman Summary

Explain the paper's main ideas in plain language.

Include:

- the big question
- why the question matters
- what the authors did
- what they found
- what the result means at a high level

Avoid jargon unless it is necessary. If jargon is necessary, define it.

### Part 2: Expert Expansion

Expand the explanation using field-specific detail.

Include:

- theoretical background
- study rationale
- key constructs
- design logic
- main measures
- how the evidence connects to the claim
- what the paper adds to the field

Keep the structure aligned with Part 1 so the simple explanation and expert explanation map onto each other.

### Part 3: Statistical Methods and Results

Explain statistics in two passes.

First, use the Feynman technique:

- what the test or model is trying to answer
- what the inputs are
- what comparison or relationship is being estimated
- what a significant, null, or mixed result would mean

Then explain like an expert:

- statistical model or test
- variables, predictors, outcomes, covariates, contrasts, or factors
- effect sizes, confidence intervals, p values, correction methods, model assumptions, or uncertainty when reported
- whether the analysis supports the authors' claim

Finish with what the results imply.

If the provided material does not include enough statistical detail, say exactly what is missing.

### Part 4: Key Findings

Combine Parts 1 and 2 into the most important takeaways.

Present the findings in the task's selected form, then under the applicable verified reporting policy. When neither sets the form, use concise prose or bullets. A supported findings figure can carry the same content once. In any form, distinguish the following.

- finding
- interpretation
- implication

### Part 5: Strengths

Name the paper's strongest features.

Possible categories:

- clear research question
- strong design
- appropriate sample
- useful measures
- transparent methods
- appropriate statistics
- important theoretical contribution
- clinical, translational, or methodological relevance

Only include strengths that the provided paper supports.

### Part 6: Weaknesses

This is the canonical section for critical evidence assessment. Name the paper's limitations, evidence gaps, and interpretive risks.

Possible categories:

- sample limitations
- measurement limitations
- design limitations
- statistical limitations
- missing controls
- unsupported or weakly supported claims
- mismatches between a claim and the reported evidence
- assumptions that materially affect interpretation
- missing reporting or unavailable information
- uncertainty and alternative explanations
- overclaiming
- unclear causal inference
- limited generalizability

Be direct but fair.

### Part 7: Discussion Questions

Give discussion questions grouped by:

- critique
- future research
- implications

Questions should be useful for seminar discussion, lab meeting, journal club, or manuscript thinking.

Interaction rules:

- If the user provides a PDF or article text, read it before summarizing.
- If only an abstract is provided, summarize only the abstract and say the full paper is needed for methods, statistics, strengths, and weaknesses.
- If the paper has no statistical analyses, say so in Part 3 and explain the analytic or argumentative structure instead.
- If the article is a review paper, adapt Part 3 to cover the review method, inclusion logic, synthesis strategy, and strength of evidence.
- If a claim seems unsupported, document the mismatch in Part 6.
- For a shorter output, make the seven content areas concise and group them when that fits the selected form. Keep source coverage and material scientific qualifications clear.
- Abstract-only coverage means no figures. Selected-section coverage allows figures built only from the supplied sections.
- A figure setting of `off` removes every figure. For a shorter summary, include a figure only when requested and eligible under the figure rules.

Scope:

- Explain one or more bounded papers separately. Do not become a literature-search or multi-paper-synthesis workflow.
- Keep contextual connections to the user's work outside this skill.
- Keep independent design, inference, and claim critique outside this skill except for paper-bounded weaknesses required by Part 6. Route detailed scientific critique of one bounded research object to [research-critique](../research-critique/SKILL.md).
- Do not draft manuscript prose or insert citations into a manuscript.
- Do not automatically ingest, save, search, chain skills, or update the vault.
- Adapt depth to the paper and the user's request. Preserve the scientific distinctions among the seven content areas in the selected form.

## Optional Add-Ons

When useful, include one of the optional additions below. Place it where it serves the selected summary form.

- `#### Optional: Methods Table`
- `#### Optional: Terms to Know`

Do not add optional sections by default if they make the summary too long. The Optional Methods Table is a figure under `## Figures`: it carries the block format and a tag, counts toward `few`, and is removed by `off`. When Part 2 already carries a measures table, do not add it.

## Checks

- Every number in a figure traces to a named table, figure, or passage and is re-read against the source after the figure is built; every derived number is recomputed and its arithmetic shown.
- Every figure has the label line, the Caption, Source, and Values lines, one tag matching one of the six forms with each placeholder filled, numbering `<part>.<n>` that restarts per paper, and sits inside the part it serves; on a Part 4 to 7 table every assessment column is headed as this skill's or the authors'; no row holds a p value without its test statistic.
- Every schematic holds only stated elements; every arrow direction and edge label traces to a stated claim; every illustrative figure carries its tag.
- Mermaid uses flowchart syntax with every label quoted and no node named `end`; code fences and `$$` pairs are balanced; LaTeX uses commands, not Unicode symbol strings; no formula sits inside a table cell.
- The figure count respects the setting and the caps. An `off` setting has no figures. Check that the selected form retains the technical content at the requested depth.
- For a saved PNG, verify the exact file and any authorized embed in the supported selected form using the playbook. Check for wider basename ambiguity only if the selected syntax requires it and the necessary search is authorized.

## References

- Adapted from: Huang, H. (n.d.). *Researcher Pack: paper-read* [Computer software]. https://github.com/andrehuang/researcher-pack (MIT License)
- Mermaid. (n.d.). *Flowcharts: Basic syntax*. https://mermaid.js.org/syntax/flowchart.html
- Obsidian. (n.d.). *Advanced formatting syntax*. https://obsidian.md/help/advanced-syntax
