# MND dataset facts that control the review (mnd-skill)

Read this reference when the skill or the user asks for it.

## MND dataset facts that control the review

Use these as dated orientation and recheck them at invocation:

- The current verified release is OpenNeuro `ds005874` snapshot `1.1.0`, DOI
  `10.18112/openneuro.ds005874.v1.1.0`, with official mirror commit
  `aafeb3ea57315f583aeeb1c9db30eccd7e5d0929`.
- Snapshot 1.1.0 uses BIDS 1.10.0, declares CC0, and added diffusion volumes
  and MRtrix code relative to 1.0.0.
- The current participant table contains 59 people: 36 MND cases and 23
  non-neurodegenerative controls.
- Case labels include ALS, PLS, undefined MND, and ALS-bvFTD. The dataset is
  not one homogeneous ALS-only group.
- Controls are a convenience sample of spouses, friends, or colleagues. A
  paper finding of no age difference is not evidence that controls were
  prospectively age-matched.
- The fasted and postprandial imaging sessions occurred during one research
  visit, about 33 minutes apart after a liquid meal. They are prandial states,
  not longitudinal disease follow-up.
- Both sessions include resting-state fMRI and a food-cue task showing
  high-calorie food, low-calorie food, and non-food images. The task is not
  finger tapping, hand grip, or another motor paradigm.
- Session 1 includes T1w MP2RAGE and T2w FLAIR. Snapshot 1.1.0 adds
  session-2 DWI.
- DWI is absent for `sub-17`. `sub-43` used a 20-channel rather than
  64-channel coil and has changed diffusion TE and TR.
- Imaging was acquired at one Brisbane site on a 3 T Siemens Prisma.
- Physiology, appetite, anthropometric, and clinical phenotype records plus
  fMRIPrep and PhysIO derivatives are released with product-specific
  completeness and provenance.
- The primary paper reports that four MND participants had more than half of
  their fMRI volumes above FD 0.5 mm. That observation is material evidence,
  not a dataset-owned exclusion threshold.
- Eyes-open versus eyes-closed resting instructions are not established by the
  currently verified release documentation and must remain unknown unless an
  exact sidecar or protocol resolves them.

Do not call the sessions longitudinal, the task motor, the controls
age-matched, or DWI absent from the current release.
