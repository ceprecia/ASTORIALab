---
name: coordinate-peer-review
description: 'Maps editor and reviewer requests to user decisions, required work,
  revised locations and responses for one manuscript decision. Coordinates a bounded
  revision without adopting scientific changes or submitting it. Triggers: map these
  reviewer requests, organize this resubmission response.'
metadata:
  level: skill
  system: Research Assistant System
  part: '5'
  family: support
  modality: any
  population: ''
  dependencies: ''
  requires: editor decision, reviewer comments, current manuscript and user decisions
  created: '2026-11-02'
  updated: '2026-11-02'
  gates: ''
---

# Coordinate Peer Review

Turn one editorial decision into traceable revision work and responses.

## Purpose

Coordinate the response to one manuscript decision, preserving the editor's
instructions, reviewers' requests, user choices and exact revised locations.
Connect requested changes to their appropriate scientific or writing owner.
A mapped request is not an adopted scientific change or a completed response.

## Inputs

- Complete editor decision and supplied reviewer comments, with their source.
- The submitted manuscript and actual revision files or analysis returns.
- Exact journal, article type, round and current revision instructions.
- User decisions already made, deadline if supplied and contributor roles.
- Invoking session, return owner and authorized scope of coordination.

## Steps

1. Establish the decision round and versions. Identify missing attachments or
   comments; preserve their absence rather than treating a partial letter
   as the complete review. Keep private correspondence within the supplied scope.
2. Read [current primary-source verification](../research-output-coordinator/references/source_verification.md)
   completely. Verify current journal revision requirements and the specific
   editorial instructions, including required files and any stated deadline.
3. Map every editor and reviewer point to a stable locator, preserving its
   wording and context. Connect overlapping requests without losing separate
   points, conflicting requests or the identity of their source.
4. Classify the work each point needs: clarification, evidence/citation,
   reporting, manuscript structure, technical correction, scientific
   interpretation, reanalysis, additional data or an editorial-process question.
   Do not infer the reviewer's motives.
5. Attach the user's existing decision and its rationale to each point.
   When a consequential decision is open, show the specific alternatives
   or question and continue independent items. A request from a reviewer
   does not itself authorize a scientific change.
6. Assign the bounded work to the appropriate existing owner. Scientific
   questions return to the research lead or critique/method owner; approved
   analyses go through their technical route. Shared writers prepare prose
   and response text from the supplied decisions and verified evidence.
7. Track dependencies between items. If a revised analysis changes a value,
   comparison or figure, identify the affected manuscript passages, displays,
   supplements and responses. Reuse unaffected work.
8. Collect actual returns and verify them against the point addressed.
   Record the revised location and supporting evidence. A proposed task,
   agent's assertion or response promising future work is not completion.
9. Reconcile each response with the current manuscript. Confirm that claimed
   changes exist, unchanged items have the user's stated explanation, and
   new caveats or scientific claims have not appeared only in the response.
10. Check the requested revision package against the current journal rules.
    Where clean and marked-up files are required, compare both against the
    same final content. Preserve superseded revision rounds as required by
    the established project layout.
11. Return coverage of the supplied decision, unresolved points, actual
    revision evidence and the next owner. Do not infer that addressing
    every request guarantees acceptance.

## Outputs

Return a compact response map with:

- Editor/reviewer locator and request.
- User decision or unresolved question.
- Assigned action and dependency.
- Actual revised location, supporting return and response status.

Include a package handoff list when requested, plus the shared contract's
source state for consequential requirements. Return the map in the current task's requested form or under the recipient's existing reporting policy. For an authorized save, follow me.md and the existing canonical project owner.

## Boundaries

- User decisions govern scientific changes, disagreements and new commitments.
- A disagreement can be documented without conceding the scientific point;
  do not silently implement provisional critique recommendations.
- This skill does not run analyses, rewrite the whole manuscript or operate
  a submission portal. Preparation remains distinct from resubmission.
- Preserve all supplied comments even when combining their implementation.
- Do not treat reviewer agreement, an editor's invitation or a checklist as
  evidence that the study's conclusions are valid.

## Handoffs

- Preserve the original session and return owner.
- Borrow shared writing capabilities for response and manuscript prose,
  reporting review for disclosure gaps and technical owners for approved analyses.
- Use [research-critique](../research-critique/SKILL.md) for
  requested scientific assessment of a disputed point.
- Pass the verified revision materials to
  [prepare-publication-package](../prepare-publication-package/SKILL.md)
  when package assembly is in scope.
- Keep grant-review and grant-resubmission requirements with Research Grant Advisor.

## Checks

- Every supplied point has a disposition, including unresolved or conflicting ones.
- Each claimed change is traceable to the actual inspected revision.
- Response wording and manuscript wording agree on the science and work completed.
- New results have their own technical evidence and affected locations identified.
- The return distinguishes drafted, checked, unresolved and submitted states.

## References

- University of Cambridge Libraries. (n.d.). *The submission process*. https://libguides.cam.ac.uk/writing-for-publication/submission-process
- PLOS. (n.d.). *Revising your manuscript: PLOS One*. https://journals.plos.org/plosone/s/revising-your-manuscript
- PLOS. (n.d.). *Editorial and peer review process: PLOS One*. https://journals.plos.org/plosone/s/editorial-and-peer-review-process
