957 Prison Cells After N Days
=============================

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

We could iterate until N to find the next state, but this is highly unefficient
once you realize that there can only be finite amount of cells state can be
present. In fact, since the first and last cell never changes and stays at 0,
the maximum number of different possible states will be 2^6.

Hence, if we generate all possible states based on the initial one, all we have
to do is use modulo operation to wrap the number around to find what we need.

So, time complexity and space complexity of this particular setup will be O(1).


---

Python:

```python
class Solution:
    def prisonCellsAfterNDays(self, initialState, N):
        day = 0
        currentState = initialState
        allStates = dict()

        def nextDay(state):
            # after first day, the first and last cells will remain at 0
            # inners cells flip based on its neighbours (XOR)
            return tuple(
                [0] 
                + [int(not(state[i-1] ^ state[i+1])) for i in range(1,7)]
                + [0])
        
        # generate all possible states:
        #   either day is less than N or repeat until cycle
        while day < N and currentState not in allStates:
            allStates[currentState] = day
            currentState = nextDay(currentState)
            day += 1
       
        # all 64 states starting fomr initialState has been generated
        # but still more days to go; subtract as may cycles possible.
        if day < N:
            cycleAt = day - allStates[currentState]
            remainingDays = (N - allStates[currentState]) % cycle
            for _ in range(remainingDays):
                currentState = nextDay(currentState)

        return list(currentState)
```
