# 1167 Minimum Cost to Connect Sticks

You have some number of sticks with positive integer lengths. These lengths are
given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying
a cost of x + y. You must connect all the sticks until there is only one stick
remaining.

Return the minimum cost of connecting all the given sticks into one stick in
this way.

---

For this problem, we need to repeatedly select two smallest values to add to
our total, and return the sum of two values back into the list until we have
exhausted the list. Since finding the min takes O(n), this naive implementation
with a simple list structure will cost O(n^2) in total.

To improve on this, we can use a priority queue or min heap - where we can
heapify in O(n) time in the beginning, and we only have to heappop and heappush
for O(log(n)) time each. Thus, total cost will be O(n * log(n)).

---

Python:

```python

import heapq

class Solution:
    def connectSticks(self, sticks):
        heapify(sticks)
        total = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            total += x + y
            heappush(sticks, x + y)
        return total
```
