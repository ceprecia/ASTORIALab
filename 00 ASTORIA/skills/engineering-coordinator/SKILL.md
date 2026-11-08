---
name: engineering-coordinator
description: >-
  Routes engineering questions to skill-loaded specialist workers in the
  current project and returns their evidence to Engineering Companion. Uses
  dedicated chats after one scoped creation choice or in-chat subagents when
  chats are declined; technical judgment stays with the companion.
metadata:
  level: coordinator
  system: Engineering System
  dependencies: mechanism-design, 3d-builder, fit-review, circuit-design, wiring-design, sensing-calibration, firmware-control, engineering-test, assembly-builder, circuit-builder, rea
  created: "2026-10-30"
  updated: "2026-11-02"
---

# Engineering Coordinator

Load the right specialists, give them concrete questions, and collect their work.

## Purpose

Run internally within Engineering Companion's chat. Route substantive engineering questions, focused technical planning and project work to actual skill-loaded specialist workers. Dedicated chats in the current chat's project are the recommended route; in-chat subagents are the alternative. Own dispatch, source context, dependencies and collection; technical synthesis and tradeoffs return to the companion. Read `00 ASTORIA/systems/Engineering System.md` for shared practice.

## Inputs

- The engineering question, outcome, constraints, completed work and current authorization.
- The parent chat's verified project ID/workspace and any explicitly selected different destination.
- Current team mappings, approved routing choice and assignment scope, if established.
- Exact task inputs, relevant facts/units, selected design/revision, owned outputs and completion evidence.

## Steps

1. **Select and load the technical owners.** Read the generated Specialist Catalog and each selected SKILL.md completely. Choose the relevant owners even for a single-area question; do not require a new project kickoff. A complete device can use the nine work areas; a focused question uses its owner and an independent reviewer when useful. Do not create unrelated roles just to fill a roster.
2. **Verify the destination and reuse.** Default to the project containing the parent/current chat, not the project that owns a referenced file. Resolve the current project through host context and project tools, verifying its binding before creation. Reuse suitable authorized specialist chats and preserve established names/numbers. Before allocating a new chat, read the single fixed registry at `00 ASTORIA/skills/research-coordinator/references/team_naming.md`; use its prefix and project-wide next unused ID, reserving numbers centrally before parallel dispatch. Engineering work-area numbers are not chat IDs. Missing or ambiguous binding uses the internal-worker fallback rather than guessing another project.
3. **Prepare a specific brief before the choice.** Read the relevant task sources and identify the component/interface, actual question, requested calculation/design/test, relevant values with units, current decisions, source paths/locators, unknowns and expected result. The parent must be able to name the proposed specialists and their concrete work in one creation question. Do not ask the user to approve an empty staffing plan.
4. **Apply the one team-choice gate.** If dedicated-chat creation/delegation is not already authorized for this scope, have the companion offer its Team Choice once. Wait for the answer before creating chats. Explicit team creation is confirmation already; an existing approved assignment needs no repeated question. Declining, no-new-chats or keep-it-here selects internal specialist subagents. A request forbidding all delegation is honored separately.
5. **Dispatch the selected workers.** Use the Execution Modes and Assignment Format below. Give each worker its exact resolved SKILL.md path and relevant source inputs, and require it to read them rather than rely on the skill name. The assignment question must be technically specific. A single specialist can run as one internal subagent; run multiple workers concurrently only for independent lanes and sequence dependent/shared-file work.
6. **Collect and inspect actual returns.** Wait for completion and inspect the returned evidence and relevant artifacts. Collect dedicated-chat reports through read/status tools rather than requiring unauthorized reply messages. Require a concise account of which skill and task sources were actually used, plus result/checks/limits. A queued chat, claimed skill load or generated plan alone does not prove the task was performed.

   Route combined mounting/packaging claims to Fit Review with the current saved model, delivered exports/views, source references, support/retention method, wiring geometry or reservations, required motion and installation states. Obtain missing interface evidence from CAD, wiring or mechanism owners. Receive findings for support/retention, wiring, motion and assembly/service, including incomplete functions and inapplicable topics. A narrowly scoped static review cannot silently replace the whole-assembly question. Propagate changed findings to the creator and assembly owner, then receive the affected correction independently.
