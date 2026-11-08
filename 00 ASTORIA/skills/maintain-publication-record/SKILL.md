---
name: maintain-publication-record
description: 'Checks proofs and publication details against authoritative versions
  and maintains identifiers, related-output links and documented corrections. Returns
  localized record repairs without changing the scientific history. Triggers: check
  these publication proofs, reconcile publication versions.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: accepted/proof/published versions and identifiers within a defined comparison
  created: '2026-11-02'
  updated: '2026-11-02'
  gates: ''
---

# Maintain Publication Record

Compare exact publication versions and prepare traceable record corrections.

## Purpose

Review proofs against an identified accepted version, or reconcile one
published work's identifiers, metadata, versions and related outputs. Prepare
localized repairs while preserving the scientific history and the distinction
between a proposed correction and an official published update.

## Inputs

- Requested mode: proof comparison or publication-record reconciliation.
- Exact accepted, proof, published or corrected versions within the comparison.
- DOI or other identifiers, preprint and related data/code links when available.
- Publisher instructions or queries and the authoritative contributor metadata.
- Original return owner, permitted local edits and known scientific decisions.

## Steps

1. Bound the work to one publication and a named comparison. Identify each
   version by its source and available version information. Do not assume
   the newest local file is the accepted source or the version of record.
2. Read [current primary-source verification](../research-output-coordinator/references/source_verification.md)
   completely. Verify the relevant proof instructions, correction procedure,
   version/linking policy or other rule for the actual publisher and stage.
3. Establish the version chain from available evidence: submitted, accepted,
   proof, published, corrected and preprint versions as relevant. Resolve
   the publication identifier to its official record and note missing links
   or conflicting metadata without inventing a relationship.
4. For proof comparison, inspect the text and the rendered material needed
   to assess tables, figures, equations, symbols, captions, references and
   layout. Use artifact owners for unsupported formats. Identify uninspected
   visual or embedded surfaces instead of declaring the whole proof checked.
5. Compare scientific values, signs, units, labels and stated results against
   the accepted material and supplied technical evidence. Separate production
   changes, accepted scientific content and proposed new content. Route a
   result discrepancy to its technical or scientific owner.
6. Reconcile names, affiliations, identifiers, contribution/funding statements
   and availability links against contributor records and current verified
   releases. An accessible landing page alone does not prove the described
   version, access state or content is correct.
7. Record each discrepancy with a precise location, expected content,
   observed content, authoritative basis, consequence and proposed repair.
   Preserve unresolved scientific decisions; do not present them as typos.
8. Prepare a proof-query list or correction request in the required format
   through the appropriate writing/artifact owner. Include the affected
   version and supporting material. Follow me.md for any requested local
   edits; do not alter the publisher's record as part of preparation.
9. For an existing correction or update, inspect the official notice and its
   relationship to the article. Report whether it is proposed, acknowledged,
   issued or incorporated based on observed evidence. Distinguish a linked
   notice from a replacement article file.
10. Reinspect authorized local repairs and verify identifiers and links in
    the bounded record. Return unresolved discrepancies and the next owner;
    keep publication, correction and preservation states separate.

## Outputs

Return a proof-query or publication-record discrepancy list with exact
locations, inspected versions, evidence and proposed or completed local repairs.
Include source state where policy matters, related-output link findings and
the specific uninspected scope.

Report checks in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization. Preserve canonical
source files and the owning project's established layout.

## Boundaries

- User and technical owners retain scientific interpretations and corrections.
- A proof review does not reopen the study's findings or change authorship.
- Proposed correction text is not an issued publisher correction.
- Do not overwrite a version of record, remove historical evidence or
  silently merge accepted content with new scientific results.
- This skill prepares and verifies local material; publisher correspondence,
  proof submission and public record changes follow their separate authorization.

## Handoffs

- Preserve the invoking session and return owner.
- Borrow shared writers for requested correction prose, artifact owners for
  rendering and [verify-writing-citations](../verify-writing-citations/SKILL.md)
  for citation-identity questions.
- Use [verify-research-outputs](../verify-research-outputs/SKILL.md)
  for result/provenance comparisons and
  [verify-repository-release](../verify-repository-release/SKILL.md)
  for related repository versions and access.
- Return an unselected scientific change to the research lead rather than
  quietly treating it as a production fix.

## Checks

- Every reported difference identifies its location and exact version pair.
- Expected values and metadata have an identified authoritative source.
- Visual/embedded material is checked or explicitly left uninspected.
- Proposed, locally repaired and officially issued changes remain distinct.
- Linked identifiers and correction relationships reflect observed records.

## References

- PLOS. (n.d.). *Accepted manuscripts: PLOS One*. https://journals.plos.org/plosone/s/accepted-manuscripts
- PLOS. (n.d.). *Editorial notes, corrections, expressions of concern, and retractions: PLOS One*. https://journals.plos.org/plosone/s/corrections-expressions-of-concern-and-retractions
