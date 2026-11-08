---
name: eeg-analysis-guide
description: >-
  Compares and specifies one already approved nonclinical sensor-space scalp EEG
  preprocessing and measurement route for an ERP or event-related time-frequency
  estimand, then returns a selection-bound EEG Analysis Method Specification
  after two approval gates. Use when the request, or a part coordinator, hands over
  one exact matching method question. It makes input state, event timing,
  filtering, resampling, reference, rank, bad-channel, artifact, interpolation,
  epoch, baseline, measurement, quality, exclusion, sensitivity, reporting, and
  statistical-handoff decisions inspectable without choosing the question,
  signal target, task, acquisition, power, software, thresholds, inferential
  model, interpretation, or claim. Triggers: plan my ERP or time frequency
  analysis, EEG measurement route.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: method-guide
  modality: eeg
  dependencies: ""
  requires: ""
  gates: choosing the method, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-11-02"
---

# EEG Analysis Guide

Specify one defensible scalp EEG method without turning an external recipe,
software default, or familiar component label into a scientific decision.

## Purpose

It does not access or alter data; run MNE or another package; perform source localization, connectivity, decoding, clinical EEG, MEG, iEEG, ECoG, fNIRS, or eye-tracking analysis; install anything; save files; or chain implementation.

`eeg-analysis-guide` is the conditional Part 4 method owner for one approved
nonclinical sensor-space scalp EEG analysis route. It owns:

- the input and acquisition-state audit needed for method planning;
- ordered preprocessing decisions and their signal, timing, and rank effects;
- ERP or event-related time-frequency measurement specification;
- outcome-blind quality control, exclusion, sensitivity, and reporting plans;
- a bounded statistical handoff; and
- one EEG Analysis Method Specification.

Handle one measurement route per invocation. A joint ERP and time-frequency
plan requires the user to approve both estimands and the shared versus distinct
processing decisions explicitly.

The user owns the research question, hypothesis, prediction, confirmatory status,
construct, task, signal target, event lock, contrast, population, acquisition,
sample and trial plan, preprocessing selections, measurement definition,
exclusions, inferential method, thresholds, interpretation, and claims.

[eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) owns event-related task schedules, markers, and
physical timing validation. [cogsci-statistics](../cogsci-statistics/SKILL.md) owns inferential model
selection, dependence, multiplicity, evidence for absence, and statistical
interpretation. `eeg-coordinator` may later route checkpoints but does not own method
choices. `mne-eeg-tool` may later implement a completed specification but does
not choose it.

Activate only when:

- The user invokes the exact trigger `eeg-analysis-guide`; or
- a verified Active capability hands off one already approved scalp EEG
  method question with an explicit target, estimand, event lock or segment
  definition, contrast, population, and scientific status.

Do not trigger from `EEG`, `ERP`, `P300`, `N400`, `ERN`, `oscillation`,
`time-frequency`, `preprocess`, `MNE`, `brain waves`, `analyze my EEG`, a file
extension, or another broad signal, component, software, or task phrase.

This skill supports:

- nonclinical scalp EEG in sensor space;
- event-related potentials and response-locked potentials;
- event-related sensor-space power, phase, or time-frequency measurement when
  the target band, time relation, and estimand are already approved;
- prospective method specification or read-only review of an existing
  pipeline against its approved scientific purpose.

This skill excludes:

- task selection, task programming, marker generation, acquisition setup,
  participant or trial power, and data collection;
- resting-state or continuous spectral analysis without an approved
  event-related estimand;
- source localization, inverse modeling, dipole fitting, beamforming, and
  source-space statistics;
- connectivity, network inference, decoding, RSA, temporal generalization,
  classification, regression prediction, and BCI analysis;
- clinical interpretation, diagnosis, seizure review, sleep staging,
  neurofeedback, monitoring, prognosis, or treatment;
- MEG, OPM, iEEG, ECoG, sEEG, fNIRS, eye tracking, EMG, ECG, and multimodal
  fusion;
- package syntax, file conversion, preprocessing execution, model fitting,
  visualization production, or file writing.

