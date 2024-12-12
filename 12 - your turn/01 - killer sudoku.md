# Killer Sudoku

__Puzzle:__ [Killer Sudoku](https://www.codingame.com/training/medium/killer-sudoku-solver)

__Author:__ [@odaxav](https://www.codingame.com/profile/23863af73ab30aa34c1abeb77f21de4e2878884)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Would You Like a Bit of Everything???

# Strategy

Killer Sudoku seems easy enough. It is just Sudoku with one twist. The cells of the Sudoku grid are grouped into cages that must sum to a given amount. No problem, right?

This puzzle is extremely interesting, especially when you look at __Test Case 4: Expert__ where the entire grid is initially empty. We know Algorithm X can easily solve a Sudoku, so how about having Algorithm X generate every possible Sudoku grid until one is generated that does not violate any of the given cage sums? There is a tiny problem with that approach. According to [Brittanica.com]( https://www.britannica.com/story/will-we-ever-run-out-of-sudoku-puzzles):

>There are 6,670,903,752,021,072,936,960 possible solvable Sudoku grids that yield a unique result (that’s 6 sextillion, 670 quintillion, 903 quadrillion, 752 trillion, 21 billion, 72 million, 936 thousand, 960 in case you were wondering). That's way more than the number of stars in the universe.

Unless you have a tremendous amount of computing power and a good amount of time on your hands, some problem-space reduction will be critical.

More than any puzzle covered so far, this puzzle can be attacked in many ways. First, you need a good set of requirements and actions. Since Killer Sudoku extends the traditional Sudoku, you should be able to reuse much of your previous work. After that, you have a lot of options, but ultimately, you will need some combination of the following:

1.	You could add some optional requirements.

1.	There is an opportunity to add optional requirements to handle mutual exclusivity.

1.	You could reuse your Sudoku problem-space reduction.

1.	You could add problem-space reduction based on cages.

1.	You could validate cage sums when solutions are generated.

1.	You could validate cage sums along the way so you can redirect Algorithm X when necessary.

No idea above is significantly more important than the rest. I suggest you experiment with them all until you find a solution fast enough to solve all the test cases.

# Suggested Path Forward

To get started, I recommend you work on setting up Algorithm X with no problem-space reduction at all. A basic Sudoku Algorithm X setup will quickly solve __Test Case 1: Easy__ and __Test Case 2: Medium__. Of course, you will need to make sure all the cage sums are properly honored. From there it gets more challenging.

A hardcore Algorithm X setup will quickly solve __Test Case 3: Hard__, and you might eke out a solution for __Test Case 4: Expert__ before timing out. To solve the 4th test case in a more reasonable amount of time requires some problem-space reduction.

Everything you learn on this puzzle will help you finish the next two puzzles, [Kakuro Solver](https://www.codingame.com/training/hard/kakuro-solver) and [Killer Sudoku Extreme Challenge]( https://www.codingame.com/training/hard/killer-sudoku-extreme-challenge). If you want to get a head start on the next two puzzles, I suggest spending some time here on reducing cages. Your ability to reduce cages will be critical on both of the next two puzzles.
