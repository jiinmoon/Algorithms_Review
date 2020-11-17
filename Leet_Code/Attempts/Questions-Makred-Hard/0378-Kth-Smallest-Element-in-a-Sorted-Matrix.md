# 378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending
order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

---

Notice the particularity of the this matrix - order is such that rows and cols
are sorted from left to right and top to bottom.

Naive approach would be to simply merge to create a singular list and iterate
to find the Kth smallest element. O(n * m) time and space will be required for
such a method.

Note that matrix is sorted in such a fashion that from leftmost upper corner
towards the rightmost bottom corner. Hence, we may use min heap to efficiently
search for the Kth smallest element by first populate our min heap with first
elements from each of the rows. Then, for K steps, continuously poll from the
min heap and update by expanding to its right. While this is efficient in
average case compared to naive solution, due to K can be the last element, this
will still cost O(n * m) but better space of O(m + n) as we are not maintaining
entire information about matrix.

---

Python:

```python

import heapq

class Solution:
    def findKthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
            return -1

        n = len(matrix)
        # we may only have to start search k row
        minHeap = [(matrix[r][0], (r, 0)) for r in range(min(k, n))]:
        heapify(minHeap)

        for _ in range(k):
            val, pos = heappop(minHeap)
            r, c = pos
            if c < n - 1:
                heappush((matrix[r][c+1], (r,c+1)))

        return val
```
