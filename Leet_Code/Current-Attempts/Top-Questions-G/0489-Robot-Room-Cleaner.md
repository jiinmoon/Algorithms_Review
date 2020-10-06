# 489 Robot Room Cleaner

Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right.
Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the
obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown
below.

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

Very simply, we think of this problem as a graph problem - and perform DFS
traversal to cover the cells.

The problem is the awkwardness of the robot's state - where it only moves
forward tne turns left and right. To resolve this, we create a record of
robot's state - the location of the robot and the direction it is in.

For each cell, robot will first clean. The current location will be added to
visited set such that it will not be visited again in subsequent calls
downwards.

At each cell, robot can move to four directions. For each of the directions, we
check whether robot can move and whether the cell has been visited previously.

If not, it is safe to visit the cell so we recursively call the function on
itself with new direction. For next call, we turn the robot (either left or
right, but consistently) and move and restore the turn. The difficulty lies in
figuring out the turning and updating next cells to visit. For this, we create
recursive helper function that maintain the location of current cell as well as
the current modifier for the next cell to visit (four directions on x and
y-axis). Then, at each cell, we expect the robot to turn left and fix the next
modifier to exaimne the next cells.

This will take linear time O(m * n) since we need to visit all the cells, but
it will only have to visit them once as we are maintaining the visited cells.

---

Python:

```python

class Solution:
    def cleanRoom(self, robot):
        def helper(x, y, dx, dy):
            robot.clean()
            visited.add(x, y)
            for _ in range(4):
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and robot.move():
                    helper(nx, ny, dx, dy)
                    # after exploration, restore position to previous
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                # turn to explore new direction
                robot.turnLeft()
                # explores all four sides
                # 0, 1 -> -1, 0 -> 0, -1 -> 1, 0
                dx, dy = -dy, dx

        visited = set()
        helper(0, 0, 0, 1)
```
