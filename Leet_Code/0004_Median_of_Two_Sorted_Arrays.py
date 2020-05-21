""" 4. Median of Two Sorted Arrays

Question:

    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity
    should be o(lg (m + n)).

+++

Solution:

    First naive solution would be to combine two lists in to one in O(m + n)
    time complexity, then find the median.

    The better approach would be in realizing that we are trying to partition
    given two arrays into two equal halves - let's call it left and right, such
    that every element on the left would be less than elements on the right.

    Then, this becomes a simple question of finding the partition points in two
    lists - but if we know one of the partition point, then another one should
    follow automatically to balance the number of elements to left and right.

    partX + partY = (len(X) + len(Y) + 1) // 2

    Suppose we have two lists of integers:

        X = [ x1, x2, x3 ]
        y = [ y1, y2, y3, y4, y5 ]

    We first choose our partition point at X, then we divide the x and y in to
    left and right.

        x1              |       x2, x3
        y1, y2, y3      |       y4, y5

    Once balanced, there are four candidates that can be considered as a 'mid'
    point. These are x1, y3, x2, and y4. To be considered as valid partition, x1
    has to be <= y4 and y3 <= x2. If satisfied, then we can take either max(x1,
    y3) or min(x2, y4).

    The runtime becomes O(lg (m+n)) since finding that partition point can be
    done with binary search algorithm.

"""

class Solution:
    def medianOfTwo(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        X, Y = len(nums1), len(nums2)
        # maybe the case that one of list is empty.
        # then X would not exist.
        if not X:
            if Y % 2 == 0:
                return (nums2[Y//2] + nums2[Y//2 -1]) // 2
            else:
                return nums2[Y//2]
        lo, hi = 0, X
        while lo <= hi:
            # partition points
            partX = lo + (hi - lo) // 2
            partY = (X + Y + 1) // 2 - partX

            # four mid value candidates
            leftMaxX = float('-inf') if partX == 0 else nums1[partX - 1]
            leftMaxY = float('-inf') if partY == 0 else nums2[partY - 1]
            rightMinX = float('inf') if partX == X else nums1[partX]
            rightMinY = float('inf') if partY == Y else nums2[partY]

            # check left <= right?
            if leftMaxX <= rightMinY and leftMaxY <= rightMinX:
                if (X + Y) % 2 == 0:
                    return (max(leftMaxX, leftMaxY) + min(rightMinX, rightMinY)) / 2
                else:
                    return max(leftMaxX, leftMaxY)
            elif leftMaxX > rightMinY:
                # still need to move X to right.
                hi = partX - 1
            else:
                lo = partX + 1
