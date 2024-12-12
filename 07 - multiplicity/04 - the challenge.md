# Duplicate Solutions

Here is the output from the previous code block:

```text
Solution 1
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 10.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8.
Solution 2
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 10.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8.
Solution 3
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 11.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8.
Solution 4
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 11.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8.
```

What is going on? Solution 1 and solution 2 are perfect duplicates. The same is true for solution 3 and solution 4. To get to the bottom of things, I will regenerate the output, but this time, I will include the `lesson_number` included in each action tuple.

```
Solution 1
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 10. This is Drew's first lesson.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1. This is Lola's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8. This is Ella's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8. This is Ella's second lesson.
Solution 2
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 10. This is Drew's first lesson.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1. This is Lola's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8. This is Ella's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8. This is Ella's second lesson.
Solution 3
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 11. This is Drew's first lesson.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1. This is Lola's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8. This is Ella's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8. This is Ella's second lesson.
Solution 4
   Add Drew/Trombone to Mrs. Knuth's schedule on F at 11. This is Drew's first lesson.
   Add Lola/Drums to Mrs. Knuth's schedule on F at 1. This is Lola's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on Tu at 8. This is Ella's first lesson.
   Add Ella/Flute to Mrs. Knuth's schedule on M at 8. This is Ella's second lesson.
```

Do you see the problem? Algorithm X considers solution 1 and solution 2 to be different because for solution 1, Ella is doing her first lesson on Monday while in solution 2, Ella is doing her second lesson on Monday. We created this problem when we told Algorithm X that scheduling Ella’s first lesson is distinct from scheduling her second lesson.

Fortunately, there is an easy fix!
