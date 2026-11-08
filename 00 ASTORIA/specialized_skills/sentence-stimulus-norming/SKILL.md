---
name: sentence-stimulus-norming
description: >-
  Creates or curates an overcomplete pool of condition-linked sentence
  candidates and specifies one bounded human norming plan for one user-approved
  manipulation, factor structure, task or modality, target language or variety,
  population, and generalization target, then produces a selection-bound
  Sentence Stimulus and Norming Specification after two approval gates. Use when
  the request, or a part coordinator, hands over an explicitly matching
  sentence-stimulus question. Triggers: norm my sentence stimuli, build a
  sentence stimulus pool.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: design
  modality: behavior
  dependencies: ""
  requires: ""
  gates: finalizing the design, preregistering
  created: "2026-07-23"
  updated: "2026-09-23"
---

# Sentence Stimulus Norming

Create or curate one bounded sentence-stimulus pool and specify its human
norming logic without treating linguistic controls, rating constructs, or
matching thresholds as universal recipes.

## Purpose

It makes intended changes, invariants, residual differences, cloze or expectancy, entropy, plausibility, naturalness, acceptability, grammaticality, familiarity, coding, population, rights, version, and precision assumptions visible without generating a hypothesis, choosing a paradigm, recruiting or collecting, calculating sample size, analyzing raw data, treating AI ratings as human norms, making a scientific conclusion, or saving without separate approval.

`sentence-stimulus-norming` is the conditional Part 3 owner for one
already-approved sentence manipulation and task context.

It owns:

- creation or curation of an overcomplete pool of condition-linked sentence
  variants;
- an item-by-condition control and provenance matrix;
- construct-specific norming options;
- prompt, anchor, presentation, coding, denominator, and version rules;
- a selection-bound Sentence Stimulus and Norming Specification;
- a versioned selection or revision ledger when independently collected,
  aggregate human norm summaries and preapproved decision rules are supplied.

It does not choose the research question, hypothesis, manipulation, paradigm,
factor structure, list allocation, modality, population, sample size, data
collection system, raw-data model, or scientific interpretation.

Activate only when:

- The user invokes the exact trigger `sentence-stimulus-norming`; or
- a verified Active capability hands off an explicit sentence-stimulus
  creation, curation, control, or norming question with the owner-level design
  already approved.

Do not activate from `language task`, `make stimuli`, `norm words`, `reading
experiment`, `cloze`, `acceptability`, `analyze ratings`, or `Latin square`.

Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) when the task or manipulation remains
undecided. Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, lists,
and general counterbalancing. Use [self-paced-reading-designer](../self-paced-reading-designer/SKILL.md) for reveal,
segmentation, spillover, response, and comprehension flow. Use
[eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) for EEG event and marker compatibility.

This skill supports sentence-level stimuli and norming for an already-selected
behavioral, reading, auditory, or EEG-compatible task context.

It excludes:

- isolated word, image, face, sound, or non-sentence stimulus ownership;
- general paradigm choice and hypothesis generation;
- survey deployment, ethics approval, recruitment, consent, compensation, and
  human-data collection;
- rater, item, list, or trial-count calculation;
- raw norm-data cleaning, modeling, inference, or main-study analysis;
- automatic corpus downloads, database installation, or external AI upload.

If the final modality is auditory, the specification must include recording,
speaker, prosody, duration, and audio-rights requirements for a later owner. It
does not synthesize or record the stimuli.

## Inputs

Handle one manipulation and item family at a time.

| Field | Required content |
|---|---|
| Approved construct | user-supplied construct, hypothesis boundary, and intended inference |
| Design | Approved factors, conditions, manipulation, invariants, contrast, critical region, and use context |
| Task and modality | Selected behavioral, reading, auditory, or EEG context |
| Population | Target language, variety, age, proficiency, culture, literacy, clinical, and accessibility context |
| Item state | Source sentences, licensed materials, or permission to create labeled candidates |
| Generalization | Intended item, language, population, and task domain |
| Norming need | Candidate constructs and purpose of each control or selection step |
| Stop point | Candidate pool, specification, aggregate-summary ledger, or separately approved handoff |

