# Kotlin

__Translation Author:__ [@VizGhar](https://www.codingame.com/profile/c152bee9fe8dc90ac4f6b84505b59ebb9086993)

Ruby is a high-level, dynamically typed programming language known for its readability and ease of use. Ruby shares many similarities with Python, such as automatic memory management and object-oriented principles.

@Rafarafa has provided a word for word translation, even preserving the comments found in the provided Python code. Using the Ruby solver below is extremely similar to the Python examples found in the playground.

# Key Difference

My Python [`AlgorithmXSolver`](the-algorithmxsolver) makes extensive use of `tuple`s. Because Ruby does not have `tuple`s, you will use `array`s for requirements and actions. These `array`s will be used as keys in a `hash`, so take appropriate care to ensure the `array` elements never change.

Be sure to scan through @Rafarafa's other comments for information regarding other minor differences.

# Example - 9x9 Sudoku

```kotlin
class SudokuSolver(grid: List<CharArray>, values: String) :
            DLXSolver<Requirement, Action>(buildRequirements(grid, values), buildActions(grid, values)) {

    companion object {

        fun buildRequirements(grid: List<CharArray>, values: String): List<Requirement> {

            val requirements = mutableListOf<Requirement>()

            // build the requirements

            return requirements
        }

        fun buildActions(grid: List<CharArray>, values: String): Map<Action, List<Requirement>> {

            val actions = mutableMapOf<Action, List<Requirement>>()

            // build the actions Map

            return actions

        }
    }

    override fun processSolution(solution: List<Action>): Boolean {

        // Using the Actions in the solution, build a grid and print the solved Sudoku.

        return true    // Return true to stop looking for more solutions.
    }
}


fun main(args : Array<String>) {
    val solver = SudokuSolver(List(9) { readln().toCharArray() }, ALL_VALUES)
    solver.solve()
}
```

# The Solver Code

