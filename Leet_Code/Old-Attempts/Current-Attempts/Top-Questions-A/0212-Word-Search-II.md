# 212 Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

---

We use Trie structure to enable efficient search of the word in the given tree.
First, we constructure the Trie, then traverse on each cell on the grid,
performing search as we do so.

---

Python:

```python

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Solution:
    def wordSearch(self, words, grid):
        if not grid or not grid[0] or not words:
            return []
        
        m, n = len(grid), len(grid[0])
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        res = list()
        for i in range(m):
            for j in range(n):
                self.search(grid, root, i, j, res)
        return res

    def search(self, grid, node, i, j, res):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return
        currChar = grid[i][j]
        if currChar not in node.children:
            return
        currNode = node.children[currChar]
        if currNode.word:
            res.append(currNode.word)
            currNode.word = None
        grid[i][j] = 0
        self.search(grid, currNode, i+1, j, res)
        self.search(grid, currNode, i-1, j, res)
        self.search(grid, currNode, i, j+1, res)
        self.search(grid, currNode, i, j-1, res)
        grid[i][j] = currChar
```
