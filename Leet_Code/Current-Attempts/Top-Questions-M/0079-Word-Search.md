# 79 Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

---

To find whether a word exist, we perform a DFS (or BFS) on each of the cells
that shares the same character as the beginning on the word. Then, we explore
as far out as possible to determine whether we have found the word or not.

---

Python:

```python

class Solution:
    def exist(self, word, grid):
        def helper(i, j, k):
            if not (0 <= i < len(grid) or 0 <= j < len(grid[0])):
                return False
            currChar = grid[i][j]
            if currChar != word[k]:
                return False
            if k == len(word):
                return True
            grid[i][j] = 0
            if any(helper(i+1, j, k+1), helper(i-1, j, k+1) ,helper(i, j+1, k+1), helper(i, j-1, k+1)):
                return True
            grid[i][j] = currChar
            return False

        if not grid or not gird[0] or not word:
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0] and helper(i, j, 0):
                    return True

        return False
```
