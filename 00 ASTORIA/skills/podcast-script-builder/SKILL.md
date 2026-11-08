---
name: podcast-script-builder
description: >-
  Converts supplied writing, papers, notes, slides or transcripts into a
  source-grounded podcast production packet. Establishes the recipient's
  audience, format, speaker arrangement, runtime and requested output. Keeps
  factual claims traceable and source material unchanged. Optional platform
  handoff instructions are included when selected. Creates scripts and
  generation instructions, not audio. Triggers: turn this into a podcast script,
  make this a podcast episode, create a podcast production packet.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: ""
  created: "2026-08-03"
  updated: "2026-10-29"
---

# Podcast Script Builder

Turn bounded source material into a performable, auditable podcast production packet.

## Purpose

Use this skill when the user asks to transform supplied material into a podcast script or production packet. Eligible inputs include:

- manuscripts and other writing;
- research papers and existing paper summaries;
- study notes, slides, and teaching material;
- transcripts and pasted text;
- user-named public vault notes or files; and
- URLs whose contents can be read and verified.

This skill creates a new podcast packet. It does not revise the source, generate audio, imitate an identifiable host, or perform open-ended literature discovery.

## Inputs

Resolve the supplied sources and episode objective first. Establish audience, format, speaker arrangement, desired runtime and output format from the request. If a consequential choice is unanswered, ask a compact question or offer a source-supported proposal for confirmation. No discipline, career stage, host count or listening platform is assumed.

| Field | Selection rule |
| --- | --- |
| Source material | Required and bounded |
| Audience and prior knowledge | Recipient-supplied; otherwise clarify |
| Format and speaker arrangement | Select for the communication purpose |
| Runtime | Select a target supported by the material |
| Script form | Match the requested performance and production use |
| Show and speaker names | Use supplied names or clearly marked placeholders |
| Research boundary | Supplied sources; external research only within current authorization |
| Output | Requested packet format; DOCX production is available when selected |
| Platform handoff | Include only for a selected platform |

### Runtime calibration

- Estimate duration from spoken dialogue, then add only the pauses and bounded improvisation windows actually planned.
- Use the selected runtime only when the supplied or approved sources support it.
- If the sources support a different duration, explain the proposed change and do not pad the script.
- Report the scripted spoken-word count and provisional timing in the Episode Brief and Studio Handoff Notes. Treat rehearsal or a read-aloud as the final timing check.

## Episode modes

- **Deep Dive:** When selected, speakers explain, connect, examine, and qualify the supplied material.
- **Brief:** A shorter source-grounded explanation with fewer acts and examples.
- **Critique:** Two hosts constructively evaluate an argument, design, draft, or source set.
- **Debate:** Two hosts examine genuinely supported competing positions. Do not manufacture an opposing position.
- **Solo:** One host presents the episode while retaining the same source and dossier requirements.
- **Interview:** A host questions a supplied or explicitly defined participant. Never impersonate a source author, fabricate testimony, or present a synthetic role as a real person.

## Source contract

### Source authority

1. Use the exact material the user supplies or names.
2. Use existing Research Summarizer outputs when supplied, but do not invoke [research-summarizer](../research-summarizer/SKILL.md) automatically.
3. If the user provides only a title, topic, or inaccessible link, ask for the source or approval for a bounded lookup.
4. Conduct supplemental research only when the user requests or approves it. Keep the search tied to the episode question and record every added source.
5. Route genuine literature discovery or systematic search to the appropriate Research Assistant capability instead of widening this skill.

### Coverage and provenance

Assign stable identifiers in source order: `S1`, `S2`, `S3`, and so on. For each source, record:

- supported identity and citation details;
- a concise spoken attribution label using the verified author, creator,
  speaker, organization, publisher, or source title;
- source type;
- complete, selected-section, abstract-only, excerpt, or other partial coverage;
- central question or purpose;
- claims and findings;
- evidence, examples, methods, or reasoning;
- definitions and protected terminology;
- limitations, alternatives, uncertainty, and unresolved questions;
- usable page, section, paragraph, figure, table, or timestamp locators; and
- the source's planned role in the episode.