Return the in-scope specification and a bounded handoff when a request crosses
these boundaries. Do not absorb the later owner.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Scientific contract | user-approved question, prediction, estimand, contrast, status, and permitted claim |
| Measurement route | ERP or one event-related sensor-space time-frequency estimand |
| Population and design | Participants, conditions, sessions, runs, blocks, trials, dependence, and relevant accessibility or clinical characteristics |
| Event basis | Event or response lock, marker provenance, physical timing evidence, neighboring events, overlap, and timing uncertainty |
| Acquisition state | System, channel types, montage, electrode coordinates, acquisition reference, sampling rate, online filters, impedances or contact-quality records, auxiliary channels, and data units |
| Input state | Raw or transformed state, file provenance, prior operations, annotations, missing channels, discontinuities, and outcome-contact history |
| Signal target | Polarity or spectral quantity, expected temporal and spatial support, measure, and evidence source without mechanistic inference |
| Quality context | Known artifacts, bad channels or segments, missingness, retained trials, condition balance, and population-specific threats |
| Statistical boundary | Observation unit, intended inferential owner, multiplicity family, exchangeability or dependence constraints, and no-result-contact boundary |
| Output boundary | Chat-only method specification and separately approved implementation handoff |

If the target, estimand, event basis, acquisition reference, sampling
information, montage, input state, contrast, or outcome-contact history is
unknown, stop with **EEG method intake incomplete**. Do not reconstruct it from
a software object, filename, component name, or source default.

## Steps

### 1. Build the EEG Method Intake Record

Separate:

- supplied facts;
- source-backed observations;
- AI interpretation;
- user-owned selections;
- missing, conflicting, or outcome-exposed decisions.

Restate the exact in-scope route and all exclusions. Do not turn a component
name, dataset, or MNE object into a scientific contract.

### 2. Gate 1: approve the signal, evidence, and decision boundary

Show:

1. approved question, target, estimand, contrast, population, and status;
2. event and acquisition state;
3. input provenance and prior transformations;
4. exact evidence sources and verification state;
5. the filtering, reference, artifact, channel, epoch, baseline, measurement,
   exclusion, quality, sensitivity, and statistical decisions to compare;
6. unresolved conflicts, outcome-contact risks, exclusions, and stop point.

Gate 1 authorizes only method comparison and read-only review of supplied
metadata or an existing pipeline description. It does not authorize data
access, transformation, preprocessing, software use, package changes,
statistics, result inspection, saving, or implementation.

Reopen Gate 1 after a material target, event, population, acquisition, input,
evidence, estimand, or outcome-contact change.

### 3. Compare only applicable method routes

For each real alternative or fixed route, show:

- exact decision and evidence;
- target-signal fit;
- operation-order and rank implications;
- artifact, distortion, information-loss, and bias risks;
- QC and verification requirements;
- sensitivity route;
- reporting consequences;
- unresolved limitations.

Use alternatives only where evidence supports more than one defensible route.
If one route is fixed by the approved design or input state, explain why
without inventing options.

### 4. Build the EEG Method Decision Ledger

Keep these approvals separate:

| Decision | Candidate routes | Evidence and applicability | Signal or rank effect | QC and sensitivity | The user selection |
|---|---|---|---|---|---|
| Input and event state | | | | | |
| Filtering and line noise | | | | | |
| Resampling | | | | | |
| Reference | | | | | |
| Bad channels and segments | | | | | |
| Artifact handling | | | | | |
| Interpolation and order | | | | | |
| Epoch and event lock | | | | | |
| Baseline treatment | | | | | |
| ERP or time-frequency measure | | | | | |
| Trial and participant exclusions | | | | | |
| Quality and reliability | | | | | |
| Statistical and multiplicity handoff | | | | | |

Approval of one row does not authorize another. Leave an unresolved row
explicit rather than filling it from a source or package default.

### 5. Gate 2: approve one complete method specification

Ask the user to select, revise, or reject:

