# Forward tests (hcppipeline-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one exact routed part with a stable source, compatible
  environment, complete manifest, verified prerequisites, empty destination,
  and approved command returns one Run Record and QC packet.
- **Trigger:** Load for the explicit `hcppipeline-tool` skill name, a request for one bounded stage such as `run an HCP Pipelines stage`, or an exact HCP Pipelines handoff from a verified active modality or method skill.
- **Broad phrase:** `run the HCP pipeline` does not activate this adapter.
- **Routing:** `which MRI preprocessing is best?` returns to the relevant
  method guide and modality coordinator.
- **Source:** stable `v5.0.0`, `v5.1.0-rc.1`, post-release master, modified
  checkout, unknown archive, tag mismatch, commit mismatch, and
  `show_version` mismatch remain distinguishable.
- **Host:** macOS stops without installation or automatic remote execution.
- **Environment:** missing or incompatible FSL, FreeSurfer, Workbench, MSM,
  FIX, Python, MATLAB Runtime, gradunwarp, CUDA, or license stops only when
  required by the selected stage.
- **Setup:** executing rather than sourcing the required setup script fails
  environment verification.
- **Prerequisite:** a missing prior stage output stops without running that
  stage.
- **Manifest:** repeated T1w or T2w files remain explicit and no
  first-sorted-file selection occurs.
- **Acquisition:** unresolved template, mask, configuration, fieldmap,
  echo-spacing, phase-encoding, gradient coefficient, distortion, or legacy
  mode stops.
- **CLI:** each candidate command is rejected when mandatory exact-version
  arguments are absent or the entry point is wrong.
- **Gate 1:** read-only inspection performs no processing, download,
  configuration edit, or output creation.
- **Gate 2:** one unchanged command and one bounded unit execute; any source,
  input, environment, resource, destination, or part change reopens it.
- **Collision:** existing output, shared active work state, or unexplained
  partial output stops.
- **Failure:** exit `137`, scheduler failure, warning, malformed output, or
  missing artifact remains visible without retry, cleanup, or stage
  expansion.
- **QC:** a successful exit and complete artifact inventory are never labeled
  visual or scientific QC acceptance.
- **Handoff:** QC returns through the originating [smri-coordinator](../../smri-coordinator/SKILL.md),
  [fmri-coordinator](../../fmri-coordinator/SKILL.md), or [dwi-coordinator](../../dwi-coordinator/SKILL.md) checkpoint.
- **Chaining:** no structural-to-functional, volume-to-surface,
  preprocessing-to-FIX, diffusion-to-bedpostx, or QC-to-analysis transition
  runs automatically.
- **License:** the official HCP Pipelines and bundled-component licenses
  remain distinct from the NeuroClaw candidate's MIT license.
