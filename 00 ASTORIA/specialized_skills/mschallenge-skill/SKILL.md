---
name: mschallenge-skill
description: >-
  Evaluates whether one exact ISBI 2015 Longitudinal Multiple Sclerosis Lesion
  Segmentation Challenge training or test product, subject and scan-timepoint
  grain, MRI modality, original or preprocessed image state, reference-mask
  state, or authorized challenge use can support one user-supplied research
  design and produces a selection-bound Dataset Suitability and Access
  Specification. Use when the request, or a part coordinator, hands over an
  explicitly matching MS Challenge question. Triggers: can the MS lesion
  challenge support my study, MS lesion segmentation dataset selection.
metadata:
  level: skill
  system: Research Assistant System
  part: "3"
  family: datasets
  modality: smri
  population: clinical
  dependencies: ""
  requires: challenge data access
  gates: downloading data, agreeing to data-use terms, selecting participants
  created: "2026-07-23"
  updated: "2026-09-23"
---

# MS Challenge Dataset Suitability

Evaluate one exact challenge evidence state without converting a
purpose-restricted benchmark into a general MS imaging dataset.

## Purpose

It treats the bundled license version 1.0 as controlling even when direct archive links are visible, defaults to metadata-only suitability unless written custodian authorization or registered challenge-participation authority is verified, preserves the 21 training and 61 test scan-timepoints, and maps modality, resolution, preprocessing, reference, subtype, access, and governance limits after two approval gates. It does not download data, interpret link visibility as permission, enable ordinary reuse, use data clinically, redistribute data or derivatives, inspect images, select subjects, preprocess, segment lesions, analyze data, submit a challenge entry, upload to a leaderboard, make scientific or clinical claims, search broadly, or save without separate approval.

`mschallenge-skill` is the conditional Part 3 owner for one bounded
prospective suitability and access question about the ISBI 2015 Longitudinal
MS Lesion Segmentation Challenge.

It pins the training or test product, subject and scan-timepoint grain,
modality, native or preprocessed state, reference-mask state, approximate
timing, subtype evidence, access route, and authority state; compares only
credible metadata-level routes; and produces one user-selected Dataset
Suitability and Access Specification.

It does not own scientific or analytic decisions. It never downloads data,
opens images, authenticates, accepts terms, selects subjects, transforms
files, preprocesses, segments, analyzes, redistributes, shares derivatives,
submits results, or uploads to a leaderboard.

Activate only when:

- The user invokes the exact trigger `mschallenge-skill`; or
- a verified Active capability hands off one explicit ISBI 2015 MS Challenge
  suitability or access-planning question.

Do not activate from `MS lesion`, `multiple sclerosis MRI`, `lesion
segmentation`, `ISBI`, `download MS Challenge`, `benchmark this model`, or
`analyze MS lesions`.

Use [experimental-design](../../skills/experimental-design/SKILL.md) when the longitudinal, reference-standard,
evaluation, or comparison structure must be designed. Offer [paper-search](../../skills/paper-search/SKILL.md)
only for a separately approved bounded search about lesion measurement,
benchmark interpretation, or prior evidence.

## Inputs

Handle one bounded scientific question at a time.

| Field | Required content |
|---|---|
| Scientific target and estimand | user-supplied question or design; comparison, unit, and timing |
| Product boundary | Training, test, original, preprocessed, mask, or an unresolved product choice |
| Longitudinal boundary | Subject, scan-timepoint, interval, change target, and dependence |
| Data requirements | T1w, T2w, PDw, FLAIR, original, preprocessed, or reference need |
| Authority boundary | Metadata only, written custodian authorization, or registered challenge participation |
| Stop point | Chat-only evidence card, specification, or separately approved handoff |

If the scientific target is absent, ask:

> What one design requirement should the ISBI 2015 MS Challenge be evaluated against?

Then stop.

## Steps

### 1. Build the MS Challenge Fit Brief

Return the exact target and estimand; training or test product; subject,
scan-timepoint, modality, resolution, image-state, reference, and timing
requirements; authority state; license, access, evaluation, and governance
constraints; known conflicts and unknowns; and the requested stop point.

If the request is really a download, account action, image inspection,
participant selection, preprocessing, segmentation, analysis, redistribution,
derivative sharing, submission, or leaderboard upload, stop and route it
outside this skill.

### 2. Gate 1: approve the inspection boundary

