""" 211. Add and Search Word

Question:

    Design a data structure that supports the following two operations.

        addWord and search.

    search should be able to support a regular expression string containing '.'.

+++

Solution:

    Trie structure would be fine for this problem. However, search requires a
    recursive backtracking for whenever we encounter '.', we need to explore all
    chars in current depth to see whether word exists.

"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, pattern):
        return self._search(self.root, pattern, 0)

    def _search(self, curr, pattern, index):
        if not curr:
            return False
        if index == len(pattern):
            # end is reached, isWord?
            return curr.isWord
        # current pattern character to match.
        matchChar = pattern[index]
        # two choices, either char is '.' or not.
        if matchChar == '.':
            # if it is a wildcard, then we need to recursively explore all
            # possible characters from current node's children.
            for child in currNode.children.values():
                return self._search(child, pattern, index + 1)
        # if it is not, then we recur only on next correct child.
        return self._search(curr.children.get(matchChar), pattern, index + 1)
