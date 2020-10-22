# 1167 Minimum Cost to Connect Sticks

You have some number of sticks with positive integer lengths. These lengths are
given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying
a cost of x + y. You must connect all the sticks until there is only one stick
remaining.

Return the minimum cost of connecting all the given sticks into one stick in
this way.

---

Here, we can utilize the heap to maintain a sorted list of stick values so that
at each iteration, we can pull out two sticks of cost x and y that are current
minimum in the given list. Heapify will cost us O(n) and each removal and
insertion into the heap will be of O(log(n)). This is repeated until we exhaust
all the sticks to connect. The total will be maintained and returned.

---

Python:

```python

import heapq

class Solution:
    def connectSticks(self, sticks):
        heapify(sticks)
        totalCost = 0

        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            totalCost += x + y
            heappush(sticks, x + y)

        return totalCost
```
