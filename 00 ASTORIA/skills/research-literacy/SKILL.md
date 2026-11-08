---
name: research-literacy
description: >-
  Audits one explicit research claim and its directly linked subclaims against
  supplied and bounded verified evidence. Use when the user asks to audit or check a
  research claim, to expose assumptions, inferential limits, and calibrated
  evidence status before producing user-selected claim wording. Do not use for
  whole-study critique, broad literature discovery, hypothesis generation,
  statistical execution, or manuscript drafting. Triggers: audit this claim
  against the evidence, does the evidence support this claim.
metadata:
  level: skill
  system: Research Assistant System
  part: "2"
  family: critique
  modality: any
  dependencies: ""
  requires: ""
  gates: ""
  created: "2026-07-23"
  updated: "2026-11-01"
---

# Research Literacy

Audit one claim bundle without taking ownership of the scientific judgment.

## Purpose

`research-literacy` is the canonical owner for auditing one explicit primary research claim and only the subclaims directly required to support, qualify, or interpret it. Its home is Part 2 of the Research Assistant System, but it may audit a bounded claim at any inquiry part.

The user owns the claim, hypotheses, predictions, confirmatory status, design choices, thresholds, interpretation, action, and final wording. This skill exposes evidence, assumptions, inferential limits, and defensible wording options. It never silently chooses the scientific position.

Use this skill when the request matches its description:

- the trigger phrases in this skill's frontmatter `description` (the model matches meaning, not exact strings; the skill's name also works as a direct call)

The input must contain, or permit extraction of, one primary claim. Include a subclaim only when the primary claim depends on it, it qualifies the primary claim's scope or force, or it supplies the proposed mechanism, comparison, population, measurement, timing, or absence interpretation. Treat independent claims as separate future audits.

Do not trigger on generic requests such as `check this claim`, `review this paper`, `analyze these data`, or `improve this paragraph`.

## Inputs

Gather only what is needed to define the claim bundle:

- exact primary claim;
- directly linked subclaims, if any;
- intended use and audience;
- claim type for each component, such as descriptive, associational, causal, predictive, mechanistic, generalizing, comparative, or absence;
- supplied evidence and any named source;
- permitted evidence boundary;
- whether outcomes were unseen, partly seen, or fully seen when each analytic decision was made;
- intended confirmatory, exploratory, or unclear status;
- relevant preregistration, protocol, analysis plan, deviations, thresholds, or decision rules.

If an essential item is missing, mark it `unknown`. Do not fill it from assumption.

## Steps

### 1. Build the Claim Audit Brief

Quote or faithfully transcribe the proposed primary claim and each directly linked subclaim. Do not strengthen, narrow, or rewrite them yet.

Show:

| Field | Required content |
|---|---|
| Primary claim | Exact proposed wording |
| Linked subclaims | Exact wording and why each is necessary to the primary claim |
| Excluded claims | Independent claims deferred to a separate audit |
| Intended use | Where and why the claim will be used |
| Claim types | Type assigned to every component |
| Evidence boundary | Supplied sources, named source, and any permitted bounded verification |
| Outcome visibility | What outcome information was available when consequential decisions were made |
| Confirmatory status | Confirmatory, exploratory, mixed, or unclear, with the user's stated basis |
| Unknowns | Missing facts that may limit the audit |

### 2. Gate 1: approve the audit bundle

Ask the user to approve or correct the Claim Audit Brief before inspecting any new source or beginning the audit.

Gate 1 authorizes only:

- the displayed primary claim and linked subclaims;
- the displayed intended use, classifications, and evidence boundary;
- inspection of supplied material;
- when supplied material is insufficient, the bounded verification rule in Step 4.

It does not authorize a broad search, a second independent claim, saving, drafting a manuscript section, starting another skill, or handing work off.

If the user changes the primary claim, adds an independent claim, changes the intended use, or materially expands the evidence boundary, rebuild the brief and repeat Gate 1.

### 3. Build the Claim-Evidence Map

Inspect supplied evidence first. For every claim component, keep these layers separate:

