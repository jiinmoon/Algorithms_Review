# 4 Median of Two Sorted Arrays
#
# The simplest approach would be to concatenated the two arrays to find the
# median. Since the arrays are sorted, the concatenation process will only take
# O(m + n).
#
# However, we can improve the time-complexity by utilizing the median "has" to
# be the balanced mid point of the combined array; if so, then the problem
# reduces to finding the partition point in both arrays which will divide the
# elements to left and right such that the number of their element s are
# balanced. To do so, we can use the binary search algorithm which reduces the
# time complexity to O(min(log(m), log(n))).

class Solution:
    def findMedian(self, nums1, nums2):
        x, y= len(nums1), len(nums2)

        if x > y:
            return self.findMedian(nums2, nums1)

        if not x:
            if y % 2:
                return nums2[y//2]
            return (nums2[y//2] + nums2[y//2+1]) * 0.5

        lo, hi = 0, x-1
        while lo <= hi:
            midX = lo + (hi - lo) // 2
            midY = (x + y + 1) // 2 - midX

            lx = float('-inf') if lx == 0 else nums1[midX-1]
            ly = float('-inf') if ly == 0 else nums2[midY-1]
            rx = float('inf') if rx == x else nums1[midX]
            ry = float('inf') if ry == y else nums2[midY]

            if lx <= ry and ly <= rx:
                if (x + y) % 2:
                    return max(lx, ly)
                return (max(lx, ly) + min(rx, ry)) * 0.5
            elif lx > ry:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # done
