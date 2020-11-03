# 1167. Minimum Cost to Connect Sticks

You have some number of sticks with positive integer lengths. These lengths are
given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying
a cost of x + y. You must connect all the sticks until there is only one stick
remaining.

Return the minimum cost of connecting all the given sticks into one stick in
this way.

---

In order to find the minimum cost to connect all the given sticks, we need to
repeatedly add the two smallest sticks at the moment and return the connected
stick back to the pool. The best approach in this case would be using heap
since maintaining the heap is a logrithmic in time complexity.

---

Python:

```python

import heapq

class Solution:
    def minCost(self, sticks):
        result = 0
        heapify(sticks)
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            result += x + y
            heappush(sticks, x + y)
        return result
```

