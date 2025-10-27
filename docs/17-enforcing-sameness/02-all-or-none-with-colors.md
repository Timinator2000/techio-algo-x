# Algorithm X Setup

This toy example is a straightforward Algorithm X setup. What are the requirements? Each student must be assigned to a team color and each grade (age) must be represented on each team. What are the actions? Each action assigns a team color to one of the students. But, how do we make sure the siblings are always placed on the same team? Using colors to enforce sameness, of course! Let’s build a solution one step at a time. At the bottom is a fully functional solution if you wish to experiment further. 

---

# Building the All-or-None Sets

Because all siblings share identical last names, the all-or-none sets are easily built using a `dictionary` to organize the `Student`s into families. Each key is a last name and each value is a list of all the `Student`s that are part of that family.

```python
        self.families = defaultdict(list)
        for student in students:
            last_name = student.name.split()[-1]
            self.families[last_name].append(student)
```

---

# Requirements and Actions

Two list comprehensions capture all the requirements. 1 to 3 actions is created for each child. If the child is a captain, only one team color assignment is possible. If the child is not a captain, the child could be put on any of the 3 teams.

```python
        requirements = [('student assigned', student.name) for student in students]
        requirements += [('grade covered', grade, team_color) for grade in range(1, 7) for team_color in 'rgb']
        
        actions = dict()
        for student in students:
            possible_teams = captains[student.name] if student.name in captains else 'rgb'
            for team_color in possible_teams:
                action = ('assign student', student.name, team_color)
                actions[action] = [('student assigned', student.name), ('grade covered', student.grade, team_color)]
```

---

# Enforcing Sameness Using Colors

Per the [steps](../15-coloring-your-requirements/02-constructing-a-word-search.md#adding-coloring-logic-to-your-solver) outlined a few pages earlier, an attribute is added to track color assignments and the `AlgorithmXSolver` `_process_row_selection()` and `_process_row_deselection()` methods are overridden:

```python
        self.student_colors = {student.name:[] for student in students}
```

```python
    def _process_row_selection(self, row):
        _, name, team_color = row
        for sibling in self.families[name.split()[-1]]:
            if self.student_colors[sibling.name] and team_color != self.student_colors[sibling.name][-1]:
                self.solution_is_valid = False

            self.student_colors[sibling.name].append(team_color)

            
    def _process_row_deselection(self, row):
        _, name, team_color = row
        for sibling in self.families[name.split()[-1]]:
            self.student_colors[sibling.name].pop()
```

---

# Building Teams from a Solution

As I loop through the actions of each solution, I append the name of each student to the appropriate team color in a `dictionary`.

```python
    for solution in solver.solve():
        teams = {'r':[], 'g':[], 'b':[]}
        for _, name, team_color in solution:
            teams[team_color].append(name)
```

---

# The Full Solution

Putting it all together results in the following. Copy the following code into your coding environment, make changes and experiment. Most importantly, this solution is provided as a comparison to the second approach to enforcing sameness covered next: complex actions.

```python
# Unless your coding environment will let you create an AlgorithmX package,
# you will need to copy all of the AlgorithmXSolver code into your code.

from AlgorithmX import AlgorithmXSolver

from collections import namedtuple, defaultdict
from typing import List, Dict

Student = namedtuple('Student', 'name grade')

class ScavengerHuntSolverUsingColors(AlgorithmXSolver):
    
    def __init__(self, students: List[Student], captains: Dict[str, str]):
        
        self.student_colors = {student.name:[] for student in students}
        
        self.families = defaultdict(list)
        for student in students:
            last_name = student.name.split()[-1]
            self.families[last_name].append(student)
            
        requirements = [('student assigned', student.name) for student in students]
        requirements += [('grade covered', grade, team_color) for grade in range(1, 7) for team_color in 'rgb']
        
        actions = dict()
        for student in students:
            possible_teams = captains[student.name] if student.name in captains else 'rgb'
            for team_color in possible_teams:
                action = ('assign student', student.name, team_color)
                actions[action] = [('student assigned', student.name), ('grade covered', student.grade, team_color)]
                
        super().__init__(requirements, actions)
        
        
    def _process_row_selection(self, row):
        _, name, team_color = row
        for sibling in self.families[name.split()[-1]]:
            if self.student_colors[sibling.name] and team_color != self.student_colors[sibling.name][-1]:
                self.solution_is_valid = False

            self.student_colors[sibling.name].append(team_color)

            
    def _process_row_deselection(self, row):
        _, name, team_color = row
        for sibling in self.families[name.split()[-1]]:
            self.student_colors[sibling.name].pop()


students = [Student('Wednesday Addams', 1), Student('Maggie Simpson', 1), Student('Michelle Tanner', 1),
            Student('Brenda Walsh', 2), Student('Arnold Jackson', 2), Student('Arthur Fonzarelli', 2),
            Student('Stephanie Tanner', 3), Student('Darlene Conner', 3), Student('Carlton Banks', 3),
            Student('Willis Jackson', 4), Student('Pugsley Addams', 4), Student('Marcia Brady', 4),
            Student('Greg Brady', 5), Student('Lisa Simpson', 5), Student('Joanie Cunningham', 5),
            Student('Richie Cunningham', 6), Student('Bart Simpson', 6), Student('D. J. Tanner', 6) ]

captains = {'Brenda Walsh': 'r', 'Arnold Jackson': 'g', 'Arthur Fonzarelli': 'b'}

solver = ScavengerHuntSolverUsingColors(students, captains)

count = 0
for solution in solver.solve():
    count += 1
    teams = {'r':[], 'g':[], 'b':[]}
    for _, name, team_color in solution:
        teams[team_color].append(name)
        
    print(f'\nOption {count}')
    for color in teams:
        print(f'{color}:', ', '.join(sorted(teams[color], key=lambda s:s.split()[-1])))
```

<BR>