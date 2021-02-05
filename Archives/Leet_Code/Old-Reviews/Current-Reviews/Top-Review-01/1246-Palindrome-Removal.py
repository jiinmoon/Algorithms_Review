# 1246 Palindrome Removal

from functools import lru_cache

class Solution:
    def minMoves(self, A):

        @lru_cache(None)
        def helper(i, j):
            if i > j:
                return 0

            # removing subarrays size 1
            minMoves = helper(i, j - 1) + 1
            
            # removing last two indicies together
            if A[j] == A[j-1]:
                minMoves = min(minMoves, helper(i, j-2) + 1)
            
            # any duplicate? break up array
            for k in range(i, j-1):
                if A[j] == A[k]:
                    minMoves = min(minMoves, helper(i, k-1) + helper(k+1, j-1))

            return minMoves

        return helper(0, len(A)-1)
