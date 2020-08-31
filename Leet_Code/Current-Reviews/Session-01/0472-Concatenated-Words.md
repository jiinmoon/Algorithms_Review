472 Concatenated Words
======================

Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

---

Here, we check for two conditions: whether a given word's prefix exists in the
initial given words list, AND whether its suffix is also comprised of prefixes
that are within the words list.

Time complexity of the problem would be O(n * k ** 2) where k is the max length
of the word since we will have to exaimne the word to generate the prefixes.

---

Python:

```python
class Solution:
    def findAllConcatenatedWordsInDict(self, words):
        wordSet = set(words)
        res = list()

        def isComposite(wordFragment):
            if not wordFragment or wordFragment in wordSet:
                return True

            for i in range(1, len(wordFragment)+1):
                prefix = wordFragment[i:]
                suffix = wordFragment[:i]
                if prefix in wordSet and isComposite(prefix):
                    return True
            return False

        for word in words:
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and isComposite(suffix):
                    res.append(word)
                    break
        return res
```
