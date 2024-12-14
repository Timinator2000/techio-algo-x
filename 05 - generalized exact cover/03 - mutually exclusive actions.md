# Mutual Exclusivity

The [Merriam-Webster Dictionary](https://www.merriam-webster.com/) defines [mutually exclusive](https://www.merriam-webster.com/dictionary/mutually%20exclusive) as:

> : being related such that each excludes or precludes the other
>> _mutually exclusive_ events

Assume I have an exact cover problem and the possible actions are `(A, B, C, D)`. Also assume the solution will consist of two actions, but we know `A` and `C` are mutually exclusive. It's pretty easy to see the possible solutions are `(A, B)`, `(A, D)`, `(B, C)`, `(B, D)` or `(C, D)`. It is not possible for `(A, C)` to be a proper solution since `A` and `C` are mutually exclusive and cannot both be part of the same solution. How can we include this knowledge in the model we build to feed Algorithm X?

# Optional Requirements to the Rescue

Mutual exclusivity comes up frequently in generalized exact cover problems and the solution is fairly simple. For each set of mutually exclusive actions, create a new optional requirement. The example above only needs a single optional requirement:

``` text
('A', 'C')
```

This optional requirement must be added to the lists of satisfied requirements for both `A` and `C`. Since both actions satisfy the requirement and all requirements can only be satisfied, at most, one time, there is no way for `A` and `C` to both show up in the same solution.

# What Exactly are `'A'` and `'C'`?
Let’s say I need an algorithm to identify smoothie recipes that meet certain criteria, one of which is that I never want bananas and kale in the same smoothie. Neither ingredient is required for a proper smoothie, but if either is used, the other must not be added to the mix. To address this, I create the following optional requirement:

```python
('banana', 'kale')
```

Putting bananas in a smoothie satisfies this requirement. Putting kale in a smoothie satisfies this requirement. Because Algorithm X will only allow this requirement to be satisfied, at most, one time, there is no way for both bananas and kale to end up in the same smoothie.

Unfortunately, the mutually exclusive elements are __rarely__ (*see note below) as simple as `'banana'` and `'kale'`. More often, a tuple of data is needed to distinguish the mutually exclusive elements. In Japanese logic puzzles, numbers are often being placed on a grid. Consider a puzzle where cells of the grid must not have the same number as any cell with which it shares a horizontal or a vertical border. To enforce this rule requires a bunch of optional requirements to enforce mutual exclusivity. Let’s assume we have chosen to use tuples of the form `(row, col, number)`. Each new requirement takes this form:

```python
((0, 0, 4), (0, 1, 4))       # ((row, col, number), (row, col, number))
```

What does this requirement tell us? The number `4` can be put in `(row 0, col 0)` or the number `4` can be put in `(row 0, col 1)`, but both cannot happen in the same solution. You should see that two distinct actions cover this one requirement. Putting a `4` in `(row 0, col 0)` covers this requirement. Putting a `4` in `(row 0, col 1)` covers this requirement. Because the requirement may only be covered once, all solutions produced by Algorithm X will fall into one of 3 categories:

1.	The solution does not have a `4` in `(row 0, col 0)`, nor does it have a `4` in `(row 0, col 1)`
1.	The solution has a `4` in `(row 0, col 0)`, and some other number in `(row 0, col 1)`.
1.	The solution has a `4` in `(row 0, col 1)`, and some other number in `(row 0, col 0)`.

This might seem like an excruciating amount of detail, but mastering mutual exclusivity will feel like a superpower as you solve more and more challenges with Algorithm X.

<BR>

>Note: I intentionally avoided the word _never_. It does happen, so never rule out the simple approach!

# BREAKING NEWS

Believe it or not, another school year has flown by, and Mrs. Knuth needs your help again. She has a few features she would like you to add, and oddly enough, her requests will give you a marvelous opportunity to practice using optional requirements to implement mutual exclusivity.

