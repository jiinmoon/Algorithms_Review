221 Maximal Square
==================

Given a 2D binary matrix filled with '0's and '1's, find the largest square
containing only '1's and return its area.

---

We can use the DP to compute the area - with DP, we maintain the maximum length
of a side of the square of any square ending at (i,j) by (1 + min(dp[i-1][j],
dp[i][j-1], dp[i][j]).

Notice that we do not have to maintain the 2D dp array at all - but all we need
is a prev and current rows of the DP. So, at each row, we compute the new dp
row based on prev.

---

Python:

```python
class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        maxSquareLength = 0
        m, n = len(matrix), len(matrix[0])
        prevDP = [0] * n

        for row in range(m):
            currDP = [1] + [0] * n
            for col in range(1, n):
                if matrix[row][col] == '1':
                    currDP[col] = 1 + min(currDP[col-1], prevDP[col], prevDP[col-1])
            maxSquareLength = max(maxSqaureLength, max(currDP))
            prevDP = currDP
        return maxSqaureLength ** 2
```

