---
related:
  - "[[ASTORIA System Builder]]"
  - "[[Research Assistant System]]"
created: 2026-10-06
updated: 2026-11-02
---

# Engineering System

![Engineering System](../assets/banner_system_engineering.png)

Start with Engineering Companion for a device project, hardware reverse engineering or recovery of a difficult build. Its internal Engineering Coordinator routes bounded work and collects reports. The companion combines the evidence and owns engineering judgment; specialists own their artifacts. The coordinator normally runs in the same main chat.

A skill supplies a reusable workflow. A dedicated chat or internal subagent actually reads that skill and the task sources to perform its assignment. Engineering Companion routes substantive technical questions through its coordinator, including a focused question or technical planning task. Recommend dedicated chats for the relevant skills in the project containing the current chat, with one concise creation choice if not already authorized. A confirmed or explicitly requested team proceeds without repeated questions. Declining chats or saying keep it here uses specialist subagents within the current chat, including one worker for a single-area question. Missing all worker tools permits a disclosed sequential loaded-skill fallback. Preserve read-only and planning limits on the work itself.

## Core Posture

### Official sources and alternatives

Engineering Companion, its coordinator and every engineering specialist follow this shared policy for the relevant work:

- Start with the selected product, revision, mirroring/orientation and official parts list, drawings and assembly documentation. Keep source identity and revision visible in the working inputs. Do not silently combine versions.
- Present **OFFICIAL STEP** first, then **ALTERNATIVES** underneath when applicable. When the user selects a local implementation as the current route, present that route clearly while retaining its local status and the documented baseline; do not silently revert the selection. Identify each alternative as **manufacturer-documented** or **local substitution/design**, state the changed parts and procedure, and name any additional materials before relying on it. When no official design exists, use **CUSTOM DESIGN** rather than inventing an official step.
- Track physical inventory as **confirmed available**, **confirmed missing** or **unconfirmed**, with quantity and the evidence for that status. Downloaded models, an order list or a purchase receipt do not establish that a part is in hand. Keep missing and unconfirmed items visible at the steps that need them.
- Check both sides of every mating interface: contacts rather than housing shape, pitch, pin order, polarity, orientation, fasteners, mounting features, tool access and cable clearance. A drawing that looks connected is not evidence that the physical parts mate.
- Treat the actual board copper, printed pin names and measured fit as evidence about the hardware in hand. When that evidence differs from the official baseline, record the mismatch and the local adaptation explicitly; do not rewrite the official requirement to hide it.
- Preserve completed assembly and passed checks. Recheck the connections, geometry and operations affected by a change, plus their dependent checks. Do not repeat unchanged work merely because a guide is regenerated.
- Distinguish official source geometry, measured dimensions, approximations, computational results and physical observations. A rendered or simulated assembly does not establish physical fit, successful wiring, firmware behavior or a passed bench test.

### Hardware work

- Use one coherent device guide owned by Assembly Builder when the request covers the whole device. Specialist output becomes the relevant section of that guide; standalone board and modeling requests remain valid.
- Use stable component and assembly-step identifiers across the inventory, model and guide. The small component-and-step manifest records sources, quantities, selected alternatives, units, dimension evidence, placements and mating relationships. Reference the verified electrical plan rather than copying its connections into a second authority.
- Keep editable project outputs in the authorized destination the user selects or the recipient's placement policy establishes. Verify current paths from `me.md` and the layout reference. Add one link from the existing owning MOC when the selected workflow calls for it and the link edit is authorized. Keep installed applications and dependency environments outside the vault.

- Construction instructions use a verified design for the affected connection or operation. A specific unknown does not block useful inspection, proposed geometry, calculations or test design; state the gap and resolve the affected operation through its owner.
- Circuit Design owns one current electrical connection plan. Compare schematics, board instructions and harness identities to it; revise the plan and its dependent outputs together when electrical evidence changes. Do not maintain competing connection tables.
- Each check has a pass criterion and a named correction; a passed check is not repeated unless the design changed.
- Plain language for a beginner: every term defined once, every joint with its reason, every reading with a tolerance.
- Title each step with the action and component. At the connection step itself, identify every contact/pad/hole, its named device or control and its terminal function; retain supplied voltage, net and controller endpoint. Repeated power/ground contacts name their assigned branches, and unused contacts are explicit. A general header label or earlier wiring explanation is not a substitute. Check that all rows survive the saved guide and figures. Photo-based pin positions carry a viewing reference and evidence status; documentation repairs preserve the circuit and completed checks.
- Required checks come from the verified design, manufacturer documentation and user constraints. Write concrete steps, label missing evidence and do not invent acceptance criteria.

