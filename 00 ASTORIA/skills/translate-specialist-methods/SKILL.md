---
name: translate-specialist-methods
description: >-
  Translates source-backed specialist procedures, configurations and technical
  reasoning into accurate material for a methods writer. Use for detailed
  technical writing across domains; specialist owners retain technical decisions
  and review the translation's fidelity. Triggers: translate specialist records
  into methods, explain these technical methods for readers.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: writing-coordinator
  created: "2026-11-01"
  updated: "2026-11-02"
---
# Translate Specialist Methods

Carry detailed technical knowledge into writing without changing what was done.

## Purpose

Turn an existing specialist's technical record into accurate material for a
methods writer or technical explanation. Work across engineering, analysis and
other specialized domains by preserving their owners, terms and evidence.
Translation does not authorize selecting methods, executing analyses or
altering a design.

## Inputs

Read the [writing contract](../writing-coordinator/references/writing_contract.md)
and [cross-system handoffs](../writing-coordinator/references/cross_system_handoff.md).
Use the current brief, relevant MOC and recipient-supplied writing guidance, target
audience, section job, exact source revision and responsible technical owner.
Obtain the actual procedure, configuration, outputs and unresolved choices,
not a general description of what the software or device usually does.

## Steps

1. Identify the established domain companion, coordinator and specialist for
   the requested facts. Preserve that return owner; do not assemble a competing
   analysis or engineering team inside the writing assignment.
2. Request or inspect the bounded technical return: source locations and
   versions; what was planned and what was executed; inputs; ordered operations;
   parameters with units; outputs; rationale; checks; limitations; open choices.
3. Separate evidence states explicitly. Planned, executed, technically checked,
   human-reviewed, accepted and unknown are different. Use the status supported
   by the source, not the confidence of the specialist's prose.
4. Translate the record into reader-facing statements in its actual operational
   order. Retain exact names, labels, values, units, interfaces and distinctions
   needed to reconstruct or understand the method. For each consequential
   metric, name the measured events or quantities, the reference/target and
   what a larger or smaller value means. Distinguish resolution, accuracy,
   precision, latency and uncertainty when they appear together; shared units
   do not establish shared meaning.
5. Explain technical rationale only when it is established by the specialist,
   source or user. A plausible mechanism is not a documented reason.
   Distinguish procedure from the inference it enables.
6. For analysis software, use the actual version, command/configuration and
   report for the relevant run. Do not insert remembered defaults. Keep
   preprocessing, confound selection, statistical fitting and image QC separate.
7. For circuits or mechanisms, preserve component identity, revision, signal
   or power path, operating domain, calibration and test conditions as needed.
   Distinguish simulated predictions, ratings and bench measurements.
8. Map each translated statement to its source and flag missing details.
   Ask the technical owner a precise question that the record can answer.
   Escalate a consequential unresolved choice through its existing owner.
9. Return the translated account to that specialist for a technical fidelity
   check when the translation changes the technical presentation. Record what
   was reviewed and what remains unverified.
10. Deliver methods-ready material and a compact unresolved list to the writer.
    Maintain the link between any revised statement and its supporting record.

## Outputs

A bounded methods content packet or requested technical prose, with exact
source/version, procedure, parameters, rationale, status and missing items.
Keep citation/support notes separate from clean prose. Apply the writing
profiles required by `me.md` when producing formal scientific prose.

## Boundaries

- Do not replace a specialist's detailed return with generic textbook language.
- Do not infer that successful software execution proves acceptable QC.
- Do not describe a circuit as validated from compilation, simulation or a
  component datasheet alone.
- Do not add missing settings, measurements, exclusions or acceptance decisions.
- A technical reviewer checks fidelity; the user retains unresolved domain choices.

## Handoffs

writing-coordinator requests and collects the translation through the existing
technical owner. write-methods turns the supported material into the selected
section structure. verify-writing-citations checks source-dependent attribution;
check-writing-substance checks retained specificity; integrate-writing preserves
technical meaning across the document.

## Checks

- Every quantitative or procedural statement maps to the actual source revision.
- All meaningful status distinctions survive the translation.
- The technical reviewer sees the revised account, not only the original notes.
- The reader can identify inputs, operations, outputs and relevant limitations.
