# 957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the
following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant,
then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row
can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] ==
1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after
N days (and N such changes described above.)

---

To generate the prison cells after given n days, we iterate to generate the
each next state that the given prison cell can be placed at. We note that after
a single day the first and last prison cells must be 0 - and any in between is
the XOR of the two adjcent neighbours (like Game of Life).

However, we do not have to repeat this process N times since there are only
8 cells, there are only finite amount of possible state that the cells can be
placed at. So, by creating a mapping of when each of the new state are found,
once the duplicate has been detected, we can use the moduolo operation to skip
the operation as it will be simple repeatition from these states.

---

Python:

```python

class Solution:
    def prisionCellsAfterNDays(self, cells, n):
        def nextCells(cells):
            return tuple([0] + [int(not(cells[i-1] ^ cells[i+1])) for i in range(1,7)] + [0])

        days = 0
        allCells = dict()
        currCells = tuple(cells)
        while days <= n and currCells not in allCells:
            allCells[currCells] = days
            days += 1
            currCells = nextCells(currCells)
        
        if days < n:
            cycleAt = days - allCells[currCells]
            remainingDays = (n - allCells[currCells]) % cycleAt
            for _ in range(reminaingDays):
                currCells = nextCells(currCells)

        return list(currCells)
```
