# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

---

#### (1) Dynamic Programming with 2-D array.

Intuitive solution would be to use DP. We define dp at follows:

    Let DP at (i, j) be a minimum path sum found thus far. To compute the min
    path sum at (i, j) it depends upon previous values from left and up which
    are dp[i-1][j] and dp[1][j-1].

        DP[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

This would be O(m * n) in time complexity and in space complexity.

#### (2) Dynamic Programming with 1-D array.

We can make further improvement on the previous as we always have previous rows
information as our current row's dp. Hence, all we ever require is a 1-D array
instead.
 
    DP[j] is DP[i-1][j] and DP[j-1] is DP[i[j-1]. Thus,

        DP[j] = min(DP[j-1], DP[j]) + grid[i-1][j-1]

This reudces space complexity down to O(n).

#### (3) Dynamic Programming with O(1) space.

We can further reduce the space complexity completely as we can use the given
array in-place. We initialize the first row and col as a single path to right
and down.

    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

By doing so, we no longer requires any space. This is only possible if given
array can be modified.

---

Java: DP no space.

```java

class Solution64 {

    public int minPathSum(int[][] grid)
    {
        int m = grid.length, n = grid[0].length;
        
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // initalize first row (path sum to right)
                if (i == 0 && j != 0)
                    grid[i][j] += grid[i][j-1];

                // initalize first col (apth sum to down)
                if (i != 0 && j != 0)
                    grid[i][j] += grid[i-1][j];
                
                // otherwise, update as min of two previous paths
                if (i != 0 && j != 0)
                    grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }

        return grid[m-1][n-1];
    }
}

```

Java: DP 1-D array.

```java

class Solution64 {

    public int minPathSum(int[][] grid) {
        
        int[] dp = new int[grid[0].length + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[1] = 0;
        
        for (int i = 1; i < grid.length + 1; i++)
        {
            for (int j = 1; j < grid[0].length + 1; j++)
                dp[j] = Math.min(dp[j], dp[j-1]) + grid[i-1][j-1];
        }
        
        return dp[dp.length-1];
    }
}
```
