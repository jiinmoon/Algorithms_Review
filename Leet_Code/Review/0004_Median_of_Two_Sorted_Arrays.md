[4] Median of Two Sorted Arrays 
===============================

There are two sorted arrays **nums1** and **nums2** of size m and
n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.


**Example 1**:

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

Solution
--------

Naive approach to this problem would be to simply merge the two arrays, and
find the median. This is O(m + n).

Better approach is hinted by the question where it gives its run time
complexity should be logrithmic. In fact, the heart of this problem is finding
the partition point via _binary search algorithm_.

**Python**:

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        X, Y = len(nums1), len(nums2)
        if X > Y:
            return self.findMedianSortedArrays(num2, num1)
        if not X:
            if Y % 2 == 0:
                return (nums2[Y // 2] + nums2[Y // 2 - 1]) / 2
            else:
                return nums2[Y // 2]
        
        lo, hi = 0, X
        while lo <= hi:
            partX = lo + (hi - lo) // 2
            partY = (X + Y + 1) // 2 - partX
            
            leftMaxX    = float('-inf') if partX == 0 else nums1[partX-1]
            leftMaxY    = float('-inf') if partY == 0 else nums2[partY-1]
            rightMinX   = float('inf') if partX == X else nums1[partX]
            rightMinY   = float('inf') if partY == Y else nums2[partY]

            if (leftMaxX <= rightMinY) and (leftMaxY <= rightMinX):
                leftMax = max(leftMaxX, leftMaxY)
                rightMin = min(rightMinX, rightMinY)
                if (X + Y) % 2 == 0:
                    return (leftMax + rightMin) / 2
                else:
                    return leftMax
            elif leftMaxX > rightMinY:
                hi = partX - 1
            else:
                lo = partX + 1
        # error if reaches down here - likely unsorted input.


```

---

LeetCode:
[Median-of-Two-Sorted-Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
