# 25x25 Sudoku

__Puzzle:__ [25x25 Sudoku](https://www.codingame.com/training/expert/25x25-sudoku)

__Author:__ [@yoch](https://www.codingame.com/profile/14a6f9fb972f723d06789c969370ff2e7411725)

__Published Difficulty:__ Very Hard

__Algorithm X Complexity:__ Should Be Straightforward, but Can Be Challenging (see below)

# Strategy

You can successfully finish 25x25 Sudoku just with what you have learned so far, but you might run into timing issues. These large Sudoku grids translate into large Algorithm X matrices that take time to process. Depending on your choice of data structures, you might find that running your code multiple times produces very different run times and there is a reason for that. To understand why that might happen, it is important to identify how many rows make up the matrix for each test case.

Using the basic strategy laid out for 9x9 Sudoku, each known cell only adds one row to the matrix, while each unknown cell adds 25 rows to the matrix. Looking at each test case results in the following:

<BR>

| | Unknown Cells (U)          | Known Cells (K)              | Rows in the Matrix (25 * U + K)|
|:--|:----:|:-------------------:|:----:|
| Test Case 1: Test 1|276|349|7249|
| Test Case 2: Test 2|331|294|8569|
| Test Case 3: Test 3|324|301|8401|
| Test Case 4: Test 4|321|304|8329|
| Test Case 5: Test 5|326|299|8449|

<BR>

# The Nature of Searching

Seven to eight thousand rows is manageable for Algorithm X, but how those rows are ordered makes a difference. If Algorithm X is trying to cover the cell at `(0, 0)` and there are 10 options to try, the order in which those 10 options are tried impacts run time. While Algorithm X will always try to optimize the order in which it tries rows and columns, there are times when a handful of options appear to be equally viable. In that case, if the correct option is toward the beginning of the list vs the end of the list makes a difference.

If you would like to see this in action, try the following. For unknown cells, shuffle the list of candidates before you build the actions dictionary. You could use a `set` since members of a `set` are unordered or you could use `random.shuffle()`. Either way, you will experience run times that vary quite a bit.

# Where to Go From Here

If patience is not your strong suit, you might be able to pass all test cases and validators just by making sure your matrix is shuffled up a bit each time you run your code. Later in the playground, I will revisit 25x25 Sudoku when I discuss using logic to reduce the problem space. By logically filling in a few more cells of the grid and reducing the candidates for unknown cells, you can shrink the size of the matrix and create a solution that works 100% of the time completely independent of how your matrix gets constructed.
