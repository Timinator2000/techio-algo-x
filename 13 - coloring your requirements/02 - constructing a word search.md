# The Algorithm X Matrix is Binary

Let's revisit the challenge of constructing a word search. Given a list of words and a grid of a certain size, what are the requirements?

1. Each word must be placed on the grid.

1. Each location may be used zero to many times, and if it is used more than once, it must always be covered, or _colored_, with the same letter.

The first set of requirements is easy. These requirements fit perfectly into the paradigms discussed earlier in this playground. The second set of requirements is troublesome. There is no way to know how many words will intersect at a single location on the grid and some sort of checking must be done to ensure grid locations are only colored a single way. From the perspective of words being placed on the grid, the following can be observed:

* Each grid location may be covered by 0 or more words.

* Any location covered by 2 or more words must be colored with the same letter by each word.

These non-binary stipulations do not fit into an Algorithm X matrix where everything is binary. The solution is to customize `AlgorithmXSolver`to monitor these non-binary requirements outside the Algorithm X matrix.

# Requirements

The binary requirements can first be put into the Algorithm X matrix. For the word search construction exercise:

```python
requirements = [('word placed', word) for word in word_list]
```

For the non-binary requirements that can be colored, add an attribute to your solver subclass to keep track of the color assignments. There are many ways you could do this. For this example, I will use a `dictionary` where the grid locations are the `key`s and each `value` is a `list`. Every time a location is covered by a word, the letter that colors the location is added to the `list`. A cell that has an empty `list` may be covered by any color (letter). A cell that has a non-empty `list` can only be covered again properly if the new color matches what is already in the `list`.

```python
self.location_colors = {(r, c):[] for r in range(height) for c in range(width)}
```

Finally, logic must be added to ensure coloring requirements are obeyed.

# Adding Coloring Logic To Your Solver

Each time a row is selected, logic must be added to check the coloring of each grid cell covered by the word being placed on the grid. This is accomplished by overriding the `AlgorithmXSolver` `_process_row_selection()` method to do the following:

1. Update the coloring of any covered grid location.

1. Redirect Algorithm X if any color violations have occurred.

The pseudocode looks like this:

```python
    def _process_row_selection(self, row):
        word and location = unpack the row
        for each letter in the word:
            if self.location_colors[grid location] not empty and letter is inappropriate:
                self.solution_is_valid = False

            self.location_colors[location].append(letter)
```

The last line above might be a little confusing. Why is the letter being added to the `list` even if the coloring was inappropriate and `self.solution_is_valid` was set to `False`? Backtracking can happen naturally or it can be forced because the current path is not valid. Either way, backtracking will "undo" the most recent row processing which means popping the most recent addition out of the `location_colors` `list`. This cleanup is accomplished by overriding the `AlgorithmXSolver` `_process_row_deselection()` method as follows:

```python
    def _process_row_deselection(self, row):
        word and location = unpack the row
        for each location covered by the word:
            remove the most recent addition to self.location_colors[location]
```

# Tremendous Power From Minimal Effort

It is much more difficult to find research done on Algorithm C or the coloring of requirements than it is to find material on Algorithm X. One way or another, modifications must be made to Algorithm X if you wish to handle requirements that can be colored. The technique laid out above requires a minimal amount of customization to your solver subclass and provides tremendous power. In the next section, I will identify puzzles with which you can employ this newfound power!
