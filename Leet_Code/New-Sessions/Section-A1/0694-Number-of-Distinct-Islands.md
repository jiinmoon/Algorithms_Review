# 694 Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as
another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

---

We can resolve the problem of counting the potentially identically shaped
islands by recording not the islands absolute coordinates, but we record the
"relative" coordinates from each starting islands.

---

Python:

```python

class Solution:
    def numDistinctIslands(self, grid):
        def helper(i, j):
            q = [ (0,0) ]
            for ri, rj in q:
                for ni, nj in [(i+ri+1,j+rj), (i+ri-1,j+rj), (i+ri,j+rj+1), (i+ri, j+rj-1)]:
                    if not (0 <= ni < m and 0 <= nj < n and grid[ni][nj]):
                        continue
                    # mark visited so we do not visit the same cell again
                    grid[ni][nj] = 0
                    # only record the relative distnace
                    q.append((ni-i,nj-j))
            # to add to queue, make the collection immutable
            return tuple(q)

        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        relativeIslands = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    helper(i,j)

        return len(q)
```
