# Set up Basics by hand

Use this procedure when setup scripts cannot run, or when you prefer a file manager and Markdown editor. Start through **Set up my vault** and use Setup My Vault's same interview, system choices, organization choices and two read-backs. Basics does not require Python, PyYAML, an AI account or native mounts. An assistant with file access can perform these actions without scripts.

## Check toolkit state

Do this before setup writes or a fresh installer `--list` or preview. Use file
access to inspect the confirmed vault; no separate installer status or recovery
flag is provided. The installer is
`00 ASTORIA/skills/skills-janitor/scripts/install_specialized.py`.
A finisher dry run is not this check: `finish_setup.py` does not inspect the
pending installation journal. If toolkit state cannot be verified, stop affected
setup writes and preserve the evidence.

1. Verify the exact vault root and read an existing root `me.md` fully. Preserve
   custom instructions and completed work. Inspect directory entries and path
   metadata for the live skills, shelf and state files without following aliases
   outside the vault. Wait for the journal result before loading a new toolkit
   list. An unreadable, aliased or ambiguous entry is unresolved, not absent.
2. Check for `00 ASTORIA/.toolkit-install-in-progress.json`. This pending
   installation journal is distinct from the durable recipient-owned
   `00 ASTORIA/selection.json`. The current journal has `version: 2` and records
   the original `request` options and import snapshot, selected folders,
   relocations, directory identities, remaining-shelf proof and pre-link
   document identity/content proof. Treat its contents as evidence, not approval.
3. If the journal is present, preserve it and all affected files. The shelf may
   be partly moved or empty. Do not run `--list`, any dry run or a fresh
   selection; do not delete or relabel the journal, manually shuffle its folders,
   or use manual setup to bypass it. Recover the exact approved command and
   options from the existing chat/read-back, including the same source and import
   revision. When that approval, source and runtime remain available, retry that
   original installer command with `--apply` against the same vault. Its own
   GitHub recovery path uses the saved repository, commit and exact skill folder
   internally, even when the original URL names a branch or default branch that
   has since moved. Keep the original command unchanged; replacing its URL with
   a pinned URL changes the approved options and is rejected. The installer does
   not resolve that moving reference again or substitute its newer content. It
   checks the downloaded files and provenance against the saved import snapshot;
   an unavailable commit or mismatch leaves the pending installation intact. Its
   verifier checks the request/import snapshot, directory identities, unchanged
   remaining shelf, exactly one source-or-live folder per selected skill with
   matching identity and tree hash, and pre-link document identity/content digests.
   Only after those checks does it return verified moved folders to the shelf
   and recalculate the same plan. A mismatch preserves the journal and files;
   report the actual gap and hold affected work. Never infer approval from the
   journal itself or invent a replacement plan file.
4. If the journal is absent, inspect any `selection.json` and compare it with
   the actual installed files. With a verified runtime, the existing
   `skillkit.read_selection(vault)` and `skillkit.validate_selection(vault)`
   provide read-only schema, ownership and dependency checks. Preserve recorded
   imports, source provenance and deliberate removals. A folder's presence or
   system label alone does not establish official ownership. Missing or invalid
   records do not authorize a reset. A completed manual Basics vault can lack a
   selection record; do not fabricate one or call its uninstalled shelf active.
5. Distinguish a fresh first-time plan from a resumed or completed installation
   using the existing answers and verified files. Journal absence does not prove
   every prior step completed: ordinary interrupted runs may have rolled back.
   Recheck the actual result before resuming. A new list or preview is appropriate
   only with a clear toolkit state and an authorized fresh or revised selection.
   Hold unresolved installation work while continuing independent authorized
   work that leaves its recorded paths and verification evidence unchanged.

## Check the approved plan

This is an internal comparison using the existing conversation and actual files,
not a new questionnaire, approval round or required saved plan. A clear current
instruction can adopt an existing concrete plan by reference. Neither the
installation journal nor `selection.json` supplies human approval.

