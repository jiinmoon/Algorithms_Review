""" 59. Spiral Matrix II

Question:

    Given a positive integer, n, generate a square matrix filled with elements
    from 1 to n^2 in spiral order.

+++

Solution:

    Similar approach to previous Spiral Matrxi I question: we would generate
    the spiral coordinates from outside to in.

"""

class Solution:
    def generate_matrix(self, n):
        r1, r2 = 0, n
        c1, c2 = 0, n

        def spiral_coords(r1, r2, c1, c2):
            for col in range(c1, c2):
                yield r1, col
            for row in range(r1+1, r2):
                yield row, c2
            if r1 < r2 and c1 < c2:
                for col in range(c2-2, c1-1, -1):
                    yield r2, col
                for row in range(r2-1, r1, -1):
                    yield row, c1

        result = [[0] * n for _ in range(n)]
        i = 1
        while r1 <= r2 and c1 <= c2:
            for row, col in spiral_coords(r1, r2, c1, c2):
                result[row][col] = i
                i += 1
            r1 += 1; c1 += 1;
            r2 -= 1; c2 -= 1;
        return result

