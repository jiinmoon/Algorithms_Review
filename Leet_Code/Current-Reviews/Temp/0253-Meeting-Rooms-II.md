# 253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

---

We split the given intervals into their respective start and end times. These
times are sorted. For every start time, we require new room. But when we found
that current start time is greater than the end time, then we do not require
a new room and would be made available for us.

Time complexity would be O(n * log(n)) due to sorting involved and O(n) in
space required.

---

Python:

```python

class Solution253:

    def minMeetingRooms(self, times):

        startTimes, endTimes = [], []

        for s, e in times:
            startTimes.append(s)
            endTimes.append(e)

        startTimes.sort()
        endTimes.sort()

        s, e, total = 0, 0, 0

        while s < len(times):
            if startTimes[s] > = endTimes[e]:
                total -= 1
                e += 1
            total += 1
            s += 1

        return total
```
