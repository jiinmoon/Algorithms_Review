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

To implement this structure, we can approach in two ways - one is using Trie
and other is hashmap by length of the given word. Both approach has its cons
and pros. The later approach will be constant in adding a new word, but will
require a linear search that is based on the count of the words inserted with
matching the count of the word.

---

Python:

```python

class WordDictionary:
    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word):
        self.d[len(word)].append(word)

    def search(self, word):
        for target in self.d[len(word)]:
            for i, char in enumerate(target):
                if word[i] != "." and word[i] != char:
                    break
            else:
                return True
        return False
```
