# 200 Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

---

We treat this problem as a graph traversal problem - that is, starting from
each "land" cell, we try to explore as far out as possible so long as the next
neighbour is also "land". We mark the visited "land" cells as non-land so that
we do not cycle back nor count it again. The time complexity should be of O(m
+ n).

---

Python:

```python

class Solution:
    def numberOfIslands(self, grid):
        def explore(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            grid[i][j] = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if grid[ni][nj]:
                    explore(ni, nj)

        if not grid or not grid[0]:
            return 0

        total = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    explore(i, j)
                    total += 1

        return total
```
