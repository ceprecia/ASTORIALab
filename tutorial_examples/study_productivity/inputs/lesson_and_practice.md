# Week 1 lesson and practice

Fictional tutorial input. Cedar Vale, its map and the closure below are invented. The rules define this exercise; the distances describe this fictional grid.

## Lesson

### M1. Read the coordinate before choosing a route

The grid has columns A through D from west to east and rows 1 through 4 from south to north. North is up. A coordinate names the column first and row second.

```text
                 NORTH
                   ^
       A      B      C      D
4      .      .      .    Clinic
3    Garden   .      .    Tower
2      .      .      .      .
1    Depot    .    Library  .
```

Depot is A1, Library is C1, Garden is A3, Tower is D3 and Clinic is D4. Every dot is a usable cell. A place name occupies one cell.

### M2. Count edges to calculate distance

A route moves between horizontally or vertically adjacent cells. Diagonal steps are outside this exercise's rules. Each permitted step crosses one edge and measures 200 metres.

For example, D1 → D2 → D3 takes two northward steps. Its distance is 2 × 200 = 400 metres. Three cells appear in that route, but only two edges are crossed.

### M3. Apply the closure in either direction

The edge joining B1 and C1 is closed. A route cannot cross that edge from either side. Other edges joining adjacent grid cells are open. The closure blocks that connection, while B1 and C1 remain usable through their other neighbours.

The overall direction from Depot to Library is east. The direct route A1 → B1 → C1 would cross the closed edge, so overall direction alone does not identify a valid route.

### M4. Keep the comparison criterion visible

The map supports distance comparisons. It supplies no walking speeds, waiting times or crowd information. Equal distances therefore support an equal-distance conclusion. They do not establish equal travel times.

## Practice questions

1. Give Library's coordinate and its overall direction from Depot. Explain why those facts alone do not establish a valid route.
2. Give the direction and distance of Tower → Clinic.
3. Find a shortest valid route from Depot to Library. Give its cell sequence, step count and distance, and explain why two steps will not work.
4. Compare A1 → A2 → B2 → C2 → C1 with A1 → B1 → B2 → C2 → C1. Is either shorter? Can this source establish which is faster?
5. A learner proposes A1 → B2 → C1 as a shortcut. Which rule decides whether it is valid?
6. Starting at D1, move two cells north and then two cells west. Give the final coordinate and total distance. Check every step against the closure.

## Work before checking

Try the questions from these inputs first. The tutorial's separate illustrative explanation and answers provide a worked comparison after an attempt.
