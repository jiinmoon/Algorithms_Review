# 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

---

First, we sort the given intervals by its starting times. Then, we compare
every pair to see whether we can merge them. If the previous interval's end
time is less than the next interval's start time, we can add the next interval
to our result. Otherwise, previous interval's end time should be updated as
a maximum of two end times.

Time complexity would be O(n * log(n)) due to sorting involved and O(n) in time
complexity.

---

Java:

```java

class Solution56 {

    public int[][] merge(int[][] intervals)
    {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int start = intervals[0][0], end = intervals[0][1];

        List<int[]> result = new ArrayList<>();

        for (int[] interval : intervals)
        {
            if (end < interval[0])
            {
                result.add(new int[] {start, end});
                start = interval[0];
            }
            end = Math.max(end, interval[1]);
        }

        result.add(new int[] {start, end});

        return result.toArray(new int[result.size()][2]);
    }
}

```

Python:

```python

class Solution56:

    def merge(self, intervals):

        intervals.sort()

        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
```

