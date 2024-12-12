# TECH.IO allows me to use this import statement to make my examples concise and easy
# to study. Unless your coding environment will let you create an AlgorithmX package,
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


def main_program():

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
