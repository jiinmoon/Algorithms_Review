# 211 Design Add and Search Words Data Structure

Use Trie structure for efficient search. This is hampered by having to
recursively searching all paths downwards when we encounter ".".

Alternatively, we can use the length of the words with the hashmap structure.

---

Python:

```python

class WordDictionary:
    def __init__(self):
        self.words = collections.defaultdict(list)

    def addWord(self, word):
        self.words[len(word)].append(word)

    def search(self, word):
        for w in self.words[len(word)]:
            for i, char in enumerate(w):
                if word[i] != '.' and word[i] != c:
                    break
            else:
                return True
        return False
```
