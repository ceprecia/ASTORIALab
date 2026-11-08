# Set up the core by hand

This procedure describes the default-folder, core-only plan for a file manager and Markdown editor. The core vault does not require Python, PyYAML, an AI account or native skill mounting. An assistant with file access can perform these file actions without scripts. Check toolkit state and the setup plan before writing.

## Check toolkit state

Before creating or changing any setup file, check for
`00 ASTORIA/.toolkit-install-in-progress.json`. Compare the exact names of the
immediate entries in `00 ASTORIA/skills/` with the optional names in
`starter.catalog_index` in
`00 ASTORIA/skills/skill-builder/assets/vocabulary.md`. An uninstalled
reference shelf is expected for manual core setup. If either check cannot be
completed, report the gap and stop before writing files.

If the install record is present or an indexed optional name is already live,
pause setup. Preserve the record, installed skills, remaining shelf contents
and existing work. Recover the exact prior installer plan and its approval
from the available setup conversation or an authorized setup record. Continue
only through the installer's supported recovery with the same approved apply
command and options and a verified runtime. Fresh listing and preview are for
a new plan after recovery. If the plan, approval, runtime or safe recovery state
cannot be verified, report what is pending and stop before any manual-core write.

## Check the setup plan

For a fresh standalone build, choose this documented manual-core plan before
writing. If guided setup has started, recover the exact Stage 3 choices and
approval. Compare the required roots and omissions, toolkit and catalog
disposition, accepted paths and required checks with what this procedure can
perform. Reuse compatible approval and preserve confirmed paths. If approval
cannot be recovered or any requirement cannot be met, stop before manual
writes. Resume with a verified runtime for the original plan, or explicitly
approve the affected changes to a compatible plan through the existing Stage 3
read-back. Preserve other confirmed choices and verified work. Keep setup
pending until the applicable approved checks pass.

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

## Build the core

1. Check the exact vault-root `me.md` path first. Open and read an existing briefing completely. Keep it once you verify it is your authoritative briefing for this vault. If the path is occupied and the briefing is unreadable or you cannot verify its identity, stop and resolve that gap before continuing. Preserve the existing entry. If the path is vacant, copy `00 ASTORIA/skills/me-builder/assets/me_template.md` to root `me.md` and fill its placeholders with your preferences, interests, actual folder paths, and today's date. Use applicable defaults, remove unanswered optional placeholder lines, and keep the standing rules and Security for Agents section. Follow Me Builder's template procedure for the new root note. Resolve real links from the template's original location and rebase them to root `me.md`. In Markdown, use `00%20ASTORIA/systems/ASTORIA%20System%20Builder.md` as the root note's System Builder link target. Verify the rendered target resolves inside this vault and leave the reusable template intact. For a newly created briefing, leave Current Projects and Areas empty when you have not selected any and remove Code Preferences if you do not write code.
2. Create the root folders listed above. Under Calendar create `capture-logs/` and `woop-captures/`; under Resources create `📎 attachments/00_to_sort/` for incoming attachments and add other collections only as your content needs them; under Archive create `finished_projects/` and `finished_areas/`. Ensure `00 ASTORIA/agent_notes/` exists. The `roots` and `layout` lists in `00 ASTORIA/skills/skill-builder/assets/vocabulary.md` are the full reference.
   For each selected Project or Area, confirm the one owner MOC, the root-me `AGENTS.md`, and the exact local `files/` path, established working location, or external workspace. Reuse or create only the approved owner entries. Reuse the exact external binding or record it in the authorized owner MOC or `AGENTS.md`. Preserve and report unavailable paths separately and keep existing files in place. Set up a local working folder only when chosen.
3. Keep all folders under `00 ASTORIA/skills/` and keep the shipped Skill Map and coordinator catalogs unchanged. Retain `00 ASTORIA/specialized_skills/` as uninstalled reference material so shipped links work; it activates no extras.
4. Create `00 ASTORIA/agent_notes/layout.md` with five sections: Folders, Files, Templates, Rules, Active projects and areas. Use the vocabulary's purposes, file kinds, and templates, your `me.md`, and the folders and installed skills you can verify. List only verified owning notes. For a project folder, use the single direct note marked `astoria_role: project_moc`. Without a marker, use the verified `MOC <project>.md` or a lone familiar MOC filename. If multiple explicit marks or unresolved legacy candidates remain, leave the row out and report the ambiguity. Preserve existing notes. For an Area folder, use its single direct note marked `astoria_role: area_moc`. If there is no marker, use its verified exact `<Area> MOC.md` only when it carries no conflicting role. Report missing or competing Area maps and leave that row out.
5. Copy `00 ASTORIA/templates/ai_log_template.md` to `00 ASTORIA/agent_notes/ai_log.md` and fill its date and first entry. State that setup and the layout were manual and that scripted lint, generated-view checks, and native skill mounts did not run.
6. Verify the root `me.md` briefing and check that layout, AI log, Skill Map, every default root, and `00 ASTORIA/templates/agents_loader_template.md` exist; check the paths and links you added and confirm optional skills remain uninstalled. Copy the loader template over the draft root `AGENTS.md`. Preserve a customized instruction file for review rather than overwriting it blindly. Keep the root `README.md`; no guide needs deletion. The full loader and verified core files identify completed setup, regardless of README presence.

You now have the usable core vault. These manual checks do not claim automated validation. Return to root `README.md` whenever you want an introduction. Optional toolkits, scripted maintenance and native skill-menu links can be added later.

## Later scripted maintenance

The configuration stays in YAML. The included setup and maintenance scripts require Python 3 with PyYAML in the interpreter that runs them. The assistant verifies an existing runtime when it needs those helpers. Use this manual path for setup only after the toolkit and approved-plan checks above pass. Nothing installs automatically. A missing script dependency does not make the completed core vault unusable.

When you choose scripted toolkit installation later, the existing installer checks dependencies, updates views and repairs links before optionally removing the uninstalled catalog. Native mounting remains a separate convenience, requested only after core setup is finished. Using an assistant does not itself request mounting.
