# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to
bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

---

We can solve this problem using the dynammic programming which we can define
each of our cell condition as follows. For any given cell on the grid, the
minimum path sum that can reach here has to be dependent upon two previous
locations which we have moved from (which would be either from left or from
up). Hence, we can solve this in-place and O(m * n) in time complexity.

---

Python:

```python

class Solution64:

    def minPathSum(self, grid):

        if not (grid and grid[0]):
            return 0

        m, n = len(grid), len(grid[0])

        # initialize first row and column
        # there can only be a singular path on first row and column
        for row in range(1, m):
            grid[row][0] += grid[row-1][0]

        for col in range(1, n):
            grid[0][col] += grid[0][col-1]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])

        return grid[-1][-1]
```
