# 953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.

---

We can compare every words pair-wise while converting them into the alien
ordered words. It would be O(n) in time complexity, and O(1) in space
complexity.

---

Python:

```python

class Solution953:

    def isAlienSorted(self, words, order):

        order = { char: i for i, char in enumerate(order) }
        prev = []

        for word in words:
            curr = [order[char] for char in word]
            if prev > curr:
                return False
            prev = curr

        return True

```
