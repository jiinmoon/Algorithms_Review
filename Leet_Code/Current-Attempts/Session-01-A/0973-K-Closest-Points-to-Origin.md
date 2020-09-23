# 973 K Closest Points to origin

Since we only require K closest, we use heap instead of sorting.

---

Python:

```python

import heapq

class Solution:
    def kClosest(self, points, k):
        pq = [(p[0]**2 + p[1]**1, p) for p in points]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```
