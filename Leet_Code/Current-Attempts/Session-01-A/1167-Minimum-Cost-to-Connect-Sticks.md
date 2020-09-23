# 1167 Minimum Cost to Connect Sticks

Use heap to maintain the least cost to connect sticks.

---

Python:

```python

import heapq

class Solution:
    def minCost(self, sticks):
        heapify(sticks)
        total = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            total += x + y
            heappush(sticks, x + y)
        return total
```