If the manipulation, conditions, task or modality, language, population, or
generalization target is absent, identify the missing owner-level decision and
stop.

## Steps

### 1. Establish the sentence-design boundary

Restate the approved construct, manipulation, conditions, invariants, task,
modality, language, population, generalization, item state, rights, intended
norming role, exclusions, and unresolved choices.

### 2. Gate 1: approve sources and candidate generation

Present:

1. approved manipulation and item architecture;
2. exact sources, corpus or database proposals, and rights state;
3. candidate creation or curation scope;
4. control and norming constructs to compare;
5. fixed owner-level decisions and unresolved choices;
6. privacy, ethics, collection, power, and analysis exclusions.

Gate 1 authorizes only the displayed source review and candidate drafting. It
does not authorize a new hypothesis, paradigm, copyrighted asset use, external
AI upload, human recruitment or collection, sample size, raw-data analysis,
deployment, or saving.

Reopen Gate 1 after a material manipulation, language, population, modality,
source, asset, or norming-construct change.

### 3. Create or curate the overcomplete pool

For each linked item family, record:

- item and version identifiers;
- condition-specific sentence;
- intended manipulated element;
- intended invariants;
- residual differences;
- critical and downstream material when supplied by the task owner;
- source, license, attribution, modification, and redistribution state;
- sensitivity, offensiveness, ambiguity, accessibility, and cultural flags;
- status: candidate, revise, blocked, or ready for norming specification.

Do not select the final set.

### 4. Build the Item and Control Matrix

| Item family | Intended change | Invariants | Residual differences | Task consequence | Norm needed | Rights |
|---|---|---|---|---|---|---|
| | | | | | | |

Unmatchable residuals stay visible. Do not repair them automatically with a
later covariate.

### 5. Build the Norming Route Matrix

| Construct | Purpose | Prompt and anchors | Population and modality | Scoring meaning | Does not establish |
|---|---|---|---|---|---|
| | | | | | |

Remove inapplicable constructs. Do not combine distinct constructs into a
single score without an approved measurement model.

### 6. Build the Coding and Denominator Plan

For completion tasks, specify context, response count, tokenization,
orthography, morphology, diacritics, clitics, multiword responses, synonyms,
response collapsing, adjudication, invalid and missing responses, denominator,
target probability, alternative distribution, entropy, and preserved raw
fields.

For ratings, specify item presentation, instructions, anchors, orientation,
practice, order, filler purpose, response balance, missing and invalid
responses, and interpretation.

### 7. Build the Threat, Rights, and Revision Register

At minimum assess:

- construct conflation;
- item and condition nonindependence;
- residual lexical, syntactic, semantic, discourse, or prosodic differences;
- normer and target-population mismatch;
- language, variety, script, proficiency, age, literacy, and clinical mismatch;
- prompt, scale, context, order, filler, and exposure effects;
- ambiguity, coder disagreement, list composition, and version exposure;
- item and rater sampling uncertainty;
- false matching from a nonsignificant test;
- corpus, database, platform, and AI proxy misuse;
- sensitive free text and external-service privacy;
- copyrighted or restricted stimuli and norms;
- version drift and post-norm revisions;
- selection on observed outcomes and confirmatory contamination.

For each threat, show evidence, consequence, possible control, residual risk,
and the user's retained decision.

### 8. Gate 2: select the specification

Present the candidate pool, control matrix, norming routes, coding plan,
threats, rights, proposed precollection decision rules, revision behavior,
limitations, and handoffs.

The user selects candidate families, control priorities, norming constructs,
prompts and anchors, target normer population, coding and denominator rules,
precollection selection or revision rules, rights boundary, unresolved items,
and next stop.

