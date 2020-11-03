# 472. Concatenated Words

Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

---

We first breakdown the given word at all possible points to generate prefix and
suffixes. For each suffixes, we recursive check for whether the suffixes
themselves are composed of the concatenated words. Since there composition of
word is fixed, we can use memoization to save work.

---

Python:

```python

from functools import lru_cache

class Solution:
    def concatenatedWords(self, words):
        @lru_cache(None)
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
        result = list()
        for word in words:
            for i in range(1, len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and helper(suffix):
                    result.append(word)
                    break

        return result
```
