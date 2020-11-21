# 221. Maximual Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

---

To determine the largest square containing only the 1s, we first visualize this
as a dynamic programming one; we iterate to in find the maximum square side at
each of the points. We can determine current cell is a potential part of square
by checking the cell at (i-1, j-1). If so, then we can update the current
square max side length by carrying over minimum of 3 coordinates
(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]). This may look like we
require a 2 dimensional array to maintain the DP. However, at each row, we only
require to look at the previous value of current columns (dp value from
previous row). Hence, we only require 1-D array.

The time complexity would be O(m * n) as we need to iterate on the matrix; the
space complexity would be O(n) for matrix m x n.

---

Java:

```java

class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) return 0;

        int m, n, prev, result, temp;
        m = matrix.length;
        n = matrix[0].length;
        prev = result = temp = 0;

        int[] dp = new int[n+1];

        for (int row = 1; row < m + 1; row++) {
            for (int col = 1; col < n + 1; col++) {
                temp = dp[j];   // save previous column value before update
                if (matrix[i][j] == '1') {
                    dp[j] = Math.min(Math.min(dp[j], dp[j-1]), prev) + 1;
                    result = Math.max(result, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }

        return (int) Math.pow(result, 2);
    }
}

```

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
                if grid[i-1][j-1] == '1':
                    # potentially so, update maxSideThusFar
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxSideThusFar = max(maxSideThusFar, dp[j])
                else:
                    # reset the square since broken
                    dp[j] = 0
                prev = temp

        return maxSideThusFar ** 2
```
