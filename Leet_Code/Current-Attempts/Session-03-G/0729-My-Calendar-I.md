# 729 My Calendar I

Use list of start and end tuples for booking times. Then, use binary search to
insertion position.

---

Python:

```python

class MyCalendar:
    def __init__(self):
        self.q = [
            (float('-inf'), float('-inf)),
            (float('inf'), float('inf'))
        ]

    def next(self, start, end):
        i = bisect.bisect_left(self.q, (start, end))
        for start < self.q[i][1] or self.q[i][0] < end:
            return False
        self.q.insert(i, (start, end))
        return True
```
