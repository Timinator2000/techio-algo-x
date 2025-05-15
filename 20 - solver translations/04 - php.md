# PHP

__Translation Author:__ [@TBali](https://www.codingame.com/profile/08e6e13d9f7cad047d86ec4d10c777500155033)

PHP is a high-level, interpreted language primarily used for web development. Its deep integration with HTML makes it a popular choice for server-side scripting. While PHP supports many modern programming constructs, it lacks native support for tuples — structures that are frequently used in my Python-based `AlgorithmXSolver`, particularly as dictionary keys.

To address this, @TBali defines classes for both requirements and actions. Each instance of these classes includes a unique string stored in a `hash` attribute. In the PHP implementation of `AlgorithmXSolver`, these unique strings are used in place of Python's `tuple`s. This approach results in a smooth and intuitive user experience that closely mirrors the original Python logic.

# Abstract Requirements and Actions

The next code snippet shows the abstract classes for requirements and actions provided with the PHP `AlgorithmXSolver`. Each problem-specific implementation must define subclasses that extend these two classes.

```php
// --------------------------------------------------------------------
/**
 * A single requirement to be used in the solver.
 *
 * Actual puzzle requirement class shall extend this and set its `hash` property in its constructor.
 */
abstract class Requirement
{
    /**
     * @var string
     */
    protected $hash;

    public function hash(): string
    {
        return $this->hash;
    }
}

// --------------------------------------------------------------------
/**
 * A single action to be used in the solver.
 *
 * Actual puzzle requirement class shall extend this and set its `hash` property in its constructor.
 * Before passing list of actions to the solver, the `reqs` property must be filled with list of requirements.
 */
abstract class Action
{
    /** @var string */
    protected $hash;

    /**
     * The list of requirements that this action covers.
     *
     * @var array<int, Requirement>
     */
    public $reqs = [];

    public function hash(): string
    {
        return $this->hash;
    }
}
```

# Problem-Specific Requirements and Actions

To use @TBali’s PHP solver, you must first create subclasses for your problem-specific requirements and actions.  These subclasses must assign a string value to the inherited `hash` attribute. Consider 9x9 Sudoku, where there are four types of requirements:

In Sudoku, there are four fundamental types of requirements:

1. Every cell must contain exactly one value.
1. Each value must appear exactly once in every row.
1. Each value must appear exactly once in every column.
1. Each value must appear exactly once in every 3×3 box.

To represent these constraints, I define four separate classes — each corresponding to one of the above requirements — all inheriting from a generic `Requirement` base class.

Each subclass assigns a string to the inherited `hash` attribute. This string format is intentionally designed to resemble the tuple representations used in my Python-based implementation, preserving clarity and structure.

```php
class CellCovered extends Requirement
{
    /** @var int */
    public $row;
    /** @var int */
    public $col;

    public function __construct(int $row, int $col)
    {
        $this->row = $row;
        $this->col = $col;
        $this->hash = "cell covered $row $col";
    }
}


class ValueInBox extends Requirement
{
    /** @var int */
    public $box;
    /** @var string */
    public $val;

    public function __construct(int $box, string $val)
    {
        $this->box = $box;
        $this->val = $val;
        $this->hash = "value in box $box $val";
    }
}


class ValueInRow extends Requirement
{
    /** @var int */
    public $row;
    /** @var string */
    public $val;

    public function __construct(int $row, string $val)
    {
        $this->row = $row;
        $this->val = $val;
        $this->hash ="value in row $row $val";
    }
}


class ValueInCol extends Requirement
{
    /** @var int */
    public $col;
    /** @var string */
    public $val;

    public function __construct(int $col, string $val)
    {
        $this->col = $col;
        $this->val = $val;
        $this->hash = "value in col $col $val";
    }
}
```

Next, a problem-specific class must be declared that extends the abstract `Action` class.

```php
class PlaceValue extends Action
{
    /** @var int */
    public $row;
    /** @var int */
    public $col;
    /** @var string */
    public $val;

    public function __construct(int $row, int $col, string $val)
    {
        $this->row = $row;
        $this->col = $col;
        $this->val = $val;
        $this->hash = "place value $row $col $val";
    }
}
```

# Example - 9x9 Sudoku

```php
class SudokuSolver extends AlgorithmXSolver {

    public function __construct(array $grid, string $values) {

        $requirements = [];
        $actions = [];

        # Build the requirements and actions. Remember that the `req` attribute inherited
        # from the abstract class Action is a list that must contain all the requirements
        # covered by the action.

        parent::__construct($requirements, $actions);
   }
}

$solver = new SudokuSolver($sudoku, '123456789');

foreach ($solver->solve() as $solution) {
    foreach ($solution as $action) {

        # Use the attributes of the $action to build the solution:
        #      $action->row
        #      $action->col
        #      $action->val

    }
    break;
}

# print the solution
```

# Mutual Exclusivity


# Multiplicity


# The Solver Code

```php
```
