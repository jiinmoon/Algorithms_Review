# 378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending
order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

---

We may approach this problem using a heap - starting from the minmum value
(starting at matrix[0][0]), we maintain a minheap to consider only the minimum
values that we have considered thus far.

Firstable, we initialize min heap by only adding the first element of from each
row of the matrix. Then, as we pop from the heap, we are gurantee'd to always
take a look at minimum value that we have examined thus far. For each values
that we have examined, we also push in additional value to its right. This step
is repeated K times - so that kth element to be removed from this process is
the answer. The time complexity should be at O(m * n) since we do have to
consider examining each of the elements regardless.

---

Python:

```python

import heapq

class Solution:
    def findKthSmallest(self, grid, k):
        if not grid or not grid[0]:
            return -1
        
        n = len(grid)
        # min heap : store starting values on each row
        pq = [(grid[row], (row, 0)) for row in range(n)]

        heapify(pq)

        for _ in range(k):
            curr, pos = heappop(pq)
            row, col = pos
            # if there are values left in this row to consider
            # add to min heap
            if col < n -1:
                heappush(pq, (grid[row][col+1], (row, col+1)))

        return curr
```

