# Skill vocabulary

The controlled values that every skill's `metadata` block may use, and the
system headings the Skill Map builder prints. Scripts read the YAML block
below; humans read this page. Change a value here first, then run
`skills-janitor/scripts/lint.py` to find every skill that needs to follow.

```yaml
levels:
  companion: Person-facing entry point that owns the session and routes. Named <name>-companion.
  coordinator: Finds and loads the right specialized skill. Makes no scientific decision. Named <name>-coordinator.
  skill: One bounded job.
  profile: Rule-only reference loaded by other skills. Never invoked directly.

trigger_counts:
  companion: [3, 5]
  coordinator: [0, 5]
  skill: [1, 5]
  profile: [0, 0]

description_max_chars: 1000

# Body sections. Canonical H2s in this order, only the ones a skill needs; a
# domain section (a catalog, a route table, a facts table) may keep its own H2.
# The lint warns when a retired skeleton name comes back and errors on footers.
sections:
  canonical: [Purpose, Inputs, Steps, Outputs, Boundaries, Handoffs, Checks, References]
  retired: [Scope, When to use, When not to use, Activation, Activation and scope, Scope rule,
    Inputs to gather, Required intake, Required inputs, Workflow, Output, Output contract,
    Saving and external actions, Rules, Edge cases, Rules and edge cases, Rules and stop conditions,
    Deterministic stops, Limits, Method rules, Human-control contract, Authority and evidence rules,
    Canonical ownership, Boundaries and handoffs, Forward tests, Health]

# full: name, tags, first sentence, triggers (about 360 characters per entry).
# compact: name, tags, triggers only (about 120 characters per entry); use it
# when a small-context model must read the Part 4 catalog.
catalog_style: full

# The five parts of scientific inquiry. Numbers, not stages: a project moves
# between them in any order.
parts:
  "1": Help me scout the field
  "2": Help me challenge my question
  "3": Help me stress-test my hypothesis and design
  "4": Help me analyze the data
  "5": Help me finish, share, and publish research

part_coordinators:
  "1": scout-coordinator
  "2": challenge-coordinator
  "3": stress-test-coordinator
  "4": analysis-coordinator
  "5": research-output-coordinator

# Nonresearch systems with generated bounded-skill catalogs.
system_coordinators:
  Engineering System: engineering-coordinator
  PhD and Career System: phd-coordinator
  Capture and Writing Helpers: writing-coordinator

# Shared helpers have two durable sections. New helper skills join one section here.
system_sections:
  Capture and Writing Helpers:
    Capture, prepare, and notetake:
      - capture-progress
      - chat-handoff
      - quick-capture
      - redactor
      - summarize
      - write-protocol
    Writing assistance:
      - writing-companion
      - writing-coordinator
      - organize-writing-project
      - plan-writing-argument
      - develop-writing-evidence
      - keep-writing-structure
      - verify-writing-citations
      - check-writing-substance
      - check-writing-cerl
      - check-research-reporting
      - translate-specialist-methods
      - integrate-writing
      - write-title
      - write-abstract
      - write-introduction
      - write-methods
      - write-results
      - write-discussion
      - write-conclusion
      - write-figure-table-text
      - write-section

system_catalog_sections:
  Capture and Writing Helpers: Writing assistance

families:
  part-coordinator: Part coordinator
  literature: Literature discovery and synthesis
  critique: Question, claim, and study critique
  hypothesis: Hypothesis and prediction stress testing
  design: Experimental, paradigm, and assessment design
  power: Power and sample size
  acquisition: Acquisition standards and conversion
  datasets: Public datasets
  method-guide: Method guides
  modality-coordinator: Modality coordinators
  software-adapter: Software adapters
  model-adapter: Model adapters
  computing: Research computing
  analysis: Analysis procedures
  writing: Funding and application support
  support: Research support

modalities: [fmri, smri, dwi, asl, pet, meg, eeg, ephys, calcium, behavior, genomics, pathology, multimodal, any]

populations: [autism, developmental, clinical, general, aging]

systems:
  ASTORIA System Builder:
    banner: "00 ASTORIA/assets/banner_system_builder.png"
    emoji: "🏗️"
    tagline: Set up and maintain the AI system
    note: true
  Research Assistant System:
    banner: "00 ASTORIA/assets/banner_system_research.png"
    emoji: "🧭"
    tagline: Coordinate bounded capabilities across five parts of scientific inquiry, 1 to 5
    note: true
  PhD and Career System:
    banner: "00 ASTORIA/assets/banner_system_phd.png"
    emoji: "🎓"
    tagline: Navigate degree requirements, mentoring, opportunities and career development
    note: true
  Productivity and Study System:
    banner: "00 ASTORIA/assets/banner_system_study.png"
    emoji: "🤹"
    tagline: Map, study, and plan progress
    note: true
  Teaching Assistant System:
    banner: "00 ASTORIA/assets/banner_system_teaching.png"
    emoji: "🍎"
    tagline: Prepare, teach, assess, and manage college courses
    note: true
  Janitor System:
    banner: "00 ASTORIA/assets/banner_system_janitor.png"
    emoji: "🧹"
    tagline: Maintain the vault and the AI system
    note: true
  Capture and Writing Helpers:
    banner: "00 ASTORIA/assets/banner_system_capture.png"
    emoji: "🗒️"
    tagline: Capture and prepare material, then develop and review writing
    note: false
  Engineering System:
    banner: "00 ASTORIA/assets/banner_system_engineering.png"
    emoji: "⚙️"
    tagline: Build, verify, and operate research hardware and inspect shipped software
    note: true
  Writing Style References:
    banner: "00 ASTORIA/assets/banner_system_writing.png"
    emoji: "✍️"
    tagline: Rule-only references for writing tasks
    note: false

# Vault layout. Roles are fixed; the names are the user's. setup-my-vault
# applies renames here first, then skills-janitor/scripts/rename_roots.py
# cascades the path strings. lint.py flags any numbered root path in a skill
# that does not start with one of these names.
roots:
  system: "00 ASTORIA"
  inbox: "01 📥 Inbox"
  calendar: "02 📅 Calendar"
  projects: "03 🌱 Projects"
  areas: "04 🌿 Areas"
  resources: "05 🍃 Resources"
  archive: "06 🪴 Archive"

optional_roots: [inbox, calendar]

# Subfolders created at setup, relative to each root.
layout:
  system: [agent_notes, skills, systems, templates]
  calendar: [capture-logs, woop-captures]
  resources: ["📎 attachments", "📎 attachments/00_to_sort"]
  archive: [finished_projects, finished_areas]

# Layout reference. vault-builder/scripts/build_layout.py writes
# 00 ASTORIA/agent_notes/layout.md from these lists plus the folder tree.
# Unregistered Resources topics use a generic purpose. Other unregistered
# folders are reported; note types without an installed owner are skipped.

purposes:
  "00 ASTORIA": "The AI system: skills, systems, templates, shared artwork, the Skill Map and agent notes. Nothing else lives here."
  "00 ASTORIA/assets": "Approved current ASTORIA artwork shared by system notes and the public starter. Stable filenames identify the product banner, whole-system architecture, research diagram, system icons and system banners; drafts and private artwork are not shipped."
  "00 ASTORIA/agent_notes": "Agent reference and records: `layout.md`, `ai_log.md` (complete running history. Locate relevant entries by heading, date or keyword and read them in bounded chunks), and dated transcripts and summaries when this is their authorized destination."
  "00 ASTORIA/skills": "One folder per skill, `<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/`. Read the selected SKILL.md completely before running it."
  "00 ASTORIA/systems": "One human-facing note per workflow system."
  "00 ASTORIA/templates": "Reusable note templates. In Obsidian, select this folder in the core Templates plugin if you choose to use it."
  "01 📥 Inbox": "The user's quick jots. In Obsidian, you can choose this folder as the new-note default. The inbox is human-owned. The AI reads it only when asked to process it and leaves writing to the user."
  "02 📅 Calendar": "Time-indexed material: capture logs and WOOP plans."
  "02 📅 Calendar/capture-logs": "One file per capture day in `YY_Q#` quarter folders, written by capture-progress and quick-capture; use-based, no daily routine."
  "02 📅 Calendar/woop-captures": "Dated WOOP plans and updates; the newest applicable date is the current plan."
  "03 🌱 Projects": "Active work with a defined outcome, an owning MOC and AGENTS.md. Use its local files folder or documented external workspace for working material. Preserve established operational layouts."
  "04 🌿 Areas": "Ongoing responsibilities with an owning MOC and AGENTS.md. Use a local files folder or a documented external workspace as the working destination."
  "05 🍃 Resources": "Reusable reference material in recipient-chosen collections. Keep related files together and use the chosen attachment intake for items without an owner."
  "05 🍃 Resources/📎 attachments": "Attachment intake and shared assets when the recipient uses them."
  "05 🍃 Resources/📎 attachments/00_to_sort": "Temporary intake for new attachments and material with no assigned owner."
  # Add recipient-selected collection purposes after confirming their content.
  "06 🪴 Archive": "Inactive projects, areas and resources kept for future reference and provenance."
  "06 🪴 Archive/finished_projects": "Finished, inactive or parked projects and their MOCs; keep capture history."
  "06 🪴 Archive/finished_areas": "Areas that have ended."

