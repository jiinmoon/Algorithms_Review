# 994 Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

---

We can approach this problem as a graph problem; using BFS, we explore from
each of the rotten cells onto the adjacent fresh cells.

---

Python:

```python

class Solution:
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n, elapsed = len(grid), len(grid[0]), 0
        f, r = set(), set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    f.add( (i,j) )
                elif grid[i][j] == 2:
                    r.add( (i,j) )

        while f:
            elapsed += 1
            newR = set()
            for i, j in r:
                for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if ni, nj in f:
                        newR.add( (ni,nj) )
            if not newR:
                return -1
            r = newR
            f -= newR

        return elapsed
```
