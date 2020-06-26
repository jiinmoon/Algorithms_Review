""" Rotate Image

Solution:

    We could apply linear algebra and perform matrix transformation to rotate
    the given matrix to 90 degrees counter clock-wise. However, the cost of
    performing matrix multiplication would be too high. A trick to this problem
    is to realize that you may reverse the matrix first, then swap the values
    diagonally.

"""

class Solution:
    def rotateImage(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
