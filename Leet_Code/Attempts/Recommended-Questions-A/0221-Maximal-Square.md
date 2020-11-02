# 221. Maximual Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

---

To determine the largest square containing only the 1s, we first visualize this
as a dynamic programming one; we iterate to in find the maximum square side at
each of the points.

---

Python:

```python

class Solution:
    def maximalSquare(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [0] * (n + 1)
        maxSideThusFar = 0
        prev = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                # is current cell an extension of previous square?
                if grid[i-1][j-1]:
                    # potentially so, update maxSideThusFar
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxSideThusFar = max(maxSideThusFar, dp[j])
                else:
                    # reset the square since broken
                    dp[j] = 0
                prev = temp

        return maxSideThusFar ** 2
```
