# 79. Word Search

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

---

We can approach this problem as a graph traversal problem - particularly path
finding using either DFS or BFS. We simply for each node (or char) in the
board, we explore in 4 directions so long as we can. When we can reach the last
character, we conclude that we can find the word.

---

Python:

```python

class Solution79:

    def wordSearch(self, board, word):

        if not (word and board and board[0]):
            return False

        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n and word[k] != board[i][j]):
                return False
            
            board[i][j] = None
            if any(dfs(ni, nj, k + 1) for (ni, nj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]):
                return True
            board[i][j] = word[k]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
```
