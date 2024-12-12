# Hitori Solver

__Puzzle:__ [Hitori Solver](https://www.codingame.com/training/hard/hitori-solver)

__Author:__ [@VilBoub](https://www.codingame.com/profile/bd6706892e49290fb119aa5ddae4238a318297)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ A Crossroads of Multiplicity Might Have Your Eyes Crossing

# Strategy

My solution for Hitori Solver is surprisingly similar to Mrs. Knuth – Part III. The goal statement is extremely short:

>* Each puzzle consists of a square grid with numbers appearing in all squares. The object is to shade squares so:
>    * No number appears in a row or column more than once.
>    * Shaded squares do not touch each other vertically or horizontally.
>    * When completed, all un-shaded squares create a single continuous area.

What are the action steps that can be taken to build a solution?

>_The object is to shade squares._

What are the requirements?

>_No number can appear in a row or column more than once._

Is there any mutual exclusivity?

>_Shaded squares must not touch vertically or horizontally._

Will solutions need to be processed to determine if they are valid?

>_When completed, all unshaded squares must create a single continuous area._

Thank you [@VilBoub]( https://www.codingame.com/profile/bd6706892e49290fb119aa5ddae4238a318297) for making the goal statement line up with the questions I had in my head already!

Let’s dig into the requirements a bit more. Consider the Example Test Case:

```text
    111
    234
    224
```

We see three `1`s in the first row. Two of those `1`s will need to be shaded. Of course, requirements need to be specific and with Algorithm X, multiplicity is handled with multiple requirements. It is more proper to say that the requirements include removing a `1` from the first row for the first time and removing a `1` from the first row for the second time. Two separate requirements need to be satisfied.

The only action that can be taken to build a solution is to shade a cell. Will you then create an action for every cell on the gameboard? Probably not. There is no reason to ever shade a cell unless the number in the cell appears more than once in its row _or_ its column.

This puzzle has a unique multiplicity twist not seen in other puzzles and you will run into it when you are identifying the requirements satisfied by each action. Consider the grid for __Test Case 4: Even Bigger__:

```text
    22153
    23145
    11135
    13542
    54321
```

Would you ever shade the top-left corner? It is definitely possible. There are multiple `2`s in the row and multiple `2`s in the column. Shading the top-left corner covers requirements associated with the row _and_ requirements associated with the column.

What about the second `2` in the top row? Absolutely possible. However, shading the top row, second from the left removes a `2` from the top row, but what does it do for the column? The answer is nothing! There is only a single `2` in the column. Shading that square does not cover any column requirements because there are no column requirements involving removing a `2` from the second column from left.

The tricky part of this puzzle is that every square you might want to shade could do any of the following:

-	Remove a problem number from both the row and the column.

-	Remove a problem number from just the row.

-	Remove a problem number from just the column.

This creates a potential crossroads of multiplicity at each grid location, which is unique to this puzzle and you will need to take all these scenarios into consideration when identifying the requirements satisfied by each action.

I hope it is obvious you will need some optional requirements to make sure no two squares that touch are both shaded.

# Memory

Even without memory, Algorithm X is able to find solutions extremely fast, especially since you can `break` as soon as your solver returns a solution, assuming you have validated that solution by overriding the `_process_solution(self)` method. Adding memory reduced my solver’s time to find a solution by roughly 30% to 40%, but this is a little challenging to measure due to how fast Algorithm X finds the solutions even without memory.
