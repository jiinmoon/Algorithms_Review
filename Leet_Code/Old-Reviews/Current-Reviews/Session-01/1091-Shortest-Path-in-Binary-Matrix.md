1091 Shortest Path in Binary Matrix
===================================

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is
composed of cells `C_1, C_2, ..., C_k `such that:

Adjacent cells `C_i` and `C_{i+1}` are connected 8-directionally (ie., they are
different and share an edge or corner)
`C_1` is at location (0, 0) (ie. has value grid[0][0])
`C_k` is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If `C_i` is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to
bottom-right.  If such a path does not exist, return -1.

---

This is basically finding the shortest path from start to goal - but avoiding
stepping into the blocked cells. This can be achived with BFS; in this case, we
can also utilize the bidirectional BFS to avoid the worst case where the one
direction has more span to neighbours to explore than another path.

This will be typical BFS algorithm with time complexity of O(mn) - n nodes for
m edges to visit.

---

Python:

```
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        if not N or grid[0][0] or grid[-1][-1]:
            return -1

        length = 0
        visited = set()
        f, b = { (0,0) }, { (N-1, N-1) }
        while f and b:
            length += 1
            if f & b:
                return length
            
            newf = set()
            for (i,j) in f:
                visited.add( (i,j) )
                candidates = [(i+x,j+y) for x in (-1,0,1) for y in (-1,0,1)]
                for (ni,nj) in candidates:
                    if 0 <= ni < N and 0 <= nj < N and \
                        not grid[ni][nj] and (ni,nj) not in visited:
                        newf.add( (ni,nj) )
            f = newf
        return -1
```

