# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

---

We can group the anagrams together by its alphanumerically sorted string. For
every sorted string of the given string, we create a list of words that share
the same anagrams. Ideal container or data structure for this would be hashmap
where we can store and retrieve the key-value pairs in constant time.

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
