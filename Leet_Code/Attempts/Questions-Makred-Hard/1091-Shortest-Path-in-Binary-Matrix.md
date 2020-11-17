# 1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is
composed of cells C\_1, C\_2, ..., C\_k such that:

```
Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are
different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
```

Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

There are many approaches to finding the length of the shortest path if we are
to examine this problem as a graph one. Think of starting node as origin
position at (0, 0) and we are trying to navigate to the end (m-1, n-1) on
m x n matrix.

There are several algorithms such as BFS or heuristic approach involving heap
and distance formula. One that can gurantee the shortest path would be BFS; in
particular, here, we can use the bidirectional bfs that spans from front and
back - where each path starts from origin and the goal. As we expand out, we
check for overlap in both.

Using bidirectional BFS, we may avoid worst case of exploring only on the path
where branching factor is severe. In short, the time complexity should be O(m
\* n) as we do not have to revisit - also, O(m \* n) in space as well to
maintain our two frontiers and visited set.

---

Python:

```python

class Solution:
    def shortestPath(self, matrix):
        # start or goal is blocked
        if not matrix or not matrix[0] or matrix[0][0] or matrix[-1][-1]:
            return -1

        m, n, result = len(matrix), len(matrix[0]), 1
        front, back, visited = {(0,0)}, {(m-1,n-1)}, {}

        while front and back:
            if front & back:
                return result
            if len(front) > len(back):
                front, back = back, front

            newFront = set()
            for i, j in front:
                visited.add((i,j))
                for ni, nj in [(i+x,j+y) for x in (-1,0,1) for y in (-1,0,1)]:
                    if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in visited and not matrix[ni][nj]:
                        newFront.add((ni,nj))

            front = newFront
            result += 1

        return -1
```

