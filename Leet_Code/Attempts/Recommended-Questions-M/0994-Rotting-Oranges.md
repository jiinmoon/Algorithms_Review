# 994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

---

This problem can be visualized as a graph problem; first, we identify the set
of coordinates for fresh and rotten oranges. Then, starting from rotting cells,
we expand out as far out as possible. The algorithm is O(m * n) in time
complexity.

---

Python:

```python

class Solution:
    def rottingOranges(self, grid):
        if not grid or not grid[0]:
            return -1

        length = 1
        f, r = set(), set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    f.add((i,j))
                elif grid[i][j] == 2:
                    r.add((i,j))
        
        # explore until all fresh oranges are rotten
        while f:
            newr = set()
            for i, j in r:
                for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (ni,nj) in f:
                        newr.add((ni,nj))

            if not newr:
                return -1
            
            f -= newr
            r = newr
            length += 1

        return length
```
