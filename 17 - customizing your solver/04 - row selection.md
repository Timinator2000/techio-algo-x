# Customizing Row Selection

By default, rows of the matrix are tried simply in the order in which they are encountered. When a column is selected, Algorithm X navigates down the column and builds a list of all rows that cover that column. These rows are tried, one-by-one, in the order Algorithm X found them.

Customizing the order in which Algorithm X tries rows is sometimes a bit more interesting than the columns, since MRV already provides a powerful strategy for column selection.  With no strategy override, row order is based on the algorithm you used to build your actions dictionary. In the `AlgorithmXSolver` code, you can see the default is to return `0` for all rows, providing no guidance to Algorithm X.

```python
    # In some cases it may be beneficial to have Algorithm X try certain paths through the matrix.
    # This can be the case when there is reason to believe certain actions have a better chance than
    # other actions at producing complete paths through the matrix. The method included here does
    # nothing, but can be overridden to influence the order in which Algorithm X tries rows (actions) 
    # that cover some particular column.
    def _action_sort_criteria(self, row_header: DLXCell):
        return 0
```

To demonstrate an override situation, let’s again look at Sudoku where every action probably took the following form:

```python
action = ('place value', row, col, val)
```

The argument passed into `_action_sort_criteria(self, row_header: DLXCell)` is a row header `DLXCell` which allows easy access to the row `title` where the action tuple is stored. The following override will make sure integers for a Sudoku cell are always tried in ascending order:

```python
    def _action_sort_criteria(self, row_header: DLXCell):
        _, _, _, val = row_header.title
        return val
```

The following override will make sure integers for a Sudoku cell are always tried in descending order:

```python
    def _action_sort_criteria(self, row_header: DLXCell):
        _, _, _, val = row_header.title
        return -val
```

If you really want to get crazy with a dynamic strategy, the following override will order rows according to the following two criteria:

* First, how close the number is the average of all remaining cell candidates.
* Second, being lower than the average is prioritized over being higher than the average. 

```python
    def _action_sort_criteria(self, row_header: DLXCell):
        _, row, col, val = row_header.title
        average = sum(all remaining candidates for grid[(row, col)] / number of remaining candidates
        return (absolute_value(average - val), val - average)
```

I understand the example above is strange, but you could try it. Hopefully, you better understand how column and row ordering can affect your Algorithm X solution. With this in mind, let's take a look at a couple of puzzles where these techniques could be used.
