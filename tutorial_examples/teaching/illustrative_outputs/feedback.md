# Illustrative feedback draft

Authored illustrative output for Sample learner K's invented submission. The proposed score uses the [supplied rubric and work](../inputs/activity_rubric_and_student_work.md), with the [Week 2 rules](../inputs/week_02_sources.md) as its content basis. It is a draft for the fictional instructor's review.

## Proposed rubric score

| Criterion | Score | Evidence and reasoning |
| --- | --- | --- |
| A. Starting conditions | 1 of 2 | “Read the size label” names an input. The draft leaves the fragile field, label completeness, tray labels and register preparation unchecked. This fits the partial starting-check anchor. |
| B. Action sequence | 2 of 2 | Steps 1 through 4 give a followable read → select → record sequence for a parcel with a readable size. The routing policy defects are assessed separately under C. |
| C. Rule priority | 0 of 2 | “If the parcel is large, put it in Red” checks size first. Both the incomplete-label and fragile priority cases are missing, matching the zero-point anchor. |
| D. Completion check | 1 of 2 | “Write R or B to match the tray you used” provides a record, but it omits an explicit verification action and completion condition. |
| **Total** | **4 of 8** | Sum of the four stated criteria. |

The required case traces are also missing. Report that completeness finding alongside the rubric result. The supplied scoring rules provide no additional numerical trace penalty.

## How the draft behaves on the supplied cards

| Card | Result supported by the draft | Expected result | Finding |
| --- | --- | --- | --- |
| P1, small and non-fragile | Blue and B | Blue and B | Correct for this case |
| P2, large and fragile | Red and R | Blue and B | Size was checked before the fragile rule |
| P3, missing size | No defined next step after attempting to read size | Hold and H | An explicit incomplete-label branch is needed |

## Feedback to the fictional learner

Your draft has a readable sequence and includes a register entry. Its main gap is rule priority. For P2, step 2 selects Red as soon as it sees large, but the source sends a fragile parcel to Blue before considering the remaining size rule. P3 also needs a route when the size field cannot be read.

Make two priority revisions.

1. Check both fields in the opening and handle an incomplete label first. Then place the fragile rule before the remaining size choice.
2. Add an action that checks the register code against the tray and marks the parcel complete.

Supply the three traces so a reader can see which step determined each result.

## One corrected procedure for comparison

1. Begin with one parcel at Intake, labelled Blue, Red and Hold trays, and a register row. Read the size and fragile fields.
2. If either field is missing, unreadable or outside its permitted values, put the parcel in Hold and select code H. Continue to step 5.
3. Otherwise, if fragile is yes, put the parcel in Blue and select code B. Continue to step 5.
4. Otherwise, put a large parcel in Red with code R, or a small parcel in Blue with code B.
5. Write the selected code in the register. Compare it with the actual tray label. Correct a mismatch using the routing rule, then check again.
6. When tray and code agree, mark complete and stop processing that parcel.

This comparison illustrates a complete revision. Different wording can satisfy the same rubric when it preserves the source's conditions and rule order.
