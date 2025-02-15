# Nonogram Inversor

__Puzzle:__ [Nonogram Inversor](https://www.codingame.com/training/hard/nonogram-inversor)

__Author:__ [@LaurentBouvier](https://www.codingame.com/profile/6061d439c21bc69dacb351d2dae6ccda742965)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Quite Challenging

# Spoiler Alert

Here I go again with the preemptive spoiler alert. This puzzle might be easier to solve with logic than it is to solve with Algorithm X. However, the Algorithm X solution is wonderfully satisfying if you choose to down that fairly challenging path.

# What I (and others) Tried

From the problem statement:

>In this version, we have only two colors, black and white.
>You will be given the length of all black groups.

For each row and each column, we are given the lengths of each _group_ of contiguous black cells in that row or column. Each group of contiguous black cells must be separated by 1 or more white cells. Because there is no difference between a row of cells and column of cells, I will use the word _line_ to generically refer to either a row or column. Each line has some number of cells and zero or more groups of contiguous black cells. 

Consider a 5 x 5 Nonogram. My initial thought was to have a 5 x 5 gameboard and then determine all possible layouts for each line. All lines must be covered by a layout. Because horizontal lines and vertical lines will intersect, I considered using coloring or significant numbers of `me_requirements` to ensure incompatible lines were not placed in the same solution.

Using this approach, I was able to solve __Test Cases 1 and 2__, but I timed out on the remaining test cases. There can be many possible layouts for a line that has multiple groups and there can be many combinations of horizontal and vertical lines that are incompatible. I needed my solution to be significantly faster, so I turned to problem-space reduction.

Once you go down the road of problem-space reduction on this puzzle, it doesn’t take long to find solutions strictly using logic. With a solution in hand, you might wonder why anyone would continue banging his or her head against the wall looking for the Algorithm X solution. Maybe you just enjoy the challenge, or maybe you really like headaches. Either way, __on the next page, I will go through how I built an Algorithm X solution to this puzzle.__

If you like Nonograms, @5DN1L turned me on to 3 more Nonogram puzzles on [CodeWars](www.codewars.com):

# 5x5 Nonogram Solver

__Puzzle:__ [5x5 Nonogram Solver](https://www.codewars.com/kata/5a479247e6be385a41000064)

__Sensei:__ [@Avanta](https://www.codewars.com/users/Avanta)

__Published Difficulty:__ [4 kyu] (https://docs.codewars.com/gamification/ranks)

# 15x15 Nonogram Solver

__Puzzle:__ [15x15 Nonogram Solver](https://www.codewars.com/kata/5a5072a6145c46568800004d)

__Sensei:__ [@Bubbler](https://www.codewars.com/users/Bubbler)

__Published Difficulty:__ [2 kyu] (https://docs.codewars.com/gamification/ranks)


# Multisize Nonogram Solver

__Puzzle:__ [Multisize Nonogram Solver](https://www.codewars.com/kata/5a5519858803853691000069)

__Sensei:__ [@Avanta](https://www.codewars.com/users/Avanta)

__Published Difficulty:__ [1 kyu] (https://docs.codewars.com/gamification/ranks)



