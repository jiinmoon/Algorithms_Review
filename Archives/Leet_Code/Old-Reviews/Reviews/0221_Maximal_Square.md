221 Maximal Square
==================

Question:
---------

Given a 2-D binary matrix, find the largest square containing only 1s and
return its area.

Solutions:
----------

We can use dynamic programming - let's suppose that the DP represents maximal
length of the square thus far. The way that we can tell whether the
matrix[i][j] is part of a square is by checking whether matrix[i-1][j-1] first,
then check to its left and above. Since we are iterating this row after row,
all we require is to maintain a current dp row, and reference the left value by
storing previous.

Codes:
------

Python:

```python
class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        maxThusFar = 0
        dp = [0] * (n+1)
        prev = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1]:
                    # length of the square
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxThusFar = max(maxThusFar, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxThusFar ** 2 
```

---

**Source:**

LeetCode: [Maximal-Square](https://leetcode.com/problems/maximal-square/)
