# Tetris Floor

__Puzzle:__ [Tetris Floor](https://www.codingame.com/training/hard/tetris-floor)

__Author:__ [@cedricdd](https://www.codingame.com/profile/20f5f88d86185be4439fc7297df0aa073968164)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Algorithm X Can Be a Very Reasonable Part of a Very Complex Puzzle

# Strategy

In Tetris Floor, the goal is to cover the floor using only tiles of 7 distinct shapes. Each tile can be rotated before it is put on the floor. The first step toward setting up Algorithm X will be identifying an exhaustive list of possible actions. For each of the 7 block types, you need to identify every location on the floor where a block of that type could be placed and you need to take rotation into consideration. If you are unsure how to make this happen, I suggest reviewing what you implemented on [Three Little Piggies](https://www.codingame.com/training/hard/three-little-piggies).

Once you have Algorithm X finding solutions, you need to determine the cheapest solution. You could begin by overriding `_process_solution()` to calculate the cost of each solution just like you did in [Mrs. Knuth – Part III – FINAL LINK NEEDED](https://www.codingame.com/contribute/view/959460130d2f9792d933f75838edb639a6dae). One look at the test cases and you will realize you probably need to do some course correction with Algorithm X. Fortunately, you built the skills necessary to keep track of partial solutions and provide corrective feedback when you completed [High-Rise Buildings]( https://www.codingame.com/training/expert/high-rise-buildings).

If you use Algorithm X, it will be just part of a fairly complex solution. You will need to implement several clever problem-space reduction techniques. The test cases are well designed, and they will lead you down a path that might seem to always end in a timeout. Use the early test cases to make sure you have a strong Algorithm X setup. The later test cases will then come down to finding ways to make the problem easier before asking Algorithm X to find solutions.

I am not 100% convinced Algorithm X is the best way to approach this puzzle, but it is doable. I will avoid any spoilers and leave it at that.
