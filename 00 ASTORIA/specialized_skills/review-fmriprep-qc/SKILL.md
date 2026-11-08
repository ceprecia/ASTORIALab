---
name: review-fmriprep-qc
description: >-
  Guides collaborative review of existing fMRIPrep reports and images, explains
  visual examples, and documents evidence-linked observations and user QC
  decisions. Use after preprocessing or to resume a review; return reviewed
  scope and unresolved findings to the invoking companion. Triggers: review my
  fmriprep reports, explain this fmriprep panel, resume my fmriprep review.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: analysis
  modality: fmri
  dependencies: ""
  requires: Existing fMRIPrep reports and supporting figures; an available browser or image viewer for visual inspection
  gates: User QC decisions and saving review records
  created: "2026-10-29"
  updated: "2026-11-01"
---

# Review fMRIPrep QC

Read each report with the user, inspect its images, and keep a useful review record.

## Purpose

- Guide review of existing fMRIPrep HTML reports, supporting figures and selected image views for one participant or an explicitly selected set of runs.
- Explain panels with source-backed examples, discuss actual evidence and its analysis relevance, and document observations and user decisions separately.
- Resume unfinished reviews and maintain one project-owned review table when requested.
- Own report navigation, image inspection, artifact discussion and review documentation. Method specification belongs to `fmri-preprocessing-pipeline-guide`; pipeline execution belongs to `fmriprep`.

## Inputs

- Current project instructions, relevant MOC context and technical notes, following `me.md`.
- Selected derivative root, participant/run scope, processing version and HTML report with supporting figures. Resolve these from supplied context before asking the user to repeat them.
- Acquisition context needed for the current panel: expected coverage, task or resting state, available distortion correction and intended output representations.
- Existing QC criteria and intended analyses when established. Unsettled ROI definitions or exclusion rules do not prevent report reading; acceptance decisions can remain pending.
- Available browser/image tools and, when needed, an existing volume viewer or supported way to render selected image planes.
- Existing review record and resume point, plus authorization to maintain them when saving is requested.

If reports are still transferring or cannot be viewed, teach from the reference examples and identify the missing evidence. Do not open unrequested participants to fill gaps.

## Steps

### 1. Bind the review to the current project

1. Identify the selected participants/runs, derivative root and fMRIPrep version. Preserve the invoking companion and return point. A named invocation begins at this bounded scope without another intake. The owning chat follows the research session core in `me.md`; a delegated review worker reads this skill and its assigned project/source material without reloading the parent pair unless its assignment requires those instructions.
2. Read only the context and files needed for this scope. Start with report/figure inventory rather than loading the imaging dataset into memory.
3. Match the project, derivative root, processing version, participant/run and exact evidence revision before resuming at the saved panel. Use a verified immutable run or manifest that identifies the actual report and each supporting artifact used for the decision, or compare their recorded and current content hashes. Matching paths or software versions alone cannot establish identity. If any relevant artifact changed or its identity is unverified, keep the prior checkpoint as history, inspect the affected evidence anew and leave its current decision pending. Ask only about consequential missing information.
4. Briefly state the current inspection scope and proceed. Do not add another route-selection menu or repeated permission questions for routine inspection within that scope.

### 2. Open the report and check figure availability

1. Open the participant HTML using available tools or guide the user to open it locally. Preserve its relative relationship to the participant's `figures/` directory.
2. Check the summary, version, listed acquisitions and error information. Keep software completion separate from image assessment.
3. If a panel is blank, inspect its linked figure path and transfer status before interpreting the MRI. Use the direct SVG/image link when useful. Mark unavailable panels `not_inspected` and continue with available evidence.
4. Follow the actual report's legends, labels and processing choices; colors and layouts vary across versions.

### 3. Explain and inspect each relevant panel

Read `./references/report_review.md` for the panel sequence and example links. Open only the example relevant to the current question.

For each panel:

