# Week 2 approved source pack

Fictional tutorial input, version 1.0. The Parcel Table is an invented classroom exercise. The definitions and rules below are the complete reference set for this activity, rather than empirical claims about teaching effectiveness or an operational delivery service.

## T1. What a complete procedure contains

In this exercise, a procedure gives another reader four things.

1. Starting conditions. Identify the object, required labels and available recording material.
2. Ordered actions. Make each action possible from the state left by the preceding action.
3. Decision rules. State which condition to check first when more than one rule could apply.
4. A completion check. Give the reader a way to verify the result and know when to stop.

Before handling each mock parcel, begin with one parcel at Intake, three trays visibly labelled Blue, Red and Hold, and a register with space for one result. Read both the parcel's size field and fragile field. A label is complete only when both fields are legible and each has one permitted value.

Permitted size values are small and large. Permitted fragile values are yes and no. A missing field, an unreadable field or another value makes the label incomplete for this exercise.

## T2. Routing policy and its priority

Apply these rules in order.

1. If the label is incomplete, place the parcel in Hold. Its register code is H.
2. Otherwise, if fragile is yes, place the parcel in Blue, regardless of size. Its code is B.
3. Otherwise, if size is large, place the parcel in Red. Its code is R.
4. Otherwise, place the small, non-fragile parcel in Blue. Its code is B.

The first matching rule supplies the destination. Continue to the recording and completion check after selecting that destination.

## T3. Recording and completion

Write one code, B, R or H, in the parcel's register row. Compare that code with the actual tray label. When they agree, mark the parcel complete and stop processing it. If they disagree, correct the tray or code against the selected routing rule, check again, and then mark complete.

## T4. A worked case

Parcel P0 has a legible size value of large and a fragile value of no. Its label is complete, so rule 1 does not select Hold. Rule 2 does not select Blue because fragile is no. Rule 3 selects Red. Place P0 in Red, write R, verify that the tray and code agree, and mark it complete.

## Why wording changes the result here

Compare “If large, use Red” with “After confirming the label is complete and fragile is no, use Red for a large parcel.” The first version would send a large fragile parcel to Red. The second preserves the earlier fragile rule. The activity asks the reader to make that priority executable in the written steps.
