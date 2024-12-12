# Tiles on a Gameboard

Every exact cover problem I have looked at could be visualized as placing tiles or game pieces on a grid or board to build a solution. Mrs. Knuth has a blank weekly calendar with the unavailable slots greyed out. A bunch of tiles need to be placed on the calendar. Each tile has a different student name and instrument on it. The task is to place those tiles on the calendar such that all constraints are obeyed and all requirements are satisfied. Every tile represents one possible action that could be taken as part of building a solution.

9x9 Sudoku is fairly easy to visualize since most of us have seen a 9x9 Sudoku grid. What are the tiles? We think of completing a Sudoku grid with a pen or pencil, but can it fit into the tile analogy? Sure it can! Consider that you have 81 tiny tiles and 9 of those tiles have a `1` on them, 9 have a `2` on them, etc. Sudoku grids normally start with some numbers already in the grid. Don’t think of these tiles already being in place. Instead, consider that the Sudoku grid has some numbers already “penciled in”. What are you going to do first? You are going to take the appropriate tiles and immediately place them on top of the “penciled in” numbers. 

# Critical Skill: Generating All Actions

I call the process of “placing a tile/game piece on the grid/board” an action. These actions are the steps that can be taken to build a solution. It is critical that an exhaustive list of all possible actions be created and given to Algorithm X so that Algorithm X can find all valid solutions.

Visualizing the grid/board and the tiles/pieces is often a powerful first step when trying to tackle an exact cover problem and build a complete model for Algorithm X. For many of the puzzles covered later, I will go over how I visualize the problem. This is not a completely objective process, so you might come up with ways that work better for you. Even if we visualize a problem differently, we both still need to come up with an exhaustive list of possible actions to feed into Algorithm X.

How about a little practice?
