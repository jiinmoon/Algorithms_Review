""" 48. Rotate Image

Question:

    You are given an n x n 2D matrix representing an image; rotate the image by
    90 degrees clockwise.

+++

Solution:

    We could apply linear algebra and do matrix transformation involving trig.
    However, the easiest way to rotate an image would be to simply reverse the
    image, then swap diagonally.

"""

class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

