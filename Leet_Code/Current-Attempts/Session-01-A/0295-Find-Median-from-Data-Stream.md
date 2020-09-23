# 295 Find Median from Data Stream

Use min and max heaps to add in the values as they come in. Balance the both to
maintain same number of elements from left to right.

---

Python:

```python

import heapq

class MedianFinder:
    def __init__(self):
        self.l = list()
        self.r = list()

    def addNum(self, num):
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if len(self.l) > len(self.r):
            heappush(self.l, -heappop(self.r))

    def findMedian(self):
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) * 0.5
```
