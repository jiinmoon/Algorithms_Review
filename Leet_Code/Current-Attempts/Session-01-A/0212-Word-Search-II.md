# 212 Word Search II

Use TrieNode for efficient search of the words.

---

Python:

```python

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Solution:
    def search(self, grid, words):
        if not grid or not grid[0]:
            return []

        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        res = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.helper(grid, root, i, j, res)

        return res

    def helper(self, grid, node, i, j, res):
        if (0 <= i < len(grid) or 0 <= j < len(grid[0])):
            return
        currChar = grid[i][j]
        if currChar not in node.children:
            return
        currNode = node.children[currChar]
        if currNode.word:
            res.append(currNode.word)
            word = None
        grid[i][j] = 0
        self.helper(grid, currNode, i+1, j, res)
        self.helper(grid, currNode, i-1, j, res)
        self.helper(grid, currNode, i, j+1, res)
        self.helper(grid, currNode, i, j-1, res)
        grid[i][j] = currChar
```