Gate 2 authorizes only the Sentence Stimulus and Norming Specification. It does
not authorize recruitment, collection, sample size, survey deployment,
participant data, raw-data analysis, final-item selection from unreviewed data,
main-study revision, or saving.

### 9. Produce the Sentence Stimulus and Norming Specification

Return:

1. approved construct, manipulation, conditions, task, modality, and
   population;
2. source, language, item, version, and rights states;
3. overcomplete linked candidate pool;
4. item and control matrix;
5. selected norming constructs and their distinct roles;
6. prompt, anchors, presentation, order, filler, and exposure plan;
7. coding, denominator, distribution, and missingness rules;
8. population, precision, ethics, privacy, and collection requirements;
9. precollection selection, revision, re-norming, and deviation rules;
10. assumptions, unknowns, exclusions, and residual risks;
11. user-selected choices and rejected routes;
12. separately approved handoff or explicit stop.

### 10. Optional aggregate-summary ledger

Only when independently collected aggregate human norm summaries, the exact
sentence versions, provenance, and Gate-2-approved rules are supplied:

- verify version and rule match;
- apply the rules mechanically;
- preserve uncertainty and the full reported distribution;
- record keep, revise, block, and unresolved statuses;
- mark every changed item as requiring re-norming;
- stop on a new rule, construct, threshold, or participant-level record.

This is not raw-data analysis and does not authorize a scientific conclusion.

### 11. Verify and stop

Verify:

- one exact trigger, one owner, zero dependencies, and zero plugins;
- owner-level scientific and task decisions were supplied;
- candidate and final stimulus states remain distinct;
- human, corpus, and AI evidence remain distinct;
- every norming construct has a separate meaning;
- cloze coding preserves alternatives and denominators;
- no universal threshold or database default was inherited;
- nonsignificance is not called equivalence;
- edits invalidate or qualify prior norms;
- rights, privacy, and population applicability remain visible;
- both gates bound their authorization;
- no recruitment, collection, raw analysis, or scientific conclusion occurred.

Report `verified`, `verified with caveats`, or `blocked`, then stop. Saving and
handoff require separate approval.

## Boundaries

The user owns the question, hypothesis, manipulation, conditions, task, modality,
population, language or variety, intended contrast, confirmatory status,
construct-specific norming choices, selection rules, revisions, and final
stimulus set.

This skill:

- treats AI- or LLM-generated sentences as labeled candidates only;
- never treats AI ratings as human norms;
- never uploads unpublished, protected, sensitive, or participant-authored
  text to an external AI or service without explicit approval;
- never copies copyrighted stimulus sets, norms, corpora, tables, or test
  materials;
- records source, version, license, attribution, modification, and
  redistribution state for every candidate and resource;
- stops when asset rights, ethical authority, or population applicability is
  unresolved.

Free-text norming can produce sensitive or offensive material. Collection
requires separate ethics, consent, privacy, moderation, and data-governance
authority.

Keep these constructs separate:

- target cloze probability or expectancy;
- the distribution and entropy of alternative completions;
- plausibility;
- naturalness;
- acceptability;
- grammaticality judgment;
- familiarity or association;
- lexical meaning dominance and intended full-sentence interpretation when ambiguity is relevant;
- lexical, morphological, syntactic, semantic, discourse, and prosodic
  controls.

For every proposed norm or control:

1. define the construct and its role in the intended contrast;
2. record source, version, language, population, task, modality, and
   applicability;
3. specify prompt, anchors, scoring, interpretation, and invalid-response rule;
4. label it `direct evidence`, `bounded adaptation`, `design-derived`,
   `candidate for pilot`, or `unknown`;
5. preserve residual differences and conflicting evidence;
6. distinguish human norms from corpus metadata and AI judgments;
7. route rater and item precision to the power owner.

No universal rater count, item count, rating scale, duration, filler ratio,
catch-trial rate, exclusion rule, pilot size, cloze bin, matching threshold,
platform, pay rate, laboratory preference, effect size, or database is a
default.

Edge cases:

