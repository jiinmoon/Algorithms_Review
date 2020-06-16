""" 221. Maximal Square

Question:

    Given a 2D binary amtrix filled with 0's and 1's, find the largest square
    containing only 1's and return its area.

+++

Solution:

    DP will provide the elegant solution. Let's suppose that DP represents
    maximal length of the square thus far. The way that we can tell whether
    current cell at matrix[i][j] can be extension from previous square is by
    checking whether matrix[i-1][j-1] is 1. If so, then we can potentially have
    updated sqaure.

"""

class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        maxThusFar = 0
        DP = [0] * (n + 1)
        prev = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = DP[j]
                # is current spot an extension of a square?
                if matrix[i-1][j-1]:
                    # possible extension;
                    DP[j] = min(DP[j], DP[j-1], prev) + 1
                    maxThusFar = max(maxThusFar, DP[j])
                else:
                    # it is not, then square length has to be 0.
                    DP[j] = 0
                prev = temp
        return maxThusFar ** 2
