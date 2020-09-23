# 253 Meeting Rooms II

We separate out the starting times from the end times. When both are in sorted
order, for each starting times, we require a new meeting room. But when the
start time is less than the end time, we do not have to reserve a new meeting
room.

---

Python:

```python

class Solution:
    def meetingRooms(self, times):
        startTimes, endTimes = list(), list()
        for t in times:
            startTimes.append(t[0])
            endTimes.append(t[1])

        startTimes.sort()
        endTimes.sort()
        s, e, total = 0, 0, 0

        for i in range(len(times)):
            if startTimes[s] >= endTimes[e]:
                total -= 1
                e += 1
            total += 1
            s += 1
        
        return total
```