Before network or local metadata inspection, show:

- exact license member, official page, archive directory metadata, paper
  section, or supplied authority document to inspect;
- any account, credential, controlled file, protected path, terms, or
  custodian boundary;
- product, count, timepoint, modality, resolution, processing, reference,
  access, and license facts to verify;
- the stop point before imaging payloads, credentials, downloads, writes,
  submissions, search expansion, or handoffs.

Ask:

> Approve this exact MS Challenge license and metadata inspection boundary?

Gate 1 authorizes only the displayed read-only inspection. It does not
authorize an account, credential, terms acceptance, challenge registration,
download, image inspection, analysis, submission, saving, or another
capability.

### 3. Pin the exact license, product, and authority state

Record the license version, date, hash, owner, purpose restriction, team and
redistribution rule; training or test identity; official page revision and
archive metadata date; subject and scan-timepoint grains; modalities and
native resolutions; original and preprocessed products; reference-mask state;
access route; supplied authority; conflicts, unknowns, and rechecks.

If authority beyond public metadata cannot be verified, set the operating
state to **Metadata only**.

### 4. Build the License and Evidence Card

| Dimension | Verified state | Grain and source | Design implication | Unknown or recheck |
|---|---|---|---|---|
| License version, date, hash, and owner | | | | |
| Permitted purpose and registered team | | | | |
| Training subjects and scan-timepoints | | | | |
| Test subjects and scan-timepoints | | | | |
| Modalities and native resolutions | | | | |
| Original and preprocessed products | | | | |
| Training and hidden test references | | | | |
| Aggregate subtype evidence | | | | |
| Direct and account access routes | | | | |
| Custodian or participation authority | | | | |

Do not infer permission from file visibility or research-resource wording.

### 5. Build the Product and Timepoint Map

| Requirement | Exact product and grain | Direct fit | Conditional fit | Mismatch | Evidence needed |
|---|---|---|---|---|---|
| Training or test role | | | | | |
| Subject and scan-timepoint unit | | | | | |
| Longitudinal interval | | | | | |
| T1w, T2w, PDw, or FLAIR | | | | | |
| Native or preprocessed state | | | | | |
| Training mask or hidden reference | | | | | |
| Subtype requirement | | | | | |
| Authority and intended use | | | | | |

Keep subject, scan-timepoint, image, modality, mask, rater, and algorithm
submission grains separate.

### 6. Build the Applicability Matrix

| Requirement | Selected route | Supported evidence | Limitation | Unknown or recheck |
|---|---|---|---|---|
| Target population and estimand | | | | |
| Longitudinal structure | | | | |
| Required modality and resolution | | | | |
| Reference-standard need | | | | |
| Original or preprocessing requirement | | | | |
| Subtype evidence | | | | |
| License and authority | | | | |

Use **Conditional fit** only when the exact unresolved condition is visible.

### 7. Build the Threat and Governance Register

Check at minimum:

- 5 training subjects, 21 training scan-timepoints, and their 4/5 pattern;
- 14 test subjects, 61 test scan-timepoints, and their 4/5/6 pattern;
- subject, scan-timepoint, modality, image, mask, rater, and submission grains;
- approximate yearly follow-up and longitudinal dependence;
- exact native voxel sizes and 1 mm MNI preprocessing target;
- original versus preprocessed products;
- two expert delineations versus distributed training masks and hidden test
  references;
- aggregate subtype evidence only;
- data EULA versus NeuroClaw's unrelated MIT code license;
- direct archive visibility versus account-required Smart Stats/Smart-TOOLs;
- registered team, purpose, clinical-use, redistribution, derivative-sharing,
  acknowledgement, notification, submission, and evaluation terms;
- whether the intended use is ordinary research reuse rather than preparation
  of a challenge entry.

Current links, papers, or repository metadata cannot relax the bundled
license.

### 8. Assess the selected or eligible routes

Assess the selected MS Challenge product and authority route against the
approved question.
If it cannot meet the requirements, report the blocker. Compare eligible
routes only if a material choice remains open and the evidence supports
more than one. These are examples of routes and possible dispositions.

1. metadata-only training-product suitability;
2. metadata-only test-product suitability;
3. metadata-only original-versus-preprocessed comparison;
4. metadata-only reference-standard assessment;
5. specification of a verified registered-participation route without data
   action;
