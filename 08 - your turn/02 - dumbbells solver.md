# Dumbbells Solver

__Puzzle:__ [Dumbbells Solver](https://www.codingame.com/training/hard/dumbbells-solver)

__Author:__ [@VilBoub](https://www.codingame.com/profile/bd6706892e49290fb119aa5ddae4238a318297)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ A Perfect Introduction to Multiplicity

# Strategy

Dumbbells Solver is the perfect puzzle for practicing what you just learned about multiplicity and it works wonderfully with the tiles on a gameboard analogy. You are given a gameboard with some markings indicating some of the weight locations. The tiles you will place on the gameboard are the dumbbells.

Where is the multiplicity in this puzzle? Consider the dumbbells. In the Example Test Case, three dumbbells need to be placed on the floor. In real life, these dumbbells might be different colors, or they might be different weights, but in this puzzle there is nothing to tell one dumbbell from another. Is there any difference between placing 3 dumbbells on the floor and scheduling 3 lessons for Ella with Mrs. Knuth? No, there really is not.

The requirements are straightforward. Some locations on the floor are marked and one end of a dumbbell _must_ cover each marked location. Every other location on the floor _may_ or _may not_ be covered. Any location that gets covered can only be covered one time since the puzzle states:

>The dumbbells can touch but not cross each other.

How about the actions you can take to build a solution? This puzzle looks very similar to [Dominoes Solver](https://www.codingame.com/training/hard/dominoes-solver) in that regard. Combine what you learned on Dominoes Solver with the skills you solidified on [Shikaku Solver](https://www.codingame.com/training/medium/shikaku-solver) and you should have a clear path forward. Of course, you will need to make sure you properly add precision to the requirements and actions, as was discussed in the approach to Mrs. Knuth – Part III.

# Memory to Avoid Duplicates

Because there is a unique solution to every test case, you may use a `break` statement as soon as Algorithm X returns the first solution. Dumbbells Solver is a great fit for Algorithm X and your solver should find the first solution very fast on every test case.

I was surprised I did not see an increase in speed when I added memory to my `DumbbellsSolver`. When a call is made to `self._remember(self, item_to_remember: tuple)`, `AlgorithmXSolver` looks for the item in its memory and if that item is already in memory, the attribute `self.solution_is_valid` is set to `False`. I added the following lines of code to my `DumbbellsSolver` to take a look at how often memory was causing backtracking.

```
    def _process_row_selection(self, row):
        unpacked action elements = row
        self._remember((some combination of unpacked action elements))

        if not self.solution_is_valid:
            print('Memory is forcing backtracking...', file=sys.stderr, flush=True)
```

What did I find? Although memory did force backtracking, it was extremely rare. Since it did not happen often, there was not much impact on overall speed.

# How Important is the `Break` Statement?

If the `break` statement is removed, Algorithm X will search for all solutions. Let's give it a try! Using the code above, you see memory forces a fair amount of backtracking. After searching for all solutions, add the following line to see how many solutions Algorithm X found.

```
print(f'{solver.solution_count=}', file=sys.stderr, flush=True)
```

What do you see? As long as memory is properly used, Algorithm X only finds a single solution for each test case. What if you delete the memory code? Algorithm X finds 6 solutions for __Test Case 1__ and 24 solutions for __Test Case 2__. For the last 3 test cases, the [Codingame](https://www.codingame.com) time limit is hit before Algorithm X finishes searching for solutions.

# Takeaways

Hopefully you are flying through some of these puzzles for which Algorithm X is such a great fit. If you run into issues, you might check these small details:

1. Are you using a `break` statement as soon as Algorithm X finds a solution?

1. Are you correctly using `AlgorithmXSolver`'s memory?
