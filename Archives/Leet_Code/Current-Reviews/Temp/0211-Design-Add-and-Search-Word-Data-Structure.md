# 211. Design Add and Search Word Data Structure

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

#### (1) Trie.

Using Trie structure, we can store every character of the word in a tree
fashion. Due to '.' wild card charcter, we have to potentially search the
entire tree. Thus, time complexity on search would be linear. As for searching,
we may use any traversal algorithm such as BFS or DFS.

#### (2) Store by length.

We may also use hashmap to store the list of words that share the same length.
Time complexity analysis is interesting one - but in general, depends upon the
average length of the words stored. Unintuitively, this appears to perform
superior compared to Trie approach on testing.

---

Python: Store by length.

```python

from collections import defaultdict

class Solution211:

    def __init__(self):

        self.d = defaultdict(list)


    def addWord(self, word):
        
        self.d[len(word)].append(word)


    def searchWord(self, word):

        for c1, c2 in zip(word, self.d[len(word)]):
            if c1 != '.' and c1 != c2:
                break
        else:
            return True

        return False

```

Python: Trie.

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


    def searchWord(self, word):

        queue = [self.root]

        for char in word:
            
            temp = list()

            for node in queue:
                
                if char == '.':
                    temp += list(node.children.values())
                elif char in node.children:
                    temp.append(node.children[char])

            queue = temp

        return any(node.isWord for node in queue)

```
