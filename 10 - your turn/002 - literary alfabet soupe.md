# Literary Alfabet Soupe (Revisited)

__Puzzle:__ [Literary Alfabet Soupe](https://www.codingame.com/training/medium/literary-alfabet-soupe)

__Author:__ [David Augusto Villa](https://www.codingame.com/profile/455d71552aef838a0c75b7617e2d22d41768324)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Is Algorithm X Really Needed?

# Strategy

In the [original discussion](literary-alfabet-soupe) for this puzzle, I wrote:

> Let’s assume you are at a point where you have some number of “candidate” languages for each excerpt. Some excerpts might have just one candidate language while others might have 2, 3, 4 or more candidate languages.

Can you do any problem-space reduction before running Algorithm X? Of course you can! Assume you have identified the following candidate languages for the first 3 excerpts:

| Excerpt | Candidate Languages |
|:----:|:------------|
| 1 | Finnish, French, German, Irish |
| 2 | German |
| 3 | French, German, Spanish |

Do you see the opportunity for problem-space reduction? The only option for excerpt 2 is German. Since each language can only be used one time, German can be removed from the candidate lists for excerpts 1 and 3.

Once you have a list of candidate languages for each excerpt, your problem-space reduction can be similar to what was covered a few pages back using Sudoku. This puzzle is not meant to be a complex exact cover problem, so keep your reduction algorithm simple. If you create a loop to reduce the candidate lists wherever possible, you might find that full solutions appear for each test case before you even begin setting up Algorithm X. 
