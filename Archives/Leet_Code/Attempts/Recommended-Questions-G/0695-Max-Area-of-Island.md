# 695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no
island, the maximum area is 0.)

---

Simply perform dfs traversal on each grid that is marked as a land - and
explore as far out as possible while recording how much land is being occupied;
to avoid revisiting the same cell, mark it off. The time complexity should be
O(m * n).

---

Python:

```python

class Solution:
    def maxArea(self, grid):
        def helper(i, j):
            grid[i][j] = 0
            result = 1
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                    result += helper(ni, nj)
            return result

        if not grid or not grid[0]:
            return -1

        m, n, result = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                result = max(result, helper(i, j))

        return result
```