7. **Correct and receive interfaces.** Give exact discrepancies to their creator, then independently check consequential changes. Carry changed decisions to every affected active assignment and receiving owner without making the user relay them. Preserve unrelated completed work and keep one writer per mutable artifact.
8. **Return to the companion.** Summarize results, actual worker IDs/states, changed interfaces, checks, uncertainty and next owners/actions. Return technical tradeoffs to the companion. Maintain only useful role/skill, routing choice/scope, worker/chat ID/host, goal, owned files and state in the existing MOC's AI Notes when authorized.

## Execution Modes

| Mode | Use and behavior |
| --- | --- |
| Dedicated project chats | Recommended for substantive engineering questions, including focused specialty questions and project kickoff. After the one choice is confirmed, or creation is explicitly requested, create/reuse one chat per relevant skill in the current chat's verified project. Give each its source-backed question and concrete output. |
| In-chat specialist subagents | Use when dedicated chats are declined, the user says keep it here/no new chats, requests this mode, or chat creation/binding is unavailable. Spawn one or more relevant workers; each reads its dedicated skill and task sources. A single lane is valid. The parent collects and combines their results. |
| Sequential loaded-skill fallback | Only when agent tools are unavailable or all delegation is explicitly disallowed. Execute the selected specialist workflow here and disclose the limitation; never silently replace requested specialists with a generic companion answer. |

Approval of the proposed current-project team authorizes its scoped creation, kickoff and follow-up assignments, including relevant existing chats identified in that choice. Do not ask again per worker or correction within that scope. Before messaging any existing chat, establish direct human authorization for the target/scope under the host's rules; another worker's request alone is insufficient. Do not infer approval from a selected-but-unsubmitted option or silence. Quoted examples and editing these routing instructions do not launch a team. Do not create recurring monitoring from a one-time assignment.

## Optional Subagent Delegation

For the user's in-chat route, use at least one worker for an area-specific question; use additional specialists or reviewers when the task needs them. Each worker has an isolated write scope and reads its assigned skill. Concurrent lanes must be independent; dependent work receives its interface first. Use the shared return format and keep stitching/acceptance with the companion. Ordinary mechanical batching stays in code. If worker tools are unavailable, use the disclosed loaded-skill fallback.

## Assignment and Return Format

Assignment: **specific engineering question and requested result; completion evidence; current project/MOC; exact SKILL.md path; relevant source paths/locators and inspected facts with units; selected design/current decisions/completed work; authorization/mode; owned files; interfaces/dependencies; return owner**.

For fit work, also supply relevant support surfaces and their uncertainty,
the function-to-component map, complete routing/transmission interfaces,
required operating/service states, current saved scene and intended claim.
Fit Review returns source-located findings and actual check coverage before
dependent packaging work.

Return: **result; skill and task sources actually read/used; changed artifacts/interfaces; checks actually performed and limits; remaining uncertainty; next owner/action**. Scale this to the task; do not require empty fields or a separate report file.

For every chat or subagent kickoff, give the project path and require applicable AGENTS.md and its briefing, relevant MOC context, the exact assigned skill body and necessary source inputs to be read. Do not substitute reading only me.md or the catalog for loading the specialist. Ask a concrete technical question, for example to compare a supplied travel requirement with a measured component range, or reconcile named connector contacts against the supplied board plan. Unknown inputs stay unknown. Read-only/planning limits pass through unchanged. The worker returns a final report for the parent to collect.

## Specialist Catalog

<!-- catalog:start -->
Generated from skill frontmatter by `skills-janitor/scripts/build_views.py`. Each link opens `00 ASTORIA/skills/<name>/SKILL.md`; read that file completely before acting, and check its `requires` and `gates` first.

