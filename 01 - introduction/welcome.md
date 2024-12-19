# Background

In August, 2022, I attempted to solve [Constrained Latin Squares](constrained-latin-squares), a recently published puzzle by [@darkhorse64]( https://www.codingame.com/profile/c9ebe76a83b33730956eda0534d6cad86053292) on [CodinGame](https://www.codingame.com/home). I noticed [@5DN1L]( https://www.codingame.com/profile/bbb8f47ea4601179303c20acdbf5fb6c1904782) had, a week earlier, posted a link to [Puzzles solvable by Algorithm X / Dancing Links](https://www.codingame.com/forum/t/puzzles-solvable-by-algorithm-x-dancing-links/196871), a post where he had compiled a list of puzzles on CodinGame he had solved with Algorithm X. I love processes that are repeatable and the idea of using a single algorithm to solve a long list of medium/hard puzzles intrigued me.

For the next 18 months, I worked on @5DN1L’s list, reaching out to him over and over again with questions and ideas. I saw tremendous opportunity for not only a reusable software architecture, but also a repeatable engineering process for solving [Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) problems. Eventually, he suggested I build an Algorithm X playground, and here we are!

I can’t thank @5DN1L enough for all of his guidance, support, ideas, encouragement, questions, answers, poking, prodding, reviewing, etc. This playground is his creation every bit as much as it is mine. His influence has made a permanent mark on who I am and how I approach problems. I am forever grateful.
 
# What is Algorithm X?

[Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) is a promise. If you can build a proper model to a particular problem space, Algorithm X promises to find all solutions to that problem space. Papers have been written and projects have been done to demonstrate “how” Algorithm X works. That is not the goal here. Instead, the focus of this exercise is to build expertise in the realm of modeling. The goal is to build models that Algorithm X easily digests and returns solutions. Only a cursory understanding of Algorithm X is required, and the implementation details will barely be covered. Instead, you will be asked to build models of problems and you will have the opportunity to see how well you modeled each problem simply by seeing how easily Algorithm X converts your models into solutions.

# What’s in It for You?

A quick Google search will surely bring you to countless implementations of [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X), usually solving a 9x9 Sudoku grid using the famous [Dancing Links (DLX)]( https://en.wikipedia.org/wiki/Dancing_Links) technique proposed by the brilliant [Donald Knuth]( https://www-cs-faculty.stanford.edu/~knuth/). This playground is NOT just another Sudoku demonstration. By the time you finish working your way through this material, you should feel confident solving any [Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) problem you run across, including…

__Exact Cover (Algorithm X Candidate) Puzzles Created for this Playground:__
<BR>[Mrs. Knuth – Part I](mrs--knuth) (+50 XP)
<BR>[Mrs. Knuth – Part II](mrs--knuth---part-ii) (+50 XP)
<BR>[Mrs. Knuth – Part III](ella-wants-more-lessons) (+50 XP)
<BR>[Equation Search](equation-search) (+50 XP)
<BR>[Ye_ An_th_r W_rd Se_rch](ye_-an_th_r-w_rd-se_rch) (+50 XP)

__Support Puzzle Created for this Playground__
<BR>[Shikaku Skill Builder](shikaku-skill-builder) (+50 XP)

__Great Candidates for Algorithm X:__
<BR>[Sudoku Solver](sudoku-solver) (+50 XP)
<BR>[16x16 Sudoku](16x16-sudoku) (+50 XP)
<BR>[25x25 Sudoku](25x25-sudoku) (+50 XP)
<BR>[Mini Sudoku Solver](mini-sudoku-solver) (+50 XP)
<BR>[Constrained Latin Squares](constrained-latin-squares) (+50 XP)
<BR>[Literary Alfabet Soupe](literary-alfabet-soupe) (+50 XP)
<BR>[Shikaku Solver](shikaku-solver) (+50 XP)
<BR>[Dominoes Solver](dominoes-solver) (+50 XP)
<BR>[Paving with Bricks](paving-with-bricks) (+50 XP)
<BR>[n Queens](n-queens) (+50 XP)
<BR>[Finish the Eight Queens](finish-the-eight-queens) (+50 XP)
<BR>[Optimized Coloring](optimized-coloring) (+50 XP)
<BR>[Einstein’s Riddle Solver](einsteins-riddle-solver) (+50 XP)
<BR>[Winamax](winamax-sponsored-contest) (+250 XP) 🚀🚀🚀
<BR>[Three Little Piggies](three-little-piggies) (+50 XP)
<BR>[Breaking Bifid](breaking-bifid) (+50 XP)
<BR>[Futoshiki Solver](futoshiki-solver) (+50 XP)
<BR>[Suguru Solver](suguru-solver) (+50 XP)
<BR>[Dumbbells Solver](dumbbells-solver) (+50 XP)
<BR>[Hitori Solver](hitori-solver) (+50 XP)
<BR>[There Is No Spoon – Episode 2](there-is-no-spoon---episode-2) (+250 XP) 🚀🚀🚀
<BR>[Takuzu Solver](takuzu-solver) (+50 XP)
<BR>[High-Rise Buildings](high-rise-buildings) (+50 XP)
<BR>[Killer Sudoku Solver](killer-sudoku-solver) (+50 XP)
<BR>[Kakuro Solver](kakuro-solver) (+50 XP)
<BR>[Killer Sudoku Extreme Challenge](killer-sudoku-extreme-challenge) (+50 XP)
<BR>[Tetris Floor](tetris-floor) (+50 XP)
<BR>[Agent X, Mission 2—Mysterious Cryptogram](agent-x-mission-2) (+50 XP)
<BR>[Harmless Rooks](harmless-rooks) (+50 XP)
<BR>[Who Dunnit?](who-dunnit) (+50 XP)


# My Promise to You

I wholeheartedly believe that working through this playground and the accompanying puzzles will be a great experience on multiple levels. How can I say this? All these things happened for me as I studied [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) and applied it to as many puzzles as possible. I promise…

* You will become proficient with a powerful and repeatable problem solving technique known as Algorithm X.
* You will experience the compelling nature of reusable software architectures.
* You will find every puzzle listed above significantly easier than it would have been otherwise. I’m not saying they’ll all be easy, but they will indeed be easier.
* You will have a lot of fun.
* You will earn up to __2200 [CodinGame](https://www.codingame.com) XP!__

# Prerequisites

* Intermediate level knowledge of Python, including object-oriented programming concepts such as classes and class method overriding. However, if you are new to Python, going through this playground will identify some intermediate level concepts that you might consider moving to the top of your to-study list.

* Cursory understanding of backtracking. To complete this playground, it is more important that you understand the general concept of backtracking than it is you be able to code a backtracking algorithm.

# Future Updates

If this is not your first time visiting this playground, be sure to click [here](revision-history) to see if any major updates (e.g. new puzzle) have been made since your last visit.
