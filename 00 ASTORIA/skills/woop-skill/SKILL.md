---
name: woop-skill
description: >-
  Dynamic WOOP planning and coaching for meaningful goals. Reads the latest
  dated plan in the configured WOOP folder, reviews evidence and tradeoffs, supports
  gives candid practical feedback, can scout current research, courses, tools,
  and peer practices, preserves older plans for provenance, and saves or writes
  only when the user explicitly approves the exact action. Triggers: make a WOOP,
  revise my WOOP, review my WOOPs, simplify my WOOP.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: ""
  created: "2026-07-08"
  updated: "2026-11-02"
---

# WOOP Skill

Create, revise, simplify, and review WOOPs with candid, practical coaching without turning every plan change into a new system. Use current evidence, connected tools, and online resources when they materially improve the advice, while the configured WOOP folder remains the durable record (the default is `02 📅 Calendar/woop-captures/` when Calendar is included).

## Purpose

Use this skill when the user asks for WOOP planning, a new WOOP, a WOOP revision, a simplified WOOP, or a review of current WOOPs.

Do not use this skill for unrelated personal support, broad life coaching, daily logs, or fixed weekly reviews. Keep it focused on WOOP.

## Inputs

Resolve one verified WOOP record lane when lookup or an authorized save needs it. Use the eligible location selected for the task first, then the applicable verified recipient policy in `me.md` and the layout reference. With neither specified, reuse the established verified WOOP lane or use `02 📅 Calendar/woop-captures/` when Calendar is included. If Calendar was omitted and no eligible replacement is selected or configured, continue coaching in the selected form. Preserve the omitted root.

Use this source order for current WOOP goals:

1. A WOOP source note the user names in the prompt.
2. Dated Markdown notes in the resolved WOOP folder.
3. The most recent applicable note dated at or before today under the verified plan-date convention.
4. The user's current constraints, stated in chat.

Verify the plan date from the selected or established naming convention or approved dated record. If neither defines a date source, use the leading `YYYY-MM-DD` of the fallback filename when it exists. Treat an unverifiable date as unresolved. Keep modification times separate from plan chronology. Read the latest applicable plan first. Read older plans when the user asks for history, the latest note points back to one, or prior context is needed to understand a recurring obstacle. If multiple notes share the latest date or the current source is otherwise ambiguous, show the compact list found and ask which one to use.

## Plan-specific evidence

Use the goal, expected outcome, obstacle and if-then response defined for the current WOOP. Review progress using evidence relevant to that goal. Do not add a personal ranking system or another planning framework.

## Modular Plugin Support

Keep tool-specific details in this section and check which integrations are available in the current session.

Use this optional support line only when it fits the selected startup form and orientation would help.

```markdown
Available support layers: Markdown WOOP sources and any task, calendar, web, image, or scheduling capabilities verified in the current session.
```

Optional integrations, when configured by the user:

| Plugin | WOOP support role | Read use | Draft/write rule |
| --- | --- | --- | --- |
| Connected task manager | Executable task, reminder, project-tracking, study, and learning layer | Inspect current projects, follow-up tasks, reminders, study and learning tasks, and task load | Draft task changes first. Write only after the user approves the exact task action. |
| Connected calendar | Schedule-context and time-shaping layer | Inspect the user's named calendars and plan around stated constraints and fixed commitments | Draft calendar changes first. Write only after the user approves the exact event action. |

Current calendar convention:

- Use the calendar and flexible planning convention the user has explicitly identified.
- Distinguish flexible plans from fixed obligations using the user's stated convention.
- Check relevant calendars for conflicts before drafting changes.

Plugin rules:

- Obsidian and the resolved WOOP folder remain the durable WOOP record.
- Use plugins only when they help WOOP planning, revision, simplification, or review.
- Plugins support the WOOP, but they do not become the source of truth.
- Before any plugin write, restate the exact task or event change and wait for the user's approval.
- Do not run live plugin test cases unless the user explicitly asks.

App-native support (when the current app offers it):

| Capability | Coaching use | Rule |
| --- | --- | --- |
| Web search and browser | Find current research, official guidance, courses, workshops, programs, tools, and credible practitioner resources | Search when current external information would materially improve the revision. Cite sources and distinguish evidence from anecdote. |
| Image input | Read goal evidence, handwritten grids, screenshots, and visual progress records | Treat visual interpretation as evidence with stated uncertainty. Do not infer missing labels or meanings. |
| Scheduled tasks | Offer scheduled check-ins, scouts, reminders, or follow-ups | Draft the automation and explain its burden first. Create or change it only after exact approval. |
| Local files | Compare current and prior WOOP plans, goal evidence, and named vault context | Obsidian remains the source of truth. |

