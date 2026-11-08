# Challenge facts that control the review (mschallenge-skill)

Read this reference when the skill or the user asks for it.

## Challenge facts that control the review

Use these as dated orientation and recheck them at invocation:

- The resource is the longitudinal MS lesion segmentation challenge conducted
  with ISBI 2015.
- Training contains 5 subjects and 21 scan-timepoints. Four subjects have 4
  scans and one has 5.
- Test contains 14 subjects and 61 scan-timepoints. Ten subjects have 4 scans,
  three have 5, and one has 6.
- Together, training and test contain 19 subjects and 82 scan-timepoints with
  approximately yearly follow-up. Exact intervals are not identical.
- Every scan-timepoint includes T1-weighted MPRAGE, T2-weighted, proton-density
  weighted, and FLAIR images.
- Native T1w MPRAGE voxel size is `0.82 × 0.82 × 1.17 mm³`.
- Native T2w and PDw double-spin-echo voxel size is
  `0.82 × 0.82 × 2.2 mm³`.
- Native FLAIR voxel size is `0.82 × 0.82 × 2.2 mm³`.
- Data were acquired on a 3.0 T Philips scanner.
- Original and preprocessed versions of all four modalities are provided for
  each released scan-timepoint.
- Preprocessing applies inhomogeneity correction and brain masking, registers
  the baseline MPRAGE rigidly to a 1 mm isotropic MNI template, and registers
  the remaining modalities and follow-ups to that baseline target.
- Two expert raters delineated lesions for all 82 scan-timepoints. Only the
  two training masks per scan-timepoint are distributed. Test reference masks
  remain hidden for evaluation.
- The public challenge summary reports relapsing-remitting, primary
  progressive, and secondary progressive MS only in aggregate. It does not
  authorize a subject-level subtype mapping.
- The current IACL overview exposes direct training and test archive links.
  The official data page instead describes account-required Smart
  Stats/Smart-TOOLs access and leaderboard submission. Treat this as an
  access-route discrepancy, not a license change.
- The restrictive version 1.0 license remains binding regardless of current
  link visibility.

Do not invent participant identifiers, individual subtype labels, hidden test
references, lesion values, image dimensions, evaluation scores, or permission
for nonchallenge use.
