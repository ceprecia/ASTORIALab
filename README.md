# ASTORIA

![ASTORIA Lab](00%20ASTORIA/assets/astoria_banner.png)

**Adaptable Scientific Toolkit for Organized Research with Interchangeable Agents.**

Make your research workspace feel like yours. Shape the toolkit around your work, keep your research connected, and bring along the AI assistant you prefer.

## Why an Adaptable Scientific Toolkit?

AI assistants and tools change, but your core workflows should stay with you. ASTORIA lets you replace these outer layers while keeping your context and working methods.

![Five layers: your researcher core, vault and evidence, portable workflows, replaceable AI tools, and optional extensions](00%20ASTORIA/assets/astoria_architecture.png)

At the center, `me.md` introduces your interests and working rules. The second layer holds notes and sources. The third holds portable skills and maps that connect the work. AI assistants and optional extensions form the replaceable outer layers. Your judgment stays at the center.

## Why Organized Research?

ASTORIA gives you and your assistants a shared structure for finding context and doing useful work.

**Companions** guide ongoing work. **Coordinators** assign focused **skills**, which give steps for a job. Results return to the Companion for synthesis. The [Skill Map](00%20ASTORIA/Skill%20Map.md) lists this starter vault's skills. You can adapt them to your methods and add workflows as your work develops. See [Customize as you need!](#customize-as-you-need) for the builders and maintenance tools that help.

![A Companion works through a Coordinator with focused skills; results return to the Companion](00%20ASTORIA/assets/agent_team.png)

