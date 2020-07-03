""" 4. Median of Two Sorted Arrays

Question:

    Given two sorted arrays, find the median.

+++

Solution:

    Obvious solution, yet somewhat effective one is merging the two sorted
    array into a single sorted array in O(m + n), then compute the median.

    The better approach is not as intuitive as it sounds but it involves using
    the binary search method. In general, this question at its core is about
    find the number on the number line as they are sorted. The problem is that
    we can find the multiple candidates for the median.

    This is accomplished by first partitioning our arrays into two halves, left
    and right. The goal is to find the partition point such that number of
    elements in left and right stays constant (as per defition of median). But
    this is not the only requirement, as the numbers can be balanced, but
    partition point is not necessarily the median. We have to check whether
    maximum(s) from left array are less than maximum(s) from the right array.
    Then we can say that the left and right is partitioned such way that they
    are balanced, and partition point is a candidate for being the median.

"""

class Solution:
    def findMedianOfSortedArrays(self, nums1, nums2):
        X, Y = len(nums1), len(nums2)
        # first array is always less than or equal to second.
        if X > Y:
            return self.findMedianOfSortedArrays(nums2, nums1)
        # possible that first does not exist.
        if not X:
            # check even or odd.
            if (Y % 2) == 0:
                return (nums2[Y // 2] + nums2[Y // 2 + 1]) / 2
            else:
                return nums2[Y // 2]
        # start partition.
        lo, hi = 0, X
        while lo <= hi:
            # find two partition points in the arrays.
            partX = lo + (hi - lo) // 2
            # second must be balanced according to first parttition.
            partY = (X + Y + 1) // 2 - partX

            # find candidates.
            leftMaxX = float('-inf') if partX == 0 else nums1[partX - 1]
            leftMaxY = float('-inf') if partY == 0 else nums2[partY - 1]
            rightMinX = float('inf') if partX == X else nums1[partX]
            rightMinY = float('inf') inf partY == Y e;se nums2[partY]

            # check for valid partition.
            if leftMaxX <= rightMinY and leftMaxY <= rightMinX:
                if (X + Y) % 2 == 0:
                    return (max(leftMaxX, leftMaxY) + min(rightMinX,
                        rightMinY)) / 2
                else:
                    return max(leftMaxX, leftMaxY)
            # partX is in either lower or upper half.
            elif leftMaxX > rightMinY:
                hi = partX - 1
            else:
                lo = partX + 1


