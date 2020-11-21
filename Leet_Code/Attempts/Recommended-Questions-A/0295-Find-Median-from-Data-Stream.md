# 295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

---

To compute the median from a data stream, one approach is to maintain a sorted
list. To do so efficiently, we may use the insertion sort which can gurantee
a relatively fast sorting method. The best approach however would be to use the
min and max heap to maintain the top half and bottom half.

Time complexity for adding would be in logrithmic and finding median would be
constant. Space complexity is O(n).

---

Java:

```java

import java.util.PriorityQueue;

class MedianFinder {
    private PriorityQueue<Integer> leftPQ;  // max-heap
    private PriorityQueue<Integer> rightPQ; // min-heap

    public MedianFinder() {
        this.leftPQ = new PriorityQueue<>(Collections.reverseOrder());
        this.rightPQ = new PriorityQueue<>();
    }

    public void addNum(int num) {
        this.leftPQ.add(num);
        this.rightPQ.add(this.leftPQ.remove());
        // always balance to left
        if (this.leftPQ.size() < this.rightPQ.size())
            this.leftPQ.add(this.rightPQ.remove());
    }

    public double findMedian() {
        return (this.leftPQ.size() > this.rightPQ.size()) ? 
            this.leftPQ.peek() :
            (double) (this.leftPQ.peek() + this.rightPQ.peek()) / 2;
    }
}


```

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
