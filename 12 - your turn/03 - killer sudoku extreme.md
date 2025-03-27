# Killer Sudoku Extreme Challenge

__Puzzle:__ [Killer Sudoku Extreme Challenge](https://www.codingame.com/training/hard/killer-sudoku-extreme-challenge)

__Author:__ [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ It Depends

# Strategy

In Killer Sudoku Extreme Challenge, your algorithm needs to solve up to 40 __Expert__ Killer Sudoku grids. You will need to do everything you did to solve the original [Killer Sudoku Solver](killer-sudoku-solver) puzzle and more. You must find some amount of problem-space reduction that makes each grid fairly easy for Algorithm X. When solving 40 puzzles, there is not enough time for Algorithm X to do too much backtracking.

# Solving Every Grid Logically

Backtracking involves making a guess and then backing up if that guess leads to a dead end or the path has been fully explored. It is possible to solve every Killer Sudoku grid in the puzzle without making a single guess. In the original puzzle, did you use a class structure similar to this?

<BR><BR>
![Killer Sudoku Classes](KillerSudokuClasses.png)
<BR>

A `SudokuGroup` could be a row, a column or a box. All `SudokuGroup`s behave identically. `Cage`s are another way to group cells and these groups have significantly different behavior which calls for a separate class. If you study how cells behave on a Killer Sudoku grid, you will find even more interesting behavior that can help you find the values of more unknown cells. For an example, click below.

<details>
<summary>Spoiler Alert: Creating Even More Groups for Killer Sudoku</summary>
<br>
  
A Cage is a group of cells that must add up to a certain amount. There are other groups of cells that also must add to a certain amount. For instance, all rows, all columns and all boxes add up to 45 since they each must contain the numbers 1 to 9. That is not all that interesting, nor helpful. However, there are more interesting groups of cells that must add up to certain amounts. Can you find those groups?
</details>
