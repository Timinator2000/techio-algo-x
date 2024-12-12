# Customizing Column Selection

In Step 2 of Algorithm X, a column is chosen from all remaining yet-to-be-covered columns. As is often the case with backtracking, `AlgorithmXSolver`’s default is to choose the column covered by the fewest number of rows. This technique is referred to as Minimum Remaining Value (MRV). Two situations could prompt you to override this default.

1. You may want to specify how ties are broken when multiple columns are covered by the same number of rows.

1. You may want to specify some non-MRV-based criteria.

To customize the sort criteria, you must override `AlgorithmXSolver`’s `_requirement_sort_criteria(self, col_header: DLXCell)` method. Algorithm X loops through the column headers to determine which column to choose. Because each argument passed to the method is a column header `DLXCell`, it is easy to access:

1. `col_header.size` - the number of rows that cover this column

1. `col_header.title` - the requirement tuple

In the `AlgorithmXSolver` code below, you see the default is to return `col_header.size`.

```python
    # In some cases it may be beneficial to have Algorithm X try covering certain requirements
    # before others as it looks for paths through the matrix. The default is to sort the requirements
    # by how many actions cover each requirement, but in some cases there might be several 
    # requirements covered by the same number of actions. By overriding this method, the
    # Algorithm X Solver can be directed to break ties a certain way or consider another way
    # of prioritizing the requirements.
    def _requirement_sort_criteria(self, col_header: DLXCell):
        return col_header.size
```

In the following code block, I sketch out what an override might look like. I have made no effort to define requirements for this example, so for illustration, I will assume the requirement tuple can be unpacked into 5 distinct elements.

```python
    def _requirement_sort_criteria(self, col_header: DLXCell):
        _, _, c, d, _ = col_header.title
        return (col_header.size, c, d)
```

In this example, the default `col_header.size` is still being used as the primary sort criteria, but ties are being broken first by `c` and then by `d`.

Often, MRV is a very good choice for column selection, so you may find it rare that you consider overriding how columns are sorted. In the next section, I will look at the rows of the matrix.