- **Only a broad language paradigm is supplied:** route to the paradigm owner.
- **Only isolated words are supplied:** route to a future lexical-stimulus
  owner.
- **Zero cloze but high plausibility:** preserve the distinct constructs.
- **Same target cloze but different entropy:** preserve alternative
  distributions.
- **Ambiguity coding collapses uncertainty:** retain meaning dominance, intended
  interpretation, `other`, `unclear`, and coder disagreement.
- **Multiple versions reach one rater:** enforce the approved list rule;
  shuffling does not repair a structurally imbalanced list.
- **A nonsignificant difference is called matching:** require an approved
  equivalence bound and method.
- **Items are edited after norming:** version and re-norm or mark unverified.
- **Dialect, age, L2, clinical, or modality mismatch:** block unqualified
  transfer.
- **Non-space, right-to-left, clitic, diacritic, or multiword response:** use
  an explicit language-specific coding plan.
- **AI sentences or ratings are proposed:** candidates only; ratings are not
  human norms.
- **A missing corpus value is set to zero:** restore missingness and verify coverage.
- **Sensitive or offensive free text appears:** stop for privacy and moderation
  authority.
- **No viable items remain:** return a blocked specification.
- **Items are revised after outcome inspection:** record an exploratory
  deviation and do not preserve confirmatory status silently.

This skill cannot establish grammatical truth, population validity, norm
precision, equivalence, or causal interpretation without appropriate evidence.
It cannot recruit, collect, analyze raw participant data, or guarantee that
later task implementation preserves the selected stimuli.

## Item controls and norming decisions

Tie the creation or curation route to the construct on the Construct Card
and the controls in the Item and Control Matrix. Use the Norming Route
Matrix and Coding Plan to show how prompts, coding, and selection rules
serve the chosen norming construct. Surface rights restrictions and
validity risks through the Rights Register and Threat Register. Compare
only evidence-compatible choices when an item or norming decision remains
open. Explain why a sole defensible route fits.

After Gate 2, record only the user's selections in the Sentence Stimulus and
Norming Specification. Apply only preapproved rules to independently
collected aggregate summaries, within the optional ledger's source and
version checks.

> [!info] References
> Read `./references/design_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- Use [cognitive-paradigm-design](../cognitive-paradigm-design/SKILL.md) for task and manipulation architecture.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) for factors, units, allocation, and list design.
- Use [self-paced-reading-designer](../self-paced-reading-designer/SKILL.md) for visual SPR administration.
- Use [eeg-paradigm-designer](../eeg-paradigm-designer/SKILL.md) for EEG event and marker compatibility.
- Use [cogsci-power-analysis](../cogsci-power-analysis/SKILL.md) and [statistical-power](../../skills/statistical-power/SKILL.md) for rater, item,
  participant, trial, and precision planning.
- Route raw norm-data cleaning, modeling, equivalence analysis, and inference
  to the later analysis owner.

Never chain automatically.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- Armstrong et al. (2012). https://doi.org/10.3758/s13428-012-0199-8
- Brysbaert & New. (2009). https://doi.org/10.3758/BRM.41.4.977
- Frade et al. (2024). https://doi.org/10.3758/s13428-023-02196-0
- Keating & Jegerski. (2015). https://doi.org/10.1017/S0272263114000187
- Lakens et al. (2018). https://doi.org/10.1177/2515245918770963
- Langsford et al. (2018). https://doi.org/10.5334/gjgl.396
- Matsuki et al. (2011). https://doi.org/10.1037/a0022964
- Peelle et al. (2020). https://doi.org/10.3758/s13428-020-01351-1
- Schütze. (2016). https://doi.org/10.17169/langsci.b89.100
- Westfall, J., Kenny, D. A., & Judd, C. M. (2014). Statistical power and optimal design in experiments in which samples of participants respond to samples of stimuli. *Journal of Experimental Psychology: General, 143*(5). https://doi.org/10.1037/xge0000014
