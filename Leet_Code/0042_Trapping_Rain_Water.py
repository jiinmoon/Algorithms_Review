""" 42. Trapping Rain Water

Question:

    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it is able to trap after raining.

+++

Solution:

    As we iterate on each cell, the problem is how much water does each cell can
    hold? It depends on surrounding heights minus the its own height.

"""

class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        m = len(heights)
        leftMaxes = heights.copy()
        rightMaxes = heights.copy()

        for i in range(1, m):
            leftMaxes[i] = max(leftMaxes[i], leftMaxes[i-1])

        for i in range(m-2, -1, -1):
            rightMaxes[i] = max(rightMaxes[i], rightMaxes[i+1])

        total = 0
        for i in range(1, m):
            total += min(leftMaxes[i], rightMaxes[i]) - heights[i]

        return total
