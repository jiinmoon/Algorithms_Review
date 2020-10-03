# 957 Prison Cells After N Days

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

There are only 8 prison cells - meaning that there are finite number of fixed
possible states that cells can ever be in. Also, after a single day, first and
last element of the cell is fixed to 0. Knowing this, we will first find all
possible states that cells can be in (if day is less than number of possible
states, we can return right away). Then, we can use modulo to determine
remainder of the day to move current state forward to return.

---

Python:

```python

class Solution:
    def prisonAfterNDays(self, cells, N):
        def nextState(currState):
            return [0] + [not(int(currState[i-1] ^ currState[i+1])) for _ in range(1, 7) + [0]

        day = 0
        allStates = dict()
        currState = tuple(cells)

        while day < N and currState not in allStates:
            allStates[currState] = day
            currState = nextState(currState)
            day += 1

        if day < N:
            cycle = day - allStates[currState]
            remaining = (N - allStates[currState]) % cycle
            for _ in range(remaining):
                currState= nextState[currState]

        retrun currState
```
