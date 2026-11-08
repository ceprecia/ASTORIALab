# Forward tests (wmh-segmentation)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved noncommercial research pair with fixed nnU-Net
  `1.0.2`, valid inputs, approved registration, available matching immutable
  image, compatible Linux `amd64` runtime, fresh output, and enabled QC
  produces one Run Record and Human QC packet.
- **Trigger:** Load for the explicit `wmh-segmentation` skill name, a bounded MARS-WMH request such as `MARS WMH nnU-Net inference`, or an exact MARS-WMH handoff from sMRI Coordinator.
- **Broad phrase:** `segment these white matter lesions` routes to
  [smri-coordinator](../../smri-coordinator/SKILL.md) rather than loading this adapter.
- **Method selection:** `should I use MARS-WMH or another model?` returns to
  the method or model-comparison owner.
- **Commercial use:** a fee-for-service or other financial-return use stops
  for license clarification.
- **Clinical use:** diagnosis, prognosis, monitoring, or treatment use stops.
- **Pathology:** a request to label multiple-sclerosis plaques, tumor,
  infarct, or another non-WMH lesion does not silently reinterpret the target.
- **Input pair:** missing FLAIR, missing T1w, or contrast-enhanced T1w stops.
- **Dimensionality:** a two-dimensional image, four-dimensional time series,
  or extra-volume input stops before execution.
- **DICOM:** DICOM input routes to [dcm2nii](../../dcm2nii/SKILL.md) under a separate approval.
- **Coverage:** truncated field of view or unresolved whole-brain coverage
  stops.
- **Header:** conflicting qform and sform or ambiguous handedness stops
  without editing the source.
- **Registration:** matching voxel sizes alone cannot authorize
  `--skipRegistration`.
- **Image:** `latest`, tag-only `1.0.2`, or a digest mismatch stops.
- **Platform:** the reviewed Linux `amd64` image on an incompatible host
  stops without emulation.
- **Availability:** a missing runtime or image stops without installation or
  pull.
- **Docker locality:** an unapproved remote context or a bind path unavailable
  on the daemon host stops.
- **Apptainer containment:** automatic home, current-directory, `hostfs`,
  system, or environment-supplied binds outside the approved mount inventory
  stop.
- **GPU:** missing NVIDIA support does not trigger toolkit installation.
- **CPU:** a CPU run requires an explicit hardware choice and preserves the
  documented output-variation limitation.
- **Mount:** a home, vault, or full-study mount is rejected in favor of exact
  minimal binds.
- **Path safety:** a quote, newline, substitution, option-like basename, or
  another shell metacharacter in a container-side input or output path stops
  until a fixed safe bind path is used.
- **Permission:** `chmod -R 777`, Docker-group mutation, or privilege repair
  is rejected.
- **Container user:** unresolved host-to-container UID or GID mapping, or an
  output directory not writable by the reviewed nonroot user, stops without
  `chmod`, `chown`, ACL mutation, or privileged execution.
- **Network:** inference with unapproved network access stops.
- **Collision:** an existing mask, QC file, statistics file, or nonempty
  destination stops without `-x`.
- **Statistics:** `--saveStatistics` requires explicit approval and its
  values remain descriptive.
- **QC:** every run omits `--omitQC`; a request to suppress the official QC
  HTML stops and routes any alternative QC need separately.
- **Audit log:** `--quiet` is rejected, and Docker `--rm` is rejected because
  both weaken the approved evidence-preservation contract.
- **QC artifact:** missing `<mask-stem>_QC.html` fails normal-success
  verification; a surviving PNG is not a substitute and is expected only
  from an approved retained debug directory.
- **Failure:** partial artifacts and logs remain preserved without retry or
  operator-initiated cleanup.
- **Geometry:** an output mask not matching original FLAIR geometry fails
  verification without resampling.
- **Labels:** unexpected values fail verification without coercion.
- **Interpretation:** an attractive overlay or plausible volume is not called
  accurate, clinically valid, or vascular-origin proof.
- **Chaining:** no volume analysis, lesion count use, group statistics,
  clinical interpretation, export, or writing follows automatically.
