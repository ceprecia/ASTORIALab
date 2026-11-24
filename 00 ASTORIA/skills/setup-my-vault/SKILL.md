---
name: setup-my-vault
description: >-
  Starts first-time setup or routes an existing ASTORIA vault to the updater.
  Owns first-time setup: the researcher interview, first read-back and me.md,
  then Basics, chosen systems and research groups, optional supplied skills,
  and scoped organization through the second read-back. Builds and checks the
  approved selection, finishes the loader, and retains the README. A manual
  path keeps Basics usable without Python or PyYAML. Native mounts remain optional.
  Resumes from the files if the chat was interrupted. Triggers: set up my
  vault, get started with this vault, continue my setup, start the vault
  setup.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: me-builder, vault-builder, skills-janitor, vault-janitor, folder-janitor, skill-builder, bridge-maker, astoria-updater
  created: "2026-09-24"
  updated: "2026-11-23"
---

# Setup My Vault

**"Set up my vault"** is the entry point in either the new download or the
working vault. When the branch is not already explicit, start with this exact greeting:

Hello! I'm here to help you set up your Obsidian vault using the ASTORIA starter vault. ASTORIA stands for Adaptable Scientific Toolkit for Organized Research with Interchangeable Agents. Are you setting up ASTORIA for the first time, or updating an existing ASTORIA vault?

Wait for the answer before continuing. Reuse an already explicit first-time or
update choice. For "continue my setup", recover the files and confirmed answers,
resume at the unfinished stage or interview round, and do not repeat the greeting,
entry question, answered rounds, or completed read-backs.

- **First-time setup:** Continue below in the confirmed setup folder. If the
  current vault is already set up, ask which fresh folder to use. When setting
  up in another Obsidian vault, verify that it has the starter's `00 ASTORIA/`
  and review any existing root `AGENTS.md` before replacing it.
- **Update an existing vault:** Read `00 ASTORIA/skills/astoria-updater/SKILL.md`
  from the open folder to locate and verify the incoming release before any
  setup interview or writes. Then read that verified release's updater in full
  and follow it through the update and its post-update checks. Reuse the
  confirmed folders and decisions when handing off.

This skill talks to the user during setup; the builders and janitors it calls
never do.

## State

The files are the state. Check them first and resume at the first stage that is not done:

| Condition | Meaning |
| --- | --- |
| `AGENTS.md` matches the shipped setup-pending draft | setup not finished; a custom instruction file is preserved for review |
| `me.md` missing | Stage 2 pending |
| root folders from the vocabulary `roots` missing | Stage 4 pending |
| `00 ASTORIA/agent_notes/layout.md` missing | Stage 4 pending |
| `00 ASTORIA/specialized_skills/` is present | uninstalled reference shelf; its presence does not activate extras or indicate unfinished setup |
| scripted selection is recorded in `00 ASTORIA/selection.json` | verify the selected systems, research groups, installed skills and dependency helpers against the files |
| `AGENTS.md` is the full loader and the selected installed skills and required files/folders pass their checks | setup done; keep README.md and do not run again |
| native skill mounts are absent, declined, or failed | optional convenience only; finished core setup stays finished |

When resuming, verify the files and confirmed choices, say what is already done, and continue only unfinished work. File presence is evidence to inspect, not permission to overwrite or a guarantee that every field is complete. Read an existing root `me.md` fully before any setup interview or write. If it is unreadable, report that and stop. Preserve its verified and custom content; setup-pending instructions do not make it a disposable template. Missing or failed mounts never reopen the build, restore the draft loader, or invalidate completion.

## Boundaries

Rules for the whole conversation:

- **Choices, not forms.** Use concise option questions with "other" where useful; a system or research-group multi-select may show its full relevant list. Use the app's option prompt when available, otherwise a numbered list. Ask one round at a time, reuse known answers, and do not present the whole interview at once.
- **Two read-backs.** One after the interview, one after the structure and toolkit choices. No other approval steps.
- **Unknown is allowed.** Use supplied answers and defaults the user actually selects or confirms in the read-back. Leave unanswered personal facts, tastes and preferences unspecified; do not infer them from the author, filenames or a template. Functional folder and Basics choices are shown in read-back two.
- **Preserve existing content.** Keep retains existing roots and content in place. A separately requested root rename is a distinct exception: include its exact moves and reference repairs in read-back two, and describe those moves instead of calling that scope "no moves". Tidy or Propose likewise executes only its approved concrete plan. Preserve notes, packages, decisions, logs and explicit holds.
- **Reporting form:** Follow the recipient's requested deliverable or reporting policy. Do not create additional audit or record files unless explicitly authorized.
- **Tone.** Neutral and brief until the user picks a tone in Stage 2; their choice from then on. Follow any emoji preferences the recipient selects for prose and headings.
- **The builders' rules apply.** Read each builder's `SKILL.md` before calling it; read `me-builder/references/interview.md` before Stage 2.

Edge cases:

- **The vault is already set up** (full loader and verified core files/folders). Say so; route a requested preference/layout change to its owner, or a requested mount to optional skill-mount. Do not repeat setup because native discovery is missing.
- **The user wants to skip the interview.** Reuse an existing verified `me.md` without replacing its content. If it is absent, prepare a minimal briefing with only supplied identity and the functional vault instructions; omit unknown personal details. Use read-back one for this bounded result, then continue to the structure and selection choices. Missing preferences can be supplied later.
- **No external research folder.** Skip the map of their work and preserve existing Current Projects and Areas entries. Leave that section empty in a new briefing when no entries were selected.
- **A chosen group has no skills in the catalog.** Say so; nothing to install for it.
- **No Python, PyYAML, or script execution.** Use `./references/manual_setup.md`. The shipped Basics remain usable. Apply optional choices manually only when their whole dependency closure and views can be verified; otherwise preserve them as pending rather than calling them installed. Report unrun checks. Do not install a runtime or package automatically.
- **Windows without symlink support.** The shims are inert; say so and move on. `AGENTS.md` still works.

## Stage 1: orientation