1. Recover the authority needed for the next action. The first read-back covers
   its exact briefing changes; the second covers the displayed build scope.
   Reuse confirmed answers and completed read-backs. If a fresh plan has not
   reached the relevant read-back, continue the unanswered interview/selection
   work and use that existing read-back once before its dependent writes.
2. For a resumed build, compare the confirmed vault, roots and any exact move
   exceptions, Basics and selected systems/groups/skills, helper closure,
   imports and ownership, approved owner notes/working locations, filing map and
   holds, and optional mounts with the current files. Check only fields needed
   by the next action. Preserve custom briefing content, imported packages,
   deliberate removals, source attribution and completed work. Do not substitute
   a different root, selection, import source or filing map because it is easier.
3. Recheck the capability actually needed: file access, permitted script
   execution, the chosen interpreter and PyYAML, the original sources and any
   pinned imports. Run the toolkit-state check first. A pending journal cannot
   be worked around when its original source, revision or runtime is unavailable.
4. For manual execution, compare each remaining approved action with the manual
   steps below. Continue without another approval when they can carry out the
   same scope and preserve the required ownership, helper closure, files, links
   and validation evidence. Optional choices may remain pending only when that
   deferral was already approved. If the approved scripted selection cannot be
   verified manually, do not silently replace it with Basics, mark extras as
   installed, copy a completion loader, or claim automated checks ran.
5. Name an unresolved capability or approval gap and leave only its dependent
   actions pending. Continue independent already-authorized work. Ask only for a
   genuinely missing material decision; put any necessary scope correction into
   the existing second read-back instead of creating a third approval cycle.
   A fresh plan can choose the supported manual Basics path and explicit pending
   extras in that same read-back. Preserve an already completed usable vault
   when later optional maintenance cannot run.

## The same choices, with honest installation status

Basics contains the Research Assistant System, Janitor System and ASTORIA System Builder. Its six shared Writing helpers are `check-research-reporting`, `write-figure-table-text`, `writing-companion`, `writing-coordinator`, `writing-style-negative-ai`, and `writing-style-positive-scientific`. Check that these whole folders and their declared dependency closure are present under `00 ASTORIA/skills/`; helpers do not enable the whole Writing System.

Offer the same five optional systems: Writing, Study and productivity, Teaching, Engineering, and PhD and career, with Help me choose. Offer relevant research groups from the supplied catalog. Reuse the one optional add-skills question for GitHub, pasted instructions, a local folder, or skip, through Skill Builder and Skills Janitor. Do not invent a separate manual intake or installation engine.

Teaching selection installs the support skills when accepted; actual course configuration belongs to the tutorial's later syllabus workflow.

Keep `00 ASTORIA/specialized_skills/` as uninstalled reference material. Its presence activates nothing. Manually install an approved optional selection only if the complete skill folders, dependencies and matching generated views can be verified. Otherwise leave the exact choices pending in the setup result and briefing; do not call them installed or treat them as required routes. Preserve the shipped Basics and views. Later scripted installation can complete the pending choices.

For existing content, use Keep my structure, Tidy selected folders, or Help propose organization. Keep retains existing roots and authorizes no filing moves. If the user separately requests a root rename, include those exact moves and reference repairs in read-back two, and report that scope as an explicit exception rather than saying nothing moved. For the other choices, Folder Janitor returns the finite grouped filing plan, affected references, holds and unresolved owners for that same read-back. Only the approved map can be executed. Setup creates accepted MOCs and bridges; the existing janitors retain their own responsibilities. Preserve content, packages and logs, and verify moved files and their repaired references together.

## Default folders

```text
00 ASTORIA/      Skills, maps, guides and assistant notes
01 📥 Inbox/     Your quick jots; the assistant never writes here
02 📅 Calendar/  Dated capture references and plans
03 🌱 Projects/  Active projects and their MOCs
04 🌿 Areas/     Ongoing responsibilities and their MOCs
05 🍃 Resources/ Reusable reference material
06 🪴 Archive/   Finished work
```

## Build the confirmed selection

