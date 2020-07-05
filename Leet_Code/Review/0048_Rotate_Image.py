""" 48. Rotate Image

Question:

    Given n x n 2D matrix representing an image, rotate clockwise by 90
    degrees.

+++

Solution:

    We can either try to indexing or to use linear algebra and perform matrix
    transformation via matix multiplication. But simplest would be to simply
    reverse the matrix, and swap the values diagnoally.

"""

class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

