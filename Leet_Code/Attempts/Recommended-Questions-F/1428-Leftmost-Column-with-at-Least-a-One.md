# 1428. Leftmost Column with at Least a One

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of
the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column
index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
-1.

You can't access the Binary Matrix directly.  You may only access the matrix
using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row,
col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which
means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged
Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the
following four examples. You will not have access the binary matrix directly.

---

We can simply iterate on the given matrix row after another - at each row, we
perform binary search to find the index of leftmost position of the 1. Amongst
all these indicies found, the minimum would be returned. The time complexity
would be O(m * log(n)) where m is the length of the row and n is the length of
the cols.

---

Python:


```python

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        m, n = binaryMatrix.dimensions()
        result = float('inf')
        for row in range(m):
            lo, hi = 0, n - 1
            # perform binary search as far out left as possible
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # is found index has One?
            if binaryMatrix.get(row, lo) == 1:
                result = min(result, lo)

        return result if result != float('inf') else -1
```
