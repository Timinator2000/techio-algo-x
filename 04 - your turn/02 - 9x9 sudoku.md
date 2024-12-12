# Sudoku Solver

__Puzzle:__ [Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver)

__Author:__ [@AllTheKingsMen](https://www.codingame.com/profile/571927d715f15c3dec7693f461e2a63c6671233)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ If Only They Were All This Straightforward

# Strategy

Sudoku is a great place to start because a basic Sudoku always comes with a partial solution already in place. Some portion of the grid has already been prefilled. Some number of actions have already been taken and are required to be a part of any complete solution. In the following sections I will compare portions of [Assaf’s Sudoku code]( https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt) to my current Sudoku code. Ultimately, I will end with a discussion of several techniques for handling partial solutions that are already in place.

# Identify Requirements – à la Ali Assaf

Note: In Assaf's code, `R` and `C` are the numbers of rows and columns in a Sudoku box or sub grid. A 9x9 Sudoku grid has 9 boxes and each box is 3x3. For a traditional 9x9 Sudoku, `N` = 9 in Assaf's code, but `R` and `C` are both 3.

```python
    R, C = size
    N = R * C
    X = ([("rc", rc) for rc in product(range(N), range(N))] +
         [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
         [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
         [("bn", bn) for bn in product(range(N), range(1, N + 1))])
```

# Identify Requirements – à la Timinator

My tuples are flatter, and my strings are a bit longer. These tuples are stored in header nodes in my DLX implementation where they have no impact on performance. Assaf’s code assumes integer values in the Sudoku cells. Because I know 16x16 Sudoku and 25x25 Sudoku both use letters of the alphabet, I have chosen to always use characters for this basic solver.

```python
        requirements = [('cell covered', row, col) for row in range(size) for col in range(size)] + \
                       [('value in row', row, val) for row in range(size) for val in all_possible_values] + \
                       [('value in col', col, val) for col in range(size) for val in all_possible_values] + \
                       [('value in box', box, val) for box in range(size) for val in all_possible_values]
```

# Identify Actions – à la Ali Assaf

Assaf builds a dictionary of actions (`Y`). Notice that __all__ possible actions are included in the dictionary. Assaf does not limit the actions for cells that already contain a value.

```python 
    Y = dict()
    for r, c, n in product(range(N), range(N), range(1, N + 1)):
        b = (r // R) * R + (c // C) # Box number
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
```

# Identify Actions – à la Timinator

Here is a key difference between Assaf’s code and mine. As I build the dictionary of actions, I limit the actions to only what is possible. A cell that is prefilled only has one candidate, while a blank cell has many candidates. I have also chosen to include an identifier string in my action tuples due to benefits realized while debugging.


```python
        actions = dict()
        for row in range(size):
            for col in range(size):
                box = (row // box_size) * box_size + (col // box_size) 
                for val in self.grid[(row, col)].candidates:
                    action = ('place value', row, col, val)
                    actions[action] = [('cell covered', row, col),
                                       ('value in row', row, val),
                                       ('value in col', col, val),
                                       ('value in box', box, val)]
```

# Preselect Known Actions – à la Ali Assaf

After the matrix is built and ready to go, Assaf uses the following code to add actions to the solution before asking Algorithm X to use backtracking to find the remaining actions that solve the entire Sudoku. For each cell in the Sudoku grid that is prefilled with a number (`n`), Assaf makes a call to `select` to add the appropriate action to the solution and make the necessary adjustments to the matrix.

```python
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
```

# Preselect Known Actions – à la Timinator

Because I have limited the actions to only what is possible, no preselection is done. Algorithm X has no choice but to select the appropriate actions to include the prefilled numbers as part of the solution.

_I believe Assaf's code has been vital to me and other Python programmers studying Algorithm X. My `AlgorithmXSolver` has been heavily influenced by Assaf, but I have intentionally left out the ability to preselect actions as Assaf has done above. Although Assaf's technique is elegant, I have chosen to limit actions as a standard process across all solutions. I want to point this out for anyone that might be familiar with Assaf's solver and wonder why <u>it is not possible</u> to preselect actions with the `AlgorithmXSolver` provided in this playground._

# Preselection Can Be Problematic

The DLX matrix is not meant to handle the selection of improper actions. Every time an action is selected to be part of a solution, DLX removes any impossible actions from the realm of possibility. When Algorithm X is in charge, it is impossible to select an action that cannot possibly be part of the final solution.

Consider the following example. Do solutions exist for the Sudoku board below?

```
0 0 6 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

You and I can easily see there are two 6s in the first row, making it impossible to find a proper solution. This is a toy example, but play along with me.  Assume you want to use Algorithm X to determine if the Sudoku can be solved or not. You first create the requirements and the actions. Then you try to preselect the action that puts a 6 in row 1, col 3 and the action that puts a 6 in row 1, col 7. As soon as you preselect the first action, the DLX matrix is adjusted and there is no longer an option to put the second 6 in row 1, col 7. You tried to preselect an action that is no longer possible. You will either get an error, or your solver might produce many solutions since it is starting with a blank Sudoku with a single 6 preselected in row 1, col 3. 

The solution is to __leave Algorithm X in charge__. Next, I will discuss options that handle preselected cells, but since Algorithm X is in charge, error situations are more easily avoided.
