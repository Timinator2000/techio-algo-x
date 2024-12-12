# Assorted Rectangular Pieces Puzzle

__Puzzle:__ [Assorted Rectangular Pieces Puzzle](https://www.codewars.com/kata/5a8f42da5084d7dca2000255)

__Author:__ [@docgunthrop](https://www.codewars.com/users/docgunthrop)

__Published Difficulty:__ [2 kyu](https://docs.codewars.com/gamification/ranks)

__Algorithm X Complexity:__ No Worse than Trying to Survive a Zombie Apocalypse

# Strategy

This puzzle on [Codewars](https://www.codewars.com) is a complex exact cover problem. You are given a number of rectangular puzzle pieces and you need to use those pieces to cover all the open locations on the puzzle board. Pieces can be rotated if necessary. The Sample Test Suite has 5 test cases and the last 3 test cases all have shapes that repeat. Because there might be multiple shapes with the same size (e.g. multiple `2 x 3` shapes or multiple `3 x 5` shapes), you need to put together a strong Algorithm X model to handle multiplicity.

Once you get a working Algorithm X setup, the real work begins. When you attempt to pass the full test suite, you get 12 seconds to complete 75 tests. I was stuck for quite a while timing out on many different variations of my solver. I tried every technique discussed in this playground.

Right after you call the inherited `AlgorithmXSolver` constructor, add this line of code to print the number of columns and rows in the matrix:

```
        print(len(requirements), len(actions), file=sys.stderr, flush=True)
```

With my Algorithm X setup, a number of the 75 test cases have between 3000 and 5000 rows. One test case actually has many more rows than that. What does this tell you? It should tell you the matrix is big, and influencing how Algorithm X chooses columns and/or chooses rows could make a significant difference.

# A Confession

I placed this puzzle in this section for a reason. Setting up Algorithm X for this puzzle requires strong attention to detail, but getting Algorithm X to find solutions for the easy test cases is not the toughest part. Optimization is where you will find the most significant challenge.

My original solution used a clever combination of dynamic sorting for both columns and rows. I kept track of remaining open cells on the gameboard, among several other things, and made various sorting decisions based on that information. Now that my understanding of Algorithm X is much better, my current solution does not use any dynamic sorting. The ordering of rows and columns in my matrix is still very important, but I handle prioritization when the matrix is created.

# Making Your Solution Fast

If you want to maximize speed, you might need to add some problem-space reduction. Are there any ways you can reduce the size of the problem before building the matrix for Algorithm X? Keep in mind that this process takes time. If you attempt to add problem-space reduction, is there a way you can quantify how much benefit you get and at what cost?
