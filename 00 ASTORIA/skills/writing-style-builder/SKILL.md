---
name: writing-style-builder
description: >-
  Creates or updates one passive writing-style reference directly from sources
  the user supplies. Names it on the scheme `writing-style-<positive|negative>-<label>`:
  positive for rules to follow, negative for habits to remove. Extracts practical
  rules for wording, syntax, rhetoric, local flow, tone, and formatting while
  excluding argument structure and scientific decisions; labels source
  limitations without blocking; writes the profile as a skill folder with level
  profile; tests it on sample drafts in its own writing contexts and adjusts the
  rules until a round comes back clean; regenerates the Skill Map; validates the
  result; reports what it built and how the test went. Triggers: build my
  writing style profile, update my writing style profile, calibrate my writing
  style from these samples.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: ""
  created: "2026-07-23"
  updated: "2026-09-25"
---

# Writing Style Profile Builder

Turn supplied writing samples or style sources into one concise, usable,
passive writing-style reference. The finished profile provides rules and
examples to a writing capability; it does not produce or revise prose itself.

## Purpose

Use this skill when the user asks to create or update a writing style profile from:

- writing samples the user supplies or explicitly names;
- a pasted or user-named style guide;
- an existing profile and new source material;
- an exact paper, webpage, repository file, or other bounded source the user identifies.

This builder creates profiles. It does not apply them to its own chat output or to an unrelated writing task, except inside the test cycle below, where applying the profile to throwaway drafts is how the profile is checked.

Activation rules:

- Creating or installing a profile does not activate it.
- The bundled scientific and editorial profiles are selectable references. Apply one or a combination only when the recipient selects it for the task or records that choice in their own preferences.
- Task genre alone does not select a profile or a profile pair.
- An explicit request to apply a named profile authorizes its use for that current writing task.
- Creating or updating a profile does not apply it to the current conversation.
- Never make a new profile assistant-wide or add it to unrelated skills automatically.

## Inputs

Use information already supplied. Ask only when one of these essentials is missing:

- the source material or exact source location;
- the intended profile name or enough purpose to name it;
- access to a source that cannot be read.

Audience, register, authorship, editing history, and intended use are helpful but not mandatory. Record unknown information as unknown rather than turning it into an intake gate.

## Steps

1. **Identify the target.** Name it `writing-style-<positive|negative>-<label>`: positive when the profile says what to do (the scientific profile), negative when it says what to remove (the AI profile). The label is one lowercase word or a short hyphenated one (scientific, ai, grant, email). If the folder exists, update it; otherwise create it.
2. **Read the supplied sources.** Inspect only the material the user supplied or exactly named. Do not search for additional examples, or follow unrelated links.
3. **Extract usable patterns.** Identify recurring or explicitly stated rules for:
   - word choice and terminology;
   - syntax and sentence construction;
   - rhetoric and claim presentation;
   - local flow and cohesion without changing the approved organization;
   - tone and reader relationship;
   - punctuation and formatting.
4. **Separate style from scientific and argumentative ownership.** Do not turn topic vocabulary, factual claims, quotations, data, or isolated subject matter into general style rules. A profile may guide expression and local cohesion, but it must not choose claims, evidence, inference, interpretation, ideas, argument structure, paragraph functions, or section organization.
5. **Qualify limitations without blocking.** Mark a rule `supported`, `context-specific`, or `tentative` when that distinction matters. Note coauthored, edited, translated, templated, sparse, or mixed sources briefly. Build the best supported profile instead of requiring a threshold or held-out set.
6. **Write the profile directly.** Create or update the skill folder `00 ASTORIA/skills/<name>/SKILL.md` with `metadata.level: profile`, `metadata.system: Writing Style References`, and no trigger sentence (profiles are loaded by writing skills, never invoked). A negative profile may ship a `scripts/` checker, as writing-style-negative-ai does, so the writing skill can test a draft instead of rereading the list. For an update, preserve unrelated existing rules unless the user asked to replace the profile.
7. **Test the profile on drafts and adjust it.** Follow `./references/test_cycle.md`: pick five to ten situations from the profile's writing context, write each once without the profile (naive) and once with it applied through the writing skill that will load it, add two or three human-written controls, and score. A negative profile's checker must fail every naive draft and pass every applied draft and every control; a positive profile's rules are tallied per rule against the naive drafts, and any rule that changed nothing, changed meaning, or contradicted an explicitly selected companion profile is rewritten or dropped. Fix the profile, rewrite the affected drafts, score again, and stop when a full round ends with no rule change. Drafts and scores stay outside the vault and are removed at the end; report only the cycle actually performed and its limitations in the requested form; keep References for outside sources.
8. **Register it.** Run `00 ASTORIA/skills/skills-janitor/scripts/build_views.py` so the Skill Map registry lists it under Writing profiles.
9. **Validate and report.** Run `00 ASTORIA/skills/skills-janitor/scripts/lint.py` (frontmatter, headings, links, registry). Then summarize in the requested report the created or changed rule groups, any material source limitations, the situations tested, the scores before and after, and the adjustments made.

