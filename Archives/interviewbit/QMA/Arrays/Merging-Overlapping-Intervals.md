# Merging Overlapping Intervals

Given a collection of intervals, merge all overlapping intervals.

---

First, sort the given intervals by its start time. Then, we exaime every pair:
previous intervals end time is less than current intervals start time? we can
safely add new intervals. Otherwise, we update the previous intervals end time
by current intervals end time.

O(n * log(n)) time complexity due to sorting involved.

---

Python:

```python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        intervals.sort(key=lambda i : i.start)
        
        result = [intervals[0]]
        
        for i in intervals[1:]:
            
            if result[-1].end < i.start:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
        
        return result
```
