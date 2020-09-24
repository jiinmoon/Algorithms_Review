# 329 Longest Increasing Path in a Matrix

From each cell in the grid, traverse as far out as possible; since on each
cell, the longest path is determined we can use the memoization to store the
longest path for each that we have visited previously.

---

Python:

```python

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, grid):
        @lru_cache(None)
        def helper(i, j):
            length = 0
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] < grid[ni][nj]:
                    length = max(length, 1 + helper(ni, nj))
            return length
            
        if not grid or not grid[0]:
            return 0

        m, n, longest = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                longest = max(longest, helper(i,j))

        return longest
```
