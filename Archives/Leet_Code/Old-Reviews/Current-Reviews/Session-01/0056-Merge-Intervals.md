56 Merge Intervals
==================

Given a collection of intervals, merge all overlapping intervals.

Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```


Example 2:

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

---

We will first sort the intervals by their first element - many language will
have a sort library that allows for custom key to sort by. Then, we will
iterate on the sorted intervals checking the last element of the prev to first
element of the next interval.

---

Go:

```go
import "sort"

func merge(intervals [][]int) [][]int {
    var res [][]int
    sortIntervals(intervals)
    for _, i := range intervals {
        if len(res) == 0 || res[len(res)-1][1] < i[0] {
            res = append(res, i)
        } else {
            res[len(res)-1][1] = max(res[len(res)-1][1], i[1])
        }
    }
    return res
}

func sortIntervals(intervals [][]int) {
    sort.Slice(
            intervals, 
            func (i, j int) bool {
                return intervals[i][0] < intervals[j][0]
    })
}

func max(x, y int) int {
    if x >= y {
        return x {
    }
    return y
}
```

