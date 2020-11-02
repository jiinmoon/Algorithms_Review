# 752 Open the Lock

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

We think of this problem as a graph problem - the find the shortest path from
starting position "0000" to the given target position. We find the next
possible postion from a current position by adding 1 or subtracting 1 on each
of the positions to build the next set of candidate positions to visit. To
avoid cycle, visited set is create to save the visited positions.

We use Bidirection BFS to improve upon the regular BFS by half of the branching
factor.

---

Python:

```python

class Solution:
    def openLock(self, target, deadends):
        def nextPositions(pos):
            result = set()
            for i, c in enumerate(pos):
                for nc in [(int(c)+1) % 10, (int(c)-1) % 10]:
                    result.add(pos[:i] + str(nc) + pos[i+1])
            return result - visited

        visited = set(deadends)
        f, b = {"0000"}, {target}
        total = 1
        
        while f:
            if f & b:
                return total

            if len(f) > len(b):
                f, b = b, f
            
            newf = set()
            for pos in f:
                visited.add(pos)
                if pos not in visited:
                    newf |= nextPositions(pos)
            
            f = newf

        return -1
```
