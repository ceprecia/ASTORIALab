---
name: setup-my-vault
description: >-
  Starts first-time setup or routes an existing ASTORIA vault to the updater.
  For first-time setup, owns the whole conversation:
  a short orientation, the researcher interview as option questions, one
  read-back, the first me.md through me-builder, structure and toolkit choices
  with a second read-back, then one build run that creates the root folders,
  installs the chosen specialized skills, writes the layout reference and
  the AI log through vault-builder, checks them through the janitors, replaces
  the draft AGENTS.md with the loader, and retains the README. Skill mounting
  is optional after completion, only when requested. A manual core path works
  without Python or PyYAML.
  Resumes from the files if the chat was interrupted. Triggers: set up my
  vault, get started with this vault, continue my setup, start the vault
  setup.
metadata:
  level: skill
  system: ASTORIA System Builder
  dependencies: me-builder, vault-builder, skills-janitor, vault-janitor, bridge-maker, astoria-updater
  created: "2026-09-24"
  updated: "2026-11-08"
---

# Setup My Vault

**"Set up my vault"** is the entry point in either the new download or the
working vault. Unless the user already chose, ask first: **Are you setting up
ASTORIA for the first time or updating a vault you already use?**

- **First-time setup:** Continue below in the confirmed setup folder. If the
  current vault is already set up, ask which fresh folder to use. When setting
  up in another Obsidian vault, verify that it has the starter's `00 ASTORIA/`
  and review any existing root `AGENTS.md` before replacing it.
- **Update an existing vault:** Read `00 ASTORIA/skills/astoria-updater/SKILL.md`
  from the open folder and follow it before any setup interview or writes.
  It locates the other folder and previews the update for approval.

For "continue my setup", resume below without asking the entry question again.
This skill talks to the user during setup; the builders and janitors it calls
never do.

## State

Check the files first to identify completed work and find the first unfinished stage.

| Condition | Meaning |
| --- | --- |
| `AGENTS.md` is the draft (says "setup pending") | setup not finished |
| root `me.md` path vacant | Stage 2 pending |
| existing root `me.md` verified as the user's authoritative briefing | keep it and reuse it for setup. Stage 2 is complete |
| root `me.md` path occupied and the briefing cannot be verified | stop and resolve its identity or access. Preserve the existing entry |
| draft loader and verified `me.md` present, with the Stage 3 plan or approval unavailable | Stage 3 pending |
| root folders from the vocabulary `roots` missing | Stage 4 folder work pending after Stage 3 approval |
| `00 ASTORIA/agent_notes/layout.md` missing | Stage 4 layout work pending after Stage 3 approval |
| toolkit install record present, or a catalog-only skill name already live while setup is pending | check the exact prior toolkit plan, its approval and the supported recovery state before continuing |
| optional catalog present while the draft loader remains | check the approved toolkit plan for remaining work. Manual core may retain a verified uninstalled catalog as reference |
| `AGENTS.md` is the full loader and core files/folders pass their checks | core setup done. Keep README.md and do not run again |
| native skill mounts are absent, declined, or failed | optional convenience only. Finished core setup stays finished |

When resuming, report which stages are complete in the current task's requested form or under the recipient's existing reporting policy. Before any pending Stage 4 work, recover the exact Stage 3 plan and its affirmative second read-back approval from the available setup conversation or an existing setup record you are authorized to read. If both are available, carry them forward and continue at the first unfinished build step without another read-back. Otherwise return to the unfinished part of Stage 3, reuse known choices and complete its second read-back before resuming Stage 4. For a partial build, verify each completed operation against the approved plan and its applicable checks before skipping it. Preserve verified completed work. Missing or failed mounts never reopen the build, restore the draft loader, or invalidate core completion.

## Boundaries

Rules for the whole conversation:

- **Choices, not forms.** Offer the interview's listed options, including omission where offered, plus "other". Use the app's option prompt when it has one; in plain chat print a numbered list. Ask one round at a time (a handful of questions), never one question per message and never the whole interview at once.
- **Two read-backs.** One after the interview, one after the structure and toolkit choices. No other approval steps.
- **Defaults and omissions.** Apply the stated default for a skipped question only when it has one. In the read-back, distinguish confirmed preferences, defaults to apply, and omitted preferences that stay out of the briefing.
- **Nothing of the user's is moved.** Their files stay where they are; the vault indexes them.
- **Reporting form:** Follow the recipient's requested deliverable or reporting policy. Do not create additional audit or record files unless explicitly authorized.
- **Tone.** Neutral and brief until the user picks a tone in Stage 2; their choice from then on. Follow any emoji preferences the recipient selects for prose and headings.
- **The builders' rules apply.** Read each builder's `SKILL.md` before calling it; read `me-builder/references/interview.md` before Stage 2.

