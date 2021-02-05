# K Largest Elements

    Given an 1D integer array A of size N you have to find and return the B largest
    elements of the array A.

    NOTE:

    Return the largest B elements in any order you like.

---

## Approach:

Use max-heap to maintain the largest element on the top of the heap. Remove top
B elements. O(max(B * log(N), N)) in time complexity as we have to perform heap rebuild
operation B number of times and heapify costs O(N).

---

Python:

```python

from heapq import nlargest, heapify, heappop

class Solution:

    def solve(self, A, B):
        return nlargest(B, A)
    
    # since above solution hides much detail, here we expand out
    def solve2(self, A, B):
        
        # create a max-heap
        # Python heapq is a min-heap by default; hence, we negate to reverse
        A = [-num for num in A]

        # heapify costs O(n) to push largest to the top
        heapify(A)

        # return B largest from heap; each heappop costs O(log(n))

        return [-heappop(A) for _ in range(B)]
```

