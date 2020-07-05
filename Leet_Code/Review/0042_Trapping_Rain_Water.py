""" 42. Trapping Rain Water

Question:

    Given n non-negative itegers representing an elevation map where the wdith
    of each bar is 1, compute how much water it is able to trap after raining.

+++

Solution:

    The question becomes manageable once we start asking how much water does
    each cell holds, and then add the total. The amount of water that each of
    the cell can hold depends upon the min of surrounding bars heights and its
    own bar height. The problem is that for each cell, we need to iterate to
    find its left and right maximum heights. We can improve upon this by first
    iterate on the array to record left max heights and right max heights such
    that we can use it fast.

"""

class Solution:
    def trap(self, heights):
        left_maxes = heights.copy()
        right_maxes = heights.copy()

        for i in range(1, len(leftmaxes)):
            left_maxes = max(left_maxes[i], left_maxes[i-1])


        for i in range(len(right_maxes)-2, -1, -1):
            right_maxes[i] = max(right_maxes[i], right_maxes[i+1])

        total = 0
        for i in range(1, len(heights)):
            total += min(left_maxes[i] - right_maxes[i]) - heights[i]

        return total