Never invent missing bibliographic details or pretend partial access is complete.

### Evidence categories

Keep these categories distinct in the script and dossier:

- **Source states:** A faithful report of one source.
- **Supported synthesis:** A connection warranted across the supplied sources.
- **Interpretation:** A reasoned reading that goes beyond direct source wording.
- **Open question:** An unresolved issue, conflict, or missing fact.

## Steps

### 1. Load and bound the sources

Read every supplied source needed for the episode. Confirm the source list, coverage, and any unreadable or missing material. Preserve source files unchanged.

### 2. Establish the episode frame

Define:

- working episode title;
- central question or tension;
- listener promise;
- audience and assumed knowledge;
- mode, host functions, and tone;
- target runtime;
- three to six major takeaways;
- source boundary; and
- one argumentative sequence for the complete episode.

Create interest from a source-supported question, tension, finding, consequence, or competing interpretation. Do not manufacture urgency or clickbait.

### 3. Build the source ledger

Create one source card per item and a claim-keyed evidence map. For every major claim, record:

- claim ID;
- category from the Evidence categories section;
- detailed context;
- supporting source and locator;
- supporting evidence or reasoning;
- counterevidence or alternatives when present;
- limitations and uncertainty;
- confidence justified by the supplied material; and
- planned script segment.

Mark unsupported gaps. Do not fill them with plausible details.

For a technical comparison, also state the estimand or direct comparison, the features held constant, and the factors not tested. Do not turn the absence of an untested factor comparison into doubt about a contrast the design directly estimates.

### 4. Design the listener journey

Use this flexible five-act progression unless the material supports a better structure:

1. **Stakes and context:** Why the question matters and what the listener needs to know.
2. **Central account:** The main argument, model, story, or explanation.
3. **Evidence and examples:** What supports the account and how the evidence works.
4. **Complications and alternatives:** Limits, uncertainty, disagreements, or competing explanations.
5. **Synthesis and application:** What can be concluded, why it matters, and what remains open.

Each act should advance through a useful sequence such as:

`question -> explanation -> evidence or example -> qualification -> takeaway -> transition`

Adapt the number and order of acts when the source material requires it. Do not force a five-act structure onto material that becomes less coherent because of it.

### 5. Draft the studio script

Write every required host line and transition. Keep the exchange natural enough to perform and complete enough that a studio does not need to reconstruct the argument.

Host rules:

- HOST 1 usually establishes the frame, explains conceptual structure, and maintains continuity.
- HOST 2 usually requests clarification, examines evidence, introduces alternatives, and restates qualified conclusions.
- Either host may lead a segment when the source logic benefits.
- Give each turn a job. Avoid repetitive agreement, decorative banter, and alternating essay-length monologues.
- Define technical terms without removing necessary precision.
- Do not fabricate personal experiences, anecdotes, emotions, disagreement, quotations, or source-author testimony.
- Do not turn an author's experience into a host's first-person story.
- Prefer faithful paraphrase to extended quotation. Flag clips, music, and any quotation requiring permission for rights review rather than assuming that production use is cleared.

Use short, audible, actionable production cues only when they help performance or comprehension:

```text
[PAUSE]
[EMPHASIZE]
[MUSIC IN]
[MUSIC OUT]
[OPTIONAL LICENSED CLIP]
```

Do not use visual-only stage directions. Keep music and sound effects sparse.

### 6. Add bounded improvisation windows

Use improvisation only where a host can elaborate without changing the science, evidence, or central argument.

```text
[IMPROV WINDOW: purpose | approved points | source boundary S1, S3 | estimated duration]
```

Every window must include:

- a clear conversational purpose;
- the points the host may cover;
- the sources that bound factual content; and
- an estimated duration.

Improvisation may vary phrasing, examples already present in the sources, and transitions. It may not add new factual claims, personal experiences, quotations, mechanisms, or conclusions.

### 7. Add source traceability

