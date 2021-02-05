# 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to
hold additional elements from nums2.

---

Since we are given enough space in nums1, we maintain the insertion point as
the sum of the length of nums1 and nums2. From behind, we compare the two
values and insert the larger values onto its insertion point in nums1. If we
have a nums2 elements left over while exhausted the nums1, we simply move over
the leftover elements from nums2. The algorithm is in O(n + m) time complexity
where n and m are the size of the nums1 and nums2 respectively.

---

Python:

```python

class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        ins = m + n - 1
        i, j = len(nums1) - 1, len(nums2) - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[ins] = nums1[i]
                i -= 1
            else:
                nums1[ins] = nums2[j]
                j -= 1
            ins -= 1
        # no more elements left in nums1
        if i < 0:
            nums1[:ins+1] = nums2[:j+1]
```
