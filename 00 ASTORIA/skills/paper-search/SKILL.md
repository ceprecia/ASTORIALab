---
name: paper-search
description: >-
  Runs one researcher-directed scholarly discovery task through a short Search
  Direction and one upfront approval, then searches the approved public,
  institutional, browser-assisted, and user-provided routes within a stated
  budget. After Gate 1, it assigns one provider agent to every approved
  provider, database, intake route, verification service, or access service when
  subagents are available, while Paper Search retains ownership of the Search
  Direction, budget, normalization, deduplication, provenance, reconciliation,
  and final packet. Use on explicit invocation, a verified Research Coordinator
  handoff, or a declared first-principles-research dependency. It supports field
  mapping, focused evidence searches, known-item
  verification, one-hop reference or citation searches, and manual gap checks.
  Browser-assisted Google Scholar and directly supplied Scholar exports are
  first-class routes. Triggers: search the literature for, find papers on this
  topic.
metadata:
  level: skill
  system: Research Assistant System
  part: "1"
  family: literature
  modality: any
  dependencies: ""
  requires: an approved Search Direction; database or browser access
  gates: ""
  created: "2026-07-23"
  updated: "2026-11-01"
---

# Paper Search

Use one short search approval, then act as a research assistant and finish the bounded search.

## Purpose

It returns every deduplicated candidate found within the approved bounds, verified metadata, observed access routes for shortlisted records, and a transparent shortlist without synthesizing the literature or claiming systematic, scoping, exhaustive, or comprehensive coverage.

Use this skill when:

- The user explicitly says `paper-search`; or
- a verified [research-coordinator](../research-coordinator/SKILL.md) handoff selects it for one bounded
  scholarly discovery task; or
- [first-principles-research](../first-principles-research/SKILL.md)
  invokes its declared search dependency for the user's current question.
  In a companion-led session, use that companion's bounded search route; in
  direct use, retain the first-principles task as the return point. This entry
  supplies no blanket search authorization: apply the Search Direction below
  using approval already given for the scope. Return the source packet to the
  original reasoning task without starting another workflow.

Use one or more labeled lanes when the approved direction requires them:

1. **Broad field mapping:** Map papers across a field, subfield, construct set, population, method, or date range.
2. **Focused evidence search:** Find papers for a defined empirical, theoretical, or methodological question.
3. **Known-item verification:** Resolve or verify a title, DOI, PMID, PMCID, OpenAlex ID, or incomplete citation.
4. **One-hop source search:** Inspect references, citations, or related works for verified seed papers without recursive snowballing.
5. **Manual gap check:** Verify user-supplied leads, titles, identifiers, authors, databases, or query ideas.

Do not use this skill for:

- explaining one paper, which belongs to [research-summarizer](../research-summarizer/SKILL.md);
- comparing theories or synthesizing a literature, which belongs to [literature-synthesis](../literature-synthesis/SKILL.md);
- broad research strategy, which belongs to [research-companion](../research-companion/SKILL.md);
- publication-facing prose, which belongs to [writing-companion](../writing-companion/SKILL.md);
- a systematic review, scoping review, meta-analysis, or other formal evidence-review protocol;
- citation insertion or library organization.

If the user requests a formal review type, explain that Paper Search can supply a
bounded discovery set but cannot establish that review's protocol or coverage.

## Inputs

The user may begin with only a field, interests, a question, or a known paper.
Gather only information that is truly needed to define the search direction:

- practical objective and intended downstream use;
- included concepts, populations, constructs, methods, modalities, or conditions;
- date, source-type, and publication-type boundaries when relevant;
- exclusions;
- seed papers or user-supplied leads;
- requested providers, databases, or access routes;
- requested scale when the user does not want the default.

Do not turn intake into a questionnaire. When the field and interests are
sufficient, draft the Search Direction instead of asking for every optional
field. Do not invent a new scientific question or silently broaden the user's
central objective.

Before Gate 1:

1. Use the optional credential file `.research_api.env` in this skill's folder, `00 ASTORIA/skills/paper-search/.research_api.env`, when a proposed provider needs it.
2. Check that exact location without loading any global profile.
3. Check only whether the credential file and expected variables are present.
4. Do not make network requests merely to prove readiness.
5. Report only a configuration problem that materially changes the proposed direction.

The credential file is not a startup dependency. Load configured credentials
only into the current process after
the search is approved. Never display, quote, log, save, or return credential
values or place them in a visible request URL.

