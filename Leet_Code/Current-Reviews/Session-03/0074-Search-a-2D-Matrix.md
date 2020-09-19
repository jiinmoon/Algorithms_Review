74 Search a 2D Matrix
=====================

Write an efficient algorithm that searches for a value in an m x n matrix where
it has following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the
  previous row.

---

The particular properties of this matrix makes it such that we can simply treat
this matrix as a single list of all concatenated rows - and perform a binary
search for an efficient search.

The problem is how to map the lo, mid, and hi points of the binary search to
the 2D matrix. This is done by realizing that for the row, it is the mid point
divided by the length of the col; and for the col, it is the mid point moulous
by the length of the col.

The time complexity should be of O(log(n)).

---

Python:

```python

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr = matrix[mid // n][mid % n]
            if curr == target:
                return True
            if curr < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
```


