---
name: rea
description: >-
  Inspects shipped software through a local REA executable and explains features
  from static evidence. Use for packaged applications and supplied artifacts;
  ordinary source repository architecture uses normal coding tools. Triggers:
  inspect this packaged application, trace a shipped app feature, analyze an
  Electron package.
metadata:
  level: skill
  system: Engineering System
  dependencies: ""
  created: "2026-10-14"
  updated: "2026-10-14"
---

# REA

Explain a shipped software feature from the supplied artifact and inspectable static evidence.

## Purpose

Inspect a supplied JavaScript/Electron application tree or ASAR, identify its components, and trace the packaged code relevant to one feature question. Use the local REA executable for static analysis and small views of saved Evidence.

The installed command surface is deliberately limited to JavaScript/Electron analysis, saved Evidence views, help, and version information. Native decompilation, browser observation, application execution, and persistent analysis sessions are outside this build.

For an ordinary architecture question about a complete source repository, use normal coding tools directly. Do not run REA setup, readiness checks, or analysis merely because a repository contains JavaScript or Electron code.

## Inputs

- The supplied local application tree or ASAR path and the feature to explain.
- The managed runtime described in `./references/install_update.md`. Locate the manager relative to this skill folder; use its `run` command rather than a vendor setup or updater.
- A temporary working directory outside the vault for complete Evidence, view inputs, and selected views. Save a durable deliverable only when the current request calls for one.

## Steps

1. Identify the requested evidence. A packaged artifact or a claim about shipped code belongs here; ordinary source repository understanding uses normal coding tools. Confirm that the supplied target exists and is supported by this build.
2. Follow `./references/commands.md` to analyze the exact supplied path. Redirect the complete JSON Evidence to the external working directory; do not load the full graph into the conversation.
3. Request its summary view, then the smallest relevant module pages or item views. Reuse the saved Evidence instead of rerunning analysis for each view. The CLI uses complete inline Evidence in view input files, not an identifier retained by a server.
4. Trace the feature through the relevant packaged modules, resources, imports, and Electron IPC observations. Read focused source ranges when needed. Distinguish observed code and graph facts from inferred behavior, and preserve missing or partial coverage.
5. For a substantial explanation with independent evidence questions, use the optional review below. Otherwise review the claims sequentially. Resolve disagreements against the evidence; leave unsupported behavior unknown.
6. Return a concise explanation with the supporting packaged-code locations or evidence entries and the limitations that affect the answer. Return to the invoking companion when there is one.

If the runtime is missing or incompatible, follow `./references/install_update.md` within the current installation or repair authorization. Otherwise report the missing prerequisite and continue any useful work supported by the supplied files. Do not silently install software or repeatedly invoke setup.

## Outputs

Explain the requested feature and the code or evidence supporting it in the current task's requested form or under the recipient's existing reporting policy. Include material unknowns where they affect a claim. Keep raw Evidence, generated views, build material, and dependencies outside the vault.

Do not create installation summaries, usage records, tracking notes, provenance pages, or a second navigation hub. A saved artifact requires authorization and follows the user's existing destination rules.

## Boundaries

- Static evidence establishes what the supplied artifact contains. It does not establish that a branch executes, a feature is reachable, or a runtime effect occurs.
- Packaged or recovered code can differ from the original source. Do not present inferred names, source-map candidates, or reconstruction choices as recovered source facts.
- A missing match or exhausted view page does not prove absence when the parent analysis reports incomplete coverage.
- Preserve the supplied target. This workflow does not launch it, attach to a running application, register an MCP server, start listeners, or add telemetry, usage tracking, background jobs, or automatic updaters.
- Do not recover excluded commands by invoking the full vendor launcher or installing additional engines. A task outside the installed command surface needs an explicit change of scope.
- Updates and reinstalls use the maintained runtime recipe; they must reapply its removals and verification before replacing the working runtime. Never repair a missing module by bringing the excluded server, listener, tracker, or updater graph back into the runtime.
- Installation into another vault follows that recipient's instructions, canonical destination, system classification, and mounting method. The portable procedure is in `./references/install_update.md`; do not assume this vault's roots or copy its personal instructions.

## Handoffs

- Ordinary source repository architecture stays with normal coding tools.
- Software installation, repair, portable setup, and updates use `./references/install_update.md` and the one runtime manager in this skill.
- When invoked within another skill's session, return only the bounded technical findings and their limitations; the invoking skill retains the broader task.

## Optional Subagent Delegation

Use two independent reviewers when the requested explanation has enough distinct claims to benefit from parallel review. Give both the same frozen Evidence and relevant selected views. Assign no shared writes and no independent reruns of the target analysis.

- **Support reviewer:** check each proposed component, code path, and IPC claim against its exact supporting location; identify gaps or partial coverage.
- **Counterexample reviewer:** look for competing paths, contradictory observations, and behavior claims that require runtime evidence the static analysis cannot supply.

Both return the same compact format:

```text
Claim: [one proposed claim]
Verdict: [supported, unsupported, or unknown]
Evidence: [exact saved evidence entry or packaged-code location]
Missing check: [what would resolve the remaining question, or none]
```

The parent compares the reviews, checks disputed claims against the saved evidence, and writes the final explanation. A reviewer judgment is not a formal equivalence proof or a replacement for a tool's deterministic verification. When delegation is unavailable or adds little value, perform the same two checks sequentially without adding another companion, router, or approval step.

## Checks

- Confirm the Evidence identifies the supplied target and requested operation.
- Inspect selected views from the saved complete Evidence and preserve their coverage and unknowns.
- Support each feature claim with a code location or evidence entry; label interpretations and unresolved runtime behavior.
- Report an unavailable runtime or unsupported target accurately. Do not turn an analysis failure into a conclusion about the application.
