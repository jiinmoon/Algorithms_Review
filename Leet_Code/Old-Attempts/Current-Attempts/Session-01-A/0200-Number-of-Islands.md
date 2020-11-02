# 200 Number of Islands

Basic path finding algorithm can be used - starting from every land cell, mark
the cell off as far out as possible to denote that island has been accounted
for. Algorithm can complete in O(m + n).

---

Python:

```python

class Solution:
    def numberIslands(self, grid):
        def explore(i, j):
            grid[i][j] = 0
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                    explore(ni, nj)

        if not grid or not grid[0]:
            return 0

        m, n, total = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += 1
                    explore(i, j)

        return total
```
