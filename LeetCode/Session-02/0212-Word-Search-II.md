# 212. Word Search II

Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

---

Naive method would involve starting from each of the cells, we exhaustively
check and search for all the matching words which would bound our time
complexity to not only the size of the board but also the number of words and
the length of the words.

We can improve this by combining our DFS search algorithm with Trie structure,
so that for each depth of our recursive search function, we also maintain the
Trie node of our currently matching character. By doing so, we can easily
identify whether we hvae a matching character by checking the node's flag
without having to exhaustively search for all given list of string words.

---

Python:

```python

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.word = None


class Solution212:

    def findWords(self, words, board):

        if not (board and board[0] and words):
            return []

        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                curr = curr.children.setdefault(char, TrieNode())
            curr.word = word

        m, n = len(board), len(board[0])
        result = []


        def explore(i, j, node):
            if not (0 <= i < m and 0 <= j < n and board[i][j] in node.children):
                return

            currChar = board[i][j]
            currNode = node.children[currChar]
            if currNode.word:
                result.append(currNode.word)
                currNode.word = None

            board[i][j] = None
            explore(i+1, j, currNode)
            explore(i-1, j, currNode)
            explore(i, j+1, currNode)
            explore(i, j-1, currNode)
            board[i][j] = currChar


        for i in range(m):
            for j in range(n):
                explore(i, j, root)

        return result
```
