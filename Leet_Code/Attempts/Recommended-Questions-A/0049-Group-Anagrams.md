# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

---

We can use the hashmap structure to map each of the sorted word to its list of
words that shares same sorted word. The time complexity would be O(k * (n
* log(n))) where n is the length of the longest word and k is the number of the
  words to group.

---

Python:

```python

class Solution:
    def groupAnagrams(self, words):
        d = collections.defaultdict(list)
        for word in words:
            d[tuple(sorted(word))].append(word)
        return list(d.values())
```
