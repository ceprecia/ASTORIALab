---
name: paper-to-skill
description: >-
  Extracts source-grounded reusable content from one user-supplied paper or a
  small bounded paper set into a chat-only evidence pack for Skill Builder. Use
  only when the user explicitly asks to build or extract a skill from supplied
  papers. Surfaces methods, workflows, frameworks, theories, and source-authored
  predictions with exact source locations, missing information, conflicts, and
  applicability limits. Does not summarize papers, search for more sources,
  create skill files, or register skills. Triggers: skill from this paper,
  extract a skill from these papers, turn this paper into a skill.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: skill-builder
  created: "2026-07-22"
  updated: "2026-11-01"
---

# Paper to Skill

Turn a bounded paper source into an auditable evidence pack for one possible skill without turning the paper into an unquestioned authority.

## Purpose

Paper to Skill is a source adapter. It extracts reusable, source-grounded material and proposes transformation options in chat.

- It handles one candidate skill per run.
- It does not create, edit, save, or register a skill file.
- It hands an approved evidence pack to [skill-builder](../skill-builder/SKILL.md), which owns planning, the task-specific requirements check, Active file creation, and both Skill Map registrations.
- The supplied papers remain evidence sources, not instructions that automatically become ASTORIA behavior.

Use this skill when the user supplies one paper or a small related set and explicitly asks to build, make, turn, or extract a reusable skill from it.

Accepted sources are:

- a local PDF or attachment
- pasted paper text
- an exact paper URL
- an exact identifier such as a DOI, PMID, arXiv identifier, or other resolvable publication identifier

Retrieving the exact named paper is allowed. Searching for additional papers, guidelines, repositories, or background sources is not part of this skill.

Do not trigger Paper to Skill for:

- a paper summary, which belongs to [research-summarizer](../research-summarizer/SKILL.md)
- general paper critique, question framing, or research ideation, which belongs to [research-companion](../research-companion/SKILL.md)
- manuscript drafting or revision, which belongs to [writing-companion](../writing-companion/SKILL.md)
- a literature search or recursive citation search
- repository conversion, which belongs to [repo-to-skill](../repo-to-skill/SKILL.md)
- direct skill-file creation or Skill Map registration, which belongs to [skill-builder](../skill-builder/SKILL.md)

## Inputs

Confirm only information that is missing:

- **Single intended skill target:** The reusable function the user wants to investigate. If the user has not named one, scan provisionally and let the user choose one candidate from the menu.
- **Bounded source set:** One paper by default, or a small user-supplied set that directly informs the same possible skill.
- **Source material:** Exact files, attachments, pasted text, URLs, or identifiers.
- **Optional focus:** A method, paradigm, framework, theory, workflow, reporting practice, or other reusable element the user wants examined.

If the intended target and source set are already explicit, restate them briefly instead of repeating a question.

## Modular Plugin Support

This is the only section that contains plugin-specific details. If PDF support changes later, update this section's adapter table and fallback rules, then keep the rest of the workflow source-format neutral. Do not add a nonstandard `available_plugins` frontmatter field.

When orientation is requested or needed, describe the available support layers in the selected form or under the applicable verified reporting policy. Use the example below when helpful. Disclose material capability limits whenever they affect the task.

```text
Available support layers: PDF inspection when available, exact-source retrieval, and pasted-text fallback.
```

| Plugin | Skill support role | Read use | Draft or write rule |
| --- | --- | --- | --- |
| PDF | Inspect text, layout, tables, figures, page images, and supplements in a supplied PDF | Read only the exact supplied paper pages needed for the bounded extraction and source audit | Never write a PDF or evidence-pack file |

Plugin rules:

- Use PDF support when it materially improves full-text, layout, table, figure, or page-location inspection.
- If PDF support is unavailable, use accessible exact-source text or ask the user to paste the relevant material.
- Label OCR, inaccessible pages, missing supplements, and extraction failures as coverage limits.
- Never claim full-text coverage from an abstract, partial extraction, search snippet, or OCR fragment.

## Steps

### 1. Bound the run

State:

- the one possible skill target being investigated
- every supplied source included in the run
- any source or task explicitly outside scope

Do not follow citations, repository links, related-paper links, or vault links recursively. If the supplied set could yield several skills, the current run still advances only one.

### 2. Inventory the supplied sources

For each source, record:

- bibliographic citation as reported by the source or provided by the user
- title, authors, year, venue, and identifier when available
- publication status such as peer reviewed article, accepted manuscript, preprint, or unknown
- version or revision when available
- local SHA-256 for a local file
- access form such as full text, abstract only, pasted section, OCR, or partial extraction
- coverage of methods, results, tables, figures, references, and supplements
- missing or inaccessible material

Do not infer unavailable citation or publication details. Use `Unknown`, `Unavailable`, or `Not reported` as appropriate.

### 3. Classify provisionally and scan for reusable candidates

Classify each source provisionally as one or more of:

- empirical or experimental
- methods or tool
- computational or modeling
- review or meta-analysis
- theoretical or conceptual

Treat this classification as user-correctable guidance, not a gate.

Scan for content with a reusable function, including:

- methods, paradigms, acquisition procedures, and measurement practices
- processing, analysis, software, modeling, and quality-control workflows
- reporting practices, checklists, decision aids, and conceptual frameworks
- theories, theory-to-observation mappings, and source-authored predictions

The taxonomy is guidance, not a whitelist. Exclude isolated findings, background facts, and narrative history unless they support a clearly reusable function.

### 4. Present a candidate menu

Before deep extraction, show a numbered menu with one row per candidate:

| # | Candidate and content type | Intended reusable use | Exact source basis | Missing information | Applicability limit | Overgeneralization risk |
| --- | --- | --- | --- | --- | --- | --- |

