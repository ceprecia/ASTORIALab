---
name: prepare-research-release
description: 'Prepares one data, code or combined research release through repository
  selection, compendium assembly and deposit preparation modes. Borrows technical
  owners and keeps preparation distinct from reproduction and deposited-record verification.
  Triggers: assemble a research release, choose a repository for these materials.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: defined materials, intended audience/access and repository candidates
    or destination
  created: '2026-11-02'
  updated: '2026-11-02'
  gates: ''
---

# Prepare Research Release

Prepare a defined research output so its contents, destination and remaining work are clear.

## Purpose

Prepare one bounded data, code or combined release from the user's selected
scientific work. Keep the material selection, destination recommendation,
assembled package, reproduced result and observed repository record distinct.

Use the mode needed by the request:

| Mode | Bounded job |
| --- | --- |
| Repository selection | Compare appropriate destinations for defined materials and access needs. |
| Compendium assembly | Connect selected findings and outputs to their data, code, configurations, environment and documentation. |
| Data-deposit preparation | Match a selected dataset and its metadata to the chosen repository's current requirements. |
| Code-release preparation | Prepare an identified code version, dependencies, instructions and associated materials for its selected destination. |

Do not start every mode merely because one is requested. Source discovery,
data conversion, reproduction execution and public release retain their own owners.

## Inputs

- Requested mode, original invoking owner and the exact materials or outputs.
- Current project context, scientific decisions, source paths and selected versions.
- Intended audience and public, embargoed or controlled-access requirements.
- Designated destination or candidate repositories, if already identified.
- Existing inventories, execution records, documentation and reproduction evidence.
- Applicable institutional, funder, publisher, repository and contributor inputs;
  distinguish supplied confirmation from unknown ownership or sharing conditions.

Ask only for missing information that changes selection or preparation. Continue
independent inventory and source checks while a consequential choice remains open.

## Steps

1. Read [source verification](../research-output-coordinator/references/source_verification.md)
   and [repository candidates](../research-output-coordinator/references/repositories.md)
   completely before requirement-dependent advice. Reuse a complete read in the
   current task; recheck the selected destination's controlling sources as required.
2. Define the bounded output and current authorization. Identify the selected
   data/code versions, findings or displays, requested preparation and return owner.
   Establish whether the current task is planning or actual package assembly.
3. Inspect the relevant materials and existing inventory. Separate raw data,
   derivatives, statistical maps, code, environments, protocols, manuscript
   versions and supporting records. Record unresolved provenance or missing inputs.
4. Establish destination requirements from current primary sources. Check any
   designated repository before comparing alternatives. Use the shared reference's
   relevant selection criteria and source states; do not copy its policy table.
5. Perform the selected mode. For repository selection, explain fit, tradeoffs
   and unresolved conditions without treating a recommendation as the user's choice.
   For other modes, use the selected destination or label destination-dependent work.
6. Connect package contents to their purpose. Reuse the existing manifest or
   documentation where possible. Identify file locations, roles, versions,
   available integrity evidence and relationships to results or other releases.
   Do not invent completed verification or create another project hub.
7. Identify the exact technical work still needed. Send bounded BIDS curation,
   redaction, environment reconstruction, reproduction or artifact requests to
   their installed owners. Preserve current scientific choices and manual steps;
   a packaging request does not silently authorize those operations.
8. For compendia, map each selected output to its inputs and generation steps.
   For data deposits, prepare the applicable metadata, dictionaries and related
   resource links. For code releases, identify dependencies, entry points, paths,
   expected outputs and license choice or its unresolved status.
9. Assemble or revise only the authorized package surfaces. Preserve the source
   materials and established project layout. Compare the result with the selected
   inventory for omissions, broken references, mismatched versions and unsupported
   claims about access, permissions, availability or reproducibility.
10. Return the prepared result or plan, current source state, inspected scope,
    unresolved requirements and the next owner. If a repository record already
    exists, give its exact identifier/version to verify-repository-release rather
    than inferring that the prepared local package matches the deposited record.

## Outputs

Return only the fields needed for the selected mode:

- Materials and versions inspected, requested mode and original return owner.
- Candidate comparison or selected destination, with current primary-source state.
- Package or assembly plan, its existing content locations and result-to-input links.
- Documentation, metadata and technical work completed versus still required.
- Separate preparation, execution, reproduction and repository-verification evidence.
- Uninspected scope, unresolved choices and a concrete next action with its owner.

Return plans and checks in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization. For an authorized
artifact, follow me.md and the layout reference and use the existing owning
location. Reuse one package manifest or create one when needed for the requested
release; avoid automatic audit files and parallel release notes.

## Boundaries

- The user selects the scientific materials, destination, access, licensing and
  commitments; proposed options remain labeled until selected.
- Follow me.md for saving and external actions. Preparation does not imply
  conversion, redaction, pipeline execution, upload, deposit, contact or publication.
- A complete inventory, valid BIDS tree, reproducibility statement or DOI does
  not establish that the specified findings were reproduced.
- Preserve the original analysis environment and provenance. Do not upgrade a
  historical pipeline or replace a manual step to make a package appear complete.
- Missing institutional confirmation or inaccessible current policy stays
  unresolved; continue preparation that does not depend on that information.

## Handoffs

- bids-organizer owns implementation of an approved BIDS curation specification;
  redactor owns scoped redaction candidates and their inspection limitations.
- analysis-coordinator selects the appropriate technical owner for environment,
  execution and reproduction work; this skill collects its actual return.
- Shared writing and artifact skills prepare their requested text or deliverable
  from verified facts. Carry the current claim, unknowns and exact output scope.
- verify-repository-release inspects the actual record/version after preparation
  or deposit. Return all results through the original invoking owner.

## Checks

- The destination and material/access type match the inspected primary sources.
- Every reported package item and version exists within the inspected scope.
- Intended, prepared, executed, reproduced and deposited states remain separate.
- Missing files, conditions and permissions were not filled with assumptions.
- The result uses existing canonical locations and has one final file owner.

## References

- National Institutes of Health. (n.d.). *Selecting a data repository*. https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/selecting-a-data-repository
- Stanford Data Science. (n.d.). *Publication phase*. https://stanforddatascience.github.io/best-practices/publication-phase.html
- OpenNeuro. (n.d.). *General policies*. https://docs.openneuro.org/policy/general.html
- Zenodo. (n.d.). *About records*. https://help.zenodo.org/docs/deposit/about-records/
