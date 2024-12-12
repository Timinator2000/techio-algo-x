# TECH.IO allows me to use this import statement to make my examples concise and easy
# to study. Unless your coding environment will let you create an AlgorithmX package,
# you will need to copy all of the AlgorithmXSolver code into your code.

from AlgorithmX import AlgorithmXSolver

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


def main_program():

    teacher_availability = None
    students = None

    solver = MrsKnuthPartISolver(teacher_availability, students)
          
    for solution in solver.solve():
        print(f'These are the steps to build a solution:')
        for _, name, instrument, day, hour in solution:
            print(f'   Add {name}/{instrument} to Mrs. Knuth\'s schedule on {day} at {hour}.')
