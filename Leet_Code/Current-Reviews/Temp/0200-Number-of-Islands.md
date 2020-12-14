# 200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

---

(1) DFS or BFS.

We may use either DFS or BFS to traverse through the given grid of maps and
mark the islands.

In either cases, time complexity would be O(m * n) as we only have to iterate
once on each of the cells and O(min(m, n)) in space complexity as we are only
looking at 4 neighbours at a time.

(2) Union-Find (Finding number of connected components).

Anoter method that has same time complexity but slightly worse space complexity
of O(m * n) would be using union-find structure. For every cell, it has
a connection or forms an edge to its neighbouring cells iff they are '1'. So,
initially, there would be as much islands as '1's. Then, as we iterate forward,
for each land cell that we discover, we check its neighbours to see if they are
connected. If so, then we can update their union-find structure; if their
parent values are not equal, our count decreases and parent values are fixed.

---

Python: BFS approach.

```python

from collections import deque

class Solution200:

    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0

        m, n, total = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    total += 1
                    grid[i][j] = '0'

                    queue = deque([(i,j)])

                    while queue:
                        x, y = queue.popleft()
                        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                queue.append((nx,ny))
        
        return total
```

Python: DFS approach.

```python

class Solution200:

    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0

        def helper(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == '1'):
                return
            grid[i][j] = '0'
            helper(i+1, j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i, j-1)

        m, n, total = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    total += 1
                    dfs(i, j)

        return total
```

Python: Union-Find approach.

```python

class Solution200:

    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] == '1' for i in range(m) for j in range(n))
        union = [i for i in range(m * n)]
        
        # collapse node's path
        def unionFind(node):
            while node != union[node]:
                union[node] = union[union[node]]
                node = union[node]
            return node
        
        # check parents and update if not equal
        # if not equal, then connections has been formed; total count decreases
        def join(x, y):
            nonlocal total
            parentX, parentY = unionFind(x), unionFind(y)
            if parentX != parentY:
                total -= 1
                union[parentX] = parentY


        for i in range(m):
            for j in range(n):

                if grid[i][j] == '0':
                    continue
                
                # convert to 1-D
                curr = i * n + y
                # only has to check right and down; prev row and col has been
                # explored and their union structure is updated
                if i < m - 1 and grid[i+1][j] == '1':
                    join(curr, curr + n)
                if j < n - 1 and grid[i][j+1] == '1':
                    join(curr, curr + 1)

        return total
```

