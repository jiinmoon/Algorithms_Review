# 212 Word Search II

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Solution:
    def wordSearch(self, grid, words):
        def helper(i, j, node):
            if not (0 <= i < m and 0 <= j < n):
                return
            currChar = grid[i][j]
            if currChar not in node.children:
                return
            currNode = node.children[currChar]
            if currNode.word:
                res.append(currNode.word)
                currNode.word = None
            grid[i][j] = 0
            helper(i+1, j, currNode)
            relper(i-1, j, currNode)
            helper(i, j+1, currNode)
            helper(i, j-1, currNode)
            grid[i][j] = currChar

        if not grid or not grid[0] or not words:
            return []

        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
            curr.word = word

        m, n = len(grid), len(grid[0])
        res = list()
        for i in range(m):
            for j in range(n):
                helper(i, j, root)

        return res
