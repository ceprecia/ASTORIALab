# Illustrative study explanation and answers

Authored illustrative output for the fictional MAP 101 materials. This is a worked example for comparison with an assistant's response. Every map value comes from the [supplied lesson](../inputs/lesson_and_practice.md).

## A short explanation

Read a coordinate as a location. Read a route as the connections you cross between locations. A1 → A2 → B2 contains three cells and two steps, so its distance is 400 metres.

The closure removes one connection, B1 ↔ C1. It does not remove the whole row or either endpoint. A useful first question is whether the proposed sequence crosses that exact edge.

For a different worked route, D1 → D2 → D3 → D4 crosses three open edges. It travels north for 600 metres.

## A practice interaction

An assistant could ask the learner to explain why A1 → B1 → C1 fails before showing a repair. A learner's answer should name the closed B1–C1 edge. If the learner only says that the route is too short, return to the closure rule and ask which connection is unavailable.

This example supplies the teaching move without recording a learner response or a completed study session.

## Answer key

| Question | Worked answer | Source |
| --- | --- | --- |
| 1 | Library is C1, east of Depot A1. The direct two-step eastward path crosses the closed B1–C1 edge. A direction and endpoint are insufficient to validate a route. | Lesson M1 and M3 |
| 2 | D3 → D4 moves north once, for 200 metres. | Lesson M1 and M2 |
| 3 | A1 → A2 → B2 → C2 → C1 uses four steps, for 800 metres. Another four-step route can also be correct. A two-step route would have to take both eastward edges along row 1, including the closed edge. A valid detour needs a northward step and a southward step in addition to two eastward steps, giving at least four. | Lesson M2 and M3 |
| 4 | Both listed routes are valid and cross four open edges, so both measure 800 metres. The source supplies no timing information with which to choose the faster route. | Lesson M2 through M4 |
| 5 | Both proposed steps are diagonal. M2 permits only horizontal or vertical moves between adjacent cells. | Lesson M2 |
| 6 | D1 → D2 → D3 → C3 → B3 ends at B3 after four steps, for 800 metres. None of those steps crosses B1–C1. | Lesson M1 through M3 |

## Self-check

Cover the answer table and explain three distinctions in your own words.

- A location versus a route.
- The number of listed cells versus the number of crossed edges.
- A shortest-distance claim versus a fastest-time claim.

Then check the exact rule in the lesson. Change the practice route or the closure only after stating the new convention, and recalculate the answer against it.
