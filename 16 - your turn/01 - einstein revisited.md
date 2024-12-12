# Einstein's Riddle Solver (Revisited)

__Puzzle:__ [Einstein's Riddle Solver](https://www.codingame.com/training/hard/einsteins-riddle-solver)

__Author:__ [@OroshiX](https://www.codingame.com/profile/045d3b89723c9acafb728c9fd1d8cb297970931)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ No More Perspective Shift Needed

# Memory Refresh

Einstein’s Riddle Solver is unique because some characteristics _must_ be assigned to the same column and other characteristics _must not_ be assigned to the same column. In the [original discussion](einsteins-riddle-solver), I suggested converting all characteristics that must be the same into a group of characteristics that must be different. In that way, all characteristic relationships could be handled with option requirements used to implement [mutual exclusivity]( mutual-exclusivity). Let’s now consider solutions for Einstein’s Riddle Solver that use [coloring]( all-or-none-with-colors) or [complex actions](complex-actions) to enforce sameness.

Einstein’s Riddle Solver is extremely similar to the [scavenger hunt](all-or-none-sets-of-events) presented in the previous section, with one key difference. The scavenger hunt did not have any mutual exclusivity. The scavenger hunt can be thought of as a grid, just like the gameboard and tiles analogy proposed in the original Einstein discussion. In the scavenger hunt, each child already has a grade level, but must be assigned a team color. In the Einstein puzzle, each characteristic already has a row and must be assigned a column.

# All-Or-None Sets of Characteristics

Because every characteristic must be accounted for, start with a list of sets where each set contains exactly one characteristic. Then, add another set to the list for each group of 2 characteristics that must be the same. The last step is to use the skills practiced on the [previous page](test-your-skills) to combine the all-or-none sets that overlap. In the end, you will have some sets with multiple characteristics that must be the same and several sets that still only contain a single characteristic, meaning that characteristic is not _required_ to be in the same column as any other characteristic.

# Enforcing Sameness with Colors

To build a solution using colors, you will follow the same steps used to build a solution for the scavenger hunt to add the coloring mechanisms. Other than that, handling the mutually exclusive characteristics does not change from the original discussion.

# Enforcing Sameness with Complex Actions

Again, building Einstein’s complex actions is almost the exact same process as described in the scavenger hunt. With complex actions, tremendous care must be taken when identifying the requirements covered by each complex action. Do not overlook the `me requirements` for each simple action that is part of the complex action.

# Comparison

The following table compares my solvers using each of the three techniques discussed here. It is important to remember my solution with coloring is an Algorithm X solution, _adapted_ for coloring. It is not an implementation of Donald Knuth’s Algorithm C.

| Sameness Enforced With: | Actions | me_requirements | Execution Time (ms) |
|:------|:------:|:------:|:------:|
| __<span style="color:red">Test Case 2: 4 * 5 Medium</span>__ |
|    Mutual Exclusivity | 80 | 152 | 3 |
|    Colors | 80 | 44 | 6 |
|    Complex Actions | 45 | 44 | 1 |
| __<span style="color:red">Test Case 3: 7 * 6 Hard</span>__ |
|    Mutual Exclusivity | 222 | 564 | 35 |
|    Colors | 222 | 99 | 3600 |
|    Complex Actions | 114 | 99 | 6 |
| __<span style="color:red">Test Case 4: 5 * 5 Medium</span>__ |
|    Mutual Exclusivity | 105 | 183 | 4 |
|    Colors | 105 | 43 | 8 |
|    Complex Actions | 55 | 43 | 1 |

# Observations

The numbers seen above tell an expected story. Enforcing sameness with mutual exclusivity requires many extra `me_requirements`, but Algorithm X is still able to chew through the matrix with relative speed. Enforcing sameness using colors requires a significant amount of color checking outside the matrix. As you can see, that adds a fair amount of time for the most difficult test case.

Enforcing sameness with complex actions combines the best of both worlds. The `me_requirements` are kept to the minimum necessary to enforce mutually exclusive characteristics while the actions are minimized by combining actions that must occur together. Properly constructing complex actions might take a bit of practice, but those efforts will be rewarded with very fast execution times.
