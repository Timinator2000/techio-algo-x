# Coloring Your Requirements

In his book, Donald Knuth identifies a category of problems where it is not only important to know which requirements have been covered, but also to know “how” those requirements have been covered. He proposes that sometimes requirements can be covered with a “color”, and if the color remains the same, certain requirements can be covered any number of times.

Going back to the analogy of tiles on a gameboard, the concept of coloring allows tiles to overlap. However, it is critical that the tiles be identical at the point of overlap. In his book, Knuth uses an example of building a word search puzzle. Given a list of words and a grid, put all the words on the grid with a certain amount of overlap.

# Example: Constructing a Word Search

Constructing a word search is a great fit for Algorithm X, until we get to the overlapping locations. What are the requirements of the exercise? Each word must be placed somewhere on the grid. Are there any optional requirements? Each square of the grid may be covered by a letter, or it may be left empty, later to be filled with a letter that is not part of the solution. What about actions? Each action is simply putting a word on the grid at a specified location and in a specified direction.

What about the requirements satisfied by each action? A word has been placed on the grid and a certain number of cells have been covered. But what about multiple words that overlap? Two words that overlap are each placed on the grid by a separate action and each of those actions covers the cell where the overlap occurs.

You might be tempted to see this as an instance of multiplicity as discussed earlier, but there is a slight difference. In this example, each cell could be left uncovered or it could be covered multiple times, as long as it is covered, or _colored_, by the same letter each time. For all multiplicity examples discussed previously, certain requirements needed to be covered an exact number of times.

# Algorithm C

Knuth proposes Algorithm C to solve exact cover problems that include the coloring of requirements. I am not going to cover Algorithm C here, but on the next page, I will show you how to easily customize `AlgorithmXSolver` to handle the coloring of requirements.
