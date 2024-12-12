# Generalized Exact Cover
 
If you completed all, or at least some portion, of the suggested puzzles, you should be gaining confidence in your ability to use Algorithm X to find solutions to an exact cover problem. Until now, I have been completely focused on requirements and actions, as summarized in the following table.

<BR>

| Playground Term | Equivalent Terms          | Definition                                |
|:--|:----|:------------------------------------------------------------------|
| requirements|<BR>items (preferred by Knuth)<BR>constraints<BR>columns<BR>primary items<BR>primary constraints<BR>primary columns<BR><BR>| __Must__ be satisfied exactly once. |
| actions |<BR>options (preferred by Knuth)<BR>rows<BR><BR>| The individual steps that can be taken to build a solution.|

<BR>

Hold everything! What is up with the word "primary"?

This is the first time I have used the terms “primary constraint” and “primary column”, and there is a good reason for that. _Generalized Exact Cover_ adds the concept of “secondary constraints”, sometimes referred to as “secondary columns” when referenced in terms of a matrix. I want you to know these terms, but in this playground, I’m going to use the term “optional requirement”.

What is the difference between a requirement (primary constraint/column) and an optional requirement (secondary constraint/column)? A requirement must be satisfied exactly once by a proper solution. It may not be left uncovered and it may not be covered more than once. On the other hand, an optional requirement is just what it says. It is optional. It does not need to be covered, but if it is covered, it can only be covered once.

I’m going to add one last equivalent term to the updated table below: At-Most-One-Time Constraint. The requirement may be covered, at most, one time, restricting the options to being covered zero times or exactly one time.

There is a reason the term “optional requirement” works for me. There is only one difference between a requirement and an optional requirement. With an optional requirement, not being covered never causes failure. As Algorithm X is looking for solutions, having no ability to cover a remaining requirement causes a failure condition and Algorithm X backtracks. That is not the case with optional requirements. Algorithm X doesn’t care if these optional requirements get covered at all, but Algorithm X very much cares that these optional requirements never get covered more than once.

<BR>

| Playground Term | Equivalent Terms          | Definition                                |
|:--|:----|:------------------------------------------------------------------|
| requirements|<BR>items<BR>constraints<BR>columns<BR>primary items<BR>primary constraints<BR>primary columns<BR><BR>| __Must__ be satisfied exactly once. |
| optional requirements|<BR>secondary items<BR>secondary constraints<BR>secondary columns<BR>at-most-one-time constraints<BR><BR>| __May__ be satisfied, but if so, one time only. |
| actions |<BR>options<BR>rows<BR><BR>| The individual steps that can be taken to build a solution.|

To demonstrate a generalized exact cover, I will use the well-known, and widely-studied, [Eight Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle).
