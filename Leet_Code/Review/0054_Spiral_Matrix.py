""" 54. Spiral Matrix

Question:

    Given a matrix of m x n elements, return all elements of the matrix in
    spiral order.

+++

Solution:

    We would procedurally generate the coords starting from outside towards the
    centre - utilizing the `yield`.

"""

class Solution:
    def spiralOrder(self, matrix)
        m, n = len(matrix)-1, len(matrix[0])-1
        r1, r2 = 0, m
        c1, c2 = 0, n
        
        def spiralCoords(self, r1, r2, c1, c2):
            # Top row -> to right
            for col in range(c1, c2+1):
                yield r1, col
            # Right col -> to bottom
            for row in range(r1+1, r2+1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                # Bottom row -> to left
                for col in range(c2-1, c1, -1):
                    yield r2, col
                # Left col -> to up
                for row in range(r2, r1, -1):
                    yield row, c1
        
        result = []
        while r1 <= r2 and c1 <= c2:
            for row, col in spiralCoords(r1, r2, c1, c2):
                result.append(matrix[row][col])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return result


