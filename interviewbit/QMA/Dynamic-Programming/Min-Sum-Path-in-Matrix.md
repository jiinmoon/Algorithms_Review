# Min Sum Path in Matrix

Given a 2D integer array A of size M x N, you need to find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

NOTE: You can only move either down or right at any point in time.

---

Approach this problem as a dp problem where dp[i][j] is the min path sum thus
far to reach cell at (i, j). Then, dp[i][j] = grid[i][j] + min(dp[i-1][j],
dp[i][j-1]). Since the previous information is available to us, we can perform
this in-place.

O(m * n) in time complexity and O(1) in space.

---

Python:

```python

class Solution:

    def minPathSum(self, A):

        m, n = len(A), len(A[0])
        
        # initalize first row and col; singluar path to right and down
        for i in range(1, m):
            A[i][0] += A[i-1][0]

        for i in range(1, n):
            A[0][i] += A[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                A[i][j] += min(A[i-1][j], A[i][j-1])

        return A[-1][-1]

``
