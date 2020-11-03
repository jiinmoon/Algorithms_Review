# 212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

---

It would be naive to approach this problem as we iterate on the given board,
and iterate on each of the words to confirm whether there is word on the board.
The better approach would be to convert the list of words into more accessible
dictionary structure such as Trie. Then, it would be a simple recursive
traversal on each of the cell to explore as far as possible while checking to
see whether current character exist in the Trie.

---

Python:

```python

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = dict()

class Solution:
    def wordSearch(self, board, words):
        def helper(i, j, node):
            if not (0 <= i < m and 0 <= j < n):
                return
            currChar = board[i][j]
            if currChar not in node.children:
                return
            currNode = node.children[currChar]
            if currNode.word:
                result.append(currNode.word)
                currNode.word = None
            board[i][j] = "#"
            helper(i+1, j, currNode)
            helper(i-1, j, currNode)
            helper(i, j+1, currNode)
            helper(i, j-1, currNode)
            board[i][j] = currChar

        if not board or not board[0] or not words:
            return []

        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        result = list()
        for i in range(m):
            for j in range(n):
                helper(i, j, root)

        return result
