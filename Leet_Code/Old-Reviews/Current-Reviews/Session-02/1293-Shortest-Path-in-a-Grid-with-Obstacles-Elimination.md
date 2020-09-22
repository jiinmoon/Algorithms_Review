1293 Shortest Path in a Grid with Obstacles Elimination
=======================================================

Given a m * n grid, where each cell is either 0 or 1, and you may move in four
directions from and to an empty cell; return the min number of steps fo walk
from the upperleft corner to the lower right corner given that you can
eliminate at most k obstacles. Return -1 if impossible.

---

We can perform a graph traversal from start to the goal; but since we are
finding the shortest path, we may apply Astar search - in this case, we may use
the Manhanttan Distance which is the sum of absolute difference from curren cells to the target cell. By using prioirity queue, we can repeatedly pick the next cell that gets us closer to the goal.

The problem here is dealing with the obstacles. In this case, we can simply
carry the obstacle value K with us and repeatedly taking the value of the cell
(either 0 or 1). If the value goes below 0 then we know that we have used up
too much values, and this path that we are on is not a valid one.

---

Python:

```python
improt heapq

class SolutioN:
    def shortestPath(self, grid, K):
        if not grid or not grid[0]:
            return -1

        # manhattan distance
        # abs sum of cartesian coord difference in x and y
        # from (i, j) to goal (m-1, n-1)
        def astar(i, j):
            return abs(m-i-1) + abs(n-j-1)

        m, n = len(grid), len(grid[0])
        
        # heuristic value, elim count, moves taken, curr coord
        q = [ (astar(0,0), -k + grid[0][0], 0, (0,0)) ]

        # cell : elims remaining
        visited = dict()

        while q:
            _, elimCount, movesTaken, currCell = heappop(q)
            if elimCount > 0:
                continue
            if currCell == (m-1, n-1):
                return movesTaken
            movesTaken += 1
            # cell was visited before and used more elimCount
            if currCell in visited and elimCount >= visited[currCell]:
                continue

            visited[currCell] = elimCount

            i, j = currCell
            for nextI, nextJ in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= nextI < m and 0 <= nextJ < n:
                    heappush(
                        q, 
                        [ (
                            astar(nextI,nextJ)+movesTaken,
                            elimCount,
                            movesTaken,
                            (nextI,nextJ))
                        ]
                    )
        return -1
```
