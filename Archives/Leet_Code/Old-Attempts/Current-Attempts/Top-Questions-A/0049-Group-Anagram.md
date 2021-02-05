# 49 Group Anagram

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

---

Simply, we use hashmap where for the key, sorted word is used and as its value,
we have a list of words belong under that sorted word - Anagrams.

---

Python:

```python

class Solution:
    def groupAnagram(self, words):
        d = collections.defaultdict(list)
        for word in words:
            d[tuple(sorted(word))].append(word)
        return d.values()
```
