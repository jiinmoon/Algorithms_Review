# 489. Robot Room Cleaner

Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
```

---

We use backtracking algorithm (DFS) to explore all rooms to clean; by default,
the robot cleans each of the room that it visits, and once the robot finishes
its exploration down the path, we restore the robots position to repeat on the
another.

---

Python:

```python

class Solution:
    def cleanRoom(self, robot):
        def helper(x, y, dx, dy):
            # robot cleans each room it visits
            robot.clean()
            # mark the room as visited so we do not visit again
            visited.add((x,y))
            # four directions to explore
            for _ in range(4):
                # alternate the up, down, left, right directions
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and robot.move():
                    helper(nx, ny, dx, dy)
                    # restore robot back to its original position
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                # turn to explore another direction
                robot.turnLeft()
                # swap the coords to explore
                dx, dy = -dy, dx

        visited = set()
        helper(0,0,0,1)
```
