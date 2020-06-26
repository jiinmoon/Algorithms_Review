""" 73. Set Matrix Zeroes

Question:

    Given a m x n matrix, if an element is 0, set its entire row and col to 0.
    Do this in-place.

"""

class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        zeroFirstRow = 0 in matrix[0]
        zeroFirstCol = 0 in [matrix[i][0] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if zeroFirstRow:
            for i in range(n):
                matrix[0][i] = 0

        if zeroFirstCol:
            for i in range(m):
                matrix[i][0] = 0
