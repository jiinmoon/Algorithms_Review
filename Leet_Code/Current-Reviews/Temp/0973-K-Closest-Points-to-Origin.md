# 973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin
(0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

---

#### 1. Sort by distance.

By computing the distance using distance formula (`d^2 = (x - x0)^2 + (y - y0)^2`), 
we can sort to find the K closest points. Due to sorting, we have to spend O(n * log(n)) in time and O(n) in space.

#### 2. Prioirty Queue (Heap).

This expands on the sorting approach where we are using heap instead. By using
heap, we can identify closests points at top of heap every time. Heapify
operation takes O(n) and we have to perform K number of trickleUp operation
which would be O(K * log(n)) in time complexity.

---

Python: Min-heap.

```python

from heapq import heapify, heappop

class Solution973:

    def kClosest(self, points, k):
        
        # Min-Heap
        pq = [(p[0]**2+p[1]**2, p) for p in points]
        heapify(pq)

        return [heappop(pq)[1] for _ in range(k)]
```


