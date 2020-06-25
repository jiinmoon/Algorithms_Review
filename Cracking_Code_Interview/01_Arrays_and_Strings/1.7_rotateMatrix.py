""" 1.7 Rotate Matrix

Question;

    Given an image represented by an N x N matrix, where each pixel in the
    image is 4 bytes, write a method to rotate the image by 90 degrees. Is this
    doable in-place?

---

Suppose that we have given this matrix; this would be represented in the 2-D
array where each cell is occupied by 4 byte.

To solve this mathmatically, we can use the linear algebra and matrix
transformation via rotating the matrix by using matrix multiplication. Of
course, this is undesirable as it involves not only the trig functions, but also
the matrix multiplication is a heavy on computation time.

Then, the first approach would be mechanical one where we approach this
layer-by-layer, computing the coord for each cell will be transformed into.

However, the better method would be noticing that we are dealing with square
matrix, and it follows a certain pattern when we are doing the rotation.

1 2 3       7 4 1
4 5 6   >   8 5 2
7 8 9       9 6 3

First, we flip the rows (reverse the rows):

    1 2 3       7 8 9
    4 5 6   >   4 5 6
    7 8 9       1 2 3

Then, we invert the matrix diagonally:

    7 8 9       7 4 1
    4 5 6   >   8 5 2
    1 2 3       9 6 3

"""


class Solution:

    def rotateMatrix_1(self, mat):
        """ computing the coord approach  """
        n = len(mat)
        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                tempNum = mat[i][j] # save current cell (top)
                mat[i][j] = mat[n - i - 1][j] # move right to top
                mat[n - j - 1][i] = mat[n - 1 - i][n - 1 - j]
                mat[n - i - 1][n - 1 - j] = mat[j][n - 1 - i]
                mat[j][n - 1 - i] = temp

