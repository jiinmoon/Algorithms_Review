""" 11. Container With Most Water

Question:

    Given a list of heights, find two lines that which forms an container that
    can contain most amount of water - and find its maximum area.

+++

Solution:

    In this problem, we will utilize the two pointers method. Start from each
    end of the list, we should find that current area is the minimum of two
    heights multiplied by distance between two heights. Then, it should be
    compared against the maximum area variable that we keep track of, and move
    on to the next. From this position, the only possible way for the current
    area to incrase should be moving the pointer at the lower hight.

"""

class Solution:
    def maxArea(self, heights):
        m = len(heights)
        if not heights or m < 2:
            return 0
        maxThusFar = float('-inf')
        lo, hi = 0, m - 1
        while lo < hi:
            currArea = min(heights[lo], heights[hi]) * (hi - lo)
            maxThusFar = max(currArea, maxThusFar)
            if heights[lo] <= heights[hi]:
                lo += 1
            else:
                hi -= 1
        return maxThusFar if maxThusFar != float('-inf') else 0
