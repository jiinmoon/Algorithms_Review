""" 240. Search a 2D Matrix II

Question:

    Write an efficient algorithm that searches for a value in an m x n matrix.

    Values in each rows are sorted left to right.

    Values in each cols are sorted top to bottom.

+++

Solution:

    Unlike first problem, the matrix values does not have a well defined range
    row after row - that is, the values ending in top row is not neceesarily
    smaller than the value begining at next row.

    However, this does not stop us from using the same algorithm as the logic
    still holds up. Suppose that we are starting at first row and last col. From
    this location, we can ask whether the target value lies within the row or
    not. If the target value is less than current value, then we have a chance
    that the value lie within the row; move the col inwards. Likewise, if the
    target value is greater than current? Then, we can move over to next row.

"""

class Solution:
    def searchMatrixII(self, matrix, target):
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r <= m-1 and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                col -= 1
            else:
                row += 1
        return False

