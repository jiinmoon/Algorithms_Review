# Rotated Sorted Array Search

Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its
index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.

---

We may still use Binary Search to reduce the size of our search; we can compare
our lo and hi values against the mid element to see which half of the array is
in sorted order - and look to see where target element falls within the range.

O(log(n)) in time complexity.

---

Python:

```python

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        l, r = 0, len(A) - 1
        
        while l <= r:
            
            m = l + (r - l) // 2
            
            if A[m] == B:
                return m
                
            if A[l] <= A[m]:
                if A[l] <= B < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if A[m] < B <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

```
