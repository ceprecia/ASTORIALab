# Repository candidates and primary sources

Use this reference for repository selection, release preparation and deposited-record verification. Read [source verification](source_verification.md) first. This is a source-finding catalog, not blanket approval or a permanently current requirements matrix. Verify the chosen repository's controlling policies and any designated funder/institutional destination for the actual project.

## Select for the material and intended use

Start with any applicable designated repository requirement, then consider a suitable discipline-specific repository, followed by an institutional or general repository. Keep data, statistical maps, code releases, manuscript versions, registrations and collaborative workspaces distinct.

For the candidates actually compared, establish accepted materials/formats; eligibility; permitted public, embargoed or controlled access; licenses and relevant permissions; metadata/documentation; identifier and version behavior; reviewer access; curation; persistence/retention; current costs/capacity; and links to associated outputs. Do not fill these fields from a generic directory entry. Omit irrelevant fields rather than imposing every criterion on every deposit.

## Initial candidate list

The source observations below were checked on **2026-11-02**. They are a dated starting point; live rechecking under the source-verification contract is required for operational advice.

| Candidate | Material fit and identifier/version considerations | Important scope or access question | Primary sources |
| --- | --- | --- | --- |
| OpenNeuro | BIDS neuroimaging data; accession and DOI-backed dataset versions/snapshots | Its general policy v1.0.0, updated 2026-10-13, specifies CC0 and eventual public release. Temporary embargo is not indefinite controlled access. Unsnapshotted edits are not guaranteed to persist; preservation does not certify usability or reproduction. | [General policies](https://docs.openneuro.org/policy/general.html); [identifiers and access](https://docs.openneuro.org/policy/data_management_plans.html) |
| DANDI | Cellular neurophysiology, electrophysiology, optophysiology and associated behavioral/image materials; Dandiset identifiers and published versions | Check the accepted standards and asset-specific publication requirements for the proposed material. Verify public/embargo behavior and version citation at the time of use. | [Scope](https://docs.dandiarchive.org/introduction/); [publishing](https://docs.dandiarchive.org/user-guide-sharing/publishing-dandisets/); [citation](https://docs.dandiarchive.org/user-guide-using/citing-dandisets/) |
| NeuroVault | Statistical brain maps, parcellations and atlases; map/collection URLs | Check supported spaces/formats and public/private-link behavior. A linked article DOI must not be described as a newly minted dataset DOI. This is not the default home for a complete raw neuroimaging dataset. | [Official FAQ](https://neurovault.org/FAQ) |
| Zenodo | General research objects and archived software releases; DOI records and separately identified versions | Check file-access settings, public metadata, licensing and version-specific citation. Bit preservation is not a guarantee that a computational environment will remain executable. | [Record documentation](https://help.zenodo.org/docs/deposit/about-records/) |
| Harvard Dataverse | Research datasets, supporting documentation and code; dataset identifiers and version history | Rules can differ by Dataverse installation. Restricted-file capability alone does not establish suitability for sensitive identifiable material. | [Harvard terms](https://support.dataverse.harvard.edu/harvard-dataverse-general-terms-use); [dataset versions](https://guides.dataverse.org/en/latest/user/dataset-management.html#dataset-versions) |
| Dryad | Curated openly shareable research data and published revisions; software can be associated through Zenodo | Check current scope, curation, timing, charges and CC0 terms. Do not assume its open-data model supports a continuing controlled-access requirement. | [Mission and scope](https://datadryad.org/mission); [publication guidance](https://datadryad.org/help/guides/publication) |
| OSF Registrations / Preprints | Registrations, study plans and preprints, with linked outputs | The transition notice, updated 2026-11-02, changes Projects: no new Projects/Components after 2026-11-16 and existing Projects read-only on 2027-02-19. Registrations and Preprints continue. Do not repeat older general-workspace recommendations without rechecking this transition. | [Transition notice](https://help.osf.io/article/759-details-of-osf-projects-transition); [registrations](https://help.osf.io/article/330-welcome-to-registrations) |
| NIMH Data Archive | Human-participant mental-health, behavioral, imaging, genomic and associated materials in applicable programs | Its role is confirmed by NIMH's official guidance. Detailed current submission/access terms were not fully retrievable in the initial check and remain **unverified**. Obtain them before operational recommendations; do not substitute the older terms PDF or a search snippet. | [NIMH guidance](https://www.nimh.nih.gov/funding/managing-your-grant/nimh-data-management-and-sharing-for-applicants-and-awardees); [archive](https://nda.nih.gov/) |
| dbGaP | Human genomic and associated phenotypic data; study accessions and versions | Verify genomic scope, study registration, controlled-access requirements and current onboarding instructions. Do not treat it as a general behavioral-data repository. | [Current submission guide](https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/) |

The OSF notice contains an inconsistent isolated API year while its main transition schedule repeatedly specifies 2027-02-19 for read-only Projects. Record that conflict if API timing matters; do not silently repair it or claim API-specific timing verified.

## Discovery directories and manuscript destinations

- [NIH repository directory](https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/scientific): identify candidate or designated repositories, then inspect the repository-owner policy. A generalist listing can lag a provider's service notice.
- [NIH selection guidance](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/selecting-a-data-repository): use applicable selection and human-data considerations.
- [re3data](https://www.re3data.org/about): discover repositories by material/discipline and profile; verify owner documentation before use.
- [FAIRsharing](https://fairsharing.gitbook.io/fairsharing): discover related repositories, standards and policies; a listing is not an operational compliance determination.

## Return the actual selection or deposit evidence

For selection, give the material and intended use, candidates considered, source state, tradeoffs, designated requirements, unresolved information and the user's selected destination if supplied. Do not label a recommendation as a selection already made.

For verification, identify the exact repository record/version, observed files or manifest comparison, metadata, identifiers and related-output links, access level actually tested, and any fields inaccessible to the reviewer. Separate an observed draft, a published record, an embargoed version, a prepared package and a verified computational result.
