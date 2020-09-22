353 Design Snake Game
=====================

Design a Snake game that is played on a device with screen size = width
x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length
= 1 unit.

You are given a list of food's positions in row-column order. When a snake eats
the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will
not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear
on a block occupied by the snake.

---

We will maintain the list of food coords, position of nsake, position of snakes
head and tail. When we evaluate the move, we first update the head of the
snake to see where it has moved to next. The space where the snake moved to can
be (1) a wall or (2) its own body that is not its tail (which would have
moved).

If it survives these conditions, we can update its head and tail. But tail is
updated only if snake did not take the food since when snake gets the food, the
tail remains.

---

Python:

```python
class SnakeGame:
    def __init__(self, width, height, food):
        self.snakeHead, self.snakeTail = (0,0), (0,0)
        self.snakeBody = { (0,0) : None }
        self.w = width
        self.h = height
        self.foods = [ tuple(f) for f in food ]
        self.directionMap = {
            "U" : (-1, 0), "D" : (1, 0),
            "L" : (0, -1), "R" : (0, 1)
        }

    def move(self, direction):
        nextHead = (
            self.snakeHead[0] + self.directionMap[direction][0],
            self.snakeHead[1] + self.directionMap[direction][1]
        )
        # did snake collided with border?
        if nextHead[0] < 0 or nextHead[0] >= self.h \
                or nextHead[1] < 0 or nextHead[1] >= self.w:
            return -1 # game over

        # did snake collided with itself (excluding tail)
        if nextHead in self.snakeBody and nextHead != self.snakeTail:
            return -1 # game over
    
        # update body and head of snake
        self.snakeBody[self.snakeHead] = nextHead
        sefl.snakeHead = nextHead

        # food will appear sequentially
        # if snake did not eat food, update tail (it does not grow)
        if len(self.snakeBody) -1 >= len(self.foods) or \
            nextHead != self.foods[len(self.snakeBody)-1]:
            prevTail = self.snakeTail
            self.snakeTail = self.snakeBody[self.snakeTail]
            del self.snakeBody[prevTail]
        
        # add head to body for next checks
        self.snakeBody[self.snakeHead] = None
        return len(self.snakeBody)-1
```