- Put a nonspoken source-anchor line at the beginning or end of each segment.
- Add an inline nonspoken locator after every exact quotation, quantitative statement, medical or legal claim, and materially contested claim.
- Keep ordinary dialogue readable rather than tagging every sentence.
- Expand the complete evidence mapping in the source dossier.

Use this notation:

```text
[SOURCE ANCHORS: S1 pp. 4-6; S3 Results]
[SOURCE: S2 p. 11]
[FACT CHECK: unresolved sample-size discrepancy between S1 and S4]
```

Source markers and production cues are not spoken.

### 8. Close the episode

End with:

- a concise synthesis of the supported takeaways;
- the most important remaining uncertainty or open question; and
- at most one original listener reflection prompt or call to action.

Do not copy a show's branded closing ritual.

### 9. Build the selected packet

For a requested DOCX, create a Word production document; otherwise use the selected output format. Organize the packet in this order:

1. Episode Brief
2. Studio Script
3. Expanded Source Dossier
4. Sources and References
5. Studio Handoff Notes
6. Selected platform handoff, if requested

Complete and internally check the source and script sections before creating any requested platform handoff. Derive the final settings and prompt from the completed
Episode Brief, source ledger, claim-keyed evidence map, Studio Script, and
Studio Handoff Notes. Do not use the final section to introduce a new source,
claim, interpretation, or level of certainty.

For DOCX, use a compact reference-guide design with a restrained cover, real Word headings and page numbers. In any selected form, keep speaker labels clear, nonspoken cues distinct and long-form text readable.

Create a file only for an authorized file deliverable. Verify and use the destination selected for the task. If none is selected, follow the applicable verified recipient or project placement policy. If placement remains open, use the verified owner location. Keep Project or Area working material in its local `files/` or documented workspace. Use Resources for reusable references. Preserve established operational layouts. Ask once if a necessary owner or destination remains unresolved.

Use the selected filename or applicable verified naming convention. If neither provides one, use `YYYY-MM-DD_<topic>_podcast_production_packet.<extension>` with the selected format’s extension. Use a concise snake_case topic slug for the fallback name. Preserve existing packets. Use a version suffix when permitted by the authorized naming scope or resolve the collision before writing.

Return the selected packet and a usable link when it is a file. Do not save a separate Markdown copy unless the user asks.

### 10. Verify the packet

Run all four checks before delivery:

1. Source and claim fidelity.
2. Spoken-script and production usability.
3. Fidelity of the selected platform handoff, when requested.
4. Structure and rendering of the selected output format.

When DOCX is selected, render and inspect every page. Repair clipping, overlap, broken tables, speaker-label drift, missing glyphs, bad page breaks, and unreadable source markers before delivery.

## Outputs

### Episode Brief

Include:

- working title and optional subtitle;
- episode mode and listener promise;
- audience and assumed knowledge;
- central question;
- host functions;
- target runtime and estimated spoken-word count;
- source boundary and coverage summary;
- three to six takeaways;
- act or segment map; and
- known unresolved decisions.

### Studio Script

Match the selected speaker arrangement. The following is one two-speaker structure, not the default:

```markdown
## Studio Script

### Cold Open | Estimated 00:00-01:00
[SOURCE ANCHORS: S1, S2]

[MUSIC IN]

**HOST 1, GUIDE:** [Performable dialogue.]

**HOST 2, ANALYST:** [Performable response or question.]

[MUSIC OUT]

### Act 1: [Descriptive title] | Estimated 01:00-08:00
[SOURCE ANCHORS: S1 pp. 2-5; S3 Discussion]

**HOST 1, GUIDE:** [Dialogue.]

**HOST 2, ANALYST:** [Dialogue.]

[IMPROV WINDOW: clarify the distinction | approved points | source boundary S1, S3 | 45 seconds]
```

Estimated timestamps are planning aids, not guarantees.

### Expanded Source Dossier

Include:

1. Source Inventory
2. Source Cards
3. Claim-Keyed Evidence Map
4. Definitions and Protected Terminology
5. Limitations, Alternatives, and Uncertainty
6. Open Questions and Unsupported Gaps
7. Pronunciation and Spoken-Form Notes

### Sources and References

List all available citation information, stable links or paths, source coverage, and useful locators. When no external references are available, state that the packet is based on user-supplied material and that no external references were supplied or verified.

### Studio Handoff Notes

Include:

- host and casting functions;
- tone and delivery guidance;
- pronunciation notes;
- estimated runtime and rehearsal note;
- fact-check flags;
- rights-clearance flags for quotations, clips, and music;
- optional pickup lines or alternate transitions; and
- a note that the runtime remains an estimate until read aloud or rehearsed.

Keep sponsor or promotional copy separate from editorial copy. Add neither unless the user supplies or requests it.

### Optional NotebookLM Audio Overview

Include this section only when NotebookLM is the selected platform. Otherwise omit platform-specific settings and prompts.

Place this section last. It is a handoff for generating an Audio Overview, not
an instruction to operate NotebookLM or a substitute for the completed
production packet.

#### Suggested Settings

Use a compact two-column table:

| Setting | Recommendation |
| --- | --- |
| Format | `[Deep Dive, Brief, Critique, or Debate]` |
| Language | `[episode language]` |
| Length | `[Short, Default, or Long]` |
| Sources | `[exact selected source titles or best verified source identities]` |

Choose the recommendations as follows:

- Match Deep Dive, Brief, Critique, and Debate directly to the completed
  episode mode.
- Map Solo to Brief because NotebookLM does not offer a Solo format, and state
  that a Brief overview will not reproduce the complete scripted Solo episode.
- Map Interview to Deep Dive and state that NotebookLM will produce a
  two-host discussion rather than a true interview.
- Match the language to the completed episode.
- Choose Short, Default, or Long separately from the format mapping, using the
  approved runtime, information density, and episode mode. A Solo-to-Brief
  format mapping does not require the Short length setting. Treat NotebookLM's
  Shorter and Longer wording as equivalent when those labels appear. Never
  promise an exact generated runtime.
- For a non-English episode, state when the current interface does not offer a
  length control instead of inventing a setting.
- List the exact source titles that support the episode, or the best verified
  source identities when titles are unavailable. Include the production packet
  only when it will be uploaded as a NotebookLM source, and identify it as
  structural guidance rather than evidence. Exclude unrelated notebook sources.

#### Suggested Podcast Prompt

Before writing the prompt, create one concise spoken attribution label for
every selected source from the verified Source Inventory. Use natural language
that a listener can follow:

- For a paper, use the verified author name. Use both names for two authors and
  the lead author plus "and colleagues" for three or more authors, unless a
  verified consortium or group author is clearer.
- For a book, report, website, guidance document, dataset record, slide deck,
  transcript, or other source, use the verified individual creator, speaker,
  organization, agency, responsible issuing publisher, or other responsible
  source identity. Do not use a publication venue as though it authored a claim.
- If no author or responsible organization is available, use the exact source
  title or the most specific verified source identity. Do not invent an author,
  creator, affiliation, or publisher.
- When a point is a supported synthesis, name the contributing sources and
  present the connection as a synthesis rather than assigning it to one source.
- For an interpretation or open question, state whether it is source-authored.
  Otherwise label it as the episode's interpretation or open question, name the
  sources it draws from, and do not assign it to a source author.
- When one creator has multiple selected sources, add a verified year or short
  title only when needed to disambiguate them.

Make the prompt instruct the hosts to use these natural spoken attributions
so every source-derived claim or description has a clear nearby origin.
Introduce a source at first use and again when the source changes or ambiguity
returns; do not repeat the name in every sentence of a clearly attributed
passage. Never use the derivative production packet as evidence or cite it in
place of an original source.

Use this structured form:

