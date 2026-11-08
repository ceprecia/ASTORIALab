---
name: skill-name
description: >-
  What the skill owns, in its own verbs, in one or two sentences. One sentence
  on when to use it and what it never does or where it returns. Triggers: phrase
  one, phrase two, phrase three.
metadata:
  level: skill
  system: System Name
  part: ""
  family: ""
  modality: ""
  population: ""
  dependencies: ""
  requires: ""
  gates: ""
  created: "YYYY-MM-DD"
  updated: "YYYY-MM-DD"
---

# Skill Name

One short tagline in the user's voice.

## Purpose

What the skill does and what it never does, when the description needs more
room. Then the request patterns it answers and the ones it sends elsewhere.

## Inputs

- What it needs before starting, what it asks for, what it assumes.

## Steps

1. Numbered steps the AI follows.
2. Where it pauses (the `gates` in the frontmatter, if any).
3. What it hands back and to whom.

For skills that create source files, include a creation-time pointer to the
vault-root `00 ASTORIA/templates/code_template.md`. Omit this for other skills.

## Outputs

State the output, destination and name, and what stays in chat.
Distinguish bounded updates from full artifacts; include only needed fields.

## Boundaries

- Hard rules, protected surfaces, stops, and the odd cases, including any rule the user supplied. Say "the user", never their name; note style and writing profiles come from `me.md`, not from rules here.

## Handoffs

- What it owns and what it sends to which skill. Delete when the Purpose says it all.

## Checks

- How the skill verifies its own result before returning. Delete when there is nothing to verify.

## References

- Delete this section when nothing outside the vault is cited.
- Adapted from: Author, A. A. (Year). *Title* (Version) [Computer software]. Publisher. URL (MIT License)
- Author, A. A., & Author, B. B. (Year). Title of article. *Journal Name, volume*(issue), pages. https://doi.org/...