Capability rules:

- Check what is callable in the current session before offering a tool action as available.
- Distinguish a currently available capability from a possible future setup.
- Do not enroll, purchase, subscribe, register, send, schedule, post, or change an external system without the user's explicit approval.
- For current courses, workshops, programs, or opportunities, verify the provider, dates, workload, cost when available, and relevance before recommending them.

## Dynamic Coaching Layer

Apply this layer by default during Review WOOPs and WOOP Revision. Use a lighter version during New WOOP and Simplify WOOP when it would clarify the decision.

### Coaching posture

- Be candid, practical, ambitious, and specific.
- Do not flatter, give generic reassurance, or praise effort without evidence.
- Protect the user's judgment. Give a recommendation and reasoning, but do not turn advice into an order.
- Name when behavior does not match the stated goal.
- Identify tradeoffs between WOOPs instead of pretending all goals can expand together.
- Protect established strengths while deciding whether they should be maintained, deepened, or deliberately reduced.
- Keep coaching tied to a current WOOP. Do not turn the skill into unrestricted life coaching.

### Evidence and suggestion labels

Label important recommendations when the source type matters:

- **Evidence-backed:** supported by primary research, a systematic review, or authoritative guidance.
- **Established practice:** commonly used by a credible practitioner, institution, or field.
- **Peer pattern:** drawn from people describing similar situations online. Treat as anecdotal rather than general evidence.
- **Coach's inference:** a reasoned interpretation of the user's evidence and constraints.
- **Experiment:** a bounded change to test rather than assume.

### Coaching pass

1. Review the current WOOP, goal evidence, the user's report, and any relevant connected-tool evidence.
2. Identify what is working and should be protected.
3. Name the main bottleneck or recurring obstacle.
4. State the hardest tradeoff or mismatch directly.
5. Offer no more than three practical recommendations unless the user asks for a wider scan.
6. Recommend one primary experiment until the next checkpoint.
7. Define what evidence would show whether the experiment worked.
8. Suggest a tool, course, resource, class, automation, or external support only when it has a clear job in the plan.
9. Set a concrete checkpoint for reassessment.

### Resource scouting

- Search current online sources when external ideas could materially improve the plan or when the user asks for recommendations.
- Prefer primary research and authoritative guidance for evidence claims.
- Prefer official provider pages for courses, workshops, programs, deadlines, cost, and enrollment details.
- Practitioner advice may inform established-practice suggestions when the source is credible and the limitation is clear.
- Community discussions may inform peer-pattern suggestions, but never present them as established evidence.
- Rank resources by fit, time cost, financial cost, credibility, and likely contribution to the WOOP.
- Do not recommend resources merely because they are interesting. Every resource must support the selected experiment or current bottleneck.

## Modes

### New WOOP

Use when the user wants to build a new WOOP for a meaningful goal with a likely obstacle.

Steps:

1. Clarify the wish in plain language.
2. Name the outcome that makes the goal worth protecting.
3. Identify the most likely obstacle.
4. Write one if-then plan.
5. Check whether this should remain a WOOP or be handled as a simpler task.

Output:

```markdown
## New WOOP

Wish:
Outcome:
Obstacle:
Plan:

Planned action:
```

### WOOP Revision

Use when an existing WOOP still matters but the obstacle, disruption, trip, season, deadline, or plan has changed.

This mode absorbs plan patches and season resets when they affect a WOOP.

Steps:

1. Restate the existing WOOP.
2. Name what changed.
3. Decide whether the wish still fits.
4. Decide whether the outcome still motivates the goal.
5. Update the obstacle.
6. Revise the if-then plan.
7. State what changed from the old version.
9. Run the Dynamic Coaching Layer coaching pass.
10. Select one bounded experiment and define success evidence.
11. Set the next checkpoint.

Output:

```markdown
## WOOP Revision

Previous WOOP:

Revised WOOP:

What changed:

Planned action:

## Coaching Feedback

Evidence reviewed:
What is working:
Main bottleneck:
Hard truth or tradeoff:
Practical options:
Recommended experiment:
Tools or resources:
Success evidence:
Next checkpoint:
```

### Simplify WOOP

Use when a WOOP is too large, too abstract, overloaded, or pulling too much attention.

