# Futoshiki Solver

__Puzzle:__ [Futoshiki Solver](https://www.codingame.com/training/medium/futoshiki-solver)

__Author:__ [@Sundiver](https://www.codingame.com/profile/a4d5c1786311a05772d1b2f5dadac78e6102203)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Great Confidence Builder

# A Special Latin Square

Parsing and organizing input for this puzzle is plenty challenging on its own. Fortunately, once the input is understood, the puzzle starts to look very familiar. Both the puzzle goal and Wikipedia confirm a Futoshiki has a lot in common with Sudoku and other Latin Square puzzles.

From the puzzle goal:

>Futoshiki is a Japanese numeric logic puzzle similar to the more popular Sudoku.

From [Wikipedia](https://en.wikipedia.org/wiki/Futoshiki):

>A solved Futoshiki puzzle is a Latin Square.

I will skip going over the requirements and actions since they have been covered in detail already, but the inequalities add an important twist.

# Inequalities

All inequalities in a Futoshiki can be expressed as `a < b` where `a` and `b` are the values in two cells that share a horizontal or vertical border. Given a 6x6 Futoshiki with no hints, we know that every cell is a number between 1 and 6.

```
Possible values for a = 1, 2, 3, 4, 5, 6
Possible values for b = 1, 2, 3, 4, 5, 6
```

?[What is wrong with the above statements? Select all that apply]
-[] Nothing is wrong. In the absence of hints, either cell could take any of those values.
-[x] b cannot be 1 since there are no values for a that allow a < b to be true. 
-[] a must be 1 and b must be 2 because a < b.
-[x] a cannot be 6 since there are no values for b that allow a < b to be true. 

Very interesting! What if `b` already had a value in the box? That would make it easy to reduce the possible values for `a`.

Ultimately, an inequality identifies what must be true, and from that, it is easy to determine what cannot happen. If `a` < `b`, then making `a = 3` and `b = 2` is not allowed. 

?[How do we tell Algorithm X certain things are not allowed?]
-[] Send an email.
-[] Post a message in the CodinGame Forum. 
-[x] Create requirements to handle mutual exclusivity.
-[] Call a special AlgorithmXSolver method.
-[] Ask @5DN1L to reach out to CodinGame directly.

It looks like you will need some requirements to handle the mutual exclusivity created by each inequality.

# Your Goal

All test cases except __Test Case 5: 7x7__ can be solved with nothing more than requirements, actions and optional requirements. To solve __Test Case 5: 7x7__, you might need a very small amount of problem-space reduction. I have already discussed one option using the inequalities to limit the realm of possibility for the cells on either side. Later in the playground, I will discuss other techniques for problem-space reduction.
