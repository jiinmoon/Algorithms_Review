# Search in Bitonic Array

Given a bitonic sequence A of N distinct elements, write a program to find
a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing
then after a point strictly decreasing.

---

First, we find the peak element where it marks the beginning of decending
sequence with binary search algorithm. So long as our mid point is in ascending
or decending path, we move over; otherwise, we have our peak element. Divide
the array into two sorted halves and perform regular binary search.

---

Python:

```python

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        def binSearch(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        # find peak to divide the array into two sorted arrays
        l, r = 0, len(A) - 1
        
        while l < r:
            m = l + (r - l) // 2
            if A[m-1] < A[m] < A[m+1]:
                l = m + 1
            elif A[m-1] > A[m] > A[m+1]:
                r = m - 1
            else:
                break
        
        nums1, nums2 = A[:m+1], A[m+1:][::-1]
        ans = binSearch(nums1, B)
        if ans != -1:
            return ans
        ans = binSearch(nums2, B)
        if ans != -1:
            return len(A) - ans - 1
        return -1
```
