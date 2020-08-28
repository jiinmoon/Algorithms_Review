329 Longest Increasing Path in a Matrix
=======================================

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or
down. You may NOT move diagonally or move outside of the boundary (i.e.
wrap-around is not allowed).

---

We can perform DFS on each cell to discover how far we can move. But since the
work is duplicated - when we visit another cell that we have seen previously
from another path - we can use memoization to avoid having to traverse
repeatedly.

So, the algorithm can run in O(m + n) time complexity.

---

Python: Memoization + DFS.

```python

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]
            longestThisPath = 0
            for nextX, nextY in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0 <= nextX < m and 0 <= nextY < n and matrix[x][y] < matrix[nextX][nextY]:
                    longestThisPath = max(longestThisPath, dfs(nextX, nextY))
            memo[x][y] = longestThisPath
            return longestThisPath

        longestThusFar = 0
        for i in range(m):
            for j in range(n):
                longestThusFar = max(longestThusFar, dfs(i, j))

        return longestThusFar
```
