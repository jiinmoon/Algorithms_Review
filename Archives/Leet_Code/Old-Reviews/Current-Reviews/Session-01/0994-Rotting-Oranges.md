994 Rotting Oranges
===================

Given 2D grid, each cell is either 0 (empty), 1 (fresh), or 2 (rotten). After
each minute, rotten oranges consume its neighbouring fresh oranges - turning
them into another rotten oranges.

Find how many minutes pass to turn every fresh oranges into rotten. If it is
not possible, return -1.

---

We perform BFS - for every rotten cell, we discover new frontier to cover every
single fresh oranges to its neighbours. If no new frontier is found, but fresh
set still remains this indicates that we cannot complete the rotting process so
we should return -1. This process repeats until no more fresh set is left.

---

Python:

```python
class Orange:
    Fresh = 1
    Rotten = 2

class Solution:
    def rottingOranges(self, grid):
        m, n = len(grid), len(grid[0])
        fresh, rotten = set(), set()
        elapsed = 0

        # collect fresh/rotten
        for i in range(m):
            for j in range(n):
                if grid[i][j] == Orange.Fresh:
                    fresh.add( (i,j) )
                elif grid[i][j] == Orange.Rotten:
                    fresh.add( (i,j) )

        # perform BFS
        while fresh:
            newRotten = set()
            for x, y in rotten:
                for nextX, nextY in [ (x+1,y), (x-1,y), (x,y+1), (x,y-1) ]:
                    if (nextX, nextY) in fresh:
                        newRotten.add( (nextX, nextY) )
            if not newRotten:
                return -1
            fresh -= newRotten
            rotten = newRotten
            elapsed += 1

        return elapsed
```
