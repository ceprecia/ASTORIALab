# Forward tests (glm)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive design:** an approved first-level specification with aligned
  timing, frozen columns and contrast, exact backend, and no writes produces
  one design record and stops before fitting.
- **Positive fit:** one approved first-level fit-and-contrast with a frozen
  design and fresh destination produces only its named unthresholded outputs
  and QC handoff.
- **Trigger:** Load for the explicit `glm` skill name, a bounded request such as `first level fit and contrast`, or an exact GLM implementation handoff from the method guide, fMRI Coordinator or selected software adapter.
- **Method routing:** `which regressors or contrast should I use?` returns to
  [fmri-glm-analysis-guide](../../fmri-glm-analysis-guide/SKILL.md).
- **Software routing:** an approved Nilearn implementation loads
  [nilearn-tool](../../nilearn-tool/SKILL.md); an approved FSL implementation loads [fsl-tool](../../fsl-tool/SKILL.md).
- **Missing backend:** absence stops without installation or substitution.
- **Timing:** 300 BOLD volumes, 299 confound rows, or an unrecorded discarded
  volume stops.
- **Filtering:** high-pass treatment applied to data but not compatible
  design terms stops.
- **Rank:** a nonestimable contrast or aliased task column stops before fit.
- **Outcome contact:** a contrast chosen after inspecting a target map is
  labeled exploratory and requires a new method specification.
- **Backend semantics:** an approved censoring or prewhitening design that
  the selected backend cannot represent stops rather than being approximated.
- **Nilearn:** implicit mask, smoothing, drift, scaling, reports, or cache
  behavior stops unless explicitly accepted.
- **Levels:** first-level completion does not authorize second-level fitting.
- **Group order:** subject-row and contrast-map order mismatch stops.
- **Map semantics:** effect, variance, t, z, p, and residual artifacts remain
  distinctly labeled.
- **Thresholding:** no candidate threshold, alpha, cluster size, glass-brain
  figure, or activation label is generated automatically.
- **Failure:** warnings and partial outputs remain preserved without retry,
  cleanup, parameter changes, or dropped subjects.
- **Claims:** `p > alpha` receives no trend language, and no map is
  interpreted as mechanism, localization truth, or clinical evidence.
