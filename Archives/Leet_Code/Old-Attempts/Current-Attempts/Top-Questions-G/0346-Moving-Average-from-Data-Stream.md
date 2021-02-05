# 346 Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

---

We can implement this in various ways but circular array would be most
efficient. We create an array of given size, and use modulo operation to wrap
around to find the next insertion point.

---

Python:

```python

class MovingAverage:
    def __init__(self, size):
        self.q = [ None for _ in range(size) ]
        self.total = 0
        self.i = 0

    def next(self, num):
        if self.q[self.i]:
            self.total -= self.q[self.i]
        self.total += num
        self.q[self.i] = num
        self.i = (self.i + 1) % len(self.q)
        size = self.i if not self.q[-1] else len(self.q)
        return self.total / size
```
