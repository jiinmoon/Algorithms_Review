# 212. Word Search II

Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

---

We require an efficient structure that stores each of the words and check their
characters; otherwise, our backtracking algorithm to search for the words will
have to repeat for the size of the given list of words. To do so, we can use
Trie.

Time complexity would be O(m * n * 4 ^ k) where m and n are dimensions of the
given board and k is the length of the word - there are 4 directions to search
for. Also, we would require O(k) space to build our Trie structure.

---

Python:

```python

class TrieNode:

    def __init__(self):
        
        self.children = dict()
        self.word = None


class Solution212:

    def findWords(self, board, words):

        if not (board and board[0] and words):
            return []

        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                curr = curr.children.setdefault(char, TrieNode())
            curr.word = word

        m, n, result = len(board), len(board[0]), []

        def search(i, j, node):
            if not (0 <= i < m and 0 <= j < n and board[i][j] in node.children):
                return

            currChar = board[i][j]
            currNode = node.children[currChar]

            if currNode.word:
                result.append(currNode.word)
                currNode.word = None

            board[i][j] = 0
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                search(ni, nj, currNode)
            board[i][j] = currChar


        for i in range(m):
            for j in range(n):
                search(i, j, root)

        return result
```
