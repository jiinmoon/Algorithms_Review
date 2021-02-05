200 Number of Islands
=====================

Question:
---------

Given a 2D grid map of 1s and 0s, count the number of islands. An island is
land (1s) surrounded by water (0s).

Solutions:
----------

We iterate on the 2D grid map - when we encounter a land, we expand in four
directions, marking them as visited until we hit the border or surrounded by
the water.

Codes:
------

Go:

```go
func numIslands(grid [][]byte) int {
    if len(grid) == 0 {
        return 0
    }
    var (
        m = len(grid)
        n = len(grid[0])
        totalIsl = 0
    )
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' {
                totalIsl++
                exploreIslands(grid, i, j)
            }
        }
    }
    return totalIsl
}

func exploreIslands(grid [][]byte, i, j int) {
    if i < 0 || i > len(grid) || j < 0 || j > len(grid[0]) {
        return
    }
    if grid[i][j] != '1' {
        return
    }
    grid[i][j] = '0'
    exploreIslands(grid, i+1, j)
    exploreIslands(grid, i-1, j)
    exploreIslands(grid, i, j+1)
    exploreIslands(grid, i, j-1)
}
```
---

**Source:**

LeetCode: [Number-of-Islands](https://leetcode.com/problems/number-of-islands/)
