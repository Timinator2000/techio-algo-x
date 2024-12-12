# Literary Alfabet Soupe

__Puzzle:__ [Literary Alfabet Soupe](https://www.codingame.com/training/medium/literary-alfabet-soupe)

__Author:__ [David Augusto Villa](https://www.codingame.com/profile/455d71552aef838a0c75b7617e2d22d41768324)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Straightforward

# Strategy

This puzzle provides an opportunity to practice Algorithm X with a very basic and straightforward setup. There is just one little problem. Understanding, analyzing and organizing the problem space is challenging enough on its own to make this puzzle deserving of its “medium” rating. What do I mean by that?

You are given 13 excerpts and 13 languages. You need to identify the language used in each excerpt. Before you can even consider Algorithm X, you need to use the information (inclusions and exclusions) provided about each language to determine which languages _could match_ each excerpt. This is a very nice algorithmic challenge with many ways in which it can be approached, and that is all I have to say about that.

Let’s assume you are at a point where you have some number of “candidate” languages for each excerpt. Some excerpts might have just one candidate language while others might have 2, 3, 4 or more candidate languages. Because every language must be assigned to exactly one excerpt, Algorithm X can easily take it from here.

What are the requirements? Every excerpt must be assigned a language. What are the actions? Each candidate language translates to one action that matches that language to that excerpt. That is all there is to it, textbook Algorithm X.

Identifying the candidate languages for the excerpts is quite a bit more challenging than finding an exact cover that uniquely matches the 13 languages to the 13 excerpts. Later in this playground, I will revisit this puzzle with a bit more information on options once you have identified candidate languages for each excerpt. If you want to jump ahead, click [here](literary-alfabet-soupe-revisited).
