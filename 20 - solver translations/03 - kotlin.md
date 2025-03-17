# Kotlin

__Translation Author:__ [@VizGhar](https://www.codingame.com/profile/c152bee9fe8dc90ac4f6b84505b59ebb9086993)

Ruby is a high-level, dynamically typed programming language known for its readability and ease of use. Ruby shares many similarities with Python, such as automatic memory management and object-oriented principles.

@Rafarafa has provided a word for word translation, even preserving the comments found in the provided Python code. Using the Ruby solver below is extremely similar to the Python examples found in the playground.

# Requirements and Actions

My Python [`AlgorithmXSolver`](the-algorithmxsolver) makes extensive use of `tuple`s. 

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

Different...

# Example - 9x9 Sudoku

Something here...

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

