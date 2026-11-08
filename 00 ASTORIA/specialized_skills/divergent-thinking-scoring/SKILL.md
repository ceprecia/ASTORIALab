---
name: divergent-thinking-scoring
description: >-
  Compares and specifies one approved nonclinical divergent-thinking
  response-scoring plan, including fluency, flexibility, originality,
  elaboration, or semantic-distance measures, with explicit coding, reliability,
  blinding, confound, and claim boundaries. It does not choose the user's construct,
  score responses, generate categories, select thresholds, or interpret
  creativity in people. Triggers: score divergent thinking responses,
  originality and flexibility scoring plan.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: analysis
  modality: behavior
  dependencies: ""
  requires: ""
  gates: running on real data, accepting results
  created: "2026-07-24"
  updated: "2026-09-23"
---

# Divergent Thinking Scoring

Specify one response-coding and scoring plan without turning a creativity
label, rarity threshold, embedding distance, or rater agreement into a
universal construct measure.

## Purpose

This is the conditional Part 4 method owner for one approved nonclinical
divergent-thinking scoring estimand. It owns the scoring-dimension comparison,
response-validity and duplicate rules, category and originality-codebook
specification, rater-blinding and reliability plan, semantic-distance
measurement boundary, fluency-opportunity confound, reporting, and bounded
statistical handoff.

The user owns the construct, task, population, response eligibility, coding
decisions, scoring method, thresholds, confirmatory status, interpretation, and
claims. [experimental-design](../../skills/experimental-design/SKILL.md) owns the task and measurement design;
[cogsci-statistics](../cogsci-statistics/SKILL.md) owns inference and dependence.

Activate only for exact `divergent-thinking-scoring` or an approved handoff
with the task, response unit, construct, and estimand stated. Do not trigger
from `creativity`, `originality`, `fluency`, `semantic distance`, `AUT`, or a
generic scoring request.

In scope: a nonclinical divergent-thinking response pool such as an
Alternative Uses task, with a selected plan for fluency, flexibility,
originality, elaboration, subjective ratings, semantic distance, or a declared
combination. Out of scope: diagnosing creativity, intelligence, giftedness,
clinical or employment assessment, automatic scoring of people, protected
test content, and treating one score as a general creativity trait.

## Inputs

Obtain or mark missing:

| Field | Required content |
|---|---|
| Scientific contract | Construct, question, estimand, status, population, and permitted claim |
| Task and response unit | Prompt, administration, time, response format, participant and item grain |
| Eligibility rules | Duplicates, conventional uses, gibberish, irrelevant responses, partial responses, and missingness |
| Dimensions | Fluency, flexibility, originality, elaboration, semantic distance, or selected subset |
| Codebook | Category system, normalization, examples, coder training, versioning, and adjudication |
| Rater design | Number, independence, blinding, reliability statistic and model, and appeal rule |
| Automated route | Embedding model, preprocessing, language, phrase handling, distance definition, and validation |
| Opportunity confound | Fluency, response count, top-N, ratio, covariate, multilevel, or acknowledged limitation |
| Outcome contact | Whether codebook, exclusions, thresholds, or scoring changed after results were seen |

If task, construct, response unit, eligibility, scoring dimension, codebook,
or outcome-contact state is missing, return **divergent-thinking scoring
intake incomplete**. Do not invent categories, originality thresholds, or
semantic embeddings.

## Steps

### Gate 1: approve the scoring boundary

Show construct, task, response unit, eligibility rules, dimensions, codebook
options, rater and automation routes, opportunity confound, blinding,
reliability, outcome contact, alternatives, limitations, and statistical
handoff. Gate 1 authorizes method comparison only, not scoring or saving.

### Decision ledger

| Decision | Candidate routes | Assumptions and evidence | Consequences | The user selection |
|---|---|---|---|---|
| Valid response and duplicate rule | | | | |
| Scoring dimension | | | | |
| Category codebook | | | | |
| Originality method | | | | |
| Rater and reliability design | | | | |
| Semantic-distance model | | | | |
| Fluency opportunity control | | | | |
| Statistical handoff | | | | |

### Gate 2: approve one complete specification

Ask the user to select, revise, or reject all rows, blinding and reliability,
deviation handling, reporting, and the permitted claim. Gate 2 authorizes a
chat-based specification only, not coding, scoring, model downloads, fitting,
or file writes.

Return:

```text
Divergent Thinking Scoring Specification
Construct, question, estimand, and status:
Task, response unit, prompt, and population:
Valid-response, duplicate, and exclusion rules:
Dimensions and scoring definitions:
Category codebook and version:
Originality or rating method:
Rater training, blinding, adjudication, and reliability:
Semantic-distance model and validation boundary:
Fluency-opportunity confound route:
Statistical handoff and permitted claim:
Outcome contact, deviations, limitations, and stop point:
```

Stop after the specification and hand off implementation separately.

## Boundaries

Method rules:

- **Fluency:** define valid and distinct responses before counting. Preserve
  exclusions and unresolved duplicates. A higher count is not automatically
  better creativity.
- **Flexibility:** select and version a category system. Category assignment
  is a coding judgment; require training, independent coding, adjudication,
  and reliability appropriate to the claim. Do not prescribe one taxonomy or
  universal ICC cutoff.
- **Originality:** compare statistical rarity, subjective rating, or another
  selected route. Rarity depends on sample, norms, normalization, and pooling;
  a 5% rule is not universal. Ratings require anchors, blinding, calibration,
  reliability, and uncertainty.
- **Elaboration:** define what counts as an additional detail and protect
  against verbosity or response-length confounding.
- **Semantic distance:** record the exact embedding model, version, language,
  tokenization, prompt representation, phrase aggregation, distance, missing
  vector handling, and validation. Distance measures one representation, not
  usefulness, appropriateness, mechanism, or creativity as a whole. Do not
  download a web model or use a remote service without separate approval.
- **Fluency opportunity:** distinguish raw originality count from proportion,
  top-N, covariate, multilevel, or other route. The user selects the estimand;
  top-N is not a default.
- **Blinding and reliability:** keep condition and outcome information away
  from coding when feasible, record unavoidable unblinding, report rater
  agreement and its model, and do not turn reliability into validity.

Stop for clinical or person-level assessment; protected test content; missing
construct or response unit; outcome-selected categories or thresholds without
an exploratory label; unblinded coding without disclosure; unsupported
semantic model; automatic score interpretation; fixed reliability cutoffs;
remote model or data access; or a request to score, fit, or interpret results.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
