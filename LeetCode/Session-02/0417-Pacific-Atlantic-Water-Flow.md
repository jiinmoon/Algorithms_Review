# 417. Pacific Atlantic Water Flow

You are given an m x n integer matrix heights representing the height of each
unit cell in a continent. The Pacific ocean touches the continent's left and
top edges, and the Atlantic ocean touches the continent's right and bottom
edges.

Water can only flow in four directions: up, down, left, and right. Water flows
from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and
Atlantic oceans.

---

We can perform traversal algorithm from each end of the ocean, recording the
coordinates that we visit. In the end, we would have two set of visited nodes
that have started from each ocean floor. Thus, we can use set operation to
check for intersection of the two coordinates.

---

Python:

```python

class Solution417:

    def pacificAtlantic(self, matrix):

        if not (matrix and matrix[0]):
            return []

        m, n = len(matrix), len(matrix[0])
        
        # set of visited coordinates in tuple (i, j)
        pacific, atlantic = set(), set()
        
        # initialize starting points
        for row in range(m):
            pacific.add( (row, 0) )
            atlantic.add( (row, n-1) )

        for col in range(n):
            pacific.add( (0, col) )
            atlantic.add( (m-1, col) )

        # explore as far out as possible
        for ocean in [pacific, atlantic]:
            
            queue = ocean

            while queue:
                temp = set()
                for i, j in queue:
                    for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if not (0 <= ni < m and 0 <= nj < n and (ni,nj) not in ocean):
                            continue
                        if matrix[i][j] <= matrix[ni][nj]:
                            temp.add( (ni, nj) )
            
            ocean |= temp
            queue = temp
        
        # use set intersection to find overlap
        return list(pacific & atlantic)
```
