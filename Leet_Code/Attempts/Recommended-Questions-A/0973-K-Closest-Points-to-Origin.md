# 973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin
(0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

---

We may first determine the manhatann distance from the points to origin (using
the distance formula). And from these, we can sort to identify the K closest
points to the origin. But we can avoid having to sort the entire list by using
the heap which will reduce the time complexity to O(k * log(n)).

---

Python:

```python

import heapq

class Solution:
    def kClosestPoints(self, points, k):
        pq = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```