1. Explain what it shows and the anatomical landmarks, boundaries or signal features to compare.
2. Show or link one relevant example when useful, naming its source, version and acquisition differences.
3. Inspect the actual rendered panel, animation or selected image view. HTML captions, filenames, metrics and a successful render command do not substitute for viewing image pixels.
4. Describe specific observations and their locations, then an interpretation and remaining uncertainty. Identify participant, run and figure or image view.
5. Discuss implications for the proposed ROI, volume or surface analysis. Offer a preliminary assessment or further check while preserving the user's acceptance decision separately.

Review anatomy once per participant, then each selected functional run. Follow the user's preferred pace, including requests to pause or move on. Do not impose quizzes or approval after every panel. A single-panel request needs only that panel's context, not a full preprocessing intake.

### 4. Investigate ambiguous findings with focused views

- Examine additional sagittal, coronal or axial views when a montage is insufficient. Use selected source/derivative views through available tools within the agreed scope; preserve their identity and space.
- Distinguish expected EPI/T1 contrast differences and limited field of view from displaced anatomy, dropout or failed processing.
- Assess alignment against the acquired signal and declared acquisition limits. Establish support for the intended analysis from inspected inputs; an output grid alone does not establish measured signal.
- Compare motion traces, FD/DVARS and carpet patterns at matching times. A band or metric alone does not identify its cause or establish exclusion. Existing confound tables can support inspection; fitting nuisance models is a different task.
- Inspect surface boundaries for surface/CIFTI use. Volumetric registration alone does not establish surface quality.
- If evidence or tooling is insufficient, retain the question as unresolved. Do not infer a visual verdict from text-only access or guess missing acquisition details.

### 5. Discuss and document the review

Discuss observations in the task's selected form, then under the recipient's applicable reporting policy if the form is open. When neither specifies a form, use a compact evidence-linked summary. Use the following row schema for an authorized QC table.

| participant | run | observation | evidence | review_status | decision |
|---|---|---|---|---|---|

- Preserve labels as strings. Use an empty run for participant-level anatomy; functional entries identify the run. Add a separate issue row only when it needs distinct evidence or a decision.
- In `evidence`, identify the panel, verified report and existing figure/image paths, relevant plane/slice or time interval, and evidence revision for the artifacts supporting the observation. Record the verified run/manifest identifier or the relevant artifact hashes. Mark identity unverified when it cannot be established. Link the existing figures.
- Use `not_inspected`, `partial`, `reviewed_no_concern_in_views`, or `needs_discussion` for `review_status`. These describe inspected evidence rather than acceptance.
- Leave `decision` empty until the user decides. Preserve their adopted accept, accept-with-limitations, exclude or defer decision. Explain recommendations without silently converting them into decisions or universal thresholds.
- Keep image-QC findings separate from behavioral trial flags. Reviewing a report does not change behavioral labels, raw data, BIDS, derivatives or analysis inclusion lists.

For an authorized QC record, use the selected destination, then the verified project policy when no destination is selected. When neither resolves placement, reuse the verified canonical review table if it fits the task. Ask once if a required destination remains unresolved. Keep a single maintained record and verify its actual path.

Once maintaining the record is authorized, update it within that scope without asking about each row. Match participant, run, panel and verified evidence revision before updating an existing row. Preserve the prior observation, user decision and unreviewed scope as history when the evidence revision differs or cannot be verified. Record affected current evidence separately in the same QC table and leave its decision empty until the user decides for that evidence. Record the review root, processing version, verified evidence revision and short resume point only when the checkpoint edit is authorized. Use the selected verified checkpoint location, then the applicable project continuity policy. When neither specifies a location, reuse the verified existing review checkpoint in the owning note if it fits the task. Preserve the approved resume state and keep one checkpoint.

### 6. Finish the bounded review and return

Report the participants/runs and panels actually inspected, significant findings, user decisions, missing evidence and exact resume point. Distinguish partial review from completion.

Return to the invoking companion. Proposed repair, rerun, denoising changes or downstream modeling are next tasks, not automatic continuations of image review.

## Outputs

