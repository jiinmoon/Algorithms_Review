# 752. Open the Lock

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

We can visualize this problem as a finding the shortest path from the starting
combination of "0000" to the given goal state "while" avoiding the deadends.
The next combinations (neighbours) are generate by converting each of the digit
of the current combination by +1 or -1. To find the shortest path, we use the
bidirectional BFS.

---

Python:

```python

class Solution:
    def openTheLock(self, deadends, target):
        def helper(state):
            allStates = set()
            for i, char in enumerate(state):
                for shifted in [(int(char) + 1) % 10, (int(char) -1) % 10]:
                    allStates.add(
                        state[:i] + str(shifted) + state[i+1:])
            return allStates - visited

        visited = set(deadends)
        f, b = {"0000"}, {target}
        length = 1

        while f and b:
            if f & b:
                return length

            if len(f) > len(b):
                f, b = b, f

            newf = set()
            for state in f:
                visited.add(state)
                newf |= helper(state)

            f = newf
            length += 1

        return -1
```

