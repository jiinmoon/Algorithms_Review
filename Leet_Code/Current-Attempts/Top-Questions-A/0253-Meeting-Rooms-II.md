# 253 Meeting Rooms II


Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

---

We first isolate the start and end times; then sort the two times. Then, we can
compare the start time against the end times - if start time is greater or
equal to current end time, then we do not require a new room to reserve.
Otherwise, we assume that we would require a room for each start time.

Due to sorting, time complexity is O(n * log(n)).

---

Python:

```python

class Solution:
    def meetingRooms(self, times):
        stimes, etimes = list(), list()
        for t in times:
            stimes.append(t[0])
            etimes.append(t[1])

        stimes.sort()
        etimes.sort()

        s, e, total = 0, 0, 0

        while s < len(times):
            if stimes[s] >= etimes[e]:
                total -= 1
                e += 1
            total += 1
            s += 1

        return total
```
