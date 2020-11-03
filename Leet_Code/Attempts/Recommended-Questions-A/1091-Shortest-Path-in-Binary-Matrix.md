# 1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is
composed of cells C\_1, C\_2, ..., C\_k such that:

Adjacent cells C\_i and C\_{i+1} are connected 8-directionally (ie., they are
different and share an edge or corner)
C\_1 is at location (0, 0) (ie. has value grid[0][0])
C\_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C\_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

This problem can be visualized as a graph problem where are to find the
shortest path from the start (0,0) to the goal (n-1,n-1). For this we can use
BFS algorithm. In particular, bidirectional BFS can be used here to better
reduce the time complexity where the depth to explore will be reduced by half
as well as avoiding exploring on the path that has the worst branching factor.

---

Python:

```python

class Solution:
    def findShorestPath(self, matrix):
        # matrix does not exist or start/goal is blocked
        if not matrix or matirx[0][0] or matrix[-1][-1]:
            return -1

        n = len(matrix)
        f, b, visited = {(0,0)}, {(n-1,n-1)}, {}
        length = 1
        while f and b:
            if f & b:
                return length

            if len(f) > len(b):
                f, b = b, f

            newf = set()
            for i, j in f:
                visited.add((i,j))
                # 8 directions to explore
                for ni, nj in [(i+x, j+y) for x in (-1,0,1) for y in (-1,0,1)]:
                    if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj] and not (ni,nj) in visited:
                        newf.add((ni,nj))

            f = newf
            length += 1
        
        return -1
```