- [3d-builder](../3d-builder/SKILL.md): Creates editable mechanical models and assembly scenes with matching step renders using parametric CAD and Blender. Triggers: model this part, make an exploded view, render these assembly steps, prepare this model for printing.
- [assembly-builder](../assembly-builder/SKILL.md): Guides complete device assembly from documented parts through mechanical, electrical and software integration, coordinating the needed engineering specialists. Triggers: assemble this device, walk me through assembly, continue this hardware build, connect these components.
- [circuit-builder](../circuit-builder/SKILL.md): Guides a beginner through building and checking a circuit board from a verified wiring plan: how to read the board and the drawing, a parts and tools table, hole-by-hole steps naming each contact's device and purpose, and a generated continuity and power-up test table; runs the engineer's verification gates (design, before the first joint, before power, staged power-up) as fault finding with corrections. Triggers: walk me through soldering this, help me build this board, check my wiring before power, is my circuit wired correctly, guide me through this PCB build.
- [circuit-design](../circuit-design/SKILL.md): Designs and analyzes the electrical plan for a device. Triggers: design this electronics circuit, select electrical replacement parts, analyze this power circuit.
- [engineering-test](../engineering-test/SKILL.md): Plans and evaluates tests of engineering claims across a complete device. Triggers: plan this device verification, test this hardware claim, review engineering test coverage.
- [firmware-control](../firmware-control/SKILL.md): Implements device firmware and its control and communication behavior. Triggers: implement this device controller, write this hardware driver, debug this embedded protocol.
- [fit-review](../fit-review/SKILL.md): Independently reviews assembly fit, service access, routing and motion against source geometry. Triggers: review whole assembly fit, find motion and access conflicts, check this packaging arrangement.
- [mechanism-design](../mechanism-design/SKILL.md): Analyzes mechanical operating principles and develops bounded mechanism concepts. Triggers: compare mechanical transmissions, size this actuator mechanism, explain how this mechanism moves.
- [rea](../rea/SKILL.md): Inspects shipped software through a local REA executable and explains features from static evidence. Triggers: inspect this packaged application, trace a shipped app feature, analyze an Electron package.
- [sensing-calibration](../sensing-calibration/SKILL.md): Defines and verifies the conversion from hardware measurements to useful quantities. Triggers: calibrate this hardware sensor, define this measurement conversion, assess sensor accuracy.
- [wiring-design](../wiring-design/SKILL.md): Designs the physical wiring that implements an electrical plan. Triggers: design this cable harness, map these connector contacts, plan moving cable routes.

11 skills in this system.
<!-- catalog:end -->

## Outputs

- Concrete specialist assignments and actual worker results returned to Engineering Companion.
- Created/reused project chat IDs or internal subagent states, skill/source inputs actually used and the scoped routing choice.
- Minimal current context in the existing MOC when authorized; no second hub or separate status registry.

## Boundaries

- The specialist catalog is generated from metadata; do not edit its entries by hand.
- Source-file ownership does not move workers out of the parent chat's project. Only an explicit user destination changes it.
- The one choice governs team creation for its scope; it does not add sign-offs for ordinary corrections or internal workers chosen after declining chats.
- Tools and permissions remain host-dependent. Missing chat capability routes to internal workers, not fabricated chats; missing all worker capability is disclosed.
- Technical disagreements return to the companion, with alternatives explicit rather than silently adopted.

## Handoffs

- Borrow the shared writing-coordinator for bounded writing work under `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`, preserving engineering-companion as the original session/return owner. Supply existing technical worker IDs and their authorized scope so writing support reuses them instead of forming a competing technical team.
- A methods/technical request returns exact source revision, operating principle, component/contact/parameter values with units, actual procedure, observed outputs, test limits and unresolved questions. Keep documented, proposed, selected, installed, calculated, simulated and measured states distinct. Receive translated passages for technical fidelity review; route changes to their engineering owner.
- Return actual dispatch/results to engineering-companion without loading another companion instance.
- Circuit Design owns electrical design; Circuit Builder owns board construction; Assembly Builder owns the complete walkthrough; Engineering Test owns claim-specific evaluation.
- Use rea for packaged JavaScript/Electron inspection; ordinary source reading uses coding tools.

## Checks

- The relevant specialist body was loaded and the worker received actual engineering facts and source references.
- A focused task has a specialist worker; declining dedicated chats does not bypass specialist work.
- Creation has an explicit human confirmation or an already authorized request/scope; the choice is not repeated per chat or follow-up.
- Every chat uses the verified current project and role mapping unless the user explicitly selected another project.
- Parallel writes are isolated, dependent work is sequenced, and every requested result was collected before synthesis.

## Modular Plugin Support

Prefer purpose-built host tools. On Codex, use current chat/project context plus `list_projects` and `list_threads` to verify the parent project's identity and relevant existing workers. Use `create_thread` only for human-authorized new tasks after the one team choice or an explicit creation request; use the verified parent project ID in its target and do not infer another destination from source paths. Use `send_message_to_thread` for authorized assignments and `wait_threads`/`read_thread` for collection. Read the current schemas and preserve pending IDs, host rules and required created-chat directives. Use collaboration tools to spawn/message/wait for internal subagents instead of creating project chats when that route is chosen. Other hosts use equivalent capabilities or the disclosed fallback. No server or integration installation is required.

## References

- OpenAI. (n.d.). *Subagents*. https://learn.chatgpt.com/docs/agent-configuration/subagents