Do not stop for a profile brief, rule-by-rule approval, task requirements, evidence matrix, calibration gate, held-out source validation, Style Profile Specification, adapter handoff, or [skill-builder](../skill-builder/SKILL.md) review. The draft test in step 7 is the builder's own check, run without asking, and its output is a report, not an approval request.

## Profile format

Use this compact shape:

```markdown
---
name: writing-style-<positive|negative>-<label>
description: >-
  Passive rule reference for [writing context]. A writing capability applies its
  patterns while preserving approved content, structure, evidence, and
  terminology. Loaded [automatically for ... | only when the user names it]; never
  invoked on its own.
metadata:
  level: profile
  system: Writing Style References
  dependencies: ""
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
---

# Writing Style: <Positive or Negative>, <Label>

## Intended use

- Writing context:
- Activation: Explicit only, unless a named writing capability is configured to load it automatically.

## Style rules

### Word choice and terminology

### Syntax

### Rhetoric and claims

### Flow and cohesion

### Tone

### Punctuation and formatting

## Source limitations

Only material qualifications that affect how the rules should be interpreted.

## References

APA 7 references for the supplied outside sources, one per bullet, with `Adapted from:` before a source the rules were adapted from. Omit the section when there are none.
```

Omit empty rule subsections. Keep the profile focused on instructions that change writing behavior. A negative profile replaces "Style rules" with its families (rule, tells, fix) and may add `scripts/` and `references/patterns.md`; see writing-style-negative-ai for the shape.

## Boundaries

Source handling:

- Preserve source files unchanged.
- Use exact links or portable profile variables when recording source locations.
- Do not retain complete source documents or long excerpts inside a profile.
- Do not infer sole authorship, editing history, ownership, license, or personal preference when it is unknown.
- Coauthored or edited work can still inform a profile, but label that limitation.
- External guides can support a style convention but cannot establish the user's personal voice by themselves.
- Mixed sources can support context-specific rules rather than forcing one universal voice.
- If a supplied source is inaccessible, ask for an accessible copy or pasted material. Do not route through another builder automatically.

Rules:

- Create one profile per invocation unless the user explicitly requests a bounded batch.
- Build from the supplied evidence without unnecessary interviews.
- Build a passive rule reference. Do not give the profile a drafting, revision,
  decision-making, routing, or application workflow.
- Test every profile before reporting it (step 7). Test drafts are temporary, live outside the vault, and are removed; report the scores in the requested deliverable or recipient-selected reporting form. Save a separate report only when authorized.
- Compare rules only against the recipient's current style specification and any other profile they selected for this task. Resolve conflicts using that selected scope; no companion profile or fixed division between additions and removals is assumed.
- Do not use [paper-to-skill](../paper-to-skill/SKILL.md), [repo-to-skill](../repo-to-skill/SKILL.md), or [skill-builder](../skill-builder/SKILL.md).
- Do not turn internal quality checks into user questions or convert internal quality checks into user gates.
- Do not independently browse for more sources.
- Do not apply a writing profile to capture, summarization, MOC, skill-building, note-making, or ordinary chat workflows.
- Do not claim that a profile detects AI authorship, and do not report a perplexity gauge or a classifier as a detector.
- Report uncertainty briefly rather than refusing to build.
- If this run creates or updates a profile as authorized and logging the change is within this role's scope, add one entry at the top of the existing `00 ASTORIA/agent_notes/ai_log.md` under its callout. Use three to six lines with the date and skill in the heading and record what was done, where and what is pending.
