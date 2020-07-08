""" 57. Insert Interval

Question:

    Give a set of non-overlaping intervals, insert a new interval into the
    intervals (merge if neccesary).

    Assume that the input array is sorted accoring to their start times.

---

Solution:

    Since the array is sorted and we may have to merge the intervals, we would
    first try to find intervals that should be to left and right of the
    new interval. This can be achieved in linear time - simply iterate while
    comparing current interval's range to new interval.

    Then, it is possible that we have to merge the intervals, we would take
    that into the consideration by updating the new interval's elements.

"""

class Solution:
    def insert(self, intervals, new_interval):
        m = len(intervals)
        left, right = 0, m-1
        
        # find intervals to left and right of new_interval.
        while left < m and intervals[left][1] < new_interval[0]:
            left += 1
        while right >= 0 and intervals[right][0] > new_interval[1]:
            right -= 1

        # if found, then we update new interval values before insertion.
        if left <= right:
            new_interval[0] = min(intervals[left][0], new_interval[0])
            new_interval[1] = max(intervals[right][1], new_interval[1])

        # either way, insert new_interval.
        return intervals[:left] + new_interval + intervals[right+1:] 
