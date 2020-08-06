""" 56. Merge Inteverals

Question:

    Given a collection of intervals, merge all overlapping intervals.

+++

Solution:

    To determine whether the intervals can be merged or not, we should first
    sort the intervals by their first element. This allows us to merge the two
    intervals next to each other if last element of first interval is less than
    first element of the second interval.

"""

class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals

        intervals.sort(key = lambda interval: interval[0])
        result = [ intervals[0] ]
        for interval in intervals[1:]:
            # last element of first interval < first element of second?
            if result[-1][1] < interval[0]:
                # interval is not overlap.
                result.append(interval)
            else:
                # interval overlaps; merge two by replacing last element of
                # first interval by greater of two last elements of intervals.
                result[-1][1] = max(result[-1][1], interval[1])
        return result

