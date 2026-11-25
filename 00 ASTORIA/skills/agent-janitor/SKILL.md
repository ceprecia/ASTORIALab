---
name: agent-janitor
description: >-
  Audits agent behavior, traces where context or instructions drift, and tests
  candidate fixes before proposing live changes. Use when an agent follows stale
  procedures, loses scope during a handoff or resume, or skips an expected
  update. Triggers: audit agent drift, agents keep using old instructions, test
  an agent handoff.
metadata:
  level: skill
  system: Janitor System
  dependencies: ""
  created: "2026-11-24"
  updated: "2026-11-24"
---

# Agent Janitor

Trace one agent workflow, test a correction in isolation, and bring the evidence and proposed fix back for approval.

## Purpose

Use this for a concrete incident or a bounded workflow that may lose current instructions, scope, decisions, or durable state. Follow the chain from instruction discovery and source retrieval through interpretation, actions, handoffs, and persisted results. Diagnose the earliest supported failure, then test whether a small change improves the intended workflow.

## Inputs

- The workflow, symptom, expected outcome, and any accessible chat, trace, file, or incident date. If there is no incident, start with one named workflow and state what the audit can test.
- The working directory, host or client, model and version, relevant runtime configuration, tool access, and resume or handoff state, as observable. The harness is the runtime around the model, including what it loads, the tools it provides, and how it manages state.
- The current owner and authoritative source for the decision being tested, plus the authority and evidence available when the incident occurred.

## Steps

1. **Define expected behavior.** Read the applicable instructions and trace the intended route through the owning skill, project bridge, current handoff, and live writer or reader where relevant. Record what the agent should read, decide, do, and leave behind. Distinguish the authority in effect at the incident from the current desired behavior. Mark unknown historical state.
2. **Search the active path.** Use targeted searches for the old and current wording, changed filenames, paths, rule names, handoff markers, and references that read or write the state. Check which copies the host actually loads or exposes to the agent. Trace relevant generated views, links, skill registrations, settings, or source availability when evidence points there. Record file and section, version or relevant date, owner, and whether each hit is active, historical, generated, or unverified. Confirm material claims against the owning source and actual state.
3. **Find the first divergence.** Build the shortest evidence chain from expected authority to sources present, sources retrieved, action taken, and durable result. Compare the producer's claimed update with the stored contents and the consumer's next read. Look for a loading or routing failure, stale or missing content, incorrect precedence or interpretation, lost scope on resume or delegation, a skipped or failed write, wrong destination, or a premature completion claim. Record the earliest observed difference, the evidence gap if the chain breaks, and any competing explanations.
4. **Reproduce and grade.** Use [drift cases](references/drift_cases.md) to make a small isolated fixture. Write acceptance checks before running the baseline. Compare the old and candidate workflows from equivalent initial states with the same request, harness, and model where possible. Inspect observable behavior and persisted state. Label each result as an incident trace, live agent trial on a fixture, mechanical check, or scripted walkthrough. Use a walkthrough or mechanical check when an isolated agent run is unavailable, and state the behavioral evidence still needed.
5. **Test the smallest supported fix.** Change one owner source, pointer, instruction, or completion check at a time. Retry the original case, vary a plausible trigger for the failure, and use a held-out variant and a valid control to detect regressions. Reset between trials. For variable behavior, repeat comparable runs when practical and report results as counts with denominators and setup. Report mixed results and preserve any failed attempts in the evidence for this audit. If nothing reproduces, return the gap and the next discriminating check. Choose between keeping a smaller candidate, revising it, and leaving the fix unresolved based on those checks.
6. **Present the proposals for approval.** When invoked directly, present findings in the reporting form resolved under Outputs, retaining stable finding IDs, supporting evidence and validation limits. When routed by Janitor Coordinator, return draft findings and evidence for Janitor Companion's one consolidated approval proposal in that form. Use the finding ID to connect the user's decision to the exact live change. Wait for approval before applying a proposed live fix.
7. **Apply and verify the approved rows.** Recheck target state before editing. If the required operation or scope has changed, return that revised row for approval. Patch the canonical source or correct its existing active references. Reread the exact persisted change, verify its scope and dependent paths, and check that a fresh run discovers and uses it when a suitable runtime is available. Use a resumed or handoff run too when the issue depended on that transition. When only live file or route checks are possible, report the missing behavioral verification. Return the result against the approved row IDs.

