# 253 Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

---

If we split the given array into start and end times, we notice that for every
start time, we can increase the number of the conference rooms to book. But,
the end times indicate that if the current start time is greater than the
previous end time, we do not have to book a new room but use the exisiting one.

Thus, we first sort both of the start and end times. Then, we iterate on both
to compare current start and end times until we have exhausted all start times.

Due to sorting involved, time complexity is bounded by O(n * log(n)).

---

Python:

```python

class Solution:
    def meetingRooms(self, times):
        sTimes, eTimes = list(), list()
        for s, e in times:
            sTimes.append(s)
            eTimes.append(e)

        sTimes.sort()
        eTimes.sort()

        s, e, total = 0, 0, 0
        while s < len(times):
            if sTimes[s] >= eTimes[e]:
                total -= 1
                e += 1
            total += 1
            s += 1

        return total
```

