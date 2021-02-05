# 417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell
to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.


Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

---

Here, starting from each of the "oceans" edges, we try to explore inwards so
long as height is in increasing order while recording coordinates visited. From
two ocean's visited set, the overlap between two will be the coordinates where
water can flow to either sides.

Time complexity would be O(m x n) as well as space complexity.

---

Java:

```java

class Solution417 {

    private int[][] matrix;

    public List<List<Integer>> pacificAtlantic(int[][] matrix)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return List.of();

        this.matrix = matrix;
        int m = matrix.length, n = matrix[0].length;

        // marks visited coords from each ocean
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];

        // start from edges, explore inwards and mark visited coords
        for (int row = 0; row < m; row++)
        {
            explore(row, 0, Integer.MIN_VALUE, pacific);
            explore(row, n - 1, Integer.MIN_VALUE, atlantic);
        }

        for (int col = 0; col < n; col++)
        {
            explore(0, col, Integer.MIN_VALUE, pacific);
            explore(m - 1, col, Integer.MIN_VALUE, atlantic);
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int row = 0; row < m; row++)
        {
            for (int col = 0; col < n; col++)
            {
                if (pacific[row][col] && atlantic[row][col])
                    result.append(List.of(row, col));
            }
        }

        return result;
    }
    
    private void explore(int x, int y, int prev, boolean[][] ocean)
    {
        if (x < 0 || x >= this.matrix.length || y < 0 || y >= this.matrix[0].length)
            return;

        if (this.matrix[x][y] < prev || ocean[x][y])
            return;
        
        ocean[x][y] = true;

        for (int[] neighbours : new int[][] { {x+1,y}, {x-1,y}, {x,y+1}, {x,y-1} })
            explore(neighbours[0], neighbours[1], this.matrix[x][y], ocean);
    }
}
```
