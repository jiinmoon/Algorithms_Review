# 253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

---

To find the minimum number of rooms to book, we first separate and sort the
start and end times. Then, we note that for each of the start times, we would
requre a new room. And every end time that we can complete before the next
start time, we can remove the room since it would be come available.

---

Java:

```java

class Solution {
    public int meetingRooms(int[][] intervals) {
        int m = intervals.length;
        int[] startTimes = new int[m];
        int[] endTimes = new int[m];

        for (int i = 0; i < m; i++) {
            startTimes[i] = intervals[i][0];
            endTimes[i] = intervals[i][1];
        }

        Arrays.sort(startTimes);
        Arrays.sort(endTimes);

        int start, end, result;
        start = end = result = 0;

        while (start < m) {
            if (startTimes[start] >= endTimes[end]) {
                result--;
                end++;
            }
            result++;
            start++;
        }

        return result;
    }
}
```

Python:

```python

class Solution:
    def meetingRooms(self, times):
        sTimes, eTimes = list(), list()
        for time in times:
            sTimes.append(time[0])
            eTimes.append(time[1])

        sTimes.sort()
        eTimes.sort()

        srt, end, total = 0, 0, 0
        while srt < len(times):
            if sTimes[srt] >= eTimes[end]:
                total -= 1
                end  += 1
            total += 1
            srt += 1
        return total
```
