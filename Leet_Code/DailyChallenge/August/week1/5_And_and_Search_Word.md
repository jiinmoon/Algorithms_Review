# LeetCode Daily Challenge: August Week.1 - Day.5

## Question

Design a data structure that supports the following two operations.

    void addWord(word)
    bool search(word)

`search` word can contain any character or '.' which represents any character.

## Solution

The problem is not difficult except dealing with the '.'. Typically, adding and
saerching data structure makes one think of hashmap structure. We may use
a Trie structure backed up by a hashmap. The idea is that this would be a tree
structure where each TrieNode contains a hashmap of itself and a boolean to
denote whether a word is in it.

Thus, when we add a word, we iterate on its character, we create new TrieNode
and move down to its children. When we arrive at last char, we mark the current
node as one of word (i.e. isWord == True).

Searching can be done iteratively as we only have to iterate on the given word
char by char, and check whether we arrive at the TrieNode where its isWord flag
is set to true. However, '.' wildcard makes it such that whenever we encounter
it, we have to recursively explore all the paths downstream.

A simpler approach would be to simply store the length of the word, and a list
of characters in the haspmap as key-value pair. When we search for a word, we
retrieve all the lists of words of same length, and perform matching. If the
current char does not match or the pattern is not '.', then we know that we
need to explore other word. This will take O(n * k) where k is the length of
the longest word.


Python: Trie approach

```python
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word):
        node = self.root
        return _search(node, word, 0)

    def _search(self, node, pattern, index):
        if not node:
            return False
        if index == len(pattern):
            return node.isWord
        currChar = pattern[index]
        if currChar == '.':
            for child in node.children.values():
                return self._search(child, pattern, index+1)
        return self._search(node.children[currChar], pattern, index+1)
```

Python: Hashmap with length of word as key and a list of words value.

```python
from collections import defaultdict

class WordDictionary:
    def __init__(self):
        self.words = defaultdict(list)

    def add(self, word):
        self.words[len(word)].append(word)

    def search(self, word):
        for currWord in self.words[len(word)]:
            for i, char in enumerate(currWord):
                if word[i] != '.' and word[i] != char:
                    break
                else:
                    return True
        return False
```

