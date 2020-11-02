# 200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

---

We use DFS to explore from every land cell to cover as much island as possible.

---

Python:

```python

class Solution:
    def numberOfIslands(self, grid):
        def helper(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return
            grid[i][j] = 0
            helper(i+1, j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i, j-1)

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
