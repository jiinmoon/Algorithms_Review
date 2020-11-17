# 221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

---

Best approach to this problem is a dynamic programming where we compute the
longest side of the square at each cells (subproblems). And amongst these
solution to the subproblems, we choose the maximum.

While 2-dimensional array appears to be necessary, we can reduce the space
requirement down to O(n) as we are iterating on this matrix row after another.
And only value that we are required to maintain is the previous columns value.

We can determine that at any given cell (i,j) is a "potential" square by
checking against the given matrix's cell at (i-1, j-1). Then, to determine the
extended square side length, this would be minimum of three neighbours cells
which is from (i-1,j-1), (i,j-1), (i-1, j); however, as we stated before, we do
not need to maintain entire information, just the previous column's value.

Hence, the time complexity of this algorithm is O(m * n) whilst the space
compleixty should be O(m).

---

Python:

```python

class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return -1

        m, n, maxSide = len(matrix), len(matrix[0]), 0
        dp = [0] * (n + 1)
        prev = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1]:
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxSide = max(maxSide, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return maxSide ** 2
```
