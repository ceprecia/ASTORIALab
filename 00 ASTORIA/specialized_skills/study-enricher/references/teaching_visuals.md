# Teaching visuals and worked examples

Use visuals to make the current concept easier to understand, including details the source leaves out. These rules guide teaching, not paper summarization or research decisions.

## Choose a useful sequence

- Deep enrichment and full visual detail are the defaults. Use several complementary figures and examples when they explain different parts of the concept; there is no fixed figure count. A simple question may need only one picture or none.
- Start with the essential relationship, then add the mechanism, comparison, mathematical detail, or application. Place each visual next to the explanation it supports rather than collecting a gallery at the end.
- Carry one worked example through observations, a table or picture, notation, and calculation. Keep names, values, units, and assumptions consistent across representations. Add another example or counterexample when it exposes a different condition or misconception.
- Reuse a clear existing visual. When it leaves a gap, simplify it in stages or add a complementary view; a previous figure is not a reason to suppress a useful one. Identify omissions that would change the interpretation and restore them at the relevant next step.
- Respect the requested pace, scope, and settings. More visual support does not require more topics, compulsory questions, or a longer answer to a quick fact.

## Choose the medium

| Teaching need | Useful representation |
| --- | --- |
| Compare conditions, quantities, or worked steps | Markdown table, with units and comparable quantities |
| Explain relationships, a mechanism, or a sequence | Mermaid or another supported schematic, with the meaning of arrows stated |
| Understand numerical patterns or change a parameter | Checked runtime plot; an interactive example built by Study Planner when useful |
| Connect the idea to its mathematics | Equation in the selected or supported form with symbols defined, followed by a worked substitution or derivation |
| See a spatial arrangement or concrete object | Supported drawing or picture; a checked source-page link for a found image |

Use the selected equation form first, then the applicable verified convention. Where the format is open and LaTeX rendering is supported, use one `$$ ... $$` block per display formula, outside table cells. In a plain-text or unsupported host, use unambiguous notation and explain variables and grouping. Define unfamiliar terms and symbols before relying on them. Use the course's notation for exam work and explain consequential differences in outside material.

## Explain how to read it

- Give a short natural explanation of what the labels, axes, arrows, colors, or symbols mean and what to notice. Do not repeat definitions already established in the continuing example or require a separate caption template.
- Distinguish a variable's possible values from probabilities assigned to those values; distinguish probability mass from density when relevant. Say what uncertainty bars represent.
- Keep labels short and put longer explanations in adjacent prose. Break a crowded figure into views using the same notation rather than shrinking its text.
- State whether arrows show event order, dependence, information flow, an assumed model relationship, or a supported causal relationship. A diagram alone does not establish causation.
- For an order-only sequence, say that spacing does not represent duration. An equation or schematic should not silently supply a missing parameter or assumption.

## Make the basis clear

- Identify course or outside-source material with its source pointer. Distinguish a redraw or simplification from the source's original figure.
- Label invented numbers as a worked example, computed quantities as a calculation under stated assumptions, and generated data as a simulation. These are useful teaching tools, not observed research findings.
- Label a proposed or illustrative model as such. Model reasoning can explain or derive a result after its steps are checked; do not attribute that reconstruction to an unavailable lecture or source.
- Keep provenance brief and proportional. A single label may cover a continuing example; repeat it when the basis changes. Do not import the paper summarizer's source-only values, figure caps, or seven-part format.

## Check before returning

- Recompute numerical examples and derivations. Check assumptions, units, signs, scales, and limits; verify probability normalization or density area when that is the point of the lesson.
- Compare figures, tables, equations, and prose for the same quantities and conclusions. Preserve meaningful uncertainty and explain consequential omissions or transformations.
- Inspect rendered visuals where possible for cropped text, overlapping labels, ambiguous arrows, readable size, and distinctions that do not depend only on color.
- Use a format the current host supports. If rendering cannot be checked, say so and provide a useful table or text alternative; do not promise that executable HTML or SVG works in every host.
- Keep existing ownership: Study Planner builds interactive examples and handles requested saving. This reference does not create notes, permanent files, progress records, or new approval gates.

## Assessment adaptation

For Study Quiz and Study Planner's practice, include enough labels and context to interpret the question, but keep answer-revealing highlights, explanations, and completed derivations in the solution. Check the question and solution separately. Do not assume that an Obsidian diagram renders in Anki; use the quiz skill's export rules.
