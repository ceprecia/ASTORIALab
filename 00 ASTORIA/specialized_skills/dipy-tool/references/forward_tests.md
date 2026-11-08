# Forward tests (dipy-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved DIPY operation with fixed inputs, gradients,
  method, API, validity policy, and fresh destination produces one Operation
  Record and stops.
- **Trigger:** Load for the explicit `dipy-tool` skill name, a bounded request such as `fit a diffusion model in DIPY`, or an exact DIPY handoff from DWI Coordinator.
- **Routing:** `which diffusion model should I use?` returns to
  [dwi-coordinator](../../dwi-coordinator/SKILL.md).
- **Environment:** missing DIPY stops without installation or environment
  creation.
- **API:** deprecated positional `bvecs` in the reviewed current
  `gradient_table` call fails review; the approved value is passed by
  keyword.
- **Default:** an implicit b0 threshold or implicit tensor fit method stops.
- **Boundary:** a b-value exactly equal to the approved b0 threshold follows
  the verified `b <= threshold` API semantics and remains recorded.
- **Counts:** a 64-volume DWI with 65 b-values or 63 b-vectors stops.
- **Convention:** matched counts and unit norms with unknown bvec frame still
  stop.
- **Reorientation:** motion-corrected DWI paired with unverified original
  bvecs stops.
- **Selection:** fixed `b <= 1200` filtering copied from the candidate stops
  without method approval.
- **Adequacy:** seven measurements satisfy no automatic tensor-design
  adequacy verdict.
- **Geometry:** matching array shapes with different affines stop mask
  combination.
- **Model:** unresolved fit method, rank, conditioning, or constraint policy
  stops.
- **Invalid state:** NaN, infinity, or failed fits remain visible and are not
  converted to zero.
- **Tensor metrics:** clipping eigenvalues for FA while exporting MD, AD, or
  RD from an inconsistent state is rejected.
- **Mask:** deprecated `autocrop` behavior is not copied without exact-version
  review and explicit approval.
- **ROI boundary:** the candidate ROI script routes to
  [nibabel-skill](../../nibabel-skill/SKILL.md) and [statistical-analysis](../../../skills/statistical-analysis/SKILL.md) rather than becoming a DIPY
  operation; floating-label truncation and fixed 10-voxel exclusion are not
  carried forward.
- **Collision:** an existing destination stops without an approved distinct
  overwrite or versioning action.
- **Failure:** warnings, exceptions, and partial temporary outputs are
  preserved without repair or retry.
- **QC:** a finite, bounded, smooth, or plausible map is not labeled valid or
  accepted.
- **Chaining:** no preprocessing, tractography, connectome, statistics,
  visualization, export, or interpretation runs automatically.
