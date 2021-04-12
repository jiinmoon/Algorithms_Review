# 211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

```
WordDictionary() Initializes the object.

void addWord(word) Adds word to the data structure, it can be matched later.

bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.' where dots can
be matched with any letter.
```
---

There are several approaches to this problem. One typical solution would be to
use Trie-structure. Each Trie Node stores a value (character), a hashmap of its
children to lead to next, and a flag to denote that current node marks as
a complete word. Since there is a wild character '.' to match, the search
algorithm would be exhaustive whenever we encounter '.' as we have to search
entire children.

Another solution would be to instead use the length of the words as our key
instead. This may or may not improve the time complexity as comparable to the
Trie approach, but if we have some idea about the data beforehand, this could
be a worthy solution to consider.

---

Python: Trie approach.

```python

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isWord = False


class Solution211:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.isWord = True

    def search(self, word):
        queue = [self.root]
        for char in word:
            temp = []
            for node in queue:
                if char == '.':
                    temp += node.children.values()
                elif char in node.children:
                    temp.append(node.children[char])
            if not temp:
                return False
            queue = temp

        return any(node.isWord for node in queue)
```