ASTORIA uses a [multi-agent system](https://developers.openai.com/api/docs/guides/responses-multi-agent): agents tackle focused assignments with the context they need, then bring their results back together. Simple tasks can stay in one chat.

**Projects** have a defined outcome or finish point. **Areas** are responsibilities you maintain over time. **Resources** hold reusable references by topic, and **Archive** holds inactive material. [PARA in ASTORIA](00%20ASTORIA/systems/ASTORIA%20System%20Builder.md#para-in-the-vault)

Each Project or Area has one **MOC**, or map of content, for context, progress and links, and one **AGENTS.md** for assistant instructions. Keep local working material in a single `files/` folder or document the external workspace where it lives. The map gives you one place to find the work and helps address [project fragmentation](https://doi.org/10.1145/1124772.1124813).

![Projects, Areas, Resources and Archive arranged in a four-part ring](00%20ASTORIA/assets/para_project.png)

## Why Interchangeable Agents?

After setup, ask a different assistant to read your me.md for vault-wide context, or your project's AGENTS.md to continue that project. Your preferences, workflows and saved progress stay in the same files.

![Different assistants can occupy the replaceable outer layers while the researcher core stays in place](00%20ASTORIA/assets/interchangeable_agents.png)

## Get started

1. **Download:** [Download the ASTORIA starter vault ZIP](https://github.com/ceprecia/ASTORIALab/releases/download/v1.0.0/ASTORIA-starter-vault-v0.1.0.zip), then extract it.

2. **Open** the extracted folder in Obsidian using **Open folder as vault**, or use your file manager and a Markdown editor.

> [!Tip]
> **Using an existing Obsidian vault?** Copy the extracted `00 ASTORIA/` folder and `AGENTS.md` directly into your existing vault's root, the top-level folder you open in Obsidian. If either already exists there, keep your current files and review how to combine the setups before proceeding.

3. Give your AI assistant access to the vault you plan to use.

> [!Tip]
> Creating a project in your AI assistant can help it keep access to your vault.

4. Copy this request into your AI assistant:

> Read this vault’s root AGENTS.md and follow Setup My Vault in the ASTORIA System Builder. Guide me through the steps in order.

Setup My Vault starts with a series of setup questions and the default layout. Tell your assistant what you work on, which tools you use, and how you like to work. Review its summary, choose your folders and any optional research toolkit, then confirm the build plan. 

None of this information is sent back to the github project. Your preferences are kept locally in your vault. Note that some AI Agent models may share data to parent companies to train their models. For a full private experience consider a local LLM.

**What you'll have**

- Your `me.md` briefing and an `AGENTS.md` that tells assistants where to start.
- An organized vault, a Skill Map, and map notes for projects or areas you choose.
- Core Research, PhD and Career, Study, Teaching, Engineering, and Writing workflows.

If relevant, the assistant offers PhD and career setup now or later. Choose **now** to answer questions about your program, milestones, or goals and save approved settings in your chosen map note.

Optional mounts come after setup. [Manual setup guide](00%20ASTORIA/skills/setup-my-vault/references/manual_setup.md)

## Try a workflow

**After setup**, start with a Companion for ongoing work. Direct utility skills and passive writing profiles support other tasks. The nine groups below give you places to begin.

![Nine toolkit groups arranged around the portable workflow layer, using their system icons](00%20ASTORIA/assets/system_toolkit.png)

| Group | Try asking |
| --- | --- |
| [Research](00%20ASTORIA/systems/Research%20Assistant%20System.md) | “Research Companion, help me compare these research directions.” |
| [PhD and Career](00%20ASTORIA/systems/PhD%20and%20Career%20System.md) | “PhD Companion, help me prepare for an advisor conversation.” |
| [Study and Productivity](00%20ASTORIA/systems/Productivity%20and%20Study%20System.md) | “Study Companion, teach this topic from my notes, then help me practice.” |
| [Teaching](00%20ASTORIA/systems/Teaching%20Assistant%20System.md) | “Teaching Companion, help me prepare a class from these course sources.” |
| [Engineering](00%20ASTORIA/systems/Engineering%20System.md) | “Engineering Companion, help me plan this device build.” |
| [System Builder](00%20ASTORIA/systems/ASTORIA%20System%20Builder.md) | “Update my working preferences in me.md.” |
| [Janitor](00%20ASTORIA/systems/Janitor%20System.md) | “Folder Janitor, organize these files using my structure and repair their links.” |
| [Capture and Writing](00%20ASTORIA/Skill%20Map.md) | “Capture Progress, save these decisions and next steps in my project MOC.” |
| [Writing Profiles](00%20ASTORIA/Skill%20Map.md) | “Writing Companion, revise this scientific paragraph using my writing preferences.” |

Research and PhD/Career have separate Companions and internal Coordinators.

For writing projects, start with **Writing Companion**. **Research Output Coordinator** helps you finish, share and publish research: publication packages, reproducibility, data/code releases, engagement, handover and funding requirements. It borrows the shared writing team when needed.

**More Research prompts:**

- “Summarize this paper’s evidence and limitations.”
- “Compare these papers’ findings and disagreements.”
- “Challenge this research question and its assumptions.”
- “Help me compare designs for testing this hypothesis.”
- “Review this analysis plan against my question and data.”
- “Draft methods from these verified procedures.”

## Customize as you need!

This is your starting point. Build around the projects, habits and tools you already use.

**Make the instructions yours.** Tell your assistant when your goals, preferences or working rules change. [Me Builder](00%20ASTORIA/skills/me-builder/SKILL.md) updates your `me.md` briefing. [Bridge Maker](00%20ASTORIA/skills/bridge-maker/SKILL.md) connects a project's `AGENTS.md` to that briefing and adds the project's own instructions. Projects stored outside the vault can use the same connection.

**Build skills from your work.**  Ask [Skill Builder](00%20ASTORIA/skills/skill-builder/SKILL.md) to turn a repeatable procedure into a skill, or adapt an existing one. For example, “Make a skill for reviewing a paper using my lab's checklist.” It checks for overlap and refreshes the Skill Map and coordinator catalogs so assistants can find the new workflow. Builders also help configure specific systems, such as PhD and career support or teaching, when you need them.

**Connect your notes and results.** Use Obsidian to read, edit and link the same Markdown files your assistant works with. Give each project a MOC linking its notes, papers and outputs, then ask your assistant to save useful work in the appropriate note and link it back. Existing scientific files can keep their established layout. Obsidian's [links and backlinks](https://obsidian.md/help/links) help you follow these connections, while the bundled templates give new notes a consistent starting point.

**Keep it organized as it grows.** The [Janitor System](00%20ASTORIA/systems/Janitor%20System.md) has three maintenance skills. **Vault Janitor** checks layout, instructions and links. **Folder Janitor** organizes selected folders using your chosen structure and repairs affected links and paths while preserving MOC prose. **Skills Janitor** checks skill consistency and refreshes the generated maps and catalogs. Try “Check my vault for stale instructions and broken links” or “Organize these attachments using my folder rules.” After folder or template changes, [Vault Builder](00%20ASTORIA/skills/vault-builder/SKILL.md) refreshes the assistant's layout reference. Ask for these checks when needed; they run as requested tasks.

## License and sources

Keep [LICENSE, including source-specific notices](LICENSE), and capability-specific sources with the files. MIT covers ASTORIA's original material; adaptations retain their source terms. External tools and datasets retain their terms. Assistant names belong to their respective owners. The [layer diagram](00%20ASTORIA/assets/astoria_architecture.svg) and slim banners include editable SVGs; system icons were generated with an image-generation tool.
