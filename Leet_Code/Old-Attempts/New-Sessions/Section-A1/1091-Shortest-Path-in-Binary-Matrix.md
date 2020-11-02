# 1091 Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

BFS algorithm can be used to find the shortest path between (0, 0) to (n-1,
n-1) cell. The important point here is that we need to consider 7 paths
including the diagonal paths.

---

Python:

```python

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if not grid or not grid[0] or grid[0][0] or grid[-1][-1]:
            return -1

        n = len(grid)
        f, b, visited = { (0,0) }, { (n-1,n-1) }, {}
        length = 1

        while f and b:
            if f & b:
                return length

            if len(f) > len(b):
                f, b = b, f

            newf = set()
            for i, j in f:
                visited.add( (i,j) )
                candidates = [(i+x, j+y) for x in (-1,0,1) for y in (-1,0,1)]
                for ni, nj in candidates:
                    if 0 <= ni < m and 0 <= nj < n and not grid[ni][nj] and (ni, nj) not in visited:
                        newf.add( (ni,nj) )
            f = newf
            length += 1

        return -1
```

