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

You can ask for help in your own words. Open the [proofreading brief](tutorial_examples/research/inputs/project_brief.md)
and [protocol](tutorial_examples/research/inputs/protocol.md) in the practice
vault and show them to your assistant. Then ask:

> Can you help me plan this study?

Read the answer and ask a follow-up about anything unclear. The assistant has
a question and source material to work with; you can develop the conversation
one step at a time. These files describe an invented study. To summarize a
paper instead, supply the actual paper you want to discuss.

Other systems work the same way. After selecting **Study and Productivity**,
open its [lesson](tutorial_examples/study_productivity/inputs/lesson_and_practice.md)
and ask:

> Can you explain this lesson?

For a task you repeat, show Skill Builder the
[example request](tutorial_examples/system_builder/inputs/custom_skill_request.md):

> Could we turn this task into a skill?

The [worked examples below](#research) give you materials to try these
conversations and see what useful results can look like.

<a id="continue-with-another-assistant"></a>

## 7. Continue with a different assistant

Before switching assistants, ask the current one to save what you want to keep:

> Can you save what we decided and what comes next?

Open the saved note and check it. In the proofreading example, it should point
back to the source files and record the design question you have not settled.
An idea still under discussion should remain a proposal.

Open the same practice vault in another assistant, show it the note and ask:

> Can we continue where we left off?

Check that the new assistant can access the files and understands where you
stopped. Its tools and answers may differ. For ongoing work, keep this context
in your existing project map so that useful progress has one place to return to.

<a id="make-it-yours"></a>

## 8. Make it yours

Tell your assistant when a preference changes. Me Builder can help update your
briefing, and the janitors can help with a folder that has become difficult to
use. Keep the structure that works for you.

Use **Set up my vault** when you want to add a system, update ASTORIA or bring
in another skill. You can also describe a procedure you repeat and ask Skill
Builder to help make it reusable.

Choose a worked example below that interests you. Try the supplied materials,
then adapt the conversation to your own work. Keep the fictional practice
projects separate from your real projects.

## Choose a worked example

| System | Included by | Try this example when you want to… |
| --- | --- | --- |
| [Research Assistant](#research) | Basics | Plan a study and understand invented observations |
| [Janitor](#janitor) | Basics | Organize a mixed folder while keeping its notes and links |
| [ASTORIA System Builder](#system-builder) | Basics | Change a briefing and make a reusable labeling skill |
| [Writing](#writing) | Help me choose | Turn supplied evidence into a scientific report |
| [Study and Productivity](#study-productivity) | Help me choose | Learn a course topic and plan practice time |
| [Teaching](#teaching) | Help me choose | Prepare a class, activity and feedback |
| [Engineering](#engineering) | Help me choose | Review a circuit before building it |
| [PhD and Career](#phd-career) | Help me choose | Prepare a milestone plan and advisor conversation |

![The eight available ASTORIA system groups](00%20ASTORIA/assets/system_toolkit.png)

The diagram shows available systems; your setup choices determine which are
installed. The projects below are fictional. Their finished examples show
possible results, not work that an assistant, class, experiment or physical
build has actually completed. Engineering component specifications have their
own manufacturer sources.

## Work through an example

Use the separate practice vault you set up earlier. Choose the system named
by the example, then copy its whole inputs folder into that vault. The starter
download contains the complete folders; the links below let you preview their
contents on GitHub. Keep any nested folders together.

Open those files in your assistant or show it the copied folder. Start with
the suggested question and continue the conversation as you would with a
colleague. Use the supplied materials for the practice task and keep initial
answers in chat. Review proposed file moves or new skills before applying them.

Try the task before opening its finished examples. Compare how the answer uses
the sources and what it helps you do next; the wording need not be identical.
Setup leaves these learning materials as examples rather than creating active
projects from them.

<a id="research"></a>

## Research Assistant: a proofreading pilot

Research Companion helps you move from a scientific question to a plan and
interpretation. This example uses **Basics**, with no additional research
software or method group needed.

Copy the [Research inputs](tutorial_examples/research/inputs) and open the
[brief](tutorial_examples/research/inputs/project_brief.md),
[protocol](tutorial_examples/research/inputs/protocol.md) and
[invented results](tutorial_examples/research/inputs/synthetic_results.csv).
They explore whether a quiet break changes performance on a proofreading task.

> Can you help me plan this study?

Read the proposed plan and discuss an unresolved design choice. Then ask what
the invented results can tell you, and check the summary against the eight
paired records. Each passage contains 12 planted errors. Does the answer keep the original question, explain its arithmetic and
distinguish invented observations from evidence about real people?

Compare your answer with the [illustrative plan](tutorial_examples/research/illustrative_outputs/research_plan.md)
and [summary](tutorial_examples/research/illustrative_outputs/synthetic_summary.md).
Neither establishes a population effect or a causal finding.

To continue, change one design choice in a practice copy and ask how it affects
the plan. For your own research, bring your actual question, protocol and
approved observations.

<a id="janitor"></a>

## Janitor: a mixed exhibit folder

The Janitor System is part of **Basics**. Folder Janitor can organize selected
files and repair their links; Vault Janitor checks the wider structure, while
Skills Janitor maintains the skills and their discovery views.

Copy the entire [Janitor folder](tutorial_examples/janitor/inputs), including
its nested folders. Read the [cleanup request](tutorial_examples/janitor/inputs/organization_choices.md)
and [exhibit map](tutorial_examples/janitor/inputs/exhibit_map.md), then look
through the mixed notes, flyer, reusable reference and kiosk files.

> Can you help me organize this folder?

Review the proposed moves before accepting them. Some notes have unclear
ownership, so leaving them in place is useful. The kiosk files belong together
as one working package. The exhibit map's text and dated decision should survive.

When you are happy with the plan, ask:

> Apply the moves we agreed on and check the links afterward.

Compare the result with the [example move plan](tutorial_examples/janitor/illustrative_outputs/move_plan.md)
and [checks](tutorial_examples/janitor/illustrative_outputs/verification_checklist.md).
The mixed-owner note and unidentified table stay where they are.

Next, try **Keep my structure** on another practice copy, or ask about one
folder whose real purpose and owners you know.

<a id="system-builder"></a>

## ASTORIA System Builder: a briefing and a custom skill

System Builder is included in **Basics**. Its skills help you adapt the vault
to your preferences and turn a repeated task into a reusable workflow.

Copy the [System Builder inputs](tutorial_examples/system_builder/inputs).
Start with the fictional [briefing answers](tutorial_examples/system_builder/inputs/briefing_answers.md):

> Can we draft a briefing from these answers?

Read the draft alongside the answers. It should leave unspecified details
unknown and use the fictional preferences rather than changing your real
briefing. Compare it with the [example excerpt](tutorial_examples/system_builder/illustrative_outputs/sample_briefing.md).

Next, open the [label-making request](tutorial_examples/system_builder/inputs/custom_skill_request.md):

> Could we turn this task into a skill?

Discuss the proposed skill and review it before creation in the practice vault.
This adds one chosen skill, rather than selecting an entire optional system.
The assistant checks for overlap and includes the supporting instructions.
Then open the [inventory](tutorial_examples/system_builder/inputs/packet_inventory.csv):

> Can you make the labels?

Compare the labels with the [finished example](tutorial_examples/system_builder/illustrative_outputs/labels.md).
You can also inspect the [illustrative skill folder](tutorial_examples/system_builder/illustrative_outputs/format-seed-labels)
and its [format guide](tutorial_examples/system_builder/illustrative_outputs/format-seed-labels/references/label_format.md);
that example folder is not already installed.

Try another procedure you repeat. An existing skill may already cover it; if
you import someone else's skill, keep its supporting files and attribution.

<a id="writing"></a>

## Writing: an evidence-bounded scientific report

Choose the **Writing System** through **Help me choose**. Writing Companion
helps develop and review documents; Research's shared writing helpers do not
select this whole system.

Copy the [Writing inputs](tutorial_examples/writing/inputs) and open the
[brief](tutorial_examples/writing/inputs/project_brief.md),
[plant data](tutorial_examples/writing/inputs/plant_height_data.csv) and
[rough report](tutorial_examples/writing/inputs/rough_report.md).
The report deliberately makes claims stronger than the fictional record supports.

> Which claims need better evidence?

Read the answer against the brief and table. Ask about any claim whose source
you cannot find. When you understand what can be supported, continue:

> Could you help me revise this report?

The revision should retain the synthetic-data label, supplied values and
limitations. Compare it with the [evidence ledger](tutorial_examples/writing/illustrative_outputs/evidence_ledger.md)
and [revised report](tutorial_examples/writing/illustrative_outputs/revised_report.md).
Look at how the wording changes when a claim has less support.

For your own report, supply approved methods and results, then use the same
conversation to examine the claims before polishing the prose.

<a id="study-productivity"></a>

## Study and Productivity: a student's course and practice week

Choose **Study and Productivity** through **Help me choose**. Study Companion
helps you learn supplied material, while planning tools help you make time to
practice it.

Copy the [Study inputs](tutorial_examples/study_productivity/inputs). Read the
[course note](tutorial_examples/study_productivity/inputs/student_course_note.md)
and [student syllabus](tutorial_examples/study_productivity/inputs/student_syllabus.md),
then open the [lesson and practice](tutorial_examples/study_productivity/inputs/lesson_and_practice.md).
You are the learner in this fictional course about maps.

> Can you explain this lesson?

After the explanation, ask for a practice question. Try the practice question
before asking to see the answer. Discuss what you understood and where you got
stuck, then compare with the [example explanation and answers](tutorial_examples/study_productivity/illustrative_outputs/study_explanation_and_answers.md).

For the productivity example, show the assistant the
[planning brief](tutorial_examples/study_productivity/inputs/weekly_planning_brief.md)
as well as the syllabus:

> Can you help me plan my study week?

Check that the plan fits the supplied deadlines and available sessions. Compare
it with the [example week](tutorial_examples/study_productivity/illustrative_outputs/weekly_plan.md).
This practice conversation does not create calendar events or reminders.

Next, bring your own syllabus and current lesson. Supply the actual lecture
material when you want an explanation grounded in that course.

<a id="teaching"></a>

## Teaching: an instructor's week and feedback

Choose the **Teaching System** through **Help me choose**. Teaching Companion
helps prepare classes and feedback using an instructor's approved course sources.

Copy the [Teaching inputs](tutorial_examples/teaching/inputs). This time you
are the instructor for a different fictional course about clear procedures.
Read the [course note](tutorial_examples/teaching/inputs/instructor_course_note.md),
[syllabus](tutorial_examples/teaching/inputs/instructor_syllabus.md) and
[week's materials](tutorial_examples/teaching/inputs/week_02_sources.md):

> Can you help me plan this class?

Check that the plan addresses the learning objective and leaves students time
to attempt the activity. Compare it with the [example lesson plan and activity](tutorial_examples/teaching/illustrative_outputs/lesson_plan_and_activity.md).

Now open the [rubric and fictional student work](tutorial_examples/teaching/inputs/activity_rubric_and_student_work.md):

> How could I give useful feedback on this work?

Check the comments and proposed score against the rubric, then compare with
the [illustrative feedback](tutorial_examples/teaching/illustrative_outputs/feedback.md).
These are drafts for instructor review, not actual grades or course policy.

Keep the practice work in chat. To adapt it, bring your own approved course
materials, objectives and rubric, and review the proposed feedback in your
role as instructor.

<a id="engineering"></a>

## Engineering: a low-voltage indicator circuit

Choose the **Engineering System** through **Help me choose**. Engineering
Companion helps you connect a design question with its parts, drawings and
checks. Reading this example does not require hardware.

Copy the [Engineering inputs](tutorial_examples/engineering/inputs). Start
with the [project map](tutorial_examples/engineering/inputs/moc_indicator.md),
[circuit and parts](tutorial_examples/engineering/inputs/circuit_and_parts.md)
and [proposed build checks](tutorial_examples/engineering/inputs/build_and_test_plan.md).
Read the schematic and its linked manufacturer source.

> Do these drawings, parts and tests agree?

Trace the connections in the drawing and discuss any mismatch the assistant
finds. Manufacturer specifications, calculated estimates and physical
measurements should remain distinguishable. No circuit was assembled, powered
or physically tested for this example.

Compare your answer with the [illustrative design review](tutorial_examples/engineering/illustrative_outputs/illustrative_design_review.md)
and [unmeasured test record](tutorial_examples/engineering/illustrative_outputs/illustrative_test_record.csv).
Physical result fields stay unmeasured until someone performs and records the checks.

Next, change one requirement, such as supply voltage, and ask which calculations
and checks must change. A later physical build needs the specified equipment
and an independently checked build plan.

<a id="phd-career"></a>

## PhD and Career: a handbook and milestone discussion

Choose the **PhD and Career System** through **Help me choose**. PhD Companion
helps with degree planning and advisor conversations using the circumstances
and sources you supply.

Copy the [PhD and Career inputs](tutorial_examples/phd_career/inputs). Read the
[project map](tutorial_examples/phd_career/inputs/moc_degree_path.md),
[invented handbook](tutorial_examples/phd_career/inputs/fictional_handbook.md),
[student's circumstances](tutorial_examples/phd_career/inputs/student_context.md)
and [progress evidence](tutorial_examples/phd_career/inputs/completion_evidence.md).
The policies and student are fictional.

> What should this student do next?

Choose one proposed milestone and trace it back to the handbook and progress
record. Does the student have evidence of completion, or only an intention?
Check that requirements, suggested targets and unknown dates remain distinct.
Then discuss which questions would be useful for the advisor meeting.

Compare your answer with the [illustrative milestone plan](tutorial_examples/phd_career/illustrative_outputs/illustrative_milestone_plan.md)
and [advisor agenda](tutorial_examples/phd_career/illustrative_outputs/illustrative_advisor_agenda.md).
Notice how the agenda turns missing information into useful questions.

Next, add a fictional approval record to your copy and ask which statuses change.
For your own degree, bring the applicable handbook and documented progress,
and verify real requirements with the responsible program.
