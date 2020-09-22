# 42 Trapping Rain Water
#
# We start by realizing that the total water that can be trapped is the sum of
# all waters trapped on individual cells which are determined by its height and
# minimum of the surrounding heights.
#
# If so, then for each cell, we can traverse left and right to find the maximum
# heights - and select minimum to compute the current trapped water; and sum
# them all together. However, this is costly and will take O(n^2).
#
# Improvement will be trade off space to speed up; we precompute all the
# maximum heights to the left and right of the each of the cells. While the
# time complexity will reduce to O(n), we also require O(n) additional space.
#
# We can make further improvement by realizing that if we are to exaimne the
# heights, the maximum heights to the left and right is fixed so long as it
# remains the maximum of the two - hence, at any moment we only have to move
# the cell whose height is smaller than the another that is being considered
# here. This will further reduce the space requirement down to constant.

class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        l, r, lmax, rmax = 0, len(heights)-1, 0, 0
        total = 0
        while l < r:
            if heights[l] < heights[r]:
                if lmax <= heights[l]:
                    lmax = heights[l]
                else:
                    total += (lmax - heights[l])
                l += 1
            else:
                if rmax <= heights[r]:
                    rmax = heights[r]
                else:
                    total += (rmax - heights[r])
                r -= 1

        return total
