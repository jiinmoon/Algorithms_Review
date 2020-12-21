# Maximum Sum Combinations

    Given two equally sized 1-D arrays A, B containing N integers each.

    A sum combination is made by adding one element from array A and another
    element of array B.

    Return the maximum C valid sum combinations from all the possible sum
    combinations.

---

## Approach:

We first sort the two given arrays such that we can always select the maximums
from back of the arrays. In order to always select maximum possible sum of
combinations each time upto C, we use heap to maintain our current sum for
chosen pair of indicies from A and B. Thus, top of our stack will always
maintain maximum sum of our choices. We also require additional set or hashmap
to record each of the visited pair such that we do not reselect the same pair
again.

O(n * log(n)) in time complexity as sorting involved.

---

Python:

```python

from heapq import heappop, heappush

class Solution:

    def solve(self, A, B, C):

        A.sort()
        B.sort()

        i, j = len(A) - 1, len(B) - 1
        pq = [(-(A[i] + B[j]), (i, j))]
        seen, result = set(), list()

        for _ in range(C):
            currSum, (i, j) = heappop(pq)

            result.append(-currSum)

            for ni, nj in [(i-1, j), (i, j-1)]:
                if ni >= 0 and nj >= 0 and (ni, nj) not in seen:
                    seen.add((ni,nj))
                    heappush(pq, (-(A[ni] + B[nj]), (ni, nj)))

        return result
```
