# 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

---

#### (1) Merge and find median.

Simple approach would be to merge the two given array as a single sorted array.
As two given arrays are already in sorted order, merging process would be
linear O(m + n) and finding median would be constant operation. This would
require O(m + n) space.

#### (2) Binary Search for partition points.

Since two arrays are sorted, there exists two partition points in two arrays
where they will be considered as mid-points of the merged array. To fit this
criteria, the partition points has to balance the array into equal parts to its
left and right in the supposed "merged" array and their orders must also
matter. This can achieve O(log(min(m, n))) time complexity without additional
space required.

---

Python: merge first, then find median.

```python

class Solution4:

    def findMedianSortedArrays(self, nums1, nums2):

        nums1 += nums2
        nums1.sort()        # as arrays are already sorted; sorting in O(n)

        if len(nums1) % 2:
            return nums1[len(nums1)//2]
        return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2]) * 0.5
```

Python: binary search.

```python

class Solution4:

    def findMedianSortedArrays(self, nums1, nums2):

        # choose smaller array to perform binary search
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        if not m:
            if n % 2:
                return nums2[n//2]
            return (nums2[n//2-1] + nums2[n//2]) * 0.5

        l, r = 0, m
        
        # Median is gurantee'd to exist
        while True:
            
            # balance elements to left and right
            part1 = l + (r - l) // 2
            part2 = (m + n + 1) // 2 - part1
            
            # 4 candidate about partition points
            lm1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            lm2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            rm1 = float('inf') if part1 == m else nums1[part1]
            rm2 = float('inf') if part2 == n else nums2[part2]

            if lm1 <= rm2 and lm2 <= rm1:
                lmax = max(lm1, lm2)
                rmin = min(rm1, rm2)
                if (m + n) % 2:
                    return lmax
                return (lmax + rmin) * 0.5
            elif lm1 > rm2:
                r = part1 - 1
            else:
                l = part1 + 1
```
