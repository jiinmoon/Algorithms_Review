""" 63. Unique Paths II

Question:

    Same basic set-up as question 62; however, there are obstacles found
    throughout the grid. Find all unique paths that can reach the goal.

+++

Solution:

    DP approach again is valid here, but we have to make adjustment when we
    first set-up our DP grid. Robot cannot move across the obstacles - which
    means that all the blocked paths should contain values of 0. Otherwise, the
    current path should be the path sum from left and above. The time
    complexity remains same, O(m * n).

"""

class Solution:
    def unique_paths_with_obstacles(self, obsGrid):
        m = len(obsGrid)
        if not m:
            return 0
        n = len(obsGrid[0])
        # start/goal == obstacle?
        if obsGrid[0][0] or obsGrid[-1][-1]:
            return 0
        
        dp = [ 0 for _ in range(n+1) ]
        dp[1] = 1

        for row in range(1, m+1):
            new_row = [0]
            for col in range(1, n+1):
                # was previous path an obstacle?
                if obsGrid[row-1][col-1]:
                    new_row.append(0)
                else:
                    new_row.append(new_row[-1] + dp[col])
            dp = new_row

        return dp[-1]