- the ordered pipeline and all separately listed decisions;
- outcome-blind review and exclusion procedures;
- measurement definition and permitted claim;
- quality, reliability, sensitivity, and reporting plan;
- statistical handoff and multiplicity boundary;
- unresolved limitations and implementation stop point.

Do not infer selection from silence. If a required row remains unresolved,
return **EEG method specification incomplete** and the exact decision needed.

Gate 2 authorizes only the chat-based specification. It does not authorize
data access, code, software, package installation, preprocessing, model
fitting, result inspection, file writes, or downstream interpretation.

### 6. Produce the EEG Analysis Method Specification

Return:

```text
EEG Analysis Method Specification
Approved question, prediction, estimand, contrast, and status:
Permitted and prohibited claims:
Population, design, and dependence:
Measurement route:
Event lock or segment definition and timing evidence:
Acquisition system, montage, coordinates, reference, sampling, and online filters:
Input identity, state, provenance, and prior transformations:
Outcome-contact and deviation state:
Ordered processing route:
Filter and line-noise specification:
Resampling and event reconciliation:
Rereference and rank accounting:
Bad-channel, bad-segment, and interpolation plan:
Artifact detection, review, correction, and residual-QC plan:
Epoch, padding, overlap, and baseline plan:
ERP or time-frequency measurement definition:
Trial, channel, participant, and dataset exclusion rules:
Retained-data, balance, quality, and reliability checks:
Sensitivity and robustness routes:
Descriptive outputs and reporting fields:
Statistical estimand, dependence, multiplicity, and exchangeability handoff:
Known conflicts, limitations, and unresolved evidence:
Implementation owner, acceptance checks, and stop point:
```

Stop after the specification. Route implementation only through a separately
invoked, verified adapter and a new approval.

## Boundaries

For each proposed decision:

1. label it `direct evidence`, `bounded adaptation`, `design-derived`,
   `candidate for sensitivity analysis`, `software constraint`, `unknown`, or
   `conflicting`;
2. record the exact source, version or publication, population, task,
   acquisition, signal target, and applicability;
3. verify every fixed value against a current primary, professional, or
   official source before presenting it as a candidate;
4. distinguish acquisition settings, method choices, implementation
   parameters, and reporting fields;
5. preserve credible conflicts and show their consequences;
6. treat package defaults as implementation facts, never scientific
   justifications;
7. record any outcome-informed change as a deviation and label affected work
   exploratory unless it was prospectively authorized.

Never supply a universal cutoff, reference, channel-count rule, artifact
threshold, ICA component count, classifier probability, ASR setting, epoch,
baseline, trial minimum, rejection percentage, time window, electrode set,
frequency band, wavelet cycle count, taper, or cluster threshold.

### Input integrity and provenance

- Preserve the untouched source recording conceptually. The specification
  names inputs and transformations but does not alter them.
- Reconstruct the ordered history of every prior filter, reference,
  resampling, interpolation, correction, rejection, epoch, baseline, and
  export operation. Unknown history is a limitation, not permission to assume
  raw data.
- Verify event identifiers, event grain, physical timing, duplicates,
  omissions, restarts, discontinuities, and synchronization evidence before
  an event-locked plan.
- Keep participant, session, run, trial, channel, event, condition, and file
  identities available through every later handoff.

### Filtering and resampling

- Justify filtering from the target signal, noise, sampling, event timing, and
  intended claim rather than a standard pipeline.
- Specify filter family, cutoff definition, passband and stopband, transition
  width, order or length, ripple, phase and delay, direction, padding, edge
  handling, and whether filtering applies to continuous or segmented data.
- Inspect or plan to inspect frequency, impulse, and step responses plus
  temporal smearing relative to events and baselines.
- Treat high-pass, low-pass, notch, regression, and line-noise methods as
  alternatives with different distortion risks. One does not imply another.
- Specify anti-aliasing behavior before downsampling and preserve event timing
  and sample-index reconciliation.
- When artifact decomposition and the scientific signal require different
  filtering, compare an explicitly documented fitting-copy route with other
  justified routes. Never overwrite the analysis signal or apply the choice
  silently.

