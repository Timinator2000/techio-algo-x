# Create an `AlgorithmXSolver` Subclass

Creating a customized solver only has two required steps. First, create a solver class that inherits from `AlgorithmXSolver`. Second, override the constructor to build your requirements and actions. Let's create a solver to help Mrs. Knuth:

``` python
class MrsKnuthPartISolver(AlgorithmXSolver):

    def __init__(self):
        
        requirements = list()
        actions = dict()

        super().__init__(requirements, actions)
```

The last line might be a bit unfamiliar. When overriding a method, such as the constructor in this case, the goal is sometimes to simply add functionality to the existing functionality. There is actually a lot going on in the `AlgorithmXSolver` constructor and it all depends on having a list of requirements and a dictionary of actions that are needed to build the matrix. Once the requirements and actions are built, use `super()` to invoke the inherited `AlgorithmXSolver` constructor with the newly identified requirements and actions.

# Build the Requirements

Of course, `MrsKnuthPartISolver` needs to know about Mrs. Knuth's availability and all the students that need to be scheduled. For now, I will add parameters to the constructor, but I will leave the details of those parameters to you. For this toy example, I will ignore those parameters and I will  _hard code_ the actions and requirements. Obviously, this will not be sufficient for anything other than the first test case in the puzzle.

```python
class MrsKnuthPartISolver(AlgorithmXSolver):

    def __init__(self, teacher_availability, students):
        
        requirements = [('student scheduled', 'Ayla'),
                        ('student scheduled', 'Bob'),
                        ('student scheduled', 'Alex'),
                        ('slot filled', 'Th', 2),
                        ('slot filled', 'Th', 3),
                        ('slot filled', 'Th', 4),
                        ('instrument on day', 'Th', 'Trumpet'),
                        ('instrument on day', 'Th', 'Drums'),
                        ('instrument on day', 'Th', 'Tuba')]
        
        actions = dict()

        super().__init__(requirements, actions)
```

# Build the Actions

Notice that I copied those requirements right out of our previous discussion. The last thing we need to do is build the dictionary of actions and for each action, I need to add a list of requirements that are satisfied if that action is included in the solution. The complete, customized solver looks like this:

```python
class MrsKnuthPartISolver(AlgorithmXSolver):

    def __init__(self, teacher_availability, students):
        
        requirements = [('student scheduled', 'Ayla'),
                        ('student scheduled', 'Bob'),
                        ('student scheduled', 'Alex'),
                        ('slot filled', 'Th', 2),
                        ('slot filled', 'Th', 3),
                        ('slot filled', 'Th', 4),
                        ('instrument on day', 'Th', 'Trumpet'),
                        ('instrument on day', 'Th', 'Drums'),
                        ('instrument on day', 'Th', 'Tuba')]
        
        actions = dict()

        action = ('place student', 'Ayla', 'Trumpet', 'Th', 2)

        actions[action] = [('student scheduled', 'Ayla'),
                           ('slot filled', 'Th', 2),
                           ('instrument on day', 'Th', 'Trumpet')]
        
        action = ('place student', 'Bob', 'Drums', 'Th', 2)
        
        actions[action] = [('student scheduled', 'Bob'),
                           ('slot filled', 'Th', 2),
                           ('instrument on day', 'Th', 'Drums')]

        action = ('place student', 'Bob', 'Drums', 'Th', 3)
        
        actions[action] = [('student scheduled', 'Bob'),
                           ('slot filled', 'Th', 3),
                           ('instrument on day', 'Th', 'Drums')]

        action = ('place student', 'Alex', 'Tuba', 'Th', 2)
        
        actions[action] = [('student scheduled', 'Alex'),
                           ('slot filled', 'Th', 2),
                           ('instrument on day', 'Th', 'Tuba')]

        action = ('place student', 'Alex', 'Tuba', 'Th', 4)
        
        actions[action] = [('student scheduled', 'Alex'),
                           ('slot filled', 'Th', 4),
                           ('instrument on day', 'Th', 'Tuba')]
        
        super().__init__(requirements, actions)
```

That's it! We have an (almost) fully functional `MrsKnuthPartISolver`. You will make it fully functional when you build the requirements and the actions from the parameters rather than hard coding them like I did. Next, we need to ask our new solver to find the solution for us!
