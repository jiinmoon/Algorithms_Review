# 1504. Count Submatrices With All Ones

Given a rows * columns matrix mat of ones and zeros, return how many
submatrices have all ones.

---

This questions is similar to previous question where we only needed to count
the squares; but here, any rectangle dimensions are valid.

However, despite this, we can still use similar approach. Here, we use dynammic
programming to maintain the maximum number of rectangles found thus far at each
row. dp[j] will be the total number of rectangles found downwards. This takes
care of vertically expanding rectangles. For horizontal rectangles, we expand
out as far out as possible while counting.

For example, suppose we have a matrix as follows:

1 0 0
1 1 0
1 1 1
1 1 1

Then, our dp would be a single dimensional dp array that tracks the rectangles
downwards thus far row after another.

dp after row 1 : [ 1 0 0 ]
dp after row 2 : [ 2 1 0 ]
dp after row 3 : [ 3 2 1 ]
dp after row 4 : [ 4 3 2 ]

Hence, we add up all the vertical rectangle values that we can find. Then, at
each row, lowest count tells the amount of horizontally expanded rectangles
that also spans from previous rows.

This would be O(m * n^2) in time complexity - for each row, will have to
iterate on row for row. dp will take up O(n) in time complexity.

---

Python:

```python

class Solution:
    def numSubmat(self, mat):
        if not mat or not mat[0]:
            return -1

        m, n, result = len(mat), len(mat[0]), 0
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                # if curr cell is empty, break the continuity
                if not mat[i][j]:
                    dp[j] = 0
                else:
                    # update rectangle vertically
                    dp[j] += 1
                    minHoriCount = dp[j]
                    # iterate as far out possible to count horizontal
                    for k in range(j-1, -1, -1):
                        if not mat[i][k]: break
                        # dp[j] also tells prev hori rectangle extended
                        minHoriCount = min(minHoriCount, dp[j])
                        result += minHoriCount
                    result += dp[j]
        
        return result
```