- Return panel explanations, relevant examples, evidence-linked observations, unresolved issues and a compact summary in the current task's requested form or under the recipient's existing reporting policy.
- Save one QC table within the authorized record scope. Update the agreed MOC resume point only within the authorized continuity scope. For teaching-only requests, explain the evidence in the selected form.
- Save reusable instructions only within the authorized note scope. Use the selected verified destination, then the applicable project policy. If neither specifies placement, reuse the verified existing methods note when it fits the task. A curated protocol rewrite stays with `write-protocol`. Separately requested progress entries stay with the capture skills.
- No automatic screenshot collection, duplicate reports, per-panel notes or second hub. Clean expendable rendering scratch after inspection.

## Boundaries

- Review existing outputs; preprocessing, denoising, downstream analysis, automated exclusion and corrective edits require separately scoped work.
- The user owns QC acceptance, exclusion criteria and corrective processing. Continue observation while unsettled scientific decisions remain pending.
- Never label a panel visually reviewed without inspecting its rendered image, or an entire participant reviewed from one run or a few sampled slices.
- Verify acquisition limits, coordinate spaces and processing provenance against the selected study. Do not import another study's cutoffs, expected extent or repair commands.
- Keep reference examples distinct from study data. Follow source, print and file conventions in `me.md` without duplicating them here.

## Handoffs

- A requested writing-support consult returns the exact reviewed scope, evidence locations/version, observations, user decisions and unreviewed or unresolved scope to translate-specialist-methods or the content writer through the existing coordinator/return owner. Use `00 ASTORIA/skills/writing-coordinator/references/cross_system_handoff.md`. Check draft QC statements against the existing review record; do not expand a sample of viewed panels into cohort-wide acceptance or start unrequested image review to complete the prose.
- The invoking companion remains the visible owner. Return the inspected scope, findings, decisions and resume point to it.
- `fmri-coordinator` can identify this skill as the next owner once preprocessing reports are available.
- `fmri-preprocessing-pipeline-guide` owns unresolved method/QC-criteria changes; `fmriprep` owns approved execution or reruns. Do not load them merely to explain an ordinary panel.
- `write-protocol` owns requested durable instructions; `capture-progress` owns a separately requested Research Log capture. Neither is called automatically after review.

## Checks

- One-panel explanation uses one relevant example and the supplied scope without a full method intake.
- Missing SVGs are unavailable evidence, not failed registration or accepted QC. Text-only access never becomes a visual pass.
- Expected cropping is distinguished from poor alignment, with coverage consequences tied to the proposed analysis.
- The older official sample is identified by its own version, not treated as a perfect scan or a source of current settings.
- Motion/carpet concerns produce observations and discussion, not automatic censoring or exclusion.
- Resume binds the correct project, version, participant, run, panel and verified evidence revision. Repeated saves of the same verified evidence do not duplicate rows. Changed or unverified evidence leaves the current decision pending, with earlier decisions preserved as history.
- User decisions remain separate from observations and inspection status. Setup, resources and skill-creation requests do not start study-data review.

## References

- DartBrains. (n.d.). *Preprocessing*. https://dartbrains.org/content/Preprocessing.html
- Jahn, A. (n.d.). *fMRIPrep tutorial #3: Examining the preprocessed data*. Andy's Brain Book. https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_3_ExaminingPreprocData.html
- NiPreps. (n.d.). *Outputs of fMRIPrep* (Version 25.2.7). https://fmriprep.org/en/25.2.7/outputs.html
- Adapted from: Provins, C., MacNicol, E., Seeley, S. H., Hagmann, P., & Esteban, O. (2023). Quality control in functional MRI studies with MRIQC and fMRIPrep. *Frontiers in Neuroimaging, 1*, 1073734. https://doi.org/10.3389/fnimg.2022.1073734 (CC BY)
- Teves, J. B., Gonzalez-Castillo, J., Holness, M., Spurney, M., Bandettini, P. A., & Handwerker, D. A. (2023). The art and science of using quality control to understand and improve fMRI data. *Frontiers in Neuroscience, 17*, 1100544. https://doi.org/10.3389/fnins.2023.1100544
