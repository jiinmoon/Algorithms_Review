212 Word Search II
==================

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

 

Example:

```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```
 
Note:

- All inputs are consist of lowercase letters a-z.
- The values of words are distinct.

---

By default, using the given list of words is going to be ineifficient due to
how we cannot access the words with ease. We will convert the list of words to
search into a Trie structure where we can easily confirm whether the given char
is in the node or not. This would be O(m * n * k) time complexity where k is
the length of the longest word.

---

Python:

```python
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def findWords(self, board, words):
        # construct Trie
        root = TrieNode():
        for word in words:
            curr = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        # iterate on the board, and search on each cell.
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.searchWord(board, root, i, j, res)
        return res

    def searchWord(board, node, i, j, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        currChar = board[[i][j]
        if currChar not in node.children:
            return
        
        curr = node.children[currChar]
        if curr.word:
            res.append(curr.word)
            curr.word = None

        board[i][j] = 0
        for nexti, nextj in [ (i+1, j), (i-1, j), (i, j+1), (i, j-1) ]:
            self.serachWord(board, curr, nexti, nextj, res)
        board[i][j] = currChar
```

