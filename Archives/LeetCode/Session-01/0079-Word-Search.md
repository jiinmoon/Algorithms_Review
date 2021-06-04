# 79. Word Search

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
"adjacent" cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.

---

We can approach this problem as a graph traversal or path finding problem where
starting from a cell which matches the first character of the target word, we
explore as far out as possible so long as word can be matched. To do so, we can
use either DFS or BFS algorithm which has O(v + e) time complexity.

---

Python:

```python

class Solution79:

    def exist(self, board, word):
        
        # dfs
        def explore(i, j, k):
            if k >= len(word):
                return True
            if not (0 <= i < m and 0 <= j < n and board[i][j] == word[k]):
                return False
            board[i][j] = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if explore(ni, nj, k + 1):
                    return True
            board[i][j] = word[k]
            return False
        
        if not (board and board[0] and word):
            return False

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j, 0):
                    return True

        return False
```



