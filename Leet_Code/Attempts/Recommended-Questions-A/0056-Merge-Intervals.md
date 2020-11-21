# 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

---

We first sort the given list of intervals by its start times. Then, we compare
pairwise against last interval that is added to our result list. If the next
interval start time is greater than the current result in the result, then it
is a new interval to be added; otherwise, we need to update our current result
interval's end time as it is to be merged.

Due to sorting invovled, time complexity would be O(n * log(n)), but space
would be as much as we need for our result to be returned which is as largeas
O(n).

---

Java:

```java

class Solution {
    public int[][] mergeIntervals(int[][] intervals) {
        List<int[]> result = new ArrayList<>();

        // sort by start times
        Arrays.sort(intervals, (int[] a, int[] b) -> {
            return Integer.compare(a[0], b[0]);
        });
        
        int start = interval[0][0];
        int end = interval[0][0];
        for (int[] interval : intervals) {
            if end < interval[0] {
                // previous end time is smaller than next interval's start
                result.add(new int[] {start, end};
                start = interval[0];
            } else {
                // otherwise, merge by updating previous end time
                end = Math.max(end, Interval[1]); 
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}

```

Python:

```python

class Solution:
    def mergeIntervals(self, intervals):
        intervals.sort()
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
```
