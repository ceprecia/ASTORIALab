# A practical guide to ASTORIA

Start with a familiar chat problem, get comfortable with your files, then use
ASTORIA in your own work. Read in order or choose a section below.

1. [Why save work outside one chat?](#why-save-your-work)
2. [Get comfortable with your workspace](#your-workspace)
3. [Understand the pieces](#how-the-pieces-fit)
4. [See how work is organized](#how-work-is-organized)
5. [Set up your vault](#guided-setup)
6. [Talk with your assistant](#ordinary-requests)
7. [Continue with a different assistant](#continue-with-another-assistant)
8. [Make it yours](#make-it-yours)

<a id="why-save-your-work"></a>

## 1. Why save work outside one chat?

Yesterday, you and an assistant agreed on a question and a useful next step.
Today, you open another chat. The new response sounds reasonable, but it answers
a slightly different question. Later, an agreed check disappears from the
procedure. You spend time recovering what you had already settled.

Those are two different problems. **Context drift** changes what the work is
about. **Procedure drift** changes how it is done. A saved project map can retain
the question, decisions, evidence and next step. A skill can retain the steps
for a recurring job. Neither makes an assistant infallible; both give you
something concrete to inspect and correct.

ASTORIA puts that context and those workflows in files you own. A chat remains
a useful place to think. The result you want to keep has a home beyond that chat.

<a id="your-workspace"></a>

## 2. Get comfortable with your workspace

**The vault is a folder of files.** Markdown notes are ordinary text files with
simple formatting. **Obsidian is an interface** for reading, editing and linking
those files. **An assistant works with the files you permit it to access.**
Opening a chat alone does not tell it which folder contains your work.

Open your vault in Obsidian with **Open folder as vault**. A Markdown editor
can read the same files.

### Try a tiny note

Create a note called `next_question.md` and write a question in it. In the same
folder, create `practice_note.md` and paste:

```markdown
# My first practice note

**Question:** What do I want to understand about my work?

- [ ] Write one question in my own words.
- [ ] Choose a next step.

[Read my next question](next_question.md)
```

The `#` makes a heading, paired `**` marks bold text, `- [ ]` makes a checklist
item, and `[label](path)` makes a standard Markdown link. This link points to
the other note you just created in the same folder.

Edit the question, tick one item, and switch between editing and reading views.
Follow the link and return to your note. Try collapsing and expanding the
heading with your editor's fold control, where available. You have changed and
navigated a file without needing an assistant.

<a id="how-the-pieces-fit"></a>

## 3. Understand the pieces

Here is how this guide uses four common terms:

| Term | Plain meaning | What it contributes |
| --- | --- | --- |
| Model | The component that generates a response from its input | Language, suggestions and reasoning to inspect |
| Harness | The application and surrounding environment that run the model | Context, file access, tools and permission controls |
| Agent | A model working in that environment on a task | It follows instructions and uses available tools to help do the work |
| Skill | Reusable instructions for a bounded job, with supporting files when needed | A procedure the assistant can load for that job |

A language model is one component in this arrangement. ASTORIA supplies durable
context and portable workflows that can be used with replaceable assistants.
The tool you use can change while your files remain yours.

![Five layers of the researcher-owned workspace](../00%20ASTORIA/assets/astoria_architecture.png)

At the center is **your researcher core**, including the preferences and working
context recorded in `me.md`. Around it sit **the vault and evidence**, then
**maps and workflows**. **Replaceable assistants** work with those files.
**Optional extensions** add capabilities when you choose them. The outer tools
support the work; your judgment remains at the center.

<a id="how-work-is-organized"></a>

## 4. See how work is organized

You can ask for help in ordinary language. For ongoing work, a **Companion**
guides the conversation. Its internal **Coordinator** finds the appropriate
capability. A **skill** handles a bounded job, such as checking a claim against
its source or preparing a practice exercise. You do not need to launch every
role or memorize the catalog.

The files connect those capabilities to your work. `me.md` holds your briefing.
`AGENTS.md` tells an assistant where to begin. A project map, or **MOC**, holds
that project's context, useful links and saved progress. The Skill Map helps
find installed capabilities; the available catalog shows choices you can add.

PARA gives four useful roles for material:

| Role | What belongs there | Example |
| --- | --- | --- |
| Projects | Work with an outcome or finish point | Preparing a small exhibit |
| Areas | Responsibilities maintained over time | Maintaining an inventory |
| Resources | References useful across tasks | A note about display paper sizes |
| Archive | Inactive work retained for later reference | A completed exhibit's records |

Use those roles to understand ownership. Keep your chosen names and useful
existing structure. A cleanup should address a present need, not create empty
folders for every possible topic.

<a id="guided-setup"></a>

## 5. Set up your vault

Download the starter ZIP from [Releases](https://github.com/ceprecia/ASTORIALab/releases)
and extract it. Open the extracted folder in Obsidian, then open it in your
assistant and give the assistant access to the folder. If you already have an
ASTORIA vault, show the assistant both your working vault and the new starter
folder so it can help you update.

For first-time setup and later updates, use the same entry:

> Set up my vault

The assistant first asks whether this is a new setup or an update, unless you
already made that clear. If you resume an interrupted setup, it reuses the
answers you have already given.

For a new vault, choose **Start with the basics** or **Help me choose**.
Basics includes **Research Assistant**, **Janitor** and **ASTORIA System
Builder**, with their required helpers. Help me choose offers Writing, Study
and Productivity, Teaching, Engineering, and PhD and Career. Relevant research
methods and software groups can be added when needed. A shared helper does
not select its entire system.

You can also offer a GitHub skill link, paste your own workflow instructions,
point to a local skill folder, or skip extra skills. The assistant includes
accepted additions and their supporting files in the setup plan.

For organization, choose **Keep my structure**, **Tidy selected folders**, or
**Help propose organization**. Explain how you use your work and who owns it.
Unclear items stay in place. Review proposed moves and the links they affect
before anything is moved.

First review your briefing answers. Then review the proposed structure, skills
and organization before the assistant applies the plan. After setup, open the
results in Obsidian and check that they reflect your choices.

For an update, the assistant preserves your system choices, custom skills and
deliberate removals. New additions remain choices. It first applies the update,
then audits the vault and shows any proposed repairs for your approval. After
any approved repairs, it rechecks for missed updates and runs a final audit.

<a id="ordinary-requests"></a>

## 6. Talk with your assistant

Once ASTORIA is integrated, use your assistant as you normally would. You can
start with a question and continue the conversation one step at a time.

For a research summary, share an article you want to read. Research Summarizer
can help you understand its question, methods, findings and limits.

> Can you summarize this article?

If you chose Study and Productivity, tell the assistant what topic you want
to learn. Share course materials when you want the explanation to follow your
course.

> Can you help me study this subject?

For a task you repeat, describe what you do and what a useful result looks
like. Skill Builder can help turn that procedure into a reusable skill.

> Can we make a skill for this?

Useful answers depend on context: what you are working on, what you have
already decided and the sources you share. You can provide that context as
you go.

For preferences that should last beyond one chat, `me.md` is your vault's
editable briefing. It describes your work, preferences and standing
instructions. Read it, correct what does not fit and update it as your work
changes. An assistant can use it when it has access and reads it; it is not
an automatic record of your conversations.

<a id="continue-with-another-assistant"></a>

## 7. Continue with a different assistant

A portable project keeps its instructions, current context and materials
together:

| Part | What it keeps |
| --- | --- |
| `AGENTS.md` | Project instructions and where the assistant should begin |
| Project map of content (MOC) | Saved context, decisions, useful links and the next step |
| `files` folder | The papers, notes, data and other materials for the work |

Before switching assistants, ask the current one to save the progress you want
to keep:

> Can you save where we left off?

Open the project map and check what was saved. It should make clear what you
decided, what remains open and what comes next. An idea still under discussion
should remain a proposal. Instructions alone do not save a conversation.

Open the same project or the whole vault in another assistant. Make sure it
can read the project instructions, map and materials, plus any linked vault
briefing or shared skills it needs. A file outside its permitted folder may
need additional access.

> Can we continue this project?

Check that the new assistant understands where you stopped. Its tools and
answers may differ; the saved project gives you a common place to continue.

<a id="make-it-yours"></a>

## 8. Make it yours

Keep the organization that helps you find and use your work. If PARA does not
fit, describe how you would like things arranged and ask your assistant to
propose changes. Review the plan before files move.

Your skills can change too. Add the systems or skills you need, adapt a
procedure that no longer fits, or build a skill for a task you repeat. You do
not need every available capability.

Update `me.md` when your preferences change. You might want shorter answers,
a different writing style or a different way of reviewing plans. Tell your
assistant what should change, then read the updated briefing to check that
it says what you intended.

For longer practice, explore the [optional worked examples](examples/README.md)
for all eight systems. These fictional learning materials stay separate from
your own projects and are not needed to follow this guide.
