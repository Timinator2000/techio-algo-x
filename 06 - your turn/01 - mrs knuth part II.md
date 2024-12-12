# Time to Finish Mrs. Knuth - Part II

You have everything you need to finish up Mrs. Knuth - Part II [Awaiting Approval - See CG Contribution Page](https://www.codingame.com/contribute/community). Before you embark on that journey, I want to give you a bit of insight into one coding technique I use over and over when dealing with mutually exclusive (ME) requirements. I keep them separate from the other requirements until I am ready to pass them to the `AlgorithmXSolver` constructor. I do that so I can easily add the appropriate ME requirements to the list of requirements satisfied by each action. The following is a mix of Python and pseudocode that you might find helpful as you organize your subclass constructor code.

```python
class MrsKnuthPartIISolver(AlgorithmXSolver):

    # Add a class attribute to identify loud instruments.
    LOUD_INSTRUMENTS = ['Trumpet', 'Trombone', 'Drums']

    def __init__(self, teacher_availability, students):

        # In this example, the requirements are still hard-coded for the example test case.

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
                                 ('instrument on day', 'F', 'Flute')]

        # Keep the ME requirements separate until after the actions are built.
        me_requirements = [(('Ella', 'F', 10), ('Drew', 'F', 11)),
                           (('loud instrument', 'F', 8), ('loud instrument', 'F', 9)),
                           (('loud instrument', 'F', 9), ('loud instrument', 'F', 10)),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        # Rather than hard-coding the actions, I will provide more generic pseudocode.
        actions = dict()

        for each student:
            for each day in the students availability:
                for each hour of availability on this day:
                    action = ('place student', student name, student instrument, day, hour)
                    actions[action] = [('student scheduled', student name),
                                       ('slot filled', day, hour),
                                       ('instrument on day', day, instrument)]

                    # At this point, only the requirements and optional requirements have been
                    # added to the list. We still need to add ME requirements for potential
                    # troublesome pairs and/or loud instrument conflicts.

                    # Use a list comprehension to add any applicable troublesome pair ME requirements.
                    actions[action] += [me for me in me_requirements if (student name, day, hour) in me]

                    # Use a list comprehension to add any applicable loud instrument ME requirements.
                    if the student plays a loud instrument
                        actions[action] += [me for me in me_requirements if ('loud instrument', day, hour) in me]

        # Now that relationships between requirements and actions have been identified, make sure the
        # ME requirements are properly included with the rest of the optional requirements.

        optional_requirements += me_requirements 

        super().__init__(requirements, actions, optional_requirements)
```

Problems that feature mutual exclusivity can have a significant number of `me_requirements`. Keeping the `me_requirements` separate until the rest of your setup is complete makes it easy to use a list comprehension to filter out and include just the appropriate `me_requirements`.

Now, on to the puzzle!
