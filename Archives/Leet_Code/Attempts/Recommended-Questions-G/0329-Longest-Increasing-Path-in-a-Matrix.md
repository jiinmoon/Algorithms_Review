# 329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or
down. You may NOT move diagonally or move outside of the boundary (i.e.
wrap-around is not allowed).

---

Here, we can use a path finding algorithm on each of the cell to find the path
so long as it is in increasing order. Since at each cell, its path length is
fixed, we can use memoization to cache the result on each cell such that if we
revisit the cell, we can immediately retrieve its length without having to
explore again.

---

Python:

```python

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):
        @lru_cache(None)
        def helper(i, j):
            longest = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    longest = max(longest, 1 + helper(ni, nj))
            return longest

        if not matrix or not matrix[0]:
            return 0

        m, n, longest = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                longest = max(longest, helper(i, j))

        return longest
```
