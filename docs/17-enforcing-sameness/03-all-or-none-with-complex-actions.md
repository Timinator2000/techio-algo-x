# Simple vs Complex Actions

The problem has not changed, so it makes sense the requirements remain exactly the same. However, in this approach, we will look at actions a bit differently. Previously, each action assigned a team color to one student, creating a _simple_ action that accomplished a single task. Here, each action will assign a team color to 1 or more students.

__Complex Action:__ Multiple simple actions combined into a single action.

Using simple actions, it takes 3 separate `tuple`s to assign Bart, Lisa and Maggie Simpson to the red team:

```python
('assign student', 'Bart Simpson', 'r')
('assign student', 'Lisa Simpson', 'r')
('assign student', 'Maggie Simpson', 'r')
```

Keep in mind, each action must be a `tuple` as it will be used as a `key` in the `actions` `dictionary`. These three simple actions could be combined into the following complex action `tuple`:

```python
(('assign student', 'Bart Simpson', 'r'), ('assign student', 'Lisa Simpson', 'r'), ('assign student', 'Maggie Simpson', 'r'))
```

Packing simple actions into a complex action can be done many ways. Ultimately, what matters is that you properly unpack the complex action `tuple` when building a solution. In the code below, I have chosen to pack simple actions into a complex action as follows:

```python
('assign students', ('Bart Simpson', 'Lisa Simpson', 'Maggie Simpson'), 'r')
```

Let’s step through a full solution using complex actions one step at a time.

---

# What Remains the Same?

The following code blocks are identical to the code used previously:

```python
        self.families = defaultdict(list)
        for student in students:
            last_name = student.name.split()[-1]
            self.families[last_name].append(student)
```

```python
        requirements = [('student assigned', student.name) for student in students]
        requirements += [('grade covered', grade, team_color) for grade in range(1, 7) for team_color in 'rgb']
```

---

# Method Overrides No Longer Necessary

The `AlgorithmXSolver` `_process_row_selection()` and `_process_row_deselection()` methods no longer need to be customized. In the full solution below, you will see this shortens the code a fair amount.

---

# Building the Actions Dictionary

In the following code snippet, notice how the list of names for each family is put into a single action. List comprehensions are used to identify _all_ requirements satisfied by the complex action.  Each student that is part of the family adds two satisfied requirements to the list.

It is important that a family with only one child is still treated as a group of children. Every action, whether the family has 1, 2, 3 or more children, assigns a team color to all members of the family group.

```python
        actions = dict()
        for family in self.families.values():
            possible_teams = 'rgb'
            for student in family:
                if student.name in captains:
                    possible_teams = captains[student.name]
                    
            for team_color in possible_teams:
                action = ('assign students', tuple(student.name for student in family), team_color)
                actions[action] = [('student assigned', student.name) for student in family]
                actions[action] += [('grade covered', student.grade, team_color) for student in family]
```

---

# Building Teams from a Solution

A very minor change must be made as the actions that make up a solution are unpacked. Each action now contains a group of names. That entire group of names must be added to the proper team.

```python
    for solution in solver.solve():
        teams = {'r':[], 'g':[], 'b':[]}
        for _, names, team_color in solution:
            teams[team_color].extend(names)
```

---

# The Full Solution

Putting it all together results in the following. Copy this code into your coding environment, make changes and experiment. Most importantly, this solution is provided as a comparison to the first approach to enforcing sameness covered previously: using colors.

```python
# Unless your coding environment will let you create an AlgorithmX package,
# you will need to copy all of the AlgorithmXSolver code into your code.

from AlgorithmX import AlgorithmXSolver

from collections import namedtuple, defaultdict
from typing import List, Dict

Student = namedtuple('Student', 'name grade')

class ScavengerHuntSolverUsingComplexActions(AlgorithmXSolver):
    
    def __init__(self, students: List[Student], captains: Dict[str, str]):
        
        self.families = defaultdict(list)
        for student in students:
            last_name = student.name.split()[-1]
            self.families[last_name].append(student)
            
        requirements = [('student assigned', student.name) for student in students]
        requirements += [('grade covered', grade, team_color) for grade in range(1, 7) for team_color in 'rgb']
        
        actions = dict()
        for family in self.families.values():
            possible_teams = 'rgb'
            for student in family:
                if student.name in captains:
                    possible_teams = captains[student.name]
                    
            for team_color in possible_teams:
                action = ('assign students', tuple(student.name for student in family), team_color)
                actions[action] = [('student assigned', student.name) for student in family]
                actions[action] += [('grade covered', student.grade, team_color) for student in family]
                
        super().__init__(requirements, actions)


students = [Student('Wednesday Addams', 1), Student('Maggie Simpson', 1), Student('Michelle Tanner', 1),
            Student('Brenda Walsh', 2), Student('Arnold Jackson', 2), Student('Arthur Fonzarelli', 2),
            Student('Stephanie Tanner', 3), Student('Darlene Conner', 3), Student('Carlton Banks', 3),
            Student('Willis Jackson', 4), Student('Pugsley Addams', 4), Student('Marcia Brady', 4),
            Student('Greg Brady', 5), Student('Lisa Simpson', 5), Student('Joanie Cunningham', 5),
            Student('Richie Cunningham', 6), Student('Bart Simpson', 6), Student('D. J. Tanner', 6) ]

captains = {'Brenda Walsh': 'r', 'Arnold Jackson': 'g', 'Arthur Fonzarelli': 'b'}

solver = ScavengerHuntSolverUsingComplexActions(students, captains)

count = 0
for solution in solver.solve():
    count += 1
    teams = {'r':[], 'g':[], 'b':[]}
    for _, names, team_color in solution:
        teams[team_color].extend(names)
        
    print(f'\nOption {count}')
    for color in teams:
        print(f'{color}:', ', '.join(sorted(teams[color], key=lambda s:s.split()[-1])))
```

<BR>