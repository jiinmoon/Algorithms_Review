# 694. Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as
another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

---

Visit each islands with either bfs or dfs; collect each of the visited coords
relative to its starting position and hash it. The result should be the total
number of theses islands found this way.

Time complexity should be O(v + e).

---

Python:

```python

class Solution694:

    def numDistinctIslands(self, grid):

        def helper(i, j, x, y):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return
            grid[i][j] = 0
            relIslands.append(((i - x) * 15 + j - y) * 31)
            helper(i+1, j, x, y)
            helper(i-1, j, x, y)
            helper(i, j+1, x, y)
            helper(i, j-1, x, y)
        
        if not grid or not grid[]:
            return 0

        m, n, result = len(grid), len(grid), set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    relIslands = list()
                    helper(i, j, i, j)
                    result.add(tuple(relIslands))

        return len(result)
```

