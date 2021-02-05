# 79. Word Search

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
"adjacent" cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.

---

This problem can be approached with graph traversal algorithms - namely DFS or
BFS. Starting from each of the cells where it matches the first character of
the word, we try to search in four directions. Time complexity would be O(n * m * 4^k) where
n and m are sizes of the boards and k is the length of the word to search for.

---

Python: backtracking dfs algorithm.

```python

class Solution79:
    
    def wordSearch(self, grid, word):

        if not (grid and grid[0] and word):
            return False

        m, n = len(grid), len(grid[0])
        
        # backtrack to search in four directions matching at k-th
        def helper(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == word[k]):
                return False
            
            # mark current cell as visited
            grid[i][j] = None

            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if helper(ni, nj, k + 1):
                    return True

            # restore the cell for other possible paths
            grid[i][j] = word[k]

            return False


        for i in range(m):
            for j in range(n):
                if grid[i][j] == word[0] and helper(i, j, 0):
                    return True

        return False
```