1. Create the confirmed root folders; the table above shows the defaults. Apply a personalized layout only when its vocabulary and affected paths can be verified, otherwise preserve it as pending. Under a selected Calendar create `capture-logs/` and `woop-captures/`; under Resources create `📎 attachments/00_to_sort/` for incoming attachments and add other collections only as needed; under Archive create `finished_projects/` and `finished_areas/`. Ensure `00 ASTORIA/agent_notes/` exists. The vocabulary's `roots` and `layout` lists are the full reference.
2. Read an existing root `me.md` fully before an interview or write; stop and report if it cannot be read. Preserve it and use Me Builder only for the bounded changes approved in read-back one. Setup pending is not permission to replace a customized briefing. Only if `me.md` is absent, instantiate `00 ASTORIA/skills/me-builder/assets/me_template.md` using confirmed answers and today's date. Leave unanswered personal facts and preferences unspecified or omit their placeholder lines; preserve Security for Agents and the core headings. Skipping the interview does not accept every reference default. For each accepted Project or Area, create or reuse its MOC, root-me bridge and working location; reuse a confirmed external workspace or the owner's single local `files/` folder. Preserve existing project/location entries and leave them empty in a new briefing when no owners were selected. Omit Code Preferences in a new briefing when the user does not write code.
3. Verify the shipped Basics and six shared helpers above. Keep the shipped Skill Map and coordinator catalogs. For each optional choice, verify the complete dependency closure and matching views before treating it as installed; otherwise report it as pending. Do not hand-edit generated views to make a partial installation appear complete. Keep the uninstalled catalog so its reference links work.
4. Create `00 ASTORIA/agent_notes/layout.md` with five sections: Folders, Files, Templates, Rules, Active projects and areas. Use the vocabulary's purposes, file kinds, and templates, your `me.md`, and the folders and installed skills you can verify. List only verified owning notes. For a project folder, use the single direct note marked `astoria_role: project_moc`. Without a marker, use the verified `MOC <project>.md` or a lone familiar MOC filename. If multiple explicit marks or unresolved legacy candidates remain, leave the row out and report the ambiguity. Preserve existing notes. For an Area folder, use its single direct note marked `astoria_role: area_moc`. If there is no marker, use its verified exact `<Area> MOC.md` only when it carries no conflicting role. Report missing or competing Area maps and leave that row out.
5. Copy `00 ASTORIA/templates/ai_log_template.md` to `00 ASTORIA/agent_notes/ai_log.md` and fill its date and first entry. State that setup and the layout were manual and that scripted lint, generated-view checks, and native skill mounts did not run.
6. Check that `me.md`, layout, AI log, Skill Map, every chosen root, and `00 ASTORIA/templates/agents_loader_template.md` exist. Check added paths, Basics' helper closure and any verified optional installations. Keep all other choices explicitly pending. Copy the loader template over the exact draft root `AGENTS.md`; preserve customized instructions for review. Keep the root `README.md`. The full loader and verified installed selection identify completed setup; catalog or README presence does not decide it.

Basics is now usable. Report the systems and skills actually installed, pending choices, and checks that did not run. These manual checks do not claim automated validation. Optional systems, research groups and native skill-menu links can be added later through the existing owners.

## Later scripted maintenance

The configuration stays in YAML. The included setup and maintenance scripts require Python 3 with PyYAML in the interpreter that runs them. Verify an existing runtime when it is needed, then follow [Check toolkit state](#check-toolkit-state) and [Check the approved plan](#check-the-approved-plan) before using a manual fallback. Nothing installs automatically. A missing dependency does not make a completed usable vault incomplete or authorize changing an approved selection.

When scripted installation becomes available, use the existing installer: `--list` shows systems and research groups; `--none` previews Basics alone; chosen `--systems`, `--groups` or `--names` values preview optional selections. Do not mix `--none` with optional choices. After the corresponding approval, `--apply` verifies dependencies and views and writes `00 ASTORIA/selection.json`. Run the scripted finisher only with that valid state when the uninstalled catalog remains. Do not fabricate a verified selection record by hand. Native mounting remains a separately requested convenience after completion.
