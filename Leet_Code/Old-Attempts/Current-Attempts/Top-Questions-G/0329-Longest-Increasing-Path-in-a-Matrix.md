# 329 Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or
down. You may NOT move diagonally or move outside of the boundary (i.e.
wrap-around is not allowed).

---

By treating this problem as a graph problem, this is about performing path
finding traversal where next neighbours are those with values greater than
previous one. Important point here is that we need to perform traversal on
every cell since we do not know which cell begins the longest path to the goal.
But we can use memoization to save the path lengths from each of the cells
since these are fixed value - once explored, it does not change as the values
must increase and there can only be one longest increasing path. So, this will
actually be O(m * n) in time complexity as opposed to squared.

---

Python:

```python

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):
        @lru_cache(None)
        def helper(i, j):
            longest = 1
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    longest = max(longest, 1 + helper(ni, nj))
            return longest

        m, n = len(matrix), len(matrix[0])
        longest = 0

        for i in range(m):
            for j in range(n):
                longest = max(longest, helper(i, j))

        return longest
```

