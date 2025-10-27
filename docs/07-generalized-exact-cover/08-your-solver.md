# Extending your `AlgorithmXSolver` Subclass

Adding optional requirements to your solver is as easy as passing a third argument to the `AlgorithmXSolver` constructor. Before I walk through the code, I need to address an alternate option that allows Algorithm X to handle a generalized exact cover. In the [Wikipedia Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) discussion, you will see the following:

>As Knuth explains, a generalized exact cover problem can be converted to an equivalent exact cover problem by simply appending one row for each secondary column, containing a single 1 in that column.[6] If in a particular candidate solution a particular secondary column is satisfied, then the added row isn't needed. But if the secondary column isn't satisfied, as is allowed in the generalized problem but not the standard problem, then the added row can be selected to ensure the column is satisfied.

The next paragraph in the Wikipedia article continues with:

>But Knuth goes on to explain that it is better working with the generalized problem directly, because the generalized algorithm is simpler and faster: __A simple change to his Algorithm X allows secondary columns to be handled directly.__ [emphasis added]

__With my `AlgorithmXSolver`, you never need to add extra rows as is suggested in the first paragraph. Could you? Yes, you could. You could add the extra rows and only use the requirements argument. You could do some of both. However, I don’t recommend any of that.__

__Conceptually, problems have requirements (primary constraints/columns) and optional requirements (secondary constraints/columns). I recommend always keeping them separate, passing them to the `AlgorithmXSolver` constructor separately, and letting the `AlgorithmXSolver` handle the needed algorithmic changes.__

In the general sense, your new solver subclass takes the following form:

```python
class MrsKnuthPartIISolver(AlgorithmXSolver):

    def __init__(self, arguments):

        requirements = list()
        optional_requirements = list()

        actions = dict()

        super().__init__(requirements, actions, optional_requirements)
```

The following hard-coded solution brings all the previous concepts together. Copy this code into your coding environment and experiment with it. If needed, include the full [AlgorithmXSolver](../03-AlgorithmXSolver/01-the-AlgorithmXSolver.md#using-the-algorithmxsolver-class) code directly instead of relying on the `import` statement.

```python
# Unless your coding environment will let you create an AlgorithmX package,
# you will need to copy all of the AlgorithmXSolver code into your code.

from AlgorithmX import AlgorithmXSolver

class MrsKnuthPartIISolver(AlgorithmXSolver):

    def __init__(self, teacher_availability, students):
        
        requirements = [('student scheduled', 'Drew'),
                        ('student scheduled', 'Ella'),
                        ('student scheduled', 'Lola')]

        optional_requirements = [('slot filled', 'F', 8),
                                 ('slot filled', 'F', 9),
                                 ('slot filled', 'F', 10),
                                 ('slot filled', 'F', 11),
                                 ('slot filled', 'F', 1),
                                 ('instrument on day', 'F', 'Trombone'),
                                 ('instrument on day', 'F', 'Drums'),
                                 ('instrument on day', 'F', 'Flute'),
                                 (('Ella', 'F', 10), ('Drew', 'F', 11)),
                                 (('loud instrument', 'F', 8), ('loud instrument', 'F', 9)),
                                 (('loud instrument', 'F', 9), ('loud instrument', 'F', 10)),
                                 (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        actions = dict()

        action = ('place student', 'Drew', 'Trombone', 'F', 10)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 10),
                           ('instrument on day', 'F', 'Trombone'),
                           (('loud instrument', 'F', 9), ('loud instrument', 'F', 10)),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Drew', 'Trombone', 'F', 11)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 11),
                           ('instrument on day', 'F', 'Trombone'),
                           (('Ella', 'F', 10), ('Drew', 'F', 11)),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Drew', 'Trombone', 'F', 1)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Trombone')]

        action = ('place student', 'Ella', 'Flute', 'F', 10)
        actions[action] = [('student scheduled', 'Ella'),
                           ('slot filled', 'F', 10),
                           ('instrument on day', 'F', 'Flute'),
                           (('Ella', 'F', 10), ('Drew', 'F', 11))]

        action = ('place student', 'Ella', 'Flute', 'F', 1)
        actions[action] = [('student scheduled', 'Ella'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Flute')]

        action = ('place student', 'Lola', 'Drums', 'F', 11)
        actions[action] = [('student scheduled', 'Lola'),
                           ('slot filled', 'F', 11),
                           ('instrument on day', 'F', 'Drums'),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Lola', 'Drums', 'F', 1)
        actions[action] = [('student scheduled', 'Lola'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Drums')]
    
        super().__init__(requirements, actions, optional_requirements)


teacher_availability = None
students = None

solver = MrsKnuthPartIISolver(teacher_availability, students)
        
for solution in solver.solve():
    print(f'These are the steps to build a solution:') 
    for _, name, instrument, day, hour in solution:
        print(f'   Add {name}/{instrument} to Mrs. Knuth\'s schedule on {day} at {hour}.')
```

<BR>