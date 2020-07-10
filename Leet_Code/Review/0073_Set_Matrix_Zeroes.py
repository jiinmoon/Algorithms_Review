""" 72. Set Matrix Zeroes

Question:

    Given a m x n matrix, if an element is 0, set its entire row nad column to
    0. Do it in-place.

+++

Solution:

    We cannot just simply go ahead and set 0 as we iterate on the given matrix
    - we will lose information about which row, col to zero out and eventually
      zero out entire matrix. Thus, we need to mark the rows and cols where we
      should zero them.

    Hence, on our first iteration, we should record the positions of zeros
    - and mark the rows and cols. We do not have to use extra data structure
      as we can use the first row and col - so long as we have recorded whether
      there is a zero in first row/col.

    Then, we iterate once again to zero the marked rows and cols including the
    first row and first col.

"""

class Solution:
    def set_zeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zeroFirstRow = 0 in matrix[0]
        zeroFirstCol = 0 in [ matrix[i][0] for i in range(m) ]

        for row in range(1, m):
            for col in range(1, n):
                if not matrix[row][col]:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if zeroFirstRow:
            for col in range(n):
                matrix[0][col] = 0

        if zeroFirstCol:
            for row in range(m):
                matrix[row][0] = 0

