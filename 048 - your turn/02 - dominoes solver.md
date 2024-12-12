# Dominoes Solver

__Puzzle:__ [Dominoes Solver](https://www.codingame.com/training/hard/dominoes-solver)

__Author:__ [@VilBoub](https://www.codingame.com/profile/bd6706892e49290fb119aa5ddae4238a318297)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ A Reasonable Challenge

# Visualizing the Problem

The goal of Dominoes Solver is to:

>find the disposition of [the] dominoes.

Did you ever do a color-by-number when you were young? Similar to the picture with numbers in the areas to color, we have a grid with numbers and we need to lay the dominoes down on the grid, making sure the numbers of the dominoes match up with the grid. It seems clear the actions we can take to solve the puzzle are simply putting each domino somewhere on the grid.

# Strategy

How do you distinguish one action from another? Is it enough to say “place a domino at location `(row=0, col=0)` on the grid”. No, it is not. Which domino are you placing at that location? How about “place domino `1-1` at location `(row=0, col=0)`”? That is still not enough! Are you placing the domino horizontally or are you placing the domino vertically?

When distinguishing actions for Algorithm X, it is critical that each action specification be enough to distinguish that action from all other actions. Remember too, only include legitimate actions. If there is a `2` at location `(row=0, col=0)`, you are not allowed to place domino `1-1` anywhere that covers `(row=0, col=0)`.

How about the requirements? We know from the __Output__ specification that all lines of output consist of only `|` or `=`, so we know the entire grid must be covered with dominoes. This seems similar to 9x9 Sudoku where the entire grid must be covered with numbers.

Just covering the grid is not enough. There is another category of requirements you will need to distinguish to complete a model for Algorithm X. What else __must happen__ to build a full solution? I’ll give you a hint: the number of requirements in the second category of requirements is equal to `(n + 1) * (n + 2) / 2`.

Dominoes Solver is a beautiful example of Exact Cover. All dominoes must be used, but no two dominoes are allowed to overlap. All spaces on the grid must be covered. The numbers on the grid must be properly covered by matching dominoes. From a modeling perspective, Dominoes Solver is a perfect opportunity to increase the model complexity a bit before moving into the next category of Exact Cover problems, _Generalized Exact Cover_.