| Layer | Record |
|---|---|
| Source statement | What the source authors explicitly state |
| Observed result | What was measured or estimated, including the comparison, sample, estimate, uncertainty, and reported analysis when available |
| AI interpretation | Any inference added during this audit, labeled as interpretation |

Then map each component:

| Field | Required content |
|---|---|
| Claim ID and exact text | Primary or linked subclaim |
| Evidence item | Source and exact location when available |
| Directness | Direct, indirect, contextual, or absent |
| Relevant result | Estimate, uncertainty, decision rule, and other material numerical information |
| Assumptions | Construct, measurement, design, model, causal, or generalization assumptions |
| Conflicts and gaps | Inaccessible material, disagreement, missing reporting, or unresolved facts |

Do not treat an abstract, title, citation count, search snippet, or author conclusion as a substitute for inspecting the evidence needed for the claim.

### 4. Verify within the approved boundary

If the supplied evidence is sufficient, do not search.

If it is insufficient after Gate 1:

1. inspect the named source, when one was supplied;
2. inspect no more than three additional directly relevant primary or authoritative sources;
3. when no named source was supplied, inspect no more than three sources total;
4. prefer the primary report for an empirical result and authoritative methodological guidance for an inferential rule;
5. record the query or route, source type, identifier or URL, access result, access date, relevance, and use decision.

Do not download or save source files unless the user separately approves it. Do not describe this bounded check as systematic, exhaustive, or proof that no other literature exists.

Stop and offer [paper-search](../paper-search/SKILL.md) when the claim requires broader discovery, citation-network expansion, several search concepts, or more than the source cap. A failed or empty bounded check is an access result, not evidence that no literature exists.

When a critical source is inaccessible, state exactly what was and was not inspected. Do not infer its full findings from metadata or an abstract. Use `unresolved` when the missing evidence prevents a defensible status.

### 5. Apply the relevant checks

Apply only checks that bear on the approved claim. Mark nonapplicable checks explicitly rather than inventing work.

#### Construct and measurement

- Identify the construct named in the claim and the operational measure actually used.
- Check whether the measure's validity, reliability, scale, timing, and scoring support that construct.
- Flag proxy-to-construct, task-to-trait, symptom-to-diagnosis, neural-signal-to-mental-state, and other level-of-inference jumps.
- Do not let a precise p-value or interval repair a construct or measurement mismatch.

#### Design, comparison, and causality

- Identify the design and the comparison that bears directly on the claim.
- Check temporal order, randomization, confounding, selection, attrition, missingness, dependence, clustering, and intervention fidelity when relevant.
- Reserve causal wording for evidence and assumptions that license it.
- Do not infer a difference merely because one comparison is statistically significant and another is not. Require the reported direct contrast or interaction that addresses the difference claim.

#### Scope and generalization

- Compare the claimed population, setting, exposure or intervention, outcome, and time frame with those actually studied.
- Distinguish sample description from population generalization.
- Identify transportability assumptions and exclusions.
- Narrow claims that extend beyond the inspected evidence.

#### Estimand, model, and analysis alignment

- Identify the quantity the claim is about and the quantity the reported analysis estimates.
- Check whether the contrast, outcome scale, unit of analysis, model, and uncertainty address that quantity.
- Treat model or estimand mismatch as an inferential limitation that statistical significance cannot repair.
- Flag missing multiplicity, dependency, model-checking, robustness, or sensitivity information when it changes what can be claimed.
- Audit reported analyses only. Do not choose a new method or execute a statistical analysis.

#### Confirmatory specification and deviations

For a confirmatory interpretation, require outcome-independent specification of:

- hypotheses and directional predictions when applicable;
- primary and secondary outcomes or estimands;
- exclusions and data-quality rules;
- sample-size or stopping rule;
- analysis and transformation rules;
- any NHST alpha, multiplicity adjustment, adaptive rule, or sequential decision rule.

Outcome-independent specification may include a documented preregistration, protocol, timestamped analysis plan, blinded check, prespecified decision tree, valid adaptive or sequential design, or genuinely independent holdout. Preregistration is evidence about timing and specification; it does not validate a claim or make an analysis correct.

