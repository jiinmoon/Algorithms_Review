# 973 K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin
(0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

---

We want to sort the points in such way that they are sorted by the order of
their "closeness" to the origin (0, 0). This can be computed by distance
formula. However, we do not need to sort the entire list, but use a heap to our
advantage such that min heap will allow us to extract the k closest points.
Hence, the time complexity can be reduced to O(k * log(n)).

---

Python:

```python

import heapq

class Solution:
    def kClosest(self, points, k):
        pq = [(p[0] ** 2 + p[1] ** 2, p) for p in points)]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```
