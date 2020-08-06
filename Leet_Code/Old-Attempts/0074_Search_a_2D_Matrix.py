""" 74. Search a 2D Matrix

Question:

    Write an efficient algorithm that searches for a value in an m x n matrix,
    where the values are sorted from left to right; and first integer of each
    row is greaterh than the last integer of the previous row.

+++

Solution:

    Because of how this matrix is ordered, we may search the matrix in a fashion
    that we can begin in top right corner. This is because at this starting
    position, we can check for boundary conditions which is, if the target value
    is less than current value, then we know it lies within the same row.
    Otherwise, we are safe to move onto the next column.

"""

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr > target:
                c -= 1
            else:
                r += 1
        return False

