""" 62. Unique Paths

Question:

    A robot is located at the top-left corner of a m x n grid. The robot can
    move only right or down, and is trying to reach the bottom-right corner.
    How many possible unique paths are there?

+++

Solution:

    Another approach is utilizes DP. Define  DP[i][j] as maximum number of
    paths to reach grid at (i, j). Then, it depends on previous steps which are
    (i-1, j) and (i, j-1).

    We can further make imporvement on this by realizing that we can compute
    this row-by-row. Hence, all we need to keep track of is the each row that
    we are working with - and build the new row to replace the previous one.
    This reduces the space complexity by O(n_.

"""

class Solution:
    def unique_paths(self, m, n):
        prev_row = [ 1 for _ in range(n) ]
        
        for row in range(m-1):
            new_row = [1]
            for col in range(1, n):
                # current row cell comes from its prevous and above.
                new_row.append(new_row[-1] + prev_row[col])
            prev_row = new_row

        return prev_row[-1]

