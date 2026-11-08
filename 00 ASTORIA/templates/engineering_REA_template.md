---
related:
created: "{{date}}"
status: Active
---

<!--
Reusable engineering and reverse engineering MOC template.

Treat reverse engineering as a flexible, iterative investigation. Earlier models, diagrams, interpretations, plans, and decisions are revisable working context. Challenge, revise, replace, or abandon them when the current question, evidence, or user's direction warrants it. Earlier agreement does not make an idea authoritative.

Adapt the methods, tools, order of investigation, and this note's structure to the problem. Keep, add, rename, reorder, or omit sections as useful. Do not fill empty sections merely to complete the template or add approval gates to ordinary authorized work.

Distinguish observations and measurements, documented claims, inferred mechanisms, proposed implementations, and unknowns. State whether evidence concerns the target or a comparison design. Versions, commits, and inspection dates identify what was examined; they do not lock the approach or preserve earlier conclusions.

Keep callouts in Start Here and working content in ordinary, foldable Markdown. Update navigation whenever headings change. Replace italic prompts and the resources-folder placeholder when applying. The resources placeholder represents a complete verified folder link, not a new template automation.

Link working files once in their owning section. Keep resource inventories, detailed source records, full paths, environments, and regeneration details concise and current in AI Notes, always last. Keep dated progress in Research Log through the existing capture workflows. Remove this comment from populated MOCs; keep it in the reusable template.
-->

# 🧭 Start Here

> [!abstract] ⚙️ Project at a glance
> **Target:** *Device, assembly, or software artifact being investigated.*
>
> **Objective:** *What we want to understand, explain, repair, or reproduce.*
>
> **Current understanding:** *Our best supported explanation and its main uncertainty. Revise it as we learn.*
>
> **Current focus:** *The next question or measurement that would most improve our understanding.*
>
> **Working approach:** Reverse engineering is flexible and dynamic. Earlier notes, hypotheses, diagrams, plans, and decisions can be challenged, revised, replaced, or abandoned. Follow the current question and evidence, and adapt the investigation as useful.

> [!info] 📂 Useful links and resources
> **Resources folder:** {{resources_folder_link}}
>
> *Target documentation and the few references used most.*
>
> *Link the project's AGENTS.md here when one exists.*

