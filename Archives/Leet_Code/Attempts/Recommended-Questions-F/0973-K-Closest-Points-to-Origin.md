# 973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin
(0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

---

A naive approach to this problem would be to sort the entire given points by
its Euclidean distance to the origin. But we can avoid having to sort the
entire array by using heap data structure to only extract the top K closest
points and not have to sort the entire array. Since the reordering heap costs
logrithmic time, the time complexity is O(n * log(k)).

---

Python:

```python

import heapq

class Solution:
    # also consider using heapq.nsmallest(n, iterable, comparator)
    def kClosest(self, points, k):
        pq = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapify(pq)
        return [heappop(pq) for _ in range(k)]
```
