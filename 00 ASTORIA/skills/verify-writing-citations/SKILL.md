---
name: verify-writing-citations
description: >-
  Verifies citation identities, bibliographic metadata and whether an accessible
  source supports the exact proposition attached to it. Use for citation and
  reference checks; existence alone is not evidential support and unavailable
  sources remain unverified. Triggers: verify these citations, check this
  bibliography.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: writing-coordinator
  created: "2026-11-01"
  updated: "2026-11-02"
---
# Verify Writing Citations

Check that the reference exists and supports the exact words it accompanies.

## Purpose

Own bibliographic identity, citation metadata, source access and precise
source-to-proposition matching. Keep these separate: an identifiable paper can
be cited for a finding it never reported. This role verifies citations without
taking over literature discovery, scientific interpretation or prose drafting.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md).
Use the current brief, relevant MOC and recipient-supplied writing guidance, bounded
draft, citation list or bibliography, exact clauses being supported and any
source files or identifiers. Preserve the selected citation style and document
format requirements.

## Local source access

When the citation brief identifies a local reference library, use its configured
read-only search before opening arbitrarily named PDFs. For Mendeley Reference
Manager on macOS, its conventional current-user locations are
`Library/Application Support/Mendeley Reference Manager/mrm/databases/*.db`
and `Library/Application Support/Mendeley Reference Manager/userfiles` under
The user's home directory. Verify the actual location and database schema;
these are optional source locations, not startup dependencies. Never scan
unrelated libraries or change the reference manager's files.

Use citation keys, title, DOI, author and year to identify a record. If the
verified schema provides `documents_fts` and `files_fts`, inspect those tables
read-only to match metadata and full-text snippets by `document_id`. UUID PDF
filenames alone do not identify an article. Read the relevant full passage;
metadata and snippets remain discovery aids. If unavailable, use the supplied
source or an authorized scholarly lookup and state the access limitation.

## Steps

1. Inventory the citations in the assigned passage and connect each to the
   exact proposition or clause. Split compound sentences when a citation
   supports only part of the sentence.
2. Resolve identity against the supplied source and a publisher, repository or
   authoritative bibliographic record as needed. Compare title, authors, year,
   venue and DOI or other identifier; do not trust plausible formatting.
3. Verify bibliographic fields individually. Never invent a missing DOI, page
   range, issue, date or author. Identify preprint versus published versions,
   corrections or retractions when the retrieved record indicates them.
4. Locate and read the source passage, table, figure or result that would
   support the proposition. Record its location and access level. Abstract
   access may verify an abstract claim but not unseen methods or results.
5. Compare the citation with the actual population, task, measure, comparison,
   effect direction, uncertainty and inference. Distinguish what the authors
   measured from what they hypothesized or discussed. Identify whether support
   comes from a measured result, a design description, a model demonstration or
   the authors’ interpretation. An assertion in a published abstract is not
   independent proof of its full scope. Cross-check relevant repeated methods
   descriptions; if they disagree, return a source conflict with both locators.
6. Classify separately: identity verified or unresolved; metadata verified or
   incomplete; proposition supported, partly supported, unsupported by the inspected
   source, contradicted, conflicting source accounts or unverified because the relevant source cannot be
   inspected. A failed lookup
   is not proof that a paper does not exist.
7. Reconcile citations with the reference list: missing entries, uncited
   entries when the requested style excludes them, duplicate versions,
   inconsistent author-year labels and misplaced citation clusters.
8. Return precise repairs. Correct verified metadata within scope. For a
   mismatched claim, identify the unsupported clause and any narrower wording
   the source licenses; do not replace the scientific position automatically.
9. After a writer changes a claim, recheck the affected citation relationship.
   A previous pass on different wording is not a pass on the new proposition.

## Outputs

For each material finding provide citation, exact claim, identity/access status,
support status, source locator and required repair. Supply a corrected
bibliography when requested. Keep unavailable sources visibly unverified;
never return an unqualified all-clear for an incompletely checked list.

## Boundaries

- Memory, citation-manager metadata and search snippets do not establish
  proposition-level support.
- A citation on a paragraph's last sentence does not automatically support
  every preceding statement.
- Do not substitute a review's citation for a primary result without explaining
  the evidence level.
- Use an available local reference library read-only through its current
  configured access; do not reorganize its files as part of verification.
- Follow `me.md` for writing profiles if producing formal replacement prose.

## Handoffs

Return findings through writing-coordinator. paper-search owns a bounded search
for missing literature; research-literacy owns substantive scientific claim
audits. Source conflicts follow
[cross-system handoffs](../writing-coordinator/references/cross_system_handoff.md).
The section writer repairs wording; integrate-writing applies the selected
reference format across the canonical document.

## Checks

- Every claim of verification has a retrievable source and precise scope.
- Bibliographic existence and evidential support remain distinct.
- Partial access, unsupported clauses and ambiguous records are disclosed.
- No repair adds unsourced metadata or strengthens the original claim.
