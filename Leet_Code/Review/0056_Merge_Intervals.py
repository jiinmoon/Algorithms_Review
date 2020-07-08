""" 56. Merge Intervals

Question:

    Given a collection of intervals, merge all overlapping intervals.

+++

Solution:

    First, we would sort the intervals by their first element to see the merge
    order. It allows us to compare the intervals next to one another - and
    merge them if necessary.

"""
class Solution:
    def merge(self, intervals):
        if not intervals:
            return 
        sort_by_first = lambda interval : interval[0]
        intervals.sort(key = sort_by_first
        result = [ intervals[0] ]
        for interval in intervals[1:]:
            # no overlap
            if result[-1][1] < interval[0]:
                result.append(interval)
            # overlap
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

