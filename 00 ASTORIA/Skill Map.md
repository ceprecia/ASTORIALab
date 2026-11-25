---
related:
  - "[[me]]"
created: 2026-01-01
updated: 2026-11-02
astoria_version: "1.3.1"
---
This is the active skill registry for the user's AI system. Every skill is a folder, `00 ASTORIA/skills/<name>/SKILL.md`, on the Agent Skills standard; the registry below is generated from the skills' frontmatter by `00 ASTORIA/skills/skills-janitor/scripts/build_views.py` and is never edited by hand. The full sortable table is the Base in [Skills](Skills.md).

> [!info] `me` (created during setup) | **[Skill Map](Skill%20Map.md)** | `00 ASTORIA/agent_notes/`

- `me` (created during setup) - `/me.md` - AI's briefing on who the user is and how to interact with the user.
- [Skill Map](Skill%20Map.md) - `/00 ASTORIA/Skill Map` - Active skills AI can use on the user's behalf.
- `00 ASTORIA/agent_notes/` - `layout.md`, where every kind of file goes; `ai_log.md`, the AI's running log.

# 🧭 Start Here

> [!abstract] 🧠 How the skills are organized
> Five components. `me.md` is read first every session; a companion owns the session and routes; a coordinator finds the skill; the skill does one bounded job; the user owns every scientific decision.
>
> | Component | Purpose |
> | --- | --- |
> | **Personal context** | Describes your preferences, goals, and working environment (`me.md`). |
> | **Companions** | The main skills you interact with for broader guidance and ongoing work. |
> | **Coordinators** | Help companions identify the appropriate specialized skills for a task. |
> | **Specialized skills** | Provide focused instructions for particular research methods, tools, or activities. |
> | **Writing profiles** | Guide expression and style during applicable writing tasks. |