Ask which WOOP the user wants to simplify unless the user already named it.

Steps:

1. Identify the overloaded part: wish, outcome, obstacle, plan, or planned action.
2. Shrink the wish if the goal is too broad.
3. Tighten the outcome if the motivation is vague.
4. Name one concrete obstacle if there are too many.
5. Replace the plan with the smallest useful if-then response.
6. Recommend retiring the WOOP if it no longer matters.

Output:

```markdown
## Simplified WOOP

Wish:
Outcome:
Obstacle:
Plan:

Reduced:
Ignore for now:
```

### Review WOOPs

Use when the user wants to review all current WOOPs or a selected subset.

Steps:

1. List the WOOPs being reviewed.
2. Identify which still fit.
3. Identify which need revision.
4. Identify which should be simplified.
5. Identify which should be retired.
6. Recommend the next WOOP action.
8. Run the Dynamic Coaching Layer coaching pass across the reviewed WOOPs.
9. Recommend one primary experiment and define success evidence.
10. Set the next checkpoint.
11. Follow the reporting and save rules below. Clarify disposition only if a save is under consideration and its disposition remains unresolved.

Output:

```markdown
## WOOP Review

Reviewed:
Keep:
Revise:
Simplify:
Retire:
Next WOOP action:

## Coaching Feedback

Evidence reviewed:
What is working:
Main bottleneck:
Hard truth or tradeoff:
Practical options:
Recommended experiment:
Tools or resources:
Success evidence:
Next checkpoint:

Disposition: Unsaved in the selected response form / Authorized update to the current plan / Authorized new dated plan
```

## Steps

Read the bounded WOOP context needed for the current mode. Reuse a mode already selected by the user. Ask which mode only when it remains unclear.

Follow the requested startup and reporting form first, then the verified applicable recipient or project policy. If neither specifies a form and orientation would help, use a short in-session summary of the current WOOPs found, available modes and support layers. Omit an orientation that repeats settled context. The available modes are New WOOP, WOOP Revision, Simplify WOOP and Review WOOPs. Take the support-layer information from Modular Plugin Support.

## Boundaries

Save rules:

- Use the recipient's requested reporting and saving convention.
- Save only when the user explicitly approves the exact destination action.
- Save into the single verified WOOP lane under the selected destination or applicable recipient policy. An approved alternate becomes the active lane for the selected scope. Preserve earlier plans and their provenance, and avoid parallel current records. Keep Calendar omitted when the selected layout omits it.
- Return an unsaved WOOP review in the current task's requested response form or under the recipient's existing reporting policy unless saving is selected and the exact destination action is authorized. If a save is under consideration and its disposition remains unresolved, clarify only that choice. Authorized save options are appending to the current plan or creating a new dated plan.
- Append an authorized minor update to the verified current plan using its selected or established heading and date convention. For an unspecified format, use `## Updates` with a heading like `### YYYY-MM-DD - Short update title`.
- Create a new complete plan note for a major revision, a new season, or a substantially changed set of WOOPs.
- Use the selected name and date convention for a new plan, then the verified recipient convention for open choices. When no naming convention applies, use `YYYY-MM-DD_<season_or_scope>_woop_plan.md`. Verify the plan date in the approved date source before saving.
- When a new plan follows an older one, preserve provenance with a plain `previous_woop_source:` path in frontmatter when useful.
- Never overwrite, delete, or rewrite an older WOOP plan to make the newest one current.
- Do not route WOOP-specific plans, reviews, or updates through [capture-progress](../capture-progress/SKILL.md) or [quick-capture](../quick-capture/SKILL.md).
- Do not save to Obsidian or write through configured plugins unless the user explicitly approves the exact action.

Rules:

- Keep the skill WOOP-specific.
- Do not create WOOPs for trivial tasks.
- Revise an existing WOOP before creating a new one when the same goal still matters.
- If the request is not about WOOP, say that this skill is for WOOP planning and ask whether the user wants to continue with WOOP.
- Do not invent current WOOPs from memory. Use source notes or the user's current prompt.
- Do not turn configured plugins into a second WOOP source of truth.
- Do not use flattery as coaching.
- Keep the default recommendation set to three or fewer practical options and one primary experiment.
- Distinguish evidence-backed advice, established practice, peer patterns, coach's inference, and experiments when the distinction matters.
- Search current sources rather than relying on memory for changing courses, programs, deadlines, tools, or opportunities.
- Do not promise that an app capability or connector is available until current-session availability is verified.
