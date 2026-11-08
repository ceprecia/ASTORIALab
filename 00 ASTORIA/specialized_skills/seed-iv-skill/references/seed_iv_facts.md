# SEED-IV facts that control the review (seed-iv-skill)

Read this reference when the skill or the user asks for it.

## SEED-IV facts that control the review

Use these facts only with their pinned source state.

### Experimental structure

- The official resource describes 15 participants completing three sessions
  on different days.
- Each session contains 24 film trials, six for each of four intended emotion
  conditions: happy, sad, fear, and neutral.
- The three sessions use different clips, yielding 72 clips across the
  experiment and 1,080 participant-session-trial observations before any
  exclusion.
- The primary paper describes 15 healthy right-handed participants, including
  eight women, aged 20 to 24.
- A trial includes an emotion-induction film of about two minutes, followed by
  a five-second hint and a 45-second PANAS self-assessment period.
- Participants reported the emotion they actually felt. The paper protocol
  discarded clips judged unsuccessful or weak during stimulus development.

Do not treat the arithmetic maximum as proof that every shared product contains
every observation. Verify manifests and missingness outside this skill before
analysis.

### Acquisition and official shared products

- EEG was acquired with a 62-channel ESI NeuroScan system at 1,000 Hz.
- Eye movement was recorded with an SMI system.
- The official page describes session-level raw EEG MATLAB files with 24 trial
  fields.
- It also describes EEG PSD and differential-entropy features, with moving
  average or linear-dynamical-system smoothing and a `62 x W x 5` structure,
  where `W` is the number of temporal windows.
- The documented EEG feature path downsamples to 200 Hz, filters from 1 to 75
  Hz, divides signals into nonoverlapping four-second segments, and derives
  five frequency-band features.
- Raw eye-movement products include blink, event, fixation, pupil, and saccade
  information; separate eye-movement feature products are also listed.
- Channel order and label interpretation depend on the distributed workbook
  and README. Do not reconstruct them from array position.
- These products are MATLAB-oriented shared products, not source BIDS.

### Construct, dependence, and rights boundaries

- Happy, sad, fear, and neutral are intended elicitation conditions supported
  by participant self-assessment. They are not clinical diagnoses or
  infallible ground-truth states.
- Participant, session, film trial, and temporal windows are nested or repeated
  units. Random window-level splitting can leak participant, session, or film
  information and cannot establish cross-participant generalization.
- Session-day and film-set differences are inseparable unless the proposed
  design explicitly models or holds them out.
- The academic data license does not confer rights to redistribute the film
  stimuli. Treat film rights as separate and unverified.
