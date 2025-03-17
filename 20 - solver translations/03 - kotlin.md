# Kotlin

__Translation Author:__ [@VizGhar](https://www.codingame.com/profile/c152bee9fe8dc90ac4f6b84505b59ebb9086993)

Ruby is a high-level, dynamically typed programming language known for its readability and ease of use. Ruby shares many similarities with Python, such as automatic memory management and object-oriented principles.

@Rafarafa has provided a word for word translation, even preserving the comments found in the provided Python code. Using the Ruby solver below is extremely similar to the Python examples found in the playground.

# Requirements and Actions

Instead of `tuple`s for requirements and actions, @VizGhar uses data classes, a similar, but more powerful container for data elements. Consider the 4 types of requirements for Sudoku. Each cell must be covered with a number, each number must appear in each row, each number must appear in each column and each number must appear in each box. @VizGhar creates 4 separate data classes, each of which inherits from a generic `Requirement`.

In my Python, each of my `tuple`s begins with a string that identifies one of the 4 requirement types. In @VizGhar’s Kotlin, the class identifies one of the 4 requirement types and the strings become unnecessary.

Before building your solver subclass, you need to define classes for your requirements and actions. In the following code snippet, I have defined the 4 types of requirements and the 1 action type found in Sudoku.

```kotlin
sealed interface Requirement {
    data class CellCovered(val row: Int, val col: Int) : Requirement
    data class BoxCovered(val box: Int, val value: Char) : Requirement
    data class RowCovered(val row: Int, val value: Char) : Requirement
    data class ColumnCovered(val col: Int, val value: Char) : Requirement
}

data class Action(val row: Int, val col: Int, val value: Char)
```

# Solver Construction and Initialization

Using my Python solver, the following process has been followed:

1. Create a subclass that inherits from `AlgorithmXSolver`.
1. Override the constructor to build requirements and actions.
1. Prior to existing the subclass constructor, call the superclass constructor passing the newly built requirements and actions.

In Kotlin, your solver subclass cannot override the inherited constructor. Requirements and actions must be built __before__ initializing your solver. In the following 9x9 Sudoku example, I have added a function called `createSolver`, which builds the requirements and actions before creating an instance of `SudokuSolver`.

# Example - 9x9 Sudoku

```kotlin
class SudokuSolver(requirements: List<Requirement>, actions: Map<Action, List<Requirement>>) : 
            DLXSolver<Requirement, Action>(requirements, actions) {

    override fun processSolution(solution: List<Action>): Boolean {

        // Using the Actions in the solution, build a grid and print the solved Sudoku.

        return true    // Return true to stop looking for more solutions.
    }
}


fun createSolver(grid: List<CharArray>, values: String): SudokuSolver {

    val requirements = mutableListOf<Requirement>()

    // Build the requirements.

    val actions = mutableMapOf<Action, List<Requirement>>()

    // Build the actions.

    return SudokuSolver(requirements, actions)
}


fun main() {
    createSolver(List(9) { readln().toCharArray() }, ALL_VALUES).solve()
}
```

# The Solver Code

For even more details, code examples and most importantly, the Kotlin `DLXSolver` code, please visit [@VizGhar's GitHub page](https://github.com/VizGhar/Kotlin-DLX/tree/main).
