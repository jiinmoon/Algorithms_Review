1031 Maximum Sum of Two Non-Overlapping Subarrays
=================================================

Given an array A of non-negative integers, return the maximum sum of elements
in two non-overlapping (contiguous) subarrays, which have lengths L and M.
(For clarification, the L-length subarray could occur before or after the
M-length subarray.)

---

Let us consider two subarray of size L and M, which are named X and Y.

We can have array A such as follows:

    [ 1 2 3 4 5 6 7 8 9 ]

Suppose that L = 3 and M = 2, then our subarray can be

    [ 1 2 [ 3 4 5 ] 6 7 8 9 ]   ==> X = [ 3 4 5 ]
    [ 1 2 3 [ 4 5 ] 6 7 8 9 ]   ==> Y = [ 4 5 ]

Now, notice that before each of these subarrays, we have another subarrays
which are convinentely sized for us to consider, `[ 1 2 ]` before X and `[
1 2 3]` before Y.

Thus, we consider these two as we slide the subarray along. First encounter
will be the element `6`, and they will be added to both of our subarray, and
its end will be decremented - as well as reflected on the subarrays appearing
before our subarraies.

    [ 1 [ 2 3 ] [ 4 5 6 ] 7 8 9 ]
    [ 1 [ 2 3 4 ] [ 5 6 ] 7 8 9 ]

Hence, we can see that our result will the maximum of either cases. Since it is
possible that our non-overlapping arrayes can be spread far apart **we maintain
the maximum of the sum of subarray**.

The time complexity should be linear O(n).

---

Python:

```
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        res = sum(A[:L + M])
        
	X, Y = sum(A[M:L + M]), sum(A[L:L + M])
        beofreX, beforeY = sum(A[:M]), sum(A[:L])
        mxBeforeX, mxBeforeY = beforeX, beforeY
        
        for i in range(L + M, len(A)):
            X += A[i] - A[i - L]
            beforeX += A[i - L] - A[i - L - M]
            mxBeforeX = max(mxBeforeX, beforeX)
            
            Y += A[i] - A[i - M]
            beforeY += A[i - M] - A[i - L - M]
            mxBeforeY = max(mxBeforeY, beforeY)
        
	    res = max(res, X + mxBeforeX, Y + mxBeforeY)
        
        return res
```