Record every relevant deviation separately:

- what changed;
- when it changed relative to outcome access;
- why it changed;
- whether the change was outcome-independent;
- which analysis or claim component it affects;
- how it changes confirmatory status.

Do not downgrade unaffected confirmatory analyses merely because another analysis deviated. A finding developed after seeing the relevant outcomes is exploratory on those data, even if plausible or later documented. It may become confirmatory only through an appropriate independent test.

#### NHST, estimates, and uncertainty

- Apply the exact valid prespecified decision rule, including its inequality, applicable alpha, multiplicity adjustment, and any sequential or adaptive threshold.
- Under that rule, a p-value above the applicable threshold does not meet the decision criterion.
- For `p = alpha`, apply the prespecified equality rule. If the rule does not define equality or the reported precision cannot resolve it, mark the decision unresolved rather than inventing a convention.
- Do not call a result a `trend`, `marginal`, `approaching significance`, `nearly supported`, or similar merely because its p-value nearly crosses a threshold. This restriction does not prohibit a substantively defined temporal trend or another formally specified trend estimand.
- Do not treat `p = .049` and `p = .051` as an evidential cliff. Report the applicable decisions and evaluate the estimates, uncertainty, design, and evidence continuously.
- Report numerical p-values at defensible precision or use a justified bound. State the attainable resolution for permutation, randomization, simulation, or rounded output; never convert finite-resolution output into `p = 0`.
- Report relevant effect estimates and method-appropriate uncertainty. Do not force a confidence interval when the method does not define one.
- Do not infer practical importance, effect size, truth, or falsity from a p-value alone.
- Nonsignificance does not establish the null or show that groups, conditions, mechanisms, or populations are the same.

#### Evidence for absence

- Require a prespecified method capable of addressing absence relative to a substantively justified bound or explicit comparison.
- Treat a smallest effect size of interest as a justified substantive bound, not as a statistical method.
- A properly specified equivalence test can support absence of effects at least as large as the equivalence bounds. It does not establish exact zero, identical groups, or absence of a mechanism.
- If neither a difference test nor an equivalence test is conclusive, report the result as inconclusive rather than as evidence for either presence or absence.
- Treat equivalence bounds chosen after seeing the relevant outcomes as exploratory for those data.

For a Bayesian absence claim, require:

- explicit competing models or hypotheses and the direction of comparison;
- a justified likelihood and priors;
- computational and model checks appropriate to the analysis;
- prior and other material sensitivity analyses;
- reporting tied to the specified models rather than an unqualified claim of absence.

A Bayes factor near 1 or otherwise insensitive evidence supports neither model. Evidence favoring a specified null model is relative to those models and assumptions; it is not proof of exact absence.

### 6. Assign calibrated evidence statuses

Assign exactly one status to every claim component:

- **supportable as written**: The component is directly supported at its stated scope and force within the inspected evidence boundary, with material assumptions and uncertainty disclosed.
- **supportable with narrowing**: A defensible claim remains after restricting scope, causal force, precision, population, mechanism, or confirmatory language.
- **unresolved**: Missing, inaccessible, conflicting, ambiguous, underpowered, insensitive, or otherwise insufficient evidence prevents a defensible directional status.
- **unsupported by available evidence**: Relevant inspected evidence is adequate to assess the component but does not supply the support the component requires, without positively supporting an incompatible claim.
- **contradicted by available evidence**: Relevant credible inspected evidence supports a result or statement incompatible with the component.

Append `within the inspected evidence boundary` to every status presentation. Never convert an empty search result or inaccessible source into `unsupported` or `contradicted`.

Keep component statuses visible. Do not average across sources or components. The primary claim's status must reflect any linked subclaim essential to its wording, mechanism, causal force, or scope. Explain conflicts by source quality, directness, design, estimand, and applicability rather than by vote counting.

For a primary claim that logically depends on linked subclaims, propagate indispensable component statuses in this order:

1. `contradicted by available evidence` if any indispensable component is contradicted;
2. otherwise, `unsupported by available evidence` if any indispensable component is unsupported;
3. otherwise, `unresolved` if any indispensable component is unresolved;
4. otherwise, `supportable with narrowing` if any indispensable component requires narrowing;
5. `supportable as written` only when the primary claim and every indispensable component are supportable as written.

Use this rule only to prevent compound wording from receiving a stronger status than a proposition it requires. Do not use it to average evidence, rank source quality mechanically, or replace scientific judgment about whether a subclaim is genuinely indispensable. If removing a subclaim leaves the primary proposition intact, the subclaim was not indispensable and must be statused separately.

### 7. Present calibrated status and action options

Present the evidence statuses before action options. Do not let a preferred action alter a status.

Offer only defensible options:

- **retain**: preserve the claim as written;
- **narrow**: restrict the wording to what the evidence supports;
- **relabel exploratory**: preserve a useful observation or proposal while removing confirmatory force on the current data;
- **defer**: withhold the claim pending specified evidence or clarification;
- **withdraw**: remove the claim from the intended use.

For each available option, show:

- an AI-drafted wording candidate, when wording is relevant;
- what changes and what remains;
- evidence and assumptions supporting the option;
- tradeoffs and unresolved risks;
- wording that would remain too strong.

Do not create artificial choices. If only one option is defensible, disclose that constraint and why.

### 8. Gate 2: The user selects the action and wording

Ask the user to select, reject, or revise an action and any wording candidate. Gate 2 authorizes only the selected action and exact wording for the current Claim Specification.

Do not infer selection from silence. Do not turn an AI-drafted option into the user's claim without explicit selection.

If the user selects wording that exceeds the evidence status, retain the status, identify the mismatch, and do not present the stronger wording as verified.

### 9. Produce and verify the Claim Specification

After Gate 2, produce:

| Field | Required content |
|---|---|
| Final wording | user-selected exact wording; for `defer` or `withdraw`, state `No outward-facing claim approved` and preserve the audited wording only in provenance |
| Intended use | Approved use and audience |
| Claim bundle | Primary claim and included linked subclaims |
| Claim types | Type of every component |
| Evidence boundary | Sources inspected, access limits, and access date |
| Evidence status | Unchanged component statuses, each qualified by the inspected evidence boundary |
| Selected action | Retain, narrow, relabel exploratory, defer, or withdraw |
| Confirmatory status | Confirmatory, exploratory, mixed, unclear, or not applicable |
| Assumptions and limits | Material construct, measurement, design, model, causal, and generalization constraints |
| Statistical specification | Applicable thresholds, estimates, uncertainty, absence method, deviations, or unresolved reporting |
| Required attribution | Citations or source statements that must accompany the wording |
| Prohibited expansions | Stronger formulations not licensed by this audit |
| Open items | Evidence or decisions still needed |
| Provenance | User wording, AI-drafted option selected by the user, and any revisions |

Verify that:

- the final wording is exactly the version the user selected;
- no scope, causal force, certainty, or confirmatory status exceeds the inspected evidence;
- every linked subclaim remains necessary and separately statused;
- numerical claims preserve defensible precision and method-appropriate uncertainty;
- deviations and exploratory analyses remain disclosed;
- the selected action has not changed any evidence status;
- no unapproved search, save, or handoff occurred.

## Outputs

Include the applicable evidence and outputs below. Use the form and order selected for this task, then the recipient's applicable reporting policy for open choices. If neither specifies a form or order, use a concise report organized around the current decision.

- **Claim Audit Brief**
- **Claim-Evidence Map**
- **Statistical and Inferential Checks**
- **Calibrated Status and Options**
- **Claim Specification**, only after Gate 2

At Gate 1 or Gate 2, stop after showing the material needed for the decision. Do not simulate the user's approval.

Present the review in the current task's requested form or under the recipient's existing reporting policy. Gate 1 and Gate 2 do not authorize saving, modifying a source, downloading a paper, starting another skill, or initiating a handoff.

Before a save, download or handoff, verify the exact file, content or packet and its source, destination or recipient as applicable. Show a preview when the task requests one, when an applicable verified reporting policy calls for it and the task leaves that choice open, or when a decision still needs approval. Honor existing authorization within its exact scope and verify the result afterward.