<!-- systems:start -->
> [!example] 🗺️ Systems
> - 🏗️ [ASTORIA System Builder](#-astoria-system-builder): Set up and maintain the AI system.
> - ✍️ [Writing System (shared helpers)](#-writing-system-shared-helpers): Develop, review, capture and prepare writing through the right bounded capability.
> - 🧹 [Janitor System](#-janitor-system): Maintain the vault and the AI system.
> - 🧭 [Research Assistant System](#-research-assistant-system): Coordinate bounded capabilities across five parts of scientific inquiry, 1 to 5.
<!-- systems:end -->

# Skills grouped by System

<!-- registry:start -->
## 🏗️ ASTORIA System Builder

![ASTORIA System Builder](assets/banner_system_builder.png)

[ASTORIA System Builder](systems/ASTORIA%20System%20Builder.md): Set up and maintain the AI system.
- [astoria-updater](skills/astoria-updater/SKILL.md): Updates an existing ASTORIA vault and follows up with two janitor audits and an update recheck. Triggers: update my astoria, upgrade my astoria vault.
- [me-builder](skills/me-builder/SKILL.md): Creates or refreshes the user's root me.md. Triggers: build my me.md, refresh my me.md, update my preferences in me.md, who am I according to my vault.
- [paper-to-skill](skills/paper-to-skill/SKILL.md): Extracts source-grounded reusable content from one user-supplied paper or a small bounded paper set into a chat-only evidence pack for Skill Builder. Triggers: skill from this paper, extract a skill from these papers, turn this paper into a skill.
- [repo-to-skill](skills/repo-to-skill/SKILL.md): Extracts source-grounded reusable content from one exact repository state into a chat-only evidence pack for one candidate skill. Triggers: skill from this repo, extract a skill from this codebase, turn this repository into a skill.
- [setup-my-vault](skills/setup-my-vault/SKILL.md): Starts first-time setup or routes an existing ASTORIA vault to the updater. Triggers: set up my vault, get started with this vault, continue my setup, start the vault setup.
- [skill-builder](skills/skill-builder/SKILL.md): Creates one new skill folder in `00 ASTORIA/skills/<name>/` with a standard SKILL.md, the required frontmatter, a description under 1,000 characters with at most five triggers, and optional references, scripts, and assets, then regenerates the Skill Map and coordinator catalogs. Triggers: make a skill, create a new skill, draft a skill for this workflow, turn this into a skill, install a ready-made skill.
- [skill-mount](skills/skill-mount/SKILL.md): Optionally mounts the vault's skills where an agent platform looks for them, keeping one copy in `00 ASTORIA/skills`. Triggers: mount my skills, remount the skills, make my skills show up in Codex, register my skills for Claude Science.
- [vault-builder](skills/vault-builder/SKILL.md): Builds or refreshes the layout reference `00 ASTORIA/agent_notes/layout.md`, the one page an agent checks before placing, naming, or moving a file. Triggers: build my layout reference, refresh the layout, map my folders for AI, map my templates for AI.

---

<a name="-writing-system"></a>

## ✍️ Writing System (shared helpers)

Only selected skills and required shared helpers are installed in this group. The full system remains an optional setup choice.

![Writing System](assets/banner_system_writing.png)

[Writing System](systems/Writing%20System.md): Develop, review, capture and prepare writing through the right bounded capability.

### Companion and coordination
- [writing-companion](skills/writing-companion/SKILL.md) (companion): Leads the Writing System and coordinates sustained writing around the author’s purpose, evidence, audience and selected structure. Triggers: coordinate my writing, assemble my writing team, help develop this document.
- [writing-coordinator](skills/writing-coordinator/SKILL.md) (coordinator): Internally assigns, collects and integrates bounded writing specialists and independent reviews while preserving the invoking companion and technical owners.

### Capture, prepare, and notetake

### Writing assistance
- [check-research-reporting](skills/check-research-reporting/SKILL.md): Audits a bounded research document against the applicable current reporting guideline and identifies missing or ambiguous disclosures. Triggers: audit research reporting completeness, check required method disclosures.
- [write-figure-table-text](skills/write-figure-table-text/SKILL.md): Drafts or revises figure legends, table notes, and associated display text from the actual artifact and analysis definitions. Triggers: draft figure captions, write table notes.

### Writing style
- [writing-style-negative-ai](skills/writing-style-negative-ai/SKILL.md) (profile): Optional editorial review for a recipient-selected audience, purpose and style specification.
- [writing-style-positive-scientific](skills/writing-style-positive-scientific/SKILL.md) (profile): Passive rule reference for precise, readable, construct-faithful scientific prose.

---
## 🧹 Janitor System

![Janitor System](assets/banner_system_janitor.png)

[Janitor System](systems/Janitor%20System.md): Maintain the vault and the AI system.
- [janitor-companion](skills/janitor-companion/SKILL.md) (companion): Leads vault cleanup and audit sessions, routes checks through Janitor Coordinator, and turns findings into specific fixes for the user to approve. Triggers: load the janitor system, fix my vault, clean up my vault.
- [janitor-coordinator](skills/janitor-coordinator/SKILL.md) (coordinator): Loads the installed specialists for a Janitor Companion request, coordinates evidence gathering and authorized repairs, and returns one owner per actionable fix.
- [agent-janitor](skills/agent-janitor/SKILL.md): Audits agent behavior, traces where context or instructions drift, and tests candidate fixes before proposing live changes. Triggers: audit agent drift, agents keep using old instructions, test an agent handoff.
- [bridge-maker](skills/bridge-maker/SKILL.md): Creates or updates a short project AGENTS.md pointing to the vault-root me.md. Triggers: make a project bridge, connect this project to obsidian, audit the project bridges, update this project AGENTS.md.
- [folder-janitor](skills/folder-janitor/SKILL.md): Organizes the requested content folders outside the AI system root using the owner’s verified structure and approved placements. Triggers: organize this folder, sort my resource intake, tidy my area folders, file these attachments.
- [propagate](skills/propagate/SKILL.md): Carries one change through everything that depends on it. Triggers: propagate this rename, I renamed this, propagate this convention, make the family match, update every reference to.
- [skills-janitor](skills/skills-janitor/SKILL.md): Audits every skill folder in `00 ASTORIA/skills/` against the skill-builder schema and regenerates the views. Triggers: audit my skills, are my skills in sync, rebuild the skill map, check for trigger overlaps, skill drift.
- [vault-janitor](skills/vault-janitor/SKILL.md): Checks vault consistency: the layout reference against the folder tree and vocabulary, rules against me.md, active instructions for stale paths and wording, and wiki-links vault-wide. Triggers: audit the layout, are my folders and templates in sync, check for folder drift, check log preservation, clean up the agent notes.
- [verify-removal](skills/verify-removal/SKILL.md): Removes named local items directly and verifies app uninstalls on macOS, Windows, and Linux. Triggers: uninstall this Mac app, check for uninstall leftovers, verify an app is gone, delete these specific files.

---
## 🧭 Research Assistant System

![Research Assistant System](assets/banner_system_research.png)

[Research Assistant System](systems/Research%20Assistant%20System.md): Coordinate bounded capabilities across five parts of scientific inquiry, 1 to 5.

- [Companions and coordination](#companions-and-coordination)
- [1. Help me scout the field](#1-help-me-scout-the-field)
- [2. Help me challenge my question](#2-help-me-challenge-my-question)
- [3. Help me stress-test my hypothesis and design](#3-help-me-stress-test-my-hypothesis-and-design)
- [4. Help me analyze the data](#4-help-me-analyze-the-data)
- [5. Help me finish, share, and publish research](#5-help-me-finish-share-and-publish-research)

### Companions and coordination
The public research entry point and its internal research-coordinator. Research Companion stays the visible session owner; research-coordinator verifies bounded assignments through the five part coordinators below (1 to 5, in any order) or an exact named capability, dispatches the needed research workers, and returns their evidence to the companion. PhD and career support has its own system; shared services preserve the original owner and task scope.
- [research-companion](skills/research-companion/SKILL.md) (companion): Research companion across all five parts of inquiry, for strategic framing, option comparison, project triage, manuscript strategy and research-session startup, resume or status. Triggers: start a research session, resume this research project, where are we in this project, compare these research directions, critique my study strategy.
- [research-coordinator](skills/research-coordinator/SKILL.md) (coordinator; internal, no triggers): Dispatches bounded research work to exact skill-loaded workers and returns their evidence to Research Companion.

### 1. Help me scout the field
- [scout-coordinator](skills/scout-coordinator/SKILL.md) (part coordinator, read first): Part 1 coordinator, help me scout the field. Triggers: help me find papers on this, summarize what the literature says, what do we know about this topic.

#### Literature discovery and synthesis
- [first-principles-research](skills/first-principles-research/SKILL.md): Explores research questions, studies, and methods by reconstructing their first principles and mathematical structure. Triggers: reason through first principles, deconstruct this study mathematically, find cross-field mathematical connections, scan all ten frameworks, explore my research from fundamentals.
- [literature-synthesis](skills/literature-synthesis/SKILL.md): Builds one bounded critical theory synthesis from supplied sources or an explicitly approved literature search. Triggers: synthesize these papers, build a theory synthesis from these sources.
- [paper-search](skills/paper-search/SKILL.md): Runs one researcher-directed scholarly discovery task through a short Search Direction and one upfront approval, then searches the approved public, institutional, browser-assisted, and user-provided routes within a stated budget. Triggers: search the literature for, find papers on this topic.
- [research-summarizer](skills/research-summarizer/SKILL.md): Explains one or more bounded research papers through a separate source-verified seven-part summary for each paper, covering plain-language and expert explanations, statistical methods and results, key findings, strengths, weaknesses, and discussion questions. Triggers: summarize this paper, explain this study to me, what does this paper claim.

### 2. Help me challenge my question
- [challenge-coordinator](skills/challenge-coordinator/SKILL.md) (part coordinator, read first): Part 2 coordinator, help me challenge my question. Triggers: is my research question worth asking, brainstorm directions for this question, check this claim against the evidence, critique this study.

#### Question, claim, and study critique
- [research-critique](skills/research-critique/SKILL.md): Critiques one bounded research object through a rapid blind-spot scan, targeted critique, or full scientific critique. Triggers: critique this paper, find the blind spots in this design, full scientific critique.
- [research-literacy](skills/research-literacy/SKILL.md): Audits one explicit research claim and its directly linked subclaims against supplied and bounded verified evidence. Triggers: audit this claim against the evidence, does the evidence support this claim.
- [scientific-brainstorming](skills/scientific-brainstorming/SKILL.md): Runs bounded scientific divergence from a user-supplied seed, using ideation heuristics when useful. Triggers: brainstorm scientific directions, divergent ideas from this seed.

### 3. Help me stress-test my hypothesis and design
- [stress-test-coordinator](skills/stress-test-coordinator/SKILL.md) (part coordinator, read first): Part 3 coordinator, help me stress-test my hypothesis and design. Triggers: stress test my hypothesis, design my experiment, is my sample big enough, which dataset can support this study, set up my data in BIDS.

#### Hypothesis and prediction stress testing
- [prediction-stress-test](skills/prediction-stress-test/SKILL.md): Prospectively stress-tests one exact user-supplied or explicitly adopted hypothesis and one primary prediction for testability, discriminability, counterexamples, boundary conditions, outcome implications, and bounded novelty evidence. Triggers: is this prediction testable, stress test this prediction.

#### Experimental, paradigm, and assessment design
- [experimental-design](skills/experimental-design/SKILL.md): Compares prospective experimental-design structures for one bounded user-supplied research question, hypothesis, or prediction and constraint set. Triggers: compare experimental designs for this question, which design fits my hypothesis.
- [method-design](skills/method-design/SKILL.md): Compares and specifies prospective computational method architectures for one user-supplied scientific objective and approved evaluation boundary. Triggers: design a computational method for this objective, compare method architectures.

#### Power and sample size
- [statistical-power](skills/statistical-power/SKILL.md): Quantifies prospective sample-size, power, minimum-detectable-effect, and operating-characteristic scenarios for one approved design and analysis specification. Triggers: power analysis for this design, how many participants do I need.

### 4. Help me analyze the data
- [analysis-coordinator](skills/analysis-coordinator/SKILL.md) (part coordinator, read first): Part 4 coordinator, help me analyze the data. Triggers: analyze my data, which analysis method fits this, preprocess my imaging data, run this analysis in, help me pick a statistical model.

#### Analysis procedures
- [exploratory-data-analysis](skills/exploratory-data-analysis/SKILL.md): Performs one approval-gated descriptive inspection of a bounded research dataset and returns an inspectable Data Structure and Quality Record. Triggers: inspect this dataset descriptively, data quality and structure check.
- [statistical-analysis](skills/statistical-analysis/SKILL.md): Plans, executes, and verifies one approved statistical analysis through an already available and pinned implementation. Triggers: run this statistical analysis, execute the approved analysis plan.

### 5. Help me finish, share, and publish research
- [research-output-coordinator](skills/research-output-coordinator/SKILL.md) (part coordinator, read first): Routes bounded publication, research-output verification, reproducibility, releases, engagement, closeout and selected funding requirements. Triggers: write up my results, help me report this study, prepare my reproducibility statement, funding application help, finish and share this research.

#### Funding and application support
- [research-grant-advisor](skills/research-grant-advisor/SKILL.md): Advises on requirements, planning, budgeting, review and preparation of one user-selected research funding application, borrowing shared writers for prose. Triggers: review this grant proposal, help me plan a grant application, check the funding announcement requirements.

#### Research support
- [close-research-project](skills/close-research-project/SKILL.md): Prepares closeout, preservation and handover for one bounded research project, connecting outstanding obligations, authoritative materials, retention, access and responsibility. Triggers: prepare this research project handover, plan research project preservation.
- [coordinate-peer-review](skills/coordinate-peer-review/SKILL.md): Maps editor and reviewer requests to user decisions, required work, revised locations and responses for one manuscript decision. Triggers: map these reviewer requests, organize this resubmission response.
- [maintain-publication-record](skills/maintain-publication-record/SKILL.md): Checks proofs and publication details against authoritative versions and maintains identifiers, related-output links and documented corrections. Triggers: check these publication proofs, reconcile publication versions.
- [plan-publication](skills/plan-publication/SKILL.md): Compares publication venues and verifies the current requirements for one selected journal, article type and stage. Triggers: compare journals for this paper, check this journal's instructions.
- [plan-research-engagement](skills/plan-research-engagement/SKILL.md): Plans and evaluates dissemination or reciprocal community engagement around supported research findings, audience purposes, channels, timing and feedback. Triggers: plan dissemination of these findings, evaluate this research engagement.
- [prepare-publication-package](skills/prepare-publication-package/SKILL.md): Assembles the required files, declarations, metadata and availability statements for one selected publication stage. Triggers: assemble this journal submission, check these submission files.
- [prepare-research-release](skills/prepare-research-release/SKILL.md): Prepares one data, code or combined research release through repository selection, compendium assembly and deposit preparation modes. Triggers: assemble a research release, choose a repository for these materials.
- [review-figures-tables](skills/review-figures-tables/SKILL.md): Reviews finished research figures and tables for APA presentation, readability and unnecessary complexity, returning practical corrections to their builders. Triggers: check APA display formatting, review figure and table readability, simplify these research displays.
- [verify-computational-reproducibility](skills/verify-computational-reproducibility/SKILL.md): Tests whether specified research outputs regenerate from recorded inputs, code, configuration and environment through the existing technical owners. Triggers: test whether these results regenerate, reproduce these reported outputs.
- [verify-repository-release](skills/verify-repository-release/SKILL.md): Checks an exact repository release against the intended files, versions, identifiers, metadata, access settings and related-output links. Triggers: inspect this deposited research version, check repository release metadata.
- [verify-research-outputs](skills/verify-research-outputs/SKILL.md): Traces reported numbers, figures, tables and files to identified analysis outputs and provenance, identifying inconsistencies and version mismatches. Triggers: trace these reported results, check manuscript output consistency.
<!-- registry:end -->
