---
related: []
created: 2026-11-23
---

# Seedling watering report: source brief

This is an original fictional writing exercise. Every pot and numerical value is synthetic. No plants were grown or measured to produce this packet. These files demonstrate source-grounded writing and do not provide plant-care advice.

## F1: Question and writing task

The fictional question is: How did the 14-day height change differ between the eight pots assigned to the two watering amounts in this example?

The requested output is a short report for research readers, at most 450 words, with Question, Methods, Results and Limitations sections. Revise the [rough report](rough_report.md) using only this brief and the [synthetic data](plant_height_data.csv). Preserve the synthetic status. No literature review, new analysis or external citation is needed.

## F2: Fictional procedure

- Eight seedling pots belonged to one fictional seed batch and used the same stated pot size and potting mix.
- Four pots received 20 mL of water per day and four received 40 mL per day for 14 days.
- Each watering group occupied one separate tray. The record does not document random assignment, position rotation or blinded measurement. Watering amount and tray position therefore cannot be separated in this design.
- Height was recorded at day 0 and day 14, in centimetres, to one decimal place. All eight synthetic records are present. No exclusion was made.
- Light exposure, temperature and soil moisture were not measured. The packet contains no further procedural records.

## F3: Outcome definition

The outcome is each pot's **height change**, calculated as day-14 height minus day-0 height, in centimetres. A larger positive value means a larger increase in recorded height over the 14 days.

The data do not measure plant health, biomass, survival, yield or water-use efficiency. The watering amount was doubled from 20 to 40 mL per day. That does not mean height change doubled.

## F4: Supplied descriptive summary

These arithmetic summaries are supplied as the writing exercise's result record. They describe the synthetic rows in `plant_height_data.csv`.

| Water per pot per day | Pots | Mean day-0 height (cm) | Mean day-14 height (cm) | Mean height change (cm) | Range of height change (cm) |
| --- | ---: | ---: | ---: | ---: | --- |
| 20 mL | 4 | 5.0 | 8.3 | 3.3 | 3.0 to 3.4 |
| 40 mL | 4 | 5.0 | 9.1 | 4.1 | 4.0 to 4.2 |

The difference in mean height change is **0.8 cm**, calculated as 4.1 minus 3.3, with the 40 mL group as the first term. Each mean gives equal weight to the four pots in that group. No statistical test, confidence interval or population estimate is supplied.

## F5: Claim limits

The report can describe the two groups and their numerical difference. It cannot conclude that the watering amount caused that difference, because tray position is confounded with watering amount and the other conditions were not measured.

The report cannot establish statistical significance, an optimal watering amount, a biological mechanism or a recommendation for other plants. No real study, preregistration or published reference is represented by this packet.

## F6: What the learner should return

First, make a table linking the rough report's claims to F1-F5 or to specific pot records, and identify unsupported claims. Then revise the report. Keep unknown details unknown rather than filling them with plausible procedures.

The separate `illustrative_outputs/` folder contains a hand-authored comparison answer. It is not a source input or a record of an assistant executing this workflow.
