# 212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

---

Since there are multiple words to find within the given board, we require an
efficient data structure to store our words to identify the words quickly. For
this purpose, we build prefix-tree or Trie-tree. Then, as we iterate on the
board, we perform word search on each of the node down as far out as possible.

---

Python:

```python

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Solution:
    def wordSearch(self, grid, words):
        def helper(i, j, node):
            if not (0 <= i < m and 0 <= j < n):
                return False
            currChar = grid[i][j]
            if currChar not in node.children:
                return False
            currNode = node.children[currChar]
            if currNode.word:
                result.append(currNode.word)
                currNode.word = None
            grid[i][j] = ""
            helper(i+1, j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i, j-1)
            grid[i][j] = currChar

        if not grid or not grid[0] or not words:
            return []

        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        result = list()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                helper(i, j, root)

        return result
```
