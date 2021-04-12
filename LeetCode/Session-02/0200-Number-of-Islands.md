# 200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

---

We can count the number of islands on the given grid by performing either DFS
or BFS to expand as far out as possible, exploring into four directions so long
as it is marked as a land tile.

Similarly, we may also approach this problem as a graph problem where we are to
find the number of connected components - which we can solve using Union-Find
structure.

---

Python: DFS approach.

```python

class Solution200:

    def numIslands(self, grid):

        if not (grid and grid[0]):
            return 0

        m, n = len(grid), len(grid[0])
        result = 0

        def explore(i, j):
            grid[i][j] = None
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                    explore(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    explore(i, j)

        return result
```

Python: Union-Find approach.

```python

class Solution200:

    def numIslands(self, grid):

        if not (grid and grid[0]):
            return 0

        m, n = len(grid), len(grid[0])
        # potential number of total islands
        total = sum(grid[i][j] == '1' for i in range(m) for j in range(n))
        # map 2-D grid unto 1-D array
        union = [i for i in range(m * n)]

        def unionFind(node):
            while node != union[node]:
                union[node] = union[union[node]]
                node = union[node]
            return node
        
        def join(i, j):
            nonlocal total
            a, b = unionFind(i), unionFind(j)
            if a != b:
                union[a] = b
                total -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                curr = i * n + j
                if j < n - 1 and grid[i][j+1] == '1':
                    join(curr, curr + 1)
                if i < m - 1 and grid[i+1][j] == '1':
                    join(curr, curr + n)

        return total
```
