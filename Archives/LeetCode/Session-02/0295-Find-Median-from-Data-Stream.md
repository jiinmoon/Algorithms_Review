# 295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value and the median is the mean of the two
middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

```
MedianFinder() initializes the MedianFinder object.

void addNum(int num) adds the integer num from the data stream to the data
structure.

double findMedian() returns the median of all elements so far. Answers within
10-5 of the actual answer will be accepted.
```

---

We can find the median easily given that we can maintain the sorted list of
integers from the data stream in efficient manner. This can be done with either
binary search method of finding the insertion place or use a heap or priority
queue structure.

In particular, we can use two heap method in order to reduce our search and
insertion time further. We divide the given list of integers into two equal
halves and balance them out into left and right heaps. The left heap would be
our max heap, and right heap would be the min heap. Hence, all we require to
maintain is the two elements from the top which means that we do not have to
maintain entire sorted list of integers and can identify median in constant
time.

---

Python:

```python

from heapq import heappush, heappop

class Solution295:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
    
    def addNum(self, num):
        # negate when pushing unto leftHeap to make it max heap
        heappush(self.leftHeap, -num)
        heappush(self.rightHeap, heappop(self.leftHeap))
        # tilt so that left heap has one more element if size is uneven
        if len(self.leftHeap) < len(self.rightHeap):
            heappush(self.leftHeap, -heappop(self.rightHeap))

    def findMedian(self):
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        return (-self.leftHeap[0] + self.rightHeap[0]) * 0.5

```

