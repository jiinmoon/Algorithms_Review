# 472 Concatenated Words

For each word, we create prefix and suffixes - to see whether prefix can exist
within the words as well as recursively same on suffixes.

---

Python:

```python

from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        @lru_cache(None)
        def isConcatenated(word):
            if not word or word in words:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and isConcatenated(suffix):
                    return True
            return False

        words = set(words)
        res = list()

        for word in words:
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and isConcatenated(suffix):
                    res.append(word)
                    break

        return res
```
