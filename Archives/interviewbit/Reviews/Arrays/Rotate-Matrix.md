# Rotate Matrix

Rotate the given matrix by 90 degrees clock-wise.

---

Transpose and swap across the diagnoal lines.

```
1 2 3           7 8 9           7 4 1
4 5 6   -->     4 5 6   -->     8 5 2
7 8 9           1 2 3           9 6 3
```

---

Python:

```python

class Solution:

    def rotateMatrix(self, grid):

        if not (grid and not grid[0]):
            return grid

        grid.reverse()

        for i in range(len(grid)):
            for j in range(i, len(grid[0])):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        return grid
```
