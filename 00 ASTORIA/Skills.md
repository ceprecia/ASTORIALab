---
related:
  - "[[Skill Map]]"
created: 2026-03-05
updated: 2026-09-23
---
Every skill in `00 ASTORIA/skills/` as a live table, read straight from each skill's `SKILL.md` frontmatter: level, system, part, family, modality, population, requirements, gates, and trigger phrases. Nothing here is maintained by hand. For the agent-facing index see [Skill Map](Skill%20Map.md); for how to add a skill see [skill-builder](skills/skill-builder/SKILL.md).

The live table needs Obsidian Bases. Outside Obsidian, use the linked Skill Map above.

The formulas read the nested `metadata` block with `note.metadata.<key>`; if a column shows empty, that is the first thing to check in the Base editor.

```base
filters:
  and:
    - file.inFolder("00 ASTORIA/skills")
    - file.path.endsWith("/SKILL.md")
formulas:
  skill: link(file.path, file.folder.replace("00 ASTORIA/skills/", ""))
  level: note.metadata.level
  system: note.metadata.system
  part: note.metadata.part
  family: note.metadata.family
  modality: note.metadata.modality
  population: note.metadata.population
  requires: note.metadata.requires
  gates: note.metadata.gates
  dependencies: note.metadata.dependencies
  updated: note.metadata.updated
  summary: description.split(". ").slice(0, 1).join("")
  triggers: description.split("Triggers:").slice(1).join("")
properties:
  formula.skill:
    displayName: Skill
  formula.level:
    displayName: Level
  formula.system:
    displayName: System
  formula.part:
    displayName: Part
  formula.family:
    displayName: Family
  formula.modality:
    displayName: Modality
  formula.population:
    displayName: Population
  formula.requires:
    displayName: Requires
  formula.gates:
    displayName: Gates
  formula.summary:
    displayName: What it does
  formula.triggers:
    displayName: Triggers
  formula.dependencies:
    displayName: Depends on
  formula.updated:
    displayName: Updated
views:
  - type: table
    name: All skills
    order:
      - formula.skill
      - formula.level
      - formula.part
      - formula.family
      - formula.modality
      - formula.summary
      - formula.triggers
    groupBy:
      property: formula.system
      direction: ASC
    sort:
      - property: formula.level
        direction: ASC
      - property: file.folder
        direction: ASC
    rowHeight: tall
  - type: table
    name: Companions and coordinators
    filters:
      or:
        - formula.level == "companion"
        - formula.level == "coordinator"
    order:
      - formula.skill
      - formula.level
      - formula.part
      - formula.summary
      - formula.triggers
    sort:
      - property: formula.level
        direction: ASC
      - property: formula.part
        direction: ASC
  - type: table
    name: Part 1 scout the field
    filters:
      and:
        - formula.part == "1"
    order:
      - formula.skill
      - formula.family
      - formula.summary
      - formula.triggers
  - type: table
    name: Part 2 challenge the question
    filters:
      and:
        - formula.part == "2"
    order:
      - formula.skill
      - formula.family
      - formula.summary
      - formula.triggers
  - type: table
    name: Part 3 stress-test the design
    filters:
      and:
        - formula.part == "3"
    order:
      - formula.skill
      - formula.family
      - formula.modality
      - formula.population
      - formula.requires
      - formula.triggers
    groupBy:
      property: formula.family
      direction: ASC
  - type: table
    name: Part 4 analyze the data
    filters:
      and:
        - formula.part == "4"
    order:
      - formula.skill
      - formula.family
      - formula.modality
      - formula.requires
      - formula.gates
      - formula.triggers
    groupBy:
      property: formula.family
      direction: ASC
  - type: table
    name: Part 5 write report reproduce
    filters:
      and:
        - formula.part == "5"
    order:
      - formula.skill
      - formula.family
      - formula.summary
      - formula.triggers
  - type: table
    name: Requirements and gates
    filters:
      and:
        - formula.requires != ""
    order:
      - formula.skill
      - formula.part
      - formula.requires
      - formula.gates
    sort:
      - property: formula.part
        direction: ASC
      - property: file.folder
        direction: ASC
```
