694 Number of Distinct Islands
==============================

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as
another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

---

We perform BFS on each cell that is a land and explore as far as possible while
marking each visited cell. Since we need to count the distinct islands, we
collect the naturally ordered (as visiting neighbours is a uniform operations
in BFS) tuple of "relative" coordinates of the islands.

---

Python:

```python
class Solution:
    def numDistinctIslands(self, grid):
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        islands = set()

        def isValid(i, j):
            return 0 <= i and i < m and 0 <= j and j < n

        def BFS(i, j):
            # collect the relative coordinates based on given (i, j)
            q = [ (0,0) ]
            for ri, rj in q:
                # neighbour cells to 4 directions
                for ni, nj = [ (ri+i+1, rj+j), (ri+i-1, rj+j), (ri+i, rj+j+1), (ri+i, rj+j-1)]:
                    if not (isValid(ni, nj) and grid[ni][nj]):
                       # mark visited
                       grid[ni][nj] = 0
                       # add only relative coords to next itr
                       q.append( (ni-i, nj-j) )
            # freeze and return relative coords of current island explored
            return tuple(q)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    islands.add(BFS(i,j))

        return len(islands)
```
