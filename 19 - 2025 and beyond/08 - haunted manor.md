# Haunted Manor

__Puzzle:__ [Haunted Manor](https://www.codingame.com/training/hard/haunted-manor)

__Author:__ [@CG-jupoulton](https://www.codingame.com/profile/d39436e9a23b5060ed3efaf1c24b4ba8929551)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ More Confusing than a [Svengoolie](https://www.metv.com/svengoolie/) Movie Marathon

# Strategy

Even in a world overrun by the undead, there’s still room for small moments of warmth —  quiet laughter over a meager meal, the comforting weight of a weapon held steady, the unspoken promise between survivors. In the midst of chaos, resilience isn’t just about fighting to stay alive, but finding reasons to keep going.

This puzzle will test your resilience! Before jumping into the code, I highly recommend playing the online version, [Undead from Simon Tatham’s Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/undead.html).

# Object Model

A powerful object model can get you started in a good direction, and I invite you to compare this puzzle’s “grid” to the grid found in [High-Rise Buildings](high-rise-buildings). In the latter, I proposed that each `CityView` has a relationship with `N` `Building`s and each `Building` has a relationship with 4 `CityView`s. More generically, the relationship could have been identified as a many-to-many relationship. Each `CityView` groups together many `Building`s and each `Building` is part of many `CityView`s.

The same model can work for Haunted Manor. Let’s call the groups `Sightline`s and say that each `Sightline` groups together many `Cell`s and each `Cell` can be a member of many `Sightline`s. Just as was done in High-Rise Buildings, it is tempting to create the following object model.

{Object model without the junction table.}

Anytime we come across a many-to-many relationship, we might want to step back and consider what the relational database folks might do. Since relational databases don’t directly support many-to-many relationships, they are implemented using a _junction table_ (_bridge table_ or _associative table_). The _junction table_ contains foreign keys referencing both tables, and breaks the many-to-many relationship into two one-to-many relationships. In the next diagram, I have inserted a class called a `Visual` to act similar to a _junction table_ between the `Sightline` class and the `Cell` class. 

{Class diagram with the Visual class.}

In coding, we can often move forward without this third class, but not always. Adding this _junction_ class makes sense when each instance has its own interesting attributes. Each `Visual` represents an instance of one `Cell` showing up in one `Sightline`. Are there any important attributes associated with an instance of one `Cell` in a particular`Sightline`? Yes, there is! For each `Visual`, it is important to know if that `Visual` exists due to normal line of sight or due to reflected line of sight. In the following diagram, I have added a single Boolean attribute called `reflected`

{Class diagram with the new attribute.}

Our class diagram tells a different story now. Each `Cell` has a relationship with many `Visual`s, each `Sightline` has a relationship with many `Visual`s, and each `Visual` has a relationship with exactly one `Cell` and exactly one `Sightline`. And the best part is that each `Visual` knows if it exists due to normal line of sight or reflected line of sight.

Consider what is possible with this new class diagram. I can try putting a Vampire in an empty `Cell`. For each `Visual` associated with that `Cell`, I need to know if that `Visual` exists due to normal line of sight or reflected line of sight. If the `reflected` attribute is `True`, the Vampire does not count as being seen in the `Sightline` because Vampires do not have reflections. However, if the `reflected` attribute is `False`, the Vampire does count as being seen the `Sightline`.

# Object Modeling Gurus

