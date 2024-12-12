# Winamax Sponsored Contest

__Puzzle:__ [Winamax Sponsored Contest](https://www.codingame.com/training/hard/winamax-sponsored-contest)

__Difficulty:__ Hard

__Algorithm X Complexity:__ Requirements are Straightforward, Actions are Complex (You May Need Aspirin)

# Big Payoff

250 XP! Need I say more? Puzzles on CodinGame that offer unusually high XP are always popular. This puzzle is so creative, I am not sure it even needs the high XP.

# Visualizing the Problem

Let’s start with a quote from the problem statement:

> In this puzzle, you are given a grid representing a golf course. On each course is a certain amount of balls and an equal amount of holes. The objective is to find the route for each ball to a different hole without their paths ever crossing.

Using the analogy of laying tiles on a grid, it seems pretty obvious the grid is the map of the golf course given in the input. Per the statement above, the grid will indicate where the holes are and where the balls are. Later in the problem statement, we are told the grid also identifies water hazards and open fairway spaces.

What are the tiles we can lay down on the grid? It might be tempting to consider each individual ball movement a tile, but that is like considering each cell in a Shikaku rectangle a separate tile. In Shikaku, Algorithm X needed a full list of possible rectangles and each one of those rectangles, possibly covering many grid cells, is a tile that can be placed on the grid. Let’s again look to the problem statement for a hint:

>The objective is to find the <ins>route</ins> for each ball to a different hole without their paths ever crossing. [emphasis added]

Each possible route from a ball to a hole is a tile that could be placed on the grid. Given 5 balls and 5 holes and a bunch of possible routes from the balls to the holes, Algorithm X will find a set of routes where each ball goes “to a different hole without their paths ever crossing”.

# Enumerating the Actions

I have recommended you use human readable tuples to identify actions for an exact cover problem and the information in those tuples needs to uniquely identify each action from all other actions. What information is needed to uniquely identify a route? Since a route can zig and zag in all kinds of directions, the only way to uniquely identify a route is with a full set of grid coordinates that make up the route. What about short routes vs long routes? This seems like it could be challenging, but there is an easy solution.

Let’s say you have 10 possible routes from the first ball to the various holes. Give every route a unique integer ID and include that unique ID in your action specification, possibly something like `('select route', bx, by, route id)` where bx and by are the ball location. The combination of ball location and route id clearly identifies one route from all other routes. 

Going back to the tiles on a board analogy, each tile now has a ball location, `(bx, by)`, and a route number on it, but what does that tile look like? Since we had to generate all the routes and we know all grid coordinates that make up each route, you can visualize each tile as the zigzagging route determined by its coordinates. Algorithm X is going to get a pile of various shaped, sometimes zigzagging, tiles to be placed on the grid, each tile representing one possible route.

Of course, you will need a data structure where you store all the cells for each route. When Algorithm X tells you route 15 for the ball at `(3, 4)` is part of the solution, you will need to know how to display that route in your output.

To be honest, generating an exhaustive list of routes in this puzzle is harder than setting up Algorithm X.

# Identifying Requirements

The Winamax problem statement is very well written. From the problem statement excerpt above we know all ball locations must be covered and all hole locations must be covered. What about the requirement that paths never cross? Since any two paths would cross at a single point on the grid, it sounds like any point on the grid that is not a ball or a hole does not need to be covered by any route, but if it is covered, it can only be covered once. That is a pretty straightforward optional requirement.

What about the requirement that a "ball [...] cannot stop in a water hazard."? Is that something Algorithm X needs to know about? No, it is not. This requirement is part of your algorithm that generates all possible routes from balls to holes. A route is not legitimate if any section of that route lands in a water hazard. By the time these routes get to Algorithm X, they need to be proper routes.

# Putting It All Together

Winamax is a great fit for Algorithm X. Once you separate the process of identifying routes and the process of finding a set of routes that exactly matches up the balls to the holes, the problem becomes much more manageable than it might have seemed at first. You still need to carefully identify every requirement covered by each route, but when you do, Algorithm X will quickly return a solution.

