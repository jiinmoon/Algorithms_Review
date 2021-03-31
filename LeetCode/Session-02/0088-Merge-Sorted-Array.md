# 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough
space to hold additional elements from nums2.

---

As nums1 have sufficient enough space to hold all the elements from combined
arrays, we can try to insert the new elements by comparing the elements from
behind which comes from two original arrays. This would be a simple process of
maintaining the insertion pointer which can be completed in O(m + n) time
complexity. There is an exceptional case where we have uneven number of
elements - in which case, we move over all the elements from 2 to 1.

---

Python:

```python

class Solution88:

    def mergeSortedArray(self, nums1, nums2, m, n):

        ins = m + n - 1
        i, j = m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[ins] = nums1[i]
                i -= 1
            else:
                nums1[ins] = nums2[j]
                j -= 1
            ins -= 1

        if i < 0:
            # list splicing
            nums1[:ins+1] = nums2[:j+1] 
```
