# 994 Rotting Oranges

Traverse on each fresh cell to expand out to rot all the cells.

---

Python:

```python

class Solution:
    def rottingOranges(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n, elapsed = len(grid), len(grid[0]), 0
        f, r = set(), set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    f.add((i,j))
                elif grid[i][j] == '2':
                    r.add((i,j))

        while f:
            newr = set()
            for i, j in r:
                for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (ni, nj) in f:
                        newr.add((ni,nj))

            if not newr:
                return -1

            elapsed += 1
            f -= newr
            r = newr

        return elapsed 
```