### Reference, rank, channels, and interpolation

- Distinguish the physical acquisition reference from every offline
  rereference.
- Compare only reference schemes compatible with the montage, coverage,
  target measure, topographic claim, and later analysis.
- Track rank changes from reference, interpolation, projection, channel
  removal, and decomposition. Do not infer full rank from channel count.
- Define bad-channel, bridged-electrode, flat, noisy, and transient-segment
  evidence without a universal threshold.
- Specify whether a channel is removed, marked, repaired, or interpolated and
  when that occurs. Check how order changes the reference and decomposition.
- Record every affected channel, interval, reason, reviewer, and downstream
  consequence. Extensive repair may bound or invalidate the estimand.

### Artifact handling and quality control

- Compare applicable rejection, annotation, regression, ICA, projection,
  ASR, or other correction routes. Availability does not establish validity.
- Define the artifact class, detection evidence, correction target, preserved
  signal, audit trail, and residual-artifact check for each route.
- Treat automated labels, probabilities, outlier scores, components, and
  suggested exclusions as review candidates, not truth.
- Review manual cleaning without condition, group, outcome, or effect
  information when practical. Record unavoidable unblinding.
- Inspect both residual artifact and possible removal or distortion of neural
  signal. A cleaner trace is not sufficient validation.
- Never prescribe how many components, channels, trials, or participants to
  remove.

### Epochs, baselines, and overlap

- Define event or response lock, epoch extent, padding, neighboring events,
  overlap, temporal smearing, and edge exclusions from the approved estimand.
- Treat baseline subtraction, baseline as a modeled covariate, detrending, and
  no baseline as assumption-bearing alternatives.
- Check whether the baseline can differ by condition, contain anticipatory
  activity, inherit prior-event activity, or overlap a filter response.
- Preserve trials and participants affected by missing markers, boundary
  events, restarts, or unequal opportunity for retention.
- Do not use an attractive poststimulus result to redefine the epoch or
  baseline while retaining a confirmatory label.

### ERP measurement

- Define component label, polarity, event lock, measurement quantity,
  contrast, time window, sensors or ROI, aggregation, and trial contribution
  independently of the tested effect.
- Use prior evidence, a valid independent localizer, a contrast-collapsed
  localizer, held-out data, or multiplicity-controlled mass-univariate work
  as applicable. Never select a window or sensor from the same effect and
  test it as if independent.
- Compare mean, peak, area, latency, difference-wave, or single-trial
  measurement only when each answers the approved estimand and its noise bias
  is explicit.
- Treat an ERP name, polarity, latency, topography, or putative generator as a
  descriptive convention. It does not establish one cognitive process,
  mechanism, anatomical source, or diagnosis.

### Event-related time-frequency measurement

- Define frequency quantity, estimator family, time-frequency resolution,
  smoothing, cycles or tapers, padding, edge region, decimation, reference,
  baseline or normalization, phase treatment, and aggregation from the
  approved estimand.
- Distinguish evoked, induced, total, phase-locked, non-phase-locked, power,
  amplitude, and phase-consistency quantities.
- Treat canonical frequency-band names as labels, not fixed numerical ranges
  or mechanisms.
- Keep source estimates, connectivity, decoding, and continuous or resting
  spectral questions outside this route.

### Exclusions, reliability, and reporting

- Define channel, segment, trial, participant, condition, and dataset
  exclusions separately, including timing, evidence, reviewer, and appeal or
  sensitivity rule.
- Report retained and rejected data by participant and condition, not only a
  pooled percentage. Surface imbalance that changes precision or the
  estimand.
- No universal trial count establishes adequate power or reliability. Tie
  usable-data requirements to the component, measurement, noise, population,
  contrast, participant count, and intended inference.
- Prespecify a data-quality or reliability assessment appropriate to group
  effects versus individual-difference claims.
- Preserve descriptive waveforms or time-frequency summaries, topographies,
  uncertainty, attrition, complete processing parameters, software versions,
  and deviations for later reporting.

