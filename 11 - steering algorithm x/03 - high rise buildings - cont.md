# High-Rise Buildings (cont.)

For some problems, it is beneficial to keep track of an updated problem space so Algorithm X can be guided away from dead ends. [High-Rise Buildings]( https://www.codingame.com/training/expert/high-rise-buildings) is a perfect candidate puzzle for this strategy.

Each time Algorithm X chooses a row from the matrix to make part of the solution, we will update the grid of the city to reflect the height assigned to one of the buildings. If any part of the grid indicates one of the `CityView`s is invalid, Algorithm X can be redirected.

I am making a bit of an assumption that you came up with the same actions for Algorithm X that I believe are necessary. What are the tiles that can be placed on the gameboard? The only option for those tiles I see is that each tile is a height that is assigned to a building by putting that tile on one of the gameboard's `(row, col)` coordinates. Building on that assumption, the next step is to override the following two `AlgorithmXSolver` methods.

<BR>

```text
    def _process_row_selection(self, row):
        action variables (most importantly height, row and col) = unpack the row
        building at (row, col) height = height
        if any affected CityView is no longer valid:
            self.solution_is_valid = False


    def _process_row_deselection(self, row):
        action variables (most importantly row and col) = unpack the row
        building at (row, col) height = 0
```

<BR>

Remember, there is never a need to reset `self.solution_is_valid` to `True`. `AlgorithmXSolver` will backtrack as soon as it sees a `False` value that indicates the current path is a dead end. Backtracking always returns to a valid state and `AlgorithmXSolver` automatically returns `self.solution_is_valid` to `True`.

# Maximizing Speed

To maximize your speed, consider adding a bit of problem-space reduction. It can be challenging to logically determine the heights of many buildings, but you should be able to limit the candidate heights enough to make your solution very fast for all test cases.
