# Crossword

__Puzzle:__ [Crossword](https://www.codingame.com/training/medium/crossword)

__Author:__ [@Humanosaure](https://www.codingame.com/profile/5bbc0f4b299d3bb28410b96df8a45b607624692)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Uniquess Provides a Challenge

# Strategy

Given two horizontal words and two vertical words, this puzzle challenges us to determine whether a valid crossword puzzle can be constructed such that all four words intersect pairwise. In the diagram below, each word's letters have been omitted, but it is easy to imagine how a properly constructed grid might appear.

<BR><BR>
![Crossword](Crossword1.png)
<BR>

To make things slightly more challenging, the author adds an extra twist: we are required to print the solved crossword grid when there is exactly one valid solution. Whether or not you use Algorithm X, constructing the grid is no easy feat — even when you already know where the four words must go!

I found it particularly interesting to frame this puzzle as an exact cover problem. This unique perspective opens the door to some elegant strategies, which I’ll explore in more detail below. But before diving into the details, I strongly encourage you to try solving the puzzle on your own. There are several compelling ways to approach it using the exact cover technique, and I believe you'll find the experience both rewarding and enjoyable.

<details><summary>Spoiler Alert: There is no way to go back.</summary>
  
<BR><BR>
![Crossword - Box](Crossword2.png)
<BR>


# Enforcing Sameness with Coloring

<BR><BR>
![Crossword (Coloring)](Crossword3.png)
<BR>

# Enforcing Sameness with Mutual Exclusivity

<BR><BR>
![Crossword (Mutual Exclusivity](Crossword4.png)
<BR>

</details>
