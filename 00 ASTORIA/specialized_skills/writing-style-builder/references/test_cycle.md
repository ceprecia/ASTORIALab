# Profile test cycle

Run this after a profile is written or updated and before it is reported. The point is to find out whether the profile changes prose the way it claims to, on drafts written for the contexts it is meant for, and to adjust the rules until it does. It is a build step, not a gate for the user: the user sees the result in the report, not the drafts.

## Where the test lives

Keep temporary test drafts and working scores in an isolated workspace outside the vault and remove expendable drafts after the cycle. A requested report may be saved only to an authorized destination. The cycle itself does not authorize saving drafts, modifying sources or adding validation history to the profile.

## The three draft sets

1. **Situations.** Pick five to ten writing situations from the profile's "Writing context". For a scientific profile: an abstract, a discussion paragraph, a specific aims page, a limitations paragraph, a figure legend, a reviewer response, a methods paragraph. For an email or grant profile: the situations that profile names. Each situation gets a short brief (topic, audience, length, the numbers to include) so that all drafts of it carry the same content.
2. **Baseline drafts.** Write each situation without applying the candidate rules. Deliberately constructed stress examples may include the habits being tested; label them synthetic. If the author already knows the profile, do not describe the comparison as blind or independent.
3. **Applied drafts.** Write each situation again with the profile applied through the writing skill that will load it (the matching content-specific writer for scientific prose), following the profile's own procedure. Keep the content fixed; only expression changes.
4. **Controls.** Two or three passages of human-written text from the same contexts (the user's own paragraphs from a project note, a published methods paragraph). Controls are not rewritten; they are there to catch rules that fire on ordinary good prose.

## Scoring

For a **negative profile** with a checker: every baseline draft must fail, every applied draft must pass, every control must pass. Record hits per 500 words for each draft. A hit on a control or an applied draft that is correct usage is a false positive; a habit still visible in an applied draft that the checker did not name is a miss. Also read each applied draft once for what the checker cannot see (a repeated metaphor, a restated thesis, a closing summary nobody asked for) and count those as misses of the prose rules, not the script.

For a **positive profile** without a checker: tally, per rule, where it changed an applied draft relative to its baseline draft. A rule that changed nothing in any situation it targets is too vague or the situations missed its context; rewrite it with a concrete pattern and an example, or add the situation. A rule that changed meaning, evidence, or organization is outside the profile's scope and comes out. When the recipient selected combined use with another profile that has a checker, run that profile's checker on the applied drafts as well: a positive rule that pushes toward a banned habit (an intensity word in an example, a signposting phrase recommended as cohesion) is a contradiction and one of the two rules changes.

For **either kind**, check the profile's own text against the current user's actual `me.md`, any companion profile explicitly selected for this task, and the writing skill that applies it. Read the applicable wording and typography preferences; do not assume a particular user forbids dashes, emoji, or another style choice.

## Adjusting

- False positive in a checker: add the technical phrase to the default allow list if the field uses it, otherwise narrow the regex; never delete the rule for one case.
- Miss in a checker: add one regex for the tell, or a structural count when the tell is a pattern across sentences (anaphora, tricolons, one-line paragraphs, punchy fragments).
- Vague rule in prose: replace with the pattern, the tell, and the fix, and add the pair from the drafts to `references/patterns.md`.
- Two selected rules in conflict: compare their purpose, source and recipient-selected scope. Revise the inconsistent rule while preserving meaning; the writing skill owns application within that selection.
- After every change, rewrite the affected applied drafts and score again. The cycle ends when a full round (all situations, all three sets) ends with no rule change. Use as many bounded rounds as the current findings require; do not report an unperformed round or reuse a previous build's outcome as current validation.

## Second opinions

An optional independent reviewer can examine missed habits, false positives and
meaning changes. A checker pass, language-model perplexity or classifier score
does not establish authorship, scientific accuracy or overall writing quality.
Do not install or run another model merely to produce a style score.

## What to report

Report in the requested deliverable or recipient-selected form: the situations used, comparable results for baseline, applied and control sets, adjustments and their reasons, remaining judgment calls, cleanup performed and limitations. Preserve References for outside sources. A separate saved report or validation history requires authorization.
