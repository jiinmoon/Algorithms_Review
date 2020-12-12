# Matrix Median

Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left
to right.

---

### (1) Merge into 1-D.

We can simply collect all elements into the array size m + n and find the
median right away. O(m * n) in merging process.

### (2) Binary Search min and max values.

First, we find the min and max values which can be found in the matrix first
and last columns in this particular matrix where each row is sorted. Then, we
take the current mid value and iterate on each of the rows to find where the
mid value is found. As we are looking for median, the number of values smaller
than median has to be exactly half or `(m * n + 1) / 2`. If we found that our
count of smaller elements are less than our target, we have to increase our
minValue to put more elements and vice versa. O(m * log(n)) in time complexity
as we have to perform binary search on each of the rows.

---

Python:

```python

from bisect import bisect_right

class Solution:

    def findMedian(self, A):

        m, n = len(A), len(A[0])

        minVal, maxVal = A[0][0], 0

        for row in range(m):
            minVal = min(minVal, A[row][0])
            maxVal = max(maxVal, A[row][n-1])

        target = (m * n + 1) // 2

        while minVal < maxVal:

            midVal = minVal + (maxVal - minVal) // 2
            count = 0

            for row in range(m):
                count += bisect_right(A, midVal)

            if count < target:
                minVal = midVal + 1
            else:
                maxVal = midVal

        return minVal

```