Use provider roles flexibly:

| Provider or route | Primary role | Availability |
| --- | --- | --- |
| OpenAlex | Broad discovery, work identifiers, references, citations, and related works | Configured `OPENALEX_API_KEY` |
| Crossref | DOI registration metadata verification and enrichment | Public service; use `CROSSREF_MAILTO` when configured |
| PubMed through NCBI E-utilities | Biomedical and neuroscience discovery and PMID verification | Use `NCBI_EMAIL`; use `NCBI_API_KEY` when configured |
| Europe PMC | Biomedical and neuroscience discovery, PMCID metadata, and full-text availability metadata | Public service |
| OpenCitations Index | Optional DOI-based reference and citation checks | Configured `OPENCITATIONS_ACCESS_TOKEN` |
| Unpaywall | Public full-text location discovery | Configured `UNPAYWALL_EMAIL` |
| PubMed Central | Public full-text source and PMCID verification | Public service |
| Google Scholar through the user's connected browser | First-class scholarly discovery, citation and related-article exploration, and institutional-link routing | No API key; use the user's existing authenticated browser session |
| User-provided Scholar export | First-class batch candidate intake and gap checking | BibTeX preferred; RIS and EndNote accepted; CSV, Markdown, DOI lists, and citation lists accepted with available provenance |
| Institutional databases and publisher pages | Database searching, article pages, and full-text access | The user's current school network and authenticated browser session |
| User-provided link or file | Known-item verification and access confirmation | Supplied in the current task |

OpenAlex is the default broad discovery provider. Add PubMed or Europe PMC
when the topic is biomedical or neuroscience-relevant. Use Crossref primarily
for DOI metadata. Google Scholar through the user's connected browser and
user-provided Scholar exports are ordinary first-class routes when named in
the Search Direction. A Search Direction may also name other
browser-accessible indexes, institutional databases, publisher pages, or
scholarly services.

Follow current provider documentation, request limits, response headers, and
request-identification requirements. Record provider failures and truncation.

## Steps

### 1. Draft the Search Direction

Use this compact form:

```markdown
## Search Direction

- Field and interests:
- Search route and practical objective:
- Included concepts and boundaries:
- Initial query families:
- Permitted within-scope query adaptations:
- Providers, databases, and access routes:
- Total raw-record cap:
- Per-lane finite request plan or attempt cap and stopping rule:
- Metadata verification:
- Shortlist full-text availability check:
- Main expected coverage limits:
```

Use these defaults unless the user requests another scale:

| Search type | Default budget |
| --- | --- |
| Broad field mapping | Up to 500 raw records total; report every unique candidate remaining after deduplication |
| Focused evidence search | Up to 80 raw records total, targeting roughly 30 to 50 unique candidates |
| Known-item verification | Up to 10 raw records total |
| One-hop source search | Up to 100 raw records total |
| Manual gap check | All supplied leads plus up to 50 raw records from approved follow-up searches |

Always show the exact total raw-record cap for the run. For each discovery lane, also show a finite plan of allowed requests or an exact attempt cap. The plan or cap covers the initial queries, adaptations, page requests and retries as applicable. Track attempts separately from raw records. Reaching a stop describes the search coverage within this plan.

### 2. Gate 1: Approve the Search Direction

Gate 1 is the only routine search approval.

Accept approval or revision through ordinary text or an available structured
selection control. Apply these rules:

- An unambiguous approval starts the complete bounded search.
- A complete user-specified direction with an explicit instruction to run
  counts as Gate 1 approval. Briefly restate the direction and proceed.
- A response that changes the direction but does not authorize execution
  revises the same pending Gate 1. Show the revised direction once.
- A response such as `change X, then run` authorizes the revised direction.
  Restate the revision and proceed without another approval.
- An empty, missing, or malformed structured response is a technical
  non-response. Keep the same Gate 1 pending, state only that no answer was
  recorded, and restate the approval request once in ordinary text.
- Never infer approval, rejection, dismissal, or a user choice from an empty
  structured response. Never describe it as the user making no selection.

Gate 1 authorizes:

- every named provider, database, access route, and fallback;
- the displayed total raw-record cap and each lane's finite request plan or attempt cap;
- within-scope query adaptation within the approved lane limit;
- one bounded retry for a transient provider failure;
- normalization, deduplication, metadata verification, and reconciliation;
- a shortlist full-text availability check;
- final reporting;
- saving only when the direction includes an exact destination.

There is no later search, refinement, expansion, verification, or
result-acceptance approval.