### Software inspection

- Start with the supplied artifact and the feature question.
- Save complete analysis outside the vault and read focused views of the evidence.
- Distinguish observed code from inferred behavior and unresolved runtime questions.
- Keep installed software and dependencies outside the vault. Use the maintained local command surface without listeners, telemetry, usage tracking, or automatic updaters.

### Flexible investigation and independent checks

- Reverse engineering is iterative. Challenge, revise or abandon an earlier explanation, design, workflow or assignment as the current question, evidence or user direction changes. Versions identify the material inspected; they do not make an old conclusion authoritative.
- Distinguish target observations, documented claims, inferred mechanisms, proposed substitutes and unknowns. Preserve the user's latest decisions and distinguish selected, installed and measured states. A changed user requirement is not automatically an assistant error.
- Reuse existing drawings, finished-board images, measurements and answered questions before requesting them again. Preserve completed hardware during documentation or rendering repairs; change it when a concrete defect or revised objective warrants change.
- Check source agreement independently of export preservation: asymmetric landmarks, front/underside orientation, contacts, cavities and wire endpoints where they affect construction. A successful roundtrip can preserve a wrong model.
- Fit Review checks the actual combined candidate early, including support and separate retention, occupied wiring/contact mates, individual and coupled motion, and assembly/tool/service access. Use its explicit per-interface workflow; support posts, lid locks, empty routing reservations and neutral noncollision do not establish the corresponding fastening, harness or motion functions. Keep absent required functions visible alongside the limits of digital evidence. Test an uncertain essential interface as one complete module before repeating fabrication.
- Fit Review also checks mounting geometry, functional component counts and
  complete transmission/routing paths for the selected operating states.
  Curved supports and articulated neighbors are included when the design
  requires them. CAD authors inspectable virtual experiments and Fit Review
  checks the supplied geometry, interfaces and coverage independently.
  Declare collision shapes, constraints, loads and solver assumptions where used;
  geometric/kinematic checks, dynamic or structural simulation and measured physical
  tests remain distinct. Optional immersive VR is an inspection/input method.
- Engineering Test matches each consequential claim to evidence that could expose a wrong result. Inspect the actual saved guide, figure, model or runtime output; do not substitute a large count of unrelated checks for a missing comparison.
- Keep part costs, purchase packs, consumed quantities and fabrication allowances distinguishable. A partially priced subsystem is not a complete device total.

## Session Roles

- [engineering-companion](../skills/engineering-companion/SKILL.md) frames the outcome, reconciles current decisions, challenges assumptions, evaluates tradeoffs and combines the result.
- [engineering-coordinator](../skills/engineering-coordinator/SKILL.md) chooses owners, prepares assignments, manages dependencies and gathers their evidence. Its specialist catalog is generated from skill metadata; it makes no independent engineering tradeoff decision.

## Engineering Work Areas

These numbers are useful default work-area labels, not global chat identities. Preserve established chat titles and numbering when reusing chats. New chat names use the fixed shared registry at `00 ASTORIA/skills/research-coordinator/references/team_naming.md`, including project-wide ID allocation across engineering, research and writing lanes; never invent a new prefix during dispatch.

| Area | Skill | Owned result |
| --- | --- | --- |
| 01. Mechanisms and Reconstruction | [mechanism-design](../skills/mechanism-design/SKILL.md) | Functional reconstruction, force/motion/travel reasoning and proposed mechanisms. |
| 02. CAD and Manufacturing | [3d-builder](../skills/3d-builder/SKILL.md) | Editable geometry, source-based assembly scenes, print/manufacturing exports and views. |
| 03. Fit and Packaging | [fit-review](../skills/fit-review/SKILL.md) | Independent whole-assembly fit, motion, access and packaging findings returned to the artifact owner. |
| 04. Circuits and Power | [circuit-design](../skills/circuit-design/SKILL.md) | Electrical selection, calculations, schematic/PCB work and one connection plan. |
| 05. Wiring and Harnesses | [wiring-design](../skills/wiring-design/SKILL.md) | Complete physical connection paths, actual mating contacts, routes, terminations and relief. |
| 06. Sensing and Calibration | [sensing-calibration](../skills/sensing-calibration/SKILL.md) | Measurement units, physical-to-signal mapping, calibration, uncertainty and validity. |
| 07. Firmware and Control | [firmware-control](../skills/firmware-control/SKILL.md) | Acquisition, drivers, timing, communication, control and recovery implementation. |
| 08. Integration and Testing | [engineering-test](../skills/engineering-test/SKILL.md) | Claim-specific independent comparisons, fixtures, measurements and stage-specific readiness. |
| 09. Assembly and Commissioning | [assembly-builder](../skills/assembly-builder/SKILL.md) | One usable construction and bring-up sequence through the requested host/application demonstration. |

