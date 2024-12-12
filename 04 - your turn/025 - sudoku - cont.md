# Alternative Approaches

The following 3 options always leave Algorithm X in charge. Instead of preselecting any cells of the Sudoku, Algorithm X will be instructed to __try__ to put certain values in certain cells. Algorithm X is great at “trying” things. After all, that is the general idea of any backtracking technique.

# Option 1: Restrict Possible Actions

Rather than preselecting certain cells, restrict Algorithm X to a single option for those cells. Algorithm X will immediately select these options because there are no other paths forward. For instance, to restrict the possible actions in a 9x9 Sudoku, loop through all the cells of the grid. If the cell is empty, add 9 possible actions. If the cell already has a value, only add a single action. The pseudocode looks like this:

```text
    for each cell in the grid
        if the cell is empty
            possible values = all possible values
        else
            possible values = cell value

        for each value in possible values
            add an action for placing this value in this cell
```

Algorithm X will immediately select the actions associated with pre-filled cells because they are the only actions that cover the requirements that values be placed in those cells. Notice that the process of restricting the option does not need to be exhaustive. At this time, the goal is to simply force Algorithm X to choose preselected options. The goal is not to perfectly minimize the full list of options available to Algorithm X.

# Option 2: Use Hints

If you search the internet for DLX Sudoku solutions, you will find solutions that use hints to guide Algorithm X. Rather than restricting the options available to Algorithm X, hints are used to force Algorithm X to make certain selections. Each hint is a must-be-covered requirement, and each hint is covered by a single action, giving Algorithm X no choice but to select the actions associated with the hints. The pseudocode looks like this:

```text
    for each cell in the grid
        if the cell is prefilled
            add a new requirement -> (‘hint’, row, col)
        for v in all possible values
            add an action for placing v in the cell
            if the cell is prefilled and v = the cell's prefilled value
                add the new "hint" to the list of satisfied requirements
```

I have not used hints as part of an exact cover solution, but you will run into this technique if you study other Algorithm X solutions found online.

# Option 3: Give Algorithm X a Partial Problem

In some puzzles, a portion of the solution can be determined before Algorithm X begins backtracking and what remains for Algorithm X feels like a puzzle that can stand alone. In these cases, I have chosen to maintain a list of actions that must be part of the final solution, while then giving Algorithm X a smaller version of the problem to solve. The smaller problem feels identical to the larger problem in all ways except size. Later in the playground, I will identify a couple of puzzles where this third technique fits much better than the first two alternatives.
