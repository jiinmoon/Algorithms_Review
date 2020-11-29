# 362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past
5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you
may assume that calls are being made to the system in chronological order (ie,
the timestamp is monotonically increasing). You may assume that the earliest
timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

---

Here, we use queue to maintain the timestamps of each hit. When we need to
retrieve the hits, we simply compare our top of queue to current timestamps
. If their difference exceeds the set limit of 5 mins, then we remove. This
process is repeated and we return the remaining hits within the queue.

---

Python:

```python

class Solution362:

    def __init__(self):
        self.q = collections.deque()

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)
```
