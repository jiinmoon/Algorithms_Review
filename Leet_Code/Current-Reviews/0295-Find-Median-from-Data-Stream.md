# 295. Find Median from Data Stream

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

#### (1) Maintain sorted data.

One method that can support efficient findMedian operation is to maintain
a sorted list of data stream. To do so, we can use binary search algorithm to
find the insertion point in O(log(n)) time to update our existing list whenever
we are adding a new value. However, due to shifting that may occur, the time
complexity to update can take upto O(n).

#### (2) Max-Heap and Min-Heap.

Another approach that can support this as efficiently as possible would be to
use max-heap and min-heap. We divide the array into two equal halves - on left,
we create a max-heap and on right, we have a min-heap. So, at any given point,
the median has to be top of two heaps. Updating the heaps can take in O(log(n))
times.

---

Python: Two Heaps.

```python

from heapq import heappush, heappop

class Solution295:

    def __init__(self):

        self.left = []      # Max-Heap
        self.right = []     # Min-Heap


    def addNum(self, num):

        heappush(self.left, -num) 
        heappush(self.right, -heappop(self.left))

        # maintain size of left greater than right to identify odd cases
        if len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))

    
    def getMedian(self):
        
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) * 0.5
```
