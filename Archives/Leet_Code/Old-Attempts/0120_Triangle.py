""" 120. Triangle

Question:

    Given a triangle, find the min path sum from top to bottom.

+++

Solution:

    To compute this, we can think of this backwards - that is starting from the
    bottom, the min path cost to reach a certain triangle[i][j] would be the
    value itself plus the minimum value of it's two adjacent neighbours from the
    row below (triangle[i+1][j], triangle[i+1][j+1]).

"""

class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        if len(triangle):
            for i in range(len(triangle)-2, -1, -1):
                for j in range(len(triangle[i])):
                    triangle[i][j] = triangle[i][j] +\
                            min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
