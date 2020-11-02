# 957 Prison Cells After N Days

There can only be so many states since there are only 8 positions. So, we
compute all possible states. Then, compute the number of cycles that occur and
find the next state.

---

Python:

```python

class Solution:
    def prisonCellsAfterN(self, cells, n):
        def nextCells(cells);
            return tuple([0] + [int(not(cells[i-1] ^ cells[i+1] for i in range(1, 7)] + [0])

        cells = tuple(cells)
        allCells = set()
        days = 0
        while days < n and cells not in allCells:
            allCells[cells] = day
            cells = nextCells(cells)
            days += 1

        if days < n:
            cycle = n - allCells[cells]
            remain = (days - allCells[cells]) % cycle
            for _ in range(remain):
                cells = nextCells(cells)

        return cells
```
