# A Sudoku Challenge

Between Assaf’s code, my `AlgorithmXSolver` and my suggestions, you should be able to complete the [Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver) puzzle. However, there are  3 more puzzles on CodinGame that are all Sudokus of different sizes:

[16x16 Sudoku]( https://www.codingame.com/training/medium/16x16-sudoku)
<BR>[25x25 Sudoku](https://www.codingame.com/training/expert/25x25-sudoku)
<BR>[Mini Sudoku Solver]( https://www.codingame.com/training/hard/mini-sudoku-solver)

My challenge to you is to create a solver that works for all 4 Sudoku puzzles on CodinGame. The only difference between one Sudoku and another is the size of the grid and the values that can be put in each cell. Let me get you started:

```python
from typing import List

class SudokuSolver(AlgorithmXSolver):

    def __init__(self, grid: List[List[str]], values: str):
```

All Sudokus on CodinGame have equal width and height, so that is easy enough to determine by the width or height of the grid. It might not be possible to determine all possible values that may be used to fill the grid, so those values need to be explicitly passed in via the `values` parameter.

Good luck!

