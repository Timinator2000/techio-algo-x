# `DLXCell`

`AlgorithmXSolver`'s DLX implementation is based on [@RoboStac](https://www.codingame.com/profile/771485904355a5f6267beb29429cad302257061)'s solution to [Constrained Latin Squares](https://www.codingame.com/training/medium/constrained-latin-squares) on [Codingame](https://www.codingame.com). Each instance of `DLXCell` is either a column header, a row header or a location of a `1` in the matrix. I add one key attribute that will be critical when customizing Algorithm X.

* `self.title` - This attribute is used by the row and column headers to store the original requirement and action tuples used to set up Algorithm X.

The cells of the matrix never use this attribute. Instead, each cell has two pointers, one to the column header and one to the row header. This gives every cell in the matrix quick access to the tuples used to create the Algorithm X matrix.

The `DLXCell` attributes are shown below:

```python
class DLXCell:
    def __init__(self, title=None):
        self.prev_x = self
        self.next_x = self
        self.prev_y = self
        self.next_y = self

        self.col_header = None
        self.row_header = None

        # Only used for column and row headers.
        self.title = title

        # Size quickly identifies how many rows are in any particular column.
        self.size = 0
```

As long as the tuples you created to build a model for Algorithm X are easy to decipher, they will provide the information needed to customize the sorting of columns and/or rows.
