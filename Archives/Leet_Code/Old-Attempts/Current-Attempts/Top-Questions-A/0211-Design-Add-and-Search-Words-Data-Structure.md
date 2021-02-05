# 211 Design Add and Search Words Data Structure

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

There are two approaches: first, we could implement this with Trie structure or
we use hashmap with length of the word as the key.

Trie structure is a bit more complex in that we need to implement recursive
search to take account for the "." to match any letter.

Another approach is simpler in that we require a hashmap of length of words to
list of words that fit. So, the search involves first retrieving the list of
words matching the length of search word. Then, for each word, we scan forward;
if no exceptional case is found (either current char has to be "." or matches
the search word char).

---

Python:

```python

class WordDictionary:
    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word):
        if word not in self.d:
            self.d[len(word)].append(word)

    def search(self, searchWord):
        for word in self.d[searchWord]:
            for i, char in enumerate(word):
                if char != "." or char != searchWord[i]:
                    break
            else:
                return True
        return False
```
