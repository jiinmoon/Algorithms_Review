1167 Minimum Cost to Connect Sticks
===================================

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying
a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in
this way.

---

Since minimum cost is the sum of two lowest valued sticks, we utilize min heap
to store our sticks values and combine them repeatedly until we have a single
stick left.

The time complexity of this algorithm would be O(n * log(n)) - heappop and
heappush costs log(n) and it is repeated for each stick until merged.

---

Python:

```python
from heapq import heappop, heappush, heappify

class Solution:
    def connectSticks(self, sticks):
        totalCost = 0
        heappify(sticks)
        while len(sticks) > 1:
            X, Y = heappop(sticks), heappop(sticks)
            totalCost += (X + Y)
            heappush(sticks, (X + Y))
        return totalCost
```
