""" 74. Search a 2D Matrix

Question:

    Write an efficient algorithm that searches for a value in an m x n matrix.
    This matrix has following properties:

        1. Integers in each row are sorted from left to right.
        2. The first integer of each row is greater tha nthe last integer of
           the previous row.

+++

Solution:

    If we change our starting search poisition, it becomes O(m + n) time
    complextiy algorithm to search. Let's start at top right corner. From here,
    we can check whether the target number lies within the row or not. If it
    does, we move down a column. If it is not, then we move downwards.

    However, we can make improvement further by treating this 2D matrix as a 1D
    list, and use the binary search algorithm since the particularity of matrix
    allows us so.

"""

class Solution:
    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            value = matrix[mid // n][mid % n]

            if target == value:
                return True
            elif target > value:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

