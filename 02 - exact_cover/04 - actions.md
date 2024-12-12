# Identifying Actions

The 9 requirements, identified previously, perfectly define the problem in Test Case #1. All we have to do now is find a set of actions that “exactly covers” these requirements, but first we have to identify actions that _could_ be taken as we try to build a solution.

A schedule is built for Mrs. Knuth by placing students into her available teaching slots. Every action we could take to build a solution comes down to placing one student into one slot. Of course, we need to make sure the student’s availability and Mrs. Knuth’s availability are properly honored, but I’ll leave those details to you. Let’s look at each student independently.

Ayla is available on Thursday at 2, so only one action is possible: We can place Ayla on the schedule on Thursday at 2. Again, we will distinguish each action with a human readable tuple.

```text
('place student', 'Ayla', 'Th', 2)
```

Notice that 3 pieces of data are required to distinguish one potential action from another. We need to know the name of the student being placed, the day and the hour.

Bob is available on Thursday at 2 and 3. Alex is available on Thursday at 2 and 4. We need to add two possible actions for placing Bob on the schedule and 2 more possible actions for placing Alex on the schedule. If we add these 4 actions to the one action we already identified, our full list of possible actions looks like this:

```text
('place student', 'Ayla', 'Th', 2)
('place student', 'Bob', 'Th', 2)
('place student', 'Bob', 'Th', 3)
('place student', 'Alex', 'Th', 2)
('place student', 'Alex', 'Th', 4)
```

# Linking Actions to Requirements

So far, we’ve built a complete list of requirements that must be satisfied by any potential solution and we have a list of actions that can be used to build potential solutions. The last thing we need to define is a map between the actions and the requirements. For each action, we must identify the requirements satisfied by that action. 

Let's look at the first action in our list: `('place student', 'Ayla', 'Th', 2)`. If we add this action to a potential solution, which requirements from our requirements list will be satisfied? A simple example like this makes it easy to go through the requirements one by one to determine which requirements are satisfied and we end up with the following:

```text
Action: ('place student', 'Ayla', 'Th', 2)
    Satisfied Requirements: ('student scheduled', 'Ayla')
                            ('slot filled', 'Th', 2)
                            ('instrument on day', 'Th', 'Trumpet')
```

The first two should be obvious, but what about the 3rd requirement? Why is that requirement satisfied? We know from the input that Ayla plays the Trumpet. We could keep a separate list of instruments played by each student, but I recommend another approach. Because each student has exactly one instrument, my preference is to update our list of actions to include each student’s instrument:

```text
('place student', 'Ayla', 'Trumpet', 'Th', 2)
('place student', 'Bob', 'Drums', 'Th', 2)
('place student', 'Bob', 'Drums', 'Th', 3)
('place student', 'Alex', 'Tuba', 'Th', 2)
('place student', 'Alex', 'Tuba', 'Th', 4)
```

Instead of “placing Ayla on Thursday at 2”, we are now “placing Ayla, with her Trumpet, on Thursday at 2. Later in this playground I will explain why these human readable tuples never impact our `AlgorithXSolver`’s performance, which is why I always prefer having a little extra data in a tuple as compared to having to keep track of a separate list that identifies what instrument each student plays.

# A Complete Model

The [Texas Gateway for Online Resources](https://www.texasgateway.org/resource/scientific-models) makes this simple statement about models on their website: 

>Models can help you visualize, or picture in your mind, something that is difficult to see or understand. Models can help scientists communicate their ideas, understand processes, and make predictions.

Models show up everywhere in life. Architects build models of buildings. Engineers build models of new products. Computer Scientists use the Unified Modeling Language (UML) to build models of software solutions before writing code.

We have now created a model of the problem using requirements, actions and a mapping from actions to satisfied requirements. Putting it all in one place looks like this:

```text
Requirements:
    ('student scheduled', 'Ayla')
    ('student scheduled', 'Bob')
    ('student scheduled', 'Alex')
    ('slot filled', 'Th', 2)
    ('slot filled', 'Th', 3)
    ('slot filled', 'Th', 4)
    ('instrument on day', 'Th', 'Trumpet')
    ('instrument on day', 'Th', 'Drums')
    ('instrument on day', 'Th', 'Tuba')

Action: ('place student', 'Ayla', 'Trumpet', 'Th', 2)
    Satisfied Requirements: ('student scheduled', 'Ayla')
                            ('slot filled', 'Th', 2)
                            ('instrument on day', 'Th', 'Trumpet')

Action: ('place student', 'Bob', 'Drums', 'Th', 2)
    Satisfied Requirements: ('student scheduled', 'Bob')
                            ('slot filled', 'Th', 2)
                            ('instrument on day', 'Th', 'Drums')
   
Action: ('place student', 'Bob', 'Drums', 'Th', 3)
    Satisfied Requirements: ('student scheduled', 'Bob')
                            ('slot filled', 'Th', 3)
                            ('instrument on day', 'Th', 'Drums')

Action: ('place student', 'Alex', 'Tuba', 'Th', 2)
    Satisfied Requirements: ('student scheduled', 'Alex')
                            ('slot filled', 'Th', 2)
                            ('instrument on day', 'Th', 'Tuba')

Action: ('place student', 'Alex', 'Tuba', 'Th', 4)
    Satisfied Requirements: ('student scheduled', 'Alex')
                            ('slot filled', 'Th', 4)
                            ('instrument on day', 'Th', 'Tuba')
```

This text-based model might work well for you, but for those of you that prefer a more visual model, we must step into the matrix...
