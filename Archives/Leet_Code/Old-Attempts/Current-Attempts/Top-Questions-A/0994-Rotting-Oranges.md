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

In essence, this is a graph problem, where we expand out from each rotten cell
to consume the neighbouring fresh cells on each step while counting the steps
taken. This is done by first identifying all the rotten cells and fresh cells.
And for each rotten cells, we expand out to fresh cells. The time complexity
should be O(V + E).

---

Python:

```python

class Solution:
    def rottingOragnes(self, grid):
        if not grid or not grid[0]:
            return -1

        elapsed, m, n = 1, len(grid), len(grid[0])
        f, r = set(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    f.add((i,j))
                elif grid[i][j] == 2:
                    r.add((i,j))

        while f:
            newr = set()
            for i, j in r:
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if (ni,nj) in f:
                        newr.add((ni,nj))

            if not newr:
                return -1

            f -= newr
            r = newr
            elapsed += 1

        return elapsed
```

