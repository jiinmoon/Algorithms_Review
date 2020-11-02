# 295 Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

```
void addNum(int num) - Add a integer number from the data stream to the data
structure.

double findMedian() - Return the median of all elements so far.
```

---

Here, we divide the elements into a two equal halves, left and right. The left
array will maintain its maximum value whereas right array will maintain its
minimum value such that the "mid" value can be identified easily.

To make this process easier, we can use max heap and min heap to optimize the
operations. Also, to deal with the odd and even length situation, we always try
to maintain the left array one higher than the right array.

As for time complexity, addNum will take O(log(n)) for pushing onto the heaps
and findMedian will be O(1).

---

Python:

```python

import heapq

class MedianFinder:
    def __init__(self):
        self.l = list()
        self.r = list()

    def addNum(self, num):
        # left is the max heap (negate values)
        # heapq is a min heap by default
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if len(self.l) < len(self.r):
            heappush(self.l, -heappop(self.r))

    def findMedian(self):
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) * 0.5
```
