# Exact Cover Definition

This playground is titled Algorithm X and we will get to that, but we need to start by understanding what types of problems can be classified as “Exact Cover” problems. Algorithm X is a backtracking algorithm proposed by Donald Knuth for solving exact cover problems. So, how do we identify candidate problems for Algorithm X?

Let’s start with the formal explanation on Wikipedia:

[Wikipedia - Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover)

If you've got the math background to understand all that, I applaud you! (I'm also a bit jealous.) Unfortunately, I am, at best, an amateur mathematician, so please forgive me for skipping over a few of the intricate details.

# A Less Formal Discussion

Now that we have covered the formal definition, I will restate it in my own words. An exact cover problem is a type of problem that can be modeled as a set of constraints and a set of options where solutions are made up of a subset of the options that exactly satisfies all the constraints. Rather than using the terms constraints and options, I’m going to use the terms requirements and actions.

An exact cover problem has a set of requirements that a proper solution must satisfy. Let’s consider the most widely-used example, Sudoku. What are the requirements of Sudoku? There must be a 1 in the first row, there must be a 1 in the first column, there must be a 2 in the first row, there must be a 2 in the first column, there must be a 1 in the top-left 3x3 box, there must be a 2 in the top-left 3x3 box, etc. 

Actions are exactly what they sound like. They are the steps that can be taken to build a solution. What are the actions you can take to solve a Sudoku? You can place a 1 in row 1, col 1 or you can place a 2 in row 1, col 1, or you might place a 7 in row 3, col 4, etc.

The last thing you need to build a complete model of an exact cover problem is a mapping of actions to requirements. For each action, you must identify which requirements are satisfied if that action is added to the solution. In Sudoku, if you put a 1 in col 1, row 1, three distinct requirements are satisfied: there must be a 1 in row 1, there must be a 1 in col 1 and there must be a 1 in the top-left 3x3 box.

Believe it or not, a proper model of 9x9 Sudoku has 243 individual requirements and 729 possible actions. Those numbers can seem a bit overwhelming at this point and because of that, I’d like to introduce you to Mrs. Knuth…
