# Constrained Latin Squares

__Puzzle:__ [Constrained Latin Squares](https://www.codingame.com/training/medium/constrained-latin-squares)

__Author:__ [@darkhorse64](https://www.codingame.com/profile/c9ebe76a83b33730956eda0534d6cad86053292)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Straightforward

# Strategy

Did you create a single SudokuSolver class that was able to solve the 4 Sudoku puzzles? If you did, you might consider starting with that structure and applying it to this puzzle since Sudoku is a special kind of Latin Square. Keep in mind a Latin Square is _less restrictive_ than a Sudoku, so it feels like a thing or two might need to be _removed_ from your Sudoku solver.

You will also need to handle grids of different sizes in the same puzzle. In all 4 Sudoku puzzles, all test case grids within a puzzle were the same size.

# Counting Multiple Solutions

This is the first puzzle in this playground where no single solution has any meaningful importance. Rather, it is only necessary to count the solutions. You always have the option to keep it simple:

```python
count = 0
for solution in solver.solve():
    count += 1

print(count)
```

`AlgorithmXSolver` automatically counts the number of solutions it returns. You still need to loop through all the solutions due to the nature of the generator used to return solutions one-by-one, but you can then access the `solution_count` attribute.

```python
for solution in solver.solve():
    pass

print(solver.solution_count)
```
