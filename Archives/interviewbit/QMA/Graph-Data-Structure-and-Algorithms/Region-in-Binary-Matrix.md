# Region in Binary Matrix

Given a binary matrix A of size N x M.

Cells which contain 1 are called filled cell and cell that contain 0 are called
empty cell.

Two cells are said to be connected if they are adjacent to each other
horizontally, vertically, or diagonally.

If one or more filled cells are also connected, they form a region. Find the
length of the largest region.

---

Use either dfs or bfs to traverse as far out as possible, discovering all the
regions with 1s. Mark each visited so that we do not revisit them.

O(n * m) in time complexity and O(m + n) in space since queue never grows
beyond the limits of its neighbours.

---

Python: BFS.

```python

from collections import deque

class Solution:

    def countMaxRegion(self, A):

        m, n, result = len(A), len(A[0]), 0

        def bfs(i, j):
            queue, count = deque([(i,j)]), 0
            A[i][j] = 0
            while queue:
                i, j = queue.popleft()
                count += 1
                for ni, nj in [(i+dx,j+dy) for dx in (-1,0,1) for dy in (-1,0,1)]:
                    if ni == i and nj == j:
                        continue
                    if 0 <= ni < m and 0 <= nj < n and A[ni][nj]:
                        A[ni][nj] = 0
                        queue.append((ni,nj))


        for i in range(m):
            for j in range(n):
                if not A[i][j]:
                    continue
                result = max(result, bfs(i, j))

        return result
```
