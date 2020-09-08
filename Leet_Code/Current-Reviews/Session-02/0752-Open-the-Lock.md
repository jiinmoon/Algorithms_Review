752 Open the Lock
=================

You have a lock in front of you with 4 circular wheels. Each wheel has 10
slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate
freely and wrap around: for example we can turn '9' to be '0', or '0' to be
'9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the
4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of
these codes, the wheels of the lock will stop turning and you will be unable to
open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it
is impossible.

---

Think of this problem as a graph problem - in particular, this is about finding
the shortest path to the start ("0000") to the target combination while
avoiding the neighbours in deadends.

Here, we will use bidirectional BFS. Since there are finite number of
combinations for 4 digits (10^4), the time complexity is actually constant.

---

Python: bidirectional BFS.

```python
class Solution:
    def openLock(self, deadends, target):
        f, b = { "0000" }, { target }
        visited = set()
        deadends = set(deadends)
        totalTurns = 0

        def nextStates(state):
            allStates = set()
            for i, c in enumerate(state):
                # mod 10 to wrap around "0" -> "9"
                nextVal = (int(c) + 1) % 10
                allStates.add(state[:i] + str(nextVal) + state[i+1:])
                nextVal = (int(c) - 1) % 10
                allStates.add(state[:i] + str(nextVal) + state[i+1:])
            return allStates

        while f:
            if f & b:
                return totalTurns

            nextf = set()
            for state in f:
                if state in visited or state in deadends:
                    continue
                visited.add(state)
                nextf |= nextStates(state)

            f = nextf
            totalTurns += 1

            if len(f) > len(b):
                f, b = b, f

        return -1
```
