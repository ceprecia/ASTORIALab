---
name: verify-repository-release
description: 'Checks an exact repository release against the intended files, versions,
  identifiers, metadata, access settings and related-output links. Reports observed
  deposit state without certifying computational reproducibility. Triggers: inspect
  this deposited research version, check repository release metadata.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: exact repository version, authorized inspection access and intended
    release evidence where available
  created: '2026-11-02'
  updated: '2026-11-02'
  gates: ''
---

# Verify Repository Release

Check what a specific repository record actually contains and what access was observed.

## Purpose

Compare one exact repository record/version with the intended release. Inspect
identifiers, files, metadata, access state and related-output links at a stated
depth. Distinguish a declared property from an observed property.

Use for draft, published, embargoed or restricted records. Verification may be
limited to metadata, a file listing, selected files or a complete comparison;
report that scope explicitly. A successful deposit is not a reproduced analysis.

## Inputs

- Exact repository URL, record identifier, version/snapshot and intended citation.
- Intended release manifest or authoritative package, including versions and
  available file-integrity information.
- Intended access, metadata, license and related-output links to compare.
- Current authorized access context: public viewer, reviewer, collaborator or owner.
- Requested inspection depth and relevant evidence from the technical owners.
- Original invoking owner and any applicable repository, publisher or funder rules.

If no intended manifest exists, inspect the observed record and identify that
limitation; do not silently substitute the file list as proof of completeness.

## Steps

1. Read [source verification](../research-output-coordinator/references/source_verification.md)
   and [repository candidates](../research-output-coordinator/references/repositories.md)
   completely. Use current repository-owner documentation for version, identifier,
   access and release behavior; recheck relevant notices for the selected record.
2. Resolve the exact record and version. Distinguish a record covering all versions
   from a version-specific identifier, the latest draft and the version cited by a
   publication. Do not choose the newest version merely because it is easiest to find.
3. Establish inspection scope and access context. Use the available read capability
   that exposes the necessary evidence. State whether the task can inspect only
   metadata, the file listing, selected content or the complete intended package.
4. Record the observed repository state and version evidence. For mutable drafts,
   identify the observation time and any changes seen during inspection. Do not
   describe a draft or unsaved changes as an immutable published snapshot.
5. Compare listed files with the intended manifest. Check paths, counts, sizes,
   file roles and version associations where available. Identify missing, extra,
   substituted or inaccessible items without assuming every difference is an error.
6. Inspect file content and integrity only to the authorized and available depth.
   A displayed filename or checksum is not an independently computed comparison.
   Record which files were retrieved, opened or compared and which were not.
7. Inspect relevant metadata: title, contributors, affiliations, description,
   provenance, license, citations, funders, access declaration and linked resources.
   Compare with the supplied authoritative material; unconfirmed contributor or
   institutional claims stay unconfirmed even when present in the repository.
8. Test the requested access behavior in the actual available viewer context.
   Owner visibility does not prove anonymous public access. A reviewer link does
   not prove all files are downloadable. Report access not tested instead of
   changing permissions, publishing a draft or bypassing restrictions to test it.
9. Check identifier resolution and related-output links. Distinguish a DOI shown
   in metadata, a resolving DOI, the correct target version and accessible files.
   A linked article DOI does not become a dataset DOI. Follow links needed for the
   bounded comparison and report redirects, broken links or version mismatches.
10. Return observed matches and discrepancies with supporting record/file evidence,
    the current source state, inspection limits and the next responsible owner.
    Separate findings about publication state, availability, content integrity,
    format validation and computational reproduction.

## Outputs

Return the result in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization and an owning destination. Include:

- Exact record/version, intended comparison and original return owner.
- Observed repository state, access context and inspection depth.
- File/manifest comparison and the content or integrity checks actually performed.
- Metadata, identifier, citation, access and related-resource findings.
- Current primary-source state for any requirement-dependent judgment.
- Discrepancies, inaccessible or uninspected scope and the next action/owner.

Use a small comparison table when useful: intended item/property, observed
evidence, comparison result and remaining work. A metadata-only inspection may
confirm metadata properties while leaving file completeness and content unverified.
Do not label the whole release verified when only a subset was inspected.

## Boundaries

- Follow me.md for saving and external actions. This inspection does not itself
  alter metadata, access controls, files, repository versions or publication state.
- A DOI, a successful upload, a green validation badge or an accessible landing
  page does not certify that the intended analysis can be reproduced.
- Repository declarations, author assertions and independent observations are
  different evidence. Do not infer consent, scientific quality or institutional
  acceptance from the existence of a record.
- Preserve the selected historical version. A corrected draft does not repair
  the contents or citation of an already published version automatically.
- When required content is inaccessible, state the precise unknown and continue
  the available comparison. Do not replace it with a cached snippet or guess.

## Handoffs

- prepare-research-release owns package and metadata preparation; return exact
  discrepancies and record/version locators rather than silently repairing them.
- analysis-coordinator and the selected technical owner handle format, pipeline,
  content-quality and reproduction questions outside this record comparison.
- Shared writers prepare accurate availability or citation text from the observed
  evidence; preserve the inspected version and access limitations in their brief.
- Return through the original invoking owner. Record verification does not
  initiate another release, a correction request or contact with repository staff.

## Checks

- The exact intended and observed versions are identified and comparable.
- Access claims name the tested viewer context; untested access is visible.
- The file comparison distinguishes listing, retrieved content and integrity evidence.
- Matches and discrepancies are traceable to inspected records or supplied materials.
- The conclusion is limited to the inspected scope and makes no reproduction claim.

## References

- OpenNeuro. (n.d.). *General policies*. https://docs.openneuro.org/policy/general.html
- OpenNeuro. (n.d.). *Data management plans*. https://docs.openneuro.org/policy/data_management_plans.html
- DANDI. (n.d.). *Publishing Dandisets*. https://docs.dandiarchive.org/user-guide-sharing/publishing-dandisets/
- Zenodo. (n.d.). *About records*. https://help.zenodo.org/docs/deposit/about-records/