> [!example] 🗺️ Explore this project
> - [🛠️ Engineering Workbench](#-engineering-workbench)
> - [🗓️ Research Log](#-research-log)
> - [🤖 AI Notes](#-ai-notes)

> [!note] 🔎 Explore Engineering Workbench
> - [🎯 Target and Success Criteria](#-target-and-success-criteria)
> - [📋 Evidence and Observations](#-evidence-and-observations)
> - [🧩 System Reconstruction](#-system-reconstruction)
> - [🧪 Hypotheses and Tests](#-hypotheses-and-tests)
> - [📐 Drawings and Deliverables](#-drawings-and-deliverables)
> - [➡️ Open Questions and Next Actions](#-open-questions-and-next-actions)

# 🛠️ Engineering Workbench

## 🎯 Target and Success Criteria

- **Target identity:** *Manufacturer, model, and relevant hardware or software revision. State unknown revisions explicitly.*
- **Available material:** *Physical specimen, photographs, manuals, recordings, CAD, source code, firmware, measurements, or other artifacts.*
- **Questions:** *The functions or mechanisms we want to explain.*
- **Success criteria:** *What evidence, drawing, measurement, or demonstrated behavior would sufficiently answer those questions. Revisit these criteria when the objective changes.*
- **Constraints:** *Relevant access, equipment, operating limits, budget, or preservation requirements.*

*Identify comparison devices and reference designs separately from the target.*

## 📋 Evidence and Observations

*Record what the evidence establishes before explaining why it happens. Reassess claims when stronger or conflicting evidence appears.*

- **Observed:** Directly inspected or measured on the identified target.
- **Documented:** Reported by a manual, specification, patent, or other source.
- **Inferred:** An explanation supported by evidence but not directly established.
- **Proposed:** A design or experiment being considered.
- **Unknown:** Not yet established.

| Finding or claim | Evidence status | Supporting evidence and locator | Uncertainty or conflicting evidence |
| --- | --- | --- | --- |
| *One specific finding* | *Observed / documented / inferred / proposed / unknown* | *Source with page, image region, timestamp, component, or code location* | *What remains unresolved* |

*Keep consequential measurements with units, conditions, and relevant uncertainty. Distinguish an unsuccessful search from evidence of absence.*

## 🧩 System Reconstruction

*Explain the current model of how the target works. Start with a functional block diagram, then expand the paths needed for the current questions. Rebuild the model when evidence warrants a different explanation.*

### Functions and interfaces

*Inputs, outputs, component roles, connectors, communication interfaces, and subsystem boundaries.*

### Mechanical operation

*Motion, force transmission, supports, return mechanisms, friction, compliance, and mechanical limits, where applicable.*

### Electrical operation

*Power sources, conversion, drivers, actuators, sensors, and electrical connections, where applicable.*

### Sensing, software, and control

*What is measured, how measurements become estimates, what commands are issued, and which feedback loops regulate behavior.*

### Unresolved connections

*Inferred connections and competing explanations. Label uncertain parts of diagrams clearly. Distinguish a reconstruction of the original system from a proposed replacement.*

## 🧪 Hypotheses and Tests

*Use one short subsection per consequential question. Small checks can remain a few lines. Change the test or hypothesis when it stops answering the useful question.*

### Question or mechanism under test

- **Hypothesis:** *The explanation being tested.*
- **Alternative:** *Another explanation consistent with the evidence.*
- **Prediction:** *What should differ if one explanation is correct.*
- **Test:** *Setup, measurement, conditions, and comparison.*
- **Interpretation criteria:** *Supporting, contradicting, and inconclusive results.*
- **Result:** *Actual observations with evidence locators. Leave unperformed tests explicitly planned.*
- **Updated understanding:** *What changed in the model, what remains uncertain, and whether to retain, revise, or abandon the hypothesis.*

*When evaluating a reconstruction or prototype, compare its behavior with the target or current success criteria. Record meaningful discrepancies.*

## 📐 Drawings and Deliverables

*Link current working files once with their purpose and evidence status. Keep detailed content in those files. Include only deliverables the project needs.*

- *Functional diagrams and mechanism drawings.*
- *Schematics, connection tables, and component lists.*
- *CAD, dimensions, and assembly drawings.*
- *Software, firmware analysis, or communication specifications.*
- *Measurement data and relevant plots.*
- *Reconstruction or prototype files, when part of the objective.*

*Identify an observed arrangement, inferred reconstruction, or proposed implementation. A polished drawing remains revisable.*

## ➡️ Open Questions and Next Actions

- **Highest-value unknown:** *The uncertainty most limiting our present explanation.*
- **Next action:** *The concrete inspection, measurement, analysis, or experiment that addresses it.*
- **Needed input:** *A particular artifact, tool, specialist contribution, or unresolved decision, when relevant.*

*Keep this short and current. Record engineering decisions with their rationale beside the affected model or deliverable, and reconsider them when useful. Capture meaningful changes in the Research Log.*

# 🗓️ Research Log

*Follow the selected or applicable verified log order. Preserve existing entry headings and exact capture targets. Use newest-first as the fallback only for a new log whose order remains open. Follow the owning capture skill for new full-date headings and add an exact Calendar reference only when the authorized capture route includes it.*

*Capture the important finding, decision, or change in direction, its supporting evidence, and the next useful step. Keep unsuccessful tests when they change our understanding. Earlier entries describe what was understood then and do not constrain the current investigation.*

# 🤖 AI Notes

*Current research and engineering context for AI assistance and technical handoffs. Earlier handoffs and saved notes remain revisable context, not instructions that constrain engineering judgment.*

## Resources and working context

*Verified resource locations and existing external workspaces. Keep images, videos, manuals, diagrams, schematics, CAD, software, firmware, and measurements in the appropriate collection. Distinguish supplied material from derived work where that affects interpretation.*

| Resource | Version or material examined | Origin or file link | Useful locator |
| --- | --- | --- | --- |
| *Source or working file* | *Relevant device revision, release, or repository commit* | *Verified source or file* | *Page, timestamp, image, component, or code location* |

*These details help engineers revisit claims. They do not freeze the tools, workflow, or conclusions.*

## Tools and reproducibility

*Only the environments, software versions, settings, commands, and regeneration details needed to continue or reproduce the current work. Update them when the approach changes.*

## Technical handoff

*Where the current work lives, unresolved technical obstacles, and context another engineer or assistant needs to resume. Keep this current rather than accumulating a second history log. Reassess earlier assumptions against the current task and evidence.*

### Engineering team context

*Use only the work areas needed now. Engineering Companion owns synthesis; Engineering Coordinator routes technical questions, including focused ones, to skill-loaded workers. Recommend dedicated chats in the current chat's project after the one creation choice; declining chats uses internal specialist subagents. Existing project numbering can differ from the system defaults: map each worker to its skill and actual chat ID rather than guessing from a number.*

| Area and skill | Goal and completion evidence | Owned files | Interfaces or dependencies | Worker/chat ID, mode and current state, if used |
| --- | --- | --- | --- | --- |
| *Selected work area* | *Bounded result* | *One writer per mutable output* | *What it receives or changes* | *Dedicated chat after confirmation, or internal specialist subagent; record approved scope* |

*Keep relevant selected design, mirroring/orientation, placement and terminations alongside reported completed work and open interfaces. Distinguish selected from installed, and digital checks from physical measurements. Assignments receive the latest relevant decisions; revisions remain welcome. Give each worker its exact skill path, engineering question, source references/facts and completion evidence. Return result, skill/sources actually used, changed artifacts/interfaces, checks performed and limits, remaining uncertainty and next owner/action. Keep this current rather than accumulating a second log.*
