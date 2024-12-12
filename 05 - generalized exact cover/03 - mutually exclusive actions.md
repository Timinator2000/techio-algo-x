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

Believe it or not, another school year has flown by, and Mrs. Knuth needs your help again. She has a few features she would like you to add, and oddly enough, her requests will give you a marvelous opportunity to practice using optional requirements to implement mutual exclusivity.
