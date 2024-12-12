# Three Little Piggies

__Puzzle:__ [Three Little Piggies](https://www.codingame.com/training/hard/three-little-piggies)

__Author:__ [@nicola](https://www.codingame.com/profile/21bf42f790de293c3aef398f18cd2627479878)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Pigs In Houses? Day? Night? Lots of Options Create Complexity

# Strategy

Three Little Piggies is likely to get you going in circles and wondering why you seem to be right back where you started. The situation is different at night than during the day. Houses can be rotated any number of times. This probably doesn’t help, but the key to success is to keep it simple.

# Requirements

The three main requirements of the puzzle are that each of the three houses be placed on the gameboard. If it is nighttime, it is also required that all pig locations on the gameboard be covered. Additionally, all `X` locations on the gameboard may be covered by a house, but if they are covered by a house, they can only be covered by one house. Easy enough right? The actions are not quite so straightforward.

# Enumerating the Actions

It is time to once again use what you learned in Shikaku Skill Builder. Unfortunately, building an exhaustive list of locations you could place each house is no easy task. Here are the key issues you need to work around:

* A house cannot cover any tree location on the gameboard.
  
* If it is daytime, a house cannot cover a pig location.

* If it is nighttime:
  
    * A house cannot cover the wolf’s location
    
    * Each pig location must be covered by a house and the pig must be in the proper location of the house.

Setting Algorithm X up for success comes down to generating an exhaustive list of every possible location a house could be placed on the gameboard in such a way that all rules are obeyed. Of course, that includes all rotations of the house. 

This puzzle is another great fit for Algorithm X, but setting up the matrix will take some time and a lot of attention to detail.

# Rotating a 2-Dimensional Array

I first learned how to rotate a 2-dimensional array by looking at another CodinGamer’s code on another puzzle. I can’t say enough about what can be learned by looking at other solutions after submitting your own. Let’s look at rotating the brick house.

```python runnable
# store the brick house as a 2-dimensional array
house = [['H', 'B', 'B'], [' ', ' ', 'B']]

# print the house and rotate it 4 times
for i in range(4):
    print(f'Rotation: {i}')
    for line in house:
        print(*line, sep='')
    print()

    # rotate the house 90 degrees to the right
    house = list(zip(*house))
    house = [line[::-1] for line in house]
```

<BR>

Keep in mind the brick house does not have equal height and width, and each time the house rotates, the height and width of the house change. You will need to be aware of that when you look to see if the house will fit on the grid.

Have you played around with Numpy Arrays? Many puzzles that involve 2-dimensional grids are great places to experiment with Numpy and learn how to use Arrays. This next code block rotates the brick house 4 times just like the code block above, but using Numpy. Unfortunately, I cannot import numpy into a runnable code block in this playground, but I am sure you get the idea.

```python
import numpy as np

# store the brick house as a 2-dimensional numpy array
house = np.array([['H', 'B', 'B'], [' ', ' ', 'B']])

# print the house and rotate it 4 times
for i in range(4):
    print(f'Rotation: {i}')
    for line in house:
        print(*line, sep='')
    print()

    # rotate the house 90 degrees to the left
    house = np.rot90(house)
```
