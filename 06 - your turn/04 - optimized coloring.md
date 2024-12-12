# Optimized Coloring

__Puzzle:__ [Optimized Coloring](https://www.codingame.com/training/medium/optimized-coloring)

__Author:__ [@Oflopy78](https://www.codingame.com/profile/78597a36a97776323b29c41b0e314f1c8444555)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ If At First You Don't Succeed, Try Again!

# Identifying Zones

Before putting any thought into an Algorithm X approach to this puzzle, the cells of the picture must be organized into zones. From the problem statement:

>Having an empty sheet of paper divided into some zones

>A zone is made of "space" characters.

I will move forward assuming you have created a list of zones where each zone is a list of row, col `(r, c)` `tuple`s. Each `(r, c)` `tuple` identifies one “space” character found in the zone. Again from the problem statement:

>two adjacent zones must be filled with two different colors.

Let’s call “two adjacent zones” a set of neighbors and let’s rephrase the statement above as:

>two neighbors must never be filled with the same color

Algorithm X needs to know every set of neighbor zones so it can make sure no neighbors are ever assigned the same color. And, how do we ensure something doesn’t happen? Correct! Mutual exclusivity.

<details>
<summary>Spoiler Alert: Python suggestions for finding neighbor zones.</summary>
<br>

You need to look at every combination of 2 zones and determine if those two zones are neighbors. This is a great opportunity to use `itertools.combinations`.

```python
# assumed data structure
# zones : List[List[tuple]] – each zone in zones is a list of (r, c) tuples

from itertools import combinations

neighbors = []
for zone_1, zone_2 in combinations(zones, 2):
    for (r1, c1) in zone_1:
        for (r2, c2) in zone_2:
            if the two cells indicate the zones are neighbors:
                add (zone_1, zone_2) to the list of neighbors
                stop checking and move on to the next combination of zones
```

If you really want to make your code “Pythonic”, try this:

```python
# assumed data structure
# zones : List[List[tuple]] – each zone in zones is a list if (r, c) tuples

from itertools import combinations

neighbors = []
for zone_1, zone_2 in combinations(zones, 2):
    if any((r1, c1, r2, c2 indicate zones are neighbors) for (r1, c1) in zone_1 for (r2, c2) in zone_2):
        add (zone_1, zone_2) to the list of neighbors
```

The code is still very readable, but the use of `any` has shortened the code and eliminated the need to do further checking to break out of the nested `for` loops.
</details>

In the Python code above, I have intentionally left out the details needed to replace `(r1, c1, r2, c2 indicate zones are neighbors)` with code. Several CodinGamers have asked for clarification on how to determine when two zones are neighbors and when they are not neighbors. Almost every puzzle on CodinGame has a discussion tab and if you need more help determining neighbors, click [here]( https://www.codingame.com/training/medium/optimized-coloring/discuss) to open this puzzle’s discussion tab.

# Algorithm X Setup

This puzzle asks us to find the __least__ number of colors with which the picture can successfully be colored without any two neighbor zones having the same color. Depending on where you are in your Algorithm X journey, something might seem a bit odd. Compare this puzzle’s request to another _hypothetical_ puzzle that might ask:

>Given 5 different colors, find all possible ways a picture can be colored, such that no two neighbor zones are colored the same.

In this _hypothetical_ puzzle, what are the requirements? Each zone must be colored. How do we make sure no two neighbors are colored the same? We create an optional requirement to handle mutual exclusivity for every color for every set of neighbors. For instance, assume zone 1 and zone 2 are neighbors. If zone 1 is assigned color 1, then zone 2 must not be assigned color 1. This sentence could be restated as: If zone 1 and zone 2 are neighbors, one or the other can be assigned color 1, but not both.

Assuming the problem has `x` zones and `y` colors, there are `x * y` actions. Each action assigns a specific color to a specific zone. Each action then covers exactly one requirement and 0 or more `me_requirements` that make sure none of the neighbors receive the same color.

Knowing how to approach this hypothetical puzzle should put you on a path to solving [Optimized coloring]( https://www.codingame.com/training/medium/optimized-coloring). If you are stuck and want further guidance, click below.

<details>

<summary>Spoiler Alert: Transitioning from the hypothetical puzzle to the actual puzzle.</summary>
<br>
    
The thought exercise above asked you to position Algorithm X to find all solutions to a hypothetical problem using 5 distinct colors. What if the solver returns zero solutions? There are no proper ways to color the entire picture with only 5 colors. If you really need to get this picture colored, what should you try next?

<details>
<summary>Spoiler Alert: Quit being so cryptic. Just tell me what to do!</summary>
<br>

I really thought about providing more details, but I believe the hypothetical problem and the questions above are enough of a push in the right direction. Good luck!
</details>
</details>

