""" 1.8 Zero Matrix

Question:

    Write an algorithm such that if an element in an M x N matrix is 0, its
    entire row and column are set to 0.

---

At first glance, intuition is to simply zero the row and column as we
read, but we will fast realize that this will create a problem as we will
overwrite the future information about where to zero.

Thus, we realize that we will first have to scan the matrix first to record
which rows and cols are to be set to 0. To save space, we can actually use the
first rows and cols as a record, given that we take note of whether the first
row and col themselves need to be zero'd or not.

"""

class Solution:

    def zeroMatrix(self, mat):
        if not mat: return mat

        zeroFirstRow = mat
        zeroFirstCol = False

        # determine whether first row/col has a 0.
        zeroFirstRow = 0 in mat[0]
        for i in range(len(mat)):
            if mat[i][0] == 0:
                zeroFirstCol = True
                break

        # check entire matrix for 0s. mark them in first row/col.
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # start zeroing the matrix according to first row/col.
        for i in range(1, len(mat)):
            if mat[i][0] == 0:
                for j in range(0, mat[0]):
                    mat[i][j] = 0

        for j in range(1, len(mat[0])):
            if mat[0][j] == 0:
                for i in range(0, len(mat)):
                    mat[j][i] = 0

        # zero first row/col if necessary.
        if zeroFirstRow:
            for i in range(0, len(mat[0])):
                mat[0][i] = 0

        if zeroFirstCol:
            for j in range(0, len(mat)):
                mat[j][0] = 0

        return mat

