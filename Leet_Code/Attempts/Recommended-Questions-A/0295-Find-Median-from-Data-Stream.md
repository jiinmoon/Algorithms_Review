# 295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

---

To compute the median from a data stream, one approach is to maintain a sorted
list. To do so efficiently, we may use the insertion sort which can gurantee
a relatively fast sorting method. The best approach however would be to use the
min and max heap to maintain the top half and bottom half.

---

Python:

```python

import heapq

class MedianFinder:
    def __init__(self):
        self.l, self.r = list(), list()

    def addNum(self, num):
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if len(self.l) < len(self.r):
            heappush(self.l, -heappop(self.r))

    def findMedian(self):
        if len(self.l) > len(self.r):
            return -self.l[0]
        return (-self.l[0] + self.r[0]) * 0.5
```
