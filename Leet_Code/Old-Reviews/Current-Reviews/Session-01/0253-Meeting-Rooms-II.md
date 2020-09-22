253 Meeting Rooms II
====================


Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

Example 1:

```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
```

---

Let's approach this problem logically. First, the intervals may be is unsorted,
so we can sort by its start or end times. The start time gives us an idea as to
when the meetings occur; end time gives us an idea when these need to close.

For example, suppose that we have a meeting starting at 1, and next at 5. We
need additional meeting room if the previous meeting that has started at 1 has
not been finished yet. Thus, this forms the basis of our algorithm.

This will be O(n * log(n)) time complexity for doing sort and O(n) for memory.

---

Go:

```go
import "sort"

func minMeetingRooms(intervals [][]int) int {
    var (
        m = len(intervals)
        startTimes = make([]int, m, m)
        endTimes = make([]int, m, m)
        sPtr = 0
        ePtr = 0
        res = 0
    )
    // split and sort times
    for i, interval := range intervals {
        startTimes[i] = interval[0]
        endTimes[i] = interval[1]
    }
    sort.Ints(startTimes)
    sort.Ints(endTimes)
    
    for sPtr < m {
        // if a meeting ended before start
        if startTimes[sPtr] >= endTimes[ePtr] {
            // free a room
            res -= 1
            ePtr += 1
        }
        // otherwise, room is always occupied by the new start
        res += 1
        sPtr += 1
    }
    return res
}
```
