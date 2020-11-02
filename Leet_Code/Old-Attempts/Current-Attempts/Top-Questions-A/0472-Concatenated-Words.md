# 472 Concatenated Words

Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

---

To determine whether one of word is decomposable into other words; we consider
every prefix and suffix; and we recursively check for suffix again until the
end or the current word is found within the list of words.

---

Python:

```python

from functools import lru_cache

class Solution:
    def findConcatenatedWords(self, words):
        @lru_cahce(None)
        def helper(word):
            if not word or word in words:
                return True
            for i in range(1, len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and helper(suffix):
                    return True
            return False

        words = set(words)
        res = list()
        for word in words:
            for i in range(1, len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and helper(suffix):
                    res.append(word)
                    break

        return res
```
