# 1091 Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is
composed of cells C\_1, C\_2, ..., C\_k such that:

Adjacent cells C\_i and C\_{i+1} are connected 8-directionally (ie., they are
different and share an edge or corner)
C\_1 is at location (0, 0) (ie. has value grid[0][0])
C\_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C\_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

Finding the shortest path can be achieved by either astar (heuristic approach)
or BFS. Here, we use bidirectional bfs to see whether we can reach from start
(0,0) to the end of the grid (n-1, n-1).

---

Python:

```python

class Solution:
    def shortestPath(self, grid):
        # if starting or ending cell is blocked, cannot complete
        if not grid or not grid[0] or grid[0][0] or grid[-1][-1]:
            return -1

        N = len(grid)
        f, b = {(0,0)}, {(n-1,n-1)}
        visited = set()
        total = 1

        while f and b:
            if f & b:
                return total

            newf = set()
            for i, j in f:
                visited.add((i,j))
                # 8 directions
                for ni, nj in [(i+x, j+y) for x in (-1,0,1) for y in (-1,0,1)]:
                    if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj]:
                        newf.add((ni,nj))

            f = newf - visited
            length += 1

            if len(f) > len(b):
                f, b = b, f
        
        return -1
```