### Statistical handoff and claims

- Define the observation unit, contrast, dependence, nuisance structure,
  inferential target, multiplicity family, exchangeability, tails, effect
  estimate, uncertainty, and sensitivity requirements before handoff.
- Keep inferential-model selection and execution with
  [cogsci-statistics](../cogsci-statistics/SKILL.md).
- For paired conditions, preserve pairing and use a paired estimand. Do not
  substitute an unpaired implementation.
- Cluster-based permutation supports a cluster-level inference. Cluster
  membership does not establish precise effect onset, offset, sensor
  location, frequency extent, or significance at every member sample.
- A nonsignificant result is not evidence of absence without an appropriate
  prespecified method. Never describe `p > alpha` as marginal, approaching
  significance, a trend, or nearly supported.

Stop when:

- the scientific target, event basis, acquisition reference, montage,
  sampling state, input history, contrast, or outcome-contact state is
  missing;
- a choice is justified only by a package default, candidate table, copied
  recipe, or unverified numerical recommendation;
- manual cleaning is condition-aware or outcome-driven without an explicit
  exploratory deviation;
- artifact correction lacks an audit trail, residual check, or preserved
  signal check;
- reference, interpolation, projection, or decomposition rank is unresolved;
- baseline contamination, overlapping events, temporal smearing, or edge
  effects threaten the estimand;
- a measurement window, sensor set, band, or parameter was selected from the
  tested effect without valid independence or multiplicity control;
- retained-data imbalance or exclusion changes the estimand;
- the multiplicity family or permutation exchangeability is undefined;
- the request would produce a clinical or person-specific interpretation.

Handoff:

- task schedule, event ontology, markers, and physical timing to
  [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md);
- participant and retained-trial power to [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) or
  [statistical-power](../../skills/statistical-power/SKILL.md);
- inferential model, multiplicity, absence evidence, and statistical
  interpretation to [cogsci-statistics](../cogsci-statistics/SKILL.md);
- decoding, RSA, or temporal generalization to
  [neural-decoding-analysis](../neural-decoding-analysis/SKILL.md);
- connectivity to [brain-connectivity-modeler](../brain-connectivity-modeler/SKILL.md);
- source localization, continuous or resting spectral analysis, and other
  research modalities to a verified dedicated research owner or an explicit
  capability gap;
- clinical EEG requires qualified human clinical expertise outside ASTORIA;
- MNE implementation to the verified `mne-eeg-tool` capability when the current
  request authorizes that bounded implementation handoff.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Boudewyn et al. (2018). *Psychophysiology, 55*, e13049. https://doi.org/10.1111/psyp.13049
- Clayson, Brush, & Hajcak (2021). *International Journal of Psychophysiology, 165*, 121–136. https://doi.org/10.1016/j.ijpsycho.2021.04.004
- Keil et al. (2014). [EEG/MEG committee report]. *Psychophysiology, 51*, 1–21. https://doi.org/10.1111/psyp.12147
- Keil et al. (2022). *Psychophysiology, 59*, e14052. https://doi.org/10.1111/psyp.14052
- Luck & Gaspelin (2017). *Psychophysiology, 54*, 146–157. https://doi.org/10.1111/psyp.12639
- Maris & Oostenveld (2007). *Journal of Neuroscience Methods, 164*, 177–190. https://doi.org/10.1016/j.jneumeth.2007.03.024
- Pernet et al. (2020). [OHBM COBIDAS-MEEG]. *Nature Neuroscience, 23*, 1473–1483. https://doi.org/10.1038/s41593-020-00709-0
- Sassenhagen & Draschkow (2019). *Psychophysiology, 56*, e13335. https://doi.org/10.1111/psyp.13335
- Tanner, Morgan-Short, & Luck (2015). *Psychophysiology, 52*, 997–1009. https://doi.org/10.1111/psyp.12437
- Widmann, Schröger, & Maess (2015). *Journal of Neuroscience Methods, 250*, 34–46. https://doi.org/10.1016/j.jneumeth.2014.08.002
