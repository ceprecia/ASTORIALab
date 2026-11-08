# SEED-VIG facts that control the review (seed-vig-skill)

Read this reference when the skill or the user asks for it.

## SEED-VIG facts that control the review

Use these facts only with their pinned source state.

### Experimental structure

- The primary paper reports 23 participants, including 12 women, with mean age
  23.3 years and standard deviation 1.4 years, and normal or corrected-to-normal
  vision.
- Participants completed an approximately two-hour monotonous four-lane
  simulated-driving experiment using vehicle controls.
- The official page states that most experiments occurred in the early
  afternoon after lunch.
- EEG, EOG, and eye tracking were recorded. PERCLOS, derived from eye tracking,
  is supplied as a continuous value from 0 to 1 and used as the vigilance
  proxy.

Do not infer that time of day, sleep history, meal state, baseline alertness,
or experimental duration is uniform when it is not documented at the required
grain.

### Acquisition and official shared products

- The primary paper reports acquisition at 1,000 Hz and describes 12 posterior
  plus six temporal EEG channels, along with forehead EOG electrodes.
- The paper's feature path filters signals from 1 to 75 Hz, downsamples to 200
  Hz, and computes features from nonoverlapping eight-second windows.
- The official page lists derived EEG feature products rather than a verified
  raw-EEG release.
- `EEG_Feature_2Hz` is described as `17 x 885 x 25` for PSD and differential
  entropy, with moving-average or linear-dynamical-system smoothing.
- `EEG_Feature_5Bands` is described as `17 x 885 x 5`.
- The official page says indices 1 through 5 are temporal and 7 through 17 are
  posterior. It leaves index 6 unexplained in that note. Preserve the gap
  instead of repairing it.
- Forehead EEG products are described as `4 x 885 x 25` and
  `4 x 885 x 5`.
- EOG feature products are described as `885 x 36`, with ICA and subtraction
  variants.
- The official page describes the PERCLOS label files as continuous values
  between 0 and 1. The primary paper separately reports 885 samples per
  experiment, matching the documented 885-sample feature products.
- These feature matrices are derived shared products, not source BIDS and not a
  verified raw-EEG product.

The paper's 18 acquired EEG channels and the official page's 17-channel shared
EEG tensor are distinct facts at different product stages. Do not call one an
error or infer the omitted channel without package-level evidence.

### Proxy, dependence, and evaluation boundaries

- PERCLOS measures the proportion of time the eyes are substantially closed
  over an interval. In SEED-VIG it is an eye-derived proxy for vigilance, not a
  direct measure of vigilance, a clinical diagnosis, or a driving-safety
  determination.
- The official page does not document Karolinska Sleepiness Scale labels or a
  canonical binary vigilance label. Do not inherit either from repository
  candidates.
- The 885 feature samples within an experiment are temporally dependent and
  nested within a participant.
- The primary paper describes splitting each experiment into five parts for
  historical evaluation. That method is precedent, not evidence of
  cross-participant generalization.
- Random window-level splits can leak participant and adjacent-time
  information. The split must match the user's stated generalization target.
