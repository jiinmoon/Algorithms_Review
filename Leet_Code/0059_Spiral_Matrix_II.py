""" 59. Sprial Matrix II

Question:

    Given a positive integer n, generate a square matrix filled with elements
    from 1 to n^2 in spiral order.

"""

class Solution:
    def generateSprialMatrix(self, n):
        result = [[0] * n for _ in range(n)]
        r1, r2 = 0, n-1
        c1, c2 = 0, n-1

        def spiralCoords(r1, r2, c1, c2):
            for col in range(c1, c2+1):
                yield r1, col
            for row in range(r1+1, r2+1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                for col in range(c2-1, c1-1, -1):
                    yield r2, col
                for row in range(r2, r1, -1):
                    yield row, c1

        i = 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiralCoords(r1, r2, c1, c2):
                result[r][c] = i
                i += 1
            r1 += 1; c1 += 1;
            r2 -= 1; c2 -= 1

        return result