Circuit Builder remains the board-construction specialist under a verified plan: [circuit-builder](../skills/circuit-builder/SKILL.md). REA remains a separate packaged JavaScript/Electron inspection capability: [rea](../skills/rea/SKILL.md). Neither needs a dedicated chat for every hardware project. Ordinary source-repository work uses normal coding tools.

## Working Together

1. Companion identifies the current outcome, constraints, selected implementation and completed work.
2. Coordinator selects and reads the relevant specialist skills and task sources, then prepares concrete engineering assignments. The companion offers one choice of current-project agent chats (recommended) or in-chat specialist subagents unless the route is already explicit/authorized. Reuse suitable authorized chats; create only relevant missing roles after confirmation. Every worker receives its exact skill path, technical question, source references/facts with units, scope, owned outputs and completion evidence. Independent lanes can run together; shared-file edits and dependent operations are sequenced.
3. Specialists return result, skill/source inputs actually used, changed artifacts/interfaces, checks actually performed and their limits, remaining uncertainty and next owner/action. Reading only the personal briefing or catalog does not replace loading the technical skill.
4. Fit and test findings return to the responsible creator. For combined mounting/packaging claims, the coordinator supplies current saved geometry, delivered exports/views and source/interface evidence; Fit Review returns support/retention, wiring, motion and assembly/service findings or explains inapplicable topics. The creator corrects the affected artifact; an independent reviewer checks the consequential result. The coordinator propagates a changed decision to every affected active assignment without requiring the user to relay it.
5. Companion reconciles the whole design and explains what is established, unfinished and useful next. Export/mesh/hash checks establish artifact properties, not functional completeness or physical fit. Exploratory mockups and fit-test exports may finish with named incomplete interfaces; do not turn a partial clearance result into whole-assembly acceptance. Continue authorized corrections without adding approval rounds.

Keep current project context and chat/role mappings in the existing MOC's AI Notes. Return specialist deliverables in the requested form and use the authorized destination for any files. Assembly Builder owns the requested complete construction walkthrough. Use the capture skills for the Research Log. Do not create parallel project hubs, copied instruction files or per-agent status systems.

## Shared writing assistance

Engineering Companion remains the domain owner when borrowing Writing Companion
and its internal Writing Coordinator. The writing team can organize a technical
report, translate specialist methods and draft sections, then use separate citation,
structure, substance and argument-reasoning reviewers. Pass the central argument/status,
selected document structure, source revisions, exact terms and unresolved facts.

Engineering Coordinator supplies the existing authorized specialist chats and
bounded factual questions. Mechanism, circuit, sensing, firmware and testing owners
return actual values, procedures and evidence with their limitations. The methods
translator preserves these details; the relevant technical owner checks the draft.
A polished account never upgrades a simulation into bench evidence or an intended
connection into installed hardware. Keep one canonical document writer and return
design changes to their engineering owner. Use the shared contract in
`00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`.

## Routing

- Broad project direction, reconstruction, redesign or recovery: Engineering Companion, then its coordinator as needed.
- Focused design, fit, harness, calibration, control or test request received by the companion: coordinator assigns the matching skill-loaded worker using the chosen chat/subagent route; the companion combines its actual result.
- Complete construction from received design: Assembly Builder, with Circuit Builder and 3D Builder where needed.
- Board construction/soldering: Circuit Builder. Missing electrical design returns to Circuit Design, rather than being invented during construction.
- Packaged JavaScript/Electron feature inspection: REA. Scientific literature, experimental design and research analysis use their research entry points.

