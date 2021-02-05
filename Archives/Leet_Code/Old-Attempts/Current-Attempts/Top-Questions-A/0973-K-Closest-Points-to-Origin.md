# 973 K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin
(0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

---

We may create a list of tuple of Euclidean distance and points; then, sort to
retrieve the K closest points. However, due to sorting involved, the time
complexity will be O(n * log(n)). The better approach would be to utilize the
heap - heapify will cost us O(n), and we only have to perform k heappop.

---

```python

import heapq

class Solution:
    def kClosestPoints(self, points, K):
        pq = [(p[0]**2 + p[1]**2, p) for p in points]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(K)]
```
