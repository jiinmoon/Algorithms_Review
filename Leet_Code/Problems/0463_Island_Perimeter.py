""" 463. Island Perimeter

Question:

    Given a 2-D grid where 0 denotes water, and 1 denotes land, determine the
    perimeter of the island.

+++

Solution:

    We can think of it this way. For a island with a single land, it is
    surrounded by 4 waters - thus, it has perimeter of 4. But, when another land
    is attached, while overall perimeter has increased to 6, still it is not
    contributing as much as lands are 'touching'.

    Hence, we iterate on the grid, and for every cell, we would check whether
    the neighbour is a land also. For every non-land mass it has, we can safely
    add to the perimeter value.

"""

class Solution:
    def islandPerimeter(self, grid):
        perimeter = 0
        m, n = len(grid), len(grid[0])

        def isValid(x, y):
            return x == 0 or x == m-1 or y == 0 or y == -1 or not grid[x][y]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for x, y in [ (i+1, j), (i-1, j), (i, j-1), (i, j+1) ]:
                        if isValid(x, y):
                            perimeter += 1
        return perimeter
