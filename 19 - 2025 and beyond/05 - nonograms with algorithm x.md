# Nonogram Inversor with Algorithm X

__Puzzle:__ [Nonogram Inversor](https://www.codingame.com/training/hard/nonogram-inversor)

__Author:__ [@LaurentBouvier](https://www.codingame.com/profile/6061d439c21bc69dacb351d2dae6ccda742965)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Quite Challenging


# Strategy

My Algorithm X approach does not do any problem-space reduction before searching for a solution. In the end, I looked at the problem in a way that did not occur to me until another CodinGamer made a comment that sent me down a path I never considered.

As I alluded to on the previous page, I eventually gave up on placing an entire line of cells on the Nonogram gameboard all in a single action. I will go through my approach in steps in case just one or two hints help you cross the finish line.

<details>
<summary>Hint #1: A Little Inspiration from @VizGhar</summary>

In a Discord message, [@VizGhar](https://www.codingame.com/profile/c152bee9fe8dc90ac4f6b84505b59ebb9086993) said to me:

>My actions are:
> * Placing [segments] vertically/horizontally marking those spaces for half a point.
> * Placing empty spaces for full point.

Although I don’t use “points”, his idea of 1/2 points and full points led me to my eventual solution, which I think feels very elegant, __primarily__ because of his points idea.

</details>


<details>
<summary>Hint #2: Reverse Engineering</summary>

To understand how I set up my Algorithm X matrix, consider the following debug output for __Test Case 1 - Dog__:

```
len(actions)=65
len(requirements)=63
len(me_requirements)=4
```

</details>

<details>
<summary>Spoiler #1: Tiles on a Gameboard</summary>

Following @VizGhar’s lead, my tiles are either `Segment`s or single white space cells. The entire Nonogram gameboard must be covered by some combination of `Segment`s and white spaces. Placing a `Segment` on the gameboard never includes any white space and placing a white space on the gameboard never covers any more than a single 1x1 cell.

</details>

<details>
<summary>Spoiler #2: Requirements</summary>

@VizGhar had a great idea with his 1/2 points and full points. All I did was convert that idea to language that felt closer to what I had done on all the puzzles before.

<details>
<summary>Show me the money!</summary>

<BR>

* All cells must be covered horizontally.
* All cells must be covered veritcally.
* All segments must be placed on the gameboard.

</details>

</details>

<details>
<summary>Spoiler #3: Actions</summary>

I cannot take much credit for this. My actions match @VizGhar's actions exactly. It is unusual for me to have two different types of actions, but to cover the entire gameboard, it worked nicely here.

* place segment
* place white space

Where this really gets interesting is in the process of identifying a full list of locations that are options for the placement of each segment. Based on the other segments in the line, the options are limited.

</details>

<details>
<summary>Spoiler #4: Mutual Exclusivity</summary>

For any two contiguous segments. Each action of placing segment 1 (action 1) must be considered with each action of placing segment 2 (action 2). These actions are mutually exclusive if:

1. The two segments do not overal at all.
2. Segment 2's placement is earlier than the right end of segement 1 + two spaces.

</details>
