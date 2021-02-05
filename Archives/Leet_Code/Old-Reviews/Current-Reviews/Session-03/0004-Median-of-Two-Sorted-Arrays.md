4 Median of Two Sorted Arrays
=============================

Given two sorted arrays, find the median of two merged sorted array.

---

O(m+n) solution involves simply merge the two array into one, and then finding
the median.

However, we can think of this problem as a finding k smallest element or binary
search for a partition point in both the the sorted arrays where it will divide
the arrays evenly. Finding such points will take O(log(n)) time complexity.

---

Python:

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        X, Y = len(nums), len(nums2)

        # maintain smaller array on the left
        if X > Y:
            return self.findMedianSortedArrays(nums2, nums1)

        # smaller array may be is empty
        if not X:
            if Y % 2:
                return nums2[Y // 2]
            return (nums2[Y // 2 - 1] + nums2[Y // 2]) * 0.5

        lo, hi = 0, X 
        while lo <= hi:
            partX = lo + (hi - lo) // 2
            partY = (X + Y + 1) // 2 - partX 
            
            # four candidates based on partition points above
            leftMaxX = float('-inf') if partX == 0 else nums1[partX - 1]
            leftMaxY = float('-inf') if partY == 0 else nums2[partY - 1]
            rightMinX = float('inf') if partX == X else nums1[partX]
            rightMinY = float('inf') if partY == Y else nums2[partY]

            # at this point, partX and partY divides arrays equally to its
            # left and right; but the points chosen may not be the median
            if (leftMaxX <= rightMinY) and (leftMaxY <= rightMinX):
                if (X + Y) % 2:
                    return max(leftMaxX, leftMaxY)
                return (max(leftMaxX, leftMaxY) + max(rightMinX, rightMinY)) * 0.5

            # candidates are not median; binsearch on chosen points
            elif leftMaxX > rightMinY:
                hi = partX - 1
            else:
                lo = partX + 1
```