### 3. Execute the Complete Bounded Search

Run each approved lane until its planned requests and permitted adaptations are exhausted, its attempt cap or other approved stop is reached, or the total raw-record cap is reached. Count every request, including empty or failed requests, against the lane's plan or attempt cap. Count raw records separately. For each request, record the provider, query, filters, requested cap, returned count, status, and any truncation or failure. Report each lane's attempts and reason for stopping.

Adapt queries within the approved concepts, lane limit and total raw-record cap.

- translate syntax for each provider;
- add spelling, acronym, singular, plural, and close semantic-synonym variants;
- use relevant controlled-vocabulary terms;
- compare exact phrases with approved term groups;
- split an overconstrained query into approved concept combinations;
- add an already approved dimension when results are too broad;
- relax syntax or conjunction structure when results are empty without removing a substantive boundary;
- paginate or change sort order within the approved cap.

Record each adapted query and its reason. Do not add a new construct,
population, method, date range, source type, provider, seed paper, or citation
hop that is outside the Search Direction. If a wider search would help, finish
the approved run and list it as an optional next search.

Retry one transient provider failure when a short retry is practical and within the approved lane limit. If an
optional provider remains unavailable, continue through the other approved
routes and record the coverage gap. Use a substitute only when Gate 1 named it
as a fallback.

Pause only when an essential approved lane requires the user to restore an API
key, institutional login, MFA, school-network connection, CAPTCHA, or another
access condition. State the exact provider and needed action without exposing
credential values. After the user resolves or skips the lane, resume the same run
without another Gate 1.

#### Google Scholar through the connected browser

When Gate 1 names Google Scholar, treat it as an approved search provider
rather than a fallback:

- allocate it an exact result or page cap inside the displayed total
  raw-record budget;
- run the approved query families through the user's connected browser using the
  approved date filters and relevance or date sorting;
- use quoted titles, `author:`, `Cited by`, `Related articles`, and
  `All versions` when they remain within the approved direction;
- record the exact query, URL, filters, sort order, pages actually inspected,
  result rank, retrieval time, and any observed citation count;
- count only records actually collected, not Scholar's approximate displayed
  result total;
- if login, MFA, school-network access, or a CAPTCHA interrupts the lane, ask
  the user to complete it in the same browser and then resume the same run without
  another Gate 1;
- stop at the approved cap or the last page actually inspected and report any
  blocking, truncation, or uninspected remainder.

#### Direct Scholar export intake

When Gate 1 names a Scholar export or the user supplies it as the approved search
route:

- prefer BibTeX `.bib`;
- accept RIS `.ris`, EndNote `.enw`, CSV `.csv`, Markdown `.md`, plain DOI
  lists, and plain citation lists;
- count each successfully parsed citation as one raw record within the
  approved budget and report any unprocessed remainder after the cap;
- preserve the source filename or supplied artifact name, SHA-256 when a local
  file is available, import timestamp, format, record key, and parse warnings;
- preserve the originating Scholar query, retrieval date, filters, sort
  order, page or result range, and selection rule when supplied;
- if search provenance is incomplete, import the records and label provenance
  partial rather than blocking the run;
- send imported records through the same identifier verification,
  normalization, conservative deduplication, reconciliation, and final
  reporting used for every other provider.

### 4. Normalize and Deduplicate

Normalize records without erasing provider-level provenance:

1. Normalize DOI prefixes, case, whitespace, and identifier formatting.
2. Merge records that share the same verified DOI, PMID, PMCID, or OpenAlex work ID.
3. When no shared identifier exists, merge only when normalized title, publication year, and first author agree exactly.
4. Keep fuzzy title matches, conflicting identifiers, uncertain preprint-to-journal pairs, and material metadata conflicts separate.
5. Put uncertain matches in an ambiguity table without pausing the search.

For every merged record, retain every contributing provider, all stable
identifiers, available core metadata, abstract availability and source,
observed access routes, disagreements, and unresolved fields. Never invent
missing metadata.

### 5. Verify Metadata and Reconcile the Set

Verify identifiers and core metadata against the appropriate records:

- DOI metadata through Crossref and, when useful, the publisher page;
- PMID through PubMed;
- PMCID through Europe PMC or PubMed Central;
- OpenAlex identifiers and graph relationships through OpenAlex.

Record verification status for every candidate. Preserve competing values when
they cannot be resolved. When verification supplies a shared identifier or
corrected metadata, repeat deduplication before constructing the final
candidate set and shortlist.