6. specification of a written custodian-authorized route without data action;
7. defer because authority, product, modality, reference, longitudinal, or
   evaluation requirements are not met.

For each show exact scope, support, non-support, license basis, authority
burden, unresolved evidence, and downstream handoffs. Do not rank routes
unless the user supplies a decision rule.

### 9. Gate 2: select the specification

Show the License and Evidence Card, Product and Timepoint Map, Applicability
Matrix, Threat and Governance Register, assessed route, disqualifying
conditions, and unresolved conflicts. Include the comparison if a material
choice required one. Carry forward the user's confirmed choices.

Ask about the MS Challenge product, subject and scan-timepoint grain,
modalities, image states, reference boundary, authority state, assumptions,
and handoffs only when a decision remains open or new evidence materially
changes it.

Ask for explicit approval of the assembled Dataset Suitability and Access
Specification and its scope, including the stopping point.

Gate 2 authorizes only the selected specification. It does not authorize
registration, an account, credentials, terms acceptance, download, image
inspection, ordinary reuse, clinical use, redistribution, derivative sharing,
selection, preprocessing, segmentation, analysis, submission, leaderboard
upload, save, or handoff.

### 10. Produce the Dataset Suitability and Access Specification

Record:

1. user-supplied target and estimand;
2. exact license version, date, hash, purpose, and team boundary;
3. training or test product and source date;
4. subject and scan-timepoint counts and pattern;
5. required modalities, native resolutions, and image state;
6. preprocessing and MNI-space boundary;
7. expert, distributed-mask, hidden-reference, and subtype boundary;
8. direct-link, account, custodian, or registered-participation authority;
9. selected assumptions and explicit non-assumptions;
10. unresolved gaps, disqualifying conditions, and handoff packets;
11. verification record and suitability status:
    - **Suitable for metadata-level planning**
    - **Conditionally suitable with verified authority**
    - **Insufficient evidence**
    - **Not suitable for the stated requirement**

The status is local to the selected design. It is not legal advice, permission
to use the data, a segmentation result, or a scientific or clinical
conclusion.

### 11. Verify and stop

Verify:

- the bundled license remains controlling;
- link visibility was not treated as permission;
- training and test subjects and scan-timepoints remain distinct;
- 21 plus 61 equals 82 and the 4/5/6 patterns remain exact;
- T1w, T2w, PDw, FLAIR, native resolutions, and 1 mm MNI state remain exact;
- original and preprocessed products remain distinct;
- two-rater delineation, distributed training masks, and hidden test
  references remain distinct;
- subtypes remain aggregate only;
- authority remains **Unknown** unless exact evidence was supplied;
- only user-selected elements entered the specification;
- no download, ordinary reuse, clinical use, redistribution, derivative
  sharing, analysis, submission, or leaderboard upload occurred.

Then stop.

## Boundaries

The user owns the scientific question, hypothesis, estimand, comparison,
evaluation target, subject and timepoint grain, image product, modality,
reference use, confirmatory status, treatment of longitudinal dependence and
rater disagreement, every access or analytic decision, the final suitability
judgment, and downstream action.

This skill exposes evidence and license constraints. It does not select a
challenge route, infer lesion truth, choose a segmentation method or metric,
or treat participation authority as established.

The bundled `training/license.txt` is the controlling source for downloaded
challenge data. It is version 1.0, dated 2015-02-11, SHA-256
`14ebf3c21d3726c0a2c0479d6288706b58c449c98ae2b31648eafde25b92554a`.

Its specific restrictions govern over general research-resource language:

- downloaded data may be used only to prepare an entry for the MS
  Longitudinal Challenge;
- data are not cleared for clinical or diagnostic use;
- downloaded data, manual delineations, and derived data may not be given or
  redistributed outside the registered team;
- challenge-result publications require acknowledgement and organizer
  notification;
- submission grants permission for public evaluation, but participating teams
  retain their methods;
- Johns Hopkins University and Johns Hopkins Hospital retain rights in the
  data.

Current link visibility does not amend these terms.

Unless the user supplies and verifies either:

1. written custodian authorization covering the exact proposed use; or
2. current registered challenge-participation authority covering the team,
   purpose, and action under the bundled license,

stop at metadata-only suitability. Even with verified authority, this skill
performs no download, ordinary reuse, clinical use, redistribution, derivative
sharing, analysis, submission, or leaderboard upload.

Use this order:

