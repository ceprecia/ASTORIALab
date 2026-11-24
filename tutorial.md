# A practical guide to ASTORIA

[Return to the README](README.md)

Start with a familiar chat problem, get comfortable with your files, then try
ASTORIA on a small task. The second half of this guide has complete fictional
projects for all eight systems. Read in order or jump to the work you want to do.

**Guided reading path**

1. [Why save work outside one chat?](#why-save-your-work)
2. [Get comfortable with your workspace](#your-workspace)
3. [Understand the pieces](#how-the-pieces-fit)
4. [See how work is organized](#how-work-is-organized)
5. [Set up your vault](#guided-setup)
6. [Ask a normal chat question](#ordinary-requests)
7. [Continue with a different assistant](#continue-with-another-assistant)
8. [Make it yours](#make-it-yours)

**Jump to a system:** [Research](#research) · [Janitor](#janitor) ·
[System Builder](#system-builder) · [Writing](#writing) ·
[Study and Productivity](#study-productivity) · [Teaching](#teaching) ·
[Engineering](#engineering) · [PhD and Career](#phd-career)

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

Use a separate copy of the starter folder for practice. Open that folder in
Obsidian with **Open folder as vault**. You can explore the notes before running
guided setup. A Markdown editor can read the same files.

### Try a tiny note

Create `practice_note.md` at the root of that practice copy and paste:

```markdown
# My first practice note

**Question:** What do I want to understand about this project?

- [ ] Read the project brief.
- [ ] Write one question in my own words.

[Open the proofreading brief](tutorial_examples/research/inputs/project_brief.md)
```

The `#` makes a heading, paired `**` marks bold text, `- [ ]` makes a checklist
item, and `[label](path)` makes a standard Markdown link. The linked brief is
included in this starter copy; its path is relative to your note.

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

![Five layers of the researcher-owned workspace](00%20ASTORIA/assets/astoria_architecture.png)

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

Open the practice vault in your assistant and give it access to that folder.
For first-time setup and later updates, use the same entry:

> Set up my vault

The assistant first resolves whether you are setting up for the first time or
updating an existing ASTORIA vault. It waits for that choice unless you already
made it explicit. Resuming an interrupted setup reuses completed answers.

For a new vault, choose **Start with the basics** or **Help me choose**.

- **Basics:** Research Assistant, Janitor and ASTORIA System Builder, with
  their required shared helpers.
- **Help me choose:** Writing, Study and Productivity, Teaching, Engineering,
  and PhD and Career are additional choices. Relevant research method and
  software groups can be added when needed.

An included helper does not select its entire system. Some Writing helpers
support Research while the full Writing System remains an optional choice.
The installed selection and the available shelf are different things.

You can offer a GitHub skill link, paste your own workflow instructions, point
to a local skill folder, or skip extra skills. Your assistant includes the accepted skills and their supporting files in the
setup plan.

For organization, choose **Keep my structure**, **Tidy selected folders**, or
**Help propose organization**. The assistant asks about actual owners and use,
keeps unclear items in place and preserves useful operational packages. Proposed
consequential moves include the affected link repairs.

First review the briefing answers. Next, review the structure, tools and
organization plan before the build. Those two reviews keep your choices
together. Detailed questions and procedures live in the setup skill and the
manual guide linked from the [README's setup section](README.md#get-started).

For an update, show the assistant your working vault and the new starter
download. It preserves recorded system choices, custom skill ownership and
removals. Newly available additions remain choices. Review proposed repairs;
the updater retains its two janitor audit passes.

<a id="ordinary-requests"></a>

## 6. Ask a normal chat question

You do not need a special command language to use skills. Naming a capability
can make the request clear. Give it a task and the relevant files.

Try this small Research request in the practice vault:

```text
Research Companion, read tutorial_examples/research/inputs/project_brief.md
and tutorial_examples/research/inputs/protocol.md. Restate the fixed question
and identify one design decision that still needs attention. Use only those
files and keep the response here in chat.
```

The packet is an invented protocol and synthetic data, not a published article.
For an article summary, supply the actual article you want summarized and ask
the assistant to ground its answer in that source.

Study and skill creation are ordinary requests too:

- **Study Companion, after selecting Study and Productivity:** “Use the lesson
  in the Study example to teach one concept, ask me a question and wait for my
  answer.”
- **Skill Builder:** “Use the custom-skill request in the System Builder
  example to help turn this repeated task into one reusable skill.”

The [Research](#research), [Study](#study-productivity), and
[System Builder](#system-builder) walkthroughs below name their exact input
files and show fuller prompts.

<a id="continue-with-another-assistant"></a>

## 7. Continue with a different assistant

Before switching, save the context you want the next assistant to use. For the
small Research request above, ask:

```text
Save a short practice_notes/proofreading_handoff.md in this practice vault.
Name the two Research input files we just read. Record that the proofreading
question is fixed, its prediction is provisional, and no design revision has
been adopted. Set the next task to comparing passage-assignment options and
carryover concerns from the protocol. Keep unknowns explicit.
```

Open and check the saved note. It should contain the stated context and next
task, not a claim that the experiment or its checks were performed. For an
ongoing project, its owning map is the place to keep this useful context; its
project `AGENTS.md` connects the assistant to the briefing and map.

Then open the same practice vault in another assistant and ask:

```text
Read this practice vault's AGENTS.md and me.md, then
practice_notes/proofreading_handoff.md and the source files it names.
Restate the fixed question and continue the documented next design task.
Keep proposals separate from decisions already adopted.
```

Check the new assistant's folder access and available tools. Responses and tool
capabilities can differ. Useful continuation depends on the saved files carrying
the question, decisions, evidence and next step.

<a id="make-it-yours"></a>

## 8. Make it yours

Start with a small task and change the system around what you actually do.
Update preferences through Me Builder. Keep useful folder choices and use the
janitors for a selected cleanup. Add systems or individual skills through
**Set up my vault** and the existing skill owners when a need arises.

You can change an example input, try another system, or bring a bounded task
from your own work. Keep the fictional learning projects separate from your
actual projects. The eight walkthroughs below show purpose, prerequisites,
files, prompts, outputs and a next customization for each system.

## Choose a worked example

| System | Included by | Try this example when you want to… |
| --- | --- | --- |
| [Research Assistant](#research) | Basics | Turn a question into a plan and inspect synthetic observations |
| [Janitor](#janitor) | Basics | Organize a genuinely mixed folder without losing its links or decisions |
| [ASTORIA System Builder](#system-builder) | Basics | Change a briefing and make a small reusable skill |
| [Writing](#writing) | Help me choose | Turn supplied evidence into a defensible short scientific report |
| [Study and Productivity](#study-productivity) | Help me choose | Study a student course and make a workable practice plan |
| [Teaching](#teaching) | Help me choose | Prepare an instructor's week, activity, rubric and feedback |
| [Engineering](#engineering) | Help me choose | Review a simple circuit and prepare build checks |
| [PhD and Career](#phd-career) | Help me choose | Turn a fictional handbook and progress record into a milestone plan |

![The eight available ASTORIA system groups](00%20ASTORIA/assets/system_toolkit.png)

The diagram shows what is available, not what every vault installs. These are
original fictional learning materials. Supplied outputs are **illustrative**,
not records of an assistant run, an experiment, a class or a physical build.
Component specifications are identified separately through manufacturer sources.

## Work through an example

1. Complete setup in the separate practice vault. Select the system named by
   the example.
2. Obtain its whole `inputs/` folder from the same starter copy as this guide.
   On GitHub, linked files provide previews; the starter download provides the
   complete folder. Copy the inputs into one working folder you choose inside
   the practice vault. Keep their nested layout.
3. In the detailed prompts below, replace `<practice_folder>` with that working
   folder's actual path. The assistant starts from the practice vault's
   `AGENTS.md` and uses only the named inputs for the exercise.
4. Keep supplied inputs unchanged unless the example practices moving them.
   Request results in an `outputs/` folder inside the practice folder, or keep
   them in chat as the prompt says.
5. Open `illustrative_outputs/` after trying the task. Compare source fidelity,
   decisions and visible outputs rather than expecting identical wording.

These materials are a reference shelf. Setup does not create their fictional
projects, enroll you in the courses or install the example custom skill.

<a id="research"></a>

## Research Assistant: a proofreading pilot

**Purpose.** Research Companion helps frame and coordinate research across
question, design, analysis and reporting. Try it when you have a scientific
question and need to decide what the available evidence supports.

**Needs.** Basics. No optional imaging or software group is needed for this
small supplied-data exercise. Its descriptive arithmetic does not require an
external service.

**Get.** Copy the [Research inputs](tutorial_examples/research/inputs):
[brief](tutorial_examples/research/inputs/project_brief.md),
[protocol](tutorial_examples/research/inputs/protocol.md) and
[CSV](tutorial_examples/research/inputs/synthetic_results.csv).

**Try it.**

1. Read the question and protocol. Notice which design choices are still open.
2. Ask Research Companion to produce a plan and descriptive summary:

```text
Research Companion, use only project_brief.md, protocol.md and
synthetic_results.csv in <practice_folder>. Keep the proofreading question
fixed. Identify design gaps and summarize the eight paired synthetic records
with denominators. Separate arithmetic, interpretation and what remains
unknown. Do not search literature or treat invented records as empirical
evidence. Save research_plan.md and synthetic_summary.md in outputs/ here.
```

3. Check the summary against the CSV. Ask the assistant to add a short
   continuation note naming the fixed question, sources and unresolved design
   choice. A different assistant should be able to resume from those files.

**See.** An [illustrative plan](tutorial_examples/research/illustrative_outputs/research_plan.md)
and [summary](tutorial_examples/research/illustrative_outputs/synthetic_summary.md).
The table has eight paired records, 12 planted errors per passage, and no
justification for a population or causal claim.

**Continue.** Change the question or supply approved observations from your own
project. Preserve the distinction between a proposed design, a synthetic check
and collected evidence.

<a id="janitor"></a>

## Janitor: a mixed exhibit folder

**Purpose.** Folder Janitor files selected material and repairs its references.
Vault Janitor checks vault structure and links; Skills Janitor checks skills
and generated discovery views. Try this system when organization obscures an
owner or breaks navigation.

**Needs.** Basics. This is a file-operation exercise on a practice copy.

**Get.** Copy the entire [Janitor inputs](tutorial_examples/janitor/inputs),
including `stuff/` and `kiosk_bundle/`. Read
[organization_choices.md](tutorial_examples/janitor/inputs/organization_choices.md)
and the existing [exhibit map](tutorial_examples/janitor/inputs/exhibit_map.md).

**Try it.**

1. Inspect the mixed notes, working flyer, reusable reference and kiosk package.
2. Ask for a finite proposal:

```text
Folder Janitor, tidy only <practice_folder>, following organization_choices.md
and exhibit_map.md. First show exact sources, destinations and affected links.
Keep unclear items in place and keep the kiosk package intact. Preserve note
text and the dated map decision. Do not make new maps or apply moves until I
accept this exercise's plan.
```

3. Accept or edit that concrete plan. Ask the assistant to apply the accepted
   moves and path repairs together, then check every affected link and manifest
   target. A kept or unclear item is a valid outcome, not unfinished sorting.

**See.** A possible [move plan](tutorial_examples/janitor/illustrative_outputs/move_plan.md)
and [verification checklist](tutorial_examples/janitor/illustrative_outputs/verification_checklist.md).
The mixed-owner note and unidentified CSV remain in place.

**Continue.** Try **Keep my structure** instead: the original files should
remain where they are. Later, apply a bounded cleanup to a folder whose actual
owners and retention needs you know.

<a id="system-builder"></a>

## ASTORIA System Builder: a briefing and a custom skill

**Purpose.** System Builder's skills configure the vault and maintain its
reusable workflows. Try them when your preferences change or a narrow task
keeps recurring.

**Needs.** Basics and the separate practice vault. The custom skill is one
explicit addition, not selection of an entire optional system.

**Get.** Copy the [System Builder inputs](tutorial_examples/system_builder/inputs):
[briefing answers](tutorial_examples/system_builder/inputs/briefing_answers.md),
[custom-skill request](tutorial_examples/system_builder/inputs/custom_skill_request.md)
and [inventory](tutorial_examples/system_builder/inputs/packet_inventory.csv).

**Try it.**

1. Ask Me Builder for a briefing draft, using only the fictional answers:

```text
Me Builder, read briefing_answers.md in <practice_folder>. Draft a briefing
using your current template, keeping unspecified details unknown. Return it
here first. This is a fictional practice persona; do not change my working
vault's me.md or install additional systems.
```

2. In the practice vault, ask Skill Builder to inspect
   `custom_skill_request.md`, check overlap and dependencies, and create only
   the accepted skill folder. Include its supporting reference. Review the
   description and trigger phrases. Have Skills Janitor refresh the practice
   vault's views and record this as your custom addition.
3. Invoke the created skill on the copied inventory:

```text
Use format-seed-labels on <practice_folder>/packet_inventory.csv. Return the
labels here and report any incomplete rows. Keep source values unchanged.
```

**See.** A [briefing excerpt](tutorial_examples/system_builder/illustrative_outputs/sample_briefing.md),
a complete illustrative [skill folder](tutorial_examples/system_builder/illustrative_outputs/format-seed-labels),
its [supporting format](tutorial_examples/system_builder/illustrative_outputs/format-seed-labels/references/label_format.md)
and [labels](tutorial_examples/system_builder/illustrative_outputs/labels.md).
Do not treat that illustrative folder as already installed. If you choose to
import a ready-made folder, include all of it; a GitHub link or local folder
goes through the import flow, while pasted workflow instructions go through
Skill Builder.

**Continue.** Supply a small procedure you actually repeat. Reuse an existing
skill when it already owns the job, and preserve supporting files and attribution
when importing someone else's skill.

<a id="writing"></a>

## Writing: an evidence-bounded scientific report

**Purpose.** Writing Companion develops a document through appropriate drafting
and review skills. Try it when you have sources and a document to produce or
revise, rather than an open research-design decision.

**Needs.** Select the Writing System through **Help me choose**. Its full
workflow is an optional choice even when some shared writing helpers support
Research. No specialist modality is needed here.

**Get.** Copy the [Writing inputs](tutorial_examples/writing/inputs):
[brief](tutorial_examples/writing/inputs/project_brief.md),
[plant data](tutorial_examples/writing/inputs/plant_height_data.csv) and
[rough report](tutorial_examples/writing/inputs/rough_report.md).

**Try it.**

1. Read the fictional methods and rough report. Look for claims that are
   stronger than the supplied record.
2. Run the audit before asking for a revision:

```text
Writing Companion, read only project_brief.md, plant_height_data.csv and
rough_report.md in <practice_folder>. Make a claim-to-source table and a short
report outline here. Identify unsupported statements. Do not search papers,
add analyses or change the inputs. Keep the illustrative outputs closed.
```

3. Ask for a report of at most 450 words with Question, Methods, Results and
   Limitations sections, preserving the synthetic label and supplied values.

**See.** The [evidence ledger](tutorial_examples/writing/illustrative_outputs/evidence_ledger.md)
and [revised report](tutorial_examples/writing/illustrative_outputs/revised_report.md).
Compare what each claim rests on, not the exact phrasing.

**Continue.** Replace the invented packet with approved methods and outputs
from your own work. Keep evidence review distinct from prose polishing.

<a id="study-productivity"></a>

## Study and Productivity: a student's course and practice week

**Purpose.** Study Companion helps you learn supplied material; planning tools
help turn study intentions into workable actions. Try this system when you are
the learner, preparing a lesson or practicing for an assessment.

**Needs.** Select Study and Productivity through **Help me choose**. The
student's course is separate from the instructor course below.

**Get.** Copy the [Study and Productivity inputs](tutorial_examples/study_productivity/inputs):
[course note](tutorial_examples/study_productivity/inputs/student_course_note.md),
[student syllabus](tutorial_examples/study_productivity/inputs/student_syllabus.md),
[lesson and practice](tutorial_examples/study_productivity/inputs/lesson_and_practice.md)
and [planning brief](tutorial_examples/study_productivity/inputs/weekly_planning_brief.md).
Their requirements, not a real institution's policies, govern this exercise.

**Try it.**

1. Read the student's course requirements and the supplied lesson.
2. Ask the assistant to teach and check understanding:

```text
Study Companion, read student_course_note.md, student_syllabus.md and
lesson_and_practice.md in <practice_folder>. Teach one short concept, ask me a
practice question, wait for my answer, then explain the answer using those
sources. Do not answer your own question before I try. Treat this as an
invented course.
```

3. Try the productivity workflow on the supplied availability:

```text
WOOP, use weekly_planning_brief.md and student_syllabus.md in <practice_folder>
to propose a small study plan. Give a wish, outcome, obstacle and if-then plan
that fit those sources and the available sessions. Keep it here in chat; do
not create reminders or calendar events.
```

**See.** Compare the [explanation and answers](tutorial_examples/study_productivity/illustrative_outputs/study_explanation_and_answers.md)
and [weekly plan](tutorial_examples/study_productivity/illustrative_outputs/weekly_plan.md)
with the explanation, practice feedback and schedule you obtained. A good plan
fits the source deadlines and available time.

**Continue.** Supply your own syllabus and current unit. Keep student learning
separate from instructor planning, and give the assistant the actual lecture
material when asking for an answer according to that course.

<a id="teaching"></a>

## Teaching: an instructor's week and feedback

**Purpose.** Teaching Companion coordinates work from an instructor's approved
course sources. Try it when preparing a class, activity, rubric or feedback in
a teaching role.

**Needs.** Select Teaching through **Help me choose**. This is a different
fictional course from the student example. No live learning platform or student
records are connected.

**Get.** Copy the complete [Teaching inputs](tutorial_examples/teaching/inputs):
[instructor course note](tutorial_examples/teaching/inputs/instructor_course_note.md),
[instructor syllabus](tutorial_examples/teaching/inputs/instructor_syllabus.md),
[week sources](tutorial_examples/teaching/inputs/week_02_sources.md) and
[rubric and student work](tutorial_examples/teaching/inputs/activity_rubric_and_student_work.md).

**Try it.**

1. Identify the week's learning objective and class length in the syllabus.
2. Ask for materials tied to those sources:

```text
Teaching Companion, read instructor_course_note.md, instructor_syllabus.md,
week_02_sources.md and activity_rubric_and_student_work.md in <practice_folder>.
Draft a class plan, one activity and formative feedback using the supplied
rubric, objective and class length. Keep its point scheme. Identify any missing
policy instead of inventing one. Return drafts here; do not post, grade in a
live system or contact anyone.
```

3. Check the activity against the objective, the plan against available class
   time, and feedback against the rubric and supplied student response.

**See.** A possible [lesson plan and activity](tutorial_examples/teaching/illustrative_outputs/lesson_plan_and_activity.md)
and [feedback](tutorial_examples/teaching/illustrative_outputs/feedback.md).
They are examples for instructor review, not actual grades or course policy.

**Continue.** Use the syllabus, role and sources from a course you actually
teach, and keep consequential grading or communication within your authorized
course workflow.

<a id="engineering"></a>

## Engineering: a low-voltage indicator circuit

**Purpose.** Engineering Companion brings a design question to the appropriate
technical skills. Try it when interfaces, parts, calculations and checks need
to agree before you build.

**Needs.** Select Engineering through **Help me choose**. Reading and reviewing
this example needs no hardware. Physical assembly would require the specified
parts, tools and an independently checked build plan.

**Get.** Copy the [Engineering inputs](tutorial_examples/engineering/inputs):
[project map](tutorial_examples/engineering/inputs/moc_indicator.md),
[circuit and parts](tutorial_examples/engineering/inputs/circuit_and_parts.md)
and [build/test plan](tutorial_examples/engineering/inputs/build_and_test_plan.md).

**Try it.**

1. Read the schematic, power limits and linked manufacturer source. Distinguish
   a stated component specification from a calculation or an unknown measurement.
2. Ask for a bounded review:

```text
Engineering Companion, review only the indicator-circuit packet in
<practice_folder>. Check the schematic, parts and proposed tests for agreement.
Separate manufacturer facts, assumptions, calculations and unmeasured results.
Return a corrected design-review draft and build-check table here. Do not
claim that a circuit was assembled, powered or tested.
```

3. Compare the proposed checks with the illustrative record. Keep every
   physical-result field unmeasured until someone actually performs that test.

**See.** An [illustrative design review](tutorial_examples/engineering/illustrative_outputs/illustrative_design_review.md)
and [unmeasured test record](tutorial_examples/engineering/illustrative_outputs/illustrative_test_record.csv).
These demonstrate preparation and evidence boundaries, not a working device.

**Continue.** Replace the simple brief with a bounded design of your own.
Verify exact interfaces and source specifications before treating it as a
construction guide.

<a id="phd-career"></a>

## PhD and Career: a handbook and milestone discussion

**Purpose.** PhD Companion supports degree planning, advisor conversations and
career decisions using the user's circumstances and current sources. Try it
when a requirement, deadline or mentorship decision needs a grounded plan.

**Needs.** Select PhD and Career through **Help me choose**. Its companion is
separate from Research Companion. This packet uses invented policies only.

**Get.** Copy the [PhD and Career inputs](tutorial_examples/phd_career/inputs):
[project map](tutorial_examples/phd_career/inputs/moc_degree_path.md),
[fictional handbook](tutorial_examples/phd_career/inputs/fictional_handbook.md),
[student context](tutorial_examples/phd_career/inputs/student_context.md) and
[completion evidence](tutorial_examples/phd_career/inputs/completion_evidence.md).

**Try it.**

1. Read the stated requirements and distinguish completed milestones from
   intentions and missing evidence.
2. Ask for a source-grounded plan:

```text
PhD Companion, use only the fictional handbook, student context and completion
evidence in <practice_folder>. Make a milestone plan and a short advisor
meeting agenda. Trace deadlines and completion labels to those files, keep
unknown requirements unknown, and distinguish proposals from confirmed dates.
Return the drafts here. Do not contact anyone or create reminders.
```

3. Check the dates and prerequisites against the fictional handbook. Identify
   which question would most usefully go to the advisor.

**See.** An [illustrative milestone plan](tutorial_examples/phd_career/illustrative_outputs/illustrative_milestone_plan.md)
and [advisor agenda](tutorial_examples/phd_career/illustrative_outputs/illustrative_advisor_agenda.md).
These policies do not apply to an actual university.

**Continue.** Bring your current handbook and documented progress. Verify real
requirements from the responsible program before relying on a deadline.