Label preprints, corrections, retractions, expressions of concern,
abstract-only records, and unresolved bibliographic status when reported.

### 6. Check Full-Text Availability for the Shortlist

Check the approved public, institutional, and user-provided routes for
shortlisted records. Use only these labels:

- `public`;
- `institutional`;
- `user-provided`;
- `unresolved`;
- `not checked`.

Record the route type, host or service, URL, observed result, verification
date, and uncertainty. Distinguish full-text access from a landing page or an
authentication requirement. Institutional access counts normally when the
expected paper opens through the user's current school network or authenticated
session.

Paper Search may open a landing page or full-text view and inspect enough
content to confirm the work and its relevance to the approved direction.
Substantive full-text explanation, critical appraisal, synthesis, and building
or modifying a local paper library are separate tasks.

### 7. Return the Final Bounded Result

Use the form and order selected for this task, then the recipient's applicable reporting policy for open choices. If neither specifies a form or order, use a concise, traceable search report. Include the following information where applicable.

- coverage Statement
- approved Search Direction
- provider and Access Status
- exact Search Record
- all Deduplicated Candidates Returned Within the Approved Bounds
- unresolved Duplicates and Metadata Conflicts
- transparent Shortlist
- other Candidates and Exclusion Reasons
- shortlist Full-Text Access Routes
- provider Gaps, Coverage Limits, and Uncertainty
- optional Next Searches
- available Handoffs

Return every deduplicated record found within the approved bounds, not only the
shortlist. Give a one-sentence inclusion reason for each shortlisted record and
a concise exclusion reason for each other candidate.

State that the result is a bounded discovery set. Do not call it systematic,
scoping, exhaustive, comprehensive, complete, or PRISMA-compliant.

## Optional Subagent Delegation

After Gate 1, assign one agent to every approved provider, database, intake route, verification service, or access service, even when only one is approved.

```text
for each approved provider or service:
    run its provider-specific work when the required input is available
    return its Search Record information and provider result
parent:
    own the Search Direction and allocate its total raw-record budget across discovery lanes
    normalize, deduplicate, reconcile, verify provenance, and produce the final packet
```

Discovery agents run Step 3, verification agents run Step 5 after normalization, and access agents run Step 6 after shortlisting. Reuse one provider lane across stages. Agents return raw results, status, failures, truncation, and provider-level provenance; the parent fills `Unique contribution` after deduplication. Agents do not normalize across providers, deduplicate, rank the complete set, choose the shortlist, or report the final packet.

Never split by query, page, candidate, or retry, and do not allow nested delegation. Run shared interactive-browser lanes sequentially when they could conflict. The parent waits for every lane, preserves partial or failed results, and runs the same provider work sequentially when the host cannot spawn subagents.

## Search Record and Candidate Fields

For every request, preserve:

| Field | Required record |
| --- | --- |
| Search date and time | Exact timestamp and timezone |
| Search lane | Broad mapping, focused evidence, known item, one hop, or manual gap check |
| Provider or database | Exact service |
| Query | Human-readable query with secrets removed |
| Adaptation reason | Original query or reason for an approved adaptation |
| Filters | Dates, source types, fields, populations, or other approved limits |
| Requested cap | Records requested within the total budget |
| Returned count | Raw records returned |
| Unique contribution | Records added after deduplication |
| Status | Complete within cap, truncated, empty, rate-limited, unavailable, skipped, or failed |
| Notes | Warnings, retries, coverage limitations, or request changes |

For browser-assisted Scholar lanes, also preserve the pages actually
inspected, result rank, sort order, and retrieval-dated citation count when
observed. For Scholar imports, also preserve the source artifact, format,
import timestamp, record key, parse warnings, and available search provenance.

The candidate table should include, when available:

- title, authors, year, venue, and source type;
- DOI, PMID, PMCID, and OpenAlex ID;
- contributing providers;
- abstract availability;
- metadata-verification status;
- observed access route;
- approved relevance fields;
- shortlist status and reason.

## Outputs

Return results in the current task's requested form or under the recipient's existing reporting policy.

If the approved Search Direction includes an exact destination, save and
verify the final result there without another approval. If the user later gives an
explicit save command and destination, that command authorizes the save. Ask
only when the destination is ambiguous or a collision requires a decision.

Preserve the approved direction, exact search record, candidate set, shortlist
logic, ambiguity table, access observations, and coverage limits in any saved
result.

