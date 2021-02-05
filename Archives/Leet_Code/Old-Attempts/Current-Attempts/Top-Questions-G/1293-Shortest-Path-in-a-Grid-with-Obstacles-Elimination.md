# 1293 Shortest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one
step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m-1, n-1) given that you can eliminate at most
k obstacles. If it is not possible to find such walk return -1.

---

To find the shortest path, we could perform either BFS or heuristic approach.
Here, we can use a heuristic approach from start (0,0) to (m-1,n-1) using the
manhattan distance. To able to update and retrieve the next best possible
neighbour to visit, we use heap to maintain the maximum manhattan distance.

Added problem is the obstacles - to deal with this, we simply update the
elimination count k along with all our states. Then check them as we visit each
cells, if the updated elimination count is invalid, we remove it.

---

Python:

```python

import heapq

class Solution:
    def shortestPath(self, grid, k):
        # shorter it is, closer we are to the goal
        def mandist(x, y):
            return (m - x - 1) + (n - y - 1)

        if not grid or not grid[0] or grid[0][0] or grid[-1][-1]:
            return -1

        m, n = len(grid), len(grid[0])
        # heap maintains
        # (heuristic-value, elimination count, moves, cell)
        pq = [(mandist(0,0), grid[0][0] - k, 0, (0,0))]
        # hashmap required to maintain the visited cells to its elimination
        # counts to check for whether it is valid (goes negative or not?)
        visited = dict()
        
        while pq:
            _, eCount, moves, cell = heappop(pq)
            if eCount > 0:
                continue
            if cell == (m-1, n-1):
                return moves
            if cell in visited and visited[cell] <= eCount:
                continue
            visited[cell] = eCount
            moves += 1
            x, y = cell
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    heappush(
                        pq, 
                        (mandist(nx,ny))+moves, eCount+grid[nx][ny], moves, (nx,ny))

        return -1
```
