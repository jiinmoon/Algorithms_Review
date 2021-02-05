# Maximum Sum Combinations

Given two equally sized 1-D arrays A, B containing N integers each.

A sum combination is made by adding one element from array A and another
element of array B.

Return the maximum C valid sum combinations from all the possible sum
combinations.

---

First sort the two given arrays A and B. By sorting, we can compute the maximum
by repeating loop upto C times iterating from behind of both arrays. To
determine the current maximum, we use heap. But it is entirely possible that we
have a duplicate pairs chosen - to avoid this, we also use set to record the
previously seen pairs. O(n * log(n)) in time complexity due to sorting involved
and O(n) in space complexity.

---

Python:

```python

from heapq import heappop, heappush

class Solution:

    def maxSumCombinations(self, A, B, C):

        N = len(A)

        A.sort()
        B.sort()

        seen, pq, result = set(), list(), list()
        # starting from last indicies where maximum is gurantee'd
        i, j = N - 1, N - 1
        seen.add( (i,j) )
        # maintain max-heap
        pq.append( (-(A[i] + B[j]), (i,j)) )

        for _ in range(C):
            currSum, (i, j) = heappop(pq)
            result.append(-currSum)
            
            # either decrement i or j for next pairs
            for ni, nj in [(i-1,j),(i,j-1)]:
                if 0 <= ni and 0 <= nj and (ni,nj) not in seen:
                    seen.add( (ni,nj) )
                    heappush(pq, (-(A[ni] + B[nj]), (ni,nj)))

        return result
```
