# Median of Array

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by
merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

---

### (1) Merge two.

By merging two arrays in O(m + n) time complexity, we can find the median in O(1).

### (2) Binary Search.

We can find the median by finding the partition point in one array that can
balaned the numbers to its left and right. By doing so, we can find the
candidates for our mid points (4 in total). Time complextiy would be
O(log(min(m, n))) since we only have to perform binary search on smaller array
and we should be able to find the other partition point.

---

Python:

```python

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        
        m, n = len(A), len(B)
        
        if m > n:
            return self.findMedianSortedArrays(B, A)
            
        if not m:
            if n % 2:
                return B[n//2]
            return (B[n//2-1] + B[n//2]) * 0.5
        
        l, r = 0, m
        
        while True:
            
            part1 = l + (r - l) // 2
            part2 = (m + n + 1) // 2 - part1
            
            lm1 = float('-inf') if part1 == 0 else A[part1 - 1]
            lm2 = float('-inf') if part2 == 0 else B[part2 - 1]
            rm1 = float('inf') if part1 == m else A[part1]
            rm2 = float('inf') if part2 == n else B[part2]
            
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
