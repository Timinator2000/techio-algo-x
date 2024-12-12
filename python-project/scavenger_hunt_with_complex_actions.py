# TECH.IO allows me to use this import statement to make my examples concise and easy
# to study. Unless your coding environment will let you create an AlgorithmX package,
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


def main_program():

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
