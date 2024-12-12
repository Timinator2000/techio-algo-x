# Requirements Need More Precision

Let's take another look at the example problem:

```
M 8 Tu 8 W 8 Th 8 F 8 9 10 11 1
3
Drew Trombone 1 M Tu W Th F 10 11
Ella Flute 2 M 8 Tu 8 W Th F 11
Lola Drums 1 M Tu W Th F 11 1
1
Drew Ella
```

Requirements must be binary in Algorithm X. Either they have been covered or they have not been covered. It is important to make sure there is no middle ground, such as Ella being scheduled is "half-way covered" because 1 of her 2 lessons has been scheduled and the other still needs to be scheduled.

As problems get more complex, it is often helpful to quickly identify the steps that need to be taken to solve a simple or “toy” version of the problem and the example test case works perfectly. What needs to happen to build a solution?

1. Drew’s one lesson must be scheduled.

1. Lola’s one lesson must be scheduled.

1. Ella’s first lesson must be scheduled.

1. Ella’s second lesson must be scheduled.

We now see four requirements are needed to make sure these three students are properly scheduled. More precisely, a requirement specification now needs more than just a name. It also needs to identify which lesson has been scheduled. Is it the student’s first lesson? Second lesson? Third lesson? Let’s add `lesson number` to each requirement specification.

```text
('student scheduled', 'Drew', 1)
('student scheduled', 'Lola', 1)
('student scheduled', 'Ella', 1)
('student scheduled', 'Ella', 2)
```

This is a much more complete set of requirements. Four requirements must be covered, resulting in four lessons being scheduled, one for Drew, one for Lola and two for Ella.

# Actions Need More Precision

Looking at each student’s availability, we initially come up with this list of possible actions:

```
('place student', 'Drew', 'Trombone', 'F', 10)
('place student', 'Drew', 'Trombone', 'F', 11)
('place student', 'Ella', 'Flute', 'M', 8)
('place student', 'Ella', 'Flute', 'Tu', 8)
('place student', 'Ella', 'Flute', 'F', 11)
('place student', 'Lola', 'Drums', 'F', 11)
('place student', 'Lola', 'Drums', 'F', 1)
```

If you think through those actions, you realize the action specification does not have enough information. If we schedule Ella on Friday at 11, are we scheduling her first lesson or her second lesson? It is critical that we schedule both her first and second lesson, but right now, we have no way to distinguish which lesson is being scheduled. We need to add `lesson number` to the action specification:

```
updated action specification = (‘place student’, student name, instrument, day, hour, lesson number)
```

Notice below that all actions must adhere to the same specification. Even the students that have only requested a single lesson need to have a `1` in the action specification for `lesson number`. You see 3 extra actions have been added for Ella since scheduling her first lesson is distinct from scheduling her second lesson.

```
('place student', 'Drew', 'Trombone', 'F', 10, 1)       # Schedule Drew's FIRST lesson on Friday at 10.
('place student', 'Drew', 'Trombone', 'F', 11, 1)       # Schedule Drew's FIRST lesson on Friday at 11.
('place student', 'Ella', 'Flute', 'M', 8, 1)           # Schedule Ella's FIRST lesson on Monday at 8.
('place student', 'Ella', 'Flute', 'M', 8, 2)           # Schedule Ella's SECOND lesson on Monday at 8.
('place student', 'Ella', 'Flute', 'Tu', 8, 1)          # Schedule Ella's FIRST lesson on Tuesday at 8.
('place student', 'Ella', 'Flute', 'Tu', 8, 2)          # Schedule Ella's SECOND lesson on Tuesday at 8.
('place student', 'Ella', 'Flute', 'F', 11, 1)          # Schedule Ella's FIRST lesson on Friday at 11.
('place student', 'Ella', 'Flute', 'F', 11, 2)          # Schedule Ella's SECOND lesson on Friday at 11.
('place student', 'Lola', 'Drums', 'F', 11, 1)          # Schedule Lola's FIRST lesson on Friday at 11.
('place student', 'Lola', 'Drums', 'F', 1, 1)           # Schedule Lola's FIRST lesson on Friday at 1.
```

As we have seen with both the requirements and the actions, multiplicity forces us to be more precise. Next, I'll bring everything together and generate solutions.
