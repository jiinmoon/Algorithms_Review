# 1031 Maximum Sum of Two Non-Overlapping Subarrays

Maintain subarray from L to L + M and M to L + M. As we iterate forward, add
and remove from the subarray. Compute the max sum as we do.

---

Python:

```python

class Solution:
    def maxSumOfTwoSubarrays(self, A, L, M):
        x, y = sum(A[M:L+M]), sum(A[L:L+M])
        bx, by = sum(A[:M]), sum(A[:L])
        maxbx maxby = bx, by
        maxSum = 0

        for i in range(L+M, len(A)):
            x += A[i] - A[i-L] 
            bx += A[i-L] - A[i-L-M]
            maxbx = max(maxbx, bx)

            y += A[i] - A[i-M]
            by += A[i-M] - A[i-L-M]
            maxby = max(maxby, by)

            maxSum = max(maxSum, x + maxbx, y + maxby)

        return maxSum
```