For launch prompts and fictional projects, use [the engineering practice examples below](#practice-examples). Examples and edits to routing instructions do not launch a team. The single creation choice names the actual specialists, current project and engineering goal; explicit chat creation already supplies that confirmation. Approval covers the current assignment and scoped follow-ups, not arbitrary other projects. Source-file ownership never silently changes the destination. An available parent-project binding is required; if it cannot be verified, use internal specialist subagents rather than guessing another project. A vault folder alone does not register an app project.

## Practice examples

These projects are fictional teaching examples. Their prompts show how to request work; reading or quoting them does not launch a project, agent or chat. The workflows use the actual skills listed above. Start in the intended project folder so its AGENTS.md, MOC and resources supply context.

### Choose the amount of help

| Need | How to ask | Expected behavior |
| --- | --- | --- |
| Focused engineering question | Ask the companion a specific design, fit, circuit, wiring, sensing, firmware or testing question. | Coordinator loads the relevant skill and recommends its current-project specialist chat; offer the one choice if needed. |
| Project direction, recovery or kickoff | Ask Engineering Companion to organize or investigate the device work. | Prepare concrete assignments and recommend the relevant team chats in the parent project; explicit creation requests already confirm that route. |
| Keep the work in this chat | Say “no new chats,” “keep it here” or “use specialist subagents.” | Coordinator spawns one or more skill-loaded internal workers and collects their results; the companion does not simply answer the technical task alone. |
| Existing approved specialist team | Ask the next engineering question within the assignment scope. | Reuse verified project/role mappings and give scoped follow-ups without repeating the creation choice. |

Skills can be loaded from their vault paths through the existing instructions; native skill-picker registration is optional. The companion and coordinator normally operate in the same main chat. Dedicated-chat tools are host-dependent; missing chat capability uses skill-loaded internal subagents first. Sequential execution or copyable handoffs are fallback options only when all worker tools are unavailable or delegation is explicitly disallowed. A project folder does not by itself register an app project.

### Example 1: Camera bracket, one focused task

**Made-up project:** A small camera needs a printed bracket attached to an existing desk fixture. Mount dimensions and screw details are supplied; one clearance is still unknown.

**Prompt:** “Engineering Companion, use 3D Builder to model a camera bracket from the supplied dimensions and fixture drawing. Keep the existing mount geometry, identify the unknown clearance, and give me editable CAD and a print-oriented view. Have Fit Review check screw access and camera adjustment before finalizing the bracket.”

**Useful skills:** `3d-builder` authors geometry; `fit-review` independently checks interfaces and access. `mechanism-design` joins only if the bracket requires a load-bearing hinge or adjustment mechanism. Circuits and firmware are unnecessary for this task.

**Expected result:** One recommendation to use current-project CAD/Fit specialist chats. If confirmed, create/reuse those chats; if declined, use the same skills through internal subagents. Their results supply a dimensioned model, source comparisons, access findings and the needed physical fit measurement. A rendered fit remains a digital result.

### Example 2: USB dial box, a temporary review team

**Made-up project:** A USB microcontroller reads two rotary sensors and a button. The board is soldered, but a proposed enclosure and detachable harness have not been built.

**Prompt:** “Engineering Companion, review this USB dial box using temporary agents for Fit Review, Wiring Design and Engineering Test. Read the existing plan and completed-board drawing. Check enclosure access, actual connector mating and whether the guide covers sensor calibration and host input. Preserve the completed board during this review and return one prioritized correction plan here.”

**Useful skills:** `fit-review`, `wiring-design` and `engineering-test` inspect independent aspects. `circuit-design` handles an identified electrical defect; `sensing-calibration` defines usable dial range; `firmware-control` addresses an acquisition or USB issue. The coordinator selects follow-up owners from the findings.

**Expected result:** Concrete conflicts and corrections tied to the supplied artifacts, with performed checks separated from proposed bench work. This launches temporary workers only when the user actually submits the prompt, not permanent project chats.

### Example 3: Camera slider, dedicated engineering chats

**Made-up project:** A compact tabletop camera slider needs a mechanical carriage, motor drive, position sensing, wiring, embedded control and a complete build procedure. An app project called `camera_slider` has already been registered against its workspace.

**Prompt:** “Engineering Companion, start the existing camera_slider project. Use the nine work areas from Engineering System, reuse suitable existing chats, and give each its dedicated skill, concrete goal, owned files and completion evidence. Start with current requirements and high-risk interface review, sequence dependent work, collect their reports here, and carry needed corrections to affected owners.”

| Work area | Example goal |
| --- | --- |
| 01 Mechanisms | Compare transmissions against supplied load, travel and speed requirements. |
| 02 CAD | Model the selected carriage and retainers using actual component interfaces. |
| 03 Fit | Check swept carriage travel, camera access, mounting stacks and service removal. |
| 04 Circuits | Develop the motor/sensor power and driver plan with justified component choices. |
| 05 Wiring | Specify the complete connector chain and moving harness reach/relief. |
| 06 Sensing | Define position conversion, calibration range, error and invalid readings. |
| 07 Firmware | Implement movement, acquisition, commands and recovery against the received interfaces. |
| 08 Testing | Plan independent travel, repeatability, limit and integration checks with observable criteria. |
| 09 Assembly | Combine received work into one construction and bring-up walkthrough. |

**Expected result:** Recommend the nine relevant work-area chats in the project containing this chat and obtain the single creation confirmation unless already given. Then create/reuse them and collect actual specialist evidence; declining selects internal specialist workers for the same scope. Chat creation is not completion. The full team need not run concurrently; dependent work receives its inputs first. Missing chat capability or project binding uses skill-loaded internal subagents. Only missing all worker tools or an explicit instruction against delegation uses sequential loaded-skill execution.

### Example 4: Unknown cable mechanism, reverse engineering

**Made-up project:** A low-voltage cable mechanism is supplied as photographs, a short movement video and a few dimensions. Its internal return arrangement is unknown.

**Prompt:** “Help me reverse engineer this hardware. Build a functional overview from the supplied evidence, compare plausible return mechanisms, and identify the inspection or measurement that would distinguish them. Use Mechanism Design and Fit Review, then 3D Builder only for useful bounded diagrams. Keep a reconstruction of the original separate from a proposed replacement; revise the explanation when new evidence arrives.”

**Expected result:** The coordinator prepares source-specific mechanism/fit questions and offers the one chat/subagent choice unless the route is already resolved. Specialist results supply a functional diagram, competing explanations with evidence limits, useful geometry and a targeted next test. No invented hidden part, exact spring preload or claim that the rendered mechanism is the recovered original.

For a packaged JavaScript/Electron application, use `rea` instead. The hardware reconstruction team is not required merely because the task is called reverse engineering.

### Specialist routing and one creation choice

The recommended route applies to any substantive engineering specialty question, not just a project kickoff. Engineering Companion asks its coordinator to load the relevant skills and read the task material before proposing a concrete assignment. A focused circuit question can use one circuit worker; a complete device can use all nine work areas. The default destination is the project containing the current chat, even when a source file comes from another project.

The one choice is: “This question is better handled by [specialists] to investigate [specific question]. May I create or reuse their agent chats in [current project]?” Options are **Project agent chats (Recommended)** and **Specialist subagents here**. A direct request to create the team already confirms it. Do not repeat the choice per chat, correction or scoped follow-up, and do not treat silence as approval.

If the user declines new chats or says keep it here, the coordinator spawns skill-loaded internal subagents, even for one specialist question. The companion collects and combines their results rather than reverting to a generic solo answer. Planning-only/read-only limits remain on the workers' actions. An instruction against all delegation or unavailable worker tools uses a disclosed sequential loaded-skill fallback. A quote or a request to edit these instructions does not itself launch engineering workers.

Every assignment includes the exact skill path, current project/MOC, engineering question, component/interface and known values with units, source paths/locators, current decisions/completed work, scope, owned output and completion evidence. Workers actually read the selected skill and relevant sources, then return the inputs used and results. Missing project binding uses in-chat specialists; it does not move the team into a source file's project.

### How to continue a project

1. State the changed objective, new evidence or desired result in the companion chat. Existing preferences and answered questions should be reused.
2. The coordinator refreshes only relevant context, gives affected owners their assignments, and sequences shared-file changes.
3. Specialists return the result, changed artifacts/interfaces, checks performed and limits, unresolved questions and next owner/action.
4. The responsible creator corrects an identified mismatch and another appropriate specialist checks the consequential result. The companion explains the combined state.
5. Keep only useful current assignments and technical context in the project's existing AI Notes. Use the capture skills for requested Research Log updates.

A request such as “The motor changes, please reassess the affected design” can change mechanism, mounting, wiring, power, sensing and control assumptions. Revisit those dependencies rather than preserving an obsolete choice. A documentation-only repair should preserve completed hardware unless a concrete defect calls for a change.
