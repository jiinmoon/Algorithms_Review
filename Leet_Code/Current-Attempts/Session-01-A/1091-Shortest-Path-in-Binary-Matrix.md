# 1091 Shortest Path in Binary Matrix

Shortest path from start to goal can be found with BFS.

---

Python:

```python

class Solution:
    def shortestPath(self, grid):
        if not grid or not grid[0] or grid[0][0] or grid[-1][-1]:
            return -1

        n = len(grid)
        f, b = {(0,0)}, {(n-1,n-1)}
        length = 1

        while f:
            if f & b:
                return length

            newf = set()
            for i, j in f:
                grid[i][j] = 0
                for ni, nj in [(i+x, j+y for x in (-1,0,1) for y in (-1,0,1)]:
                    if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj]:
                        newf.add((ni,nj))

            f = newf
            length += 1

            if len(f) > len(b):
                f, b = b, f

        return -1
```