Edge cases:

- **The vault is already set up** (full loader and verified core files/folders). Say so; route a requested preference/layout change to its owner, or a requested mount to optional skill-mount. Do not repeat setup because native discovery is missing.
- **The user wants to skip the interview.** If root `me.md` is absent, use the name and applicable defaults for the first briefing and tell them how to fill it later. Reuse a verified existing briefing.
- **No external research folder.** Skip the map of their work and preserve existing Current Projects and Areas entries. Leave that section empty in a new briefing when no entries were selected.
- **A chosen group has no skills in the catalog.** Say so; nothing to install for it.
- **No Python, PyYAML, or script execution.** For a fresh setup, offer the supported manual-core plan before the Stage 3 read-back. For resumption, check the recovered plan against the manual build below and `./references/manual_setup.md` before any manual write. Preserve shipped generated views and report which checks did not run. Do not install a runtime or package automatically.
- **Windows without symlink support.** The shims are inert; say so and move on. `AGENTS.md` still works.

## Stage 1: orientation

1. Verify access by listing the vault root. If access fails, ask the user to connect or open the vault root folder containing `00 ASTORIA/` and stop. For a pending setup, follow the [toolkit state check](references/manual_setup.md#check-toolkit-state) before any setup write or fresh toolkit list or preview.
2. Notice which app you are in from your tools (Cowork, Claude Code, Codex, Antigravity, other).
3. Quietly check for an existing Python 3 runtime in the current app: `python3`, `python` when its version is 3, or `py -3` on Windows. Verify that the app can run it and that the same interpreter can import `yaml` from PyYAML. The vocabulary stays in YAML; scripted setup needs Python 3 and PyYAML. If either dependency or script execution is unavailable, explain the manual-core option for a fresh plan. During resumption, use the approved-plan check before choosing a manual build. The commands below show `python3`; use the verified launcher instead when different. Do not install software or add an approval step for this check.
4. Say, in a few plain sentences: four short steps; questions come as options; everything can be changed later; nothing on the computer is moved. Keep runtime/package details out of the introduction. Use the available script or manual path internally, mention a dependency only if the user needs to act or asks, and do not promise scripted checks in manual mode. Do not repeat the README.
5. Ask: ready to start with you?

## Stage 2: the researcher interview and the me file

Check the exact vault-root `me.md` path before any setup write. Read an existing briefing completely and verify that it is the user's authoritative briefing for this vault. Keep the verified file and use its recorded answers for Stage 3. If the path is occupied and the briefing cannot be read or verified, stop and resolve that gap while preserving the entry. Use the interview and creation steps below only when the root path is vacant.

1. Read `00 ASTORIA/skills/me-builder/references/interview.md`. Ask its four rounds as it describes.
2. Read back every answer and applied default for the proposed `me.md` in the current task's requested form or under the recipient's existing reporting policy. Identify omitted or unspecified preferences separately. Wait for one yes or corrections. Apply corrections in place.
3. Recheck that the root `me.md` path is vacant before calling [me-builder](../me-builder/SKILL.md) in new-vault mode with the confirmed answers. It fills `00 ASTORIA/skills/me-builder/assets/me_template.md` and creates `me.md`. If an entry has appeared, use the existing-briefing check above.
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

**Structure.** First question: default layout, or personalize it? The default is the vocabulary `roots` with the `layout` subfolders. If personalized, ask as options with the default shown: working root names (keep, no emoji, no numbers, or custom words) with `00 ASTORIA/` fixed, which optional roots to keep (Inbox, Calendar), note naming (snake_case; spaces), date format, and whether to select an optional writing-style profile or leave personal style unspecified. In manual mode, explain the complete path with default root names and core skills; defer root renaming and optional toolkit installation until the user chooses to add those capabilities later.

**Toolkit.** For a fresh plan with verified toolkit state and a verified runtime, run `python3 "00 ASTORIA/skills/skills-janitor/scripts/install_specialized.py" --list`. Use the read-only list and preview to plan a fresh selection. If an install is already pending, recover its exact prior plan and approval and use the Stage 4 recovery path. From the methods and software answered in Stage 2, propose groups: the imaging modalities they named, behavior when they run behavioral experiments, general (software adapters and computing usable with any data) when they write code, and any other group the list shows that matches their answers. Include **No optional toolkit; keep the core skills** as an explicit choice that cannot be combined with groups or individual skill names. Show the proposal as a multi-select with the counts from the list, let them adjust, then run the script with `--groups` (dry run), or `--none` for the core-only choice. Show the plan: installed skills, coordinators and dependencies pulled in, what stays available in the repository. Do not substitute an empty group list or `--groups none` for `--none`. In manual mode, show the core-only plan without running the installer. Keep the optional catalog as an uninstalled reference shelf so shipped links remain valid; its presence does not activate those skills. Later scripted installation can repair links and remove it.

**Map of their work.** If Stage 2 identifies research files outside the vault, let the user identify the folder. Inspect only authorized immediate entries, and report any selected location that cannot be reached. Show candidate Projects, Areas, or Resources in the task's requested form or under the recipient's existing reporting policy. Explain that their existing files stay where they are. Let the user accept, drop, or relabel entries. For each accepted Project or Area, identify its exact local `files/` path, documented external workspace, or established working location, along with the exact owner MOC or `AGENTS.md` that documents any external binding. Use the selected owner and verified applicable policy when choices are open. An unresolved or unavailable location remains explicit in the plan.

**PhD and career support.** When relevant to the interview answers, offer configuration now or later through phd-career-builder. Reuse the supplied role, goals and accepted Area MOC. If selected now, read that builder and ask only useful unanswered groups within this conversation, including links to applicable program/cohort sources and the requested support areas. Keep proposed settings and the exact existing/accepted MOC destination in the second read-back below; that approval also covers those settings. Do not add another interview, profile, setup gate or active reminder job. Unanswered details stay unknown and can be filled later without blocking core setup.

**Native discovery, optional.** Default to skipping mounts. Include the choice in the existing second read-back, without adding a compulsory question: skip, or the native discovery the user has requested. A requested mount is a separate action after core completion, not a setup dependency. Merely using an app or having skills on disk does not request mounting.

**Read-back two:** confirm the structure choices against the defaults, toolkit plan, accepted PARA list, and native discovery after completion if requested. Show each accepted Project and Area, its exact selected MOC, and its planned local `files/` path, established working location, or exact external workspace path. Include the owner MOC or `AGENTS.md` that already documents that external binding or will receive the proposed authorized entry. Include any role-property edit to an existing note in the same approval. Report unavailable external locations separately and explain when a selected nested or external MOC is outside generated direct-folder discovery. Wait for one yes.

Include only any PhD settings actually selected above in this same read-back, with unanswered fields left unknown.

## Stage 4: the build

One run, no questions. Report which build steps have completed using the current task's requested form or the recipient's existing reporting policy. Use the following scripted steps only with verified Python 3 and PyYAML. If scripted execution is unavailable, compare the recovered Stage 3 approval with the manual plan before any manual write. Build and check the core before finishing it in Stage 5. Do not mount skills in this stage.

1. **Names.** If root names changed or optional roots were dropped: `python3 "00 ASTORIA/skills/skills-janitor/scripts/rename_roots.py" <flags> --apply`, then `lint.py`. Flags: `--no-emoji`, `--no-numbers`, `--set role=name`, `--drop role`.
2. **Folders.** `python3 "00 ASTORIA/skills/setup-my-vault/scripts/create_layout.py" --apply` creates the roots and the layout subfolders from the vocabulary, skipping dropped roots.
3. **Toolkit.** Run `python3 "00 ASTORIA/skills/skills-janitor/scripts/install_specialized.py" --groups <groups> --apply --remove-catalog`, or use `--none --apply --remove-catalog` for the confirmed core-only choice. The group path moves the chosen folders into `00 ASTORIA/skills/`; `--none` installs no optional skills. Both paths repair portable links, rebuild the Skill Map and coordinator catalogs, lint, and remove the optional catalog only after successful checks. If an earlier apply was interrupted, recover the exact toolkit plan and its Stage 3 approval before resuming with the same installer command and options. Use the installer's supported recovery for the recorded run. Stop and report an unverified or unsafe recovery state while preserving installed folders, remaining shelf contents, and other existing work. A partial scripted install stays pending until it can resume safely.
4. **Projects and areas.** Follow the approved plan for each accepted project. Reuse a verified existing MOC when selected. If the plan leaves the hub open, reuse the verified existing MOC identified by the applicable project policy. If the approved plan calls for a new MOC, use its selected path and template. Where the plan leaves those open, follow the verified applicable project or recipient policy. With no selected convention, create `<projects root>/<project>/MOC <project>.md` from `00 ASTORIA/templates/Research Project Template.md` for research or `Projects Template.md` for other work. Fill only the supplied title, one-line description and `workspace:` path. On the approved owning project MOC, use the top-level frontmatter property `astoria_role: project_moc`. Keep this property from the selected template when creating the MOC. For an existing note, add the property only when that exact edit was approved. Preserve its body and other properties, and leave an identical property in place. If a property conflicts or another direct note has the same role, report the conflict and preserve both notes. Leave nested or external selected notes at their approved paths and report the discovery limit. For newly created project MOCs, apply the confirmed Stage 2 heading style using the selected template's mapping. For a research MOC, also apply the confirmed Stage 2 callout preference. For a new nonresearch MOC, follow the approved navigation and link form, then the verified applicable project or recipient convention where that choice is open. Use the illustrated three-callout opening only when the resolved form calls for it or navigation remains open. If the resolved plain Markdown form omits callouts, keep the supplied brief in ordinary Markdown and include only its applicable navigation. Verify each retained navigation label and fragment against its actual heading. If a project bridge names AI Notes, verify and use the exact rendered heading. Keep the Stage 3 folder choices and project paths. For each accepted Area, reuse the verified existing owning MOC named in the approved plan. If the plan leaves the existing owner open, use the applicable verified Area convention. When the plan authorizes creating a note, use its selected path and template, then the applicable verified convention if those choices remain open. Use `<areas root>/<Area>/<Area> MOC.md` and `Base Template.md` as fallbacks when no other convention was chosen. On an approved new Area MOC, use the top-level frontmatter property `astoria_role: area_moc`. For an existing note, add that property only when the exact edit was approved. If the approved scope leaves a custom-named direct note unmarked, keep it and report that layout discovery needs the role. Preserve its content and other properties and leave an identical property in place. If there are competing markers or a conflicting property, report the gap and preserve the notes. Keep an approved nested or external note at its selected path and report that it falls outside generated direct-folder discovery. For a new MOC, add the supplied title and one-line purpose and apply the approved template. Include an empty AI Notes section when the selected template or applicable continuity policy calls for one. Use `# AI Notes` for plain headings and `# 🤖 AI Notes` for the illustrated emoji style, or follow the confirmed heading preference. When an existing MOC section is the selected continuity location, verify its actual heading without rewriting the note. For each accepted Project or Area, use Bridge Maker for its one `AGENTS.md` pointing to root `me.md` and the verified MOC. For a selected external workspace, reuse its exact existing binding in the owner MOC or `AGENTS.md`. If the plan approves an owner entry, document the exact selected path in that file, using `workspace:` when the MOC's format supports it. Preserve unrelated instructions and conflicting bindings pending resolution. Record path availability separately from the approved binding. If the location cannot be reached, preserve the path, report it as unavailable, and leave the existing files in place. Create or reuse the single approved local `files/` folder only when the plan chooses that local arrangement. Preserve any established working location chosen in the plan. Keep reusable references in Resources. Add a verified MOC link only when its edit is within the approved scope. Preserve external source files and established scientific layouts. Read each template before instantiating it.
5. **Me file, second pass.** Pass the confirmed Stage 3 changes to me-builder for a bounded refresh under the existing second read-back. Update only approved entries in `## Current Projects and Areas`, the approved external folder path in `## Working Locations`, and any confirmed choices for ordinary note names or filename dates in the existing File naming rule under `## Rules`. Preserve existing preferences for choices the user left open, technical record formats and all other entries.
   If PhD settings were approved in read-back two, call phd-career-builder after the accepted MOC exists, passing those exact settings, source links, owner and approval. Save only that approved scope in its existing sections, without another confirmation. Otherwise leave configuration for later.
6. **Layout.** Call [vault-builder](../vault-builder/SKILL.md): it runs `build_layout.py`, fills the purpose lines the report asks for from the accepted projects and areas, and writes `00 ASTORIA/agent_notes/layout.md`. Then write `00 ASTORIA/agent_notes/ai_log.md` from `00 ASTORIA/templates/ai_log_template.md` with one first entry naming what setup did.
7. **Check.** Call [vault-janitor](../vault-janitor/SKILL.md) with fixes authorized for anything the build produced; call [skills-janitor](../skills-janitor/SKILL.md) (`lint.py` and `build_views.py --check`).

If a step fails, stop, report the step and the error, and leave the files as they are; the state table tells the next session where to resume.

### Manual build

Use the verified existing or confirmed newly created briefing and the exact Stage 3 plan and approval. Before any manual write, pass the toolkit state check in `./references/manual_setup.md` and compare the approved root names, optional roots, toolkit and catalog disposition, accepted paths and required checks against the supported manual build. Continue without another read-back when the manual build can carry out that plan. If it cannot, leave the affected work pending. Resume the original plan when its verified runtime is available, or return to Stage 3 for explicit approval of the affected changes to a compatible plan in the existing second read-back. Preserve other confirmed choices, paths and verified work. Perform only the file actions the approved manual plan supports. Preserve shipped generated views. For accepted projects and Areas, follow scripted steps 4 and 5 to reuse or create the approved owning MOCs and make the authorized property and root-me bridge edits. Apply the same approved working location and owner-documentation rules as scripted step 4. Reuse the documented binding or write the exact approved path in the owner MOC or `AGENTS.md` when authorized. Preserve and report unavailable external locations. Create or reuse the approved local working folder only when the plan chose it. Use the same resolved heading style and navigation form for any new nonresearch MOC. Verify retained navigation links and any AI Notes heading named by a project bridge. Leave external source files in place. Use vault-builder's manual first-setup exception for the layout. Report which checks were manual; do not claim generators or lint ran. Then continue to Stage 5. Native mounts are not needed.

Apply any PhD settings already approved in the same read-back through phd-career-builder after their accepted MOC exists, just as in the scripted build. If there is no chosen owner, leave the configuration unsaved and pending. Report the pending item in the current task's requested response form or under the recipient's existing reporting policy. Complete the core setup without creating a profile for it.

## Stage 5: finish the usable vault

With the scripted build, run `python3 "00 ASTORIA/skills/setup-my-vault/scripts/finish_setup.py" --apply`. It checks that `me.md`, the layout reference, AI log, Skill Map, loader template, and required roots exist and the optional catalog is gone, writes root `AGENTS.md` from `00 ASTORIA/templates/agents_loader_template.md`, and retains `README.md` as the participant guide.

In manual mode, verify the manual file/link checks above, retaining the uninstalled optional catalog, copy the loader template over the draft root `AGENTS.md`, and keep `README.md`. Preserve a customized instruction file for review rather than overwriting it blindly. Preserve all other files. Report manual file/link checks and the automated checks that were not run.

The vault is now usable and setup is complete without mounts. Completed setup is the full loader plus verified core files and folders; README presence is not a setup-state signal. Do not check for native discovery as a completion condition.

In the chosen tone: what exists now (the three core files, any project MOCs, the core or selected toolkit, and verified references to outside work); three phrases to try that match their goals ("help me scout the field on <topic>", "start a research session on <project>", "summarize this paper"); where to change their mind later ("update my me file", "rename my folders", "refresh the vault map"); and that optional skills and native mounts can be added later. A specialized or add-on skill is installed as its whole folder in `00 ASTORIA/skills/`, with dependencies and generated views checked through skills-janitor when the required runtime is available. In manual mode, state the unrun automated checks without calling the core setup incomplete. Continue to a requested optional mount without asking another setup question; otherwise close directly.

## Stage 6: optional native discovery after completion

Skip this stage unless the user requested mounting, including through the existing second read-back. Load [skill-mount](../skill-mount/SKILL.md) only for that optional handoff. Use its dry run and requested scope; a core set is sufficient for the companions and part coordinators. Registry-platform registration follows that skill's adapter from a session with the required capabilities; do not treat it as a core setup action.

If mounting is declined, unavailable, or fails, report that optional status and keep the completed loader and vault intact. Do not rerun setup, alter its README, require software installation, or delay use of the vault. The direct `AGENTS.md` route remains available.

After the optional action, or immediately after Stage 5 when it is skipped, give the closing line in the chosen tone and the one handoff question: what do you want to work on first? Read `me.md` and route the answer through its Skills table.
