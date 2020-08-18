295 Find Median from Data Stream
================================

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

We will need to maintain a sorted ordering to retrieve the median efficiently.
As more data comes in, we want to sort as the same time as well. This is
efficiently done by using insertion sort where we only have to find the
insertion point for the new element into already sorted list. Thus, adding
every element will cost us O(log (n)) but retrieving a median can be done in
O(1). This assumes that the underlying structure used supports efficient
insertion and resizing at any index such as doubly linked list.

Alternatively, we can use heap (or priority queue) structure.

We may use two heaps where we are going to use max heap for left and min heap
for the right. Thus, when we add elements, we balance the two heap counts and
median candidates should be on top.

We first insert into the left heap (max). Then, take the max of left heap and
insert to the right heap (min). To balance out, if the left heap size is lower
than right heap, then we remove the min from right heap onto left heap.

---

Python:

Using two heaps; note that heapq does have internal unexposed max heapq
functions, but simply we will negate the values to create max heaps.

```python
import heapq

class MedianFinder:     
    def __init__(self):
        self.left = []  # max heap
        self.right = [] # min heap
        

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        heappush(self.right, -heappop(self.left))
        # balance heaps
        if len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) * 0.5
```