1. exact bundled `training/license.txt`;
2. current official IACL challenge, data, guidelines, and evaluation pages;
3. exact archive directory metadata without imaging-payload retrieval;
4. primary challenge and data-resource papers for historical context;
5. user-supplied authorization or local documentation;
6. external candidate material only as provenance and negative evidence.

Label every material statement as **Verified license fact**, **Verified current
source fact**, **Dated archive fact**, **Historical-paper context**,
**User-supplied authority**, **Inference**, or **Unknown**.

Do not let a paper, public index, direct URL, account page, candidate skill,
repository license, or leaderboard visibility supersede the data EULA.

Edge cases:

- **Only MS Challenge is supplied**: ask for the one scientific requirement.
- **A direct link is treated as permission**: return to the bundled license and
  metadata-only state.
- **Research use is treated as ordinary reuse**: preserve the narrower
  challenge-entry purpose restriction.
- **Five training subjects are called ten scan-timepoints**: correct the total
  to 21 and show the 4/4/4/4/5 pattern.
- **Fourteen test subjects are called 56 scans**: correct the total to 61 and
  show the ten-by-4, three-by-5, one-by-6 pattern.
- **All images are called 0.5 mm isotropic**: replace that claim with the exact
  modality-specific native resolutions and 1 mm MNI preprocessing target.
- **Test masks are requested**: record that both experts delineated them but
  the references remain hidden.
- **A subject subtype is assigned from the public table**: return to aggregate
  subtype evidence only.
- **A derivative is proposed for sharing**: stop because the bundled license
  restricts derived-data redistribution outside the registered team.
- **Leaderboard submission is requested**: stop and require separate verified
  participation authority and action approval.
- **Current official metadata are unavailable**: return **Insufficient
  evidence** and stop.

This skill cannot establish permission, participant subtype, lesion truth,
clinical validity, segmentation performance, longitudinal inference,
preprocessing superiority, power, benchmark comparability, generalizability,
or fitness for clinical use. It cannot guarantee that an archive link,
account route, leaderboard, custodian policy, or participation mechanism
remains current after the recorded query date.

## Design choices and verification

These design references describe the workflow, not a prior decision for this user. Apply the current request's scope and required approvals; these notes authorize no additional action.

Use the Applicable Route Comparison only when a choice remains among metadata-supported training, test, original, preprocessed, mask, verified-authority, or defer routes. The License and Evidence Card, Product and Timepoint Map, Applicability Matrix, and Threat and Governance Register keep license, authority, counts, timepoints, modalities, resolution, preprocessing, hidden references, subtype limits, and the access discrepancy reviewable.

After Gate 2, record only the elements the user selected in the metadata-level Dataset Suitability and Access Specification and retain the verification record. This is a specification-only handoff with no data action.

The stronger behaviors of downloading, opening images, constructing a cohort,
running segmentation, evaluating test results, or uploading a submission are
outside this skill.

> [!info] References
> Read `./references/challenge_facts.md` before the workflow; it holds the facts that control the review.

## Handoffs

- Use [paper-search](../../skills/paper-search/SKILL.md) for a separately approved bounded search about lesion
  delineation, longitudinal evaluation, benchmark interpretation, or prior
  algorithms.
- Use [experimental-design](../../skills/experimental-design/SKILL.md) when the longitudinal unit, reference standard,
  comparison, or evaluation structure changes the design.
- Route custodian contact, challenge registration, credentials, terms,
  controlled transfer, storage, segmentation, evaluation, publication, and
  submission to separately approved owners.

No handoff auto-activates.

## References

- Adapted from: CUHK-AIM-Group. (2026). *NeuroClaw* [Computer software]. GitHub. https://github.com/CUHK-AIM-Group/NeuroDiscovery (MIT License)
- Carass et al. (2017a). *NeuroImage, 148*, 77–102. https://doi.org/10.1016/j.neuroimage.2016.12.064
- Carass et al. (2017b). https://doi.org/10.1016/j.dib.2017.04.004
- IACL. (2022a, July 3). *MSChallenge/data*. https://iacl.ece.jhu.edu/index.php?title=MSChallenge%2Fdata
- IACL. (2022b, July 3). *MSChallenge/guidelines*. https://iacl.ece.jhu.edu/index.php/MSChallenge/guidelines
- IACL. (2026, January 22). *MSChallenge*. https://iacl.ece.jhu.edu/index.php/MSChallenge
