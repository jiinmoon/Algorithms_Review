362 Design Hit Counter
======================

Design a hit counter which counts the number of hits received in the past
5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you
may assume that calls are being made to the system in chronological order (ie,
the timestamp is monotonically increasing). You may assume that the earliest
timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

---

Simply, we maintain a queue of timestamps. Whenever hit occurs, we append the
timestamp to this queue. And when getHit is called, we start dequeue from the
queue until its difference of requested timestamp and queue.peek() is greater
than the 300 s or 5 mins difference. To support removal at left in O(1), we
should use a linked list. hit is O(1) but getHit may take upto O(n) depending
on the timestamp that it was called with.

---

Python: deque appraoch (supports popleft at O(1))

```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()
    
    def hit(self, timestamp):
        sefl.q.append(timestamp)

    def getHit(self, timestamp):
        # if we want to maintain the timestamps instead poping them off
        # we can use index pointer instead
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)
```