1. List the vault root to verify access. If the listing fails, ask the user to connect or open that folder and stop. Follow [Check toolkit state](references/manual_setup.md#check-toolkit-state) before a setup write or a fresh installer list or preview. A pending installation is recovered through its original approved command, not a new preview or a manual bypass.
2. Notice which app you are in from your tools (Cowork, Claude Code, Codex, Antigravity, other).
3. Quietly check for an existing Python 3 runtime in the current app: `python3`, `python` when its version is 3, or `py -3` on Windows. Verify that the app can run it and that the same interpreter can import `yaml` from PyYAML. The vocabulary stays in YAML; scripted setup needs Python 3 and PyYAML. If a dependency or execution is unavailable, explain the manual option for a fresh plan. Before switching a resumed build, follow [Check the approved plan](references/manual_setup.md#check-the-approved-plan); preserve any incompatible or unverifiable approved work as pending. The commands below show `python3`; use the verified launcher instead when different. Do not install software or add an approval round for this check.
4. Briefly explain the interview, the two read-backs, and the build. Choices can change later. Existing content stays in place unless the user selects and approves a concrete organization plan. Keep runtime/package details out of the introduction and do not promise scripted checks in manual mode. Continue to the first unanswered interview round without another readiness question.

## Stage 2: the researcher interview and the me file

1. Read `00 ASTORIA/skills/me-builder/references/interview.md`. Reuse answers and existing verified briefing content; ask only the unanswered relevant parts of its four rounds. A reference default does not supply an unknown personal fact or preference. If the user skips the interview, follow the minimal-briefing rule above.
2. Read-back one: "Here is what I will write into your me file", showing supplied answers, explicitly accepted defaults, unspecified fields and the exact supported changes. For an existing briefing, identify what stays and limit the proposal to the requested missing or corrected material. Wait for one yes or corrections; apply corrections in place.
3. Call [me-builder](../me-builder/SKILL.md) with those confirmed answers. Use new-vault mode and its template only if root `me.md` is absent. Otherwise use a bounded refresh and preserve unrelated content; never overwrite an existing briefing merely because setup is pending. A separately explicit new-file rebuild retains its own stated scope.
4. Greet the user from the written file, in the chosen tone and address form: who they are, what they work on, one thing about how you will behave. Read it from `me.md`, not from the chat.

## Stage 3: structure, toolkit, and the map of their work

Nothing is written in this stage.

Before asking about folders, introduce PARA briefly. Projects have a finish
point. Areas are ongoing responsibilities. Resources hold reusable references.
Archive holds inactive material. Show one simple example, such as:

```text
03 Projects
├── Research project
└── Writing project
04 Areas
├── Coursework
├── Lab operations
└── Community outreach
05 Resources
├── Ebooks
├── Code
├── Manuals
└── Hobbies
06 Archive
```

Use generic examples fitted to the work the user shared. The tree illustrates
choices. Create folders or map notes only for items the user accepts.

**Structure.** First question: default layout, or personalize it? The default is the vocabulary `roots` with the `layout` subfolders. If personalized, ask as options with the default shown: working root names (keep, no emoji, no numbers, or custom words) with `00 ASTORIA/` fixed, which optional roots to keep (Inbox, Calendar), note naming (snake_case; spaces), and date format. Keep preserves any existing roots. If the user separately requests a root rename, preview the exact current-to-proposed moves with the existing `rename_roots.py` command without `--apply`, and include its affected references in read-back two. Distinguish creating a missing root from moving an existing one. Do not silently combine Keep with root moves. Offer writing-style profiles only with the relevant selected writing capability. In manual mode, explain which choices can be applied and verified now and which must remain pending.

**Systems and research toolkit.** Basics includes the Research Assistant System, Janitor System and ASTORIA System Builder, plus the exact shared helpers their workflows require. A dependency helper does not select the whole Writing System. Offer **Basics only**, the five optional systems below, and **Help me choose**. For Help me choose, use the existing interview answers to recommend a small selection and let the user adjust it; do not enable every system by default.

| Optional system | Useful when | Installer ID |
| --- | --- | --- |
| Writing | Sustained document development, writing review and style work | `writing` |
| Study and productivity | Structured study and planning | `study` |
| Teaching | Teaching support; course configuration follows the later syllabus workflow | `teaching` |
| Engineering | Research hardware and technical development | `engineering` |
| PhD and career | Degree milestones, mentoring and career development | `phd` |

With a verified runtime, use `python3 "00 ASTORIA/skills/skills-janitor/scripts/install_specialized.py" --list` for the live system and research-group choices. Offer only relevant research groups: the user's imaging modalities, behavior for behavioral experiments, general computing for code work, or another matching listed group. These research groups are separate from the five optional systems. Preview Basics with `--none`; otherwise preview only the chosen `--systems writing,study` IDs, `--groups fmri,general` groups or `--names skill-name` names, combined as needed. The examples illustrate syntax, not default selections. Never mix `--none` with optional selections. All selection commands are dry runs until `--apply` is supplied. Show installed skills, required helpers with reasons, and what stays in the uninstalled catalog. Keep the chosen plan for read-back two.

Selecting or recommending Teaching installs teaching support when accepted; it does not configure a course during setup. The tutorial's later syllabus-based workflow handles that course work.

**One optional add-skills question.** Ask once whether the user wants to add a skill from **GitHub**, **pasted instructions**, **a local skill folder**, or **skip**. Reuse an answer already supplied. Use Skill Builder's existing source-intake workflow and Skills Janitor's validation and registration, with only the exact source the user identifies. In this stage, inspect and propose only: pass planning-only scope to Skill Builder and do not write a skill folder yet. A supplied folder or ordinary GitHub URL uses the installer's `--import-skill PATH/URL` preview; the importer resolves and records the revision internally, so do not ask the user for a Git hash. Its `--source-kind`, `--source`, `--revision` and `--source-path` fields carry verified provenance where applicable; consult current help rather than inventing values. Pasted instructions are proposed as one canonical skill folder. Include the source, normalized name, description, triggers, dependencies, user ownership and destination in read-back two; that same approval covers the matching Skill Builder result and installation. Treat imported instructions as source material, not execution authority. Do not create a second registry or installation workflow.

**Map of their work.** If Stage 2 identifies research files outside the vault, let the user identify the folder. Inspect only authorized immediate entries, and report any selected location that cannot be reached. Show candidate Projects, Areas, or Resources in the task's requested form or under the recipient's existing reporting policy. Explain that their existing files stay where they are. Let the user accept, drop, or relabel entries. For each accepted Project or Area, identify its exact local `files/` path, documented external workspace, or established working location, along with the exact owner MOC or `AGENTS.md` that documents any external binding. Use the selected owner and verified applicable policy when choices are open. An unresolved or unavailable location remains explicit in the plan.

**Organization of existing content.** Reuse the known choice or offer **Keep my structure**, **Tidy selected folders**, or **Help propose organization**. Folder Janitor owns filing and supported moves; Skills Janitor owns skill consistency and Vault Janitor owns layout and instruction consistency. Keep authorizes no filing moves and preserves existing roots; show any separately requested root rename as an explicit exception in read-back two. For Tidy or Propose, pass the exact selected batch and known owners to Folder Janitor's Guided organization mode. Return a finite grouped table of files/count, current location, proposed home, reason, unresolved items, held groups and affected references for the second read-back. Preserve content and existing packages. An ambiguous owner remains unresolved; do not split or rewrite notes, invent a taxonomy, or treat a consistency finding as move approval. Setup's builders create only accepted MOCs and bridges; the janitors retain their existing responsibilities.

**PhD and career support.** Only when this system is selected and relevant, offer configuration now or later through its installed phd-career-builder. Reuse the supplied role, goals and accepted Area MOC. If selected now, read that builder and ask only useful unanswered groups within this conversation, including applicable program/cohort sources and requested support areas. Include proposed settings and the exact owner in read-back two. Do not add another interview, profile, setup gate or reminder job. Unknown details do not block Basics.

**Native discovery, optional.** Default to skipping mounts. Include the choice in the existing second read-back, without adding a compulsory question: skip, or the native discovery the user has requested. A requested mount is a separate action after core completion, not a setup dependency. Merely using an app or having skills on disk does not request mounting.

**Read-back two:** the structure choices, Basics and chosen systems/research groups, exact dependency helpers, supplied-skill sources, descriptions, triggers and ownership, accepted PARA owners, the concrete organization plan or Keep, and optional native discovery. Distinguish immediately verifiable manual actions from pending choices. Wait for one yes or corrections. This approval covers only this displayed scope and its ordinary checks; do not ask again for the same skill installation or filing plan.

Include only any PhD settings actually selected above in this same read-back, with unanswered fields left unknown.

## Stage 4: the build

One run within the confirmed scope. Follow [Check toolkit state](references/manual_setup.md#check-toolkit-state) and [Check the approved plan](references/manual_setup.md#check-the-approved-plan) before continuing writes. Use the scripted steps only with verified Python 3 and PyYAML. A manual build must be compatible with the recovered approval; a capability gap does not authorize silently reducing that scope. Report completed steps, hold only affected unresolved work, and continue independent authorized work. Build and check the selected usable vault before Stage 5. Do not mount skills in this stage or add another approval round.

1. **Names.** Apply only the layout changes shown in read-back two: `python3 "00 ASTORIA/skills/skills-janitor/scripts/rename_roots.py" <flags> --apply`, then `lint.py`. Flags: `--no-emoji`, `--no-numbers`, `--set role=name`, `--drop role`. Keep preserves existing roots unless the user separately requested the exact root moves included in that read-back. Report any such approved exception as moves; do not claim the whole run moved nothing. No additional approval is needed for that same concrete scope.
2. **Folders.** `python3 "00 ASTORIA/skills/setup-my-vault/scripts/create_layout.py" --apply` creates the roots and the layout subfolders from the vocabulary, skipping dropped roots.
3. **Skills.** Apply the exact installer commands previewed in read-back two, adding `--apply`: `--none --apply` for the Basics release selection, or only the selected `--systems`, `--groups` and `--names` values. Do not mix `--none` with an import or other optional-selection command. Apply a supplied folder or GitHub skill through `--import-skill PATH/URL`. For an approved pasted workflow, Skill Builder writes the canonical folder, then the installer records user ownership with `--register-skill NAME --source-kind workflow --source pasted --apply`. Verify `00 ASTORIA/selection.json` against the actual installed folders, including required helpers and user-owned imports. The installer rebuilds views and checks the selection. Retain the uninstalled catalog; its contents do not activate additional systems.
4. **Projects and areas.** Follow the approved plan for each accepted project. Reuse a verified existing MOC when selected. If the plan leaves the hub open, reuse the verified existing MOC identified by the applicable project policy. If the approved plan calls for a new MOC, use its selected path and template. Where the plan leaves those open, follow the verified applicable project or recipient policy. With no selected convention, create `<projects root>/<project>/MOC <project>.md` from `00 ASTORIA/templates/Research Project Template.md` for research or `Projects Template.md` for other work. Fill only the supplied title, one-line description and `workspace:` path. On the approved owning project MOC, use the top-level frontmatter property `astoria_role: project_moc`. Keep this property from the selected template when creating the MOC. For an existing note, add the property only when that exact edit was approved. Preserve its body and other properties, and leave an identical property in place. If a property conflicts or another direct note has the same role, report the conflict and preserve both notes. Leave nested or external selected notes at their approved paths and report the discovery limit. For newly created project MOCs, apply the confirmed Stage 2 heading style using the selected template's mapping. For a research MOC, also apply the confirmed Stage 2 callout preference. For a new nonresearch MOC, follow the approved navigation and link form, then the verified applicable project or recipient convention where that choice is open. Use the illustrated three-callout opening only when the resolved form calls for it or navigation remains open. If the resolved plain Markdown form omits callouts, keep the supplied brief in ordinary Markdown and include only its applicable navigation. Verify each retained navigation label and fragment against its actual heading. If a project bridge names AI Notes, verify and use the exact rendered heading. Keep the Stage 3 folder choices and project paths. For each accepted Area, reuse the verified existing owning MOC named in the approved plan. If the plan leaves the existing owner open, use the applicable verified Area convention. When the plan authorizes creating a note, use its selected path and template, then the applicable verified convention if those choices remain open. Use `<areas root>/<Area>/<Area> MOC.md` and `Base Template.md` as fallbacks when no other convention was chosen. On an approved new Area MOC, use the top-level frontmatter property `astoria_role: area_moc`. For an existing note, add that property only when the exact edit was approved. If the approved scope leaves a custom-named direct note unmarked, keep it and report that layout discovery needs the role. Preserve its content and other properties and leave an identical property in place. If there are competing markers or a conflicting property, report the gap and preserve the notes. Keep an approved nested or external note at its selected path and report that it falls outside generated direct-folder discovery. For a new MOC, add the supplied title and one-line purpose and apply the approved template. Include an empty AI Notes section when the selected template or applicable continuity policy calls for one. Use `# AI Notes` for plain headings and `# 🤖 AI Notes` for the illustrated emoji style, or follow the confirmed heading preference. When an existing MOC section is the selected continuity location, verify its actual heading without rewriting the note. For each accepted Project or Area, use Bridge Maker for its one `AGENTS.md` pointing to root `me.md` and the verified MOC. For a selected external workspace, reuse its exact existing binding in the owner MOC or `AGENTS.md`. If the plan approves an owner entry, document the exact selected path in that file, using `workspace:` when the MOC's format supports it. Preserve unrelated instructions and conflicting bindings pending resolution. Record path availability separately from the approved binding. If the location cannot be reached, preserve the path, report it as unavailable, and leave the existing files in place. Create or reuse the single approved local `files/` folder only when the plan chooses that local arrangement. Preserve any established working location chosen in the plan. Keep reusable references in Resources. Add a verified MOC link only when its edit is within the approved scope. Preserve external source files and established scientific layouts. Read each template before instantiating it.
   For an approved organization plan, have Folder Janitor execute only that plan and its supported reference repairs after the accepted owners exist. Keep means no filing moves. Verify moved content and repaired links together; preserve held or unresolved groups and return actual results.
5. **Me file, second pass.** Call me-builder for the accepted additions or corrections in `## Current Projects and Areas` and `## Working Locations`. Also persist the ordinary note-name and filename-date choices confirmed in read-back two in the briefing's existing appropriate conventions field, or the context selected in that read-back. Do not require a particular `## Rules` heading or File naming field in a customized briefing. Preserve unspecified preferences, technical record formats, unrelated existing projects, locations and custom wording, including `### Pipeline layout`; the accepted list does not replace the rest of an existing briefing. This uses the same approved second read-back without another gate.
   If PhD settings were approved in read-back two, call phd-career-builder after the accepted MOC exists, passing those exact settings, source links, owner and approval. Save only that approved scope in its existing sections, without another confirmation. Otherwise leave configuration for later.
6. **Layout.** Call [vault-builder](../vault-builder/SKILL.md): it runs `build_layout.py`, fills the purpose lines the report asks for from the accepted projects and areas, and writes `00 ASTORIA/agent_notes/layout.md`. Then write `00 ASTORIA/agent_notes/ai_log.md` from `00 ASTORIA/templates/ai_log_template.md` with one first entry naming what setup did.
7. **Check.** Call [vault-janitor](../vault-janitor/SKILL.md) with fixes authorized for anything the build produced; call [skills-janitor](../skills-janitor/SKILL.md) (`lint.py` and `build_views.py --check`).

If a step fails, stop, report the step and the error, and leave the files as they are; the state table tells the next session where to resume.

### Manual build

Use the same interview, Basics, selected systems and organization conversation, and second read-back. Follow `./references/manual_setup.md`; do not add an approval round or silently downgrade the user's choices. Keep the shipped Basics and uninstalled shelf. Install optional choices manually only if complete folders, dependencies and matching views can be verified; otherwise report those exact choices as pending. Apply only the organization plan approved in read-back two, through the same owners and preservation rules. Use Vault Builder's manual first-setup exception. Report manual checks and unrun automated checks, then continue to Stage 5 without mounts.

Apply any PhD settings already approved in the same read-back through phd-career-builder after their accepted MOC exists, just as in the scripted build. If there is no chosen owner, leave the configuration unsaved and pending. Report the pending item in the current task's requested response form or under the recipient's existing reporting policy. Complete the core setup without creating a profile for it.

## Stage 5: finish the usable vault

With the scripted build, run `python3 "00 ASTORIA/skills/setup-my-vault/scripts/finish_setup.py" --apply`. It checks the required files, folders and recorded installed selection, writes root `AGENTS.md` from `00 ASTORIA/templates/agents_loader_template.md`, and retains `README.md`. A verified uninstalled catalog is allowed; catalog absence is not a completion requirement.

In manual mode, verify the manual file/link checks above, retaining the uninstalled optional catalog, copy the loader template over the draft root `AGENTS.md`, and keep `README.md`. Preserve a customized instruction file for review rather than overwriting it blindly. Preserve all other files. Report manual file/link checks and the automated checks that were not run.

The vault is now usable and setup is complete without mounts. Completed setup is the full loader plus verified core files and folders; README presence is not a setup-state signal. Do not check for native discovery as a completion condition.

In the chosen tone: what exists now (the three core files, any project MOCs, the core or selected toolkit, and verified references to outside work); three phrases to try that match their goals ("help me scout the field on <topic>", "start a research session on <project>", "summarize this paper"); where to change their mind later ("update my me file", "rename my folders", "refresh the vault map"); and that optional skills and native mounts can be added later. A specialized or add-on skill is installed as its whole folder in `00 ASTORIA/skills/`, with dependencies and generated views checked through skills-janitor when the required runtime is available. In manual mode, state the unrun automated checks without calling the core setup incomplete. Continue to a requested optional mount without asking another setup question; otherwise close directly.

## Stage 6: optional native discovery after completion

Skip this stage unless the user requested mounting, including through the existing second read-back. Load [skill-mount](../skill-mount/SKILL.md) only for that optional handoff. Use its dry run and requested scope; a core set is sufficient for the companions and part coordinators. Registry-platform registration follows that skill's adapter from a session with the required capabilities; do not treat it as a core setup action.

If mounting is declined, unavailable, or fails, report that optional status and keep the completed loader and vault intact. Do not rerun setup, alter its README, require software installation, or delay use of the vault. The direct `AGENTS.md` route remains available.

After the optional action, or immediately after Stage 5 when it is skipped, give the closing line in the chosen tone and the one handoff question: what do you want to work on first? Read `me.md` and route the answer through its Skills table.