## Outputs

Report the case summary, evidence, checks and proposed fixes. Use the current request's reporting form. For choices left open, follow the recipient's applicable verified reporting policy, with chat as the fallback. Honor explicit current chat-only, no-save and read-only limits. Create or save a report only within authorized output and destination scope; a reporting preference alone supplies no save, capture/log or external-send authority. Reuse applicable existing authorization without another gate. Keep stable finding IDs through reporting, approval and verification. Reporting does not approve live fixes.

Retain Issue found, Behavior, Fix and New behavior as semantic fields, with stable finding IDs, in internal Coordinator packets. Convey that information in the selected human-facing form. The following table is an optional template when table output is selected.

| Issue found | Behavior | Fix | New behavior |
| --- | --- | --- | --- |
| 1. Short issue and affected owner | Expected action, observed divergence, and evidence | Exact target and proposed change | Observed result with test label, or expected result with validation pending |

Give each finding a stable ID; include it in **Issue found** in internal Coordinator packets. Associate evidence, pass counts, unresolved points and verification limits with that ID in the selected human-facing form. Table headers and below-table placement apply only when that form calls for them. If there are no supported findings, report the checked scope and limits without inventing a finding; show empty table headers only when the selected form calls for them. After implementation, report for each approved finding what changed and which checks passed or remain open.

## Boundaries

- Follow the vault's existing authority, security, scope, and MOC rules in `me.md`. Audit findings are evidence for a decision. Apply only approved fixes, and use the current owner and existing handoff location for a permitted note update.
- If the candidate changes a MOC handoff, verify that agent state stays in the final `# 🤖 AI Notes` section and that the existing `# AI Study Notes` workflow, visible human plans, and approved capture history remain intact. Visible edits require the user's explicit authorization for the affected content.
- A comparison between different clients, tools, files, context settings, or budgets measures differences between those setups. For a model comparison, hold those factors constant and record what cannot be controlled. Keep attribution provisional when runtime context or the historical setup is unavailable.

## Handoffs

- Return draft rows, source evidence, scope, and unresolved checks to Janitor Coordinator when routed. Janitor Companion presents one consolidated approval proposal in the selected reporting form. On return, execute and verify the approved rows assigned to this skill.
- Refer skill registration or contract maintenance to Skills Janitor, vault structure or bridge consistency to the owning vault skill, and agreed changes with affected dependents to Propagate. Supply the first divergence, the exact active source, and the expected behavior so the receiving skill can verify its part.

## Checks

- The expected action follows from current authority, with historical uncertainty kept explicit. The first divergence cites observable evidence.
- The baseline and candidate have comparable initial states. Every behavioral claim matches how the test was run, with repeated outcomes and unresolved regressions visible.
- Verification inspects the actual persisted state and distinguishes a fresh lookup from an agent's claim that it updated or used the source.

## References

- Anthropic. (2025, September 29). *Effective context engineering for AI agents*. https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Anthropic. (2026, January 9). *Demystifying evals for AI agents*. https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs get lost in multi-turn conversation*. International Conference on Learning Representations. https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/
- Lopopolo, R. (2026, February 11). *Harness engineering: Leveraging Codex in an agent-first world*. OpenAI. https://openai.com/index/harness-engineering/
- OpenAI. (2026, May 29). *A shared playbook for trustworthy third party evaluations*. https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- OpenAI. (n.d.). *Custom instructions with AGENTS.md*. https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2025). *LongMemEval: Benchmarking chat assistants on long-term interactive memory*. International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html
