79 Word Search
==============

Question:
---------

Given a 2D board and a word, find it the word exists in the grid.

Solutions:
----------

We use a path-finding algorithm at each character where the word starts - we
continue the path as long as the characters match up with the word. We need to
iterate the entire board, and each position we start our search up to the
length of the word - thus, O(m * n * w) where w is the length of the word.

Codes:
------

Python:

```python
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        def isValidCoords(x, y):
            return (0 <= x < m) and (0 <= y < n)
        
        def search(index, i, j):
            if index == len(word):
                return True
            if not isValidCoords(i, j) and board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = None
            for nextX, nextY in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
                if search(index+1, nextX, nextY):
                    return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(0, i, j):
                    return True
        return False
```

---

**Source:**

LeetCode: [Word-Search](https://leetcode.com/problems/word-search)
