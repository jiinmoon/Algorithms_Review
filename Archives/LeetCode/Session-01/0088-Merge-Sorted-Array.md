# 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough
space to hold additional elements from nums2.

---

We can merge two array in O(m + n) time complexity since two arrays are sorted
already. As we want to move over elements unto nums1, best approach here would
be to insert the new elements from behind and iterate backwards while comparing
elements from both end of the nums1 and nums2.

---

Python:

```python

class Solution88:

    def merge(self, nums1, m, nums2, n):

        i, j, ins = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[ins] = nums1[i]
                i -= 1
            else:
                nums1[ins] = nums2[j]
                j -= 1
            ins -= 1

        # array splice; move over whichever is left over from nums2
        if i < 0:
            nums1[:ins + 1] = nums2[:j + 1]
```

