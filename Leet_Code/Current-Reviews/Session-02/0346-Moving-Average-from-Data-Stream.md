346 Moving Average from Data Stream
===================================

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

---

This can be easily implmented with deque (which can support popleft in O(1)) or
circular array by keeping track of the index to put.

---

Python: deque approach.

```python
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.q = deque()
        self.size = size

    def next(self, val):
        if len(self.q) < self.size:
            self.q.append(val)
        else:
            self.q.popleft()
            self.q.append(val)
        return sum(self.q) / len(self.q)
```

Python: circular-array approach.

```python
class MovingAverage:
    def __init__(self, size):
        self.totalSum = = 0
        self.ins = 0
        self.circularArray = [ None for _ in range(size) ]

    def next(self, val):
        # array is full; update totalSum and array
        if self.array[self.ins]:
            self.totalSum -= self.circularArray[self.ins]
        self.totalSum += val
        self.circularArray[self.ins] = val

        # update insertion point
        self.ins = (self.ins+1) % len(self.circularArray)
        count = sum(v != None for v in self.circularArray)
        return self.total / count
```

