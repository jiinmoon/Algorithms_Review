62 Unique Paths
===============

Question:
---------

Find all possible paths that a robot can take to move from top-left corner of
a m x n grid to bottom-right corner.

Solutions:
----------

This problem can be seen as a combinatory problem; a robot has two options to
choose at each cell and there are (m+n-1) chocies to make.

Another approach is to use the dynamic programming - we define DP[i][j] as
a maximum number of paths that robot has taken thus far. Then, this must be
based on previous values DP[i-1][j] and DP[i][j-1] where the robot has came
from. This would take O(n * m) to iterate on the grid.

```
any pseudocodes will live here
```

Codes:
------

Python:

```python
class Solution:
    def uniquePaths(self, m, n):
        dp = [ [1] * n for _ in range(m) ]
        # first row and col has to be 1 since only a single path.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

---

**Source:**

LeetCode: [Unique-Paths](https://leetcode.com/problems/unique-paths)
