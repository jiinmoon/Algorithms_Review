# 200 Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

---

Treat this problem as a graph problem - starting from each of the land cell,
explore as far as possible, marking it non-land.

---

Python:

```python

class Solution:
    def numberIslands(self, grid):
        def helper(i, j):
            grid[i][j] = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                    helper(ni,nj)

        if not grid or not grid[0]:
            return 0

        m, n, total = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += 1
                    helper(i, j)

        return total
```
