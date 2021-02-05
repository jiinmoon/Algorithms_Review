# 252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

---

Firstable, we sort the given intervals by its start times. Then, as we iterate
on forward, check each interval's start time against previous maximum end
times. If the previous end time is greater than current interval's start time,
we cannot attend all the meetings.

Due to sorting, the time complexity should be O(n * log(n)); but no additional
space is required.

---

Java:

```java

class Solution {
    
    public boolean canAttendMeetings(int[][] intervals) {

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int end = intervals[0][0];
        for (int[] interval : intervals) {
            if (end > interval[0]) return false;
            end = Math.max(end, interval[1]);
        }

        return true;
    }
}

```

Python:

```python

class Solution:

    def canAttendMeetings(intervals):
        intervals.sort()

        prevEnd = intervals[0][0]
        for interval in intervals:
            if prevEnd > interval[0]:
                return False
            prevEnd = max(prevEnd, interval[1])

        return True

```