note_types:
  - kind: Research project MOC
    location: "03 🌱 Projects/<project>/MOC <project>.md"
    template: Research Project Template.md
    owner: ""
  - kind: Other project MOC
    location: "03 🌱 Projects/<project>/MOC <project>.md"
    template: Projects Template.md
    owner: ""
  - kind: Engineering reverse engineering MOC
    location: "03 🌱 Projects/<project>/MOC <project>.md"
    template: engineering_REA_template.md
    owner: ""
  - kind: Standalone reusable topic MOC, created only when authorized
    location: "Resolve Project, Area, or course ownership first and reuse its verified continuity note when applicable. For an authorized standalone topic, use the selected eligible location and name, then verified policy. Its fallback is <resources root>/<owning collection>/<Topic>.md. Use emoji when selected or configured."
    template: Base Template.md
    owner: study-planner
  - kind: Class note (a course taken or audited)
    location: "Use the verified selected course folder, then the course owner’s verified placement. Local fallback: <areas root>/<chosen school area>/files/<existing course folder>/<Course code> <Course title>.md"
    template: Class Template.md
    owner: class-builder
  - kind: Teaching MOC
    location: "Verified eligible selected Teaching MOC path, then applicable verified policy. Fallback: <areas root>/<chosen teaching area>/<Area> MOC.md."
    template: Teaching MOC Template.md
    owner: teaching-assistant-builder
  - kind: Teaching course note (an instructor, TA, or grader offering)
    location: "Use the verified eligible selected offering folder, then the teaching owner’s verified working destination. Keep the note and supporting files together. Local fallback: <areas root>/<chosen teaching area>/files/<existing offering folder>/<Role and course title with term>.md. Reuse a documented external workspace when it applies."
    template: Teaching Class Template.md
    owner: teaching-assistant-builder
  - kind: Project capture, structured or quick
    location: "Inline in the owning project MOC's single Research Log, with unique full-date (`YYYY-MM-DD`) entry headings. Follow the selected or verified log order and preserve existing headings. Use newest-first as the fallback only for a new log whose order remains open."
    template: ""
    owner: capture-progress, quick-capture
  - kind: Capture log (calendar index, and captures without a project owner)
    location: "02 📅 Calendar/capture-logs/YY_Q#/YYYY-MM-DD_capture_log.md"
    template: ""
    owner: capture-progress, quick-capture
  - kind: WOOP plan or major update
    location: "02 📅 Calendar/woop-captures/YYYY-MM-DD_<season_or_scope>_woop_plan.md"
    template: ""
    owner: woop-skill
  - kind: Conversation transcript
    location: "Authorized destination and verified owner policy. Resolve an ownerless user record's location before saving. Use `00 ASTORIA/agent_notes/YYYY-MM-DD_transcript_<description>.md` only for authorized system or agent records that belong there."
    template: ""
    owner: summarize
  - kind: Conversation summary
    location: "Authorized destination and verified owner policy. Resolve an ownerless user record's location before saving. Use `00 ASTORIA/agent_notes/YYYY-MM-DD_summary_<description>.md` only for authorized system or agent records that belong there."
    template: ""
    owner: summarize
  - kind: Any other regular note
    location: "verified selected destination or applicable verified policy. Working material belongs in the owner files folder or documented external workspace. Reusable reference uses the appropriate Resources collection. Skill and system work stays in `00 ASTORIA/`."
    template: Base Template.md
    owner: ""