```markdown
**Focus:** [One concise statement of what the AI hosts should emphasize.]

**Core Theme:** Address the central question: **"[source-supported central question]"**

**Source Attribution:** [Using the exact verified attribution labels, instruct the hosts to introduce each source at first use, repeat attribution when the source changes or ambiguity returns, preserve synthesis, interpretation, and open-question ownership, and never cite the production packet as evidence.]

**Key Discussion Points:**

**[Point label]:** [Source-supported explanation of the first major point, introducing or switching its natural spoken attribution here when needed.]

**[Point label]:** [Source-supported explanation of the second major point, introducing or switching its natural spoken attribution here when needed.]

**[Point label]:** [Additional source-supported point with attribution when needed.]

**Scientific Caution:** [The most important limitation, alternative, uncertainty, or inference boundary the hosts must preserve, attributed to its source when source-derived.]

**Audience:** [Intended expertise level and necessary background.]

**Structure:** [The approved progression of the episode.]
```

Keep the prompt concise and directly pasteable into NotebookLM's host-focus
field. Preserve the completed episode's terminology, evidence categories,
qualifications, and source boundary. Do not include internal claim IDs, source
anchors, production cues, formal parenthetical citations, reference-list
formatting, or dossier notation. Natural spoken source attribution is required
and is not citation clutter.

## Optional Subagent Delegation

Use this design when there are at least three substantial independent sources or the user explicitly requests parallel source analysis.

### Lane contract

- Assign each agent one distinct source or bounded source group.
- Keep every lane read-only.
- Give every lane the same source-card schema from Coverage and provenance.
- Require exact source identity, coverage, locators, evidence categories, and unresolved gaps.
- Do not let subagents draft script sections, create or save deliverables, rename source IDs, or make the final episode argument.
- Do not permit nested delegation.

### Parent contract

The owning skill remains the user-facing owner and must:

1. assign stable source IDs;
2. collect every lane;
3. deduplicate overlapping material;
4. reconcile or preserve material disagreements;
5. build the claim-keyed evidence map;
6. choose the episode structure;
7. write the complete script and improvisation windows;
8. prepare and verify the packet in the selected form, creating a file only within the authorized scope; and
9. report unresolved source or validity problems.

If the host cannot use subagents, run the same source-card work sequentially and retain the same parent-owned stitching and verification steps.

## Boundaries

- **Source is too sparse:** Build only what it supports, show the gaps, and ask whether the user wants a bounded supplemental search.
- **Sources disagree:** Preserve the disagreement, identify its basis, and make it part of the episode only when the evidence supports doing so.
- **Source has no references:** Treat it as user-supplied material, preserve its claims as such, and do not invent a bibliography.
- **Research paper needs a complete paper summary first:** Offer [research-summarizer](../research-summarizer/SKILL.md) as a separate next action. Do not invoke it automatically.
- **Request becomes manuscript revision:** Route the writing task to a research writing skill. Do not edit the manuscript inside this skill.
- **Request becomes interactive studying:** Route the learning session to [study-companion](../study-companion/SKILL.md). Do not turn a production packet into a tutoring loop.
- **Request asks for audio:** Explain that this skill prepares the studio script and source packet. Include generation instructions when the recipient requests a handoff for a selected platform. Audio generation and platform operation are outside this skill's scope.
- **NotebookLM mode is Solo or Interview:** Use the approved closest-format mapping in the final settings and state the mismatch explicitly.
- **NotebookLM length control is unavailable:** Record that the control is unavailable for the selected language or current interface and omit a fabricated recommendation.
- **NotebookLM source title is missing:** Use the best supported source identity
  recorded in the Source Inventory and mark the unresolved title. For multiple
  anonymous untitled sources, use neutral labels based only on verified type,
  date, topic, or supplied order, such as "the first supplied lab note."
- **NotebookLM author or creator is missing:** Use a verified organization,
  agency, responsible issuing publisher, named speaker, exact title, or other
  specific source identity. If none is available, identify the material by its
  supported source type and keep the missing identity visible in the dossier.
- **One creator has multiple selected sources:** Add a verified year or short
  title only when the spoken attribution would otherwise be ambiguous.
