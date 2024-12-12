# Create a Solver Instance

So far, all we have is a `MrsKnuthPartISolver` class. We need to create an instance of that class. You’ll need to get the input data and organize that data so you can pass it to the constructor.

```python
# Coding the following input is left to you.

# teacher_availability = 
# students =

solver = MrsKnuthPartISolver(teacher_availability, students)
```

# `solver.solve()`

The last step is to ask our solver to give us the solutions. Some exact cover problems have multiple solutions and `AlgorithmXSolver` will always search for __all__ solutions. Each solution found is returned one-by-one via a generator and each solution is a list of actions that make up that solution. Even if your problem is guaranteed to have a single solution, you should use the following format to get all solutions from your solver.

```python
for solution in solver.solve():
    for action in solution:
        # use the action to build your problem's answer
```

I prefer to "unpack" the action tuple so that I have easy access to the information I need. For Mrs. Knuth Part I, each action is a tuple with 5 pieces of data - a title (not needed right now), name, instrument, day and hour.

```python
schedule = some data structure to manage the answer to the puzzle

for solution in solver.solve():
    for _, name, instrument, day, hour in solution:
        # add name/instrument on day/hour to schedule

print(schedule)    # Don't forget how particular Mrs. Knuth is about her schedule formatting.
```

# `solver.solve()` – Only One Solution

Some exact cover problems are guaranteed to have a single solution. When that is the case, you can add a `break` statement after processing the first solution to prevent Algorithm X from looking for more solutions that you know are not to be found. The `break` statement will decrease the amount of time required to finish the problem, and, in extreme cases, this may be exactly what your code needs to finish the problem within the given time limit.

```python
for solution in solver.solve():
    for action in solution:
        # use the action to build your problem's answer

    break
```

It can be helpful to leave the `break` statement out of your code until you are fairly confident in your solution. If your solver is incorrectly generating multiple solutions, the `break` statement will possibly _hide_ your error from you. After you are confident that your code is working properly, add the `break` statement if you need to minimize processing time.

# Putting it All Together

Let's put this all together now. As you look over this code example, keep in mind that the details of _how_ Algorithm X works have been abstracted away. Solving Mrs. Knuth's _Exact Cover_ problem comes down to these fairly reasonable steps:

* Identify the Requirements
  
* Identify the Actions

* Identify the Requirements Satisfied by Each Action

* Process a List of Actions Algorithm X Identified as a Valid Solution

@[Use Algorithm X to find a schedule for Mrs. Knuth Part I]({"stubs": ["part_I_solver.py"], "command": "python3 part_I_solver_test.py"})

As is always the case with computer programming, bugs will work their way into your code. In the next section, I'll give you some debugging tips when using `AlgorithmXSolver`.
