# 1031 Maximum Sum of Two Non-Overlapping Subarrays

class Solution:
    def maxSum(self, A, L, M):
        x, y = sum(A[M:L+M]), sum(A[L:L+M])
        bx, by = sum(A[:M]), sum(A[:L])
        mbx, mby = bx, by
        maxSum = 0

        for i in range(L+M, A):
            x += A[i] - A[i-L]
            bx += A[i-L] - A[i-L-M]
            mbx = max(mbx, bx)

            y += A[i] - A[i-M]
            by += A[i-L] - A[i-L-M]
            mby = max(mby, by)

            maxSum = max([maxSum, x + mbx, y + mby])

        return maxSum