- **Selected DOCX tooling is unavailable:** State that the requested DOCX is blocked and offer usable alternatives, such as a complete review copy in a reply or a supported file format. Return the complete packet in an alternative form only if the recipient has requested or selected it. Saving remains subject to the destination and authorization rules above.
- **Protected private source:** Follow the access boundaries in `me.md`. Material the user manually pastes may be used only within the authorized request.
- **Existing output filename:** Preserve the existing packet. Use the next versioned filename when the naming scope permits it. If an exact filename is required and occupied, resolve an authorized alternative before writing.
- NotebookLM's current interface labels the length choices Short, Default, and Long.

## Checks

### Source fidelity

- Every source has a stable identifier and coverage statement.
- Every quotation, number, contested statement, and central factual claim is traceable.
- Source statements, synthesis, interpretation, and open questions remain distinguishable.
- Claims do not exceed the supplied evidence.
- Contradictions remain visible until they can be reconciled from source evidence.
- Unsupported gaps are labeled rather than completed speculatively.
- Technical constructs and non-substitutable terminology are preserved.

### Script quality

- The opening earns interest from the sources.
- The episode follows one coherent argumentative progression.
- Each act advances the central question rather than listing source summaries.
- Each selected speaker has a distinct communication function.
- Dialogue is pronounceable, conversational, and suitable for the selected audience.
- Technical detail remains accurate and is explained when needed.
- Improvisation windows are bounded and source-labeled.
- Production cues are sparse, audible, and actionable.
- The close states supported takeaways and remaining uncertainty.
- The script does not imitate an identifiable host, branded ritual, signature phrasing, or title formula.

### Production readiness

- The packet includes every required section in the required order.
- When requested, the selected platform handoff is last and contains settings and a prompt supported by that platform.
- Every prompt point and scientific caution is traceable to the completed packet without adding a new claim, source, interpretation, or certainty.
- Every source-derived claim or description in the prompt has a clear nearby
  verified attribution to its author, creator, speaker, organization,
  responsible issuing publisher, title, or other supported source identity.
- Supported synthesis, interpretation, and open questions preserve their
  evidence category and source basis without being misattributed to one source.
- An uploaded production packet is never presented as evidentiary authority or
  cited in place of an original source.
- No author, creator, organization, affiliation, publisher, or source identity
  is inferred when it is absent from the Source Inventory.
- When NotebookLM is selected, check its format, language, length and source recommendations against the episode. In that handoff, disclose unsupported Solo or Interview mappings and unavailable non-English length controls.
- The prompt is directly pasteable, keeps spoken attribution concise, and
  contains no internal source-anchor, formal citation, or production-cue
  clutter.
- Estimated timestamps and spoken-word count are internally consistent.
- Dense methodological detail that would disrupt speech is moved to the dossier or producer notes without hiding a necessary qualification.
- Pronunciation, fact-check, and rights-clearance flags are visible.
- A read-aloud pass checks overlong sentences, awkward referents, tongue-twisters, repetitive transitions, and timing.
- Every rendered page is free of clipping, overlap, broken layout, and missing text.

## References

- Austin Film Festival. (2019, June 19). *How to write a killer podcast script with Sarah Rhea Werner*. https://austinfilmfestival.com/blog/how-to-write-a-killer-podcast-script-with-sarah-rhea-werner/
- Buzzsprout. (2026, August 3). *How to write a podcast script [8 free script templates]*. https://www.buzzsprout.com/blog/write-podcast-script-examples
- The Diary of a CEO. (2026). *David Eagleman independent research & further reading* [PDF]. https://stevenbartlett.com/wp-content/uploads/2026/03/DOAC-David-Eagleman-Independent-Research-Further-Reading.pdf
- Google. (n.d.). *Generate Audio Overview in NotebookLM*. NotebookLM Help. https://support.google.com/notebooklm/answer/16212820
- Ruland, M. (2022, April 6). *How to write a podcast intro script that grabs attention*. LinkedIn. https://www.linkedin.com/pulse/how-write-podcast-intro-script-grabs-attention-molly-ruland