Offer relevant handoffs without starting them:

- [research-summarizer](../research-summarizer/SKILL.md) for one selected paper;
- [literature-synthesis](../literature-synthesis/SKILL.md) for an approved multi-source critical synthesis;
- [prediction-stress-test](../prediction-stress-test/SKILL.md) for bounded counterevidence or novelty assessment;
- [research-companion](../research-companion/SKILL.md) for broader framing or strategy;
- [writing-companion](../writing-companion/SKILL.md) after the user selects evidence for publication-facing prose.

A later refinement, save, or handoff is a new user-commanded action, not a
post-search gate.

## Boundaries

Scientific and coverage rules:

- Search identifies candidates. It does not establish scientific conclusions.
- Separate provider metadata, source-authored claims, and AI relevance judgments.
- Prefer primary empirical sources when the question requires empirical evidence, while retaining other approved source types.
- Preserve null findings and contradictory candidates when they satisfy the approved criteria.
- Treat citation counts only as dated descriptive metadata.
- Do not equate retrieval rank, citation count, journal name, access status, or recency with study quality.
- Do not infer evidence for absence from an empty or failed search lane.
- Never invent papers, identifiers, metadata, abstracts, links, access status, or coverage.

Edge cases:

- **Missing field or interests:** Ask only for the missing core input, then draft the Search Direction.
- **Credential location unavailable:** Use the verified current location above; no global loader is required. Missing credentials affect only the routes that need them.
- **Credential missing for an optional lane:** Continue through the functioning approved routes and record the gap.
- **Credential or institutional action required for an essential lane:** Pause for the exact action, then resume or skip without another Gate 1.
- **Scholar login, MFA, school-network access, or CAPTCHA required:** Ask the user to complete it in the connected browser, then resume the same approved lane without another Gate 1.
- **Scholar export has incomplete search provenance:** Import the parsable records, preserve the available provenance, and label the missing fields rather than blocking the run.
- **Scholar browser lane cannot reach its approved cap:** Return only the records actually collected and report the pages inspected, stopping point, and limitation.
- **Transient provider failure:** Retry once when practical, then record the failure and continue.
- **Empty results:** Try only permitted adaptations within the approved lane limit. Stop when the lane's planned requests and permitted adaptations are exhausted or the lane's approved attempt cap is reached, whichever comes first. Report the empty lane, attempts used and stopping reason even if the raw-record cap remains unused.
- **Excessive results:** Stop at the approved cap and label the lane truncated.
- **Provider syntax error:** Translate syntax while preserving meaning, record the repair, and retry only within the approved lane limit and raw-record cap.
- **Missing identifiers:** Verify by exact title, year, and first-author agreement when possible; otherwise label the record unverified.
- **Fuzzy duplicate or metadata conflict:** Keep records separate and surface the ambiguity.
- **Preprint and journal article:** Keep the relationship visible unless identifiers and publication history resolve it.
- **Only an abstract is available:** Label abstract-only coverage and do not infer full methods, results, or limitations.
- **No full-text route confirmed:** Report which routes were checked and which remain unresolved or untested.
- **Scope change during execution:** Preserve the completed record, stop adding requests under the old direction, and treat the changed scope as a new search.
- **Refinement after results:** Draft a new Search Direction and use one new Gate 1, unless the user supplies a complete revised direction and explicitly says to run it.
- **Reformatting existing results:** Reformat or sort without starting another search or approval.

## References

- Crossref. (n.d.). *REST API access and authentication*. https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/
- Europe PMC. (n.d.). *RESTful web service*. https://europepmc.org/RestfulWebService
- Google. (n.d.). *Search help*. Google Scholar. https://scholar.google.com/intl/us/scholar/help.html
- National Center for Biotechnology Information. (n.d.). *The E-utilities in-depth*. https://www.ncbi.nlm.nih.gov/books/NBK25499/
- National Library of Medicine. (n.d.). *Open access web service*. PubMed Central. https://pmc.ncbi.nlm.nih.gov/tools/oa-service/
- OpenAI. (n.d.). *Subagents*. https://learn.chatgpt.com/docs/agent-configuration/subagents.md
- OpenCitations. (n.d.). *Index API version 2* (Version 2.2.0). https://api.opencitations.net/index/v2
- OurResearch. (n.d.-a). *API*. Unpaywall. https://unpaywall.org/api
- OurResearch. (n.d.-b). *Authentication*. OpenAlex. https://developers.openalex.org/guides/authentication
