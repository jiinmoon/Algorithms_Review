""" 11. Container With Most Water

Question:

    Given n non-negative integers, where each represents a point at coords. n
    vertical lines are drawn such that the two endpoints of line is at i and j.
    Find the two lines, which together with x-axis forms a container such that
    container contains the most water.

+++

Solution:

    We can find that only way to increase the area is to move to smaller height.
    Thus, this problem has a directionality that we can use with our two pointer
    algorithm.

"""

class Solution:
    def maxArea(self, heights):
        if not heights:
            return 0
        maxArea = 0
        lo, hi = 0, len(heights)-1
        while lo < hi:
            currArea = min(heights[lo], heights[hi]) * (hi - lo)
            maxArea = max(maxArea, currArea)
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        return maxArea
