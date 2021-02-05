# 74 Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, (m * n) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr = matrix[mid // n][mid % n]

            if curr == target:
                return True
            elif curr < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
