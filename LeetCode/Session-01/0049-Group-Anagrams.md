# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

---

We can group the anagrams by using hashmap data structure where we store the
sorted string to list of words belong under same anagram. This requires O(n) in
space but we can complete the algorithm in linear time.

---

Python:

```python

from collections import defaultdict

class Solution49:

    def groupAnagrams(self, strs):

        d = defaultdict(list)

        for s in strs:
            d[tuple(sorted(s))].append(s)

        return d.values()
```
