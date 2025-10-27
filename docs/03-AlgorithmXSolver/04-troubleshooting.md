# Print Your Requirements & Actions

The first troubleshooting step to take is simply printing the requirements, the actions and the requirements satisfied by each action. Hopefully, this can be done on a small test case. If the test case is big and there are a lot of requirements and actions, sifting through the printed data can be daunting.

When printing the requirements and actions, I suggest doing it right before you invoke the inherited `AlgorithmXSolver` constructor, similar to this:

``` python
        for r in requirements:
            print(r)

        for a in actions:
            print(a)
            for r in actions[a]:
                print('   ', r)
        
        super().__init__(requirements, actions)
```

---

# Study Your Errors

It is critical the tuples you use for requirements and actions always line up with each other so you do not get `KeyError`s when `AlgorithmXSolver` is setting up the DLX matrix. For instance, `('slot filled', 'Th', 4)` is __not__ the same as `('slot filled', 'Thurs', 4)`. I’m sure that seems obvious, but when you get a `KeyError`, look for places you might have requirement specs that are supposed to be the same, but are slightly different.

```text
Traceback (most recent call last):
  File "/project/target/part_I_generate_solutions_test.py", line 51, in <module>
    main_program()
  File "/project/target/part_I_generate_solutions.py", line 70, in main_program
    solver = MrsKnuthPartISolver(teacher_availability, students)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/project/target/part_I_generate_solutions.py", line 62, in __init__
    super().__init__(requirements, actions)
  File "/project/target/AlgorithmX.py", line 201, in __init__
    current_col_header   = self.R[requirement]
                           ~~~~~~^^^^^^^^^^^^^
KeyError: ('slot filled', 'Thurs', 4)
```

---

# No Solutions Found

Algorithm X not finding any solutions can be the most frustrating situation of all, and it always comes down to some issue with your model. Assuming your problem is guaranteed to have a solution, the only reason Algorithm X will fail to find a solution is that something in your model is not sufficient. __The requirements cannot be perfectly covered by any possible combination of actions.__ Something is wrong in your mapping of satisfied requirements for each action.

Although this can be frustrating, you will get better and better at building models with practice. The flip side of this frustration is that after you become proficient at building models you will experience elation when you surprise yourself by solving an exact cover problem much faster than you ever expected!

---

# Practice Makes Perfect

This exercise will help you understand how **Algorithm X** depends on precise mappings between *requirements* and *actions* — and how even small inconsistencies can cause runtime or logical errors.

On the previous page, you saw a *hard-coded* solution to the **Mrs. Knuth Part I** example test case. Copy that code into your coding environment. Make sure the `AlgorithmX` solver code is available — either include it directly or place it in a separate file and import it.

Now, explore and experiment with the code as follows:

## 1. Inspect the Data Structures

Print out all of the following:

* The **requirements**
* The **actions**
* The list of **requirements satisfied by each action**

Verify that:

* Every requirement is covered by at least one action.
* The structure of your data matches what the solver expects.

This step helps you confirm that your constraint data is correctly linked before running the solver.

## 2. Introduce a `KeyError`

Make a **tiny edit** that breaks the connection between requirements and actions.
For example:

* Change `"R3"` to `"R-3"` in one place, or
* Remove a single requirement from the dictionary.

Run the solver again and observe the **`KeyError`** message. Which part of the algorithm raised the error? Why did it fail there?

## 3. Create a “Silent Failure”

Now make a **different small change** — one that doesn’t cause a runtime error but still prevents Algorithm X from finding a solution.
For instance:

* Remove one action that is essential for satisfying all requirements

Run the solver. It should complete without crashing, but **no solution** will be found. Is it clear what happened?

<BR>