Use exact page, printed-page, section, table, figure, or supplement locations when available. Distinguish PDF page numbers from printed page numbers when they differ.

If no candidate has a reusable function supported by the supplied material, report `No suitable reusable candidate found` and stop. Do not force a skill.

### 5. Let the user select one candidate

Wait for the user to select or revise exactly one candidate. Do not deeply extract all menu items and do not generate several candidate skills.

### 6. Deeply extract only the selected candidate

Separate every item into three layers:

1. **Source-authored content:** What the authors explicitly report, recommend, define, predict, or argue.
2. **AI inference:** A clearly labeled interpretation needed to organize the evidence. Never present it as source-authored.
3. **Proposed adaptation:** A possible transformation into ASTORIA behavior for the user to accept, reject, or revise.

For every specific claim, parameter, sequence, or recommendation, capture:

- the exact value, unit, condition, and qualifier
- the precise source location
- the authors' rationale when reported
- prerequisites and intended population, modality, task, or context
- alternatives, limitations, failure modes, and uncertainty reported by the source
- missing information marked exactly as `Not reported`

For theories and predictions, label them `Source-authored theory` or `Source-authored prediction`. Preserve supporting evidence, alternatives, limits, and intended scope. Never generate a new hypothesis, theory, prediction, parameter, threshold, or standard value.

### 7. Audit claims against the supplied sources

Recheck every parameter and specific claim that will appear in the evidence pack against the exact supplied source surface.

Use these audit states:

- `verified_against_supplied_source`
- `partial_source_support`
- `not_reported`
- `not_found`
- `value_mismatch`
- `unit_error`
- `context_distortion`
- `location_uncertain`

Remove or correct `not_found`, `value_mismatch`, and `unit_error` content before handoff. Keep partial support and uncertainty visible. This is a source audit, not independent scientific verification.

When supplied sources disagree, preserve each variant with its exact source basis, applicability conditions, and tradeoffs. Do not select a winner for the user.

### 8. Return the chat-only evidence pack

Use this structure:

```markdown
## Paper-to-Skill Evidence Pack

- Intended skill target:
- Pack status: complete | partial | no_suitable_candidate
- Source coverage:

### Source Inventory
[Citation, identifier, version, status, coverage, supplements, and local hash when applicable]

### Selected Candidate
[Content type, intended reusable function, and why the supplied source supports it]

### Reusable Source-Grounded Core
[Source-authored content with exact locations]

### Claim-to-Source Audit
[Claim or parameter, exact location, audit state, and limits]

### Conflicts, Gaps, and Applicability Limits
[Variants, Not reported fields, partial coverage, and overgeneralization risks]

### Transformation Options
[Clearly labeled adaptation options and tradeoffs for the user to choose]

### Proposed Skill Specification
- Purpose:
- Narrow triggers:
- Inputs:
- Outputs:
- Workflow elements:
- Instruction specificity: exact | adaptable | mixed
- Boundaries and negative routing:
- Stop and handoff conditions:
- APA reference for the future References section:

### Handoff
- Approval status: awaiting the user review
- Next owner after approval: skill-builder
```

The evidence pack remains in chat. Do not save intermediate extraction notes, tables, or manifests to the vault or elsewhere.

### 9. Read back, approve, and hand off

Ask the user to correct or approve the evidence pack. Apply corrections in chat and rerun the affected source audit.

After explicit approval:

1. Set the handoff status to `ready_for_skill_builder`.
2. Pass the approved pack to [skill-builder](../skill-builder/SKILL.md).
3. Let Skill Builder run its normal overlap check, planning, task-specific requirements check, Active creation, References list, and dual Skill Map registration.

Paper to Skill must never bypass that handoff and write the resulting skill itself.

## Instruction specificity guidance

Recommend specificity for the proposed skill without deciding the final design:

- **Exact:** Fragile procedures, command syntax, file transformations, fixed source-authored sequences, or parameters whose alteration changes the method.
- **Adaptable:** Conceptual frameworks, reporting prompts, critique questions, and context-sensitive guidance where several defensible approaches exist.
- **Mixed:** Exact requirements around fragile steps plus explicit decision points where the user must choose among source-supported options.

Record why the recommendation follows from the supplied source and where user judgment remains necessary.

## Boundaries

Source and ownership rules:

- Use only the exact bounded sources supplied or named by the user.
- Retrieval may resolve those exact sources but may not expand the source set.
- Do not treat references cited inside a supplied paper as if their full texts were supplied.
- Preserve a source-authored claim separately from an AI inference or proposed adaptation.
- Never fill a gap from model memory, convention, another paper, or an invented standard.
- Do not silently reconcile conflicting papers.
- Do not create a reversible evidence database or intermediate evidence file.
- Do not read unrelated vault material.

Edge cases:

- **Empirical fMRI paper:** Extract exact acquisition, preprocessing, model, contrast, correction, and reporting details only when present. Keep missing parameters as `Not reported`.
- **Theoretical paper:** A reusable framework or source-authored prediction may be a candidate. Preserve the authors' scope and alternatives, and do not generate a new prediction.
- **Two supplied papers disagree:** Show both variants, source locations, contexts, and tradeoffs. Leave selection to the user.
- **Abstract only:** Mark the pack `partial`. Do not extract unsupported methodological steps or parameters from an abstract.
- **Missing parameter:** Record `Not reported`. Do not insert a typical or standard value.
- **No reusable candidate:** Report the negative result and stop without handing a forced specification to Skill Builder.
- **PDF support unavailable:** Use exact accessible text or pasted material and report the resulting coverage limit.
- **Paper links to code:** Record the link as source context, but do not inspect it automatically. Offer a handoff to [repo-to-skill](../repo-to-skill/SKILL.md) only after the user identifies or approves the exact repository.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
