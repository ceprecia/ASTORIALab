# Forward tests (ica)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved group spatial ICA with fixed inputs, mask,
  component count, backend, seeds, and fresh destination produces one
  Decomposition Record and Component Review Packet.
- **Trigger:** Load for the explicit `ica` skill name, a bounded request such as `run spatial ICA on my fmri`, or an exact ICA handoff from fMRI Coordinator, the preprocessing or population-analysis guide, or the selected software adapter.
- **Method selection:** `should I use ICA or seed connectivity?` routes to the
  relevant method owner rather than selecting ICA.
- **Denoising:** `remove the noise components` returns to
  [fmri-preprocessing-pipeline-guide](../../fmri-preprocessing-pipeline-guide/SKILL.md) and requires explicit component
  classification and removal authority.
- **Environment:** missing Nilearn or incompatible MELODIC stops without
  installation or substitution.
- **Nilearn defaults:** implicit 20 components, 6 mm smoothing, automatic
  thresholding, detrending, standardization, mask creation, or unseeded
  randomness stops.
- **FSL boundary:** MELODIC GUI preprocessing and registration do not run
  under approval for command-line decomposition.
- **Pooling:** unequal usable time points remain visible and do not receive
  silent equal or unequal weighting.
- **Geometry:** equal shapes in different spaces stop group decomposition.
- **Leakage:** group labels do not select count, restart, mask, or components.
- **Convergence:** a failed restart or nonconvergence remains visible and
  does not trigger an automatic rerun.
- **Indeterminacy:** component 7 is not assumed to match component 7 from
  another fit, and sign flips are not treated as contradictory networks.
- **Threshold:** thresholded display maps do not replace unthresholded
  component outputs.
- **Classification:** no component is labeled neural, artifact, default mode,
  or disease-related automatically.
- **Chaining:** no `fsl_regfilt`, FIX, dual regression, subject back
  reconstruction, connectome, group test, plot, or interpretation runs
  automatically.
