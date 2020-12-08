# 221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

---

#### (1). Dynammic Programming 2-D array.

We can define our DP as follows:

    Let DP[i][j] be maximal side of the square upto including grid[i][j]. Then,
    we have following cases:

    (1) Current cell can extend the square.

    We can check for whether current cell is an extension from the previous
    square by checking for previous cell at grid[i-1][j-1]. Then, current
    square side depend upon three previous values at dp[i-1][j], dp[i][j-1],
    dp[i][j].

    (2) Current cell cannot extend the square.

    In this case, current maximal side should be set to 0.

In this approach, O(m * n) in time complexity to iterate on the given grid and
O(m * n) in space complexity to prepare a 2-D array for DP.

#### (2). Dynammic Programming 1-D array.

Improvement can be made further in terms of space as we can compute our dp row
after row - if so, then only value that we would be missing is the dp[i][j-1]
which will be overwritten. So, we save this value before we possibly update our
dp. In short, dp[j] is dp[i-1][j], dp[j-1] is dp[i][j-1]. By doing so, we can
reduce space complexity down to O(n).

---

Python: DP 1-D array.

```python

class Solution221:

    def maximalSquare(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n, maxSide = len(matrix), len(matrix[0]), 0

        dp = [0] * (n + 1)
        prev = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if grid[i-1][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    maxSide = max(maxSide, dp[j])
                else:
                    dp[j] = 0
                prev = dp[j]

        return maxSide ** 2
```
