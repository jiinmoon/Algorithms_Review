# 54 Spiral Matrix

class Solution:
    def spiralMatrix(self, matrix):
        def spiralcoords(r1, r2, c1, c2):
            # top left to right
            for col in range(c1, c2+1):
                yield r1, col
            # right top to bottom
            for row in range(r1+1, r2+1):
                yield row, c2
            if r1 < r2 and c1 < c2:
                # bottom right to left
                for col in range(c2-1, c1-1, -1):
                    yield r2, col
                # left bottom to top
                for row in range(r2, r1, -1):
                    yield row, c1

        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        r1, r2, c1, c2 = 0, m-1, 0, n-1
        res = list()
        while r1 <= r2 and c1 <= c2:
            for r, c in spiralCoords(r1, r2, c1, c2):
                res.append(matrix[r][c])
            r1 += 1; c1 += 1
            r2 -= 1; c2 -= 1

        return res
