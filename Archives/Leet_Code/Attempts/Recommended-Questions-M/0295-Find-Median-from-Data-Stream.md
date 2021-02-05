# 295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.

---

To find the median from the given stream of integer values, we need a way to
identify the "middle" values quickly as possible. To do so, we use heap. We
visualize the given queue as lower and upper half. In the lower half, we create
a max heap where we can maintain the maximum of the lower half - and vice versa
for the upper half with a min heap.

To deal with the even and odd cases, we purposely make the lower half 1 greater
than the upper half so that if we see that lower array length is greater than
the upper, we have an odd case where we can simply return the top of the lower
half. Otherwise, we compute the median of the top of the two halves.

---

Python:

```python

import heapq

class MedianFinder:
    def __init__(self):
        self.lower, self.upper = list(), list()

    def addNum(self, num):
        heappush(self.lower, -num)
        heappush(self.upper, -heappop(self.lower))
        if len(self.lower) < len(self.upper):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self):
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        return (self.lower[0] + self.upper[0]) * 0.5
```
