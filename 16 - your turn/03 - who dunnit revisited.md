# Who Dunnit? (Revisited)

__Puzzle:__ Who Dunnit? [Awaiting Approval - See CG Contribution Page](https://www.codingame.com/contribute/community)

__Author:__ [@David Augusto Villa](https://www.codingame.com/profile/455d71552aef838a0c75b7617e2d22d41768324)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Strong Mutual Exclusivity Skills Needed

# Strategy

The [original Who Dunnit discussion](who-dunnit) focused on mutual exclusivity. There is no way to simplify that mutual exclusivity. Whenever you pick an item from an evidence line, you must ensure that none of the other items in that line are ever picked from _any_ line. By the same token, any item that appears in multiple lines must be picked in _all_ line where it occurs if it is picked in _any_ line where it occurs. Can you make your original solution even faster by enforcing sameness with complex actions?

# The Power of Complex Actions

| Test Case | Basic Algorithm X (ms) | Algorithm X With Complex Actions (ms) |
|:---------:|:----------------------:|:--------------------------------:|
| 1 | 0 | 0 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 0 | 0 |
| 6 | 0 | 0 |
| 7 | 0 | 0 |
