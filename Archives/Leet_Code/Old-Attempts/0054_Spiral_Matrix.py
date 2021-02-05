""" 54. Sprial Matrix

Question:

    Given a matrix of m x n elements (m rows, n cols), return all elements of
    the matrix in spiral order.

+++

Solution:

    One way to go about it is to generate the coords that go through the matrix
    in spiral manner. This is achieved by keeping track of start, and end rows
    and cols. We can also take advantage of using 'yield' function of Python.

"""

class Solution:
    def sprialOrder(self, matrix):
        if not matrix:
            return []

        result = []
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1

        def sprialCoords(r1, r2, c1, c2):
            for col in range(c1, c2+1):
                yield r1, col
            for row in range(r1+1, r2+1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                for col in range(c2-1, c1, -1):
                    yield r2, col
                for row in range(r2, r1, -1):
                    yield row, c1

        while r1 <= r2 and c1 <= c2:
            for r, c in spiralCoords(r1, r2, c1, cc2):
                result.append(matrix[r][c])
            r1 += 1; c1 += 1
            r2 -= 1; c2 -= 1

        return result

