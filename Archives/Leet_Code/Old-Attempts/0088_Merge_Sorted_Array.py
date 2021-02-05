""" 88. Merge Sorted Array

Question:

    Given two sorted integer arrays, merge them into a single array.

"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        # assume nums1 has enough space to hold additional elements.
        first = m - 1
        second = n - 1
        for i in range(len(nums1)-1, -1, -1):
            if second < 0:
                break
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[i] = nums1[first]
                first -= 1
            else:
                nums1[i] = nums2[second]
                second -= 1
