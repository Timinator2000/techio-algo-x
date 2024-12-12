# Algorithm X Setup

This toy example is a straightforward Algorithm X setup. What are the requirements? Each student must be assigned to a team color and each grade (age) must be represented on each team. What are the actions? Each action assigns a team color to one of the students. But, how do we make sure the siblings are always placed on the same team? Using colors to enforce sameness, of course! Let’s build a solution one step at a time. At the bottom is a fully funcitonal solution if you wish to experiment further. 


# Building the All-or-None Sets

Because all siblings share identical last names, the all-or-none sets are easily built using a `dictionary` to organize the `Student`s into families. Each key is a last name and each value is a list of all the `Student`s that are part of that family.

```python
        self.families = defaultdict(list)
        for student in students:
            last_name = student.name.split()[-1]
            self.families[last_name].append(student)
```

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

# Enforcing Sameness Using Colors

Per the [steps]( coloring-with-your-solver) outlined a few pages earlier, an attribute is added to track color assignments and the `AlgorithmXSolver` `_process_row_selection()` and `_process_row_deselection()` methods are overridden:

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

# Building Teams from a Solution

As I loop through the actions of each solution, I append the name of each student to the appropriate team color in a `dictionary`.

```python
    for solution in solver.solve():
        teams = {'r':[], 'g':[], 'b':[]}
        for _, name, team_color in solution:
            teams[team_color].append(name)
```

# The Full Solution

Putting it all together results in the following. Feel free to make changes and experiment. Most importantly, this solution is provided as a comparison to the second approach to enforcing sameness covered next: complex actions.

@[Enforcing Sameness with Colors]({"stubs": ["scavenger_hunt_with_coloring.py"], "command": "python3 scavenger_hunt_with_coloring_test.py"})
