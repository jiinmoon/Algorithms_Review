# 346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

---

The window size is fixed; thus, it would be simplest to implement this data
structure as a circular array where new elements will be inserted at the
insertion point which is mouluo by the given size.

---

Python:

```python

class MovingAverage:
    def __init__(self, size):
        self.ins = 0
        self.total = 0
        self.q = [ None for _ in range(size) ]

    def next(self, num):
        # queue is full;
        # update the queue and current total sum
        if self.q[self.ins]:
            self.total -= self.q[self.ins]
        self.total += num
        self.q[self.ins] = num
        self.ins = (self.ins + 1) % len(self.q)
        # queue is not full yet; count is upto insertion pointer
        count = self.ins if not self.q[-1] else len(self.q)
        return self.total / count
```

