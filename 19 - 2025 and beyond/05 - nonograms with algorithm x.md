# Nonogram Inversor with Algorithm X

__Puzzle:__ [Nonogram Inversor](https://www.codingame.com/training/hard/nonogram-inversor)

__Author:__ [@LaurentBouvier](https://www.codingame.com/profile/6061d439c21bc69dacb351d2dae6ccda742965)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Quite Challenging


# Strategy

My Algorithm X approach does not do any problem-space reduction before searching for a solution with Algorithm X. In the end, I looked at the problem in a way that did not occur to me until another CodinGamer made a comment that sent me down a path I never considered.

As I alluded to on the previous page, I eventually gave up on placing an entire line of cells on the Nonogram gameboard all in a single action. I will go through my approach in steps in case just one or two hints help you cross the finish line.

<details>
<summary>Hint #1: A Little Inspiration from @VizGhar</summary>

In a Discord message, [@VizGhar](https://www.codingame.com/profile/c152bee9fe8dc90ac4f6b84505b59ebb9086993) said to me:

>My actions are:
>placing whole lines vertically/horizontally marking those spaces for half a point
>Placing empty spaces for full point

Although I don’t use “points”, his idea of 1/2 points and full points led me to my eventual solution, which I think feels very elegant, __primarily__ because of his points idea.

</details>


<details>
<summary>Hint #2: Reverse Engineering</summary>

To understand how I set up my Algorithm X matrix, consider the followign debug output for __Test Case 1 - Dog__:

```
len(actions)=65
len(requirements)=63
len(me_requirements)=6
```

</details>

<details>
<summary>Spoiler #1: Tiles on a Gameboard</summary>

Fill the entire gameboard by placing groups of black cells or 1 x 1 white space cells on the gameboard.

</details>

<details>
<summary>Spoiler #2: Actions</summary>

* place segment
* place white space

</details>

<details>
<summary>Spoiler #3: Requirements</summary>

* All cells must be covered horizontally.
* All cells must be covered veritcally.
* All segments must be placed on the gameboard.

</details>
