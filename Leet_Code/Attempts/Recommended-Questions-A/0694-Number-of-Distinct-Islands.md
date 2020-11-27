# 693. Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as
another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

---

To find the number of distinct islands, we create a set of "relative"
coordinates of all the islands found in uniform manner while traversing on the
given grid. We hash each of the x, y coordinates that we visit.

O(m * n) in time complexity and space.

---

Java:

```java

class Solution {
    
    private Set<Integer> relCoords;

    public int numDistinctIslands(int[][] grid)
    {
        if (grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;
        
        Set<Set<Integer>> result = new HashSet<>();

        for (int i = 0; i < grid.length; i++)
        {
            for (int j = 0; j < grid[0].length; j++)
            {
                if (grid[i][j] == 1)
                {
                    this.relCoords = new HashSet<>();
                    helper(i, j, i, j, grid);
                    if (!this.relCoords.isEmpty()
                        result.add(this.relCoords);
                }
            }
        }

        return result.size();
    }

    private void helper(int i, int j, int i0, int j0, int[][] grid)
    {
        if (i < 0 || j < 0 || i >= this.grid.length || j >= this.grid[0].length || this.grid[i][j] != 1)
            return;
        
        grid[i][j] = 0;
        this.relCoords.add(hash(i - i0, j - j0));
        helper(i+1, j, i0, j0, grid);
        helper(i-1, j, i0, j0, grid);
        helper(i, j+1, i0, j0, grid);
        helper(i, j-1, i0, j0, grid);
    }

    private int hash(int x, int y) { return (x + 5) * 13 + y; }
}

```

Python:

```python

class Solution:
    def numDistinctIslands(self, grid):
        def helper(i, j):
            q = [ (0,0) ]
            for ri, rj in q:
                for ni, nj in [(ri+i+1,rj+j),(ri+i-1,rj+j),(ri+i,rj+j+1),(ri+i,rj+j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                        grid[ni][nj] = 0
                        q.append((ni-i,nj-j))
            return tuple(q)

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        result = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    result.add(helper(i, j))

        return len(result)
```
