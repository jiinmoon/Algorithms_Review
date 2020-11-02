# 200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

---

To find the number of islands present, we iterate on the given grid first.
Then, for each of the land ('1's) encountered, we perform DFS to explore out as
far out as possible, while marking the visited land such that we do not revisit
them. The time complexity of this algorithm would be of typical DFS O(v + e).

---

Python:

```python

class Solution:
    def numIslands(self, grid):
        # dfs to explore current land tiles as far as possible
        def explore(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return
            grid[i][j] = 0
            explore(i+1, j)
            explore(i-1, j)
            explore(i, j+1)
            explore(i, j-1)
            
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
