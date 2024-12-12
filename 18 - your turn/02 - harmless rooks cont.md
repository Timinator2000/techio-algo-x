# Harmless Rooks (cont.)

On the previous page, the following task was proposed for Algorithm X:

>Try to cover every `AttackLine` by placing rooks on open squares. If no solution exists that covers all `AttackLine`s, return the length of the partial solution that gets the closest.

Algorithm X is designed to be efficient, and it is extremely efficient at identifying when paths are dead ends. As soon as Algorithm X determines a path will eventually be a dead end, all forward exploration stops and the algorithm backtracks. Without any customization, Algorithm X can quickly determine if __all__ `AttackLine`s can be covered, but it is not designed to tell us how close it can get to a proper solution when no full solution is possible.

# Customizing Algorithm X To Be Inefficient

How does Algorithm X know when a path is a dead end? The matrix has at least one requirement that no longer has any rows that cover it. Since it is impossible for one of the (mandatory) requirements to be satisfied, Algorithm X backtracks. `AlgorithmXSolver` implements this process by sorting requirements by the number of rows remaining that cover each requirement, often referred to as Minimum Remaining Value (MRV). Columns that are not covered by any rows are sifted to the front of the line and Algorithm X immediately knows it is time to backtrack. This default behavior is found in the `AlgorithmXSolver` method `_requirement_sort_criteria()` as shown below. 


```python
    def _requirement_sort_criteria(self, col_header: DLXCell):
        return col_header.size
```

The `size` attribute of a `DLXCell` is only meaningful when the `DLXCell` instance is a column header and it keeps track of the number of rows that still cover the requirement. `AlgorithmXSolver` will sort all remaining requirements by the number of rows covering each requirement and then pick the requirement with the _minimum remaining value (number of rows)_.

In this puzzle, occupied cells most likely create boards where Algorithm X cannot cover every `AttackLine` and I don’t want Algorithm X to backtrack just because it finds one `AttackLine` that cannot be covered. Instead, I want Algorithm X to keep placing rooks until none of the remaining `AttackLine`s can be covered. This is easily accomplished simply be reversing the sort order to push requirements that cannot be covered to the end of the line. To implement this in your solver, override the `_requirement_sort_criteria()` method as follows:

```python
    def _requirement_sort_criteria(self, col_header: DLXCell):
        return -col_header.size
```

A single `-` sign is all that is needed! As long as a rook can be placed, Algorithm X will continue exploring, looking for a solution that covers all `AttackLine`s. Backtracking will __only__ happen when the matrix shows that none of the remaining `AttackLine`s can be covered by any rook placement. 

# Counting Rooks

Just a few lines of code can customize your solver to keep track of the maximum number of rooks placed. First add two attributes in your solver’s constructor:

```python
self.rooks_placed = 0
self.most_rooks_placed = 0
```

Then, because each action (row) is the placement of a rook at a particular location, the following overrides will keep track of the current number of rooks placed and the max number of rooks placed:

```python
    def _process_row_selection(self, row):
        self.rooks_placed += 1
        self.max_rooks_placed = max(self.rooks_placed, self.max_rooks_placed)


    def _process_row_deselection(self, row):
        self.rooks_placed -= 1
```

We now have a fully functional solver that can finish test cases 1 and 2, but you will probably run into timeout issues after that. To solve the remaining test cases, you will need to find ways to reduce the problem space by placing rooks logically. 
