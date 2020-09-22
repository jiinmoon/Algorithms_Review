973 K Closest Points to Origin
==============================

We have a list of _points_ on the plane; find the closest points to the origin
as determined by the euclidean distance.

---

We will gather the Euclidean distance of all the points releative to the origin
- note that we do not have to compute sqrt here. And we sort to retrieve the
  Kth smallest points.

---

Python:

```python
from heapq import heapify, heappop

class Solution:
    def kClosest(self, K, points):
        res = []
        for p in points:
            x, y = p
            res.append( (x*x + y*y, p) )
        heapify(res)
        return [heappop(res) for _ in range(K)]
```