## Boundaries

- **Causal overclaim**: status the causal component separately; do not let a supported association carry unsupported causal wording.
- **Several clauses**: retain only clauses directly linked to one primary claim; split independent claims into future audits.
- **Conflicting sources**: preserve the disagreement and assess directness, design, estimand, quality, and applicability; do not average conclusions.
- **Inaccessible critical evidence**: record the access limit and use `unresolved` when the missing material matters.
- **Sufficient supplied evidence**: complete the audit without network search.
- **Source cap reached**: stop and offer `paper-search`; do not quietly inspect a fourth additional source.
- **Optional stopping**: distinguish an outcome-dependent extension from a prespecified and correctly implemented sequential or adaptive rule.
- **Blinded change**: assess whether the change was genuinely outcome-independent and document its scope.
- **Exploratory discovery**: label it exploratory on the current data even when theoretically plausible.
- **Rounded threshold result**: do not decide `p = alpha` when rounding or finite numerical resolution prevents the comparison.
- **Multiplicity**: use the applicable adjusted rule, not the unadjusted alpha or raw p-value in isolation.
- **Subgroup or condition comparison**: require the direct contrast or interaction rather than comparing two significance labels.
- **Equivalence claim**: report the prespecified bounds, their substantive justification, and what effects they exclude.
- **Bayesian absence claim**: report the compared models, likelihood, priors, checks, and sensitivity; treat insensitive evidence as unresolved.
- **Generic request**: `check this claim` does not trigger this skill.

## Handoffs

- Use [research-summarizer](../research-summarizer/SKILL.md) when the main request is to explain one paper rather than audit one claim bundle.
- Use [paper-search](../paper-search/SKILL.md) when the evidence need exceeds the bounded source rule.
- Use [research-companion](../research-companion/SKILL.md) for broad framing, strategic options, or project-level critique.
- Use writing-companion when the task becomes publication-facing drafting, carrying the current scientific claim/status and supplied evidence. verify-writing-citations owns bibliographic identity and exact citation-support checks; this skill retains its deeper bounded scientific claim audit. Do not trigger this full audit for every ordinary citation check.
- Use [research-critique](../research-critique/SKILL.md) for detailed critique of one bounded research object. If a selected critique finding needs a claim audit, accept only the approved Research Literacy input packet and perform the claim-level audit without duplicating the critique workflow.
- Prospective stress testing of a user-supplied hypothesis and prediction belongs to [prediction-stress-test](../prediction-stress-test/SKILL.md). Prepare a bounded handoff and wait for separate approval.
- Route statistical execution or method implementation to the relevant approved Part 4 capability. If no active approved capability matches, disclose the gap and stop. Do not select a method merely because software is available.

This skill does not generate hypotheses, decide confirmatory status for the user, choose a design or model, execute statistics, audit an entire study, run broad discovery, draft a manuscript, or make an unsupported scientific conclusion.

## References

- American Statistical Association. (2016). *Statement on statistical significance and p-values*. https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf
- Appelbaum, M., Cooper, H., Kline, R. B., Mayo-Wilson, E., Nezu, A. M., & Rao, S. M. (2018). Journal article reporting standards for quantitative research in psychology. *American Psychologist, 73*(1), 3–25. https://doi.org/10.1037/amp0000191
- Gelman, A., & Stern, H. (2006). The difference between "significant" and "not significant" is not itself statistically significant. *The American Statistician, 60*(4), 328–331. https://doi.org/10.1198/000313006X152649
- Kruschke, J. K. (2021). Bayesian analysis reporting guidelines. *Nature Human Behaviour, 5*, 1282–1291. https://doi.org/10.1038/s41562-021-01177-7
- Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence testing for psychological research: A tutorial. *Advances in Methods and Practices in Psychological Science, 1*(2), 259–269. https://doi.org/10.1177/2515245918770963
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114
- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's statement on p-values: Context, process, and purpose. *The American Statistician, 70*(2), 129–133. https://doi.org/10.1080/00031305.2016.1154108
