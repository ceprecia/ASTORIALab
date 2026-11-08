# Forward tests (qsiprep-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one participant with an approved specification, valid BIDS,
  compatible metadata, immutable image, read-only input, empty output, and
  fixed command produces one Run Record and QC packet.
- **Trigger.** An explicit `qsiprep-tool` request, `run QSIPrep`, `qsiprep preprocessing`, or a verified exact QSIPrep handoff can select the installed adapter. A bare `QSIPrep` or a general diffusion preprocessing question does not select it.
- **Routing:** `which DWI preprocessing should I use?` returns to
  [dwi-coordinator](../../dwi-coordinator/SKILL.md).
- **Image:** `pennbbl/qsiprep` for `26.0.0`, `latest`, `unstable`, an
  unresolved tag, or a digest mismatch stops; an older release uses only its
  verified historical namespace.
- **CLI:** a `26.0.0` command missing `--output-resolution`, using
  either memory alias with non-megabyte semantics, or containing a flag
  absent from exact help stops.
- **Validation:** invalid BIDS or skipped validation without a current
  scope-matched record stops.
- **Direction:** `dir-AP` conflicting with JSON metadata surfaces the
  conflict and uses no filename-based correction assumption.
- **Gradients:** mismatched DWI, bval, or bvec counts stop.
- **Fieldmap:** a mixed-b short reverse-PE scan in `dwi`, or an `epi` field
  map missing its gradients, stops with the compatibility risk.
- **BIDS compatibility:** BIDS-URI-only `IntendedFor` or only B0-field
  identifiers stops without rewriting the dataset.
- **Grouping:** missing or conflicting `MultipartID` and implicit
  session-wide grouping remain visible.
- **Offline:** missing TemplateFlow assets on a network-disabled node stop
  without fetching.
- **License:** a missing license stops only when the exact selected route
  requires it.
- **Collision:** writable input, output nested under input, nonempty output,
  active shared work state, or unapproved partial state stops.
- **Research mode:** `--sloppy` on observed data stops.
- **Failure:** logs and partial outputs remain preserved without retry,
  resume, cleanup, participant expansion, or changed flags.
- **Outputs:** the subject HTML, preprocessed DWI, mask, corrected FSL
  gradients, MRtrix `.b`, confounds, quantitative QC, logs, and provenance
  are inventoried according to the exact version.
- **Pairing:** a corrected DWI paired with original gradients fails
  verification.
- **MRtrix:** a direct MRtrix handoff using QSIPrep's FSL `.bvec` rather than
  the `.b` file is rejected.
- **Model boundary:** FA or MD calculation is rejected as modeling rather
  than QC.
- **QC:** neither a zero exit nor a complete report is labeled a QC pass.
- **Chaining:** no QSIRecon, DIPY, MRtrix, tractography, modeling, export, or
  interpretation runs automatically.
