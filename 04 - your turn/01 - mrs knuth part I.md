# Time to Finish Mrs. Knuth - Part I

You have everything you need to finish Mrs. Knuth's first puzzle and get her through the summer. Again, this puzzle can be found here:

Mrs. Knuth - Part I [Awaiting Approval - See CG Contribution Page](https://www.codingame.com/contribute/community)

Here is a little pseudocode to help as you put together your full solution:

```text
copy all the AlgorithmX code

define MrsKnuthPartISolver as a subclass of AlgorithmXSolver 
    override the constructor to build your requirements and actions from 
    the passed in teacher_availability and students

read all input
organize input
    teacher_availability
    students

create an instance of your new MrsKnuthPartISolver class, passing teacher_availability and students to the constructor

for each solution in solver.solve()
    for each action in solution
        add the student/instrument to schedule at hour/day

print the schedule
```

If you run into trouble, review the previous sections in this playground and you will find everything you need. Now that Mrs. Knuth is ready to go, let's look at a few other puzzles you are already fully prepared to solve!
