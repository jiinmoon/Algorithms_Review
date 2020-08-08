200 Number of Islands
=====================

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.
 

Example 1:

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

Example 2:

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

---

Iterate on the given grid, and whenever we encounter land, we explore as far
out as possible while marking the land as visited. 

---

Go:

```go
func numIslands(grid [][]byte) int {
    if len(grid) == 0 {
        return 0
    }
    var (
        m = len(grid)
        n = len(grid[0])
        total = 0
    )
    for i in range(m) {
        for j in range(n) {
            if grid[i][j] == '1' {
                exploreIsl(grid, i, j, m, n)
                total++
            }
        }
    }
    return total
}

func exploreIsl(grid [][]byte, i, j, m, n int) {
    if i < 0 or i >= m or j < 0 or j >= n {
        return
    }
    if grid[i][j] != '1' {
        return
    }
    grid[i][j] = '0'
    exploreIsl(grid, i+1, j, m, n)
    exploreIsl(grid, i-1, j, m, n)
    exploreIsl(grid, i, j+1, m, n)
    exploreIsl(grid, i, j-1, m, n)
}
```