template_purposes:
  "code_template.md": "Shared prolog and readable body scaffold for new authored source files."
  "Base Template.md": "Universal starter with base frontmatter only; the fallback when no other template fits."
  "Class Template.md": "A course the user takes or audits."
  "Teaching MOC Template.md": "The single teaching-area MOC, with current-term navigation and a teaching timeline."
  "Teaching Class Template.md": "One college teaching offering for an instructor, TA, or grader, with approved sources, responsibilities, and course resources."
  "Projects Template.md": "A nonresearch project MOC with headings and navigation in the selected or verified form. Its illustrated opening callouts are the fallback when navigation is open."
  "Research Project Template.md": "A research project MOC; omit unused sections."
  "engineering_REA_template.md": "A flexible engineering and reverse engineering MOC: Start Here, an evidence-led workbench, Research Log, and AI Notes last."
  "agents_draft_template.md": "The few-line `AGENTS.md` a starter vault ships with; replaced at the end of setup."
  "agents_loader_template.md": "The full vault-root `AGENTS.md` loader written by setup-my-vault."
  "global_codex_agents_template.md": "Source for a short `AGENTS.md` in an external workspace that points at `me.md`."
  "ai_log_template.md": "The first `00 ASTORIA/agent_notes/ai_log.md`: the selective-reading and history-preservation callout and one setup entry; written by setup-my-vault."

