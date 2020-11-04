# 953. Verifying Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.

---

From given "order" of characters, we can create its character to index mapping.
Thus, for each word that we examine, we create a mapping based on above
criteria - end result will be a list of indicies. Overall, all this resulting
lists should be in lexcographically sorted order. Since for each word, we need
to iterate on the word, the time complexity should be O(k * n) where k is the
length of the word and n is the number of words given.

---

Python:

```python

class Solution:
    def isAlienSorted(self, words, order):
        order = {i:char for i, char in enumerate(order)}
        prevMapping = list()
        for word in words:
            currMapping = [order[char] for char in word]
            if prevMapping >= currMapping:
                return False
            prevMapping = currMapping
        return True
```
