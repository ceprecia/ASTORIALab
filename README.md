# ASTORIA

![ASTORIA Lab](00%20ASTORIA/assets/astoria_banner.png)

**Adaptable Scientific Toolkit for Organized Research with Interchangeable Agents.**

**ASTORIA version:** 1.3.1

An Obsidian toolkit to make your research workspace feel like yours. Shape the toolkit around your work, keep your research connected, and bring along the AI assistant you prefer!

[Tutorial](tutorial.md)

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

**First-time setup**

1. Download **ASTORIA-starter-vault-v1.3.1.zip** from [ASTORIA Releases](https://github.com/ceprecia/ASTORIALab/releases/tag/v1.3.1) and extract it.
2. Open that folder in your assistant and grant access. Show your existing Obsidian vault too, if using one.
3. Say **Set up my vault**. Choose first-time setup and follow the questions and plan. Use Obsidian's **Open folder as vault** to open your chosen folder, or use a Markdown editor.

The starter contains `AGENTS.md` and `00 ASTORIA/`; **Code → Download ZIP** contains the repository.

**Update an existing ASTORIA vault**

1. Download and extract the new starter ZIP.
2. Open your working vault in the assistant and show it the new ZIP or extracted folder.
3. Say **Set up my vault** and choose update. The assistant applies the update, then audits your vault. Review proposed repairs before they are applied.

**Start with the basics** selects Research Assistant, Janitor and ASTORIA System Builder with required shared helpers. **Help me choose** offers other systems and skill groups. Offer a GitHub skill link, workflow instructions or a local skill folder, or skip additions. App mounting is optional.

Keep your structure, tidy selected folders or request an organization proposal. Unclear items stay put; consequential moves and link repairs appear in the plan.

None of this information is sent back to the github project. Your preferences are kept locally in your vault. Note that some AI Agent models may share data to parent companies to train their models. For a full private experience consider a local LLM.

**What you'll have**

- Your `me.md` briefing and an `AGENTS.md` that tells assistants where to start.
- The folder structure and map notes you accepted, plus a Skill Map showing your selected tools.
- The three basics and any additional systems or skills you chose.

Read the [practical tutorial](tutorial.md) to get started, or download the [optional worked examples](https://github.com/ceprecia/ASTORIALab/releases/download/v1.3.1/ASTORIA-examples-v1.3.1.zip) for longer practice. See the [manual setup guide](00%20ASTORIA/skills/setup-my-vault/references/manual_setup.md) for detailed setup instructions.

## Try a workflow

**After setup**, start with a Companion for ongoing work. Direct utility skills and passive writing profiles support other tasks. The eight groups below are available; your choices determine what is installed.

![Eight toolkit groups arranged around the portable workflow layer, using their system icons](00%20ASTORIA/assets/system_toolkit.png)

| Group | Included by | Try asking |
| --- | --- | --- |
| [Research](00%20ASTORIA/systems/Research%20Assistant%20System.md) | Basics | “Research Companion, help me compare these research directions.” |
| [PhD and Career](00%20ASTORIA/systems/PhD%20and%20Career%20System.md) | Help me choose | “PhD Companion, help me prepare for an advisor conversation.” |
| [Study and Productivity](00%20ASTORIA/systems/Productivity%20and%20Study%20System.md) | Help me choose | “Study Companion, teach this topic from my notes, then help me practice.” |
| [Teaching](00%20ASTORIA/systems/Teaching%20Assistant%20System.md) | Help me choose | “Teaching Companion, help me prepare a class from these course sources.” |
| [Engineering](00%20ASTORIA/systems/Engineering%20System.md) | Help me choose | “Engineering Companion, help me plan this device build.” |
| [System Builder](00%20ASTORIA/systems/ASTORIA%20System%20Builder.md) | Basics | “Update my working preferences in me.md.” |
| [Janitor](00%20ASTORIA/systems/Janitor%20System.md) | Basics | “Folder Janitor, organize these files using my structure and repair their links.” |
| [Writing](00%20ASTORIA/systems/Writing%20System.md) | Help me choose | “Writing Companion, help develop this document.” |

Research includes its required shared writing helpers. Their presence does not select the whole Writing System.

Research and PhD/Career have separate Companions and internal Coordinators.

For writing projects, start with **Writing Companion**. Named capture, summary, handoff, redaction and style-profile tasks go directly to their utility. Capture requests save to their known owner. Summaries stay in chat unless saving is authorized. **Research Output Coordinator** helps you finish, share and publish research through publication packages, reproducibility, data/code releases, engagement, handover and funding requirements, borrowing the shared writing team when needed.

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

**Connect your notes and results.** Use Obsidian to read, edit and link the same Markdown files your assistant works with. Give each project a MOC linking its notes, papers and outputs, then ask your assistant to save useful work in the appropriate note and link it back. Existing scientific files can keep their established layout. Obsidian's [internal links](https://obsidian.md/help/links) help you follow these connections, while the bundled templates give new notes a consistent starting point.

**Keep it organized as it grows.** In the [Janitor System](00%20ASTORIA/systems/Janitor%20System.md), ask **Janitor Companion** to “Clean up my vault.” It routes checks and presents fixes for your approval. **Vault Janitor** checks layout, instructions and links. **Folder Janitor** organizes selected folders and repairs affected paths and links while preserving MOC prose. **Skills Janitor** checks skill consistency and generated views. **Agent Janitor** traces instruction drift and tests proposed fixes. After folder or template changes, [Vault Builder](00%20ASTORIA/skills/vault-builder/SKILL.md) refreshes the layout reference.

## License and sources

Keep [LICENSE, including source-specific notices](LICENSE), and capability-specific sources with the files. MIT covers ASTORIA's original material; adaptations retain their source terms. External tools and datasets retain their terms. Assistant names belong to their respective owners. 