layout_rules:
  - "Each Project or Area has one owning MOC and one AGENTS.md. Use a local files folder or documented external workspace for working material. Report genuinely missing entries and separately report workspace availability. Add a MOC link only within authorized note-edit scope."
  - "Preserve established project operational layouts and complete packages."
  - "Resources is a reference library. Collection names and grouping come from the recipient and their content. Preserve useful existing organization during routine filing."
  - "Give each file one canonical home. Keep related files together and link to reusable references without duplication."
  - "Folder tidying changes structure and active links, embeds and path tokens. Preserve MOC prose, headings, decisions, log narratives, and scientific logic."
  - "Keep unclear attachments in the configured intake. Preserve unlinked files. Use the verified selected destination or applicable owner policy for authorized saves."
  - "`01 📥 Inbox/` is human-owned: never a destination for AI output; read it only when asked to process it."
  - "For ordinary new notes, use the naming and date choices approved for the current task. When the request leaves them open, follow the verified applicable project or recipient convention, including choices recorded in `me.md`. If no applicable convention was chosen, use snake_case and `YYYY-MM-DD` for filename dates. Preserve fixed filenames, date formats and exact heading anchors required by existing technical records and workflows."
  - "Verify that a link target exists before writing the link, and verify the destination folder before placing a file. When moving or renaming content, update and verify the affected links, embeds, and file-path references in the same task; unclear existing files stay in intake."
  - "Dotfolders are out of scope; `.agents/skills/` and `.claude/skills/` hold only the skill mounts."
  - "Keep temporary build and test material outside the vault when practical. Use a verified in-vault staging location only when the recipient explicitly configures or authorizes it for that purpose. Keep Resources intake separate from scratch and build storage."

# Starter vault settings and its specialized-skills catalog
# (install_specialized.py reads the catalog index).
starter:
  portable_links: true
  catalog_index: [abcd-skill, abide-skill, adhd200-skill, adni-skill, aeon, aibl-skill, alternative-uses-task-designer, anndata, aomic-skill, arboreto, asl-coordinator, bayesian-cognitive-model-builder, bids, bids-organizer, biopython, bnt, bold5000-skill, brain-connectivity-modeler, bulk-rnaseq, calcium-imaging-analysis-guide, camcan-skill, cobre-skill, cognitive-paradigm-design, cogsci-power-analysis, cogsci-statistics, conn-tool, dask, dcm2nii, deeplabcut, deeptools, dictlearning, dipy-tool, divergent-thinking-scoring, dmt-har-med-skill, drift-diffusion-model, dwi-coordinator, eeg-analysis-guide, eeg-coordinator, eeg-paradigm-designer, eeg-preprocessing-pipeline-guide, erp-analysis, evidence-accumulation-selector, experiment-controller, fmri-coordinator, fmri-glm-analysis-guide, fmri-preprocessing-pipeline-guide, fmri-task-design-guide, fmriprep, freesurfer-tool, fsl-tool, geniml, glm, gtars, harmonization-tool, hbn-skill, hcpa-skill, hcpd-skill, hcpep-skill, hcppipeline-tool, hcpya-skill, hierarchical, histolab, ica, infant-looking-time-designer, ixi-skill, kmeans, lesion-symptom-mapping-guide, matlab, meg-coordinator, mnd-skill, mne-eeg-tool, mne-python-guide, mschallenge-skill, netneurotools-guide, networkx, neural-decoding-analysis, neural-population-analysis-guide, neuroimaging-power-guide, neuroimaging-sample-size-calculator, neurokit2, neuropixels-spikeinterface, neuropsych-battery-selector, neurostorm, nibabel-skill, nifd-skill, nilearn-tool, nsd-skill, oasis-skill, pathml, pathway-enrichment, pet-coordinator, pnc-skill, polars, polars-bio, ppmi-skill, pydeseq2, pydicom, pymc, pysam, pytorch-lightning, qsiprep-tool, r-research-computing, reading-time-analysis, rest-mneta-mdd-skill, review-fmriprep-qc, run-models, scanpy, scikit-learn, scvelo, scvi-tools, seed-iv-skill, seed-vig-skill, self-paced-reading-designer, sentence-stimulus-norming, signal-detection-analysis, smri-coordinator, spacenet, statsmodels, svm, sympy, tcp-skill, tiledbvcf, tom-task-selector, torch-geometric, transformers, ucla-cnp-skill, umap-learn, visual-search-array-generator, wmh-segmentation, zarr-python]
  catalog_folder: specialized_skills
  specialized_families: [modality-coordinator, software-adapter, model-adapter, datasets, acquisition, computing, method-guide]
  imaging_modalities: [fmri, smri, dwi, asl, pet, meg, eeg]

companion_order: [research-companion, phd-companion, study-companion, teaching-companion, engineering-companion, writing-companion]

system_order:
  - ASTORIA System Builder
  - Writing Style References
  - Productivity and Study System
  - Teaching Assistant System
  - Capture and Writing Helpers
  - Janitor System
  - Engineering System
  - PhD and Career System
  - Research Assistant System
```
