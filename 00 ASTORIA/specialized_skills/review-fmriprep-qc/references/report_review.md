# fMRIPrep report review reference

Use the report's own legends, processing version and acquisition context. The linked examples teach inspection; they do not supply acceptance thresholds for another study.

## 1. Open and navigate

1. Keep the HTML report and its linked figures in their expected relative locations. Moving the HTML alone can leave blank panels.
2. Open the report in an available browser. Inspect the linked SVG directly when a panel is too small or fails to appear. Where supported, hover over an alignment panel to alternate images.
3. Read Summary, version and error information first. Confirm the acquisitions and operations actually reported, including slice timing and distortion correction.
4. Review anatomy once per participant, followed by each selected functional run. Successful processing is separate from visual assessment.

Use these resources for orientation:

- [Official output reference, version 25.2.7](https://fmriprep.org/en/25.2.7/outputs.html): report organization and output descriptions. Use the matching version when reviewing another release.
- [Official interactive sample](https://fmriprep.org/en/25.2.7/_static/SampleReport/sample_report.html): the sample identifies itself as fMRIPrep **20.2.3**, with no slice timing or susceptibility distortion correction. The hosting URL does not identify its processing version. Treat it as a navigation example, not a certified perfect scan or a configuration to reproduce.
- [Andy's illustrated walkthrough and video](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_3_ExaminingPreprocData.html): opening the report, comparing alignment views and interpreting functional panels. Its layout reflects an older version.
- [DartBrains preprocessing guide](https://dartbrains.org/content/Preprocessing.html): explanations of masks, tissue segmentation, registration and spatial normalization. Use current fMRIPrep documentation for release-specific operations.

## 2. Inspect the panels

Follow the actual report's labels and legend. A panel absent because an operation was not performed is different from a linked figure that has not transferred.

| Panel or evidence | What to compare | A concern to investigate |
|---|---|---|
| Summary and errors | Participant, acquisitions, TR, output spaces and reported operations | Missing acquisitions, unexpected settings or incomplete report sections |
| T1 brain mask | Mask outline against the acquired anatomy | Acquired brain excluded or large nonbrain inclusions |
| Tissue segmentation | Gray matter, white matter and CSF labels against plausible tissue boundaries | Labels visibly displaced or compartments substantially mixed |
| Anatomical normalization | Alternate anatomy/template views; compare ventricles, corpus callosum and internal landmarks across planes | Systematic displacement or severe deformation; local sulcal variation needs context |
| FreeSurfer surfaces | White and pial boundaries against the cortex | Boundaries crossing tissues incorrectly or extending into nonbrain tissue |
| BOLD/anatomical alignment | Tissue edges and internal landmarks within the acquired slab | Shift, rotation or local mismatch; expect different contrast and lower EPI detail |
| Distortion correction, when available | Correction/reference views and anatomical correspondence | Remaining displacement, new mismatch or dropout needing closer inspection |
| Functional mask and CompCor regions | Measured brain coverage and plausible white matter/CSF compartments | Acquired tissue omitted or nuisance masks substantially entering relevant gray matter |
| Motion and BOLD summary/carpet | FD, DVARS, signal traces and carpet changes at matching times | Broad abrupt bands, repeated disturbances or persistent changes |
| ROI coverage in selected images | Measured signal, mask and intended ROI in compatible spaces | ROI partly outside acquisition or affected by dropout |

For a systematic example, use [Provins et al., section 2.4.3 and Table 3](https://www.frontiersin.org/journals/neuroimaging/articles/10.3389/fnimg.2022.1073734/full). The categories above adapt that inspection framework (CC BY). Its study-specific whole-brain criteria and exclusion rate are not rules for another dataset.

## 3. Choose one teaching example

Pick the example that answers the current question. Explain how its acquisition, software or analysis differs before applying the visual lesson.

| Question | Example and lesson |
|---|---|
| How do I compare alignment? | Andy's anatomical and functional animations illustrate checking internal landmarks. CSF can be bright in BOLD and dark in T1; compare locations and boundaries rather than equal brightness. |
| Could a montage hide a concern? | Provins et al., Figure 2, shows a CompCor-mask concern and dropout easier to identify in sagittal than axial views. Inspect another plane when the montage is ambiguous. |
| Does an artifact invalidate every analysis? | Provins et al., Figure 3, contrasts consequences of distortion, wrap-around and structural ringing for different analysis scopes. Tie consequences to the intended measurement. |
| What do motion and coverage problems look like? | [Teves et al., Figures 1–3](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1100544/full) illustrates motion artifacts and coverage/dropout differences. It uses AFNI; borrow the visual reasoning, not its pipeline or numerical rules. |
| What does the carpet show? | [MRIQC BOLD report documentation](https://mriqc.readthedocs.io/en/latest/reports/bold.html) explains voxel signals across time, tissue grouping and accompanying motion metrics. Rows represent voxel time series; columns represent time points. |

A vertical carpet band indicates an intensity change shared across many voxels. It does not establish the cause. Compare its timing with motion and other evidence. Task-related changes can differ from resting-state patterns, and an unregressed carpet alone does not establish denoising adequacy.

MRIQC examples can support teaching without making MRIQC execution a prerequisite for reviewing existing fMRIPrep reports.

## 4. Assess acquisition limits and ambiguous evidence

Compare the acquisition's documented extent with the inspected images and the intended analysis. Distinguish locations supported by measured signal from locations represented only by an output grid. Resampling does not recover missing measurements.

Distinguish these observations:

- **Expected slab boundary:** anatomy stops where the acquisition ends.
- **Susceptibility dropout:** signal is lost or attenuated within the nominal acquisition.
- **Registration concern:** corresponding anatomical structures are displaced in the images being compared.
- **Missing report asset:** the linked figure cannot be displayed or is not yet available.

These can coexist. Inspect selected planes or source/derivative views when needed, retaining their image identity and space. Assess surface boundaries separately when surface or CIFTI analyses are planned; volume alignment alone is insufficient.

No automatic cutoff is supplied for FD, DVARS, tSNR, coverage fraction or registration quality. Apply established project criteria when available. Otherwise describe the evidence and keep the scientific decision pending. Behavioral trial flags remain separate from image QC.

## 5. Explain and record what was inspected

For each finding, identify the participant/run, actual panel or image, relevant view or time interval, and what was directly observed. Separate the observation from interpretation and the user's decision. Do not label a panel visually reviewed from HTML text or filenames alone.

This fictional teaching example does not describe current study data:

> The report's caption names a registration panel, but its image did not render in this session. The caption establishes the intended comparison, not alignment quality. Record this panel as not inspected and request an accessible image before giving a visual assessment.

A draft entry would identify the actual panel and use `partial`, leaving the decision blank. If the image itself could not be viewed, use `not_inspected`. A reviewed montage with no concern supports `reviewed_no_concern_in_views`, not acceptance of an entire participant.

Retain unresolved concerns as `needs_discussion`. Only an adopted user decision fills the acceptance/exclusion field. Record scope accurately so the next session resumes at the next unreviewed panel.
